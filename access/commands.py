"""Query commands over a loaded access index."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from access.build import load_index
from access.model import (
    DEFAULT_AUTHORITIES,
    AccessError,
    Index,
    _fold,
    _ids_in,
    _load_project_index,
    make_record,
    repo_root_from,
    resolve_project,
)
from access.report import _coverage

def _optional_records(repo: Path, include_evaluation: bool, include_imported: bool) -> list[dict]:
    if not include_evaluation and not include_imported:
        return []
    roots = []
    if include_evaluation:
        roots.append(repo / "research" / "kit-evaluation")
    if include_imported:
        roots.append(repo / "research" / "prior-dnd-solo")
    records = []
    for root in roots:
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in {".md", ".json", ".jsonl", ".txt"}:
                continue
            rel = path.relative_to(repo).as_posix()
            try:
                body = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            kind = "evaluation" if rel.startswith("research/kit-evaluation/") else "imported_snapshot"
            records.append(
                make_record(
                    record_id=f"access:{kind}:{rel}",
                    record_class=kind,
                    authority=kind,
                    title=path.name,
                    path=rel,
                    body_status="present",
                    project_resolution="none",
                    cites=_ids_in(body),
                    text=body,
                )
            )
    return records


def _public(row: dict, full: bool = False) -> dict:
    data = {key: row[key] for key in row if key != "text"}
    if full:
        data["text"] = row.get("text") or ""
    return data


def _snippet(text: str, tokens: list[str], phrase: str | None) -> str:
    folded = _fold(text)
    needle = phrase or (tokens[0] if tokens else "")
    at = folded.find(needle) if needle else -1
    if at < 0 and tokens:
        for token in tokens:
            at = folded.find(token)
            if at >= 0:
                break
    if at < 0:
        clip = text[:280]
    else:
        start = max(0, at - 120)
        end = min(len(text), at + 160)
        # Folded offsets can diverge from original when accents are stripped.
        # The corpora are mostly ASCII; fall back to the head if the slice looks empty.
        clip = text[start:end] if start < len(text) else text[:280]
    clip = re.sub(r"\s+", " ", clip).strip()
    return clip[:360]


def _tokens(query: str) -> list[str]:
    parts = []
    for raw in query.split():
        token = raw.strip(" \t\r\n.,;:!?()[]{}<>\"'`")
        if token:
            parts.append(_fold(token))
    return parts


def _matches_project(row: dict, project_id: str | None) -> bool:
    if not project_id:
        return True
    return project_id in row["project_ids"]


def _search_rows(rows: list[dict], query: str, project_id: str | None, limit: int, full: bool) -> dict:
    phrase = None
    stripped = query.strip()
    if len(stripped) >= 2 and stripped[0] == stripped[-1] and stripped[0] in {"'", '"'}:
        phrase = _fold(stripped[1:-1])
        tokens = _tokens(stripped[1:-1])
    else:
        tokens = _tokens(stripped)
    if not tokens and not phrase:
        raise AccessError("Empty query.")
    exact_ids = {row["record_id"] for row in rows if row["record_id"] == stripped or _fold(row["record_id"]) == _fold(stripped)}
    hits = []
    ambiguous_excluded = 0
    for row in rows:
        folded = _fold(row["record_id"] + "\n" + row["title"] + "\n" + row["text"])
        match = None
        if row["record_id"] in exact_ids:
            match = "record_id"
            score = 1000
        elif phrase and phrase in folded:
            match = "phrase"
            score = folded.count(phrase)
        elif tokens and all(token in folded for token in tokens):
            match = "terms"
            score = sum(folded.count(token) for token in tokens)
        else:
            continue
        if project_id and not _matches_project(row, project_id):
            if row.get("project_resolution") in {"ambiguous_label", "unmapped_label", "filename_span"}:
                ambiguous_excluded += 1
            continue
        hit = _public(row, full=full)
        hit["match"] = match
        hit["score"] = score
        hit["snippet"] = _snippet(row["text"], tokens, phrase)
        hits.append(hit)
    hits.sort(key=lambda item: (0 if item["match"] == "record_id" else 1, -item["score"], item["record_id"]))
    total = len(hits)
    return {
        "ambiguous_label_excluded": ambiguous_excluded if project_id else 0,
        "hits": hits[:limit],
        "returned": min(limit, total),
        "total": total,
    }


def _scope(project_id, authorities, include_evaluation, include_imported, ambiguous_excluded) -> dict:
    return {
        "ambiguous_label_excluded": ambiguous_excluded,
        "authorities": list(authorities),
        "include_evaluation": include_evaluation,
        "include_imported": include_imported,
        "project": project_id,
    }


def _rows_for(index: Index, authorities: tuple[str, ...] | list[str], include_evaluation: bool, include_imported: bool) -> list[dict]:
    allowed = set(authorities)
    if include_evaluation:
        allowed.add("evaluation")
    if include_imported:
        allowed.add("imported_snapshot")
    rows = [row for row in index.records if row["authority"] in allowed]
    if include_evaluation or include_imported:
        rows.extend(row for row in _optional_records(index.repo, include_evaluation, include_imported) if row["authority"] in allowed)
    return rows


def search(repo, query, project=None, authorities=None, limit=20, full=False, include_evaluation=False, include_imported=False, rebuild=False):
    index = load_index(Path(repo), rebuild=rebuild)
    project_index = _load_project_index(index.repo)
    project_id = resolve_project(project, project_index) if project else None
    allowed = tuple(authorities or DEFAULT_AUTHORITIES)
    rows = _rows_for(index, allowed, include_evaluation, include_imported)
    found = _search_rows(rows, query, project_id, limit, full)
    scope = _scope(project_id, allowed, include_evaluation, include_imported, found["ambiguous_label_excluded"])
    return {
        "coverage": _coverage(index.repo, index.records, scope),
        "hits": found["hits"],
        "project": project_id,
        "query": query,
        "returned": found["returned"],
        "total": found["total"],
    }


def _identity_labels(row: dict) -> list[str]:
    attrs = row.get("attributes") or {}
    labels = [
        row["record_id"],
        row.get("title") or "",
        attrs.get("canonical_name") or "",
        attrs.get("display_name") or "",
        attrs.get("username") or "",
        attrs.get("person_id") or "",
        attrs.get("account_id") or "",
    ]
    for alias in attrs.get("aliases") or []:
        if isinstance(alias, dict):
            labels.append(alias.get("name") or "")
        elif isinstance(alias, str):
            labels.append(alias)
    return [item for item in labels if item]


def _name_match(query: str, label: str) -> str | None:
    needle = _fold(query.strip())
    folded = _fold(label)
    if not needle or not folded:
        return None
    if needle == folded:
        return "exact"
    if needle in folded.split():
        return "token"
    if len(needle) >= 4 and needle in folded:
        return "substring"
    return None


def entity(repo, name, limit=15, rebuild=False):
    index = load_index(Path(repo), rebuild=rebuild)
    people = [row for row in index.records if row["record_class"] == "person"]
    identities = [row for row in index.records if row["record_class"] == "identity"]
    matched_people = []
    for row in people:
        kinds = {kind for label in _identity_labels(row) if (kind := _name_match(name, label))}
        if kinds:
            best = "exact" if "exact" in kinds else "token" if "token" in kinds else "substring"
            item = _public(row)
            item["match"] = best
            matched_people.append(item)
    matched_person_ids = {row["record_id"] for row in people if any(_name_match(name, label) for label in _identity_labels(row))}
    matched_identities = []
    for row in identities:
        kinds = {kind for label in _identity_labels(row) if (kind := _name_match(name, label))}
        person_id = (row.get("attributes") or {}).get("person_id")
        if person_id in matched_person_ids or kinds:
            best = "exact" if "exact" in kinds else "token" if "token" in kinds else "substring" if "substring" in kinds else "person"
            item = _public(row)
            item["match"] = best
            matched_identities.append(item)
    person_ids = {item["record_id"] for item in matched_people}
    person_ids.update((item.get("attributes") or {}).get("person_id") for item in matched_identities)
    person_ids.discard(None)
    if matched_identities and not matched_people:
        for row in people:
            if row["record_id"] in person_ids:
                item = _public(row)
                item["match"] = "via_identity"
                matched_people.append(item)
    mentions = search(index.repo, name, limit=limit)
    return {
        "ambiguous": len(person_ids) > 1,
        "coverage": mentions["coverage"],
        "identities": matched_identities,
        "identity_note": (
            "Registry identity rows are scoped assertions with their own confidence and attribution_use. "
            "Text mentions are not identity assertions. Discord message text was not searched."
        ),
        "mentions": mentions["hits"],
        "mention_total": mentions["total"],
        "people": matched_people,
        "query": name,
    }


def sources(repo, project, rebuild=False):
    index = load_index(Path(repo), rebuild=rebuild)
    project_index = _load_project_index(index.repo)
    project_id = resolve_project(project, project_index)
    project_row = index.by_id.get(project_id)
    selected = [row for row in index.records if project_id in row["project_ids"]]
    ambiguous = [
        row
        for row in index.records
        if row["project_resolution"] in {"ambiguous_label", "unmapped_label"}
        and project_id.startswith("roanoke")
        and "roanoke" in _fold(" ".join(row.get("project_labels") or []))
    ]

    def pack(rows, limit=None):
        packed = [_public(row) for row in rows]
        packed.sort(key=lambda item: (item.get("date_start") or "9999", item["record_id"]))
        return packed if limit is None else packed[:limit]

    containers = [row for row in selected if row["record_class"] == "source_container"]
    sites = [row for row in selected if row["record_class"] == "site_page"]
    cases = [row for row in selected if row["record_class"] == "derived_case"]
    notes = [row for row in selected if row["record_class"] == "research_note"]
    servers = [row for row in selected if row["record_class"] == "discord_server"]
    evidence_rows = [row for row in selected if row["record_class"] == "evidence"]
    scope = _scope(project_id, DEFAULT_AUTHORITIES, False, False, len(ambiguous))
    return {
        "counts": {
            "derived_cases": len(cases),
            "discord_servers": len(servers),
            "evidence": len(evidence_rows),
            "research_notes": len(notes),
            "site_pages": len(sites),
            "source_containers": len(containers),
        },
        "coverage": _coverage(index.repo, index.records, scope),
        "derived_cases": pack(cases),
        "discord_servers": pack(servers),
        "evidence": pack(evidence_rows),
        "omitted_ambiguous_catalog": {
            "count": len(ambiguous),
            "reason": "Rows whose project label is only 'Roanoke' (or otherwise unmapped) are omitted from a season slice unless a registry source_anchor names that BCS id.",
            "sample_ids": [row["record_id"] for row in ambiguous[:15]],
        },
        "project": _public(project_row) if project_row else {"record_id": project_id},
        "project_id": project_id,
        "research_notes": pack(notes),
        "site_pages": pack(sites),
        "source_containers": pack(containers),
    }


def _resolve_cite(index: Index, cite: str) -> dict:
    row = index.by_id.get(cite)
    if row:
        return {"body_status": row["body_status"], "cite": cite, "kind": "record", "record": _public(row)}
    if cite.startswith("discord-message:"):
        return {
            "body_status": "inaccessible",
            "cite": cite,
            "kind": "discord_message_candidate",
            "reason": "Candidate snowflake extracted from a derived record or an explicit discord-message: reference. This tool did not open the Discord database, so the id is not confirmed as a message id and the message text was not retrieved.",
        }
    return {"body_status": "unknown", "cite": cite, "kind": "unresolved", "reason": "No indexed record uses this id."}


def evidence(repo, record_id, rebuild=False):
    index = load_index(Path(repo), rebuild=rebuild)
    row = index.by_id.get(record_id)
    if not row:
        folded = _fold(record_id)
        hits = [item for item in index.records if _fold(item["record_id"]) == folded]
        if len(hits) == 1:
            row = hits[0]
        elif len(hits) > 1:
            raise AccessError(f"Ambiguous id '{record_id}'.", code="ambiguous_id")
    cited_by = []
    if row:
        cited_by = [_public(item) for item in index.records if row["record_id"] in item["cites"]]
        cited_by.sort(key=lambda item: item["record_id"])
    resolved = []
    if row:
        resolved = [_resolve_cite(index, cite) for cite in row["cites"]]
    scope = _scope(None, DEFAULT_AUTHORITIES, False, False, 0)
    return {
        "cited_by": cited_by,
        "cites_resolved": resolved,
        "coverage": _coverage(index.repo, index.records, scope),
        "found": row is not None,
        "query_id": record_id,
        "record": _public(row, full=True) if row else None,
    }


def related(repo, record_id, rebuild=False):
    found = evidence(repo, record_id, rebuild=rebuild)
    if not found["found"]:
        return found | {"links": []}
    links = []
    for item in found["cites_resolved"]:
        if item["kind"] == "record":
            links.append({"direction": "outgoing", "record": item["record"], "via": "cites"})
        else:
            links.append({"direction": "outgoing", "unresolved": item, "via": "cites"})
    for item in found["cited_by"]:
        links.append({"direction": "incoming", "record": item, "via": "cited_by"})
    return {
        "coverage": found["coverage"],
        "found": True,
        "links": links,
        "query_id": found["record"]["record_id"],
        "record": found["record"],
    }


def timeline(repo, query, project=None, limit=40, rebuild=False):
    found = search(repo, query, project=project, limit=200, full=False, rebuild=rebuild)
    dated = []
    undated = []
    capture_only = []
    for hit in found["hits"]:
        # search() already limited to 200; re-query without the cap by using the index directly if needed.
        if hit.get("date_start"):
            dated.append(hit)
        elif hit.get("captured_at"):
            capture_only.append(hit)
        else:
            undated.append(hit)
    # The search call capped hits. For timeline, run a higher internal limit.
    if found["total"] > found["returned"]:
        found = search(repo, query, project=project, limit=max(found["total"], limit), full=False, rebuild=False)
        dated, undated, capture_only = [], [], []
        for hit in found["hits"]:
            if hit.get("date_start"):
                dated.append(hit)
            elif hit.get("captured_at"):
                capture_only.append(hit)
            else:
                undated.append(hit)
    dated.sort(key=lambda item: (item["date_start"], item["record_id"]))
    capture_only.sort(key=lambda item: (item.get("captured_at") or "", item["record_id"]))
    return {
        "coverage": found["coverage"],
        "capture_time_only": capture_only[:limit],
        "dated": dated[:limit],
        "date_note": (
            "dated rows use registry dates, attributable-evidence dates, or ISO dates cited inside "
            "decision-case JSON. Research-note prose is not date-mined. Google Sites fetched_at values "
            "are archive capture times, not historical event dates, and are listed separately."
        ),
        "project": found["project"],
        "query": query,
        "undated_count": len(undated),
        "undated_ids": [item["record_id"] for item in undated[:limit]],
    }


def export_bundle(repo, query, project=None, limit=30, out_path: Path | None = None, rebuild=False):
    found = search(repo, query, project=project, limit=limit, full=False, rebuild=rebuild)
    index = load_index(Path(repo), rebuild=False)
    provenance = []
    seen = set()
    for hit in found["hits"]:
        row = index.by_id.get(hit["record_id"])
        if not row:
            continue
        for cite in row["cites"]:
            if cite in seen or len(provenance) >= 80:
                continue
            seen.add(cite)
            provenance.append(_resolve_cite(index, cite))
    bundle = {
        "bundle_type": "bfdm_access_export/v1",
        "coverage": found["coverage"],
        "hits": found["hits"],
        "project": found["project"],
        "provenance": provenance,
        "query": query,
        "returned": found["returned"],
        "total": found["total"],
    }
    if out_path:
        destination = Path(out_path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(bundle, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        bundle["wrote"] = str(destination)
    return bundle


def coverage(repo, rebuild=False):
    index = load_index(Path(repo), rebuild=rebuild)
    return _coverage(index.repo, index.records)


def _excluded_file_count(repo: Path) -> dict:
    counts = {}
    for name in ("research/kit-evaluation", "research/prior-dnd-solo"):
        root = repo / name
        counts[name] = sum(1 for path in root.rglob("*") if path.is_file()) if root.is_dir() else 0
    return counts


def audit(repo, rebuild=False):
    index = load_index(Path(repo), rebuild=rebuild)
    report = _coverage(index.repo, index.records)
    records = index.records
    return {
        "counts": {
            "catalog_only_records": sum(1 for row in records if row["body_status"] == "catalog_only"),
            "databases_with_bytes": sum(1 for row in records if row["record_class"] == "discord_server" and row["attributes"].get("database_access") == "hydrated_sqlite"),
            "excluded_files": _excluded_file_count(index.repo),
            "inaccessible_databases": sum(1 for row in records if row["record_class"] == "discord_server" and row["attributes"].get("database_access") == "git_lfs_pointer"),
            "indexed_records": len(records),
            "searchable_records": sum(1 for row in records if row["body_status"] in {"present", "not_applicable"}),
        },
        "coverage_report": report["coverage_report"],
        "families": [
            {
                "coverage": row["coverage"],
                "family": row["family"],
                "reasons": row.get("reasons") or [],
                "status": row["status"],
            }
            for row in report["families"]
        ],
        "gaps": report["coverage_report"]["gaps"],
    }


def record(repo, record_id, rebuild=False):
    found = evidence(repo, record_id, rebuild=rebuild)
    return {"coverage": found["coverage"], "found": found["found"], "record": found["record"]}


def _print(payload) -> None:
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2, sort_keys=True)
    sys.stdout.write("\n")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="access", description="Query readable BFDM corpus families. Discord message bodies are not searched.")
    parser.add_argument("--repo", type=Path, default=None)
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("build")
    sub.add_parser("coverage")
    sub.add_parser("audit")

    search_parser = sub.add_parser("search")
    search_parser.add_argument("query")
    search_parser.add_argument("--project")
    search_parser.add_argument("--authority", action="append", dest="authorities")
    search_parser.add_argument("--limit", type=int, default=20)
    search_parser.add_argument("--full", action="store_true")
    search_parser.add_argument("--include-evaluation", action="store_true")
    search_parser.add_argument("--include-imported", action="store_true")

    entity_parser = sub.add_parser("entity")
    entity_parser.add_argument("name")
    entity_parser.add_argument("--limit", type=int, default=15)

    sources_parser = sub.add_parser("sources")
    sources_parser.add_argument("project")

    for name in ("evidence", "related", "record"):
        item = sub.add_parser(name)
        item.add_argument("record_id")

    timeline_parser = sub.add_parser("timeline")
    timeline_parser.add_argument("query")
    timeline_parser.add_argument("--project")
    timeline_parser.add_argument("--limit", type=int, default=40)

    export_parser = sub.add_parser("export")
    export_parser.add_argument("query")
    export_parser.add_argument("--project")
    export_parser.add_argument("--limit", type=int, default=30)
    export_parser.add_argument("--out", type=Path)

    args = parser.parse_args(argv)
    try:
        root = Path(args.repo).resolve() if args.repo else repo_root_from(Path.cwd())
        if args.cmd == "build":
            _print(build_index(root))
        elif args.cmd == "coverage":
            _print(coverage(root))
        elif args.cmd == "audit":
            _print(audit(root))
        elif args.cmd == "search":
            _print(
                search(
                    root,
                    args.query,
                    project=args.project,
                    authorities=args.authorities,
                    limit=args.limit,
                    full=args.full,
                    include_evaluation=args.include_evaluation,
                    include_imported=args.include_imported,
                )
            )
        elif args.cmd == "entity":
            _print(entity(root, args.name, limit=args.limit))
        elif args.cmd == "sources":
            _print(sources(root, args.project))
        elif args.cmd == "evidence":
            _print(evidence(root, args.record_id))
        elif args.cmd == "related":
            _print(related(root, args.record_id))
        elif args.cmd == "record":
            _print(record(root, args.record_id))
        elif args.cmd == "timeline":
            _print(timeline(root, args.query, project=args.project, limit=args.limit))
        elif args.cmd == "export":
            _print(export_bundle(root, args.query, project=args.project, limit=args.limit, out_path=args.out))
        else:
            raise AccessError(f"Unknown command {args.cmd}")
    except AccessError as exc:
        json.dump({"error": exc.code, "message": str(exc)}, sys.stderr, ensure_ascii=False)
        sys.stderr.write("\n")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
