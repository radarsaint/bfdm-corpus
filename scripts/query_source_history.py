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
REVISION_CONTEXT = {"REVISION_CONTEXT_FOR_SOURCE_FAMILY"}


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
    family_live = []
    if family:
        for other_id, other in records.items():
            if other_id == corpus_id or other.get("document_family_id") != family:
                continue
            for link in other.get("source_links") or []:
                if link.get("link_type") in LIVE:
                    family_live.append(_link_view(other_id, link, "family"))
    family_live.sort(key=lambda row: (row["owner"], row["link_type"] or ""))
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
        "revision_context": [row for row in links if row["link_type"] in REVISION_CONTEXT],
        "live_contact": [row for row in links if row["link_type"] in LIVE],
        "family_live_contact": family_live,
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


def render_text(report: dict) -> str:
    if not report.get("found"):
        return f"{report.get('corpus_id')}: not found\n"
    lines = [
        f"{report['corpus_id']}: {report.get('title')}",
        f"family: {report.get('document_family_id')}",
        "members: " + ", ".join(report.get("family_members") or []),
    ]
    projects = report.get("project") or []
    if projects:
        lines.append(
            "project: "
            + "; ".join(
                f"{item.get('project_id')} ({item.get('confidence')})" for item in projects
            )
        )
    elif report.get("project_unresolved"):
        lines.append("project: unresolved")
    stages = report.get("production_stages") or []
    if stages:
        lines.append("stage: " + ", ".join(item.get("stage") or "" for item in stages))
    elif report.get("production_stage_unresolved"):
        lines.append("stage: unresolved")
    def dump(label: str, rows: list[dict]) -> None:
        lines.append(f"{label}:")
        if not rows:
            lines.append("  (none)")
            return
        for row in rows:
            target = row.get("to_corpus_id") or row.get("external_locator") or ""
            lines.append(
                f"  {row.get('direction')} {row.get('link_type')} {target} owner={row.get('owner')}"
            )

    dump("before", report.get("came_before") or [])
    dump("after", report.get("came_after") or [])
    dump("revision_context", report.get("revision_context") or [])
    dump("publication", report.get("publication") or [])
    dump("companions", report.get("companions") or [])
    dump("live_contact", report.get("live_contact") or [])
    dump("family_live_contact", report.get("family_live_contact") or [])
    if report.get("live_use_unresolved"):
        lines.append("live use: not established")
    gaps = report.get("not_established") or []
    if gaps:
        lines.append("not established:")
        for item in gaps:
            lines.append(f"  {item.get('question')}: {item.get('status')}")
    lines.append(
        "Family live contact is another member's link. It is not a claim this document was used."
    )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read recorded source history for one corpus id.")
    parser.add_argument("corpus_id")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--text", action="store_true", help="Print a short reading instead of JSON.")
    parser.add_argument("--json", action="store_true", help="Print JSON. This is the default.")
    args = parser.parse_args(argv)
    repo = Path(args.repo).resolve()
    report = orient(load_records(repo), args.corpus_id)
    if args.text and not args.json:
        sys.stdout.write(render_text(report))
    else:
        json.dump(report, sys.stdout, indent=2)
        sys.stdout.write("\n")
    return 0 if report.get("found") else 1


if __name__ == "__main__":
    raise SystemExit(main())
