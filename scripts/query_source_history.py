#!/usr/bin/env python3
"""Answer source-history questions from metadata already in the repo.

This does not infer relationships. Incoming links count: a revision stored
on the later document is visible from the earlier one.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

BEFORE = {"REVISES", "SUPERSEDES", "PREDECESSOR_OF", "SUCCESSOR_OF"}
LIVE = {"IMPLEMENTED_IN", "ALTERED_IN", "ABANDONED_IN", "OUTCOME_DOCUMENTED_IN", "DISCUSSED_IN"}
PUBLICATION = {"PUBLISHED_AS", "PUBLISHED_VERSION_OF_OR_RELATED_TO"}


def load_records(repo: Path) -> dict[str, dict]:
    records = {}
    for base in (repo / "sources", repo / "context"):
        if not base.exists():
            continue
        for path in base.glob("**/metadata.json"):
            meta = json.loads(path.read_text(encoding="utf-8"))
            cid = meta.get("corpus_id")
            if isinstance(cid, str):
                records[cid] = meta
    return records


def _link_view(owner: str, link: dict, direction: str) -> dict:
    return {
        "direction": direction,
        "owner": owner,
        "link_type": link.get("link_type"),
        "to_corpus_id": link.get("to_corpus_id"),
        "external_locator": link.get("external_locator"),
        "confidence": link.get("confidence"),
        "basis": link.get("basis"),
    }


def orient(records: dict[str, dict], corpus_id: str) -> dict:
    meta = records.get(corpus_id)
    if meta is None:
        return {"corpus_id": corpus_id, "found": False}
    context = meta.get("historical_context") or {}
    family = meta.get("document_family_id")
    outgoing = [
        _link_view(corpus_id, link, "outgoing") for link in meta.get("source_links") or []
    ]
    incoming = []
    for other_id, other in records.items():
        if other_id == corpus_id:
            continue
        for link in other.get("source_links") or []:
            if link.get("to_corpus_id") == corpus_id:
                incoming.append(_link_view(other_id, link, "incoming"))
    incoming.sort(key=lambda row: (row["owner"], row["link_type"] or ""))
    gaps = context.get("not_established") or []
    gap_questions = {item.get("question") for item in gaps}
    stages = context.get("production_stages") or []
    projects = context.get("project_links") or []
    links = outgoing + incoming
    return {
        "corpus_id": corpus_id,
        "found": True,
        "title": meta.get("title") or meta.get("source_title"),
        "source_role": meta.get("source_role"),
        "document_family_id": family,
        "family_members": sorted(
            cid for cid, row in records.items() if family and row.get("document_family_id") == family
        ),
        "project": [
            {
                "relation": link.get("relation"),
                "project_id": link.get("project_id"),
                "confidence": link.get("confidence"),
                "basis": link.get("basis"),
            }
            for link in projects
        ],
        "project_unresolved": "exact_project" in gap_questions,
        "production_stages": [
            {"stage": stage.get("stage"), "confidence": stage.get("confidence"), "basis": stage.get("basis")}
            for stage in stages
        ],
        "production_stage_unresolved": "production_stage" in gap_questions,
        "came_before": [
            row for row in links if row["link_type"] in BEFORE and _is_before(corpus_id, row)
        ],
        "came_after": [
            row for row in links if row["link_type"] in BEFORE and _is_after(corpus_id, row)
        ],
        "companions": [row for row in links if row["link_type"] in {"COMPANION_TO", "DEV_PUBLIC_PAIR"}],
        "publication": [row for row in links if row["link_type"] in PUBLICATION],
        "live_contact": [row for row in links if row["link_type"] in LIVE],
        "live_use_unresolved": "live_use" in gap_questions,
        "not_established": gaps,
        "other_links": [
            row
            for row in links
            if row["link_type"] not in BEFORE | LIVE | PUBLICATION | {"COMPANION_TO", "DEV_PUBLIC_PAIR"}
        ],
    }


def _is_before(corpus_id: str, row: dict) -> bool:
    """True when the link says some other source precedes corpus_id."""
    kind = row["link_type"]
    outgoing = row["direction"] == "outgoing"
    if kind in {"REVISES", "SUPERSEDES"}:
        return outgoing
    if kind == "PREDECESSOR_OF":
        return not outgoing
    if kind == "SUCCESSOR_OF":
        return outgoing
    return False


def _is_after(corpus_id: str, row: dict) -> bool:
    kind = row["link_type"]
    outgoing = row["direction"] == "outgoing"
    if kind in {"REVISES", "SUPERSEDES"}:
        return not outgoing
    if kind == "SUCCESSOR_OF":
        return not outgoing
    if kind == "PREDECESSOR_OF":
        return outgoing
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read recorded source history for one corpus id.")
    parser.add_argument("corpus_id")
    parser.add_argument("--repo", default=".")
    args = parser.parse_args(argv)
    repo = Path(args.repo).resolve()
    report = orient(load_records(repo), args.corpus_id)
    json.dump(report, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0 if report.get("found") else 1


if __name__ == "__main__":
    raise SystemExit(main())
