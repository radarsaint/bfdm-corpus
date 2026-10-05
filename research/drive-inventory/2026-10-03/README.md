# Google Drive discovery ledger — 2026-10-03

This ledger records Drive search hits that are not represented by a native Google Drive ID in `evidence/catalog.jsonl` at discovery time. A row is a candidate, not an attribution claim, corpus admission, or new BCS assignment.

## Search coverage

- `Roanoke`: 103 results across 2 page(s).
- `Empire City`: 77 results across 1 page(s).
- `Earthfall`: 2 results across 1 page(s).
- `Bastion Redoubt`: 8 results across 1 page(s).
- `At War's End`: 100 results across 2 page(s).

Unique Drive items seen: 224.
Already cataloged by native Drive ID: 66.
Uncataloged candidates recorded: 158.

## Admission rule

Before a candidate receives a BCS ID, verify source identity, campaign/project relationship, authorship/provenance boundaries, duplication/version-family relationships, and whether the item is first-party source material, collaborator context, third-party reference material, or irrelevant search noise.

Machine-readable candidates: `candidates.jsonl`.

## Admission progress

As of 2026-10-04, 8 of the 158 uncataloged candidates have been admitted and ingested as BCS-000069 through BCS-000076 after project-identity review. Admission remains source-by-source rather than title-only.

One exception is BCS-000076 (Public Lore Document.): its rich DOCX export is approximately 4.5 MB and repeatedly failed the connector's inline binary-transfer path. The corpus preserves the full current body, provider text export, comments, revision metadata, and native Drive identity; rich binary/asset mirroring remains explicitly pending.


## ID remap — 2026-10-05

Donor IDs BCS-000087 through BCS-000093 in this 2026-10-03 ledger collided with canonical Season 5 sources already on main. Those seven admitted containers were renumbered to BCS-000115 through BCS-000121. `candidates.jsonl` now stores the canonical id and keeps the old id as `donor_corpus_id`. The ledger is still a discovery snapshot, not a claim that every `INGESTED` row has a finished historical chain.

## Glance — 2026-10-05

`TRIAGE_2026-10-05.md` is the first handful of openings. `TRIAGE_PASS_2026-10-05.md` is the pass over the rest of the unreviewed rows. Rows that were opened are not admitted. Five files could not be read; the reason is in that pass.


