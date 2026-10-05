# Discord retrieval completion — 2026-10-05

Base inspected: `main` at `962d8cd236b364de09e602b1a23829370518cb0d`.
Completion branch: `ingest/discord-retrieval-completion`.

## Reconciliation and root cause

Canonical Discord databases use Git LFS. GitHub-connected models receive pointers,
not a queryable SQLite archive. Internal SQLite FTS did not solve model access.

The original `ingest/discord-retrieval-v1` branch was published, but never merged.
While that work was paused, `main` gained `model-index/discord/`, deterministic
term routing, and PR #23's search consumer. The old branch was 132 commits behind
main at inspection. This completion extends the current path instead of merging
its duplicate `indexes/discord/` projection and a second search implementation.
Historical validation remains on that old branch; it is not current-main evidence.

## Architecture and completed changes

Canonical SQLite → deterministic non-LFS message shards and term buckets →
campaign-scoped aliases and attachment metadata → GitHub file reads or
`scripts/search_corpus.py`. SQLite remains authoritative; no source IDs change.

- Attachment metadata now covers all three harvests. Previously only S3 had it.
- The existing refresh workflow now rebuilds attachments as well as messages.
  The superseded workflow that wrote `model/discord/` was removed.
- Manifest version 4 records the source SQLite SHA-256 and term-file checksums.
  Attachment manifests also record the source SHA-256. Search compares these
  with hydrated source bytes or the LFS OID before claiming exhaustive coverage.
- Missing attachment catalogs, missing shards, modified term files, and stale
  source versions are reported as partial coverage, not exhaustive absence.
- Native author/channel IDs work as filters. Short queries fall back to scanning
  the text projection; non-alias multiword queries use literal phrase matching.
- S3 aliases now cite native support-message IDs and readable shard paths.
- A read-only verifier compares every projected field with SQLite, checks stored
  attachment hashes or LFS OIDs, and can repeat the full deterministic rebuild.
- CI checks the no-LFS consumer, then hydrates only the three canonical databases
  and checks full source parity. The publication workflow also runs these gates.

## Executed validation

`python3 -m unittest scripts.test_discord_retrieval -v`: **15 passed, none skipped**.
Checks include scoped aliases, common-name ambiguity, phrase/channel/author filters,
native-ID filters, attachment lookup, provenance, pointer-only access, short and
multiword queries, missing/corrupted/stale index handling, and SQLite/projection
search-result parity. An attempted export from a pointer preserves existing shards.

`python3 scripts/verify_discord_retrieval.py --rebuild`: **passed**. Two rebuilds
produced **13,902 byte-identical files**. All canonical archive checksums remained
unchanged. Every message field and attachment metadata field matched SQLite.
All 5,588 stored attachment references matched their bytes or LFS OIDs.

| Harvest | Messages | Attachments |
|---|---:|---:|
| Roanoke Season 3 | 197,013 | 1,421 |
| Empire City | 189,761 | 3,528 |
| Empire City Dev | 12,692 | 639 |
| Total | 399,466 | 5,588 |

Machine-readable results: [2026-10-05-validation.json](2026-10-05-validation.json).

## Sandigil acceptance: passes

Both `Sandigil` and `Gil` plus `Roanoke Season 3` return **1,153** candidates with
the current curated aliases. Both SQLite and projection return the same message
IDs. The old branch's 1,268 count additionally included `Gill`, which current main
keeps ambiguous. This completion preserves current main's alias policy.

The connected GitHub file API successfully read the term routers and these exact
source rows from the inspected main commit, without reading SQLite:

| Evidence | Native message ID | Source shard |
|---|---|---|
| Self-introduction linking Sandigil, Sandi, Gil | `739533579134042193` | `messages-0178.jsonl` |
| Background contract using Sandigill of the Twin Vents | `734131693971308636` | `messages-0002.jsonl` |
| Mention with stored attachment | `737113252726702111` | `messages-0103.jsonl` |

The attachment join resolves `737113252395352184`, `unknown.png`, its stored path,
channel, timestamp, and SHA-256. This establishes retrievability, not that the image
is a portrait. All shard paths above are under `model-index/discord/roanoke-season-3/`.
The exact phrase `of the Twin Vents` returns six matches.

## Access decision

Repository visibility was verified public. Brendon explicitly authorized public
publication of the generated Discord text and provenance on 2026-10-04. That
authorization remains in effect. This work uses the existing repository boundary;
it creates no external service, second corpus, or additional publishing destination.
Source bodies and attachment binaries are unchanged by this completion.

## Remaining limitations

- Alias curation initially covers one S3 entity; automatic entity discovery,
  coreference, semantic search, and typo correction are not implemented.
- An alias-expanded mention is a candidate, not certain character attribution.
- GitHub-only consumers must follow the documented file protocol. Code-search
  indexing is not guaranteed; a subset of fetched shards is not exhaustive evidence.
- Attachment binaries still require LFS-capable access. There is no image OCR or
  audio transcription, and no reconstruction of missing/deleted/voice material.
- Context comes from adjacent shard rows and reply IDs; there is no dedicated
  context endpoint. The CLI supports larger `--limit` values, not paginated cursors.
- The separate Kit runtime is not automatically wired to this CLI. No hosted MCP
  service is deployed. This is the usable corpus retrieval layer it can consume.

Active Drive-history PRs #24–#26 were inspected for overlap and left to their own
workstream. The old retrieval branch is retained as historical implementation
evidence and explicitly superseded, rather than silently merged or deleted.
