# Model-facing corpus retrieval

The canonical corpus is allowed to use storage formats that are excellent locally but opaque to GitHub-connected models. Model access is provided by **derived, rebuildable projections**, never by replacing the canonical source.

## Discord

Canonical source: `discord/<server>/<server>.sqlite` (Git LFS).

Model projection: `model-index/discord/<server>/messages-NNNN.jsonl` plus `manifest.json`. Each message retains immutable Discord IDs, timestamps, channel/thread identity, author identity, reply target, and content. The projection is deliberately non-LFS plain text.

Regenerate one archive:

```bash
git lfs pull
python scripts/export_discord_model_index.py discord/roanoke-season-3/roanoke-season-3.sqlite
```

Search projections locally:

```bash
python scripts/search_corpus.py "Sandigil" --server roanoke-season-3 --context 3
```

Every search result includes a `coverage_report`. A zero-match result is only strong evidence of absence when coverage is `EXHAUSTIVE`; missing mirrors lower zero-match confidence instead of being silently treated as "not found."

## Automation

`.github/workflows/refresh-model-index.yml` hydrates Git LFS, rebuilds Discord projections, and commits changed projection files. It runs when canonical Discord SQLite files change and can also be dispatched manually.

## Authority and provenance

The SQLite harvest remains source truth. JSONL is a retrieval projection. Stable message IDs make a retrieved projection row traceable back to the canonical database. Do not edit projection rows by hand.


## GitHub-connected model protocol

A model that cannot execute the SQLite database should use this order:

1. Read `bfdm_inventory.jsonl` and identify the intended source families and their `model_cloud` status.
2. Search the repository for the requested names, aliases, phrases, or distinctive terms. Prefer hits under `model-index/discord/` over derived research when the task asks for primary Discord evidence.
3. Fetch the matching `messages-NNNN.jsonl` shard. Each row is one complete Discord message with stable message/channel/author IDs and timestamp.
4. Expand context using nearby rows in the same shard. If the hit is at a shard boundary, fetch the immediately preceding/following shard.
5. Treat research files as leads unless the task explicitly asks for derived research. Primary-message evidence outranks a research paraphrase.
6. Report coverage. If an intended source family is `OPAQUE`, has no manifest, or is otherwise unavailable, do not turn a zero result into a claim of absence.

### Zero-result rule

GitHub code search is a discovery surface, not proof of exhaustive absence. A GitHub-only model may report that it found no indexed match, but should use `zero_match_confidence: LOW` unless it has exhaustively checked the relevant projection. Environments with shell access should use `scripts/search_corpus.py`, which scans the complete generated projection and emits the required `coverage_report`.

### Projection health check

For Discord, a usable projection requires all of the following:

- a `manifest.json`;
- manifest `message_count` matching the canonical Discord registry;
- one or more non-LFS `messages-NNNN.jsonl` files;
- shard files small enough for GitHub/model retrieval;
- an inventory row pointing at the generated mirror.

A model should distinguish “source missing,” “mirror missing,” “search returned no indexed match,” and “exhaustive projection search returned zero.” Those are different claims.
