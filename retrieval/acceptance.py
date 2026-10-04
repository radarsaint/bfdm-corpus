"""Real S3 regression checks using only the generated model-facing representation."""
import argparse
import json
from pathlib import Path

from retrieval import discord_search as ds


def run(export_dir, index):
    def query(text="", **kw):
        return ds.search(export_dir, index, query=text, campaign="Roanoke Season 3", **kw)

    long_name, short_name = query("Sandigil", limit=100), query("Gil", limit=100)
    assert long_name["total"] > 0
    assert long_name["total"] == short_name["total"]
    assert [m["id"] for m in long_name["hits"]] == [m["id"] for m in short_name["hits"]]
    assert not long_name["ambiguous"]
    assert {m["id"] for m in long_name["alias_evidence"]} == {"735158331332624514", "739533579134042193"}
    # Description/background exists in the first page without a bespoke summary.
    assert "734131693971308636" in {m["id"] for m in long_name["hits"]}
    phrase = query("of the Twin Vents", exact=True)
    assert phrase["total"] > 0
    filtered = query("Gil", channel="the-red-road-reform-club", author="237577351532249110")
    assert filtered["total"] > 0
    assert all(m["author_id"] == "237577351532249110" and m["channel"]["name"] == "the-red-road-reform-club" for m in filtered["hits"])
    attached = query("Gil", has_attachment=True)
    assert attached["total"] > 0
    m = attached["hits"][0]
    a = m["attachments"][0]
    assert a["local_path"].startswith("discord/roanoke-season-3/attachments/")
    assert a["sha256"]
    fetched = query(message_id=m["id"], context=2)["hits"][0]
    assert fetched["provenance"]["message_id"] == m["id"]
    assert fetched["provenance"]["database_path"] == "discord/roanoke-season-3/roanoke-season-3.sqlite"
    assert fetched["context"]["before"] and fetched["context"]["after"]
    assert query(attachment_id=a["id"])["hits"][0]["id"] == m["id"]
    assert query(a["filename"], has_attachment=True)["total"] > 0
    assert query("sandigi", prefix=True)["total"] > 0

    # GitHub-only consumer simulation: follow ordinary-text routes, never open a
    # canonical SQLite. Each matching shard includes full source metadata.
    nav = ds.lookup(export_dir, "Roanoke Season 3", "Sandigil")
    assert {r["term"] for r in nav["matches"]} >= {"sandigil", "sandigill", "gil", "gill"}
    navigated = set()
    for match in nav["matches"]:
        for location in match["shards"]:
            path = export_dir / match["server_slug"] / location["path"]
            rows = ds.read_jsonl(path)
            assert rows[0]["server"]["id"] == "636012145204527125"
            navigated.update(row["id"] for row in rows[1:])
    assert m["id"] in navigated
    for e in nav["entities"]:
        for ref in e["support"]:
            rows = ds.read_jsonl(export_dir / e["server_slug"] / ref["shard"])
            assert ref["message_id"] in {row["id"] for row in rows[1:]}
    return {"passed": True, "sandigil_hits": long_name["total"], "gil_hits": short_name["total"],
            "alias_support_messages": sorted(m["id"] for m in long_name["alias_evidence"]),
            "exact_phrase_hits": phrase["total"], "channel_author_hits": filtered["total"],
            "attachment_message_id": m["id"], "attachment_id": a["id"],
            "connector_navigation": "PASS (ordinary text files only)",
            "canonical_sqlite_required_by_consumer": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export-dir", type=Path, default=ds.DEFAULT_EXPORT)
    parser.add_argument("--index", type=Path, default=ds.DEFAULT_INDEX)
    args = parser.parse_args()
    print(json.dumps(run(args.export_dir, args.index), sort_keys=True))
