# Discord retrieval validation — 2026-10-04

Base: `main` at `d69a773215d7806b920514052f02a346aae67333`.
Implementation branch: `ingest/discord-retrieval-v1`.
Machine-readable results: [validation.json](validation.json).

## Root cause and architecture

The canonical SQLite archives had internal FTS indexes, but GitHub-connected
consumers received LFS pointers. A binary archive being searchable locally did
not make its messages searchable through GitHub file tools. No shared Discord
exporter, consumer CLI, or model-readable navigation layer existed on current
main. There were no open PRs at the initial inspection. Active ingestion and
cognitive-architecture branches were checked; they did not supply this layer.

Implemented a deterministic canonical-SQLite → ordinary-Git JSONL/message and
token index → scoped alias resolution → consumer path. GitHub-only consumers
follow term routers and fetch source-bearing shards; Python consumers build a
local FTS5 cache from the same text. Both work without opening the LFS archives.
Canonical sources remain authoritative and byte-unchanged.

## Executed checks

| Check | Result |
|---|---|
| Regression suite | 13 tests passed |
| S3 `Sandigil` + campaign | 1,268 candidate messages |
| S3 `Gil` + campaign | Same 1,268 candidates |
| Alias evidence | Native messages `735158331332624514`, `739533579134042193` |
| Background/description evidence | Native contract message `734131693971308636` appears in first result page |
| Exact phrase `of the Twin Vents` | 6 matches |
| Channel + author filter | 2 matches in the Red Road Reform Club by the specified account |
| Attachment lookup | Message `737113252726702111`, attachment `737113252395352184` |
| Full source field parity | All 399,466 messages, authors, threads, and attachment records checked |
| Attachment storage references | All 5,588 path checksums match stored LFS OIDs/bytes |
| Rebuild determinism | Two complete exports: all 13,057 files byte-identical |
| Canonical archive checksums | Unchanged before/after export |
| Model navigation | Term routers → source shards → alias support/attachment references passed |
| No-LFS consumer | Fixture archives removed before building/searching the text-only index; passed |
| Registry validator | Passed; no new BCS/BCE/BCR IDs |
| Git configuration | Generated text has LFS filtering disabled; canonical SQLite retains LFS |

Implementation commit: `a8d0dab91f7dae5fcc071e75dabd1136037b795c`.
The initial push was blocked by automatic approval review. On 2026-10-04,
Brendon explicitly authorized publishing the generated Discord message text
and provenance to the currently public `radarsaint/bfdm-corpus` repository.
Publication is proceeding under that authorization. The checks above are local;
remote connector retrieval and CI results are recorded below when completed.

The S3 attachment hit is an archived mention with an attachment. This check
establishes retrievability and provenance, not the interpretation of the image
as a portrait. Neighboring context remains separately labeled. An author account
is not treated as one character across all its posts.

Fixture tests also cover exact versus nonadjacent phrases, case/diacritics,
prefixes, query punctuation, two entities sharing one name within a campaign,
the same alias across campaigns, duplicate author display names, attachment-only
messages, reply lookup, thread boundaries, pagination, LFS pointers, stale
exports/caches, corrupt generated files, and over-budget records.

## Coverage and storage

| Harvest | Messages | Attachment references |
|---|---:|---:|
| Roanoke Season 3 | 197,013 | 1,421 |
| Empire City | 189,761 | 3,528 |
| Empire City Dev | 12,692 | 639 |
| Total | 399,466 | 5,588 |

Generated text occupies 319,848,871 bytes before Git compression. JSONL pages are
bounded at 48 KiB; directory routers for very busy channels can be larger. The
local FTS cache is ignored and not committed. No attachment binaries are copied.

## Access and remaining work

Repository visibility was verified public. Brendon explicitly confirmed that
public access is intentional while multiple models work with the material. The
text export uses that owner-authorized repository access; no external service,
second repository, or extra publication destination was introduced. Current
access is recorded in README/governance guidance so old private-source wording
does not block this workflow.

The alias registry initially contains the source-supported S3 regression entity.
Other terms already have complete lexical indexes. Automatic alias discovery,
semantic search, OCR/transcription, and automatic integration with the separate
Kit runtime remain future work. Reactions remain in canonical SQLite. Missing
source material and messages outside each harvest window cannot be recovered
by this index. Full operational details and limits are in [README.md](README.md).

## Changed files

- `retrieval/discord_search.py`: deterministic export, term navigation, local
  FTS cache, search/filters, context/attachment lookup, verification/freshness.
- `retrieval/tests/test_discord_search.py` and `retrieval/acceptance.py`: fixture
  regressions and real S3 end-to-end acceptance checks.
- `indexes/discord/`: generated messages, provenance, token postings, aliases,
  catalogs, and checksum inventories for every current harvest.
- `registry/discord_entities.jsonl`: scoped alias assertions citing native IDs.
- `.github/workflows/discord-retrieval.yml`: regression and freshness checks
  with LFS disabled, followed by real-corpus acceptance.
- README, charter, hygiene, Discord/index/registry guidance, `.gitattributes`,
  and `.gitignore`: navigation, current owner access decision, and cache/export
  storage roles. Canonical source bodies and source IDs were not changed.
