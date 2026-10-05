#!/usr/bin/env python3
"""Rebuild indexes/documents.sqlite from source containers.

The database is a derivative index. Human-readable containers remain canonical.
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    db_path = repo / "indexes" / "documents.sqlite"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    schema = (repo / "ingest" / "document_archive_schema.sql").read_text(encoding="utf-8")
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(schema)
    run_id = "reconcile-source-ingests-2026-10-05"
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
            "grok-reconciliation",
            "non-discord source containers on reconciled integration branch",
            "Rebuilt once from combined historical recovery, Earthfall history, and Saturday D&D history. Not merged from donor SQLite files.",
        ),
    )
    pending_links = []
    for meta_path, meta in load_records(repo):
        cid = meta["corpus_id"]
        body = primary_body(repo, meta, meta_path)
        body_text = body.read_text(encoding="utf-8", errors="replace") if body else ""
        conn.execute(
            """
            INSERT INTO source_containers (
                corpus_id, project, project_slug, title, source_role, source_kind,
                authorship_status, authorship_basis, partition_name, created_at,
                modified_at, normalized_path, primary_representation_path,
                normalized_sha256, document_family_id, ingest_run_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                meta.get("partition"),
                meta.get("created_at") or meta.get("created_timestamp"),
                meta.get("modified_at") or meta.get("modified_timestamp"),
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
                    meta.get("modified_at"),
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
    print(f"containers {count}")
    print(f"integrity_check {integrity}")
    print(f"foreign_key_check {len(fk)}")
    conn.close()
    return 0 if integrity == "ok" and not fk else 1


if __name__ == "__main__":
    raise SystemExit(main())
