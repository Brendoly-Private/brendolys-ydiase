#!/usr/bin/env python3
"""Validate the YDIASE machine-readable knowledge catalog.

K2 validator: structural checks only. It never invents missing entities.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ID_RE = re.compile(r"^YD-[A-Z0-9-]+$")
REFERENCE_KEYS = {
    "domain", "system", "producer", "owner", "contract", "from", "to",
    "logicalServices", "consumers", "consumesFrom", "consumesEvents",
    "verifiedBy", "affectedComponents", "systems", "capabilities",
}


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def collect_ids(value: Any, ids: dict[str, Path], duplicates: list[str], path: Path) -> None:
    if isinstance(value, dict):
        metadata = value.get("metadata")
        if isinstance(metadata, dict):
            entity_id = metadata.get("id")
            if isinstance(entity_id, str) and ID_RE.match(entity_id):
                if entity_id in ids and ids[entity_id] != path:
                    duplicates.append(f"{entity_id}: {ids[entity_id]} <> {path}")
                else:
                    ids[entity_id] = path
        for child in value.values():
            collect_ids(child, ids, duplicates, path)
    elif isinstance(value, list):
        for child in value:
            collect_ids(child, ids, duplicates, path)


def collect_references(value: Any, refs: list[tuple[str, str, Path]], path: Path, key: str | None = None) -> None:
    if isinstance(value, dict):
        for child_key, child in value.items():
            collect_references(child, refs, path, child_key)
    elif isinstance(value, list):
        for child in value:
            collect_references(child, refs, path, key)
    elif key in REFERENCE_KEYS and isinstance(value, str) and ID_RE.match(value):
        refs.append((key or "", value, path))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default="documentations/_knowledge")
    parser.add_argument("--strict", action="store_true", help="fail on unresolved references")
    args = parser.parse_args()

    root = Path(args.root)
    yaml_files = sorted(root.rglob("*.yaml"))
    ids: dict[str, Path] = {}
    duplicates: list[str] = []
    refs: list[tuple[str, str, Path]] = []
    parse_errors: list[str] = []

    documents: list[tuple[Path, Any]] = []
    for path in yaml_files:
        try:
            document = load_yaml(path)
            documents.append((path, document))
            collect_ids(document, ids, duplicates, path)
        except Exception as exc:
            parse_errors.append(f"{path}: {exc}")

    for path, document in documents:
        collect_references(document, refs, path)

    relation_file = root / "ontology" / "RELATION_TYPES.yaml"
    allowed_relations: set[str] = set()
    if relation_file.exists():
        relation_doc = load_yaml(relation_file) or {}
        for relation in relation_doc.get("spec", {}).get("relations", []):
            if isinstance(relation, dict) and relation.get("id"):
                allowed_relations.add(relation["id"])

    invalid_relations: list[str] = []
    for path, document in documents:
        if isinstance(document, dict) and document.get("kind") == "RelationSet":
            for relation in document.get("spec", {}).get("relations", []):
                relation_type = relation.get("type") if isinstance(relation, dict) else None
                if relation_type and relation_type not in allowed_relations:
                    invalid_relations.append(f"{path}: {relation_type}")

    unresolved = sorted({(key, ref, str(path)) for key, ref, path in refs if ref not in ids})

    print(f"YAML files: {len(yaml_files)}")
    print(f"Registered IDs: {len(ids)}")
    print(f"References: {len(refs)}")
    print(f"Parse errors: {len(parse_errors)}")
    print(f"Duplicate IDs: {len(duplicates)}")
    print(f"Invalid relation types: {len(invalid_relations)}")
    print(f"Unresolved references: {len(unresolved)}")

    for title, errors in (
        ("PARSE", parse_errors),
        ("DUPLICATE", duplicates),
        ("RELATION", invalid_relations),
    ):
        for error in errors:
            print(f"[{title}] {error}")
    for key, ref, path in unresolved:
        print(f"[UNRESOLVED] {ref} via {key} in {path}")

    hard_failure = bool(parse_errors or duplicates or invalid_relations)
    if args.strict and unresolved:
        hard_failure = True
    return 1 if hard_failure else 0


if __name__ == "__main__":
    sys.exit(main())
