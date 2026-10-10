#!/usr/bin/env python3
"""Validate the YDIASE machine-readable knowledge catalog."""
from __future__ import annotations
import argparse, json, re, sys
from collections import defaultdict
from pathlib import Path
from typing import Any
import yaml
from jsonschema import Draft202012Validator, RefResolver
from maturity import calculate_knowledge, calculate_evidence

ID_RE = re.compile(r"^YD-[A-Z0-9-]+$")
PREFIX_BY_KIND = {"Domain":"YD-DOM-","System":"YD-SYS-","Microservice":"YD-MS-","API":"YD-API-","Event":"YD-EVT-","ADR":"YD-ADR-","Requirement":"YD-REQ-","RelationSet":"YD-RELSET-","EventCatalog":"YD-EVTCAT-","RequirementCatalog":"YD-REQCAT-"}
SCHEMA_BY_KIND = {"Domain":"domain.schema.yaml","System":"system.schema.yaml","Microservice":"microservice.schema.yaml","API":"api.schema.yaml","Event":"event.schema.yaml","ADR":"decision.schema.yaml"}
REFERENCE_KEYS = {"domain","system","producer","publisher","provider","owner","authority","contract","from","to","logicalServices","consumers","consumesFrom","consumesEvents","subscribesTo","publishes","verifiedBy","affectedComponents","affectedEntities","affects","systems","capabilities","dependsOn","supersedes","supersededBy"}
AUTHORITIES={"AUTH","MIXED","DERIVED"}

def load_yaml(path:Path)->Any:
    with path.open("r",encoding="utf-8") as h:
        source = h.read()
    # Some catalog YAML files contain a documentation front matter and a
    # human-readable role preamble before their machine-readable payload.
    # Preserve the files and parse the actual catalog beginning at apiVersion.
    # Embedded catalog and JSON Schema documents follow a governance preamble.
    # Anchor at their actual top-level payload key, not the front matter.
    lines = source.splitlines(keepends=True)
    payload_keys = ("apiVersion: knowledge.ydiase/v1", "$schema:", "$id:")
    offset = 0
    for line in lines:
        if any(line.startswith(key) for key in payload_keys):
            source = source[offset:]
            break
        offset += len(line)
    return yaml.safe_load(source)

def iter_entities(document:Any):
    if not isinstance(document,dict):return
    md=document.get("metadata")
    if isinstance(md,dict) and isinstance(md.get("id"),str):yield md["id"],document.get("kind"),document,True
    spec=document.get("spec",{})
    if document.get("kind")=="EventCatalog":
        for item in spec.get("events",[]):
            if isinstance(item,dict) and isinstance(item.get("id"),str):yield item["id"],"Event",item,False
    if document.get("kind")=="RequirementCatalog":
        for item in spec.get("requirements",[]):
            if isinstance(item,dict) and isinstance(item.get("id"),str):yield item["id"],"Requirement",item,False

def collect_references(value:Any,refs:list,path:Path,key:str|None=None)->None:
    if isinstance(value,dict):
        for k,v in value.items():collect_references(v,refs,path,k)
    elif isinstance(value,list):
        for v in value:collect_references(v,refs,path,key)
    elif key in REFERENCE_KEYS and isinstance(value,str) and ID_RE.match(value):refs.append((key or "",value,path))

def normalize_event(entity):
    spec=entity.get("spec") if isinstance(entity.get("spec"),dict) else entity
    return spec.get("producer") or spec.get("publisher"),[v for v in (spec.get("consumers") or spec.get("subscribers") or []) if isinstance(v,str)]

def schema_errors_for(path,document,schema_dir):
    if not isinstance(document,dict):return []
    name=SCHEMA_BY_KIND.get(document.get("kind"))
    if not name:return []
    sp=schema_dir/name
    if not sp.exists():return [f"{path}: schema missing for kind {document.get('kind')}: {sp}"]
    schema=load_yaml(sp);resolver=RefResolver(base_uri=sp.resolve().as_uri(),referrer=schema);validator=Draft202012Validator(schema,resolver=resolver)
    out=[]
    for e in sorted(validator.iter_errors(document),key=lambda x:list(x.absolute_path)):
        loc=".".join(str(v) for v in e.absolute_path) or "$";out.append(f"{path}: {loc}: {e.message}")
    return out

def lifecycle_maturity_errors(entity_id:str,entity:dict,path:Path)->list[str]:
    if entity.get("kind")!="Microservice":return []
    spec=entity.get("spec",{}) if isinstance(entity.get("spec"),dict) else {};lc=spec.get("lifecycle",{}) if isinstance(spec.get("lifecycle"),dict) else {}
    architecture=lc.get("architecture");implementation=lc.get("implementation");deployment=lc.get("deployment");errors=[]
    def need(field,condition=True):
        if condition and not spec.get(field):errors.append(f"{path}: {entity_id} maturity requires spec.{field}")
    if architecture in {"under-review","confirmed","superseded"}:
        need("domain");need("system");need("logicalServices");need("responsibility")
    if architecture=="confirmed":
        need("owns")
        if not spec.get("documentation",{}).get("root"):errors.append(f"{path}: {entity_id} confirmed architecture requires documentation.root")
    if implementation in {"planned","in-progress","implemented"}:
        if architecture!="confirmed":errors.append(f"{path}: {entity_id} implementation {implementation} requires architecture confirmed")
        need("domain");need("system")
    if deployment in {"development","staging","production"} and implementation not in {"in-progress","implemented"}:
        errors.append(f"{path}: {entity_id} deployment {deployment} requires implementation in-progress or implemented")
    if deployment=="production":
        if implementation!="implemented":errors.append(f"{path}: {entity_id} production requires implementation implemented")
        code=spec.get("code",{}) if isinstance(spec.get("code"),dict) else {}
        if code.get("status")!="present":errors.append(f"{path}: {entity_id} production requires code.status present")
        need("domain");need("system");need("logicalServices");need("owns")
    return errors

def assertion_evidence(entity:dict)->list[dict]:
    spec=entity.get("spec",{}) if isinstance(entity.get("spec"),dict) else {}
    values=spec.get("assertions",[])
    return [v for v in values if isinstance(v,dict)] if isinstance(values,list) else []

def main()->int:
    p=argparse.ArgumentParser();p.add_argument("root",nargs="?",default="documentations/_meta");p.add_argument("--strict",action="store_true");p.add_argument("--json",dest="json_path");p.add_argument("--no-schema",action="store_true");p.add_argument("--no-maturity",action="store_true");args=p.parse_args()
    root=Path(args.root);schema_dir=root/"schemas";yaml_files=sorted(root.rglob("*.yaml"));catalog_files=[x for x in yaml_files if "schemas" not in x.parts and "ontology" not in x.parts]
    documents=[];parse_errors=[];schema_errors=[];ids={};duplicates=[];prefix_errors=[];refs=[]
    for path in yaml_files:
        try:doc=load_yaml(path);documents.append((path,doc))
        except Exception as exc:parse_errors.append(f"{path}: {exc}");continue
        if not args.no_schema and path in catalog_files:
            try:schema_errors.extend(schema_errors_for(path,doc,schema_dir))
            except Exception as exc:schema_errors.append(f"{path}: schema validation infrastructure error: {exc}")
        for eid,kind,entity,_ in iter_entities(doc):
            if not ID_RE.match(eid):prefix_errors.append(f"{path}: invalid YD id {eid}");continue
            if eid in ids:duplicates.append(f"{eid}: {ids[eid][1]} <> {path}")
            else:ids[eid]=(kind,path,entity)
            expected=PREFIX_BY_KIND.get(kind or "")
            if expected and not eid.startswith(expected):prefix_errors.append(f"{path}: {eid} must start with {expected}")
        collect_references(doc,refs,path)
    relation_doc=load_yaml(root/"ontology"/"RELATION_TYPES.yaml") or {};allowed={i.get("id") for i in relation_doc.get("spec",{}).get("relations",[]) if isinstance(i,dict) and i.get("id")};invalid_relations=[];edges=[]
    for path,doc in documents:
        if not isinstance(doc,dict) or doc.get("kind")!="RelationSet":continue
        for r in doc.get("spec",{}).get("relations",[]):
            if not isinstance(r,dict):continue
            a,b,c=r.get("from"),r.get("type"),r.get("to")
            if b and b not in allowed:invalid_relations.append(f"{path}: {b}")
            if a and b and c:edges.append((a,b,c,path))
    unresolved=sorted({(k,r,str(path)) for k,r,path in refs if r not in ids});ownership=defaultdict(list);authority_errors=[];maturity_errors=[];knowledge_matrix=[];evidence_matrix=[]
    for eid,(kind,path,entity) in ids.items():
        if kind=="Microservice":
            spec=entity.get("spec",{}) if isinstance(entity.get("spec"),dict) else {};auth=spec.get("authority")
            if auth is not None and auth not in AUTHORITIES:authority_errors.append(f"{path}: invalid authority {auth}")
            for agg in spec.get("owns",[]) or []:
                if isinstance(agg,str):ownership[agg].append(eid)
            if not args.no_maturity:
                maturity_errors.extend(lifecycle_maturity_errors(eid,entity,path))
                kr=calculate_knowledge(entity);knowledge_matrix.append({"id":eid,"path":str(path),**kr})
                for error in kr.get("errors",[]):maturity_errors.append(f"{path}: {eid} {error}")
        if not args.no_maturity:
            for index,assertion in enumerate(assertion_evidence(entity)):
                er=calculate_evidence(assertion);evidence_matrix.append({"entityId":eid,"assertionIndex":index,"assertionId":assertion.get("id"),**er})
                for error in er.get("errors",[]):maturity_errors.append(f"{path}: {eid} assertion[{index}] {error}")
    ownership_conflicts=[f"{a}: {', '.join(sorted(o))}" for a,o in sorted(ownership.items()) if len(set(o))>1]
    event_errors=[];relations={(a,b,c) for a,b,c,_ in edges}
    for eid,(kind,path,entity) in ids.items():
        if kind!="Event":continue
        producer,consumers=normalize_event(entity)
        if not producer:event_errors.append(f"{eid}: no producer")
        elif producer in ids and ids[producer][0]!="Microservice":event_errors.append(f"{eid}: producer {producer} is not a Microservice")
        if producer and producer in ids and (producer,"publishes",eid) not in relations:event_errors.append(f"{eid}: missing publishes relation from {producer}")
        for consumer in consumers:
            if consumer in ids and ids[consumer][0]=="Microservice" and (consumer,"subscribesTo",eid) not in relations:event_errors.append(f"{eid}: missing subscribesTo relation from {consumer}")
    hard=parse_errors+schema_errors+duplicates+prefix_errors+invalid_relations+authority_errors+ownership_conflicts+event_errors+maturity_errors
    distribution=defaultdict(int)
    for item in knowledge_matrix:distribution[item.get("calculated") or "NONE"]+=1
    evidence_distribution=defaultdict(int)
    for item in evidence_matrix:evidence_distribution[item.get("calculated") or "E0"]+=1
    report={"summary":{"yamlFiles":len(yaml_files),"catalogFiles":len(catalog_files),"registeredIds":len(ids),"references":len(refs),"schemaErrors":len(schema_errors),"maturityErrors":len(maturity_errors),"hardErrors":len(hard),"unresolvedReferences":len(unresolved),"knowledgeEntities":len(knowledge_matrix),"evidenceAssertions":len(evidence_matrix)},"errors":{"parse":parse_errors,"schema":schema_errors,"duplicateIds":duplicates,"idPrefixes":prefix_errors,"relationTypes":invalid_relations,"authority":authority_errors,"ownership":ownership_conflicts,"events":event_errors,"maturity":maturity_errors},"maturity":{"knowledge":{"distribution":dict(sorted(distribution.items())),"entities":sorted(knowledge_matrix,key=lambda x:x["id"])},"evidence":{"distribution":dict(sorted(evidence_distribution.items())),"assertions":evidence_matrix}},"migrationDebt":[{"key":k,"reference":r,"path":path} for k,r,path in unresolved]}
    print(json.dumps(report["summary"],ensure_ascii=False,indent=2))
    if knowledge_matrix:
        print("Knowledge maturity:")
        for item in sorted(knowledge_matrix,key=lambda x:x["id"]):print(f"  {item['id']}: declared={item.get('declared') or '-'} calculated={item.get('calculated') or 'NONE'}")
    for cat,errs in report["errors"].items():
        for e in errs:print(f"[{cat.upper()}] {e}")
    for i in report["migrationDebt"]:print(f"[UNRESOLVED] {i['reference']} via {i['key']} in {i['path']}")
    if args.json_path:
        out=Path(args.json_path);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return 1 if hard or (args.strict and unresolved) else 0
if __name__=="__main__":sys.exit(main())
