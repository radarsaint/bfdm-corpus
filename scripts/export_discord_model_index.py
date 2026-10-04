#!/usr/bin/env python3
"""Export a Discord SQLite harvest into small, non-LFS JSONL shards for model retrieval.

The SQLite database remains canonical. This projection is deterministic and rebuildable.
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
    ap.add_argument("--shard-messages", type=int, default=2500)
    args=ap.parse_args()
    db=Path(args.database)
    slug=db.stem
    out=Path(args.out_root)/slug
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("messages-*.jsonl"): old.unlink()

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
    files=[]; count=0; first=None; last=None; fh=None; h=None; path=None
    try:
        for row in cur:
            if count % args.shard_messages == 0:
                if fh:
                    fh.close(); files[-1]["sha256"]=h.hexdigest()
                n=count//args.shard_messages+1
                path=out/f"messages-{n:04d}.jsonl"
                fh=path.open("w",encoding="utf-8",newline="\n"); h=hashlib.sha256()
                files.append({"path":path.as_posix(),"messages":0,"sha256":None})
            obj=dict(row)
            line=(dump(obj)+"\n").encode("utf-8")
            fh.write(line.decode("utf-8")); h.update(line)
            files[-1]["messages"]+=1
            first=first or obj["created_at"]; last=obj["created_at"]; count+=1
    finally:
        if fh:
            fh.close(); files[-1]["sha256"]=h.hexdigest()
        con.close()
    manifest={"schema_version":1,"source_database":db.as_posix(),"server_slug":slug,
              "message_count":count,"date_coverage":{"first":first,"last":last},
              "shard_messages":args.shard_messages,"files":files}
    (out/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(f"{slug}: {count} messages -> {len(files)} shards")

if __name__=="__main__": main()
