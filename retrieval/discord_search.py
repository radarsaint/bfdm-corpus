#!/usr/bin/env python3
"""Dependency-free Discord export, navigation, and search. See retrieval/README.md."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import shutil
import sqlite3
import sys
import tempfile
import unicodedata

VERSION = 1
PAGE_BYTES = 48 * 1024
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXPORT = ROOT / "indexes/discord"
DEFAULT_INDEX = ROOT / ".cache/discord-search.sqlite"


def dumps(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256(path):
    with Path(path).open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def read_jsonl(path, missing_ok=False):
    if missing_ok and not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def tokens(text):
    # Shared by deterministic token navigation and prefix suggestions. SQLite's
    # unicode61 tokenizer is used separately for CLI phrase/FTS matching.
    text = unicodedata.normalize("NFKD", text or "").casefold()
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.findall(r"[^\W_]+", text, flags=re.UNICODE)


def normalized(text):
    return " ".join(tokens(text))


def bucket(term):
    value = term[:2]
    return value if re.fullmatch(r"[a-z0-9]{1,2}", value) else "_other"


def read_db(path):
    with path.open("rb") as f:
        if f.read(16) != b"SQLite format 3\0":
            raise ValueError(f"{path} is not a hydrated SQLite database. Run git lfs pull --include='discord/*/*.sqlite'.")
    db = sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    return db


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dumps(value) + "\n", encoding="utf-8")


def write_pages(directory, rows, *, header=None, key=None, max_bytes=PAGE_BYTES):
    """Bounded UTF-8 JSONL pages; fail rather than truncate an oversized record."""
    directory.mkdir(parents=True, exist_ok=True)
    prefix = (dumps(header) + "\n").encode() if header else b""
    pages, pending, size = [], [], len(prefix)

    def flush():
        if not pending:
            return
        path = directory / f"{len(pages):05d}.jsonl"
        path.write_bytes(prefix + b"".join(line for _, line in pending))
        item = {"path": path.name, "records": len(pending), "bytes": path.stat().st_size,
                "sha256": sha256(path)}
        if key:
            item.update(first=pending[0][0][key], last=pending[-1][0][key])
        pages.append(item)

    for row in rows:
        line = (dumps(row) + "\n").encode()
        if len(prefix) + len(line) > max_bytes:
            raise ValueError(f"Oversized record for {directory}: {len(line)} bytes")
        if pending and size + len(line) > max_bytes:
            flush()
            pending, size = [], len(prefix)
        pending.append((row, line))
        size += len(line)
    flush()
    write_json(directory / "index.json", {"pages": pages})
    return pages


def export(repo, output):
    """Read canonical databases only. Generate into a staging directory first."""
    repo, output = repo.resolve(), output.resolve()
    if output == repo or repo.is_relative_to(output) or any(
        output.is_relative_to(repo / name) for name in ("discord", "registry", ".git", "sources", "context", "evidence")
    ):
        raise ValueError("Export destination must be a dedicated derived directory")
    if output.exists() and any(output.iterdir()) and not (output / "catalog.json").exists():
        raise ValueError("Refusing to replace a non-export directory")
    paths = sorted((repo / "discord").glob("*/*.sqlite"))
    if not paths:
        raise ValueError("No canonical Discord archives found")
    registry = read_jsonl(repo / "registry/discord_servers.jsonl", missing_ok=True)
    projects = read_jsonl(repo / "registry/projects.jsonl", missing_ok=True)
    entities = read_jsonl(repo / "registry/discord_entities.jsonl", missing_ok=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".discord-export-", dir=output.parent) as stage:
        target = Path(stage)
        catalog = {"format_version": VERSION, "derived": True, "page_bytes": PAGE_BYTES,
                   "generator_sha256": sha256(Path(__file__)),
                   "source_authority": "Canonical discord/<server>/<server>.sqlite; native Discord IDs are unchanged.",
                   "inputs": {}, "harvests": []}
        for name in ("discord_servers.jsonl", "projects.jsonl", "discord_entities.jsonl"):
            path = repo / "registry" / name
            if path.exists():
                catalog["inputs"]["registry/" + name] = sha256(path)
        for path in paths:
            slug = path.parent.name
            source_path = path.relative_to(repo).as_posix()
            source_hash = sha256(path)
            db = read_db(path)
            try:
                if db.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
                    raise ValueError(f"Integrity check failed: {path}")
                servers = [dict(row) for row in db.execute("SELECT * FROM servers ORDER BY id")]
                if len(servers) != 1:
                    raise ValueError(f"Expected one server in {source_path}")
                server = servers[0]
                reg = next((r for r in registry if r["server_id"] == server["id"]), {})
                project_ids = reg.get("project_ids", [])
                project_names = set()
                for p in projects:
                    if p["project_id"] in project_ids:
                        project_names.update([p["project_id"], p.get("canonical_name", p.get("title", ""))])
                        project_names.update(a["name"] for a in p.get("aliases", []))
                scope = {"server_slug": slug, "server": server, "project_ids": project_ids,
                         "campaign_names": sorted(project_names), "database_path": source_path,
                         "database_sha256": source_hash}
                users = {r["id"]: dict(r) for r in db.execute("SELECT * FROM users ORDER BY id")}
                threads = {r["id"]: dict(r) for r in db.execute("SELECT * FROM threads ORDER BY id")}
                attachments = defaultdict(list)
                for row in db.execute("SELECT * FROM attachments ORDER BY message_id, id"):
                    a = dict(row)
                    # Native path and URL are preserved; binary bytes are never copied.
                    attachments[a["message_id"]].append(a)
                aliases = [e for e in entities if e["server_id"] == server["id"]]
                entity_keys = [e["entity_key"] for e in aliases]
                if len(entity_keys) != len(set(entity_keys)):
                    raise ValueError(f"Duplicate entity key in {slug}")
                for entity in aliases:
                    if not entity.get("support"):
                        raise ValueError(f"Alias lacks source support: {entity['entity_key']}")
                    for ref in entity["support"]:
                        if ref["database_path"] != source_path or not db.execute(
                            "SELECT 1 FROM messages WHERE id=?", (ref["message_id"],)).fetchone():
                            raise ValueError(f"Alias source is missing: {entity['entity_key']} {ref}")
                base = target / slug
                channels = []
                postings = defaultdict(Counter)
                attachment_hits = defaultdict(Counter)
                count = 0
                locations = {}
                for chrow in db.execute("SELECT * FROM channels ORDER BY id"):
                    ch = dict(chrow)
                    rows = []
                    for row in db.execute("SELECT * FROM messages WHERE channel_id=? ORDER BY created_at,id", (ch["id"],)):
                        m = dict(row)
                        m["author"] = users.get(m["author_id"])
                        m["thread"] = threads.get(m.get("thread_id"))
                        m["attachments"] = attachments.get(m["id"], [])
                        rows.append(m)
                    header = {"_type": "shard", **scope, "channel": ch}
                    rel = f"messages/{ch['id']}"
                    pages = write_pages(base / rel, rows, header=header, key="created_at")
                    for p in pages:
                        shard = rel + "/" + p["path"]
                        for m in read_jsonl(base / shard)[1:]:
                            locations[m["id"]] = shard
                            text = (m["content"] or "") + " " + " ".join(a.get("filename") or "" for a in m["attachments"])
                            for term in set(tokens(text)):
                                postings[term][shard] += 1
                                if m["attachments"]:
                                    attachment_hits[term][shard] += 1
                    channels.append({**ch, "message_count": len(rows), "index_path": rel + "/index.json"})
                    count += len(rows)
                expected = db.execute("SELECT count(*) FROM messages").fetchone()[0]
                if count != expected:
                    raise ValueError(f"Unmapped/orphan channel messages in {source_path}: {count}/{expected}")
                alias_rows = []
                for e in aliases:
                    copy = dict(e)
                    copy["support"] = [{**ref, "shard": locations[ref["message_id"]]} for ref in e["support"]]
                    alias_rows.append(copy)
                write_json(base / "entities.json", {"entities": alias_rows})
                write_pages(base / "channels", channels, key="id")
                write_json(base / "manifest.json", {**scope, "message_count": count,
                    "attachment_count": sum(map(len, attachments.values())), "channel_count": len(channels),
                    "channels_index": "channels/index.json", "entities": "entities.json", "lookup": "lookup/<first-two-normalized-characters>/index.json"})
                buckets = defaultdict(list)
                for term in sorted(postings):
                    matches = [{"path": p, "hits": n, "attachment_hits": attachment_hits[term][p]}
                               for p, n in sorted(postings[term].items(), key=lambda item: (-attachment_hits[term][item[0]], -item[1], item[0]))]
                    # Frequent terms span records/pages; never drop the tail.
                    for start in range(0, len(matches), 100):
                        buckets[bucket(term)].append({"term": term, "message_hits": sum(postings[term].values()),
                            "shard_count": len(matches), "part": start // 100 + 1,
                            "parts": (len(matches) + 99) // 100, "shards": matches[start:start + 100]})
                for name, rows in sorted(buckets.items()):
                    write_pages(base / "lookup" / name, rows, key="term")
                write_json(base / "lookup/index.json", {"buckets": sorted(buckets)})
                catalog["harvests"].append({**scope, "manifest": f"{slug}/manifest.json", "message_count": count,
                    "attachment_count": sum(map(len, attachments.values())), "tokens": len(postings)})
                print(f"Exported {slug}: {count:,} messages", file=sys.stderr)
            finally:
                db.close()
            if sha256(path) != source_hash:
                raise ValueError(f"Source changed during export: {source_path}")
        write_json(target / "catalog.json", catalog)
        # A deterministic manifest commits to every generated byte, without timestamps.
        files = [{"path": p.relative_to(target).as_posix(), "sha256": sha256(p), "bytes": p.stat().st_size}
                 for p in sorted(target.rglob("*")) if p.is_file()]
        write_pages(target / "checksums", files, key="path")
        if output.exists():
            shutil.rmtree(output)
        shutil.move(str(target), str(output))
    return catalog


def scoped_harvests(export_dir, campaign=None):
    catalog = json.loads((export_dir / "catalog.json").read_text())
    if catalog["format_version"] != VERSION:
        raise ValueError("Unsupported export version; rebuild using the matching exporter")
    harvests = catalog["harvests"]
    if campaign:
        needle = normalized(campaign)
        harvests = [h for h in harvests if needle in [normalized(x) for x in
                    [h["server_slug"], h["server"]["name"], h["server"]["id"]] + h["campaign_names"] + h["project_ids"]]]
        if not harvests:
            raise ValueError(f"Unknown campaign/server: {campaign}")
    return harvests


def entity_matches(export_dir, harvests, query):
    found = []
    for h in harvests:
        for e in json.loads((export_dir / h["server_slug"] / "entities.json").read_text())["entities"]:
            if normalized(query) in {normalized(a) for a in e["aliases"] + [e["canonical_name"]]}:
                found.append({**e, "server_slug": h["server_slug"]})
    return found


def lookup(export_dir, campaign, query, prefix=False):
    """Connector-equivalent navigation: read tiny text routers and posting pages."""
    harvests = scoped_harvests(export_dir, campaign)
    entities = entity_matches(export_dir, harvests, query)
    result = {"query": query, "entities": entities, "ambiguous": len(entities) > 1, "matches": []}
    for h in harvests:
        terms = set(tokens(query))
        for e in entities:
            if e["server_id"] == h["server"]["id"]:
                for alias in e["aliases"]:
                    terms.update(tokens(alias))
        base = export_dir / h["server_slug"]
        pages = set()
        for term in terms:
            names = [bucket(term)]
            if prefix and len(term) == 1:
                names = [n for n in json.loads((base / "lookup/index.json").read_text())["buckets"] if n.startswith(term)]
            for name in names:
                index = base / "lookup" / name / "index.json"
                if not index.exists():
                    continue
                for p in json.loads(index.read_text())["pages"]:
                    upper = term + "\U0010ffff" if prefix else term
                    if p["first"] <= upper and p["last"] >= term:
                        pages.add(index.parent / p["path"])
        for page in sorted(pages):
            for row in read_jsonl(page):
                if any(row["term"].startswith(t) if prefix else row["term"] == t for t in terms):
                    result["matches"].append({"server_slug": h["server_slug"], **row})
    return result


INDEX_SCHEMA = """
CREATE TABLE meta(key TEXT PRIMARY KEY, value TEXT);
CREATE TABLE messages(
 rowid INTEGER PRIMARY KEY, server_slug TEXT, server_id TEXT, id TEXT,
 channel_id TEXT, thread_id TEXT, channel_text TEXT, author_id TEXT, author_text TEXT,
 created_at TEXT, reply_to_id TEXT, has_attachment INTEGER, content TEXT, attachment_text TEXT,
 record_json TEXT, UNIQUE(server_slug,id));
CREATE INDEX channel_time ON messages(server_slug,channel_id,thread_id,created_at,id);
CREATE INDEX author_filter ON messages(author_id);
CREATE INDEX reply_filter ON messages(server_slug,reply_to_id);
CREATE TABLE attachments(id TEXT, server_slug TEXT, message_id TEXT, filename TEXT, record_json TEXT,
 PRIMARY KEY(server_slug,id));
CREATE VIRTUAL TABLE search USING fts5(content,attachment_text,content='messages',content_rowid='rowid',tokenize='unicode61 remove_diacritics 2');
"""


def build_index(export_dir, index):
    verify_export_files(export_dir)
    index.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".discord-index-", dir=index.parent) as temp:
        staged = Path(temp) / "search.sqlite"
        db = sqlite3.connect(staged)
        db.executescript(INDEX_SCHEMA)
        count = 0
        for h in scoped_harvests(export_dir):
            base = export_dir / h["server_slug"]
            for path in sorted((base / "messages").glob("*/*.jsonl")):
                header, *messages = read_jsonl(path)
                for m in messages:
                    author = m.get("author") or {}
                    record = {**m, "server_slug": h["server_slug"], "server": header["server"],
                        "project_ids": header["project_ids"], "channel": header["channel"],
                        "provenance": {"database_path": header["database_path"], "database_sha256": header["database_sha256"],
                            "table": "messages", "message_id": m["id"], "shard": path.relative_to(export_dir).as_posix(),
                            "discord_url": f"https://discord.com/channels/{h['server']['id']}/{m.get('thread_id') or m['channel_id']}/{m['id']}"}}
                    db.execute("INSERT INTO messages VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                        h["server_slug"], h["server"]["id"], m["id"], m["channel_id"], m.get("thread_id"),
                        normalized(header["channel"]["name"]), m["author_id"],
                        normalized(" ".join(author.get(k) or "" for k in ("username", "display_name"))),
                        m["created_at"], m.get("reply_to_id"), bool(m["attachments"]), m["content"] or "",
                        " ".join(a.get("filename") or "" for a in m["attachments"]), dumps(record)))
                    for a in m["attachments"]:
                        db.execute("INSERT INTO attachments VALUES(?,?,?,?,?)", (a["id"], h["server_slug"], m["id"], a.get("filename"), dumps(a)))
                    count += 1
        db.execute("INSERT INTO search(search) VALUES('rebuild')")
        db.execute("INSERT INTO meta VALUES('export_sha256',?)", (sha256(export_dir / "checksums/index.json"),))
        db.execute("INSERT INTO meta VALUES('format_version',?)", (str(VERSION),))
        db.commit()
        db.execute("VACUUM")
        if db.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise ValueError("Search index failed integrity check")
        db.close()
        staged.replace(index)
    return {"messages": count, "index": str(index)}


def open_index(export_dir, index):
    if not index.exists():
        build_index(export_dir, index)
    db = read_db(index)
    expected = sha256(export_dir / "checksums/index.json")
    row = db.execute("SELECT value FROM meta WHERE key='export_sha256'").fetchone()
    if not row or row[0] != expected:
        db.close()
        raise ValueError("Search index is stale. Run build-index.")
    return db


def quoted(term):
    return '"' + term.replace('"', '""') + '"'


def resolve_query(export_dir, harvests, query, exact=False, prefix=False, aliases=True):
    found = entity_matches(export_dir, harvests, query) if aliases and not exact else []
    by_server = []
    for h in harvests:
        terms = {query} if query else set()
        for e in found:
            if e["server_id"] == h["server"]["id"]:
                terms.update(e["aliases"])
        expressions = []
        for term in sorted(terms):
            words = tokens(term)
            if not words:
                continue
            if exact or len(words) == 1:
                expressions.append(quoted(" ".join(words)) + ("*" if prefix else ""))
            else:
                expressions.append("(" + " AND ".join(quoted(w) + ("*" if prefix else "") for w in words) + ")")
        if expressions:
            by_server.append((h["server_slug"], " OR ".join(expressions)))
    return found, by_server


def context_for(db, record, count):
    result = {}
    for side, op, order in (("before", "<", "DESC"), ("after", ">", "ASC")):
        rows = db.execute(f"""SELECT record_json FROM messages WHERE server_slug=? AND channel_id=?
            AND thread_id IS ? AND (created_at,id) {op} (?,?) ORDER BY created_at {order},id {order} LIMIT ?""",
            (record["server_slug"], record["channel_id"], record.get("thread_id"), record["created_at"], record["id"], count)).fetchall()
        values = [json.loads(r[0]) for r in rows]
        result[side] = values[::-1] if side == "before" else values
    reply = db.execute("SELECT record_json FROM messages WHERE server_slug=? AND id=?", (record["server_slug"], record.get("reply_to_id"))).fetchone()
    result["reply_to"] = json.loads(reply[0]) if reply else None
    return result


def search(export_dir, index, *, query="", campaign=None, channel=None, author=None,
           exact=False, prefix=False, aliases=True, has_attachment=False, limit=10, offset=0, context=0,
           message_id=None, attachment_id=None):
    harvests = scoped_harvests(export_dir, campaign)
    found, expressions = resolve_query(export_dir, harvests, query, exact, prefix, aliases)
    if query and not expressions:
        raise ValueError("Query contains no searchable words")
    if exact and prefix:
        raise ValueError("Choose either exact phrase or prefix mode")
    db = open_index(export_dir, index)
    try:
        clauses, params = [], []
        if query:
            for slug, expr in expressions:
                clauses.append("(m.server_slug=? AND m.rowid IN (SELECT rowid FROM search WHERE search MATCH ?))")
                params.extend([slug, expr])
            where = ["(" + " OR ".join(clauses) + ")"]
        else:
            where = ["m.server_slug IN (" + ",".join("?" for _ in harvests) + ")"]
            params.extend(h["server_slug"] for h in harvests)
        if channel:
            where.append("(m.channel_id=? OR instr(m.channel_text,?)>0)")
            params.extend([channel, normalized(channel)])
        if author:
            where.append("(m.author_id=? OR instr(m.author_text,?)>0)")
            params.extend([author, normalized(author)])
        if message_id:
            where.append("m.id=?")
            params.append(message_id)
        if has_attachment:
            where.append("m.has_attachment=1")
        if attachment_id:
            where.append("EXISTS(SELECT 1 FROM attachments a WHERE a.server_slug=m.server_slug AND a.message_id=m.id AND a.id=?)")
            params.append(attachment_id)
        condition = " AND ".join(where)
        total = db.execute("SELECT count(*) FROM messages m WHERE " + condition, params).fetchone()[0]
        # Transparent chronological order, with complete pagination. No opaque
        # relevance score may silently bury a source in the archive.
        rows = db.execute("SELECT record_json FROM messages m WHERE " + condition +
            " ORDER BY m.created_at,m.server_slug,m.id LIMIT ? OFFSET ?", params + [limit, offset]).fetchall()
        hits = [json.loads(r[0]) for r in rows]
        for record in hits:
            if context:
                record["context"] = context_for(db, record, context)
        support = []
        seen = set()
        for e in found:
            for ref in e["support"]:
                key = (e["server_slug"], ref["message_id"])
                if key in seen:
                    continue
                seen.add(key)
                row = db.execute("SELECT record_json FROM messages WHERE server_slug=? AND id=?", key).fetchone()
                if row:
                    support.append(json.loads(row[0]))
        return {"query": query, "campaign": campaign, "total": total, "offset": offset,
                "next_offset": offset + len(hits) if offset + len(hits) < total else None,
                "entities": found, "ambiguous": len(found) > 1, "alias_evidence": support, "hits": hits}
    finally:
        db.close()


def verify_export_files(export_dir):
    """Validate the complete ordinary-text export without requiring LFS sources."""
    count = 0
    checksum_index = json.loads((export_dir / "checksums/index.json").read_text())
    expected_paths = {"checksums/index.json"}
    for p in checksum_index["pages"]:
        page = export_dir / "checksums" / p["path"]
        expected_paths.add(page.relative_to(export_dir).as_posix())
        if sha256(page) != p["sha256"]:
            raise ValueError(f"Checksum page differs: {page}")
        for row in read_jsonl(page):
            path = export_dir / row["path"]
            expected_paths.add(row["path"])
            if path.stat().st_size != row["bytes"] or sha256(path) != row["sha256"]:
                raise ValueError(f"Generated file differs: {path}")
            count += 1
    actual_paths = {p.relative_to(export_dir).as_posix() for p in export_dir.rglob("*") if p.is_file()}
    if actual_paths != expected_paths:
        raise ValueError("Export file inventory differs; rebuild export")
    return count


def verify(repo, export_dir):
    """Validate file bytes, source hashes, and row parity without modifying inputs."""
    count = verify_export_files(export_dir)
    catalog = json.loads((export_dir / "catalog.json").read_text())
    for path, checksum in catalog["inputs"].items():
        if sha256(repo / path) != checksum:
            raise ValueError(f"Registry changed: {path}; rebuild export")
    totals = {}
    for h in scoped_harvests(export_dir):
        if sha256(repo / h["database_path"]) != h["database_sha256"]:
            raise ValueError(f"Source changed: {h['database_path']}; rebuild export")
        db = read_db(repo / h["database_path"])
        source_attachments = defaultdict(list)
        for r in db.execute("SELECT * FROM attachments ORDER BY message_id,id"):
            source_attachments[r["message_id"]].append(dict(r))
        users = {r["id"]: dict(r) for r in db.execute("SELECT * FROM users")}
        threads = {r["id"]: dict(r) for r in db.execute("SELECT * FROM threads")}
        n = 0
        seen = set()
        for path in sorted((export_dir / h["server_slug"] / "messages").glob("*/*.jsonl")):
            if path.stat().st_size > PAGE_BYTES:
                raise ValueError(f"Shard exceeds size budget: {path}")
            for record in read_jsonl(path)[1:]:
                original = db.execute("SELECT * FROM messages WHERE id=?", (record["id"],)).fetchone()
                if record["id"] in seen or not original or any(record[k] != original[k] for k in original.keys()):
                    raise ValueError(f"Message differs: {record['id']}")
                seen.add(record["id"])
                if record["attachments"] != source_attachments[record["id"]]:
                    raise ValueError(f"Attachments differ: {record['id']}")
                if record["author"] != users.get(record["author_id"]) or record["thread"] != threads.get(record.get("thread_id")):
                    raise ValueError(f"Author/thread differs: {record['id']}")
                n += 1
        db.close()
        if n != h["message_count"]:
            raise ValueError(f"Message count differs: {h['server_slug']}")
        totals[h["server_slug"]] = n
    return {"verified_files": count, "messages": totals}


def check_freshness(repo, export_dir):
    """CI check against hydrated sources OR their LFS pointer SHA-256 values."""
    catalog = json.loads((export_dir / "catalog.json").read_text())
    if catalog["generator_sha256"] != sha256(Path(__file__)):
        raise ValueError("Exporter changed; rebuild the retrieval export")
    for path, checksum in catalog["inputs"].items():
        if sha256(repo / path) != checksum:
            raise ValueError(f"Registry changed: {path}; rebuild export")
    expected = {h["database_path"]: h["database_sha256"] for h in catalog["harvests"]}
    actual = {p.relative_to(repo).as_posix() for p in (repo / "discord").glob("*/*.sqlite")}
    if actual != set(expected):
        raise ValueError("Harvest inventory changed; rebuild export")
    for path, checksum in expected.items():
        source = repo / path
        with source.open("rb") as f:
            header = f.read(200)
        if header.startswith(b"version https://git-lfs.github.com/spec/v1\n"):
            match = re.search(rb"oid sha256:([a-f0-9]{64})\n", header)
            digest = match.group(1).decode() if match else None
        else:
            digest = sha256(source)
        if digest != checksum:
            raise ValueError(f"Source changed: {path}; rebuild export")
    return {"fresh": True, "harvests": len(expected), "verified_files": verify_export_files(export_dir)}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root", type=Path, default=ROOT)
    p.add_argument("--export-dir", type=Path, default=DEFAULT_EXPORT)
    p.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    sub = p.add_subparsers(dest="command", required=True)
    for name in ("export", "build-index", "verify", "check-freshness"):
        sub.add_parser(name)
    for name in ("search", "lookup", "get", "attachments"):
        q = sub.add_parser(name)
        if name in ("search", "lookup", "attachments"):
            q.add_argument("query", nargs="?", default="")
        q.add_argument("--campaign")
        if name == "lookup":
            q.add_argument("--prefix", action="store_true")
            continue
        q.add_argument("--channel")
        q.add_argument("--author")
        q.add_argument("--exact", action="store_true")
        q.add_argument("--prefix", action="store_true")
        q.add_argument("--no-aliases", action="store_true")
        q.add_argument("--has-attachment", action="store_true")
        q.add_argument("--limit", type=int, default=10)
        q.add_argument("--offset", type=int, default=0)
        q.add_argument("--context", type=int, default=0)
        q.add_argument("--message-id", required=name == "get")
        q.add_argument("--attachment-id")
    a = p.parse_args(argv)
    try:
        if a.command == "export":
            result = export(a.repo_root, a.export_dir)
        elif a.command == "build-index":
            result = build_index(a.export_dir, a.index)
        elif a.command == "verify":
            result = verify(a.repo_root, a.export_dir)
        elif a.command == "check-freshness":
            result = check_freshness(a.repo_root, a.export_dir)
        elif a.command == "lookup":
            result = lookup(a.export_dir, a.campaign, a.query, a.prefix)
        else:
            if not 1 <= a.limit <= 100 or a.offset < 0 or not 0 <= a.context <= 20:
                raise ValueError("limit must be 1..100, offset >= 0, context 0..20")
            result = search(a.export_dir, a.index, query=getattr(a, "query", ""), campaign=a.campaign,
                channel=a.channel, author=a.author, exact=a.exact, prefix=a.prefix, aliases=not a.no_aliases,
                has_attachment=a.has_attachment or a.command == "attachments", limit=a.limit, offset=a.offset,
                context=a.context, message_id=a.message_id, attachment_id=a.attachment_id)
        print(dumps(result))
    except (ValueError, sqlite3.Error, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
