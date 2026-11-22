"""Foundry publishing pilot: exercise the actual Discord projection exporter."""
import contextlib
import hashlib
import io
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import export_discord_model_index as exporter  # noqa: E402


def make_database(path):
    db = sqlite3.connect(str(path))
    db.executescript("""
        CREATE TABLE channels (id TEXT PRIMARY KEY, name TEXT, category TEXT);
        CREATE TABLE threads (id TEXT PRIMARY KEY, name TEXT);
        CREATE TABLE users (id TEXT PRIMARY KEY, username TEXT, display_name TEXT, is_bot INTEGER);
        CREATE TABLE messages (
            id TEXT PRIMARY KEY, created_at TEXT, edited_at TEXT, content TEXT,
            reply_to_id TEXT, channel_id TEXT, thread_id TEXT, author_id TEXT
        );
        INSERT INTO channels VALUES ('c1', 'town-square', 'main');
        INSERT INTO users VALUES ('u1', 'player', 'Player', 0);
        INSERT INTO messages VALUES ('m1', '2020-01-01T00:00:00Z', NULL, 'A mysterious door opens', NULL, 'c1', NULL, 'u1');
        INSERT INTO messages VALUES ('m2', '2020-01-01T00:01:00Z', NULL, 'The door closes again', NULL, 'c1', NULL, 'u1');
    """)
    db.commit()
    db.close()


class ProjectionPublicationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.db = root / "example.sqlite"
        self.outroot = root / "projection"
        self.output = self.outroot / "example"
        make_database(self.db)

    def run_export(self, **overrides):
        args = ["export_discord_model_index.py", str(self.db), "--out-root", str(self.outroot)]
        if "shard_messages" in overrides:
            args.extend(["--shard-messages", str(overrides["shard_messages"])])
        with patch.object(sys, "argv", args), contextlib.redirect_stdout(io.StringIO()):
            exporter.main()

    def snapshot(self):
        return {p.relative_to(self.output).as_posix(): p.read_bytes()
                for p in self.output.rglob("*") if p.is_file()}

    def test_completed_export_uses_final_paths_and_valid_hashes(self):
        self.run_export(shard_messages=1)
        manifest = json.loads((self.output / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["message_count"], 2)
        self.assertEqual(len(manifest["files"]), 2)
        self.assertEqual(manifest["term_index"]["directory"], str(self.output / "terms"))
        for item in manifest["files"] + manifest["term_index"]["files"]:
            path = Path(item["path"])
            self.assertTrue(path.is_file(), item)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), item["sha256"])
        first = self.snapshot()
        self.run_export(shard_messages=1)
        self.assertEqual(first, self.snapshot())

    def test_module_import_keeps_working(self):
        import importlib
        module = importlib.import_module("scripts.export_discord_model_index")
        self.assertTrue(callable(module.main))

    def test_failed_rebuild_preserves_every_previous_shard_and_manifest(self):
        self.run_export(shard_messages=1)
        before = self.snapshot()
        real_dump = exporter.dump
        counter = [0]
        def fail_on_second_message(obj):
            counter[0] += 1
            if counter[0] == 2:
                raise RuntimeError("simulated JSONL serialization failure")
            return real_dump(obj)
        with patch.object(exporter, "dump", side_effect=fail_on_second_message):
            with self.assertRaisesRegex(RuntimeError, "simulated"):
                self.run_export(shard_messages=2)
        self.assertEqual(before, self.snapshot())
        self.assertFalse(list(self.outroot.glob(".example.stage-*")))
        self.assertFalse((self.outroot / ".example.foundry-backup").exists())

    def test_failed_swap_restores_old_projection(self):
        self.run_export()
        before = self.snapshot()
        real_replace = __import__("os").replace
        counter = [0]
        def fail_new_tree_rename(*args):
            counter[0] += 1
            if counter[0] == 2:
                raise OSError("simulated promotion failure")
            return real_replace(*args)
        with patch("_foundry_publish.os.replace", side_effect=fail_new_tree_rename):
            with self.assertRaisesRegex(OSError, "simulated"):
                self.run_export(shard_messages=1)
        self.assertEqual(before, self.snapshot())


if __name__ == "__main__":
    unittest.main()
