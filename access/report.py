"""Coverage statuses and reason codes for one checkout."""

from __future__ import annotations

from pathlib import Path

from access.model import DEFAULT_AUTHORITIES, GENERATOR, _read_jsonl

REASON_CODES = (
    "lfs_pointer_only",
    "missing_readable_projection",
    "external_auth",
    "missing_target",
    "intentionally_excluded",
    "unmerged_workstream",
)

_ATTACHMENT_PROBE = {}


def assess_database_access(access_counts: dict) -> dict:
    """Describe whether database bytes are readable. SQLite itself is not a failure."""
    pointer = int(access_counts.get("git_lfs_pointer") or 0)
    hydrated = int(access_counts.get("hydrated_sqlite") or 0)
    missing = int(access_counts.get("missing") or 0)
    if pointer and not hydrated and not missing:
        return {"bytes": "pointer_only", "coverage": "INACCESSIBLE", "query_path": False, "reasons": ["lfs_pointer_only"]}
    if hydrated and not pointer:
        return {"bytes": "present", "coverage": "NOT_SEARCHED", "query_path": True, "reasons": []}
    if hydrated and pointer:
        return {"bytes": "mixed", "coverage": "PARTIAL", "query_path": True, "reasons": ["lfs_pointer_only"]}
    if missing and not hydrated and not pointer:
        return {"bytes": "missing", "coverage": "INACCESSIBLE", "query_path": False, "reasons": ["missing_target"]}
    if not access_counts:
        return {"bytes": "unknown", "coverage": "UNKNOWN", "query_path": False, "reasons": []}
    return {"bytes": "unknown", "coverage": "UNKNOWN", "query_path": False, "reasons": []}


def _probe_file_bytes(root: Path) -> dict:
    key = str(root.resolve()) if root.exists() else str(root)
    cached = _ATTACHMENT_PROBE.get(key)
    if cached is not None:
        return cached
    pointer = present = 0
    if root.is_dir():
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            head = path.read_bytes()[:30]
            if head.startswith(b"version https://git-lfs"):
                pointer += 1
            elif head:
                present += 1
    result = {"bytes_present": present, "pointer": pointer}
    _ATTACHMENT_PROBE[key] = result
    return result


def _snapshot_claims(row: dict) -> list[str]:
    snap = row.get("portable_snapshot")
    claims = []
    if isinstance(snap, str):
        claims.append(snap)
    elif isinstance(snap, dict):
        for key in ("repo_path", "normalized_path", "text_path"):
            if isinstance(snap.get(key), str):
                claims.append(snap[key])
    return claims


def _has_external_locator(row: dict) -> bool:
    locators = row.get("locators") or {}
    if not isinstance(locators, dict):
        return False
    drive = locators.get("google_drive") or {}
    if isinstance(drive, dict) and (drive.get("url") or drive.get("id")):
        return True
    for value in locators.values():
        if isinstance(value, dict) and isinstance(value.get("url"), str) and value["url"].startswith("http"):
            return True
        if isinstance(value, str) and value.startswith("http"):
            return True
    return False


def _classify_catalog_bodies(repo: Path, records: list[dict]) -> dict:
    indexed = {row["record_id"]: row for row in records if row["record_class"] == "source_container"}
    legacy_ids = {row.get("corpus_id") for row in _read_jsonl(repo / "research" / "legacy-staging" / "manifest.all.jsonl")}
    states = {"body_present": [], "catalog_only": [], "missing_target": []}
    reason_sets = {"catalog_only": set(), "missing_target": {"missing_target"}}
    for row in _read_jsonl(repo / "evidence" / "catalog.jsonl"):
        corpus_id = row["corpus_id"]
        current = indexed.get(corpus_id)
        if current and current["body_status"] == "present":
            states["body_present"].append(corpus_id)
            continue
        claims = _snapshot_claims(row)
        if claims and not any((repo / claim).is_file() for claim in claims):
            states["missing_target"].append(corpus_id)
            continue
        states["catalog_only"].append(corpus_id)
        reason_sets["catalog_only"].add("missing_readable_projection")
        if corpus_id in legacy_ids:
            reason_sets["catalog_only"].add("unmerged_workstream")
        if _has_external_locator(row):
            reason_sets["catalog_only"].add("external_auth")
    if not states["missing_target"]:
        reason_sets["missing_target"] = set()
    return {
        "counts": {name: len(ids) for name, ids in states.items()},
        "reasons": {name: sorted(values) for name, values in reason_sets.items()},
        "sample_ids": {name: sorted(ids)[:12] for name, ids in states.items()},
    }


def _family_report(repo: Path, records: list[dict], scope: dict | None = None) -> list[dict]:
    scope = scope or {}
    include_evaluation = bool(scope.get("include_evaluation"))
    include_imported = bool(scope.get("include_imported"))
    servers = [row for row in records if row["record_class"] == "discord_server"]
    discord_paths = []
    access_counts: dict[str, int] = {}
    for row in servers:
        path = row["attributes"].get("database_path")
        access = row["attributes"].get("database_access")
        if path:
            discord_paths.append(path)
        access_counts[access] = access_counts.get(access, 0) + 1
    database = assess_database_access(access_counts)
    export_path = repo / "indexes" / "discord" / "catalog.json"
    export_present = export_path.is_file()
    if database["bytes"] == "present":
        message_reason = (
            "SQLite database bytes are in this checkout. This command does not query them. "
            "Binary SQLite is not treated as inaccessible. Use retrieval.discord_search when "
            "indexes/discord is present, or query the database directly."
        )
    elif database["bytes"] == "pointer_only":
        message_reason = (
            "The canonical database paths are Git LFS pointers here, so message text cannot be read. "
            "This is lfs_pointer_only, not a property of SQLite."
        )
    elif database["bytes"] == "mixed":
        message_reason = "Some Discord databases are hydrated and some are still Git LFS pointers. This command queries neither."
    elif database["coverage"] == "INACCESSIBLE":
        message_reason = "A registered Discord database path is missing."
    else:
        message_reason = "Discord database access was not verified."
    if export_present:
        export_coverage = "NOT_SEARCHED"
        export_reasons = []
        export_status = "present_not_searched_here"
        export_reason = (
            "indexes/discord/catalog.json is present. Message search belongs to "
            "python -m retrieval.discord_search. This access layer does not query that export."
        )
    else:
        export_coverage = "INACCESSIBLE"
        export_reasons = ["missing_readable_projection", "unmerged_workstream"]
        export_status = "absent"
        export_reason = (
            "No indexes/discord/catalog.json in this checkout. The text projection is developed on "
            "branch ingest/discord-retrieval-v1 and is not merged here. Do not treat a zero from this "
            "tool as absence from the Discord harvests."
        )
    attachment_probe = {"bytes_present": 0, "pointer": 0}
    attachment_roots = []
    discord_root = repo / "discord"
    if discord_root.is_dir():
        attachment_roots = sorted(path / "attachments" for path in discord_root.glob("*") if path.is_dir())
    for attachment_root in attachment_roots:
        probe = _probe_file_bytes(attachment_root)
        attachment_probe["bytes_present"] += probe["bytes_present"]
        attachment_probe["pointer"] += probe["pointer"]
    if attachment_probe["pointer"] and not attachment_probe["bytes_present"]:
        attachment_coverage = "INACCESSIBLE"
        attachment_reasons = ["lfs_pointer_only"]
        attachment_reason = "Attachment paths are Git LFS pointers in this checkout. No text sidecar is searched."
    elif attachment_probe["bytes_present"] and attachment_probe["pointer"]:
        attachment_coverage = "PARTIAL"
        attachment_reasons = ["lfs_pointer_only"]
        attachment_reason = "Some attachment bytes are present and some paths are still LFS pointers. This command does not search attachment contents."
    elif attachment_probe["bytes_present"]:
        attachment_coverage = "NOT_SEARCHED"
        attachment_reasons = ["missing_readable_projection"]
        attachment_reason = "Attachment bytes are present, but this command has no text projection to search."
    else:
        attachment_coverage = "UNKNOWN"
        attachment_reasons = []
        attachment_reason = "No Discord attachment files were found to verify."
    bodies = _classify_catalog_bodies(repo, records)
    drive_reasons = sorted(set(bodies["reasons"]["catalog_only"]) | set(bodies["reasons"]["missing_target"]))
    if bodies["counts"]["body_present"] and (bodies["counts"]["catalog_only"] or bodies["counts"]["missing_target"]):
        drive_coverage = "PARTIAL"
    elif bodies["counts"]["body_present"]:
        drive_coverage = "EXHAUSTIVE"
    elif bodies["counts"]["missing_target"] or bodies["counts"]["catalog_only"]:
        drive_coverage = "INACCESSIBLE"
    else:
        drive_coverage = "UNKNOWN"
    capture_count = len(list((repo / "sources").rglob("capture.json"))) if (repo / "sources").is_dir() else 0
    site_pages = sum(
        1
        for row in records
        if row["record_class"] == "site_page"
        or (row["record_class"] == "source_container" and "google-sites/" in (row.get("path") or "") and row["body_status"] == "present")
    )
    if capture_count and site_pages >= capture_count:
        sites_coverage = "EXHAUSTIVE"
        sites_reasons = []
    elif site_pages:
        sites_coverage = "PARTIAL"
        sites_reasons = ["missing_target"]
    elif capture_count:
        sites_coverage = "INACCESSIBLE"
        sites_reasons = ["missing_readable_projection"]
    else:
        sites_coverage = "UNKNOWN"
        sites_reasons = []
    cases = sum(1 for row in records if row["record_class"] == "derived_case")
    notes = sum(1 for row in records if row["record_class"] == "research_note")
    families = [
        {
            "coverage": "EXHAUSTIVE",
            "family": "registry",
            "reasons": [],
            "reason": "projects, series, people, identities, project relations, and Discord server registry rows.",
            "record_count": sum(1 for row in records if row["authority"] == "registry" or row["record_class"] == "discord_server"),
            "status": "searched",
        },
        {
            "coverage": "EXHAUSTIVE",
            "family": "evidence_registry",
            "reasons": [],
            "reason": "evidence/catalog.jsonl, evidence.jsonl, and relations.jsonl rows are searched. Document bodies are reported separately as drive_bcs_bodies.",
            "record_count": sum(1 for row in records if row["authority"] in {"source_catalog", "attributable_evidence", "relation"} or row["record_class"] == "portable_snapshot"),
            "status": "searched",
        },
        {
            "coverage": sites_coverage,
            "family": "google_sites_markdown",
            "reasons": sites_reasons,
            "reason": "Normalized Google Sites markdown searched on the BCS record when a corpus id exists. Raw HTML is not a second copy.",
            "record_count": site_pages,
            "status": "searched" if site_pages else "absent",
        },
        {
            "coverage": "EXHAUSTIVE" if cases else "UNKNOWN",
            "family": "derived_cases",
            "reasons": [],
            "reason": "JSONL decision/revision cases are searched per id. Empire City cases remain whole-file research notes, not per-case ids.",
            "record_count": cases,
            "status": "searched",
        },
        {
            "coverage": "EXHAUSTIVE" if notes else "UNKNOWN",
            "family": "research_notes",
            "reasons": [],
            "reason": "research markdown outside kit-evaluation and prior-dnd-solo, plus the S3 revision chronology JSON.",
            "record_count": notes,
            "status": "searched",
        },
        {
            "access": database["bytes"],
            "coverage": database["coverage"],
            "database_access_counts": access_counts,
            "family": "discord_messages",
            "paths": discord_paths,
            "query_path": database["query_path"],
            "reasons": database["reasons"],
            "reason": message_reason,
            "status": "not_searched",
        },
        {
            "alternate_command": "python -m retrieval.discord_search search QUERY --campaign CAMPAIGN",
            "coverage": export_coverage,
            "family": "discord_text_export",
            "path": "indexes/discord/catalog.json",
            "reasons": export_reasons,
            "reason": export_reason,
            "status": export_status,
            "workstream": "ingest/discord-retrieval-v1",
        },
        {
            "byte_counts": attachment_probe,
            "coverage": attachment_coverage,
            "family": "discord_attachments",
            "reasons": attachment_reasons,
            "reason": attachment_reason,
            "status": "not_searched",
        },
        {
            "bodies_present": bodies["counts"]["body_present"],
            "catalog_count": sum(bodies["counts"].values()),
            "catalog_only": bodies["counts"]["catalog_only"],
            "coverage": drive_coverage,
            "family": "drive_bcs_bodies",
            "legacy_manifest_count": len({row.get("corpus_id") for row in _read_jsonl(repo / "research" / "legacy-staging" / "manifest.all.jsonl")}),
            "missing_target": bodies["counts"]["missing_target"],
            "reasons": drive_reasons,
            "reason": (
                f"{bodies['counts']['body_present']} BCS containers were searched with a local body. "
                f"{bodies['counts']['catalog_only']} were metadata only. "
                f"{bodies['counts']['missing_target']} name a body path that is not in the checkout. "
                "Metadata matches are not document-body matches. Reconciliation of the missing legacy bodies is on ingest/drive-project-v3."
            ),
            "reason_scope": "non_present_states_only",
            "sample_ids": bodies["sample_ids"],
            "states": [
                {"count": bodies["counts"]["body_present"], "searched": True, "state": "body_present"},
                {
                    "count": bodies["counts"]["catalog_only"],
                    "reasons": bodies["reasons"]["catalog_only"],
                    "sample_ids": bodies["sample_ids"]["catalog_only"],
                    "searched": False,
                    "state": "catalog_only",
                },
                {
                    "count": bodies["counts"]["missing_target"],
                    "reasons": bodies["reasons"]["missing_target"],
                    "sample_ids": bodies["sample_ids"]["missing_target"],
                    "searched": False,
                    "state": "missing_target",
                },
            ],
            "status": "partial_catalog_only" if bodies["counts"]["catalog_only"] else "searched",
        },
        {
            "coverage": "EXHAUSTIVE" if include_evaluation else "EXCLUDED",
            "family": "kit_evaluation",
            "path": "research/kit-evaluation/",
            "reasons": [] if include_evaluation else ["intentionally_excluded"],
            "reason": "Included in this query." if include_evaluation else "Present on disk and intentionally excluded from the default search. Pass --include-evaluation. Exclusion is not inaccessibility.",
            "status": "searched" if include_evaluation else "not_in_default_search",
        },
        {
            "coverage": "EXHAUSTIVE" if include_imported else "EXCLUDED",
            "family": "prior_dnd_solo_import",
            "path": "research/prior-dnd-solo/",
            "reasons": [] if include_imported else ["intentionally_excluded"],
            "reason": "Included in this query." if include_imported else "Present on disk and intentionally excluded from the default search. Pass --include-imported.",
            "status": "searched" if include_imported else "not_in_default_search",
        },
        {
            "coverage": "EXHAUSTIVE",
            "family": "campaigns_directory",
            "reasons": [],
            "reason": "campaigns/ was inspected. It holds registry guidance, not a hidden document store.",
            "status": "empty_pointer",
        },
    ]
    return families


def _coverage_report(families: list[dict]) -> dict:
    searched = [row["family"] for row in families if row["coverage"] == "EXHAUSTIVE"]
    partial = [row["family"] for row in families if row["coverage"] == "PARTIAL"]
    omitted = []
    for row in families:
        if row["coverage"] in {"INACCESSIBLE", "NOT_SEARCHED", "EXCLUDED", "UNKNOWN"}:
            omitted.append(
                {
                    "coverage": row["coverage"],
                    "family": row["family"],
                    "impact": row.get("reason"),
                    "reasons": row.get("reasons") or [],
                }
            )
    coverages = {row["coverage"] for row in families}
    if coverages and coverages <= {"EXHAUSTIVE"}:
        status = "EXHAUSTIVE"
    elif coverages and coverages <= {"INACCESSIBLE"}:
        status = "INACCESSIBLE"
    elif coverages and coverages <= {"UNKNOWN"}:
        status = "UNKNOWN"
    elif not families:
        status = "UNKNOWN"
    else:
        status = "PARTIAL"
    gaps = []
    export = next((row for row in families if row["family"] == "discord_text_export"), None)
    if export and export["coverage"] != "EXHAUSTIVE":
        gaps.append(
            {
                "family": "discord_text_export",
                "id": "discord_text_export",
                "reasons": export.get("reasons") or [],
                "workstream": "ingest/discord-retrieval-v1",
            }
        )
    drive = next((row for row in families if row["family"] == "drive_bcs_bodies"), None)
    if drive and drive["coverage"] == "PARTIAL":
        gaps.append(
            {
                "family": "drive_bcs_bodies",
                "id": "legacy_drive_bodies",
                "reasons": sorted(set(drive.get("reasons") or []) & {"missing_readable_projection", "unmerged_workstream", "external_auth", "missing_target"}),
                "workstream": "ingest/drive-project-v3",
            }
        )
    return {
        "gaps": gaps,
        "omitted_families": omitted,
        "partial_families": partial,
        "reason_codes": list(REASON_CODES),
        "searched_families": searched,
        "status": status,
        "zero_match_means_absence": status == "EXHAUSTIVE",
    }


def _coverage(repo: Path, records: list[dict], scope: dict | None = None) -> dict:
    families = _family_report(repo, records, scope)
    report = _coverage_report(families)
    return {
        "absence_is_not_evidence": not report["zero_match_means_absence"],
        "coverage_report": report,
        "default_authorities": list(DEFAULT_AUTHORITIES),
        "families": families,
        "indexed_record_count": len(records),
        "query_scope": scope or {"authorities": list(DEFAULT_AUTHORITIES), "include_evaluation": False, "include_imported": False, "project": None},
        "tool": GENERATOR,
    }
