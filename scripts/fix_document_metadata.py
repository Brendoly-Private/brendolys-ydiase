#!/usr/bin/env python3
"""Normalize documentation metadata without changing document bodies."""
from pathlib import Path
from datetime import date
import hashlib
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "documentations"
TODAY = date.today().isoformat()
REQUIRED = ("document_id", "title", "document_type", "institutional_reference", "created_at", "last_reviewed_at")
# Semantic governance fields require human review; do not fabricate their values.

def first_commit_date(path):
    result = subprocess.run(["git", "log", "--follow", "--diff-filter=A", "--format=%as", "--", str(path.relative_to(ROOT))],
                            cwd=ROOT, capture_output=True, text=True, check=False)
    dates = [s.strip() for s in result.stdout.splitlines() if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s.strip())]
    return dates[-1] if dates else TODAY

def matrix_entries():
    matrix = DOCS / "00-foundation/governance/registers/DOCUMENT_METADATA_MIGRATION_MATRIX.tsv"
    entries = {}
    for line in matrix.read_text(encoding="utf-8-sig").splitlines():
        if re.match(r"^\d+\t", line):
            cells = line.split("\t")
            if len(cells) >= 6:
                entries[cells[1]] = cells
    return entries

def normalize(path, entries):
    original = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", original, re.S)
    if match:
        front = match.group(1)
        body = original[match.end():]
    else:
        front = ""
        body = original
    present = set(re.findall(r"(?m)^([A-Za-z_][\w-]*):", front))
    rel = path.relative_to(DOCS).as_posix()
    stable_id = "YD-DOC-AUTO-" + hashlib.sha256(rel.encode()).hexdigest()[:16].upper()
    values = {
        "document_id": stable_id,
        "title": path.stem.replace("_", " ").replace('"', "'"),
        "document_type": "documentation-reference",
        "institutional_reference": "YDIASE-INSTITUTIONAL-IDENTITY",
        "created_at": first_commit_date(path),
        "last_reviewed_at": TODAY,
    }
    additions = [f'{key}: "{values[key]}"' for key in REQUIRED if key not in present]
    row = entries.get(path.relative_to(ROOT).as_posix())
    grounded = {"product": "BRENDOLYS YDIASE"}
    if row:
        grounded.update({"document_role": row[2], "authority_level": row[3],
                         "development_usage": row[4]})
    for key, value in grounded.items():
        if key not in present and value.strip():
            safe = value.replace('"', "'")
            additions.append(f'{key}: "{safe}"')
    if not additions:
        return False
    # last_reviewed_at records this automated metadata inspection, not business-content approval.
    if "last_reviewed_at" not in present:
        additions.append('review_scope: "metadata-only"')
    if match:
        updated = "---\n" + front.rstrip() + "\n" + "\n".join(additions) + "\n---\n" + body
    else:
        updated = "---\n" + "\n".join(additions) + "\n---\n\n" + body
    path.write_text(updated, encoding="utf-8")
    return True

def main():
    entries = matrix_entries()
    changed = [p for p in sorted(DOCS.rglob("*.md")) if normalize(p, entries)]
    print(f"Metadata normalized: {len(changed)} files")
    for p in changed:
        print(p.relative_to(ROOT))

if __name__ == "__main__":
    main()
