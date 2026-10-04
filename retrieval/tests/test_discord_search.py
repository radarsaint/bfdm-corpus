import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from retrieval import discord_search as ds


SCHEMA = """
CREATE TABLE servers(id TEXT PRIMARY KEY,name TEXT,harvested_at TEXT);
CREATE TABLE channels(id TEXT PRIMARY KEY,server_id TEXT,name TEXT,type TEXT,category TEXT,topic TEXT,position INTEGER);
CREATE TABLE threads(id TEXT PRIMARY KEY,channel_id TEXT,name TEXT,created_at TEXT,archived INTEGER);
CREATE TABLE users(id TEXT PRIMARY KEY,username TEXT,display_name TEXT,is_bot INTEGER);
CREATE TABLE messages(id TEXT PRIMARY KEY,channel_id TEXT,thread_id TEXT,author_id TEXT,created_at TEXT,edited_at TEXT,content TEXT,reply_to_id TEXT);
CREATE TABLE attachments(id TEXT PRIMARY KEY,message_id TEXT,filename TEXT,url TEXT,content_type TEXT,size INTEGER,sha256 TEXT,local_path TEXT);
CREATE TABLE reactions(message_id TEXT,emoji TEXT,count INTEGER);
"""


class RetrievalTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "repo"
        self.output = Path(self.temp.name) / "export"
        self.index = Path(self.temp.name) / "cache/search.sqlite"
        (self.repo / "registry").mkdir(parents=True)
        registry, entities = [], []
        for slug, sid in (("alpha", "1"), ("beta", "2")):
            path = self.repo / f"discord/{slug}/{slug}.sqlite"
            path.parent.mkdir(parents=True)
            db = sqlite3.connect(path)
            db.executescript(SCHEMA)
            db.execute("INSERT INTO servers VALUES(?,?,?)", (sid, slug.title(), "2020-01-01T00:00:00Z"))
            db.executemany("INSERT INTO channels VALUES(?,?,?,?,?,?,?)", [("10", sid, "character-introduction", "text", "Lore", None, 0), ("20", sid, "tavern", "text", "Play", None, 1)])
            db.executemany("INSERT INTO users VALUES(?,?,?,?)", [("100", "first", "Same Name", 0), ("200", "second", "Same Name", 0)])
            db.execute("INSERT INTO threads VALUES('30','20','Side thread',NULL,0)")
            records = [
                ("101", "10", None, "100", "2020-01-01T00:00:00Z", None, 'Sandigill says: "Call me Gill."', None),
                ("102", "10", None, "100", "2020-01-01T00:01:00Z", None, "Gill wears a blue cloak.", "101"),
                ("103", "10", None, "200", "2020-01-01T00:02:00Z", None, "A blue cotton cloak.", None),
                ("104", "20", None, "100", "2020-01-01T00:03:00Z", None, None, None),
                ("105", "20", "30", "200", "2020-01-01T00:04:00Z", None, "Gill enters the side thread.", "104"),
                ("106", "20", None, "200", "2020-01-01T00:05:00Z", None, "Guild guards arrive. Café naïve.", None),
            ]
            db.executemany("INSERT INTO messages VALUES(?,?,?,?,?,?,?,?)", records)
            db.execute("INSERT INTO attachments VALUES('900','104','portrait.png','https://example.invalid/a','image/png',12,'abc',?)", (f"discord/{slug}/attachments/20/900-portrait.png",))
            db.commit()
            db.close()
            registry.append({"server_id": sid, "project_ids": [slug]})
            entities.append({"entity_key": slug + ":sandigill", "server_id": sid, "canonical_name": "Sandigill", "aliases": ["Sandigill", "Sandigil", "Gill", "Gil"], "support": [{"database_path": f"discord/{slug}/{slug}.sqlite", "message_id": "101"}]})
        for filename, rows in (("discord_servers.jsonl", registry), ("discord_entities.jsonl", entities), ("projects.jsonl", [{"project_id": "alpha", "title": "Alpha Campaign", "aliases": [{"name": "A Season 3"}]}])):
            (self.repo / "registry" / filename).write_text("".join(ds.dumps(r) + "\n" for r in rows))
        ds.export(self.repo, self.output)

    def query(self, **kwargs):
        return ds.search(self.output, self.index, **kwargs)

    def test_aliases_and_no_lfs_consumer(self):
        # The consumer succeeds after the canonical databases have been removed.
        for path in self.repo.glob("discord/*/*.sqlite"):
            path.unlink()
        result = self.query(query="Gil", campaign="A Season 3")
        self.assertEqual(result["total"], 3)
        self.assertEqual(result["alias_evidence"][0]["id"], "101")
        self.assertEqual(result["hits"][1]["reply_to_id"], "101")
        self.assertEqual(self.query(query="Sandigil", campaign="alpha")["total"], 3)
        self.assertEqual(self.query(query="Gil", campaign="alpha", aliases=False)["total"], 0)

    def test_exact_phrase_prefix_and_punctuation(self):
        self.assertEqual(self.query(query="blue cloak", exact=True)["total"], 2)
        self.assertEqual(self.query(query="blue cloak")["total"], 4)
        self.assertEqual(self.query(query="guild", prefix=True)["total"], 2)
        self.assertEqual(self.query(query="cafe naive", exact=True)["total"], 2)
        self.assertEqual(self.query(query='x" OR delete', exact=True)["total"], 0)

    def test_ambiguity_is_retained_and_scoped(self):
        both = self.query(query="Gil")
        self.assertTrue(both["ambiguous"])
        self.assertEqual(len(both["entities"]), 2)
        self.assertEqual({m["server_slug"] for m in both["hits"]}, {"alpha", "beta"})
        self.assertFalse(self.query(query="Gil", campaign="alpha")["ambiguous"])
        # Same display name never implies one person.
        named = self.query(author="Same Name", campaign="alpha")
        self.assertEqual({m["author_id"] for m in named["hits"]}, {"100", "200"})

    def test_common_alias_within_same_campaign(self):
        path = self.repo / "registry/discord_entities.jsonl"
        entities = ds.read_jsonl(path)
        entities.append({**entities[0], "entity_key": "alpha:other-gil", "canonical_name": "Other Gil", "aliases": ["Gil"]})
        path.write_text("".join(ds.dumps(e) + "\n" for e in entities))
        ds.export(self.repo, self.output)
        r = self.query(query="Gil", campaign="alpha")
        self.assertTrue(r["ambiguous"])
        self.assertEqual(len(r["entities"]), 2)
        self.assertEqual(len(r["alias_evidence"]), 1)

    def test_filters_attachments_and_provenance(self):
        r = self.query(campaign="alpha", channel="tavern", author="100", has_attachment=True)
        self.assertEqual(r["total"], 1)
        m = r["hits"][0]
        self.assertEqual(m["id"], "104")
        self.assertEqual(m["provenance"]["database_path"], "discord/alpha/alpha.sqlite")
        self.assertEqual(m["attachments"][0]["id"], "900")
        self.assertEqual(self.query(query="portrait.png", campaign="alpha")["total"], 1)
        self.assertEqual(self.query(attachment_id="900", campaign="alpha")["hits"][0]["id"], "104")
        self.assertEqual(self.query(query="Gil", campaign="alpha", channel="10", author="100")["total"], 2)

    def test_reply_context_and_thread_boundaries(self):
        m = self.query(campaign="alpha", message_id="102", context=2)["hits"][0]
        self.assertEqual(m["context"]["reply_to"]["id"], "101")
        self.assertEqual([x["id"] for x in m["context"]["before"]], ["101"])
        t = self.query(campaign="alpha", message_id="105", context=2)["hits"][0]
        self.assertEqual(t["context"]["before"], [])
        self.assertEqual(t["context"]["after"], [])
        self.assertEqual(t["context"]["reply_to"]["id"], "104")

    def test_text_only_navigation(self):
        result = ds.lookup(self.output, "alpha", "Sandigil")
        self.assertIn("sandigill", {r["term"] for r in result["matches"]})
        for r in result["matches"]:
            for shard in r["shards"]:
                records = ds.read_jsonl(self.output / "alpha" / shard["path"])
                self.assertEqual(records[0]["database_path"], "discord/alpha/alpha.sqlite")
        self.assertTrue(ds.lookup(self.output, "alpha", "s", prefix=True)["matches"])
        self.assertTrue(ds.lookup(self.output, "alpha", "sand", prefix=True)["matches"])

    def test_pagination(self):
        r = self.query(campaign="alpha", limit=2)
        self.assertEqual(r["total"], 6)
        self.assertEqual(r["next_offset"], 2)
        self.assertEqual(self.query(campaign="alpha", limit=2, offset=4)["next_offset"], None)

    def test_determinism_and_source_parity(self):
        before = {p.relative_to(self.output): ds.sha256(p) for p in self.output.rglob("*") if p.is_file()}
        expected_sources = {p: ds.sha256(p) for p in self.repo.glob("discord/*/*.sqlite")}
        ds.export(self.repo, self.output)
        after = {p.relative_to(self.output): ds.sha256(p) for p in self.output.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        self.assertEqual(expected_sources, {p: ds.sha256(p) for p in expected_sources})
        self.assertEqual(ds.verify(self.repo, self.output)["messages"], {"alpha": 6, "beta": 6})

    def test_unhydrated_archive_does_not_replace_good_export(self):
        before = ds.sha256(self.output / "checksums/index.json")
        path = self.repo / "discord/alpha/alpha.sqlite"
        path.write_text("version https://git-lfs.github.com/spec/v1\n")
        with self.assertRaisesRegex(ValueError, "hydrated"):
            ds.export(self.repo, self.output)
        self.assertEqual(before, ds.sha256(self.output / "checksums/index.json"))

    def test_tamper_and_stale_index_detection(self):
        self.query(query="Gill")
        path = self.repo / "discord/alpha/alpha.sqlite"
        db = sqlite3.connect(path)
        db.execute("UPDATE messages SET content='Different' WHERE id='101'")
        db.commit()
        db.close()
        ds.export(self.repo, self.output)
        with self.assertRaisesRegex(ValueError, "stale"):
            self.query(query="Gill")
        shard = next((self.output / "alpha/messages").glob("*/*.jsonl"))
        shard.write_text(shard.read_text() + "\n")
        with self.assertRaisesRegex(ValueError, "differs"):
            ds.build_index(self.output, self.index)

    def test_bounded_pages_never_truncate(self):
        rows = [{"id": str(i), "content": "x" * 50} for i in range(6)]
        directory = Path(self.temp.name) / "pages"
        pages = ds.write_pages(directory, rows, key="id", max_bytes=160)
        self.assertEqual(sum(p["records"] for p in pages), 6)
        self.assertTrue(all(p["bytes"] <= 160 for p in pages))
        with self.assertRaisesRegex(ValueError, "Oversized"):
            ds.write_pages(directory, [{"content": "x" * 200}], max_bytes=160)

    def test_freshness_without_lfs_bytes_and_new_harvest(self):
        for path in self.repo.glob("discord/*/*.sqlite"):
            digest = ds.sha256(path)
            size = path.stat().st_size
            path.write_text(f"version https://git-lfs.github.com/spec/v1\noid sha256:{digest}\nsize {size}\n")
        self.assertTrue(ds.check_freshness(self.repo, self.output)["fresh"])
        other = self.repo / "discord/new/new.sqlite"
        other.parent.mkdir()
        other.write_text("pointer")
        with self.assertRaisesRegex(ValueError, "inventory"):
            ds.check_freshness(self.repo, self.output)


if __name__ == "__main__":
    unittest.main()
