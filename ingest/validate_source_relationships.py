#!/usr/bin/env python3
"""Validate optional historical-context and source-link metadata on BFDM sources."""

from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT_RELATIONS = {"BELONGS_TO_PROJECT", "RELATES_TO_PROJECT", "CROSS_PROJECT"}
STAGES = {
    "RESEARCH_INSPIRATION", "BRAINSTORMING", "PREPRODUCTION", "SYSTEM_DEVELOPMENT",
    "CAMPAIGN_OPERATIONS", "LIVE_USE_ARTIFACT", "PUBLIC_PLAYER_FACING_PUBLICATION",
    "POSTMORTEM_CORRECTION", "LATER_RETROSPECTIVE",
}
LINK_TYPES = {
    "VERSION_OF", "PREDECESSOR_OF", "SUCCESSOR_OF", "REVISES", "SUPERSEDES",
    "PUBLISHED_AS", "DEV_PUBLIC_PAIR", "DERIVED_FROM", "COPIED_REPRESENTATION_OF",
    "RESPONDS_TO", "COMPANION_TO", "IMPLEMENTED_IN", "DISCUSSED_DURING",
    "ALTERED_DURING_PLAY", "ABANDONED_BEFORE_PLAY", "OUTCOME_DOCUMENTED_IN",
}
TARGET_KINDS = {"SOURCE", "DISCORD_MESSAGE", "DISCORD_CHANNEL", "DISCORD_SERVER", "EXTERNAL_SOURCE", "RESEARCH_RECORD"}

def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def main() -> int:
    errors: list[str] = []
    projects = {r["project_id"] for r in load_jsonl(ROOT / "registry" / "projects.jsonl")}
    catalog = {r["corpus_id"] for r in load_jsonl(ROOT / "evidence" / "catalog.jsonl")}

    checked = 0
    for base in (ROOT / "sources", ROOT / "context"):
        if not base.exists():
            continue
        for path in base.glob("**/metadata.json"):
            meta = json.loads(path.read_text(encoding="utf-8"))
            cid = meta.get("corpus_id")
            hist = meta.get("historical_context") or {}
            links = meta.get("source_links") or []
            if not hist and not links:
                continue
            checked += 1

            for p in hist.get("project_links", []):
                if p.get("project_id") not in projects:
                    errors.append(f"{cid}: unknown project_id {p.get('project_id')}")
                if p.get("relation") not in PROJECT_RELATIONS:
                    errors.append(f"{cid}: invalid project relation {p.get('relation')}")
                if not p.get("basis") or not p.get("confidence") or not p.get("support_refs"):
                    errors.append(f"{cid}: project link lacks basis/confidence/support_refs")

            for s in hist.get("production_stages", []):
                if s.get("stage") not in STAGES:
                    errors.append(f"{cid}: invalid production stage {s.get('stage')}")
                if not s.get("basis") or not s.get("confidence") or not s.get("support_refs"):
                    errors.append(f"{cid}: production stage lacks basis/confidence/support_refs")

            for link in links:
                if link.get("link_type") not in LINK_TYPES:
                    errors.append(f"{cid}: invalid source link type {link.get('link_type')}")
                if link.get("target_kind") not in TARGET_KINDS:
                    errors.append(f"{cid}: invalid target_kind {link.get('target_kind')}")
                target = link.get("to_corpus_id")
                external = link.get("external_locator")
                if not target and not external:
                    errors.append(f"{cid}: source link has no target")
                if target and target not in catalog:
                    errors.append(f"{cid}: source link target {target} not in catalog")
                if not link.get("basis") or not link.get("confidence") or not link.get("support_refs"):
                    errors.append(f"{cid}: source link lacks basis/confidence/support_refs")

    print(f"source metadata records with historical relationships: {checked}")
    if errors:
        print(f"FAILED: {len(errors)} source relationship error(s)", file=sys.stderr)
        for e in errors:
            print(f" - {e}", file=sys.stderr)
        return 1
    print("OK: BFDM source relationship validation passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
