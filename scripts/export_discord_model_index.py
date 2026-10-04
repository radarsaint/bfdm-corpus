#!/usr/bin/env python3
"""Export a Discord SQLite harvest into GitHub-searchable non-LFS JSONL shards.

The SQLite database remains canonical. This projection is deterministic and rebuildable.
Shards are capped by byte size so GitHub/model code search can index them reliably.
"""
from __future__ import annotations
import argparse, hashlib, json, sqlite3
from pathlib import Path

def dump(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("database")
    ap.add_argument("--out-root", default="model-index/discord")
    ap.add_argument("--shard-messages", type=int, default=500,
                    help="Maximum messages per shard")
    ap.add_argument("--shard-bytes", type=int, default=250_000,
                    help="Target maximum UTF-8 bytes per shard")
    args=ap.parse_args()
    db=Path(args.database)
    slug=db.stem
    out=Path(args.out_root)/slug
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("messages-*.jsonl"):
        old.unlink()

    con=sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    con.row_factory=sqlite3.Row
    q="""SELECT m.id,m.created_at,m.edited_at,m.content,m.reply_to_id,
                m.channel_id,c.name channel,c.category,
                m.thread_id,t.name thread,
                m.author_id,u.username,u.display_name,u.is_bot
         FROM messages m
         JOIN channels c ON c.id=m.channel_id
         LEFT JOIN threads t ON t.id=m.thread_id
         LEFT JOIN users u ON u.id=m.author_id
         ORDER BY m.created_at,m.id"""
    cur=con.execute(q)
    files=[]; count=0; first=None; last=None
    fh=None; h=None; shard_bytes=0; shard_messages=0; shard_no=0

    def close_shard():
        nonlocal fh, h
        if fh:
            fh.close()
            files[-1]["sha256"]=h.hexdigest()
            fh=None
            h=None

    def open_shard():
        nonlocal fh, h, shard_bytes, shard_messages, shard_no
        shard_no += 1
        path=out/f"messages-{shard_no:04d}.jsonl"
        fh=path.open("w",encoding="utf-8",newline="\n")
        h=hashlib.sha256()
        shard_bytes=0
        shard_messages=0
        files.append({"path":path.as_posix(),"messages":0,"bytes":0,"sha256":None})

    try:
        for row in cur:
            obj=dict(row)
            line=(dump(obj)+"\n").encode("utf-8")
            if fh is None:
                open_shard()
            elif shard_messages >= args.shard_messages or (shard_bytes + len(line) > args.shard_bytes and shard_messages > 0):
                close_shard()
                open_shard()
            fh.write(line.decode("utf-8"))
            h.update(line)
            shard_bytes += len(line)
            shard_messages += 1
            files[-1]["messages"] += 1
            files[-1]["bytes"] = shard_bytes
            first=first or obj["created_at"]
            last=obj["created_at"]
            count += 1
    finally:
        close_shard()
        con.close()

    manifest={
        "schema_version":2,
        "source_database":db.as_posix(),
        "server_slug":slug,
        "message_count":count,
        "date_coverage":{"first":first,"last":last},
        "shard_limits":{"messages":args.shard_messages,"bytes":args.shard_bytes},
        "files":files
    }
    (out/"manifest.json").write_text(
        json.dumps(manifest,ensure_ascii=False,indent=2,sort_keys=True)+"\n",
        encoding="utf-8"
    )
    print(f"{slug}: {count} messages -> {len(files)} searchable shards")

if __name__=="__main__":
    main()
