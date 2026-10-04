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
