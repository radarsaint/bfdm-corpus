#!/usr/bin/env python3
"""Stage matrix for source families.

PRESENT means at least one recorded artifact of that stage.
KNOWN_GAP means a named artifact for that stage is absent and no artifact of
that stage is already present.
NOT_ESTABLISHED means this audit did not find evidence the stage occurred.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

STAGES = [
    "IDEATION / RESEARCH",
    "DRAFT / PREP",
    "REVISION",
    "DEV DISCUSSION",
    "OPERATIONS / HANDOFF",
    "PLAYER-FACING PUBLICATION",
    "LIVE CONTACT",
    "OUTCOME / AFTERMATH",
    "LATER CORRECTION / RETROSPECTIVE",
]
STAGE_MAP = {
    "RESEARCH_INSPIRATION": "IDEATION / RESEARCH",
    "BRAINSTORMING": "IDEATION / RESEARCH",
    "PREPRODUCTION": "DRAFT / PREP",
    "SYSTEM_DEVELOPMENT": "DRAFT / PREP",
    "CAMPAIGN_OPERATIONS": "OPERATIONS / HANDOFF",
    "LIVE_USE_ARTIFACT": "LIVE CONTACT",
    "PUBLIC_PLAYER_FACING_PUBLICATION": "PLAYER-FACING PUBLICATION",
    "POSTMORTEM_CORRECTION": "LATER CORRECTION / RETROSPECTIVE",
    "LATER_RETROSPECTIVE": "LATER CORRECTION / RETROSPECTIVE",
}
REVISION = {"REVISES", "SUPERSEDES", "PREDECESSOR_OF", "SUCCESSOR_OF", "REVISION_CONTEXT_FOR_SOURCE_FAMILY"}
LIVE = {"IMPLEMENTED_IN", "ALTERED_IN", "ABANDONED_IN", "OUTCOME_DOCUMENTED_IN"}
PUBLICATION = {"PUBLISHED_AS", "PUBLISHED_VERSION_OF_OR_RELATED_TO"}

# Applied only when the stage is still NOT_ESTABLISHED.
KNOWN_GAPS = {
    "roanoke-s3-halwudgie-lore": {
        "REVISION": "Player race edits (drive 11GF5rYImy_jdf7NxAtf5gI-OW2DCTlxjgZCOHLnC3cY) records Halfwudgie revisions and is not in the corpus.",
    },
    "roanoke-s3-uru-lore": {
        "REVISION": "The same player-race-edits document records Urucokra flight changes and is not in the corpus.",
    },
    "roanoke-s3-jackalope-lore": {
        "REVISION": "The same player-race-edits document records Jackalope revisions and is not in the corpus.",
    },
    "roanoke-chinnokin-lore": {
        "REVISION": "The same player-race-edits document records Chinnokin changes and is not in the corpus.",
    },
    "roanoke-s3-uru-halfwudgie": {
        "REVISION": "The player-race-edits document is the known revision layer for these ancestries and is not a container.",
    },
}

NOTES = {
    "roanoke-crafting-system": "Live contact is on the public doc only. BCS-000020 and BCS-000080 have no season.",
    "roanoke-s3-campaign-manuscript": "BCS-000043 is in the family and has no predecessor or successor edge.",
    "roanoke-s3-changelog": "The changelog is a revision document. Its links are companions to lore, not REVISES edges to the manuscript.",
    "roanoke-s3-week-operations": "Week sheets schedule modules. That is not live contact. Week 4 cast and the week 5 map file are archive gaps.",
    "roanoke-s3-campaign-structure": "The only member is a disambiguation that revises the timeline. Readiness calls that a trajectory.",
    "roanoke-s3-timeline": "Longitudinal readiness is the incoming revision from BCS-000115, not a play history.",
    "empire-city-airship-qualification": "One flight-school session matches the standard exercise. Airship Rules is named and has no drive id.",
    "empire-city-crafting": "IMPLEMENTED_IN is the approval channel. rule_by_rule_live_identity stays not established.",
    "empire-city-broadsheet": "Issues are companions, not an ordered successor chain. Distribution in live chat is not established.",
    "empire-city-operations": "Season 4 Master Timeline is a known Drive file and is not a container.",
    "at-wars-end-narrative": "Draft 3 is not a REVISES edge. Draft 5 revises draft 1 and does not supersede the middle drafts.",
    "roanoke-s5-google-sites-revision-process": "REVISION_CONTEXT points at named site pages. The readiness label does not count that link type as a trajectory.",
    "roanoke-s5-way-of-gun-fu": "PUBLISHED_AS is a publication edge. Live use is not established. No Season 5 harvest is in the corpus.",
    "roanoke-s5-published-sites": "Publication is not live use. The 2022 style guide and the Season 5 DM guide are not containers.",
    "bastion-redoubt-campaign": "Three companions. No live harvest.",
    "earthfall-rod": "Spec and operator script. No live harvest.",
    "exploration-impossible-context": "Third-party manuscript. Not BFDM precedent.",
}


def blank() -> dict[str, str]:
    return {stage: "NOT_ESTABLISHED" for stage in STAGES}


def build(repo: Path) -> dict:
    records = {}
    for base in (repo / "sources", repo / "context"):
        for path in base.glob("**/metadata.json"):
            meta = json.loads(path.read_text(encoding="utf-8"))
            cid = meta.get("corpus_id")
            if isinstance(cid, str):
                records[cid] = meta
    families: dict[str, list[str]] = {}
    for cid, meta in records.items():
        family = meta.get("document_family_id")
        if family:
            families.setdefault(family, []).append(cid)
    matrix = []
    for family, members in sorted(families.items()):
        stages = blank()
        if family == "exploration-impossible-context":
            for key in ("DEV DISCUSSION", "OPERATIONS / HANDOFF", "LIVE CONTACT", "OUTCOME / AFTERMATH"):
                stages[key] = "NOT_APPLICABLE"
        for cid in members:
            meta = records[cid]
            context = meta.get("historical_context") or {}
            for item in context.get("production_stages") or []:
                mapped = STAGE_MAP.get(item.get("stage"))
                if mapped:
                    stages[mapped] = "PRESENT"
            for link in meta.get("source_links") or []:
                kind = link.get("link_type")
                if kind in REVISION:
                    stages["REVISION"] = "PRESENT"
                if kind in LIVE:
                    stages["LIVE CONTACT"] = "PRESENT"
                    if kind == "OUTCOME_DOCUMENTED_IN":
                        stages["OUTCOME / AFTERMATH"] = "PRESENT"
                if kind in PUBLICATION:
                    stages["PLAYER-FACING PUBLICATION"] = "PRESENT"
                if kind == "DISCUSSED_IN":
                    stages["DEV DISCUSSION"] = "PRESENT"
        for stage, why in KNOWN_GAPS.get(family, {}).items():
            if stages.get(stage) == "NOT_ESTABLISHED":
                stages[stage] = "KNOWN_GAP"
        matrix.append(
            {
                "document_family_id": family,
                "members": sorted(members),
                "stages": stages,
                "note": NOTES.get(family, ""),
            }
        )
    return {
        "substrate": "ingest/drive-history-v1",
        "stage_vocabulary": STAGES,
        "families": matrix,
    }


def render(payload: dict) -> str:
    lines = [
        "# Source-family stage matrix — 2026-10-05",
        "",
        "`PRESENT` means the corpus has at least one recorded artifact of that stage.",
        "`KNOWN_GAP` means a named artifact for that stage is absent, and nothing else already fills the stage.",
        "`NOT_ESTABLISHED` means this audit did not find evidence that the stage happened.",
        "`NOT_APPLICABLE` is used only for Exploration Impossible's table-play stages.",
        "",
        "A missing file inside a stage that is otherwise present stays in the archive-gap ledger. It does not flip the stage to `KNOWN_GAP`.",
        "",
    ]
    header = "| Family | " + " | ".join(STAGES) + " |"
    lines.append(header)
    lines.append("| --- | " + " | ".join("---" for _ in STAGES) + " |")
    for row in payload["families"]:
        cells = " | ".join(row["stages"][stage] for stage in STAGES)
        lines.append(f"| `{row['document_family_id']}` | {cells} |")
    lines.extend(["", "## Notes", ""])
    for row in payload["families"]:
        if row["note"]:
            lines.append(f"- `{row['document_family_id']}`: {row['note']}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build(Path(args.repo).resolve())
    if args.write:
        dest = Path(args.repo).resolve() / "research" / "substrate"
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "family_stage_matrix.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        (dest / "family_stage_matrix.md").write_text(render(payload), encoding="utf-8")
    print(len(payload["families"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
