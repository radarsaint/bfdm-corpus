#!/usr/bin/env python3
"""Verify every projected record against canonical SQLite; optionally rebuild twice.

Run from the repository root after hydrating discord/*/*.sqlite. No source
content is printed. The JSON result contains counts and checksums only.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sqlite3
import subprocess
import sys

from discord_index import load_servers, projection_issues, source_digest, sqlite_usable


def rows(path):
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def snapshot(base):
    return {path.relative_to(base).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(base.rglob("*")) if path.is_file()}


def verify(repo, server):
    database = repo / server["database_path"]
    if not sqlite_usable(database):
        raise ValueError(f"Hydrate {server['database_path']} before source verification")
    issues = projection_issues(repo, server, database)
    if issues:
        raise ValueError(f"{server['server_slug']}: {issues}")
    digest = source_digest(database)
    base = repo / "model-index/discord" / server["server_slug"]
    manifest = json.loads((base / "manifest.json").read_text())
    con = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        canonical = con.execute("""
            SELECT m.id,m.created_at,m.edited_at,m.content,m.reply_to_id,
                   m.channel_id,c.name channel,c.category,m.thread_id,t.name thread,
                   m.author_id,u.username,u.display_name,u.is_bot
            FROM messages m JOIN channels c ON c.id=m.channel_id
            LEFT JOIN threads t ON t.id=m.thread_id
            LEFT JOIN users u ON u.id=m.author_id ORDER BY m.created_at,m.id
        """)
        projected = itertools.chain.from_iterable(rows(repo / item["path"]) for item in manifest["files"])
        count = 0
        for source, derived in itertools.zip_longest(canonical, projected):
            if source is None or derived is None or dict(source) != derived:
                raise ValueError(f"{server['server_slug']}: message parity failure at row {count}")
            count += 1
        if count != con.execute("SELECT count(*) FROM messages").fetchone()[0]:
            raise ValueError("Messages lost in a source join")
        canonical = con.execute("""
            SELECT a.id,a.message_id,a.filename,a.content_type,a.size,a.sha256,a.local_path,
                   m.created_at,m.channel_id,c.name channel
            FROM attachments a JOIN messages m ON m.id=a.message_id
            JOIN channels c ON c.id=m.channel_id ORDER BY m.created_at,m.id,a.id
        """)
        attachments = 0
        for source, derived in itertools.zip_longest(canonical, rows(base / "attachments.jsonl")):
            if source is None or derived is None or dict(source) != derived:
                raise ValueError(f"{server['server_slug']}: attachment parity failure at row {attachments}")
            stored = repo / derived["local_path"]
            if not stored.is_file():
                raise ValueError(f"Missing attachment reference: {derived['local_path']}")
            data = stored.read_bytes()
            if data.startswith(b"version https://git-lfs.github.com/spec/v1"):
                expected = f"oid sha256:{derived['sha256']}".encode()
                if expected not in data.splitlines():
                    raise ValueError(f"Attachment LFS OID mismatch: {derived['id']}")
            elif hashlib.sha256(data).hexdigest() != derived["sha256"]:
                raise ValueError(f"Attachment checksum mismatch: {derived['id']}")
            attachments += 1
        if attachments != con.execute("SELECT count(*) FROM attachments").fetchone()[0]:
            raise ValueError("Attachments lost in a source join")
        alias_path = base / "aliases.jsonl"
        if alias_path.is_file():
            for alias in rows(alias_path):
                for support in alias.get("support", []):
                    if support["canonical_database"] != server["database_path"]:
                        raise ValueError("Alias support database mismatch")
                    if not con.execute("SELECT 1 FROM messages WHERE id=?", (support["message_id"],)).fetchone():
                        raise ValueError("Alias support message missing from SQLite")
                    if not any(row["id"] == support["message_id"] for row in rows(repo / support["shard"])):
                        raise ValueError("Alias support shard reference is stale")
    finally:
        con.close()
    if source_digest(database) != digest:
        raise ValueError("Canonical SQLite changed during verification")
    return {"server": server["server_slug"], "messages": count, "attachments": attachments,
            "source_sha256": digest, "source_parity": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rebuild", action="store_true", help="Rebuild twice and require byte-identical output")
    args = parser.parse_args()
    repo = Path.cwd()
    servers = load_servers(repo)
    deterministic = None
    if args.rebuild:
        previous = None
        source_hashes = {server["server_slug"]: source_digest(repo / server["database_path"]) for server in servers}
        for attempt in range(2):
            for server in servers:
                for exporter in ("export_discord_model_index.py", "export_discord_attachments.py"):
                    subprocess.run([sys.executable, f"scripts/{exporter}", server["database_path"]], check=True, stdout=subprocess.DEVNULL)
            current = snapshot(repo / "model-index/discord")
            if previous is not None and current != previous:
                raise ValueError("Rebuilds are not byte-identical")
            previous = current
        if source_hashes != {server["server_slug"]: source_digest(repo / server["database_path"]) for server in servers}:
            raise ValueError("Rebuild modified canonical source bytes")
        deterministic = {"byte_identical": True, "files": len(previous), "builds": 2}
    print(json.dumps({"harvests": [verify(repo, server) for server in servers],
                      "determinism": deterministic}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
