# Saturday D&D ChatGPT Project History — Ingest Batch 2

**Local date:** 2026-10-04  
**Repository date / UTC:** 2026-10-05  
**Project:** Saturday D&D  
**Branch:** `ingest/chatgpt-project-saturday-dnd-history`  
**Base branch:** `main`  
**Base SHA inspected before branch creation:** `7e6b2dccf73efe70a01caf69ecd4a6e39e4c3f53`  
**Recovery status:** `PROJECT_HISTORY_RECOVERY_PARTIAL`

## Announced scope

Batch 2 covers five early Saturday D&D Project-history clusters:

- 2026-04-07 — early Neverwinter / Evernight setting discussion;
- 2026-05-14 — House of Measured Coin / Tasha-in-the-jar campaign development;
- 2026-05-24 — Tasha head-in-jar voice development;
- 2026-05-29 — Circle of Stars druid rooted in Neverwinter after Greengrass;
- 2026-05-30 — Water Peculiar / Lower Cistern encounter development.

## New source containers

- `BCS-000132` — April 7 Neverwinter / Evernight partial recovery
- `BCS-000133` — May 14 House of Measured Coin / Tasha partial recovery note
- `BCS-000134` — May 24 Tasha voice partial recovery
- `BCS-000135` — May 29 Circle of Stars / Greengrass partial recovery
- `BCS-000136` — May 30 Water Peculiar / Lower Cistern partial recovery

Each source separates exact recovered wording from search-recovered context that is not a verbatim transcript.

## Evidence-state handling

The sources are preserved as `CONTEMPORANEOUS_DM_WORKBENCH`.

No generated assistant material is treated as user-authored. AI proposals remain `PROPOSED / DELIVERY_UNKNOWN` unless later source evidence establishes selection or use.

The Water Peculiar source preserves exact user correction/refinement text: the user first requested a Neverwinter Water Peculiar and then explicitly removed its ability to talk, redirecting the encounter toward rigid rules the party must negotiate. This sequence is preserved as source history only; no Phase 2 inference or BCE was minted.

## Batch counts

- new BCS containers: 5
- BCS range: `BCS-000132`–`BCS-000136`
- total catalog rows after batch: 136
- project-history manifest conversation clusters: 11
- conversation clusters moved from QUEUED to PARTIAL in this batch: 5
- binary assets copied: 0
- comments captured: 0
- revision metadata rows captured: 0
- revision bodies captured: 0
- BCE records minted: 0

## Source hashes

- `BCS-000132/source.md` — `c5a7b5655ad04c4d4cef5b73431ae8a7a8bb6020803130ad15d0d9c20728a42d`
- `BCS-000133/source.md` — `ae167f7ab140469483a2a2d3d9b7ede036c0ef73806676bbac9ed58b28ee85d4`
- `BCS-000134/source.md` — `44447fe757a09a2e5b54f21c708cddcfc3334c32e95eebef46ab1ce365e7dad6`
- `BCS-000135/source.md` — `7224dff1b46a33f3a5ca25d8c8badfa9be72c1f2ff28f32794f5546f85705135`
- `BCS-000136/source.md` — `667f2b0b91fcaf42480e5a6eb382ccdf080ce46c6a538b6b85a5b8cfa853d706`

## Known limitations

- exact native conversation titles remain unavailable;
- stable native ChatGPT message IDs remain unavailable;
- several clusters expose only one exact sentence or no exact transcript body;
- BCS-000133 intentionally contains no fabricated transcript text because the May 14 body could not be re-verified verbatim;
- BCS-000135 preserves a previously exposed exact sentence even though the current re-query did not return that conversation again;
- table delivery / implementation is not established by these sources;
- generated/uploaded Project art remains inventoried but is not duplicated in this batch;
- `indexes/documents.sqlite` has not been rebuilt in this connector-only environment.

## Validation boundary

Connector-level validation can check JSON/JSONL parsing, BCS uniqueness, branch comparison, and file presence.

Repository-local shell checks are not available in this chat, so this batch does not claim completion of:

- `python ingest/validate_ingest.py`;
- `python registry/validate_registry.py`;
- document-index rebuild / SQLite integrity / FTS checks.

No BCE, personality, training, precedent-card, or Phase 2 judgments were minted.
