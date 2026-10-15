# Discord retrieval completion

First completion commit inspected `main` at `962d8cd236b364de09e602b1a23829370518cb0d` on 2026-10-05.
This revalidation, 2026-10-15, merges current `main` `6795362e967e89230086afc28c04450cc7d0cce4` and repairs the review defect on that completion.
Branch: `ingest/discord-retrieval-completion`. This branch is not canonical `main`.

## Reconciliation and root cause

Canonical Discord databases use Git LFS. GitHub-connected models receive pointers, not a queryable SQLite archive. Internal SQLite FTS did not solve model access.

The original `ingest/discord-retrieval-v1` branch was published, but never merged. While that work was paused, `main` gained `model-index/discord/`, deterministic term routing, and PR #23's search consumer. This completion extends that path instead of merging the old branch's duplicate `indexes/discord/` projection. Historical validation on that old branch is not current-main evidence.

Current `main` was 90 commits ahead of the 2026-10-05 PR head and had not changed the Discord SQLite OIDs or the model-index scripts. The merge conflict was only `README.md`. Main's archive, registry, and coordination updates are kept. Visibility stays outside corpus authority; the 2026-10-04 public retrieval authorization stays recorded.

## Architecture and completed changes

Canonical SQLite → deterministic non-LFS message shards and term buckets → campaign-scoped aliases and attachment metadata → GitHub file reads or `scripts/search_corpus.py`. SQLite remains authoritative; no source IDs change.

- Attachment metadata covers all three harvests.
- The refresh workflow rebuilds attachments as well as messages. The superseded workflow that wrote `model/discord/` was already removed. `export_discord_model_view.py` and `mark_discord_projection.py` had no remaining callers; inventory updates go through `sync_inventory_from_model_index.py`. Those two scripts are now removed.
- Manifest version 4 records the source SQLite SHA-256 and hashes every message shard and term bucket. Attachment manifests record the same source hash. Search compares these with hydrated bytes or the LFS OID before claiming exhaustive coverage.
- Missing, stale, checksum-mismatched, or unreadable index material returns `PARTIAL`. A missing manifest returns `INACCESSIBLE`. Neither is an exhaustive empty result.
- A manifest that exists but is not a JSON object no longer raises `JSONDecodeError` out of `search()`. The CLI scans readable message shards and reports `PARTIAL`. Corrupt term, message, attachment, or alias JSONL is the same kind of failure: partial coverage, not a crash and not absence.
- Message shards are LF-delimited. `json.dumps(..., ensure_ascii=False)` leaves U+2028 and U+2029 inside records. Splitting those shards with a universal line splitter is a false corruption. The consumer splits on LF only.
- Native author and channel IDs work as filters. Names with punctuation work as the same filters. Short queries scan the message projection. Non-alias multiword queries use literal phrase matching. A bare message id is not an id lookup; it is searched as text.
- S3 aliases cite native support-message IDs and shard paths. `Gil` does not include `Gilbert`, `Gill`, or `Gilligan`.
- `scripts/verify_discord_retrieval.py` compares every projected field with SQLite, checks attachment bytes or LFS OIDs, and can rebuild twice.

## Review finding

Codex review on `f503bd853f7d6781268453a0a653950bc38f62a0`, thread `PRRT_kwDOU36SRc6o4iFV`: `projection_issues()` classified a malformed `manifest.json`, then `_shards_for_tokens()` parsed it again and raised before `search()` could return `PARTIAL`.

Resolved in this branch. `scripts/test_discord_retrieval.py` covers a truncated manifest, a non-object manifest, corrupt message/attachment/term JSONL, a corrupt alias file, and a message containing U+2028. Those cases do not claim exhaustive absence.

## Executed validation — 2026-10-15

Python 3.11.

`python3.11 -m unittest scripts.test_discord_retrieval -v`: **18 passed, 0 skipped** after the three canonical databases were hydrated. The same module had **17 passed, 1 skipped** while those databases were still LFS pointers; the skipped test is the hydrated S3 identity comparison. The real S3 projection test passed in that pointer checkout.

`python3.11 scripts/validate_model_index.py` and `python3.11 scripts/audit_inventory.py`: passed. 0 inventory errors.

`python3.11 scripts/verify_discord_retrieval.py --rebuild`: passed. Two rebuilds produced **13,902 byte-identical files**. Canonical archive checksums did not change. Every projected message field and attachment metadata field matched SQLite. Attachment files were checked as LFS pointers against the recorded OID, not by hydrating image bytes.

| Harvest | Messages | Attachments | Source SHA-256 |
|---|---:|---:|---|
| Roanoke Season 3 | 197,013 | 1,421 | `16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d` |
| Empire City | 189,761 | 3,528 | `a0c71f99ff403e5a91d88c2dfb647326cbc332b4b943fa207cb080173a83f98e` |
| Empire City Dev | 12,692 | 639 | `a339a26de8e01d63e608c9d5cdedc494d40fbde76c7d8fa19b482a6f8584aaab` |
| Total | 399,466 | 5,588 | |

These counts were recomputed from the hydrated databases. They were not copied in as expected truth. Machine-readable verifier output: [2026-10-05-validation.json](2026-10-05-validation.json).

## Retrieval sample

Expected ids came from scanning canonical SQLite message text with the documented word-boundary or folded-phrase rule. That scan did not use FTS and did not use the term index. `scripts/search_corpus.py` was then run with `--source projection` and `--source sqlite`. No mismatches.

| Query | Server | Kind | Expected / both consumers |
|---|---|---|---:|
| Sandigil | S3 | alias | 1,153 |
| Gil | S3 | alias, same expansion, excludes Gilbert/Gill/Gilligan | 1,153 |
| Gilbert | S3 | word, not the alias | 1 |
| Gill | S3 | word, not the alias | 120 |
| Gilligan | S3 | word, not the alias | 2 |
| Croatoan | S3 | word | 84 |
| Eloise | S3 | word in message text | 0 exhaustive |
| of the Twin Vents | S3 | phrase | 6 |
| Gil's | S3 | apostrophe token | 15 |
| map --author 360967589511561218 | S3 | native author id (Noah) | 11 |
| Sandigil --channel 738994547635519488 | S3 | native channel id `town-square` (5,334 messages in channel) | 79 |
| Croatoan --channel château-de-léclipse | S3 | punctuation/accent channel name, same as id `739546506184491089` | 3 |
| Sandigil --attachments | S3 | attachment-bearing alias hit | 1 |
| New Jersey | Empire City | multiword phrase | 12 |
| hobos | Empire City | word | 3 |
| Cruithne --author 150319814836092928 | Empire City | native author id | 3 |
| noodles | Empire City | word | 67 |
| Boroughs | Empire City Dev | word | 15 |
| homebrew races | Empire City Dev | multiword phrase | 6 |
| my | Empire City Dev | short token, full shard scan | 608 |
| zzzzneverpresentxyz | S3 and Dev | absent | 0 exhaustive |

The one attachment hit is message `737113252726702111`, shard `messages-0103.jsonl`, author `594008151779573762`, channel `636012145204527127`, attachment `737113252395352184`, filename `unknown.png`, sha256 `52d925c1081d4edc2ee008228018e5111f2765efdcf641ea3c336ca14a60f4b7`. That shows the file was attached. It does not show that the image is a portrait.

No-LFS path: the same Sandigil projection search with `--database` pointed at an LFS pointer for the S3 OID returned 1,153, `access=jsonl_projection`, `canonical_database_state=lfs_pointer`, `EXHAUSTIVE`, and the same id set.

Direct LF-split reads of these shards matched SQLite id, channel, author, and timestamp:

| Message | Shard |
|---|---|
| `739533579134042193` | `model-index/discord/roanoke-season-3/messages-0178.jsonl` |
| `734131693971308636` | `model-index/discord/roanoke-season-3/messages-0002.jsonl` |
| `737113252726702111` | `model-index/discord/roanoke-season-3/messages-0103.jsonl` |

## Search-scope limits found by the sample

- `Eloise` has 13,064 S3 messages whose username or display name contains that string, and **zero** message bodies containing the word. An exhaustive content zero is not absence of the person. Use `--author`.
- Channel `636012707123822623` (`3⃣ Week Three, Stillwater`) has the name and **zero** harvested messages. An exhaustive zero there is an empty channel.
- Searching the native message id `739533579134042193` as query text is an exhaustive content zero. The id is recovered from the shard path above, not by using the id as a search term.
- `cranium` filtered to Dev author `237577351532249110` (`hekiryuu`) is an exhaustive zero. The word exists in that harvest under other authors.

## Consumer check

Observed here: `scripts/search_corpus.py` on hydrated SQLite and on an LFS pointer, plus direct reads of the projection files in this checkout.

Not observed: a separate GitHub-connected GPT following `MODEL_RETRIEVAL.md` against this branch after it is pushed. That acceptance check stays pending. The queries and source ids above are the check. Kit runtime integration was not modified and was not exercised.

## Remaining limitations

- Alias curation is one S3 entity. Other names are lexical. There is no entity discovery, coreference, semantic search, or typo correction.
- An alias hit is a candidate, not character attribution.
- GitHub-only consumers must follow the file protocol, including the LF split. Code search is not exhaustive. A few fetched shards are not exhaustive evidence.
- Attachment binaries still require LFS-capable access. There is no OCR or audio transcription.
- Context is adjacent shard rows and `reply_to_id`. There is no context endpoint and no cursor pagination.
- The separate Kit runtime is not wired to this CLI. No hosted MCP service is deployed.
- Unmerged work is not canonical.
