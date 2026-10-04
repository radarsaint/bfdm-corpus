"""Build and load the readable-family index."""

from __future__ import annotations

import json
import re
from pathlib import Path

from access.model import (
    CASE_JSONL,
    FORMAT_VERSION,
    GENERATOR,
    SKIP_RESEARCH_PREFIXES,
    SNOW_RE,
    AccessError,
    Index,
    _assign_catalog_projects,
    _cited_dates,
    _dumps,
    _explicit_messages,
    _ids_in,
    _input_files,
    _inputs_sha256,
    _load_project_index,
    _project_for_path,
    _read_jsonl,
    _sqlite_access,
    make_record,
)

def _read_json(path: Path) -> dict | None:
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def _load_site_captures(repo: Path) -> tuple[dict, dict]:
    """Map Google Sites captures by BCS id and by normalized markdown path."""
    by_corpus: dict[str, dict] = {}
    by_text: dict[str, dict] = {}
    root = repo / "sources"
    if not root.is_dir():
        return by_corpus, by_text
    candidates = list(root.rglob("capture.json"))
    for path in root.rglob("metadata.json"):
        data = _read_json(path)
        if data and data.get("schema_version") == "bfdm_google_site_capture/v1":
            candidates.append(path)
    seen = set()
    for capture_path in sorted(set(candidates)):
        capture = _read_json(capture_path)
        if not capture or capture.get("schema_version") != "bfdm_google_site_capture/v1":
            continue
        key = capture_path.resolve()
        if key in seen:
            continue
        seen.add(key)
        corpus_id = None
        meta = _read_json(capture_path.parent / "metadata.json")
        if meta and meta.get("schema_version") == "bfdm_source_metadata/v1":
            corpus_id = meta.get("corpus_id")
        info = {
            "captured_at": capture.get("captured_at"),
            "corpus_id": corpus_id,
            "limitations": capture.get("limitations") or [],
            "project_id": capture.get("project_id"),
            "role": capture.get("role"),
            "seed_url": capture.get("seed_url"),
            "site_slug": capture.get("site_slug") or capture_path.parent.name,
            "source_family": capture.get("source_family"),
        }
        if corpus_id:
            by_corpus[corpus_id] = info
        for page in capture.get("pages") or []:
            if isinstance(page, dict) and page.get("text_path"):
                by_text[page["text_path"]] = {
                    **info,
                    "fetched_at": page.get("fetched_at"),
                    "page_title": page.get("title"),
                    "raw_path": page.get("raw_path"),
                }
    return by_corpus, by_text


def _catalog_body_path(repo: Path, row: dict) -> Path | None:
    """Return the readable body for a catalog row, preferring markdown or text over HTML."""
    candidates: list[str] = []
    snap = row.get("portable_snapshot")
    if isinstance(snap, str):
        candidates.append(snap)
    elif isinstance(snap, dict):
        for key in ("repo_path", "normalized_path", "text_path"):
            if isinstance(snap.get(key), str):
                candidates.append(snap[key])
    corpus_id = row.get("corpus_id") or ""
    for root_name in ("sources", "context", "evidence"):
        root = repo / root_name
        if not root.is_dir() or not corpus_id:
            continue
        for name in ("source.md", "source.txt"):
            candidates.extend(path.relative_to(repo).as_posix() for path in root.glob(f"**/{corpus_id}/{name}"))
    chosen: list[Path] = []
    for rel in candidates:
        path = repo / rel
        if path.is_file() and path.suffix.lower() in {".md", ".txt"}:
            chosen.append(path)
    if not chosen:
        return None
    chosen.sort(key=lambda path: (0 if path.suffix.lower() == ".md" else 1, path.as_posix()))
    return chosen[0]


def build_index(repo: Path) -> dict:
    repo = repo.resolve()
    project_index = _load_project_index(repo)
    records: list[dict] = []

    for row in project_index["projects"]:
        dates = row.get("dates") or {}
        activity = dates.get("activity_window") or {}
        live = dates.get("live_window") or {}
        planning = dates.get("planning_anchors") or []
        candidates = [item.get("date") for item in planning if isinstance(item, dict)]
        candidates.append((live or {}).get("start") if isinstance(live, dict) else None)
        candidates.append(activity.get("start") if isinstance(activity, dict) else None)
        starts = [item for item in candidates if item]
        ends = []
        if isinstance(live, dict) and live.get("end"):
            ends.append(live["end"])
        if isinstance(activity, dict) and activity.get("end"):
            ends.append(activity["end"])
        text = _dumps(row)
        records.append(
            make_record(
                record_id=row["project_id"],
                record_class="project",
                authority="registry",
                title=row.get("canonical_name") or row.get("title") or row["project_id"],
                project_ids=[row["project_id"]],
                project_labels=[row.get("title") or ""],
                project_resolution="explicit",
                date_start=min(starts) if starts else None,
                date_end=max(ends) if ends else None,
                date_kind="registry" if starts else None,
                path="registry/projects.jsonl",
                body_status="not_applicable",
                cites=_ids_in(text) + _explicit_messages(text),
                text=text,
                attributes={
                    "record_kind": row.get("record_kind"),
                    "status": row.get("status"),
                    "formal_name_status": row.get("formal_name_status"),
                },
            )
        )

    for row in _read_jsonl(repo / "registry" / "series.jsonl"):
        text = _dumps(row)
        records.append(
            make_record(
                record_id=f"series:{row['series_id']}",
                record_class="series",
                authority="registry",
                title=row.get("canonical_name") or row["series_id"],
                project_ids=list(row.get("project_ids") or []),
                project_resolution="explicit",
                path="registry/series.jsonl",
                cites=_ids_in(text),
                text=text,
                attributes={"series_id": row["series_id"]},
            )
        )

    for row in _read_jsonl(repo / "registry" / "project_relations.jsonl"):
        text = _dumps(row)
        records.append(
            make_record(
                record_id=row["relation_id"],
                record_class="project_relation",
                authority="registry",
                title=f"{row['from_project_id']} {row['relation']} {row['to_project_id']}",
                project_ids=[row["from_project_id"], row["to_project_id"]],
                project_resolution="explicit",
                path="registry/project_relations.jsonl",
                cites=_ids_in(text),
                text=text,
                attributes={"relation": row["relation"], "confidence": row.get("confidence")},
            )
        )

    for row in _read_jsonl(repo / "registry" / "people.jsonl"):
        text = _dumps(row)
        records.append(
            make_record(
                record_id=row["person_id"],
                record_class="person",
                authority="registry",
                title=row.get("canonical_name") or row["person_id"],
                path="registry/people.jsonl",
                project_resolution="none",
                cites=_ids_in(text),
                text=text,
                attributes={
                    "person_id": row["person_id"],
                    "canonical_name": row.get("canonical_name"),
                    "aliases": row.get("aliases") or [],
                    "person_kind": row.get("person_kind"),
                },
            )
        )

    for row in _read_jsonl(repo / "registry" / "identities.jsonl"):
        text = _dumps(row)
        project_ids = [row["project_id"]] if row.get("project_id") else []
        records.append(
            make_record(
                record_id=row["identity_id"],
                record_class="identity",
                authority="registry",
                title=row.get("display_name") or row.get("canonical_name") or row["identity_id"],
                project_ids=project_ids,
                project_resolution="explicit" if project_ids else "none",
                date_start=row.get("valid_from"),
                date_end=row.get("valid_to"),
                date_kind="identity_validity" if row.get("valid_from") or row.get("valid_to") else None,
                path="registry/identities.jsonl",
                cites=_ids_in(text) + _explicit_messages(text),
                text=text,
                attributes={
                    "person_id": row.get("person_id"),
                    "platform": row.get("platform"),
                    "account_id": row.get("account_id"),
                    "username": row.get("username"),
                    "display_name": row.get("display_name"),
                    "canonical_name": row.get("canonical_name"),
                    "server_id": row.get("server_id"),
                    "project_id": row.get("project_id"),
                    "confidence": row.get("confidence"),
                    "attribution_use": row.get("attribution_use"),
                },
            )
        )

    for row in _read_jsonl(repo / "registry" / "discord_servers.jsonl"):
        readme_rel = row.get("readme_path") or ""
        readme_text = ""
        readme_path = repo / readme_rel if readme_rel else None
        if readme_path and readme_path.is_file():
            readme_text = readme_path.read_text(encoding="utf-8", errors="replace")
        database_rel = row.get("database_path") or ""
        access = _sqlite_access(repo / database_rel) if database_rel else "missing"
        text = _dumps(row) + "\n" + readme_text
        window = row.get("observed_message_window") or {}
        records.append(
            make_record(
                record_id=f"server:{row.get('server_slug') or row['server_id']}",
                record_class="discord_server",
                authority="harvest_metadata",
                title=f"Discord harvest metadata: {row.get('server_name')}",
                project_ids=list(row.get("project_ids") or []),
                project_labels=[row.get("server_name") or ""],
                project_resolution="explicit",
                date_start=window.get("earliest"),
                date_end=window.get("latest"),
                date_kind="observed_message_window" if window.get("earliest") else None,
                path=readme_rel or "registry/discord_servers.jsonl",
                body_status="not_applicable",
                cites=_ids_in(text) + _explicit_messages(text),
                text=text,
                attributes={
                    "server_id": row.get("server_id"),
                    "server_slug": row.get("server_slug"),
                    "database_path": database_rel,
                    "database_access": access,
                    "message_count_claimed": row.get("message_count"),
                    "harvest_status": row.get("harvest_status"),
                    "searchable_messages": False,
                },
            )
        )

    captures_by_corpus, captures_by_text = _load_site_captures(repo)
    consumed_bodies: set[str] = set()

    for row in _read_jsonl(repo / "evidence" / "catalog.jsonl"):
        corpus_id = row["corpus_id"]
        project_ids, resolution = _assign_catalog_projects(corpus_id, row.get("project") or "", project_index)
        body_path = _catalog_body_path(repo, row)
        capture = captures_by_corpus.get(corpus_id)
        body_text = ""
        if body_path is not None:
            body_text = body_path.read_text(encoding="utf-8", errors="replace")
            consumed_bodies.add(body_path.relative_to(repo).as_posix())
        text = _dumps(row) if not body_text else _dumps(row) + "\n" + body_text
        body_status = "present" if body_path is not None else "catalog_only"
        captured_at = None
        if capture:
            captured_at = capture.get("captured_at")
        records.append(
            make_record(
                record_id=corpus_id,
                record_class="source_container",
                authority="source_catalog",
                title=row.get("title") or corpus_id,
                project_ids=project_ids,
                project_labels=[row.get("project") or ""],
                project_resolution=resolution,
                date_start=row.get("approximate_source_date"),
                date_kind="approximate_source_date" if row.get("approximate_source_date") else None,
                captured_at=captured_at,
                path=body_path.relative_to(repo).as_posix() if body_path is not None else "evidence/catalog.jsonl",
                body_status=body_status,
                cites=_ids_in(text) + _explicit_messages(text),
                text=text,
                attributes={
                    "source_role": row.get("source_role"),
                    "source_kind": row.get("source_kind"),
                    "authorship": row.get("authorship"),
                    "partition": row.get("partition"),
                    "project_label": row.get("project"),
                    "catalog_path": "evidence/catalog.jsonl",
                },
            )
        )

    sources_dir = repo / "evidence" / "sources"
    if sources_dir.is_dir():
        for path in sorted(sources_dir.glob("*")):
            if not path.is_file() or path.suffix.lower() not in {".md", ".txt"}:
                continue
            rel = path.relative_to(repo).as_posix()
            if rel in consumed_bodies:
                continue
            match = re.search(r"(BCS-\d{6})", path.name)
            corpus_id = match.group(1) if match else None
            body = path.read_text(encoding="utf-8", errors="replace")
            records.append(
                make_record(
                    record_id=f"access:snapshot:{corpus_id or path.stem}",
                    record_class="portable_snapshot",
                    authority="normalized_source",
                    title=path.stem,
                    project_resolution="source_anchor" if corpus_id and corpus_id in project_index["anchors"] else "none",
                    project_ids=sorted(project_index["anchors"].get(corpus_id, set())) if corpus_id else [],
                    path=rel,
                    body_status="present",
                    cites=([corpus_id] if corpus_id else []) + _ids_in(body) + _explicit_messages(body),
                    text=body,
                    attributes={"corpus_id": corpus_id},
                )
            )

    for rel, info in sorted(captures_by_text.items()):
        if rel in consumed_bodies:
            continue
        page = repo / rel
        if not page.is_file():
            continue
        body = page.read_text(encoding="utf-8", errors="replace")
        project_id = info.get("project_id")
        site_slug = info.get("site_slug") or "site"
        title = info.get("page_title") or page.stem
        records.append(
            make_record(
                record_id=f"access:site:{project_id or 'unknown'}/{site_slug}/{page.stem}",
                record_class="site_page",
                authority="normalized_source",
                title=title,
                project_ids=[project_id] if project_id else [],
                project_labels=[site_slug],
                project_resolution="explicit" if project_id else "none",
                captured_at=info.get("fetched_at") or info.get("captured_at"),
                path=rel,
                body_status="present",
                cites=_ids_in(body) + _explicit_messages(body),
                text=body,
                attributes={
                    "site_slug": site_slug,
                    "source_family": info.get("source_family"),
                    "role": info.get("role"),
                    "seed_url": info.get("seed_url"),
                    "raw_path": info.get("raw_path"),
                },
            )
        )

    for row in _read_jsonl(repo / "evidence" / "evidence.jsonl"):
        parent = row.get("parent_corpus_id")
        project_ids, resolution = _assign_catalog_projects(parent or "", row.get("project") or "", project_index)
        if parent and parent in project_index["anchors"]:
            project_ids = sorted(set(project_ids) | project_index["anchors"][parent])
            resolution = "source_anchor"
        text = _dumps(row)
        records.append(
            make_record(
                record_id=row["evidence_id"],
                record_class="evidence",
                authority="attributable_evidence",
                title=row.get("title") or row["evidence_id"],
                project_ids=project_ids,
                project_labels=[row.get("project") or ""],
                project_resolution=resolution,
                date_start=row.get("date_start"),
                date_end=row.get("date_end"),
                date_kind="attributable_evidence" if row.get("date_start") else None,
                path="evidence/evidence.jsonl",
                body_status="not_applicable",
                cites=([parent] if parent else []) + _ids_in(text) + _explicit_messages(text),
                text=text,
                attributes={
                    "parent_corpus_id": parent,
                    "evidence_type": row.get("evidence_type"),
                    "authorship": row.get("authorship"),
                    "seed_eligibility": row.get("seed_eligibility"),
                },
            )
        )

    for row in _read_jsonl(repo / "evidence" / "relations.jsonl"):
        text = _dumps(row)
        endpoints = [row.get("from_id"), row.get("to_id")]
        records.append(
            make_record(
                record_id=row["relation_id"],
                record_class="relation",
                authority="relation",
                title=f"{row.get('from_id')} {row.get('relation')} {row.get('to_id')}",
                path="evidence/relations.jsonl",
                cites=[item for item in endpoints if item] + _ids_in(text),
                text=text,
                attributes={"relation": row.get("relation"), "from_id": row.get("from_id"), "to_id": row.get("to_id")},
            )
        )

    skip_snowflakes = set()
    for row in _read_jsonl(repo / "registry" / "identities.jsonl"):
        if row.get("account_id"):
            skip_snowflakes.add(str(row["account_id"]))
    for row in _read_jsonl(repo / "registry" / "discord_servers.jsonl"):
        if row.get("server_id"):
            skip_snowflakes.add(str(row["server_id"]))

    case_stems = set()
    for rel in CASE_JSONL:
        path = repo / rel
        if not path.is_file():
            continue
        case_stems.add(path.with_suffix(".md").relative_to(repo).as_posix())
        project_ids, resolution = _project_for_path(rel)
        for row in _read_jsonl(path):
            case_id = row.get("id")
            if not case_id:
                continue
            text = _dumps(row)
            start, end = _cited_dates(text)
            snow = [f"discord-message:{item}" for item in SNOW_RE.findall(text) if item not in skip_snowflakes]
            records.append(
                make_record(
                    record_id=case_id,
                    record_class="derived_case",
                    authority="derived_case",
                    title=row.get("title") or case_id,
                    project_ids=project_ids,
                    project_resolution=resolution,
                    date_start=start,
                    date_end=end,
                    date_kind="cited_in_case" if start else None,
                    path=rel,
                    body_status="not_applicable",
                    cites=_ids_in(text) + _explicit_messages(text) + snow,
                    text=text,
                    attributes={"schema": row.get("schema"), "confidence": row.get("confidence")},
                )
            )

    chronology = repo / "research" / "roanoke-s3" / "revision-source-chronology-v3.json"
    extra_notes = []
    if chronology.is_file():
        extra_notes.append(chronology)

    research = repo / "research"
    if research.is_dir():
        for path in sorted(research.rglob("*.md")):
            rel = path.relative_to(repo).as_posix()
            if rel.startswith(SKIP_RESEARCH_PREFIXES) or rel in case_stems:
                continue
            extra_notes.append(path)
    for path in extra_notes:
        rel = path.relative_to(repo).as_posix()
        project_ids, resolution = _project_for_path(rel)
        body = path.read_text(encoding="utf-8", errors="replace")
        title = path.stem
        for line in body.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break
        records.append(
            make_record(
                record_id=f"access:note:{rel}",
                record_class="research_note",
                authority="research_note",
                title=title,
                project_ids=project_ids,
                project_resolution=resolution,
                path=rel,
                body_status="present",
                cites=_ids_in(body) + _explicit_messages(body),
                text=body,
            )
        )

    # Optional families are built only when requested at query time by a second pass.
    # Default records stay free of evaluation and imported snapshots.

    _ensure_unique(records)
    records.sort(key=lambda row: (row["record_class"], row["record_id"]))
    files = _input_files(repo)
    manifest = {
        "format_version": FORMAT_VERSION,
        "generator": GENERATOR,
        "inputs_sha256": _inputs_sha256(repo, files),
        "input_count": len(files),
        "record_count": len(records),
        "record_classes": _counts(records, "record_class"),
        "authorities": _counts(records, "authority"),
        "note": "Generated index. Rebuild with python -m access build. Not a canonical source.",
    }
    out = repo / "indexes" / "access"
    out.mkdir(parents=True, exist_ok=True)
    lines = [_dumps(row) for row in records]
    (out / "records.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def _counts(records: list[dict], field: str) -> dict:
    counts: dict[str, int] = {}
    for row in records:
        counts[row[field]] = counts.get(row[field], 0) + 1
    return dict(sorted(counts.items()))


def _ensure_unique(records: list[dict]) -> None:
    seen: dict[str, int] = {}
    for row in records:
        seen[row["record_id"]] = seen.get(row["record_id"], 0) + 1
    duplicates = sorted(key for key, count in seen.items() if count > 1)
    if duplicates:
        raise AccessError(f"Duplicate access record ids: {', '.join(duplicates[:12])}")


def load_index(repo: Path, rebuild: bool = False) -> Index:
    repo = repo.resolve()
    index = Index(repo)
    files = _input_files(repo)
    current_hash = _inputs_sha256(repo, files)
    manifest_path = index.manifest_path()
    fresh = False
    if manifest_path.is_file() and index.records_path().is_file() and not rebuild:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        fresh = manifest.get("inputs_sha256") == current_hash and manifest.get("format_version") == FORMAT_VERSION
    if not fresh:
        build_index(repo)
    index.manifest = json.loads(index.manifest_path().read_text(encoding="utf-8"))
    index.records = _read_jsonl(index.records_path())
    index.by_id = {row["record_id"]: row for row in index.records}
    return index
