#!/usr/bin/env python3
"""Audit documentaire non destructif : chemins, identifiants et métadonnées."""
from collections import defaultdict
from pathlib import Path
import csv
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "documentations"
MATRIX = DOCS / "00-foundation/governance/registers/DOCUMENT_METADATA_MIGRATION_MATRIX.tsv"
FIELDS = ("document_id", "title", "document_type", "institutional_reference", "created_at", "last_reviewed_at")
errors = []
warnings = []
seen = defaultdict(list)

def audit_file(path):
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---\n"):
        errors.append(f"{rel}: frontmatter YAML absent")
        return
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.S)
    if not match:
        errors.append(f"{rel}: frontmatter YAML non fermé")
        return
    meta = {}
    for line in match.group(1).splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip().strip('"\'')
    for field in FIELDS:
        if not meta.get(field) or meta[field].lower() in ("null", "none", "todo", "tbd", "placeholder"):
            errors.append(f"{rel}: {field} manquant ou placeholder")
    if meta.get("document_id"):
        seen[meta["document_id"]].append(rel)
    for field in ("created_at", "last_reviewed_at"):
        if meta.get(field) and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", meta[field]):
            errors.append(f"{rel}: {field} doit être YYYY-MM-DD")

def main():
    if not MATRIX.exists():
        sys.exit(f"Matrice introuvable : {MATRIX}")
    rows = []
    for line in MATRIX.read_text(encoding="utf-8-sig").splitlines():
        if re.match(r"^\d+\t", line):
            cells = line.split("\t")
            if len(cells) < 6:
                errors.append(f"Ligne de matrice incomplète : {line[:90]}")
            else:
                rows.append(cells)
    paths = defaultdict(list)
    for row in rows:
        paths[row[1]].append(row[0])
        if not (ROOT / row[1]).is_file():
            errors.append(f"Matrice : fichier absent {row[1]}")
    for p, indices in paths.items():
        if len(indices) > 1:
            errors.append(f"Matrice : chemin dupliqué {p} (lignes {','.join(indices)})")
    if len(rows) != 415:
        errors.append(f"Matrice : {len(rows)} entrées, 415 attendues")
    for path in sorted(DOCS.rglob("*.md")):
        audit_file(path)
    for ident, files in seen.items():
        if len(files) > 1:
            errors.append(f"document_id dupliqué {ident}: {', '.join(files)}")
    print(f"Matrice : {len(rows)} entrées ; Markdown : {sum(1 for _ in DOCS.rglob('*.md'))} ; IDs uniques : {len(seen)}")
    for item in errors:
        print("ERROR:", item)
    for item in warnings:
        print("WARN:", item)
    print(f"Résultat : {len(errors)} erreur(s), {len(warnings)} avertissement(s)")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
