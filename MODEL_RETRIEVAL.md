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

Search one campaign. `--server` is required because aliases are campaign-scoped:

```bash
python scripts/search_corpus.py "Gil" --server "Roanoke Season 3"
python scripts/search_corpus.py "Sandigil of the Twin Vents" --server roanoke-s3 --phrase
python scripts/search_corpus.py "Sandigil" --server roanoke-season-3 --channel town-square --author hekiryuu
python scripts/search_corpus.py "Sandigil" --server roanoke-season-3 --attachments
```

`auto` uses a hydrated SQLite file when the bytes are present and otherwise uses the JSONL projection. An LFS pointer is not a searched corpus. `coverage_report.status` is `EXHAUSTIVE`, `PARTIAL`, or `INACCESSIBLE`. `zero_match_means_absence` is true only for `EXHAUSTIVE`. `absence_is_not_evidence` is the inverse. Reason codes are attached only when the search did not cover the family. Alias matches also include `lead_hits`: messages that contain at least two of that entity's names, so a short name does not bury the messages that use the other names. `hits` stays in chronological order.

Attachment metadata, still subordinate to SQLite:

```bash
python scripts/export_discord_attachments.py discord/roanoke-season-3/roanoke-season-3.sqlite
```

That writes `attachments.jsonl` and `attachments-manifest.json`. Rows carry attachment id, message id, filename, content type, size, sha256, repo-relative `local_path`, channel, and timestamp. They omit CDN urls, message text, and file bytes.

## Automation

`.github/workflows/refresh-model-index.yml` hydrates Git LFS, rebuilds Discord projections, and commits changed projection files. It runs when canonical Discord SQLite files change and can also be dispatched manually.

## Authority and provenance

The SQLite harvest remains source truth. JSONL is a retrieval projection. Stable message IDs make a retrieved projection row traceable back to the canonical database. Do not edit projection rows by hand.


## GitHub-connected model protocol

A model that cannot execute the SQLite database should use this order:

1. Read `bfdm_inventory.jsonl` and identify the intended source families and their `model_cloud` status.
2. If the query is one campaign-scoped token, read `model-index/discord/<server>/aliases.jsonl`. An explicit alias expands to that entity's names only. Tokens that merely share a prefix, such as Gilbert beside Gil, stay in `ambiguous_neighbors` and are not the same entity. No alias row means search the token itself; it does not mean the name is absent.
3. Route each normalized term through `terms/<prefix>.jsonl` and fetch only the listed `messages-NNNN.jsonl` shards. Each row is one Discord message with stable message, channel, and author ids, timestamp, and reply target. The search result names the shard to open for adjacent rows.
4. Join attachment metadata from `model-index/discord/<server>/attachments.jsonl` on `message_id`. The canonical file bytes remain at `local_path` inside the harvest. Do not expect a live CDN url.
5. Treat research files as leads unless the task explicitly asks for derived research. Primary-message evidence outranks a research paraphrase.
6. Report coverage. `INACCESSIBLE` with `lfs_pointer_only` means the SQLite pointer was not readable and no projection manifest was searched. That is not a claim that the messages do not exist.

## Public repository constraint

This GitHub repository is public, while the Discord harvests are private source material. Message JSONL projections were already published on `main` before this search layer. Do not add further raw Discord message text to ordinary Git files. Alias rows and attachment metadata are the only new derived Discord records this layer adds, and neither contains message bodies. The SQLite harvest remains the canonical archive. If an alias and the archive disagree, the archive is authoritative. Alias ids are retrieval ids, not BCS or BCE source ids.

### Zero-result rule

GitHub code search is a discovery surface, not proof of exhaustive absence. A GitHub-only model may report that it found no indexed match, but should use `zero_match_confidence: LOW` unless it has exhaustively checked the relevant projection. Environments with shell access should use `scripts/search_corpus.py`, which reads a hydrated SQLite harvest or the term-routed projection and emits `coverage_report`.

### Projection health check

For Discord, a usable projection requires all of the following:

- a `manifest.json`;
- manifest `message_count` matching the canonical Discord registry;
- one or more non-LFS `messages-NNNN.jsonl` files;
- shard files small enough for GitHub/model retrieval;
- an inventory row pointing at the generated mirror.

A model should distinguish “source missing,” “mirror missing,” “search returned no indexed match,” and “exhaustive projection search returned zero.” Those are different claims.


## Deterministic term routing

GitHub connector code search is not treated as a required dependency. Every Discord projection also contains a deterministic term-to-shard index under:

`model-index/discord/<server>/terms/<prefix>.jsonl`

Normalize a lookup term by case-folding it, converting curly apostrophes to ASCII apostrophes, and taking the first three characters. Replace any character outside `[a-z0-9]` with `_`; pad short terms with `_`. Tokens shorter than three characters are not indexed.

Examples:

- `Sandigil` -> `sandigil` -> `san` -> `terms/san.jsonl`
- `Gil` -> `gil` -> `gil` -> `terms/gil.jsonl`

Each term row contains the normalized token, the number of messages containing it, and the exact message shard filenames where it occurs. Fetch only those shards, then inspect the complete message rows and adjacent context.

This routing index gives a GitHub-connected model a direct retrieval path even when repository code search is unavailable, stale, or returns no results.
