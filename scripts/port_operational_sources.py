#!/usr/bin/env python3
"""Port operational and context containers that were left out of the first history pass.

Source preservation is not historical placement. A container is copied when the
donor branch has one. Exact season, week, or live-use claims stay unresolved
unless the body or a cited Discord message supports them.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DONOR = "origin/ingest/drive-project-v3"
INGESTED_AT = "2026-10-05T18:10:00Z"

LIVE_GAP = {
    "question": "live_use",
    "status": "NOT_ESTABLISHED",
    "basis": (
        "This container is preparation, publication, or an operations form. "
        "It does not by itself show what players did, what a DM approved in play, "
        "or which planned events occurred."
    ),
}


def git_bytes(path: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), "show", f"{DONOR}:{path}"])


def git_paths(prefix: str) -> list[str]:
    out = subprocess.check_output(
        ["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only", DONOR, prefix],
        text=True,
    )
    return [line for line in out.splitlines() if line]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def belongs(project_id: str, confidence: str, basis: str, refs: list[str]) -> dict:
    return {
        "project_id": project_id,
        "relation": "BELONGS_TO_PROJECT",
        "confidence": confidence,
        "basis": basis,
        "support_refs": refs,
    }


def stage(name: str, confidence: str, basis: str, refs: list[str]) -> dict:
    return {"stage": name, "confidence": confidence, "basis": basis, "support_refs": refs}


def link(kind: str, target: str, confidence: str, basis: str, refs: list[str]) -> dict:
    return {
        "link_type": kind,
        "target_kind": "SOURCE",
        "to_corpus_id": target,
        "confidence": confidence,
        "basis": basis,
        "support_refs": refs,
    }


def gap(question: str, basis: str) -> dict:
    return {"question": question, "status": "NOT_ESTABLISHED", "basis": basis}


def spec(**kwargs) -> dict:
    kwargs.setdefault("not_established", [LIVE_GAP])
    kwargs.setdefault("project_links", [])
    kwargs.setdefault("stages", [])
    kwargs.setdefault("links", [])
    kwargs.setdefault("role", None)
    kwargs.setdefault("dest_prefix", None)
    return kwargs


S4 = "roanoke-s4"
S3 = "roanoke-s3"

POSTS = [
    ("BCS-000005", "July 10, 1776"),
    ("BCS-000006", "July 11, 1776"),
    ("BCS-000007", "July 12, 1776"),
    ("BCS-000008", "July 13, 1776"),
    ("BCS-000009", "July 16, 1776"),
    ("BCS-000010", "July 17, 1776"),
    ("BCS-000011", "July 19, 1776"),
    ("BCS-000012", "July 21, 1776"),
    ("BCS-000013", "July 22, 1776"),
    ("BCS-000014", "July 23, 1776"),
    ("BCS-000015", "July 24, 1776"),
]


def post_spec(cid: str, in_world: str, previous: str | None) -> dict:
    links = []
    if previous:
        links.append(
            link(
                "COMPANION_TO",
                previous,
                "STRONG",
                (
                    f"This is the Empire City broadsheet issue dated {in_world}. "
                    f"{previous} is an earlier issue of the same broadsheet. "
                    "A later issue is not treated as a revision or replacement of the earlier one."
                ),
                [cid, previous],
            )
        )
    else:
        links.append(
            link(
                "COMPANION_TO",
                "BCS-000004",
                "STRONG",
                (
                    "The July 10 issue uses Empire City, Ferrytown, Hampstead, and the Redcoats. "
                    "The Season 4 orientation script introduces those same places. "
                    "The newspaper is not evidence that the orientation was delivered."
                ),
                [cid, "BCS-000004"],
            )
        )
    return spec(
        donor_id=cid,
        corpus_id=cid,
        donor_prefix=f"sources/empire-city/{cid}",
        dest_prefix=f"sources/empire-city/{cid}",
        family="empire-city-broadsheet",
        project_links=[
            belongs(
                S4,
                "STRONG",
                (
                    f"The issue is dated {in_world} and names Empire City. "
                    "It uses boroughs and the Redcoats from the Season 4 orientation. "
                    "The in-world date is not proof the issue was posted on that real-world day."
                ),
                [cid, "BCS-000004"],
            )
        ],
        stages=[
            stage(
                "PUBLIC_PLAYER_FACING_PUBLICATION",
                "STRONG",
                "The source is written as a priced city newspaper. Whether it was posted to players is not established.",
                [cid],
            )
        ],
        links=links,
    )


WEEK = {
    "BCS-000048": ("week 1 breakdown", "CAMPAIGN_OPERATIONS", "The source is the Roanoke S3 week 1 run sheet, opening Saturday 07/18/20 in London."),
    "BCS-000049": ("week 1 cast", "CAMPAIGN_OPERATIONS", "The source is titled Week 1 Cast and describes NPCs prepared for that week."),
    "BCS-000030": ("week 1 set list", "CAMPAIGN_OPERATIONS", "The source is the Week One set list for Roanoke S3 2.1, naming player hubs and society locations."),
    "BCS-000050": ("week 1 passdown", "CAMPAIGN_OPERATIONS", "The source is the week 1 handoff form for other DMs. It contains one recruitment note and is not a log of the week."),
    "BCS-000029": ("week 2 breakdown", "CAMPAIGN_OPERATIONS", "The source is the Roanoke S3 week 2 breakdown for the Tir Na Nog, opening Saturday 7/25/2020."),
    "BCS-000051": ("week 2 cast", "CAMPAIGN_OPERATIONS", "The source is the week 2 cast for the Tir Na Nog."),
    "BCS-000032": ("week 2 set list", "CAMPAIGN_OPERATIONS", "The source is the week 2 set list for the Tir Na Nog."),
    "BCS-000031": ("week 2 passdown", "CAMPAIGN_OPERATIONS", "The source is the week 2 handoff template. The captured body has the template and no filled incident notes."),
    "BCS-000052": ("week 3 breakdown", "CAMPAIGN_OPERATIONS", "The source is the Roanoke S3 week 3 breakdown, opening Saturday 08/01/2020 on the island."),
    "BCS-000033": ("week 3 cast", "CAMPAIGN_OPERATIONS", "The source lists NPCs new for the week and points back to the week 2 cast."),
    "BCS-000035": ("week 3 set list", "CAMPAIGN_OPERATIONS", "The source is the week 3 set list and cites the master schedule and the main map."),
    "BCS-000034": ("week 3 passdown", "CAMPAIGN_OPERATIONS", "The source is the week 3 handoff template. The captured body has no filled incident notes."),
    "BCS-000037": ("week 4 breakdown", "CAMPAIGN_OPERATIONS", "The source is the week 4 breakdown, with Saturday 08/08/2020, and it cites the week 4 set list."),
    "BCS-000039": ("week 4 set list", "CAMPAIGN_OPERATIONS", "The source is the week 4 set list for flooded Roanoke."),
    "BCS-000038": ("week 4 passdown", "CAMPAIGN_OPERATIONS", "The source is the week 4 handoff template. The captured body has no filled incident notes."),
    "BCS-000053": ("week 5 breakdown", "CAMPAIGN_OPERATIONS", "The source is the week 5 breakdown, opening Saturday 08/15/2020, including the Morkoth lodestone."),
    "BCS-000040": ("week 5 passdown", "CAMPAIGN_OPERATIONS", "The source is the week 5 handoff template. The captured body has no filled incident notes."),
}

ABSENT_REFS = {
    "BCS-000029": (
        "The week 2 breakdown links Tir Na Nog stats at drive:1PaDpQNqaX-6uTxQCmDkNqjqpVJcquSaYtRkCNSzHcd0 "
        "and Travel Drama at drive:1YN-UzOjCMX7zuM3RxaHMQ5MnGqJErkofEIn5R-CGp_g. "
        "Neither Drive id is a cataloged corpus source."
    ),
    "BCS-000037": (
        "The week 4 breakdown names a week four cast list without a corpus container, "
        "and links a Tatankan escape room at drive:1HeeyOpTO5OFuM0tPT5l-K3Dq4osnyUEa-PEJBbEabsc, "
        "which is not a cataloged corpus source."
    ),
    "BCS-000048": (
        "The week 1 breakdown links Twilight Manor at drive:1PlvWTEJ_C294RdlY2OlkPxB_8AV1SFm9jZWIWJWMloY, "
        "which is not a cataloged corpus source."
    ),
    "BCS-000053": (
        "The week 5 breakdown links a Spelljammer lodestone document at "
        "drive:1sMZDhkyu6ktndPQF1j5NPP4cjw-XbTjGQTvN0f5oho0 and a map at "
        "drive:1NnYMxq39WObWYIn-1blbuD7uHXon-c-v. Neither id is a cataloged corpus source. "
        "The headings 'Week 4 Cast list' and 'Week 4 Sets' are not a found container for a separate week 4 cast."
    ),
}


def build_specs() -> list[dict]:
    specs = [
        spec(
            donor_id="BCS-000002",
            corpus_id="BCS-000002",
            donor_prefix="sources/empire-city/BCS-000002",
            dest_prefix="sources/empire-city/BCS-000002",
            family="unplaced-five-week-planning",
            project_links=[],
            stages=[
                stage(
                    "PREPRODUCTION",
                    "STRONG",
                    "The body is a draft task list for a five-week calendar, main events, meetings, art, economy, items, and vehicles.",
                    ["BCS-000002"],
                )
            ],
            not_established=[
                gap(
                    "exact_project",
                    (
                        "The list mentions a calendar based on kings bridge noir and dates in 2020 and 2021. "
                        "It does not name Empire City or a season. The donor folder is not treated as season membership."
                    ),
                ),
                LIVE_GAP,
            ],
        ),
        spec(
            donor_id="BCS-000004",
            corpus_id="BCS-000004",
            donor_prefix="sources/empire-city/BCS-000004",
            dest_prefix="sources/empire-city/BCS-000004",
            family="empire-city-player-orientation",
            project_links=[
                belongs(
                    S4,
                    "CONFIRMED",
                    "The script welcomes the listener to Season 4 of Tales from Arcania and guides them through Empire City.",
                    ["BCS-000004"],
                )
            ],
            stages=[
                stage(
                    "PUBLIC_PLAYER_FACING_PUBLICATION",
                    "STRONG",
                    "The source is a player-facing server orientation script. Delivery of the video is not established.",
                    ["BCS-000004"],
                )
            ],
            links=[
                link(
                    "COMPANION_TO",
                    "BCS-000072",
                    "STRONG",
                    "The script and the Season 4 directory describe the same event's boroughs. The script is not an edition of the directory.",
                    ["BCS-000004", "BCS-000072"],
                )
            ],
        ),
        spec(
            donor_id="BCS-000016",
            corpus_id="BCS-000016",
            donor_prefix="sources/empire-city/BCS-000016",
            dest_prefix="sources/empire-city/BCS-000016",
            family="empire-city-operations",
            role="signup_responses",
            project_links=[
                belongs(
                    S4,
                    "STRONG",
                    (
                        "The form is the Empire City RP sign-up and asks whether the person played in any of the three Roanoke seasons. "
                        "Responses are not a cast list and do not show who actually played."
                    ),
                    ["BCS-000016"],
                )
            ],
            stages=[
                stage(
                    "CAMPAIGN_OPERATIONS",
                    "STRONG",
                    "The source is a signup response sheet. A response is not evidence of attendance or of what that character did.",
                    ["BCS-000016"],
                )
            ],
        ),
        spec(
            donor_id="BCS-000059",
            corpus_id="BCS-000059",
            donor_prefix="context/exploration-impossible/BCS-000059",
            dest_prefix="context/exploration-impossible/BCS-000059",
            family="exploration-impossible-context",
            role="CONTEXT_ONLY_THIRD_PARTY",
            project_links=[
                belongs(
                    "exploration-impossible",
                    "CONFIRMED",
                    (
                        "This is the Exploration Impossible manuscript. "
                        "Placement here does not make the prose Brendon-authored or BFDM precedent."
                    ),
                    ["BCS-000059"],
                )
            ],
            stages=[],
            links=[],
            not_established=[
                gap(
                    "brendon_authorship",
                    (
                        "The manuscript is credited to Michael Kennish. "
                        "Comments attributed to Brendon Faulkner in the preserved comments file are editorial context, "
                        "not authorship of the manuscript."
                    ),
                ),
                gap(
                    "production_stage",
                    "The manuscript's own drafting stage is not a BFDM production stage and is not assigned.",
                ),
            ],
        ),
        spec(
            donor_id="BCS-000018",
            corpus_id="BCS-000018",
            donor_prefix="sources/roanoke/BCS-000018",
            dest_prefix="sources/roanoke/BCS-000018",
            family="roanoke-s3-week-operations",
            role="master_schedule",
            project_links=[
                belongs(
                    S3,
                    "CONFIRMED",
                    "The sheet is the Roanoke 3 master schedule and its week 1 Saturday is 7/18, the registered Season 3 opening.",
                    ["BCS-000018"],
                )
            ],
            stages=[
                stage(
                    "CAMPAIGN_OPERATIONS",
                    "CONFIRMED",
                    "The sheet assigns days, events, and DMs across five weeks. An assignment is not evidence the event was run.",
                    ["BCS-000018"],
                )
            ],
        ),
        spec(
            donor_id="BCS-000071",
            corpus_id="BCS-000071",
            donor_prefix="sources/roanoke/BCS-000071",
            dest_prefix="sources/roanoke/BCS-000071",
            family="roanoke-s3-week-operations",
            role="mod_directory",
            project_links=[
                belongs(
                    S3,
                    "CONFIRMED",
                    "The source titles itself Roanoke S3 MOD Directory and indexes week resources from 7/18/2020.",
                    ["BCS-000071"],
                )
            ],
            stages=[
                stage(
                    "CAMPAIGN_OPERATIONS",
                    "CONFIRMED",
                    "The directory indexes week breakdowns, sets, casts, and passdowns for moderators.",
                    ["BCS-000071"],
                )
            ],
            not_established=[
                gap(
                    "week_5_date_alignment",
                    (
                        "The directory dates week 5 as 8/07/2020-8/19/2020. "
                        "The master schedule's week boundaries and the week 5 breakdown's Saturday 08/15/2020 "
                        "do not use 8/07 as the week 5 start. The directory line is preserved and not corrected."
                    ),
                ),
                LIVE_GAP,
            ],
        ),
        spec(
            donor_id="BCS-000036",
            corpus_id="BCS-000036",
            donor_prefix="sources/roanoke/BCS-000036",
            dest_prefix="sources/roanoke/BCS-000036",
            family="roanoke-s3-week-operations",
            role="voice_event_draft",
            project_links=[
                belongs(
                    S3,
                    "STRONG",
                    (
                        "The draft is the wreck of the Falmouth after the sub's sabotage, with the Tir Na Nog crew at red alert. "
                        "The Season 3 schedule names a Wreckage of the Falmouth voice event."
                    ),
                    ["BCS-000036", "BCS-000018"],
                )
            ],
            stages=[
                stage(
                    "PREPRODUCTION",
                    "STRONG",
                    "The source is a prepared voice-event scene with checks and lair actions. Performance is not established.",
                    ["BCS-000036"],
                )
            ],
            links=[
                link(
                    "COMPANION_TO",
                    "BCS-000018",
                    "STRONG",
                    (
                        "The schedule names a Wreckage of the Falmouth voice event on 7/31. "
                        "This draft is that scene. The filename says W3, so the schedule date is not rewritten into a week assignment."
                    ),
                    ["BCS-000036", "BCS-000018"],
                )
            ],
            not_established=[
                gap(
                    "exact_week",
                    (
                        "The filename says W3. The master schedule places the Falmouth wreck voice event on 7/31, "
                        "which is week 2 on that sheet. Week membership is not forced from the filename."
                    ),
                ),
                LIVE_GAP,
            ],
        ),
    ]
    previous = None
    for cid, label in POSTS:
        specs.append(post_spec(cid, label, previous))
        previous = cid
    for cid, (role, stage_name, basis) in WEEK.items():
        extra = []
        if cid in ABSENT_REFS:
            extra.append(
                {
                    "question": "referenced_source_absent",
                    "status": "ARCHIVE_GAP",
                    "basis": ABSENT_REFS[cid],
                }
            )
        notes = [LIVE_GAP, *extra]
        if cid == "BCS-000050":
            notes[0] = gap(
                "live_use",
                (
                    "The week 1 passdown records one note, that Ozgur Tepiderez was recruited to the Tir Na Nog crew by Rob. "
                    "That note is not evidence for the rest of the week's schedule."
                ),
            )
        specs.append(
            spec(
                donor_id=cid,
                corpus_id=cid,
                donor_prefix=f"sources/roanoke/{cid}",
                dest_prefix=f"sources/roanoke/{cid}",
                family="roanoke-s3-week-operations",
                role=role,
                project_links=[
                    belongs(
                        S3,
                        "STRONG",
                        f"The preserved opening identifies this as Roanoke S3 material ({role}). {basis}",
                        [cid],
                    )
                ],
                stages=[stage(stage_name, "STRONG", basis, [cid])],
                not_established=notes,
            )
        )
    return specs


def mime_for(path: str) -> str:
    if path.endswith(".md"):
        return "text/markdown"
    if path.endswith(".json") or path.endswith(".jsonl"):
        return "application/json"
    if path.endswith(".docx"):
        return "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    if path.endswith(".xlsx"):
        return "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    if path.endswith(".png"):
        return "image/png"
    if path.endswith((".jpg", ".jpeg")):
        return "image/jpeg"
    return "application/octet-stream"


def kind_for(rel: str) -> str:
    if rel == "source.md":
        return "NORMALIZED_HUMAN_READABLE"
    if rel.startswith("original/"):
        return "GOOGLE_NATIVE_EXPORT_SNAPSHOT"
    if "comment" in rel:
        return "COMMENTS"
    if rel.startswith("revisions/") or rel.endswith("revisions.jsonl"):
        return "REVISION_RECORD"
    if rel.startswith("assets/"):
        return "EMBEDDED_ASSET"
    return "PRESERVED_FILE"


def catalog_rows() -> list[dict]:
    path = ROOT / "evidence" / "catalog.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def locator_from_meta(meta: dict) -> dict:
    drive = None
    library = None
    for loc in meta.get("locators") or []:
        if loc.get("provider") == "google_drive" and drive is None:
            drive = {"id": loc.get("native_id"), "url": loc.get("url"), "mime_type": meta.get("mime_type")}
        if loc.get("provider") == "chatgpt_library" and library is None:
            library = {
                "library_file_id": loc.get("library_file_id"),
                "source_path": loc.get("source_path"),
            }
    return {"google_drive": drive, "chatgpt_library": library}


def load_donor_meta(item: dict) -> dict:
    return json.loads(git_bytes(item["donor_prefix"] + "/metadata.json"))


def build_metadata(item: dict, files: dict[str, bytes], donor_meta: dict) -> dict:
    cid = item["corpus_id"]
    if donor_meta.get("schema_version") == "bfdm_source_metadata/v1":
        meta = json.loads(json.dumps(donor_meta))
    else:
        catalog = next((row for row in catalog_rows() if row["corpus_id"] == cid), {})
        drive = (catalog.get("locators") or {}).get("google_drive") or {}
        drive_id = donor_meta.get("drive_id") or drive.get("id")
        locators = []
        if drive_id:
            locators.append(
                {
                    "provider": "google_drive",
                    "locator_type": "native_document",
                    "native_id": drive_id,
                    "url": drive.get("url") or f"https://docs.google.com/document/d/{drive_id}/edit",
                }
            )
        meta = {
            "schema_version": "bfdm_source_metadata/v1",
            "corpus_id": cid,
            "project": donor_meta.get("project") or catalog.get("project"),
            "project_slug": item["dest_prefix"].split("/")[1],
            "title": donor_meta.get("title") or catalog.get("title"),
            "source_kind": "google_drive_native",
            "original_filename": donor_meta.get("title") or catalog.get("title"),
            "mime_type": (drive or {}).get("mime_type") or "application/vnd.google-apps.document",
            "created_at": None,
            "modified_at": None,
            "ingested_at": INGESTED_AT,
            "authorship": {
                "status": catalog.get("authorship") or "UNKNOWN",
                "basis": catalog.get("authorship_basis")
                or donor_meta.get("provenance_note")
                or "Whole-document authorship was not established by this port.",
            },
            "locators": locators,
            "normalization": {
                "method": "Donor normalized body preserved byte-for-byte.",
                "tool": "BFDM operational-source port",
                "warnings": ["Google-native export is a snapshot, not the live Google document."],
            },
        }
    meta["corpus_id"] = cid
    meta["document_family_id"] = item["family"]
    if item.get("role"):
        meta["source_role"] = item["role"]
    elif donor_meta.get("source_role"):
        meta["source_role"] = donor_meta["source_role"]
    if cid == "BCS-000059":
        meta["seed_eligibility"] = "CONTEXT_ONLY"
        meta["authorship"] = {
            "status": "OTHER_AUTHOR",
            "basis": (
                "The manuscript is credited to Michael Kennish and is not Brendon-authored creative work. "
                "The preserved comments file contains editorial notes, including notes attributed to Brendon Faulkner."
            ),
        }
    representations = []
    for rel in sorted(files):
        representations.append(
            {
                "kind": kind_for(rel),
                "path": f"{item['dest_prefix']}/{rel}",
                "sha256": sha256(files[rel]),
                "mime_type": mime_for(rel),
                "size_bytes": len(files[rel]),
            }
        )
    meta["representations"] = representations
    meta["capture_status"] = {
        "current_body": "CAPTURED" if "source.md" in files else "NOT_CAPTURED",
        "comments": "PRESERVED" if any("comment" in name for name in files) else "NOT_PRESENT",
        "revision_metadata": "PRESERVED" if any(name.endswith("revisions.jsonl") for name in files) else "NOT_PRESENT",
        "revision_bodies": "PRESERVED" if any(name.startswith("revisions/") for name in files) else "NOT_PRESENT",
        "assets": "PRESERVED" if any(name.startswith("assets/") for name in files) else "NONE_EXTRACTED",
    }
    meta["historical_context"] = {
        "project_links": item["project_links"],
        "production_stages": item["stages"],
        "not_established": item["not_established"],
    }
    meta["source_links"] = list(item["links"])
    meta["reconciliation"] = {
        "donor_branch": "ingest/drive-project-v3",
        "donor_corpus_id": item["donor_id"],
        "canonical_corpus_id": cid,
        "id_collision_remap": False,
        "preservation_note": (
            "Native Drive identity and captured artifacts preserved. Source wording was not rewritten. "
            "project/project_slug may record filing location and are not a season assignment when project_links is empty."
        ),
    }
    return meta


def add_url_links(metas: dict[str, dict]) -> None:
    id_by_drive = {}
    for row in catalog_rows():
        drive = (row.get("locators") or {}).get("google_drive") or {}
        if drive.get("id"):
            id_by_drive[drive["id"]] = row["corpus_id"]
    for meta in metas.values():
        for loc in meta.get("locators") or []:
            if loc.get("native_id"):
                id_by_drive[loc["native_id"]] = meta["corpus_id"]
    for cid, meta in metas.items():
        path = ROOT / meta["representations"][0]["path"]
        # source.md is the readable body even if not first after sort; find it.
        source = ROOT / f"{next(item['dest_prefix'] for item in SPECS if item['corpus_id']==cid)}/source.md"
        if not source.exists():
            continue
        body = source.read_text(encoding="utf-8", errors="replace")
        existing = {link.get("to_corpus_id") for link in meta.get("source_links") or []}
        for drive_id, target in sorted(id_by_drive.items()):
            if not drive_id or target == cid or target in existing:
                continue
            if drive_id in body:
                meta["source_links"].append(
                    {
                        "link_type": "COMPANION_TO",
                        "target_kind": "SOURCE",
                        "to_corpus_id": target,
                        "confidence": "CONFIRMED",
                        "basis": "This source's body contains the other source's native Google Drive id.",
                        "support_refs": [cid, target, f"drive:{drive_id}"],
                    }
                )
                existing.add(target)


def upsert_catalog(rows: list[dict], meta: dict, dest_prefix: str) -> list[dict]:
    cid = meta["corpus_id"]
    snap = {"repo_path": f"{dest_prefix}/source.md", "status": "RECONCILED_CONTAINER"}
    note = (
        " 2026-10-05: operational/context container ported from ingest/drive-project-v3. "
        "Placement and links are only those in metadata. Unknowns stay in not_established."
    )
    if cid == "BCS-000059":
        note += (
            " Preserved comments.json has 31 comment objects (29 attributed to Brendon Faulkner, "
            "2 to Michael Kennish). The earlier 78 figure was not re-counted from that file."
        )
    found = False
    for row in rows:
        if row.get("corpus_id") != cid:
            continue
        found = True
        row["portable_snapshot"] = snap
        row["document_family_id"] = meta.get("document_family_id")
        notes = row.get("notes") or ""
        if "operational/context container ported" not in notes:
            row["notes"] = notes.rstrip() + note
        if cid == "BCS-000059":
            row["context_policy"] = (
                "Use only to understand linked Brendon editorial comments. "
                "Do not ingest manuscript prose as Brendon evidence or as BFDM precedent."
            )
    if not found:
        rows.append(
            {
                "corpus_id": cid,
                "legacy_source_id": cid,
                "title": meta.get("title"),
                "project": meta.get("project"),
                "source_role": meta.get("source_role"),
                "source_kind": meta.get("source_kind"),
                "authorship": (meta.get("authorship") or {}).get("status", "UNKNOWN"),
                "authorship_basis": (meta.get("authorship") or {}).get("basis", ""),
                "approximate_source_date": meta.get("created_at"),
                "partition": "DISCOVERY",
                "split_group": meta.get("project_slug"),
                "document_family_id": meta.get("document_family_id"),
                "reliability": "UNASSESSED",
                "review_status": "RECONCILED_UNREVIEWED",
                "context_policy": "Read the container and its source_links. Do not infer live use from preparation.",
                "locators": locator_from_meta(meta),
                "portable_snapshot": snap,
                "notes": note.strip(),
                "record_class": "SOURCE_CONTAINER",
                "related_evidence_ids": [],
                "seed_eligibility": meta.get("seed_eligibility", "PENDING_EVIDENCE_EXTRACTION"),
                "evidence_scope": "RECONCILED_CONTAINER_UNVERIFIED_INTERPRETATION",
            }
        )
    return rows


def bind_essence_channel() -> None:
    path = ROOT / "sources/empire-city/BCS-000001/metadata.json"
    meta = json.loads(path.read_text(encoding="utf-8"))
    locator = "discord://850779382791536640/channel/852796889194954762"
    links = meta.setdefault("source_links", [])
    if not any(link.get("external_locator") == locator for link in links):
        links.append(
            {
                "link_type": "IMPLEMENTED_IN",
                "target_kind": "DISCORD_CHANNEL",
                "external_locator": locator,
                "confidence": "STRONG",
                "basis": (
                    "Empire City #essence-crafting is channel 852796889194954762. "
                    "No other harvested server has a channel by that name. "
                    "Message 862921268666957844 restates this document's post format, "
                    "Sane Magical Prices cost, quality-matched double value, and DM approval before use. "
                    "Later posts use that format and some are marked approved. "
                    "This is the approval step, not proof that harvesting, conversion, or airship upgrades were used as written."
                ),
                "support_refs": [
                    "discord:850779382791536640:862921268666957844",
                    "discord:850779382791536640:862924750561083412",
                    "discord:850779382791536640:865374650828849214",
                ],
            }
        )
    context = meta.setdefault("historical_context", {})
    context["not_established"] = [
        gap(
            "rule_by_rule_live_identity",
            (
                "The approval channel is identified and the posting procedure was used there. "
                "Harvesting checks, conversion in #advanced-crafting, and airship-upgrade rules "
                "are not established by the messages cited on the channel link."
            ),
        )
    ]
    path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


SPECS = build_specs()


def main() -> None:
    rows = catalog_rows()
    written: dict[str, dict] = {}
    for item in SPECS:
        prefix = item["donor_prefix"]
        files: dict[str, bytes] = {}
        for path in git_paths(prefix):
            rel = path[len(prefix) + 1 :]
            if rel == "metadata.json":
                continue
            files[rel] = git_bytes(path)
        dest = ROOT / item["dest_prefix"]
        for rel, data in files.items():
            target = dest / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        meta = build_metadata(item, files, load_donor_meta(item))
        written[item["corpus_id"]] = meta
        rows = upsert_catalog(rows, meta, item["dest_prefix"])
        print(f"ported {item['corpus_id']} files={len(files)}")
    add_url_links(written)
    for cid, meta in written.items():
        dest = ROOT / next(item["dest_prefix"] for item in SPECS if item["corpus_id"] == cid)
        (dest / "metadata.json").write_text(
            json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
    text = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    (ROOT / "evidence" / "catalog.jsonl").write_text(text, encoding="utf-8")
    bind_essence_channel()
    print(f"ported {len(written)} containers")


if __name__ == "__main__":
    main()
