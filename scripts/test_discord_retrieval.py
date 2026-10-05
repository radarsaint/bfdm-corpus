#!/usr/bin/env python3
"""Retrieval tests for the Discord search layer.

Synthetic rows cover the mechanics. The Roanoke tests use the checked-out
projection and, when present, the hydrated S3 database. They do not embed a
character summary.
"""

from __future__ import annotations

import json
import hashlib
import sqlite3
import subprocess
import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from discord_index import RetrievalError, export_attachments, search, sqlite_usable  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
S3 = ROOT / "discord/roanoke-season-3/roanoke-season-3.sqlite"
INTRO_ID = "739533579134042193"
ATTACHMENT_ID = "737113252726702111"


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def _refresh_fixture_manifest(root: Path) -> None:
    base = root / "model-index/discord/example"
    def entry(path):
        data = path.read_bytes()
        return {"path": path.relative_to(root).as_posix(), "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest()}
    files = []
    for path in sorted(base.glob("messages-*.jsonl")):
        files.append({**entry(path), "messages": len(path.read_text().splitlines())})
    manifest = {"source_database": "discord/example/example.sqlite", "source_database_sha256": "a" * 64,
                "message_count": sum(item["messages"] for item in files), "files": files,
                "term_index": {"files": [{**entry(path), "prefix": path.stem} for path in sorted((base / "terms").glob("*.jsonl"))]}}
    (base / "manifest.json").write_text(json.dumps(manifest))
    (base / "attachments-manifest.json").write_text(json.dumps({
        **entry(base / "attachments.jsonl"), "source_database_sha256": "a" * 64}))


def _mini_repo(root: Path) -> None:
    (root / "discord").mkdir()
    (root / "CORPUS_CHARTER.md").write_text("charter\n", encoding="utf-8")
    _write_jsonl(
        root / "registry" / "discord_servers.jsonl",
        [
            {
                "database_path": "discord/example/example.sqlite",
                "project_ids": ["example-campaign"],
                "server_name": "Example Campaign",
                "server_slug": "example",
            }
        ],
    )
    _write_jsonl(
        root / "model-index" / "discord" / "example" / "aliases.jsonl",
        [
            {
                "aliases": ["Sandigil", "Sandigill", "Gil", "Sandi"],
                "canonical": "Sandigill",
                "entity_id": "alias:example:sandigill",
                "server": "example",
            }
        ],
    )
    (root / "model-index" / "discord" / "example" / "manifest.json").write_text("{}\n", encoding="utf-8")
    messages = [
        {
            "author_id": "u1",
            "channel": "town-square",
            "channel_id": "c1",
            "content": "my name is Sandigil of the Twin Vents. they call me Sandi or Gil.",
            "created_at": "2020-08-01T00:00:00Z",
            "display_name": "Hek",
            "id": "m-intro",
            "reply_to_id": None,
            "thread": None,
            "thread_id": None,
            "username": "hekiryuu",
        },
        {
            "author_id": "u2",
            "channel": "out-of-character",
            "channel_id": "c2",
            "content": "Gilbert brought the map.",
            "created_at": "2020-08-01T00:01:00Z",
            "display_name": "Mapkeeper",
            "id": "m-gilbert",
            "reply_to_id": "m-intro",
            "thread": None,
            "thread_id": None,
            "username": "mapkeeper",
        },
        {
            "author_id": "u2",
            "channel": "out-of-character",
            "channel_id": "c2",
            "content": "sandigill while everyone is arguing",
            "created_at": "2020-08-01T00:02:00Z",
            "display_name": "Mapkeeper",
            "id": "m-attach",
            "reply_to_id": None,
            "thread": None,
            "thread_id": None,
            "username": "mapkeeper",
        },
    ]
    _write_jsonl(root / "model-index" / "discord" / "example" / "messages-0001.jsonl", messages)
    _write_jsonl(
        root / "model-index" / "discord" / "example" / "terms" / "san.jsonl",
        [
            {"message_count": 2, "shards": ["messages-0001.jsonl"], "token": "sandi"},
            {"message_count": 1, "shards": ["messages-0001.jsonl"], "token": "sandigil"},
            {"message_count": 1, "shards": ["messages-0001.jsonl"], "token": "sandigill"},
        ],
    )
    _write_jsonl(
        root / "model-index" / "discord" / "example" / "terms" / "twi.jsonl",
        [{"message_count": 1, "shards": ["messages-0001.jsonl"], "token": "twin"}],
    )
    _write_jsonl(
        root / "model-index" / "discord" / "example" / "terms" / "ven.jsonl",
        [{"message_count": 1, "shards": ["messages-0001.jsonl"], "token": "vents"}],
    )
    _write_jsonl(
        root / "model-index" / "discord" / "example" / "terms" / "gil.jsonl",
        [
            {"message_count": 1, "shards": ["messages-0001.jsonl"], "token": "gil"},
            {"message_count": 1, "shards": ["messages-0001.jsonl"], "token": "gilbert"},
            {"message_count": 1, "shards": ["messages-0001.jsonl"], "token": "gill"},
            {"message_count": 1, "shards": ["messages-0001.jsonl"], "token": "gilligan"},
        ],
    )
    _write_jsonl(
        root / "model-index" / "discord" / "example" / "attachments.jsonl",
        [
            {
                "channel": "out-of-character",
                "channel_id": "c2",
                "content_type": "image/png",
                "created_at": "2020-08-01T00:02:00Z",
                "filename": "unknown.png",
                "id": "a1",
                "local_path": "discord/example/attachments/c2/a1-unknown.png",
                "message_id": "m-attach",
                "sha256": "abc",
                "size": 10,
            }
        ],
    )
    pointer = root / "discord" / "example" / "example.sqlite"
    pointer.parent.mkdir(parents=True, exist_ok=True)
    pointer.write_text(
        "version https://git-lfs.github.com/spec/v1\noid sha256:" + "a" * 64 + "\nsize 1\n",
        encoding="utf-8",
    )
    _refresh_fixture_manifest(root)


class ProjectionMechanics(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        _mini_repo(self.repo)

    def tearDown(self):
        self.tmp.cleanup()

    def test_alias_does_not_swallow_gilbert(self):
        result = search(self.repo, "Gil", server="example", source="projection", limit=20)
        self.assertEqual(result["entity"]["entity_id"], "alias:example:sandigill")
        self.assertEqual(result["aliases_expanded"], ["gil", "sandi", "sandigil", "sandigill"])
        self.assertNotIn("gilbert", result["aliases_expanded"])
        self.assertIn("gilbert", result["ambiguous_neighbors"])
        self.assertIn("gill", result["ambiguous_neighbors"])
        ids = {hit["message_id"] for hit in result["hits"]}
        self.assertIn("m-intro", ids)
        self.assertIn("m-attach", ids)
        self.assertNotIn("m-gilbert", ids)
        self.assertEqual(result["lead_hits"][0]["message_id"], "m-intro")
        self.assertTrue(all(name.startswith("gil") for name in result["ambiguous_neighbors"]))
        hit = next(item for item in result["hits"] if item["message_id"] == "m-intro")
        self.assertEqual(hit["server"], "example")
        self.assertEqual(hit["channel_id"], "c1")
        self.assertEqual(hit["author_id"], "u1")
        self.assertEqual(hit["username"], "hekiryuu")
        self.assertEqual(hit["created_at"], "2020-08-01T00:00:00Z")
        self.assertEqual(hit["shard"], "messages-0001.jsonl")
        self.assertEqual(result["coverage_report"]["status"], "EXHAUSTIVE")
        self.assertEqual(result["coverage_report"]["reason_codes"], [])
        self.assertTrue(result["coverage_report"]["zero_match_means_absence"])
        self.assertFalse(result["coverage_report"]["absence_is_not_evidence"])
        self.assertEqual(result["coverage_report"]["canonical_database_state"], "lfs_pointer")
        self.assertFalse(result["coverage_report"]["database_usable"])

    def test_phrase_channel_author_and_attachment(self):
        phrase = search(self.repo, "Twin Vents", server="example", phrase=True, source="projection")
        self.assertEqual(phrase["aliases_expanded"], [])
        self.assertEqual([hit["message_id"] for hit in phrase["hits"]], ["m-intro"])
        channel = search(self.repo, "Gil", server="example", channel="town-square", source="projection")
        self.assertEqual([hit["message_id"] for hit in channel["hits"]], ["m-intro"])
        author = search(self.repo, "Gil", server="example", author="mapkeeper", source="projection")
        self.assertEqual([hit["message_id"] for hit in author["hits"]], ["m-attach"])
        attached = search(self.repo, "Gil", server="example", attachments_only=True, source="projection")
        self.assertEqual(len(attached["hits"]), 1)
        self.assertEqual(attached["hits"][0]["attachments"][0]["filename"], "unknown.png")
        self.assertNotIn("url", attached["hits"][0]["attachments"][0])
        self.assertEqual(attached["hits"][0]["reply_to_id"], None)

    def test_repeat_is_deterministic(self):
        first = search(self.repo, "Gil", server="example", source="projection")
        second = search(self.repo, "Gil", server="example", source="projection")
        self.assertEqual(first, second)

    def test_native_id_filters(self):
        result = search(self.repo, "Gil", server="example", channel="c1", author="u1")
        self.assertEqual([hit["message_id"] for hit in result["hits"]], ["m-intro"])

    def test_common_alias_requires_disambiguation(self):
        path = self.repo / "model-index/discord/example/aliases.jsonl"
        with path.open("a") as handle:
            handle.write(json.dumps({"entity_id": "another-gil", "canonical": "Gil", "aliases": []}) + "\n")
        with self.assertRaises(RetrievalError) as raised:
            search(self.repo, "Gil", server="example")
        self.assertEqual(raised.exception.code, "ambiguous_alias")

    def test_stale_source_cannot_claim_absence(self):
        pointer = self.repo / "discord/example/example.sqlite"
        pointer.write_text(pointer.read_text().replace("a" * 64, "b" * 64))
        result = search(self.repo, "Gil", server="example")
        self.assertEqual(result["coverage_report"]["status"], "PARTIAL")
        self.assertIn("stale_or_unverified_projection", result["coverage_report"]["reason_codes"])
        self.assertFalse(result["coverage_report"]["zero_match_means_absence"])

    def test_missing_attachments_cannot_claim_absence(self):
        (self.repo / "model-index/discord/example/attachments.jsonl").unlink()
        result = search(self.repo, "Gil", server="example", attachments_only=True)
        self.assertEqual(result["returned"], 0)
        self.assertEqual(result["coverage_report"]["status"], "PARTIAL")

    def test_modified_term_index_cannot_claim_exhaustive(self):
        path = self.repo / "model-index/discord/example/terms/san.jsonl"
        path.write_text(path.read_text() + "\n")
        result = search(self.repo, "Gil", server="example")
        self.assertIn("projection_checksum_mismatch", result["coverage_report"]["reason_codes"])
        self.assertEqual(result["coverage_report"]["status"], "PARTIAL")

    def test_missing_shard_cannot_claim_exhaustive(self):
        (self.repo / "model-index/discord/example/messages-0001.jsonl").unlink()
        result = search(self.repo, "Gil", server="example")
        self.assertEqual(result["coverage_report"]["status"], "PARTIAL")

    def test_short_and_multiword_queries(self):
        short = search(self.repo, "my", server="example")
        self.assertEqual(short["match_count"], 1)
        phrase = search(self.repo, "Twin Vents", server="example")
        self.assertEqual(phrase["match_count"], 1)
        absent = search(self.repo, "zzzzneverpresent", server="example")
        self.assertEqual(absent["match_count"], 0)
        self.assertTrue(absent["coverage_report"]["zero_match_means_absence"])

    def test_pointer_export_preserves_existing_projection(self):
        path = self.repo / "model-index/discord/example/messages-0001.jsonl"
        before = path.read_bytes()
        result = subprocess.run([sys.executable, str(ROOT / "scripts/export_discord_model_index.py"),
                                 "discord/example/example.sqlite"], cwd=self.repo, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(path.read_bytes(), before)

    def test_pointer_without_projection_is_not_absence(self):
        bare = Path(self.tmp.name) / "bare"
        (bare / "discord").mkdir(parents=True)
        (bare / "CORPUS_CHARTER.md").write_text("charter\n", encoding="utf-8")
        _write_jsonl(
            bare / "registry" / "discord_servers.jsonl",
            [{"database_path": "discord/example/example.sqlite", "project_ids": ["example-campaign"], "server_name": "Example Campaign", "server_slug": "example"}],
        )
        pointer = bare / "discord" / "example" / "example.sqlite"
        pointer.parent.mkdir(parents=True, exist_ok=True)
        pointer.write_text("version https://git-lfs.github.com/spec/v1\noid sha256:abc\nsize 1\n", encoding="utf-8")
        result = search(bare, "Gil", server="example", source="auto")
        self.assertEqual(result["returned"], 0)
        self.assertEqual(result["coverage_report"]["status"], "INACCESSIBLE")
        self.assertEqual(result["coverage_report"]["reason_codes"], ["lfs_pointer_only"])
        self.assertFalse(result["coverage_report"]["zero_match_means_absence"])
        self.assertTrue(result["coverage_report"]["absence_is_not_evidence"])


class AttachmentExport(unittest.TestCase):
    def test_export_omits_url_and_is_stable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "discord").mkdir()
            (root / "CORPUS_CHARTER.md").write_text("charter\n", encoding="utf-8")
            database = root / "example.sqlite"
            connection = sqlite3.connect(database)
            connection.executescript(
                """
                CREATE TABLE channels (id TEXT PRIMARY KEY, name TEXT, category TEXT);
                CREATE TABLE messages (
                  id TEXT PRIMARY KEY, channel_id TEXT, created_at TEXT, content TEXT
                );
                CREATE TABLE attachments (
                  id TEXT PRIMARY KEY, message_id TEXT, filename TEXT, url TEXT,
                  content_type TEXT, size INTEGER, sha256 TEXT, local_path TEXT
                );
                INSERT INTO channels VALUES ('c1', 'town-square', NULL);
                INSERT INTO messages VALUES ('m1', 'c1', '2020-08-01T00:00:00Z', 'secret message body');
                INSERT INTO attachments VALUES ('a1', 'm1', 'portrait.png', 'https://cdn.example/secret', 'image/png', 4, 'ff', 'discord/example/attachments/c1/a1-portrait.png');
                """
            )
            connection.commit()
            connection.close()
            first = export_attachments(database, root, "example")
            payload = (root / "model-index" / "discord" / "example" / "attachments.jsonl").read_text(encoding="utf-8")
            second = export_attachments(database, root, "example")
            self.assertEqual(first["sha256"], second["sha256"])
            self.assertEqual(first["subordinate_to"], "discord/example/example.sqlite")
            self.assertNotIn("secret message body", payload)
            self.assertNotIn("cdn.example", payload)
            self.assertNotIn("url", json.loads(payload))


class RoanokeSeason3(unittest.TestCase):
    def test_projection_finds_introduction_and_attachment(self):
        intro = search(
            ROOT,
            '"Sandigil of the Twin Vents"',
            server="Roanoke Season 3",
            source="projection",
            limit=10,
        )
        self.assertEqual(intro["coverage_report"]["access"], "jsonl_projection")
        self.assertEqual(intro["coverage_report"]["status"], "EXHAUSTIVE")
        self.assertEqual(intro["coverage_report"]["project_ids"], ["roanoke-s3"])
        self.assertIn(intro["coverage_report"]["canonical_database_state"], ["lfs_pointer", "hydrated"])
        self.assertFalse(intro["coverage_report"]["absence_is_not_evidence"])
        self.assertTrue(any(hit["message_id"] == INTRO_ID for hit in intro["hits"]))
        intro_hit = next(hit for hit in intro["hits"] if hit["message_id"] == INTRO_ID)
        self.assertEqual(intro_hit["channel"], "town-square")
        self.assertEqual(intro_hit["username"], "hekiryuu")
        self.assertIn("message_id", intro_hit)
        self.assertTrue(intro_hit["created_at"])
        self.assertTrue(intro_hit["shard"])

        attached = search(
            ROOT,
            "Sandigil",
            server="roanoke-s3",
            attachments_only=True,
            source="projection",
            limit=20,
        )
        self.assertTrue(any(hit["message_id"] == ATTACHMENT_ID for hit in attached["hits"]))
        attachment_hit = next(hit for hit in attached["hits"] if hit["message_id"] == ATTACHMENT_ID)
        self.assertEqual(attachment_hit["attachments"][0]["filename"], "unknown.png")
        self.assertTrue(attachment_hit["attachments"][0]["local_path"].endswith("unknown.png"))
        self.assertNotIn("url", attachment_hit["attachments"][0])

        gil = search(ROOT, "Gil", server="roanoke-season-3", source="projection", limit=5)
        self.assertEqual(gil["entity"]["canonical"], "Sandigill")
        self.assertNotIn("gilbert", gil["aliases_expanded"])
        self.assertIn("gilbert", gil["ambiguous_neighbors"])
        self.assertTrue(all(name.startswith("gil") for name in gil["ambiguous_neighbors"]))
        self.assertTrue(any(hit["message_id"] == INTRO_ID for hit in gil["lead_hits"]))
        self.assertGreater(gil["match_count"], gil["returned"])
        again = search(ROOT, "Gil", server="roanoke-season-3", source="projection", limit=5)
        self.assertEqual(gil, again)

    def test_hydrated_sqlite_matches_projection_identity(self):
        if not sqlite_usable(S3):
            self.skipTest("hydrated S3 sqlite is not in this environment")
        result = search(
            ROOT,
            "Sandigil",
            server="Roanoke Season 3",
            source="sqlite",
            database=S3,
            channel="town-square",
            author="hekiryuu",
            limit=30,
        )
        self.assertEqual(result["coverage_report"]["access"], "hydrated_sqlite")
        self.assertEqual(result["coverage_report"]["status"], "EXHAUSTIVE")
        self.assertEqual(result["coverage_report"]["reason_codes"], [])
        self.assertTrue(any(hit["message_id"] == INTRO_ID for hit in result["hits"]))
        phrase = search(
            ROOT,
            "of the Twin Vents",
            server="roanoke-season-3",
            phrase=True,
            source="sqlite",
            database=S3,
            limit=20,
        )
        self.assertEqual(phrase["aliases_expanded"], [])
        self.assertTrue(all("of the twin vents" in hit["content"].casefold() for hit in phrase["hits"]))
        self.assertTrue(any(hit["message_id"] == INTRO_ID for hit in phrase["hits"]))
        for query in ("Sandigil", "Gil"):
            projected = search(ROOT, query, server="roanoke-s3", source="projection", limit=10000, full=True)
            hydrated = search(ROOT, query, server="roanoke-s3", source="sqlite", limit=10000, full=True)
            self.assertEqual(projected["match_count"], hydrated["match_count"])
            self.assertEqual([hit["message_id"] for hit in projected["hits"]],
                             [hit["message_id"] for hit in hydrated["hits"]])


if __name__ == "__main__":
    unittest.main()
