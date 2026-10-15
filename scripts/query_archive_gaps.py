#!/usr/bin/env python3
"""Filter the archive-gap ledger. This does not decide that an event happened."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_gaps(repo: Path) -> list[dict]:
    path = repo / "research" / "substrate" / "archive_gaps.jsonl"
    if not path.is_file():
        raise SystemExit(f"missing ledger: {path}")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def select(rows: list[dict], project: str | None, status: str | None) -> list[dict]:
    chosen = rows
    if project:
        chosen = [row for row in chosen if project in (row.get("project_or_family") or "")]
    if status:
        chosen = [row for row in chosen if row.get("status") == status]
    return chosen


def render_text(rows: list[dict]) -> str:
    if not rows:
        return "No archive-gap rows matched.\n"
    lines = [f"{len(rows)} archive-gap rows"]
    for row in rows:
        lines.append(
            f"{row.get('gap_id')} [{row.get('status')}] {row.get('referenced_name')}"
        )
        lines.append(f"  from: {row.get('referenced_from')}")
        lines.append(f"  project: {row.get('project_or_family')}")
        if row.get("known_drive_id_if_any"):
            lines.append(f"  drive: {row.get('known_drive_id_if_any')}")
        if row.get("candidate_ledger_match_if_any"):
            lines.append(f"  candidate: {row.get('candidate_ledger_match_if_any')}")
        lines.append(f"  why: {row.get('why_it_matters')}")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read known missing-source rows.")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--project", help="Substring of project_or_family, for example roanoke-s3.")
    parser.add_argument("--status")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    rows = select(load_gaps(Path(args.repo).resolve()), args.project, args.status)
    if args.json:
        json.dump(rows, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(render_text(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
