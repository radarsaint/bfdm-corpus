#!/usr/bin/env python3
"""Show the current readiness labels, including why a thin edge still counts.

The label LONGITUDINAL_RESEARCH_READY means the family has at least one
recorded revision link or live-contact link. It does not mean every stage
of that history is present.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from validate_source_history import load_jsonl, metadata_records, readiness


def report(repo: Path) -> dict:
    records = metadata_records(repo)
    catalog = {row["corpus_id"]: row for row in load_jsonl(repo / "evidence" / "catalog.jsonl")}
    return readiness(repo, records, catalog)


def render_text(payload: dict, rows: list[dict]) -> str:
    lines = [
        "LONGITUDINAL_RESEARCH_READY means one recorded revision or live-contact link.",
        "A publication link, a companion, or an explicit live-use gap does not qualify.",
        "REVISION_CONTEXT_FOR_SOURCE_FAMILY is not counted as that revision link.",
        f"{len(rows)} families shown",
    ]
    for row in rows:
        lines.append(
            f"{row['document_family_id']}: {row['status']} / {row['longitudinal_status']} / {row['trajectory']}"
        )
        lines.append("  members: " + ", ".join(row["members"]))
        if row.get("revision_link_types"):
            lines.append("  revision edges: " + ", ".join(row["revision_link_types"]))
        if row.get("live_link_types"):
            lines.append("  live edges: " + ", ".join(row["live_link_types"]))
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read family readiness labels from metadata.")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--longitudinal-gap", action="store_true")
    parser.add_argument("--longitudinal-ready", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    payload = report(Path(args.repo).resolve())
    rows = payload["families"]
    if args.longitudinal_gap:
        rows = [row for row in rows if row["longitudinal_status"] == "LONGITUDINAL_RESEARCH_GAP"]
    if args.longitudinal_ready:
        rows = [row for row in rows if row["longitudinal_status"] == "LONGITUDINAL_RESEARCH_READY"]
    if args.json:
        json.dump(rows, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(render_text(payload, rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
