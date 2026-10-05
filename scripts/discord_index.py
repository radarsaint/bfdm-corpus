"""Model-facing Discord retrieval.

The SQLite harvest stays canonical. This module searches a hydrated database
when the bytes are present, and otherwise searches the non-LFS JSONL projection
through the term index. It does not write message bodies.
"""

from __future__ import annotations

import hashlib
import json
import re
import sqlite3
from pathlib import Path

LFS_MARK = b"version https://git-lfs.github.com/spec/v1"
TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_'’-]{1,}")
CONTENT_CAP = 1200


class RetrievalError(Exception):
    def __init__(self, message: str, code: str = "error"):
        super().__init__(message)
        self.code = code


def repo_root_from(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "CORPUS_CHARTER.md").is_file() and (candidate / "discord").is_dir():
            return candidate
    raise RetrievalError("Not inside a bfdm-corpus checkout.")


def _fold(value: str) -> str:
    return (value or "").casefold().replace("’", "'").replace("‘", "'")


def _read_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise RetrievalError(f"Invalid JSONL {path}:{line_no}: {exc}") from exc
    return rows


def _dumps(row: dict) -> str:
    return json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _prefix_bytes(path: Path, size: int) -> bytes:
    try:
        with path.open("rb") as handle:
            return handle.read(size)
    except OSError:
        return b""


def is_lfs_pointer(path: Path) -> bool:
    if not path.is_file():
        return False
    return _prefix_bytes(path, len(LFS_MARK)) == LFS_MARK


def sqlite_usable(path: Path) -> bool:
    if not path.is_file() or is_lfs_pointer(path):
        return False
    return _prefix_bytes(path, 16) == b"SQLite format 3\x00"


def load_servers(repo: Path) -> list[dict]:
    return _read_jsonl(repo / "registry" / "discord_servers.jsonl")


def resolve_server(spec: str, repo: Path) -> dict:
    needle = _fold(spec)
    servers = load_servers(repo)
    exact = []
    for row in servers:
        labels = [
            row.get("server_slug") or "",
            row.get("server_name") or "",
            row.get("server_id") or "",
            *(row.get("project_ids") or []),
        ]
        if needle in {_fold(label) for label in labels if label}:
            exact.append(row)
    if len(exact) == 1:
        return exact[0]
    if not exact:
        known = ", ".join(sorted(row["server_slug"] for row in servers))
        raise RetrievalError(f"Unknown Discord server '{spec}'. Known slugs: {known}", code="unknown_server")
    slugs = ", ".join(row["server_slug"] for row in exact)
    raise RetrievalError(f"Server '{spec}' matches multiple harvests: {slugs}", code="ambiguous_server")


def load_aliases(repo: Path, server_slug: str) -> list[dict]:
    path = repo / "model-index" / "discord" / server_slug / "aliases.jsonl"
    rows = _read_jsonl(path)
    for row in rows:
        names = [_fold(row.get("canonical") or "")]
        names.extend(_fold(item) for item in row.get("aliases") or [])
        row["_names"] = {item for item in names if item}
    return rows


def resolve_alias(query: str, aliases: list[dict]) -> dict | None:
    needle = _fold(query.strip().strip("\"'"))
    hits = [row for row in aliases if needle in row.get("_names", set())]
    if len(hits) == 1:
        return hits[0]
    if len(hits) > 1:
        raise RetrievalError(
            "Alias matches multiple entities: " + ", ".join(row["entity_id"] for row in hits),
            code="ambiguous_alias",
        )
    return None


def _word_pattern(term: str) -> re.Pattern[str]:
    return re.compile(rf"(?i)(?<![A-Za-z0-9]){re.escape(term)}(?![A-Za-z0-9])")


def _public_message(row: dict, attachments: list[dict], full: bool, shard: str | None = None) -> dict:
    content = row.get("content") or ""
    truncated = False
    if not full and len(content) > CONTENT_CAP:
        content = content[:CONTENT_CAP]
        truncated = True
    return {
        "attachments": [
            {
                "content_type": item.get("content_type"),
                "filename": item.get("filename"),
                "id": item.get("id") or item.get("attachment_id"),
                "local_path": item.get("local_path"),
                "sha256": item.get("sha256"),
                "size": item.get("size"),
            }
            for item in attachments
        ],
        "author_id": row.get("author_id"),
        "channel": row.get("channel"),
        "channel_id": row.get("channel_id"),
        "content": content,
        "content_truncated": truncated,
        "created_at": row.get("created_at"),
        "display_name": row.get("display_name"),
        "message_id": row.get("id") or row.get("message_id"),
        "reply_to_id": row.get("reply_to_id"),
        "server": row.get("server"),
        "shard": shard,
        "thread": row.get("thread"),
        "thread_id": row.get("thread_id"),
        "username": row.get("username"),
    }


def _filters_match(row: dict, channel: str | None, author: str | None) -> bool:
    if channel and channel.casefold() not in (row.get("channel") or "").casefold():
        return False
    if author:
        needle = author.casefold()
        names = {(row.get("display_name") or "").casefold(), (row.get("username") or "").casefold()}
        if needle not in names and not any(needle in name for name in names if name):
            return False
    return True


def export_attachments(database: Path, repo: Path, server_slug: str | None = None) -> dict:
    """Write attachment metadata only. No message text and no CDN url."""
    if not sqlite_usable(database):
        raise RetrievalError(f"Database is not a hydrated SQLite file: {database}", code="lfs_pointer_only")
    slug = server_slug or database.stem
    out = repo / "model-index" / "discord" / slug
    out.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        fetched = connection.execute(
            """
            SELECT a.id AS id, a.message_id AS message_id, a.filename AS filename,
                   a.content_type AS content_type, a.size AS size, a.sha256 AS sha256,
                   a.local_path AS local_path, m.created_at AS created_at,
                   m.channel_id AS channel_id, c.name AS channel
            FROM attachments a
            JOIN messages m ON m.id = a.message_id
            JOIN channels c ON c.id = m.channel_id
            ORDER BY m.created_at, m.id, a.id
            """
        ).fetchall()
    finally:
        connection.close()
    rows = [{key: row[key] for key in row.keys()} for row in fetched]
    payload = "\n".join(_dumps(row) for row in rows) + ("\n" if rows else "")
    path = out / "attachments.jsonl"
    path.write_text(payload, encoding="utf-8")
    canonical = f"discord/{slug}/{slug}.sqlite"
    manifest = {
        "attachment_count": len(rows),
        "bytes": len(payload.encode("utf-8")),
        "canonical_database": canonical,
        "fields_omitted": ["url", "content", "file_bytes"],
        "path": path.relative_to(repo).as_posix(),
        "server_slug": slug,
        "sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
        "subordinate_to": canonical,
    }
    (out / "attachments-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest


def _attachment_map(repo: Path, server_slug: str) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}
    for row in _read_jsonl(repo / "model-index" / "discord" / server_slug / "attachments.jsonl"):
        grouped.setdefault(row["message_id"], []).append(row)
    return grouped


def _term_prefix(token: str) -> str:
    head = token[:3].ljust(3, "_")
    return "".join(ch if ("a" <= ch <= "z" or "0" <= ch <= "9") else "_" for ch in head)


def _single_token(value: str) -> str | None:
    folded = _fold(value.strip().strip("\"'"))
    if re.fullmatch(r"[a-z0-9][a-z0-9'_-]{1,}", folded):
        return folded
    return None


def _neighbor_tokens(repo: Path, server_slug: str, query: str) -> list[str]:
    token = _fold(query.strip().strip("\"'"))
    if len(token) < 3:
        return []
    path = repo / "model-index" / "discord" / server_slug / "terms" / f"{_term_prefix(token)}.jsonl"
    names = []
    for row in _read_jsonl(path):
        other = row.get("token") or ""
        if other.startswith(token) and other != token:
            names.append(other)
    return sorted(names)


def _search_sqlite(database: Path, server: dict, terms: list[str], phrase: str | None, channel, author, attachments_only, limit, full) -> list[dict]:
    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        if phrase is not None:
            match = '"' + phrase.replace('"', " ") + '"'
            id_rows = connection.execute(
                "SELECT rowid FROM messages_fts WHERE messages_fts MATCH ?",
                (match,),
            ).fetchall()
        else:
            clauses = " OR ".join(["messages_fts MATCH ?"] * len(terms))
            id_rows = connection.execute(
                f"SELECT rowid FROM messages_fts WHERE {clauses}",
                tuple(f'"{term}"' for term in terms),
            ).fetchall()
        if not id_rows:
            return []
        ids = list(dict.fromkeys(row[0] for row in id_rows))
        fetched = []
        for start in range(0, len(ids), 800):
            chunk = ids[start : start + 800]
            placeholders = ",".join("?" for _ in chunk)
            fetched.extend(
                connection.execute(
                    f"""
                    SELECT m.id, m.created_at, m.content, m.reply_to_id, m.channel_id, c.name AS channel,
                           m.thread_id, t.name AS thread, m.author_id, u.username, u.display_name
                    FROM messages m
                    JOIN channels c ON c.id = m.channel_id
                    LEFT JOIN threads t ON t.id = m.thread_id
                    LEFT JOIN users u ON u.id = m.author_id
                    WHERE m.rowid IN ({placeholders})
                    """,
                    chunk,
                ).fetchall()
            )
        fetched.sort(key=lambda row: (row["created_at"], row["id"]))
        patterns = [] if phrase is not None else [_word_pattern(term) for term in terms]
        phrase_needle = _fold(phrase) if phrase is not None else None
        kept = []
        for row in fetched:
            item = dict(row)
            item["server"] = server["server_slug"]
            text = item.get("content") or ""
            if phrase_needle is not None:
                if phrase_needle not in _fold(text):
                    continue
            elif not any(pattern.search(text) for pattern in patterns):
                continue
            if not _filters_match(item, channel, author):
                continue
            attachment_rows = [
                dict(att)
                for att in connection.execute(
                    """
                    SELECT id, filename, content_type, size, sha256, local_path
                    FROM attachments WHERE message_id = ? ORDER BY id
                    """,
                    (item["id"],),
                )
            ]
            if attachments_only and not attachment_rows:
                continue
            kept.append(_public_message(item, attachment_rows, full))
        return kept
    finally:
        connection.close()


def _shards_for_tokens(repo: Path, server_slug: str, terms: list[str]) -> tuple[list[str], list[str]]:
    shards: set[str] = set()
    missing = []
    seen: dict[str, list[dict]] = {}
    root = repo / "model-index" / "discord" / server_slug
    for term in terms:
        prefix = _term_prefix(term)
        if prefix in seen:
            rows = seen[prefix]
        else:
            path = root / "terms" / f"{prefix}.jsonl"
            if not path.is_file():
                missing.append(path.relative_to(repo).as_posix())
                rows = []
            else:
                rows = _read_jsonl(path)
            seen[prefix] = rows
        for row in rows:
            token = row.get("token") or ""
            if token == term or token.startswith(term + "'") or token.startswith(term + "-"):
                shards.update(row.get("shards") or [])
    return sorted(shards), missing


def _search_projection(repo, server, terms, phrase, channel, author, attachments_only, limit, full) -> tuple[list[dict], list[str]]:
    if phrase is None:
        lookup_terms = terms
    else:
        tokens = [_fold(token) for token in TOKEN_RE.findall(phrase) if len(_fold(token)) >= 3]
        if tokens:
            longest = max(len(token) for token in tokens)
            lookup_terms = [token for token in tokens if len(token) == longest]
        else:
            lookup_terms = [term for term in terms if len(term) >= 3] or terms
    shard_names, missing = _shards_for_tokens(repo, server["server_slug"], lookup_terms)
    root = repo / "model-index" / "discord" / server["server_slug"]
    patterns = [] if phrase is not None else [_word_pattern(term) for term in terms]
    phrase_needle = _fold(phrase) if phrase is not None else None
    attachments = _attachment_map(repo, server["server_slug"])
    kept = []
    for name in shard_names:
        path = root / name
        if not path.is_file():
            missing.append(path.relative_to(repo).as_posix())
            continue
        for row in _read_jsonl(path):
            text = row.get("content") or ""
            if phrase_needle is not None:
                if phrase_needle not in _fold(text):
                    continue
            elif not any(pattern.search(text) for pattern in patterns):
                continue
            row = dict(row)
            row["server"] = server["server_slug"]
            if not _filters_match(row, channel, author):
                continue
            attached = attachments.get(row["id"], [])
            if attachments_only and not attached:
                continue
            kept.append((row.get("created_at") or "", row["id"], row, attached, name))
    kept.sort(key=lambda item: (item[0], item[1]))
    return [_public_message(row, attached, full, shard) for _, _, row, attached, shard in kept], missing


def _lead_hits(hits: list[dict], terms: list[str], cap: int = 5) -> list[dict]:
    """Messages that use more than one name of an expanded entity.

    Chronological hits stay intact. This only surfaces a short reading list
    when a short alias would otherwise bury the messages that use the other names.
    """
    if len(terms) < 2 or not hits:
        return []
    patterns = [_word_pattern(term) for term in terms]

    def score(hit: dict) -> int:
        text = hit.get("content") or ""
        return sum(1 for pattern in patterns if pattern.search(text))

    ranked = sorted(hits, key=lambda hit: (-score(hit), hit.get("created_at") or "", hit.get("message_id") or ""))
    if score(ranked[0]) < 2:
        return []
    return [hit for hit in ranked if score(hit) >= 2][:cap]


def search(
    repo: Path,
    query: str,
    server: str | None = None,
    channel: str | None = None,
    author: str | None = None,
    phrase: bool = False,
    attachments_only: bool = False,
    limit: int = 20,
    full: bool = False,
    source: str = "auto",
    database: Path | None = None,
) -> dict:
    repo = repo.resolve()
    if not query or not query.strip():
        raise RetrievalError("Empty query.")
    raw = query.strip()
    quoted = len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in {"'", '"'}
    if quoted:
        raw = raw[1:-1]
        phrase = True
    if server is None:
        raise RetrievalError("Pass --server. Discord aliases are campaign-scoped and are not searched globally.", code="server_required")
    server_row = resolve_server(server, repo)
    slug = server_row["server_slug"]
    aliases = load_aliases(repo, slug)
    entity = None if phrase else resolve_alias(raw, aliases)
    if entity:
        terms = sorted(entity["_names"])
    else:
        terms = [_fold(raw)]
    database_path = Path(database) if database else repo / (server_row.get("database_path") or "")
    use_sqlite = source == "sqlite" or (source == "auto" and sqlite_usable(database_path))
    if source == "sqlite" and not sqlite_usable(database_path):
        raise RetrievalError(f"SQLite bytes are not available at {database_path}", code="lfs_pointer_only")
    missing: list[str] = []
    if use_sqlite:
        hits = _search_sqlite(
            database_path, server_row, terms, raw if phrase else None, channel, author, attachments_only, limit, full
        )
        access = "hydrated_sqlite"
    else:
        if source == "projection" or source == "auto":
            hits, missing = _search_projection(
                repo, server_row, terms, raw if phrase else None, channel, author, attachments_only, limit, full
            )
            access = "jsonl_projection"
        else:
            raise RetrievalError(f"Unknown source '{source}'", code="bad_source")
    match_count = len(hits)
    leads = _lead_hits(hits, terms if entity else [])
    hits = hits[:limit]
    if use_sqlite:
        status = "EXHAUSTIVE"
    else:
        manifest = repo / "model-index" / "discord" / slug / "manifest.json"
        if not manifest.is_file():
            status = "INACCESSIBLE"
        elif missing:
            status = "PARTIAL"
        else:
            status = "EXHAUSTIVE"
    pointer = is_lfs_pointer(database_path)
    if status == "INACCESSIBLE":
        reason_codes = ["lfs_pointer_only" if pointer or not database_path.is_file() else "missing_readable_projection"]
    elif status == "PARTIAL":
        reason_codes = ["missing_readable_projection"]
    else:
        reason_codes = []
    if pointer:
        database_state = "lfs_pointer"
    elif sqlite_usable(database_path):
        database_state = "hydrated"
    else:
        database_state = "missing"
    query_token = None if phrase else _single_token(raw)
    neighbors = []
    if query_token:
        expanded = set(terms)
        neighbors = [token for token in _neighbor_tokens(repo, slug, query_token) if token not in expanded]
    return {
        "aliases_expanded": terms if entity else [],
        "ambiguous_neighbors": neighbors,
        "coverage_report": {
            "absence_is_not_evidence": status != "EXHAUSTIVE",
            "access": access,
            "canonical_database": server_row.get("database_path"),
            "canonical_database_state": database_state,
            "database_usable": sqlite_usable(database_path),
            "missing": missing,
            "project_ids": server_row.get("project_ids") or [],
            "reason_codes": reason_codes,
            "searched_families": [f"discord:{slug}"],
            "server": slug,
            "status": status,
            "zero_match_means_absence": status == "EXHAUSTIVE",
        },
        "entity": None
        if entity is None
        else {"canonical": entity.get("canonical"), "entity_id": entity.get("entity_id"), "server": slug},
        "hits": hits,
        "lead_hits": leads,
        "match_count": match_count,
        "query": query,
        "returned": len(hits),
        "truncated": match_count > len(hits),
    }
