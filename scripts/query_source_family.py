#!/usr/bin/env python3
"""List one document family from source metadata.

This does not infer missing stages. Live links are shown on the member that
records them.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from query_source_history import load_records, orient


def family_report(records: dict[str, dict], family_id: str) -> dict:
    members = sorted(
        cid for cid, meta in records.items() if meta.get("document_family_id") == family_id
    )
    rows = [orient(records, cid) for cid in members]
    return {
        "document_family_id": family_id,
        "found": bool(members),
        "member_count": len(members),
        "members": [
            {
                "corpus_id": row["corpus_id"],
                "title": row.get("title"),
                "project": [item.get("project_id") for item in row.get("project") or []],
                "project_unresolved": row.get("project_unresolved"),
                "production_stages": [item.get("stage") for item in row.get("production_stages") or []],
                "production_stage_unresolved": row.get("production_stage_unresolved"),
                "came_before": row.get("came_before"),
                "came_after": row.get("came_after"),
                "revision_context": row.get("revision_context"),
                "publication": row.get("publication"),
                "live_contact": row.get("live_contact"),
                "live_use_unresolved": row.get("live_use_unresolved"),
            }
            for row in rows
        ],
    }


def render_text(report: dict) -> str:
    if not report["found"]:
        return f"{report['document_family_id']}: no source uses this family id\n"
    lines = [f"{report['document_family_id']} ({report['member_count']} members)"]
    for row in report["members"]:
        project = ", ".join(row["project"]) or ("unresolved" if row["project_unresolved"] else "unrecorded")
        stages = ", ".join(s for s in row["production_stages"] if s) or (
            "unresolved" if row["production_stage_unresolved"] else "unrecorded"
        )
        lines.append(f"{row['corpus_id']}: {row['title']}")
        lines.append(f"  project: {project}")
        lines.append(f"  stage: {stages}")
        for label in ("came_before", "came_after", "revision_context", "publication", "live_contact"):
            links = row[label] or []
            if not links:
                continue
            bits = []
            for link in links:
                if link.get("direction") == "incoming":
                    target = link.get("owner")
                else:
                    target = link.get("to_corpus_id") or link.get("external_locator")
                bits.append(f"{link.get('direction')} {link.get('link_type')} {target}")
            rendered = ", ".join(bits)
            lines.append(f"  {label}: {rendered}")
        if row["live_use_unresolved"] and not row["live_contact"]:
            lines.append("  live use: not established")
    if not any(row["live_contact"] for row in report["members"]):
        lines.append("No member records a live-contact link.")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read one recorded source family.")
    parser.add_argument("family_id")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    records = load_records(Path(args.repo).resolve())
    report = family_report(records, args.family_id)
    if args.json:
        json.dump(report, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(render_text(report))
    if report["found"]:
        return 0
    known = sorted({meta.get("document_family_id") for meta in records.values() if meta.get("document_family_id")})
    print("Known families:", file=sys.stderr)
    for name in known:
        print(f"  {name}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
