# Drive donor inventory — material absent from current main

Donor: `ingest/drive-project-v3`
Fresh integration branch: `ingest/drive-integration-v4`

## Newly admitted donor BCS records

Current main lacks the donor's non-conflicting Drive IDs:

- BCS-000069 — Season 3 Directory
- BCS-000070 — Master Timeline
- BCS-000071 — Mod Directory
- BCS-000072 — Season 4 Directory
- BCS-000073 — Airship Qualification Module
- BCS-000074 — Boss Monsters
- BCS-000075 — The Red Coats
- BCS-000076 — Public Lore Document.
- BCS-000077 — Crafting with Class (Dev Doc)
- BCS-000078 — Crafting with Class (Public Doc)
- BCS-000079 — Brendon's copy of crafting.
- BCS-000080 — Crafting, another attempt
- BCS-000081 — Map Key
- BCS-000082 — Cryptid Beastiary
- BCS-000083 — Cryptid Bestiary
- BCS-000084 — Complete Manuscript.
- BCS-000085 — Player backgrounds
- BCS-000086 — S3 Uru/Wudgie Lore.

These IDs were explicitly reserved on current main for the active Drive work and do not require renumbering.

## Colliding donor BCS records

Seven donor IDs collide with canonical Season 5 IDs now on main:

- 087 Timeline disambiguation
- 088 RS3 Public docs copy editing.
- 089 Island games draft
- 090 Golden Dawn quest arc
- 091 The Halfwudgie Verbatim
- 092 The Urucokra Verbatim
- 093 The Jackalope Verbatim

See `BCS_COLLISION_RECONCILIATION.md` for the deterministic 115–121 mapping.

## Discovery ledger

`research/drive-inventory/2026-10-03/candidates.jsonl` on the donor currently contains:

- 23 INGESTED
- 1 INGESTED_PARTIAL
- 134 UNREVIEWED_CANDIDATE

The 134 unreviewed candidates are not to be bulk-classified merely to reduce the number.

## Legacy source bodies

The donor also contains archival source-container material for already-established BCS identities that is absent from canonical source directories on main. This includes legacy Roanoke, Empire City, Earthfall, Bastion/Redoubt, At War's End, and Exploration Impossible material. Current main separately verifies the exact 51-source staging archive and 284-file transfer target.

The donor branch is therefore a source of canonical archival payload, not merely analysis.

## Valuable donor-side data to reconcile

For applicable source containers preserve:

- `source.md` current readable body;
- native Drive ID and URL;
- Google-native export snapshot/original representation;
- comments and replies;
- revision metadata;
- fetched revision bodies where present;
- assets where present;
- authorship status and basis;
- document-family IDs;
- project/source-role metadata;
- discovery-ledger admission basis;
- any internal source links;
- exact donor Git blob identities during transport.

No source container should be replaced by a prose summary.
