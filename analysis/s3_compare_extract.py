#!/usr/bin/env python3
import csv, json, sqlite3, re
from pathlib import Path
from collections import defaultdict

DB = Path("discord/roanoke-season-3/roanoke-season-3.sqlite")
OUT = Path("analysis-output")
OUT.mkdir(exist_ok=True)

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row

def rows(sql, args=()):
    return con.execute(sql, args).fetchall()

def write_csv(name, records, fields=None):
    p = OUT / name
    records = list(records)
    if not records:
        p.write_text("", encoding="utf-8")
        return
    if fields is None:
        fields = list(records[0].keys())
    with p.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in records:
            w.writerow({k:r[k] for k in fields})

# Integrity + schema counts
meta = {}
meta["integrity_check"] = con.execute("PRAGMA integrity_check").fetchone()[0]
for table in ["servers","channels","threads","users","messages","attachments","reactions"]:
    meta[table] = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
meta["min_message"] = con.execute("SELECT MIN(created_at) FROM messages").fetchone()[0]
meta["max_message"] = con.execute("SELECT MAX(created_at) FROM messages").fetchone()[0]
(OUT/"meta.json").write_text(json.dumps(meta,indent=2),encoding="utf-8")

# Top users by total messages.
top_users = rows("""
SELECT u.id, u.username, u.display_name, u.is_bot, COUNT(*) AS messages
FROM messages m LEFT JOIN users u ON u.id=m.author_id
GROUP BY m.author_id
ORDER BY messages DESC
LIMIT 200
""")
write_csv("top_users.csv", top_users)

# Candidates likely to be Brendon based on names.
candidates = rows("""
SELECT u.id, u.username, u.display_name, u.is_bot, COUNT(m.id) AS messages
FROM users u LEFT JOIN messages m ON m.author_id=u.id
WHERE lower(coalesce(u.username,'')) LIKE '%brendon%'
   OR lower(coalesce(u.display_name,'')) LIKE '%brendon%'
   OR lower(coalesce(u.username,'')) LIKE '%faulk%'
   OR lower(coalesce(u.display_name,'')) LIKE '%faulk%'
   OR lower(coalesce(u.username,'')) LIKE '%radarsaint%'
   OR lower(coalesce(u.display_name,'')) LIKE '%radarsaint%'
GROUP BY u.id ORDER BY messages DESC
""")
write_csv("brendon_candidates.csv", candidates)

# Daily activity.
daily = rows("""
SELECT substr(created_at,1,10) AS day, COUNT(*) AS messages,
       COUNT(DISTINCT author_id) AS authors,
       COUNT(DISTINCT channel_id) AS channels
FROM messages GROUP BY day ORDER BY day
""")
write_csv("daily_activity.csv", daily)

# Top channels by total.
channel_stats = rows("""
SELECT c.id, c.category, c.name, COUNT(m.id) AS messages,
       MIN(m.created_at) AS first_message, MAX(m.created_at) AS last_message,
       COUNT(DISTINCT m.author_id) AS authors
FROM channels c LEFT JOIN messages m ON m.channel_id=c.id
GROUP BY c.id
ORDER BY messages DESC
""")
write_csv("channel_stats.csv", channel_stats)

# Top channels each day.
daily_channels = rows("""
WITH x AS (
 SELECT substr(m.created_at,1,10) AS day, c.category, c.name, c.id AS channel_id,
        COUNT(*) AS messages,
        ROW_NUMBER() OVER (PARTITION BY substr(m.created_at,1,10) ORDER BY COUNT(*) DESC) rn
 FROM messages m JOIN channels c ON c.id=m.channel_id
 GROUP BY day,c.id
)
SELECT day,category,name,channel_id,messages FROM x WHERE rn<=12 ORDER BY day,messages DESC
""")
write_csv("daily_top_channels.csv", daily_channels)

# Planning-derived terms. Broad enough to catch variants.
groups = {
"week1_father_thames":["father thames","fat friar","eponine"],
"week1_werewolf":["werewolf","jimmothy","la fleur"],
"week1_mummy":["mummy","sarcophagus","ogden"],
"week1_jekyll":["willamina","billie","grey render","jekyll","hyde","cadsberry","royal jelly"],
"week1_golden_dawn":["golden dawn","illuminati"],
"week1_twilight":["twilight manor","twilight","thames"],
"week2_sub":["tir na nog","submarine","airlock","command deck","engine room"],
"week2_mantapolis":["mantapolis","mantapolis"],
"week2_duckton":["duckton","duck"],
"week2_kraken":["kraken","leviathan"],
"week2_sabotage":["sabotage","sacrific"],
"week3_roanoke":["stillwater","roanoke island","hanging tree","croatoan"],
"week3_uru":["uru","vulture"],
"week3_chinnokin":["chinnokin"],
"week3_hags":["hag","coven"],
"week3_howler":["howler","myconoid"],
"week3_democracy":["democracy","election","mayor","town hall"],
"week4_darkwater":["darkwater"],
"week4_pen":["the pen","pen's curse","pens curse"],
"week4_chuul":["chuul"],
"week4_wendigo":["wendigo"],
"week4_levialich":["levialich","levi-lich","levi lich"],
"week5_aether":["aether"],
"week5_dregen":["dregen","ossuary"],
"week5_tinkers":["tinker","otis","iona","spellweaver"],
"week5_infernal_well":["infernal well","well"],
"week5_hunger":["the hunger","hunger","croatoan"],
"lodestones":["lodestone"],
"masonic":["free mason","freemason","masonic","hiram","pym"],
"roi_soleil":["roi soleil","sun king","machidiel","luna","eclipse knight"],
"kairo":["kairo"],
"golden_dawn":["golden dawn","illuminati"],
"player_building":["build","construction","town"],
}

# Count term hits by day, using LIKE so punctuation doesn't break FTS phrase syntax.
term_rows=[]
samples=[]
for group, terms in groups.items():
    ors=" OR ".join(["lower(coalesce(m.content,'')) LIKE ?" for _ in terms])
    params=[f"%{t.lower()}%" for t in terms]
    counts=rows(f"""
      SELECT substr(m.created_at,1,10) AS day, COUNT(*) AS hits
      FROM messages m
      WHERE {ors}
      GROUP BY day ORDER BY day
    """,params)
    for r in counts:
        term_rows.append({"group":group,"day":r["day"],"hits":r["hits"]})
    hitrows=rows(f"""
      SELECT m.id,m.channel_id,m.author_id,m.created_at,m.content,
             c.category,c.name AS channel,u.username,u.display_name
      FROM messages m JOIN channels c ON c.id=m.channel_id
      LEFT JOIN users u ON u.id=m.author_id
      WHERE {ors}
      ORDER BY m.created_at
    """,params)
    # chronologically stratified samples: first/last + evenly spread, max 24
    n=len(hitrows)
    idx=[]
    if n:
        take=min(24,n)
        idx=sorted(set(round(i*(n-1)/(take-1)) if take>1 else 0 for i in range(take)))
    for i in idx:
        r=hitrows[i]
        samples.append({
          "group":group,"id":r["id"],"created_at":r["created_at"],
          "category":r["category"],"channel":r["channel"],
          "author_id":r["author_id"],"username":r["username"],"display_name":r["display_name"],
          "content":r["content"]
        })

write_csv("term_hits_by_day.csv", term_rows, ["group","day","hits"])
with (OUT/"term_samples.jsonl").open("w",encoding="utf-8") as f:
    for s in samples:
        f.write(json.dumps(s,ensure_ascii=False)+"\n")

# Messages from likely Brendon candidates: sample by day and channel, plus explicit adjudication/action language.
candidate_ids=[r["id"] for r in candidates]
if candidate_ids:
    qs=",".join("?"*len(candidate_ids))
    br_daily=rows(f"""
      SELECT substr(m.created_at,1,10) day,c.category,c.name channel,COUNT(*) messages
      FROM messages m JOIN channels c ON c.id=m.channel_id
      WHERE m.author_id IN ({qs})
      GROUP BY day,c.id ORDER BY day,messages DESC
    """,candidate_ids)
    write_csv("brendon_daily_channels.csv",br_daily)

    action_patterns=[
      "%roll%","%dc %","%make a % check%","%initiative%","%you see%",
      "%you find%","%you hear%","%you notice%","%take % damage%",
      "%saving throw%","%you can%","%you may%","%you have%"
    ]
    aors=" OR ".join(["lower(coalesce(m.content,'')) LIKE ?" for _ in action_patterns])
    params=candidate_ids+action_patterns
    adjud=rows(f"""
      SELECT m.id,m.created_at,c.category,c.name channel,m.content,
             u.username,u.display_name
      FROM messages m JOIN channels c ON c.id=m.channel_id
      LEFT JOIN users u ON u.id=m.author_id
      WHERE m.author_id IN ({qs}) AND ({aors})
      ORDER BY m.created_at
      LIMIT 12000
    """,params)
    with (OUT/"brendon_adjudication_samples.jsonl").open("w",encoding="utf-8") as f:
        # stratify if enormous
        n=len(adjud); take=min(1200,n)
        indices=sorted(set(round(i*(n-1)/(take-1)) if take>1 else 0 for i in range(take))) if n else []
        for i in indices:
            r=adjud[i]
            f.write(json.dumps(dict(r),ensure_ascii=False)+"\n")

# Context windows around planning-term samples: previous/current/next two in same channel.
# This lets us see player action -> response without dumping the whole corpus.
sample_ids=[s["id"] for s in samples]
with (OUT/"term_context_windows.jsonl").open("w",encoding="utf-8") as f:
    for s in samples:
        target=con.execute("SELECT created_at,channel_id FROM messages WHERE id=?",(s["id"],)).fetchone()
        if not target: continue
        before=rows("""
          SELECT m.id,m.created_at,m.author_id,u.username,u.display_name,m.content
          FROM messages m LEFT JOIN users u ON u.id=m.author_id
          WHERE m.channel_id=? AND m.created_at < ?
          ORDER BY m.created_at DESC LIMIT 2
        """,(target["channel_id"],target["created_at"]))
        after=rows("""
          SELECT m.id,m.created_at,m.author_id,u.username,u.display_name,m.content
          FROM messages m LEFT JOIN users u ON u.id=m.author_id
          WHERE m.channel_id=? AND m.created_at > ?
          ORDER BY m.created_at ASC LIMIT 2
        """,(target["channel_id"],target["created_at"]))
        current=rows("""
          SELECT m.id,m.created_at,m.author_id,u.username,u.display_name,m.content
          FROM messages m LEFT JOIN users u ON u.id=m.author_id WHERE m.id=?
        """,(s["id"],))
        window=[dict(r) for r in reversed(before)]+[dict(r) for r in current]+[dict(r) for r in after]
        f.write(json.dumps({"group":s["group"],"category":s["category"],"channel":s["channel"],"window":window},ensure_ascii=False)+"\n")

# Meta/OOC channels potentially documenting live adaptation and decisions.
meta_channels = rows("""
SELECT c.id,c.category,c.name,COUNT(m.id) messages
FROM channels c LEFT JOIN messages m ON m.channel_id=c.id
WHERE lower(c.name) LIKE '%ooc%' OR lower(c.name) LIKE '%mod%'
   OR lower(c.name) LIKE '%rule%' OR lower(c.name) LIKE '%announce%'
   OR lower(c.name) LIKE '%help%' OR lower(c.category) LIKE '%dm%'
GROUP BY c.id ORDER BY messages DESC
""")
write_csv("meta_channels.csv",meta_channels)

con.close()
print(json.dumps(meta,indent=2))
