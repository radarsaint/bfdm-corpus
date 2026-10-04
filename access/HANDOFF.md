# Access handoff — 2026-10-04

## What was already true

The checkout is source-rich and split by family.

- Discord harvests for Roanoke S3, Empire City, and Empire City Dev are Git LFS
  SQLite. File tools see pointers, not messages.
- `registry/` and `evidence/` are small structured JSONL registries (projects,
  people, identities, BCS/BCE/BCR).
- Season 5 Google Sites were admitted as `BCS-000087`–`BCS-000112` while this layer was being written (`0d766db`). The access layer uses those ids and the page markdown. It does not mint `access:site:` ids for them.
- S3 decision cases are JSONL. Empire City decision cases are markdown only.
- Most BCS document bodies are catalogued and not present. Legacy staging
  reconciliation has not landed on `main`.

## What this change adds

`python -m access` searches the readable families through one JSON interface,
keeps authority on every hit, slices by registry project, walks cites in both
directions, separates historical dates from Google Sites capture times, and
reports families it did not search.

Coverage now distinguishes exhaustive, partial, inaccessible, and unknown searches. See [COVERAGE_DECISIONS.md](COVERAGE_DECISIONS.md) for what was taken from the proposed inventory contract. `python -m access audit` is the summary command.

Acceptance coverage is `python -m unittest access.tests.test_access -v`.
The real checks are Sandigil (empty result, Discord reported not searched),
DM radar (scoped identities, not a global attribution), cryptid across a
Season 5 site page and `BCE-000014`, Golden Dawn split between `roanoke-s3`
and `roanoke-s5-legends`, `BDC-S3-001` → `BCS-000045` catalog-only plus an
unconfirmed Discord snowflake, the reverse cite, and a JSON export bundle.

## Left alone on purpose

- `ingest/discord-retrieval-v1` — Discord text export and
  `python -m retrieval.discord_search`. Do not build a second message index.
- `ingest/drive-project-v1` through `v3` — BCS body reconciliation, including
  the unmerged Halfwudgie container. This layer finds the Season 5 site page
  and does not mint a BCS id.
- `research/kit-design/kit-cognitive-architecture-survey*` — architecture notes,
  not an access implementation.
- Registry facts, evidence wording, harvest databases, and research conclusions
  were not edited.

## Next usability gaps

1. Merge the Discord text export, then teach `access search` to call
   `retrieval.discord_search` and label those hits `discord_message` without
   copying the exporter.
2. Once Drive bodies land, point `body_status` at `sources/<project>/BCS-*`
   instead of leaving them `catalog_only`.
3. Give Empire City decision cases stable per-case ids the way S3 JSONL already
   has, so provenance is not file-level.
4. Character aliases such as Sandigil belong in the Discord entity registry on
   the retrieval branch. This tool should consume that file, not invent a
   second alias list.
