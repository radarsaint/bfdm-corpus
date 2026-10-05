#!/usr/bin/env python3
"""List sources that record a project link for one registry project id."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

from query_source_history import load_records


def project_report(records: dict[str, dict], project_id: str) -> dict:
    families: dict[str, list[dict]] = defaultdict(list)
    for cid, meta in sorted(records.items()):
        context = meta.get("historical_context") or {}
        matches = [
            link
            for link in context.get("project_links") or []
            if link.get("project_id") == project_id
        ]
        if not matches:
            continue
        live = [
            link.get("external_locator") or link.get("to_corpus_id")
            for link in meta.get("source_links") or []
            if link.get("link_type") in {"IMPLEMENTED_IN", "ALTERED_IN", "ABANDONED_IN", "OUTCOME_DOCUMENTED_IN", "DISCUSSED_IN"}
        ]
        families[meta.get("document_family_id") or "(no family)"].append(
            {
                "corpus_id": cid,
                "title": meta.get("title") or meta.get("source_title"),
                "relation": matches[0].get("relation"),
                "confidence": matches[0].get("confidence"),
                "production_stages": [
                    stage.get("stage") for stage in context.get("production_stages") or []
                ],
                "live_locators": [item for item in live if item],
                "not_established": [
                    item.get("question") for item in context.get("not_established") or []
                ],
            }
        )
    return {
        "project_id": project_id,
        "found": bool(families),
        "source_count": sum(len(rows) for rows in families.values()),
        "families": [
            {"document_family_id": name, "members": members}
            for name, members in sorted(families.items())
        ],
    }


def render_text(report: dict) -> str:
    if not report["found"]:
        return f"{report['project_id']}: no source records this project id\n"
    lines = [f"{report['project_id']}: {report['source_count']} sources"]
    for family in report["families"]:
        lines.append(f"{family['document_family_id']}")
        for row in family["members"]:
            stages = ", ".join(row["production_stages"]) or "stage unrecorded"
            live = ", ".join(row["live_locators"]) or "no live link"
            lines.append(
                f"  {row['corpus_id']} {row['relation']} {row['confidence']} | {stages} | {live}"
            )
            lines.append(f"    {row['title']}")
    lines.append("Sources with no project link are omitted. Omission is not a season assignment.")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read sources placed on one project.")
    parser.add_argument("project_id")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    report = project_report(load_records(Path(args.repo).resolve()), args.project_id)
    if args.json:
        json.dump(report, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(render_text(report))
    return 0 if report["found"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
