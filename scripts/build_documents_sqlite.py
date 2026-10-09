#!/usr/bin/env python3
"""Rebuild indexes/documents.sqlite from source containers.

The database is a derivative index. Human-readable containers remain canonical.

Timestamp rule: source_containers.modified_at and the current
document_versions.modified_at use native_dates.modified when that value is
present, otherwise the top-level modified_at or modified_timestamp.

Comment rule: comments.jsonl, comments.json, and brendon-comments.native.json
are loaded into comments and comments_fts. A provider id from the sidecar is
stored as native_comment_id. If the sidecar has no id, comment_key is a
deterministic local key and native_comment_id stays null.

Revision rule: revisions.jsonl rows become document_versions. A body file is
indexed only when the sidecar says it was fetched and the file is in the
container. Rows without a body are stored as NOT_FETCHED. Their text is not
invented. Revision bodies that were never retrieved remain absent.

Not indexed here: context containers such as BCS-000059, because this builder
only scans sources/. BCS-000068 has no source container.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def authorship_status(meta: dict) -> str:
    authorship = meta.get("authorship")
    if isinstance(authorship, dict):
        return str(authorship.get("status") or "UNKNOWN")
    if isinstance(authorship, str) and authorship:
        return authorship
    return "UNKNOWN"


def authorship_basis(meta: dict) -> str | None:
    authorship = meta.get("authorship")
    if isinstance(authorship, dict):
        return authorship.get("basis")
    return meta.get("authorship_basis")


def authorship_object(meta: dict) -> dict:
    authorship = meta.get("authorship")
    return authorship if isinstance(authorship, dict) else {}


def attribution_fields(meta: dict) -> tuple[str | None, str | None, str | None, str | None, str | None]:
    authorship = authorship_object(meta)
    attribution = authorship.get("attribution")
    attribution = attribution if isinstance(attribution, dict) else {}
    archival = meta.get("archival_provenance")
    archival = archival if isinstance(archival, dict) else {}
    return (
        authorship.get("creator"),
        authorship.get("copyright_owner"),
        attribution.get("basis_kind"),
        attribution.get("attested_on"),
        archival.get("status"),
    )


def native_dates(meta: dict) -> dict:
    value = meta.get("native_dates")
    return value if isinstance(value, dict) else {}


def container_modified_at(meta: dict) -> str | None:
    modified = native_dates(meta).get("modified")
    if modified:
        return modified
    return meta.get("modified_at") or meta.get("modified_timestamp")


def container_created_at(meta: dict) -> str | None:
    created = native_dates(meta).get("created")
    if created:
        return created
    return meta.get("created_at") or meta.get("created_timestamp")


def load_records(repo: Path) -> list[tuple[Path, dict]]:
    records = []
    for meta_path in sorted((repo / "sources").glob("**/metadata.json")):
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        records.append((meta_path, meta))
    return records


def primary_body(repo: Path, meta: dict, meta_path: Path) -> Path | None:
    for key in ("source_body_path", "current_source_body_path"):
        if meta.get(key):
            path = repo / meta[key]
            if path.exists():
                return path
    sibling = meta_path.parent / "source.md"
    if sibling.exists():
        return sibling
    return None


def author_name(value) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    if isinstance(value, dict):
        name = value.get("displayName") or value.get("name")
        if isinstance(name, str) and name.strip():
            return name.strip()
    return None


def author_is_self(value) -> int | None:
    if isinstance(value, dict) and "me" in value:
        return 1 if value.get("me") else 0
    return None


def flag(value) -> int | None:
    if value is True:
        return 1
    if value is False:
        return 0
    return None


def quoted_text(row: dict) -> str | None:
    quoted = row.get("quoted")
    if isinstance(quoted, str) and quoted.strip():
        return quoted
    quoted_file = row.get("quotedFileContent")
    if isinstance(quoted_file, dict):
        value = quoted_file.get("value")
        if isinstance(value, str) and value.strip():
            return value
    parts = []
    for anchor in row.get("anchors") or []:
        if not isinstance(anchor, dict):
            continue
        for para in anchor.get("paragraphs") or []:
            if isinstance(para, dict) and isinstance(para.get("text"), str) and para["text"].strip():
                if not parts or parts[-1] != para["text"]:
                    parts.append(para["text"])
    if parts:
        return "\n".join(parts)
    return None


def comment_record(row: dict, cid: str, sidecar: str, index: int, provider: str, parent_native: str | None = None) -> dict | None:
    content = row.get("content")
    if not isinstance(content, str):
        content = row.get("text")
    if not isinstance(content, str) or not content.strip():
        return None
    native = row.get("id")
    native_id = str(native) if native not in (None, "") else None
    if native_id:
        key = f"{cid}:{provider}:{native_id}"
    else:
        key = f"{cid}:{sidecar}:local:{index:04d}"
    return {
        "comment_key": key,
        "provider": provider,
        "native_comment_id": native_id,
        "parent_native_id": parent_native,
        "author_display_name": author_name(row.get("author")),
        "author_is_self": author_is_self(row.get("author")),
        "created_at": row.get("createdTime") or row.get("created") or row.get("date"),
        "modified_at": row.get("modifiedTime") or row.get("modified"),
        "resolved": flag(row.get("resolved")),
        "deleted": flag(row.get("deleted")),
        "quoted_context": quoted_text(row),
        "content": content,
        "metadata_json": json.dumps(
            {
                "sidecar": sidecar,
                "record_type": row.get("record_type"),
                "action": row.get("action"),
                "capture": row.get("capture"),
            },
            ensure_ascii=False,
        ),
    }


def load_comments(container: Path, cid: str) -> tuple[list[dict], list[str]]:
    warnings = []
    records: list[dict] = []

    jsonl = container / "comments.jsonl"
    if jsonl.exists():
        for index, line in enumerate(jsonl.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                warnings.append(f"{jsonl.name}:{index} is not JSON ({exc})")
                continue
            if not isinstance(row, dict):
                warnings.append(f"{jsonl.name}:{index} is not an object")
                continue
            provider = "docx_export" if "text" in row and "content" not in row and "id" not in row else "google_drive"
            parent = row.get("parent_comment_id")
            parent_native = str(parent) if parent else None
            item = comment_record(row, cid, jsonl.name, index, provider, parent_native)
            if item:
                records.append(item)

    comments_json = container / "comments.json"
    if comments_json.exists():
        try:
            payload = json.loads(comments_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            warnings.append(f"comments.json is not JSON ({exc})")
            payload = None
        rows = []
        if isinstance(payload, dict):
            rows = payload.get("comments") or []
        elif isinstance(payload, list):
            rows = payload
        if not isinstance(rows, list):
            warnings.append("comments.json has no comment list")
            rows = []
        for index, row in enumerate(rows, 1):
            if not isinstance(row, dict):
                continue
            item = comment_record(row, cid, comments_json.name, index, "docx_export")
            if item:
                records.append(item)

    native = container / "brendon-comments.native.json"
    if native.exists():
        try:
            payload = json.loads(native.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            warnings.append(f"brendon-comments.native.json is not JSON ({exc})")
            payload = None
        rows = payload.get("comments") if isinstance(payload, dict) else None
        if not isinstance(rows, list):
            if payload is not None:
                warnings.append("brendon-comments.native.json has no comment list")
            rows = []
        for index, row in enumerate(rows, 1):
            if not isinstance(row, dict):
                continue
            item = comment_record(row, cid, native.name, index, "google_drive")
            if item:
                records.append(item)
                for reply_index, reply in enumerate(row.get("replies") or [], 1):
                    if not isinstance(reply, dict):
                        continue
                    reply_row = dict(reply)
                    reply_item = comment_record(
                        reply_row,
                        cid,
                        native.name,
                        index * 100 + reply_index,
                        "google_drive",
                        item["native_comment_id"],
                    )
                    if reply_item and reply_item["native_comment_id"] is None:
                        reply_item["comment_key"] = f"{item['comment_key']}:reply:{reply_index:02d}"
                    if reply_item:
                        records.append(reply_item)
    return records, warnings


def dedupe_comment_keys(records: list[dict]) -> list[dict]:
    seen = set()
    kept = []
    for record in records:
        key = record["comment_key"]
        if key in seen:
            suffix = 2
            while f"{key}:{suffix}" in seen:
                suffix += 1
            record["comment_key"] = f"{key}:{suffix}"
            key = record["comment_key"]
        seen.add(key)
        kept.append(record)
    return kept


def insert_comments(conn: sqlite3.Connection, cid: str, container: Path, run_id: str) -> int:
    records, warnings = load_comments(container, cid)
    records = dedupe_comment_keys(records)
    keys = {record["comment_key"] for record in records}
    for record in records:
        conn.execute(
            """
            INSERT INTO comments (
                comment_key, corpus_id, provider, native_comment_id, parent_comment_key,
                author_display_name, author_native_id, author_is_self, created_at,
                modified_at, resolved, deleted, quoted_context, content, metadata_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record["comment_key"],
                cid,
                record["provider"],
                record["native_comment_id"],
                None,
                record["author_display_name"],
                None,
                record["author_is_self"],
                record["created_at"],
                record["modified_at"],
                record["resolved"],
                record["deleted"],
                record["quoted_context"],
                record["content"],
                record["metadata_json"],
            ),
        )
        conn.execute(
            "INSERT INTO comments_fts (corpus_id, comment_key, content, quoted_context) VALUES (?, ?, ?, ?)",
            (cid, record["comment_key"], record["content"], record["quoted_context"] or ""),
        )
    for record in records:
        parent_native = record["parent_native_id"]
        if not parent_native:
            continue
        parent_key = None
        for candidate in (
            f"{cid}:google_drive:{parent_native}",
            f"{cid}:docx_export:{parent_native}",
        ):
            if candidate in keys and candidate != record["comment_key"]:
                parent_key = candidate
                break
        if parent_key:
            conn.execute(
                "UPDATE comments SET parent_comment_key = ? WHERE comment_key = ?",
                (parent_key, record["comment_key"]),
            )
    for message in warnings:
        conn.execute(
            """
            INSERT INTO ingest_warnings (ingest_run_id, corpus_id, code, severity, message)
            VALUES (?, ?, ?, ?, ?)
            """,
            (run_id, cid, "COMMENT_SIDECAR", "WARNING", message),
        )
    return len(records)


def insert_revisions(conn: sqlite3.Connection, cid: str, container: Path, repo: Path, run_id: str) -> tuple[int, int]:
    path = container / "revisions.jsonl"
    if not path.exists():
        return 0, 0
    indexed = 0
    missing = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        rev_id = str(row.get("id") or "").strip()
        if not rev_id:
            continue
        if rev_id == "normalized-current":
            rev_id = "sidecar:normalized-current"
        modifier = row.get("lastModifyingUser") if isinstance(row.get("lastModifyingUser"), dict) else {}
        body_rel = row.get("body_path")
        body_text = None
        body_repo = None
        status = "NOT_FETCHED"
        fetched = bool(row.get("body_fetched")) and isinstance(body_rel, str) and body_rel and ".." not in Path(body_rel).parts
        if fetched:
            full = container / body_rel
            if full.is_file():
                body_text = full.read_text(encoding="utf-8", errors="replace")
                body_repo = str(full.relative_to(repo))
                status = "REVISION_BODY_PRESERVED"
            else:
                status = "BODY_PATH_MISSING"
                missing += 1
        else:
            missing += 1
        digest = hashlib.sha256(body_text.encode("utf-8")).hexdigest() if body_text is not None else row.get("body_sha256")
        conn.execute(
            """
            INSERT INTO document_versions (
                corpus_id, provider_revision_id, modified_at, modifier_display_name,
                modifier_native_id, modifier_metadata_json, is_current, body_capture_status,
                body_path, body_sha256, body_text, export_mime_type, capture_error
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                cid,
                rev_id,
                row.get("modifiedTime"),
                modifier.get("displayName") or None,
                modifier.get("permissionId"),
                json.dumps(modifier, ensure_ascii=False) if modifier else None,
                0,
                status,
                body_repo,
                digest,
                body_text,
                row.get("mimeType"),
                row.get("fetch_error"),
            ),
        )
        if body_text is not None:
            conn.execute(
                "INSERT INTO revision_fts (corpus_id, provider_revision_id, body) VALUES (?, ?, ?)",
                (cid, rev_id, body_text),
            )
            indexed += 1
    if missing:
        conn.execute(
            """
            INSERT INTO ingest_warnings (ingest_run_id, corpus_id, code, severity, message)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                run_id,
                cid,
                "REVISION_BODY_NOT_IN_REPO",
                "LIMITATION",
                f"{missing} revision record(s) have no preserved body. Their text was not invented.",
            ),
        )
    return indexed, missing


def build(repo: Path, db_path: Path) -> dict:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    schema = (repo / "ingest" / "document_archive_schema.sql").read_text(encoding="utf-8")
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(schema)
    run_id = "owner-attestation-2026-10-09"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    conn.execute(
        """
        INSERT INTO ingest_runs
        (ingest_run_id, started_at, completed_at, agent, source_scope, notes)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            run_id,
            now,
            now,
            "owner-attestation",
            "non-discord source containers",
            "Rebuilt after the 2026-10-09 owner attestation. "
            "authorship_status is creator attribution. "
            "archival_provenance_status is missing lineage and is not authorship. "
            "Context containers such as BCS-000059 are not in this index. BCS-000068 has no source container.",
        ),
    )
    pending_links = []
    comment_count = 0
    revision_bodies = 0
    for meta_path, meta in load_records(repo):
        cid = meta["corpus_id"]
        body = primary_body(repo, meta, meta_path)
        body_text = body.read_text(encoding="utf-8", errors="replace") if body else ""
        modified = container_modified_at(meta)
        creator, copyright_owner, basis_kind, attested_on, archival_status = attribution_fields(meta)
        conn.execute(
            """
            INSERT INTO source_containers (
                corpus_id, project, project_slug, title, source_role, source_kind,
                authorship_status, authorship_basis, creator, copyright_owner,
                attribution_basis_kind, attested_on, archival_provenance_status,
                partition_name, created_at,
                modified_at, normalized_path, primary_representation_path,
                normalized_sha256, document_family_id, ingest_run_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                cid,
                meta.get("project"),
                meta.get("project_slug"),
                meta.get("title") or cid,
                meta.get("source_role"),
                meta.get("source_kind"),
                authorship_status(meta),
                authorship_basis(meta),
                creator,
                copyright_owner,
                basis_kind,
                attested_on,
                archival_status,
                meta.get("partition"),
                container_created_at(meta),
                modified,
                str(body.relative_to(repo)) if body else None,
                str(body.relative_to(repo)) if body else None,
                hashlib.sha256(body_text.encode("utf-8")).hexdigest() if body else None,
                meta.get("document_family_id"),
                run_id,
            ),
        )
        for locator in meta.get("locators") or []:
            if not isinstance(locator, dict):
                continue
            native = locator.get("native_id") or locator.get("id")
            conn.execute(
                """
                INSERT INTO source_locators (
                    corpus_id, provider, locator_type, native_id, url,
                    project_name, source_path, metadata_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    cid,
                    locator.get("provider") or "unknown",
                    locator.get("locator_type") or "unspecified",
                    native,
                    locator.get("url"),
                    locator.get("project_name") or locator.get("project"),
                    locator.get("source_path"),
                    json.dumps(locator, ensure_ascii=False),
                ),
            )
        for rep in meta.get("representations") or []:
            if not isinstance(rep, dict) or not rep.get("path") or not rep.get("sha256"):
                continue
            path = repo / rep["path"]
            conn.execute(
                """
                INSERT INTO source_representations (
                    corpus_id, kind, repo_path, mime_type, size_bytes, sha256,
                    is_primary, metadata_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    cid,
                    rep.get("kind") or "unspecified",
                    rep["path"],
                    rep.get("mime_type"),
                    path.stat().st_size if path.exists() else rep.get("size_bytes"),
                    rep["sha256"],
                    1 if "HUMAN" in str(rep.get("kind", "")).upper() or str(rep.get("kind")) == "normalized_markdown" else 0,
                    json.dumps(rep, ensure_ascii=False),
                ),
            )
            if path.exists() and path.suffix.lower() in {".docx", ".xlsx", ".png", ".jpg", ".pdf"}:
                conn.execute(
                    """
                    INSERT OR REPLACE INTO assets (
                        asset_key, corpus_id, filename, mime_type, size_bytes,
                        sha256, repo_path, metadata_json
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        f"{cid}:{rep['path']}",
                        cid,
                        path.name,
                        rep.get("mime_type"),
                        path.stat().st_size,
                        rep["sha256"],
                        rep["path"],
                        json.dumps({"kind": rep.get("kind")}, ensure_ascii=False),
                    ),
                )
        if body:
            conn.execute(
                """
                INSERT INTO document_versions (
                    corpus_id, provider_revision_id, modified_at, is_current,
                    body_capture_status, body_path, body_sha256, body_text,
                    export_mime_type
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    cid,
                    "normalized-current",
                    modified,
                    1,
                    "NORMALIZED_CURRENT",
                    str(body.relative_to(repo)),
                    hashlib.sha256(body_text.encode("utf-8")).hexdigest(),
                    body_text,
                    "text/markdown",
                ),
            )
            conn.execute(
                "INSERT INTO source_fts (corpus_id, title, body) VALUES (?, ?, ?)",
                (cid, meta.get("title") or "", body_text),
            )
            conn.execute(
                "INSERT INTO revision_fts (corpus_id, provider_revision_id, body) VALUES (?, ?, ?)",
                (cid, "normalized-current", body_text),
            )
        comment_count += insert_comments(conn, cid, meta_path.parent, run_id)
        bodies, _missing = insert_revisions(conn, cid, meta_path.parent, repo, run_id)
        revision_bodies += bodies
        pending_links.extend((cid, link) for link in (meta.get("source_links") or []) if isinstance(link, dict))
    for cid, link in pending_links:
        conn.execute(
            """
            INSERT INTO source_links (
                from_corpus_id, link_type, to_corpus_id, external_locator, basis, confidence
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                cid,
                link.get("link_type") or "UNSPECIFIED",
                link.get("to_corpus_id"),
                link.get("external_locator"),
                link.get("basis"),
                link.get("confidence"),
            ),
        )
    conn.commit()
    conn.execute("VACUUM")
    integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
    fk = conn.execute("PRAGMA foreign_key_check").fetchall()
    count = conn.execute("SELECT COUNT(*) FROM source_containers").fetchone()[0]
    comments = conn.execute("SELECT COUNT(*) FROM comments").fetchone()[0]
    conn.close()
    return {
        "containers": count,
        "integrity_check": integrity,
        "foreign_key_check": len(fk),
        "comments": comments,
        "revision_bodies": revision_bodies,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--db", default=None)
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    db_path = Path(args.db).resolve() if args.db else repo / "indexes" / "documents.sqlite"
    result = build(repo, db_path)
    print(f"containers {result['containers']}")
    print(f"comments {result['comments']}")
    print(f"revision_bodies {result['revision_bodies']}")
    print(f"integrity_check {result['integrity_check']}")
    print(f"foreign_key_check {result['foreign_key_check']}")
    return 0 if result["integrity_check"] == "ok" and not result["foreign_key_check"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
