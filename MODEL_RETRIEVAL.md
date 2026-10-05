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

`.github/workflows/refresh-model-index.yml` hydrates the canonical Discord SQLite files, rebuilds message and attachment projections for every harvest, verifies source parity, and commits changed projection files. It runs when canonical Discord SQLite files or the exporters change and can also be dispatched manually. The superseded `model/discord` workflow has been retired so only one projection is maintained.

`.github/workflows/discord-retrieval.yml` checks the consumer with LFS hydration disabled, then checks every projected source field against hydrated SQLite. Maintainers can reproduce the full parity and byte-determinism checks with:

```bash
python -m unittest scripts.test_discord_retrieval -v
python scripts/verify_discord_retrieval.py --rebuild
```

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

Brendon explicitly authorized publishing the Discord text index and provenance to this currently public repository on 2026-10-04 for multi-model work. The projections use that repository's access boundary. Canonical SQLite and attachment bytes remain authoritative. No separate corpus, hosted service, or publication destination is introduced. Alias support records cite native source messages; alias ids are retrieval ids, not BCS or BCE source ids.

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

Manifest version 4 records the canonical SQLite SHA-256 and hashes every message shard and term bucket. Attachment manifests record the same source hash. The consumer compares these with hydrated SQLite or the LFS pointer OID. Missing, changed, stale, or unverified components produce `PARTIAL` coverage; an unavailable projection produces `INACCESSIBLE`. A missing attachment catalog therefore cannot silently turn into an exhaustive empty attachment result.

Channel and author filters accept native IDs as well as names. Multiword queries without a known alias use literal phrase matching. Queries whose tokens are too short for the routing index scan the message projection through the CLI.

## Current limits and integration status

The canonical model-facing path is `model-index/discord/` and `scripts/search_corpus.py`. The earlier `ingest/discord-retrieval-v1` experiment under `indexes/discord/` is superseded and must not be merged as a second projection. Its historical 1,268-candidate result included `Gill`; the current curated alias set excludes that ambiguous token and returns 1,153 candidates for both `Sandigil` and `Gil` in S3.

- Alias coverage currently begins with the S3 regression entity. Other names use lexical retrieval; there is no automatic entity discovery, coreference, semantic search, or typo correction.
- GitHub-only consumers follow the term routing and source shards. Code search freshness is not guaranteed, and a few shards are evidence, not an exhaustive search.
- Attachment filenames, stored paths, IDs, and hashes are available for all three harvests. Binary images/audio remain in LFS; their contents are not OCR'd or transcribed. An attached mention does not establish that the image is a character portrait.
- Search output is capped by `--limit` and text by `--full`. Context requires opening the named shard and adjacent shards or resolving `reply_to_id`; no dedicated conversation-context endpoint exists.
- The CLI and GitHub file protocol are available to model consumers. Automatic integration into the separate Kit runtime and a hosted search/MCP endpoint remain future work.
- The index cannot recover unharvested/deleted messages or voice sessions. All findings remain bounded by the harvest windows.


## Deterministic term routing

GitHub connector code search is not treated as a required dependency. Every Discord projection also contains a deterministic term-to-shard index under:

`model-index/discord/<server>/terms/<prefix>.jsonl`

Normalize a lookup term by case-folding it, converting curly apostrophes to ASCII apostrophes, and taking the first three characters. Replace any character outside `[a-z0-9]` with `_`; pad short terms with `_`. Tokens shorter than three characters are not indexed.

Examples:

- `Sandigil` -> `sandigil` -> `san` -> `terms/san.jsonl`
- `Gil` -> `gil` -> `gil` -> `terms/gil.jsonl`

Each term row contains the normalized token, the number of messages containing it, and the exact message shard filenames where it occurs. Fetch only those shards, then inspect the complete message rows and adjacent context.

This routing index gives a GitHub-connected model a direct retrieval path even when repository code search is unavailable, stale, or returns no results.
