#!/usr/bin/env python3
"""Executable pre-implementation harness for YD-MS-KNW-001 K5 invariants."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

REQUIRED_FIELDS={"source_ref","source_version","relation_class","provenance","operation"}
ALLOWED_OPS={"UPSERT","DELETE","WITHDRAW","REVOKE"}
ALLOWED_CLASSES={"SOURCE-ASSERTED","DETERMINISTIC-DERIVED","INFERRED","CURATED-GRAPH"}

def validate_event(e):
    missing=sorted(k for k in REQUIRED_FIELDS if not e.get(k))
    if missing:return False,"missing:"+",".join(missing)
    if e["operation"] not in ALLOWED_OPS:return False,"invalid-operation"
    if e["relation_class"] not in ALLOWED_CLASSES:return False,"invalid-relation-class"
    if e.get("shared_graph") and e.get("contains_pii"):return False,"pii-default-deny"
    return True,"accepted"

def apply(state,e):
    ok,reason=validate_event(e)
    if not ok:return reason
    key=(e["source_ref"],e.get("relation_ref","default"))
    current=state.get(key)
    version=int(e["source_version"])
    if current and version < current["version"]:return "stale-ignored"
    if e["operation"] in {"DELETE","WITHDRAW","REVOKE"}:
        state.pop(key,None);return "removed"
    state[key]={"version":version,"class":e["relation_class"],"provenance":e["provenance"]}
    return "upserted"

def logical(state):
    return sorted((a,b,v["version"],v["class"],v["provenance"]) for (a,b),v in state.items())

def run():
    base=[
      {"source_ref":"SKL:1","source_version":"1","relation_ref":"r1","relation_class":"SOURCE-ASSERTED","provenance":"SKL:v1","operation":"UPSERT","shared_graph":True},
      {"source_ref":"EDU:1","source_version":"2","relation_ref":"r2","relation_class":"DETERMINISTIC-DERIVED","provenance":"EDU:v2","operation":"UPSERT","shared_graph":True},
    ]
    tests=[]
    s={}
    for e in base: apply(s,e)
    expected=logical(s)
    s2={}
    for e in base: apply(s2,e)
    tests.append(("full_rebuild_convergence",logical(s2)==expected))
    before=logical(s2)
    for e in base: apply(s2,e)
    tests.append(("replay_idempotence",logical(s2)==before))
    newer={**base[0],"source_version":"3","provenance":"SKL:v3"}
    older={**base[0],"source_version":"2","provenance":"SKL:v2"}
    apply(s2,newer);apply(s2,older)
    tests.append(("out_of_order_version",dict(s2[("SKL:1","r1")])["version"]==3))
    delete={**newer,"source_version":"4","operation":"REVOKE"}
    apply(s2,delete)
    tests.append(("revoke_propagation",("SKL:1","r1") not in s2))
    no_prov={**base[0],"provenance":""}
    tests.append(("provenance_required",validate_event(no_prov)[0] is False))
    pii={**base[0],"contains_pii":True}
    tests.append(("pii_default_deny",validate_event(pii)[0] is False))
    results=[{"test":n,"status":"PASS" if ok else "FAIL"} for n,ok in tests]
    return {"harness":"YD-MS-KNW-001-K5","scope":"logical-preimplementation","results":results,"passed":all(ok for _,ok in tests)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--json");args=ap.parse_args()
    report=run();print(json.dumps(report,indent=2))
    if args.json:
        p=Path(args.json);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    return 0 if report["passed"] else 1
if __name__=="__main__":sys.exit(main())
