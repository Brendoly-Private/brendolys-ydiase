#!/usr/bin/env python3
"""Audit documentaire non destructif : chemins, identifiants et métadonnées."""
from collections import defaultdict, Counter
from pathlib import Path
import csv
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "documentations"
MATRIX = DOCS / "00-foundation/governance/registers/DOCUMENT_METADATA_MIGRATION_MATRIX.tsv"
FIELDS = ("document_id", "title", "document_type", "institutional_reference", "created_at", "last_reviewed_at")
SEMANTIC_FIELDS = ("document_role", "product", "status", "authority_level", "canonical", "development_usage")
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
    for field in SEMANTIC_FIELDS:
        if not meta.get(field):
            warnings.append(f"{rel}: {field} à qualifier selon le standard officiel")
    if meta.get("document_id"):
        seen[meta["document_id"]].append(rel)
    if meta.get("institutional_reference") and meta["institutional_reference"] != "YDIASE-INSTITUTIONAL-IDENTITY":
        errors.append(f"{rel}: institutional_reference invalide")
    if meta.get("product") and meta["product"] != "BRENDOLYS YDIASE":
        errors.append(f"{rel}: product invalide")
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
    compliance = Counter(row[5].strip() for row in rows)
    for status, count in sorted(compliance.items()):
        print(f"Matrice statut {status}: {count}")
    if compliance.get("MIGRATED-CONFORMING", 0):
        warnings.append("Matrice : MIGRATED-CONFORMING est déclaré avant validation des champs sémantiques ; conformité complète non démontrée")
    for row in rows:
        relpath = row[1]
        if not relpath.endswith(".md"):
            continue
        p = ROOT / relpath
        if not p.is_file():
            continue
        raw = p.read_text(encoding="utf-8-sig")
        fm = re.match(r"\\A---\\n(.*?)\\n---(?:\\n|\\Z)", raw, re.S)
        if not fm:
            continue
        meta = dict((m.group(1), m.group(2).strip().strip('"\\\'')) for line in fm.group(1).splitlines() if (m := re.match(r"^([A-Za-z_][\\w-]*):\\s*(.*)$", line)))
        for field, expected in (("authority_level", row[3].strip()), ("development_usage", row[4].strip())):
            actual = meta.get(field)
            if actual and actual != expected:
                warnings.append(f"{relpath}: matrice {field}={expected}, document={actual}")
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
    print(f"REVIEW_PENDING: {len(warnings)} avertissement(s) de gouvernance à qualifier")
    print(f"Résultat : {len(errors)} erreur(s), {len(warnings)} avertissement(s)")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
