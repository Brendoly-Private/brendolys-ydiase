#!/usr/bin/env python3
"""Validate the YDIASE machine-readable knowledge catalog.

K2 compiler gate. It reports migration debt separately from semantic errors and
never creates missing knowledge entities.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

ID_RE = re.compile(r"^YD-[A-Z0-9-]+$")
PREFIX_BY_KIND = {
    "Domain": "YD-DOM-",
    "System": "YD-SYS-",
    "Microservice": "YD-MS-",
    "API": "YD-API-",
    "Event": "YD-EVT-",
    "ADR": "YD-ADR-",
    "Requirement": "YD-REQ-",
    "RelationSet": "YD-RELSET-",
    "EventCatalog": "YD-EVTCAT-",
    "RequirementCatalog": "YD-REQCAT-",
}
REFERENCE_KEYS = {
    "domain", "system", "producer", "publisher", "provider", "owner", "authority",
    "contract", "from", "to", "logicalServices", "consumers", "consumesFrom",
    "consumesEvents", "subscribesTo", "publishes", "verifiedBy", "affectedComponents",
    "affectedEntities", "systems", "capabilities", "dependsOn", "supersedes", "supersededBy",
}
AUTHORITIES = {"AUTH", "MIXED", "DERIVED"}


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def iter_entities(document: Any):
    """Yield top-level and catalog-embedded YD entities."""
    if not isinstance(document, dict):
        return
    metadata = document.get("metadata")
    if isinstance(metadata, dict) and isinstance(metadata.get("id"), str):
        yield metadata["id"], document.get("kind"), document
    spec = document.get("spec", {})
    if document.get("kind") == "EventCatalog":
        for item in spec.get("events", []):
            if isinstance(item, dict) and isinstance(item.get("id"), str):
                yield item["id"], "Event", item
    if document.get("kind") == "RequirementCatalog":
        for item in spec.get("requirements", []):
            if isinstance(item, dict) and isinstance(item.get("id"), str):
                yield item["id"], "Requirement", item


def collect_references(value: Any, refs: list[tuple[str, str, Path]], path: Path, key: str | None = None) -> None:
    if isinstance(value, dict):
        for child_key, child in value.items():
            collect_references(child, refs, path, child_key)
    elif isinstance(value, list):
        for child in value:
            collect_references(child, refs, path, key)
    elif key in REFERENCE_KEYS and isinstance(value, str) and ID_RE.match(value):
        refs.append((key or "", value, path))


def normalize_event(entity: dict[str, Any]) -> tuple[str | None, list[str]]:
    spec = entity.get("spec") if isinstance(entity.get("spec"), dict) else entity
    producer = spec.get("producer") or spec.get("publisher")
    consumers = spec.get("consumers") or spec.get("subscribers") or []
    return producer, [v for v in consumers if isinstance(v, str)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default="documentations/_knowledge")
    parser.add_argument("--strict", action="store_true", help="fail on unresolved migration references")
    parser.add_argument("--json", dest="json_path", help="write a machine-readable report")
    args = parser.parse_args()

    root = Path(args.root)
    yaml_files = sorted(root.rglob("*.yaml"))
    documents: list[tuple[Path, Any]] = []
    parse_errors: list[str] = []
    ids: dict[str, tuple[str | None, Path, dict[str, Any]]] = {}
    duplicates: list[str] = []
    prefix_errors: list[str] = []
    refs: list[tuple[str, str, Path]] = []

    for path in yaml_files:
        try:
            document = load_yaml(path)
            documents.append((path, document))
        except Exception as exc:
            parse_errors.append(f"{path}: {exc}")
            continue
        for entity_id, kind, entity in iter_entities(document):
            if not ID_RE.match(entity_id):
                prefix_errors.append(f"{path}: invalid YD id {entity_id}")
                continue
            if entity_id in ids:
                duplicates.append(f"{entity_id}: {ids[entity_id][1]} <> {path}")
            else:
                ids[entity_id] = (kind, path, entity)
            expected = PREFIX_BY_KIND.get(kind or "")
            if expected and not entity_id.startswith(expected):
                prefix_errors.append(f"{path}: {entity_id} must start with {expected}")
        collect_references(document, refs, path)

    relation_doc = load_yaml(root / "ontology" / "RELATION_TYPES.yaml") or {}
    allowed_relations = {
        item.get("id") for item in relation_doc.get("spec", {}).get("relations", [])
        if isinstance(item, dict) and item.get("id")
    }
    invalid_relations: list[str] = []
    relation_edges: list[tuple[str, str, str, Path]] = []
    for path, document in documents:
        if not isinstance(document, dict) or document.get("kind") != "RelationSet":
            continue
        for relation in document.get("spec", {}).get("relations", []):
            if not isinstance(relation, dict):
                continue
            source, relation_type, target = relation.get("from"), relation.get("type"), relation.get("to")
            if relation_type and relation_type not in allowed_relations:
                invalid_relations.append(f"{path}: {relation_type}")
            if source and relation_type and target:
                relation_edges.append((source, relation_type, target, path))

    unresolved = sorted({(key, ref, str(path)) for key, ref, path in refs if ref not in ids})

    ownership: dict[str, list[str]] = defaultdict(list)
    authority_errors: list[str] = []
    for entity_id, (kind, path, entity) in ids.items():
        if kind != "Microservice":
            continue
        spec = entity.get("spec", {}) if isinstance(entity.get("spec"), dict) else {}
        authority = spec.get("authority")
        if authority is not None and authority not in AUTHORITIES:
            authority_errors.append(f"{path}: invalid authority {authority}")
        for aggregate in spec.get("owns", []) or []:
            if isinstance(aggregate, str):
                ownership[aggregate].append(entity_id)
    ownership_conflicts = [
        f"{aggregate}: {', '.join(sorted(owners))}"
        for aggregate, owners in sorted(ownership.items()) if len(set(owners)) > 1
    ]

    event_errors: list[str] = []
    relations = {(a, b, c) for a, b, c, _ in relation_edges}
    for event_id, (kind, path, entity) in ids.items():
        if kind != "Event":
            continue
        producer, consumers = normalize_event(entity)
        if not producer:
            event_errors.append(f"{event_id}: no producer")
        elif producer in ids and ids[producer][0] != "Microservice":
            event_errors.append(f"{event_id}: producer {producer} is not a Microservice")
        if producer and producer in ids and (producer, "publishes", event_id) not in relations:
            event_errors.append(f"{event_id}: missing publishes relation from {producer}")
        for consumer in consumers:
            if consumer in ids and ids[consumer][0] == "Microservice" and (consumer, "subscribesTo", event_id) not in relations:
                event_errors.append(f"{event_id}: missing subscribesTo relation from {consumer}")

    hard_errors = parse_errors + duplicates + prefix_errors + invalid_relations + authority_errors + ownership_conflicts + event_errors
    report = {
        "summary": {
            "yamlFiles": len(yaml_files),
            "registeredIds": len(ids),
            "references": len(refs),
            "hardErrors": len(hard_errors),
            "unresolvedReferences": len(unresolved),
        },
        "errors": {
            "parse": parse_errors,
            "duplicateIds": duplicates,
            "idPrefixes": prefix_errors,
            "relationTypes": invalid_relations,
            "authority": authority_errors,
            "ownership": ownership_conflicts,
            "events": event_errors,
        },
        "migrationDebt": [
            {"key": key, "reference": ref, "path": path} for key, ref, path in unresolved
        ],
    }

    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    for category, errors in report["errors"].items():
        for error in errors:
            print(f"[{category.upper()}] {error}")
    for item in report["migrationDebt"]:
        print(f"[UNRESOLVED] {item['reference']} via {item['key']} in {item['path']}")

    if args.json_path:
        output = Path(args.json_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return 1 if hard_errors or (args.strict and unresolved) else 0


if __name__ == "__main__":
    sys.exit(main())
