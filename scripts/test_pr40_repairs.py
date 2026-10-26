#!/usr/bin/env python3
"""Regression checks for the PR #40 review repairs."""

import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from build_documents_sqlite import build


ROOT = Path(__file__).resolve().parents[1]
ADMISSION = "2026-10-08T11:37:42Z"
PLACEHOLDER = "2026-10-08T12:00:00Z"


def metadata(corpus_id: str) -> dict:
    matches = list(ROOT.glob(f"sources/**/{corpus_id}/metadata.json"))
    if len(matches) != 1:
        raise AssertionError(f"expected one metadata file for {corpus_id}, found {matches}")
    return json.loads(matches[0].read_text(encoding="utf-8"))


def source_text(corpus_id: str) -> str:
    matches = list(ROOT.glob(f"sources/**/{corpus_id}/source.md"))
    if len(matches) != 1:
        raise AssertionError(matches)
    return matches[0].read_text(encoding="utf-8")


def catalog_row(corpus_id: str) -> dict:
    for line in (ROOT / "evidence" / "catalog.jsonl").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("corpus_id") == corpus_id:
            return row
    raise AssertionError(corpus_id)


class PR40RepairTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.db_path = Path(cls.tmp.name) / "documents.sqlite"
        cls.result = build(ROOT, cls.db_path)
        cls.conn = sqlite3.connect(cls.db_path)
        cls.conn.row_factory = sqlite3.Row

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        cls.tmp.cleanup()

    def test_index_integrity(self):
        self.assertEqual(self.result["integrity_check"], "ok")
        self.assertEqual(self.result["foreign_key_check"], 0)
        self.assertEqual(self.result["containers"], 193)
        self.assertEqual(self.conn.execute("SELECT COUNT(*) FROM source_containers").fetchone()[0], 193)
        self.assertIsNone(self.conn.execute("SELECT corpus_id FROM source_containers WHERE corpus_id = 'BCS-000059'").fetchone())
        self.assertIsNone(self.conn.execute("SELECT corpus_id FROM source_containers WHERE corpus_id = 'BCS-000068'").fetchone())

    def test_staaten_comments_are_searchable(self):
        rows = self.conn.execute(
            "SELECT author_display_name, created_at, native_comment_id, content FROM comments WHERE corpus_id = 'BCS-000187' ORDER BY created_at"
        ).fetchall()
        self.assertEqual(len(rows), 7)
        authors = {row["author_display_name"] for row in rows}
        self.assertEqual(authors, {"Brendon Faulkner", "Jack Hagey"})
        self.assertTrue(all(row["native_comment_id"] is None for row in rows))
        self.assertTrue(all(row["created_at"] for row in rows))
        hits = self.conn.execute(
            "SELECT corpus_id FROM comments_fts WHERE comments_fts MATCH 'Liberty'"
        ).fetchall()
        self.assertEqual({row["corpus_id"] for row in hits}, {"BCS-000187"})
        ferry = self.conn.execute(
            "SELECT content FROM comments_fts WHERE corpus_id = 'BCS-000187' AND comments_fts MATCH 'ferry'"
        ).fetchall()
        self.assertTrue(any("ferry town" in row["content"] for row in ferry))

    def test_existing_comment_and_revision_sidecars_are_indexed(self):
        hi = self.conn.execute(
            "SELECT author_display_name, native_comment_id FROM comments WHERE corpus_id = 'BCS-000003' AND content = 'hi lol'"
        ).fetchone()
        self.assertIsNotNone(hi)
        self.assertEqual(hi["author_display_name"], "Gracen Livingston")
        self.assertEqual(hi["native_comment_id"], "AAAAM4tYECw")
        missing = self.conn.execute(
            """
            SELECT body_capture_status, body_text FROM document_versions
            WHERE corpus_id = 'BCS-000079' AND provider_revision_id = '1'
            """
        ).fetchone()
        self.assertEqual(missing["body_capture_status"], "NOT_FETCHED")
        self.assertIsNone(missing["body_text"])
        warning = self.conn.execute(
            """
            SELECT message FROM ingest_warnings
            WHERE corpus_id = 'BCS-000079' AND code = 'REVISION_BODY_NOT_IN_REPO'
            """
        ).fetchone()
        self.assertIsNotNone(warning)
        preserved = self.conn.execute(
            """
            SELECT body_path FROM document_versions
            WHERE corpus_id = 'BCS-000003' AND body_capture_status = 'REVISION_BODY_PRESERVED'
            LIMIT 1
            """
        ).fetchone()
        self.assertIsNotNone(preserved)
        self.assertTrue(preserved["body_path"].startswith("sources/empire-city/BCS-000003/revisions/"))

    def test_modification_times_survive_rebuild(self):
        expected = {
            "BCS-000173": "2021-08-18T18:37:07.755Z",
            "BCS-000180": "2021-09-30T18:37:54.295Z",
            "BCS-000148": "2020-09-14T19:50:32.679Z",
        }
        for corpus_id, modified in expected.items():
            container = self.conn.execute(
                "SELECT modified_at FROM source_containers WHERE corpus_id = ?",
                (corpus_id,),
            ).fetchone()
            current = self.conn.execute(
                """
                SELECT modified_at FROM document_versions
                WHERE corpus_id = ? AND provider_revision_id = 'normalized-current'
                """,
                (corpus_id,),
            ).fetchone()
            self.assertEqual(container["modified_at"], modified)
            self.assertEqual(current["modified_at"], modified)
            self.assertEqual(metadata(corpus_id)["native_dates"]["modified"], modified)

    def test_authorship_is_not_inferred_from_ownership(self):
        attested = ["BCS-000180", "BCS-000185", "BCS-000187", "BCS-000188", "BCS-000190"]
        for corpus_id in attested:
            meta = metadata(corpus_id)
            authorship = meta["authorship"]
            self.assertEqual(authorship["status"], "BRENDON")
            self.assertEqual(authorship["attribution"]["basis_kind"], "owner_attestation")
            self.assertIn("not an inference", authorship["basis"])
            self.assertNotEqual(authorship["basis"], authorship.get("project_ownership_context"))
            self.assertTrue(authorship["project_ownership_context"])
            indexed = self.conn.execute(
                """
                SELECT authorship_status, attribution_basis_kind, archival_provenance_status
                FROM source_containers WHERE corpus_id = ?
                """,
                (corpus_id,),
            ).fetchone()
            self.assertEqual(indexed["authorship_status"], "BRENDON")
            self.assertEqual(indexed["attribution_basis_kind"], "owner_attestation")
            self.assertNotEqual(indexed["authorship_status"], indexed["archival_provenance_status"])
            self.assertEqual(catalog_row(corpus_id)["authorship"], "BRENDON")
            self.assertEqual(catalog_row(corpus_id)["copyright_owner"], "Brendon Faulkner")
        for corpus_id in ("BCS-000182", "BCS-000183"):
            authorship = metadata(corpus_id)["authorship"]
            self.assertEqual(authorship["status"], "BRENDON")
            self.assertNotIn("attribution", authorship)
            indexed = self.conn.execute(
                "SELECT authorship_status, attribution_basis_kind FROM source_containers WHERE corpus_id = ?",
                (corpus_id,),
            ).fetchone()
            self.assertEqual(indexed["authorship_status"], "BRENDON")
            self.assertIsNone(indexed["attribution_basis_kind"])

    def test_pigeon_lord_comparison_replaces_the_unread_claim(self):
        meta = metadata("BCS-000148")
        bases = [
            item["basis"]
            for item in meta["historical_context"]["not_established"]
            if item.get("question") == "superseded_by_v2"
        ]
        self.assertEqual(len(bases), 1)
        self.assertNotIn("was not read", bases[0])
        self.assertIn("compared", bases[0])
        self.assertIn("not proven", bases[0])
        link = next(item for item in meta["source_links"] if item["to_corpus_id"] == "BCS-000175")
        self.assertNotIn("SUPERSEDES", link["link_type"])
        self.assertNotIn("unread", catalog_row("BCS-000148")["context_policy"])
        self.assertIn("compared", catalog_row("BCS-000148")["context_policy"])

    def test_admission_timestamp_is_the_commit_not_the_placeholder(self):
        for corpus_id in [f"BCS-{number:06d}" for number in range(173, 196)]:
            meta = metadata(corpus_id)
            self.assertEqual(meta["ingested_at"], ADMISSION)
            self.assertNotEqual(meta["ingested_at"], PLACEHOLDER)
            self.assertIn("repository_admission", meta["ingested_at_meaning"])
            self.assertIn("Not a Drive capture time", meta["ingested_at_meaning"])

    def test_normalized_bodies_keep_structure(self):
        season = source_text("BCS-000183")
        self.assertIn("\nThe way to Legend.\n", season)
        self.assertNotIn("Season 5.The way to Legend.", season)
        bodfish = source_text("BCS-000177")
        self.assertIn("\n1. The ole' silver mine.\n", bodfish)
        self.assertNotIn("Bodfish Boom Town1.", bodfish)
        self.assertIn("![](assets/image1.jpg)", bodfish)
        arcania = source_text("BCS-000180")
        self.assertIn("\nA New 5e Setting\n", arcania)
        self.assertIn("Originally conceived by Brendon Faulkner", arcania)
        staaten = source_text("BCS-000187")
        self.assertIn("| NPC Name | Role | Primary Location |", staaten)
        self.assertIn("| Benny Culper | Leader of Smugglers | Crescent Cove |", staaten)
        self.assertIn("July 11", staaten)
        self.assertIn("Intro week", staaten)
        pigeon = source_text("BCS-000175")
        self.assertIn("| Level | Bread. | Spells Known |", pigeon)
        self.assertIn("\nPigeon Lord.\n", pigeon)

    def test_markdown_export_image_references_still_resolve(self):
        ferrytown = source_text("BCS-000173")
        hampstead = source_text("BCS-000174")
        for number in range(1, 11):
            self.assertIn(f"[image{number}]: assets/image{number}.png", ferrytown)
            path = ROOT / "sources" / "empire-city" / "BCS-000173" / "assets" / f"image{number}.png"
            self.assertTrue(path.is_file(), path)
        for number in range(1, 21):
            self.assertIn(f"[image{number}]: assets/image{number}.png", hampstead)
            path = ROOT / "sources" / "empire-city" / "BCS-000174" / "assets" / f"image{number}.png"
            self.assertTrue(path.is_file(), path)


if __name__ == "__main__":
    unittest.main()
