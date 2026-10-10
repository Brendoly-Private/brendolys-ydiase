#!/usr/bin/env python3
"""Generate a transitive impact view from YDIASE RelationSet YAML files."""
from __future__ import annotations

import argparse
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

import yaml


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("entity_id")
    parser.add_argument("--root", default="documentations/_meta")
    parser.add_argument("--max-depth", type=int, default=6)
    args = parser.parse_args()

    root = Path(args.root)
    graph: dict[str, list[tuple[str, str, str]]] = defaultdict(list)

    for path in sorted((root / "relations").rglob("*.yaml")):
        with path.open("r", encoding="utf-8") as handle:
            content = handle.read()
        # RelationSet files contain a documentary preamble before the YAML payload.
        marker = "apiVersion: knowledge.ydiase/v1"
        lines = content.splitlines(keepends=True)
        offset = 0
        for line in lines:
            if line.strip() == marker:
                content = content[offset:]
                break
            offset += len(line)
        doc: Any = yaml.safe_load(content) or {}
        if doc.get("kind") != "RelationSet":
            continue
        for rel in doc.get("spec", {}).get("relations", []):
            if not isinstance(rel, dict):
                continue
            source, relation_type, target = rel.get("from"), rel.get("type"), rel.get("to")
            if source and relation_type and target:
                graph[source].append((relation_type, target, str(path)))

    queue = deque([(args.entity_id, 0)])
    visited = {args.entity_id}
    rows: list[tuple[int, str, str, str, str]] = []

    while queue:
        source, depth = queue.popleft()
        if depth >= args.max_depth:
            continue
        for relation_type, target, origin in sorted(graph.get(source, [])):
            rows.append((depth + 1, source, relation_type, target, origin))
            if target not in visited:
                visited.add(target)
                queue.append((target, depth + 1))

    print(f"# Impact graph: {args.entity_id}\n")
    print("| Depth | From | Relation | To | Source |")
    print("|---:|---|---|---|---|")
    for depth, source, relation_type, target, origin in rows:
        print(f"| {depth} | `{source}` | `{relation_type}` | `{target}` | `{origin}` |")
    print(f"\nReachable entities: {max(0, len(visited) - 1)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
