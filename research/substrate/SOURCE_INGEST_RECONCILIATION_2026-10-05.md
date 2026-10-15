# Source ingest reconciliation 2026-10-05

This is an integration record, not new BFDM research.

## Input branches

| PR | Branch | Head used |
| --- | --- | --- |
| main | main | `7e6b2dccf73efe70a01caf69ecd4a6e39e4c3f53` |
| #31 | `hardening/substrate-audit-main-2026-10-05` | `27a8e69c1dca142108e28328aba3974eff357e67` |
| #35 | `ingest/research-critical-lineages-2026-10-05` | `36d53fa218dcfa2ee131edfe408dd5f39ff5f44b` |
| #32 | `ingest/chatgpt-project-earthfall-live-history` | `316f8bb57a2c9e6f8c24142f3ea08b66995fd5f6` |
| #34 | `ingest/chatgpt-project-saturday-dnd-history` | `cf54d344ebbedb1fb19f92fff5149ccb30d0ca49` |

PR #33 (`research/human-object-index-v0`, `dc358a00fcea9c3aa8777ea83d4e3cdd9a3606e5`) was inspected and not integrated.

## Final BCS allocation

Highest canonical BCS on refreshed main was BCS-000130. No canonical ID was renumbered.

| Donor | Old provisional id | Final id | Title |
| --- | --- | --- | --- |
| #35 | BCS-000131 | BCS-000131 | S4 Master Timeline. |
| #35 | BCS-000132 | BCS-000132 | S5 style guide |
| #35 | BCS-000133 | BCS-000133 | Season 5 Dungeon Master's guide |
| #35 | BCS-000134 | BCS-000134 | Server guidelines and house rules |
| #35 | BCS-000135 | BCS-000135 | Player race edits. |
| #35 | BCS-000136 | BCS-000136 | The Rowing Oak |
| #35 | BCS-000137 | BCS-000137 | The rowing oak guide. |
| #35 | BCS-000138 | BCS-000138 | The Tatankan Verbatim |
| #35 | BCS-000139 | BCS-000139 | The Chinnokin Verbatim |
| #35 | BCS-000140 | BCS-000140 | Ferrytown Main Event Schedule |
| #35 | BCS-000141 | BCS-000141 | Hampstead Players Guide |
| #35 | BCS-000142 | BCS-000142 | Archavist Daysong Timeline. |
| #35 | BCS-000143 | BCS-000143 | The Arcanian Almanac |
| #35 | BCS-000144 | BCS-000144 | Arcanian Lore |
| #35 | BCS-000145 | BCS-000145 | Season 5 character creation |
| #35 | BCS-000146 | BCS-000146 | Elevator Guantlet. |
| #35 | BCS-000147 | BCS-000147 | Mirabelle – A Tragedy in Five Acts |
| #35 | BCS-000148 | BCS-000148 | Pigeon Lord- draft |
| #35 | BCS-000149 | BCS-000149 | Gil's Rebirth v1 |
| #35 | BCS-000150 | BCS-000150 | Monster Chess |
| #35 | BCS-000151 | BCS-000151 | Legends sign up |
| #32 | BCS-000131 | BCS-000152 | Area 16 Survival Challenge |
| #32 | BCS-000132 | BCS-000153 | Polish Session Draft |
| #32 | BCS-000133 | BCS-000154 | Game Tracking Update |
| #32 | BCS-000134 | BCS-000155 | Build Earthfall App |
| #32 | BCS-000135 | BCS-000156 | Build Fryvern Fight |
| #32 | BCS-000136 | BCS-000157 | Dnd Arcade Consumables |
| #32 | BCS-000137 | BCS-000158 | Caribbean Pirate Theme |
| #32 | BCS-000138 | BCS-000159 | Show Aggro Level 2 Art |
| #32 | BCS-000139 | BCS-000160 | New chat — Floor 2 Aggro art example |
| #32 | BCS-000140 | BCS-000161 | Plan Dead Turtle Transition |
| #32 | BCS-000141 | BCS-000162 | Rod Voice Achievement Generator |
| #34 | BCS-000131 | BCS-000163 | Saturday D&D ChatGPT project history recovery, May 28–31 2026 |
| #34 | BCS-000132 | BCS-000164 | Saturday D&D ChatGPT project history recovery, April 7 2026 |
| #34 | BCS-000133 | BCS-000165 | Saturday D&D ChatGPT project history recovery, May 14 2026 |
| #34 | BCS-000134 | BCS-000166 | Saturday D&D ChatGPT project history recovery, May 24 2026 |
| #34 | BCS-000135 | BCS-000167 | Saturday D&D ChatGPT project history recovery, May 29 2026 |
| #34 | BCS-000136 | BCS-000168 | Saturday D&D ChatGPT project history recovery, May 30 2026 |
| #34 | BCS-000137 | BCS-000169 | Saturday D&D ChatGPT project history recovery, June 13 2026 |
| #34 | BCS-000138 | BCS-000170 | Saturday D&D ChatGPT project history recovery, June 27 2026 |
| #34 | BCS-000139 | BCS-000171 | Saturday D&D ChatGPT project history recovery, July 11 2026 |
| #34 | BCS-000140 | BCS-000172 | Saturday D&D current Project conversation segment, July 29–August 8 2026 |

## Source counts

- historical recovery: 21 (BCS-000131–BCS-000151)
- Earthfall: 11 (BCS-000152–BCS-000162)
- Saturday D&D: 10 (BCS-000163–BCS-000172)
- total new sources: 42
- highest BCS: BCS-000172

## Relationship corrections

Earthfall donor links used `PROJECT_COMPANION_CONTEXT`, which source-history validation does not accept. Links from the eleven Earthfall history containers to BCS-000054 and BCS-000055 were rewritten to existing `COMPANION_TO`. The relationship vocabulary was not expanded.

## Registry reconciliation

Earthfall kept project_id `earthfall`. ChatGPT-history anchors were added to that record after renumbering; no second Earthfall campaign was created. Saturday D&D received a separate `saturday-dnd` project record. PR #35 did not add project records. Historical projects already on main remain intact.

## Derived outputs

- Readiness regenerated with `python scripts/validate_source_history.py --write-report` from the PR #31 script. `LONGITUDINAL_RESEARCH_READY` still means at least one qualifying trajectory edge, not a complete chain.
- Candidate triage regenerated with `python scripts/classify_drive_candidates.py --write` after PR #35 marked admitted Drive rows ingested.
- `indexes/documents.sqlite` rebuilt once from the combined tree. Donor branches had no SQLite index to merge. FTS rebuilt. VACUUM run.

## Validation

```
python ingest/validate_ingest.py
python registry/validate_registry.py
python scripts/validate_source_history.py
python scripts/test_substrate_queries.py
python scripts/test_source_readiness.py
python scripts/test_query_source_history.py
PRAGMA integrity_check;  -- ok
PRAGMA foreign_key_check;  -- no rows
```

All of the commands above passed on the reconciled tree. SQLite has 170 source_containers. Catalog has 172 BCS rows. BCS-000059 and BCS-000068 are pre-existing catalog rows without source containers on main; they were not dropped and were not invented.

Phrase searches reached the requested examples: Archavist Daysong (BCS-000142), Rowing Oak (BCS-000136/137), Monster Chess (BCS-000150), Master Timeline (BCS-000131), Fryvern (BCS-000156), Nassau / spot osha (BCS-000161), House of Measured Coin (BCS-000163 and later Saturday containers), Neris Quill and Vault Custodian (BCS-000172).

## Remaining source gaps

These are source gaps, not reconciliation failures.

- Earthfall and Saturday D&D remain partial Project-history recoveries. Missing assistant turns were not synthesized. Search fragments were not upgraded to transcripts. Generation was not treated as table delivery.
- Saturday BCS-000172 still contains more than one recovered visible segment; it was not repartitioned.
- Drive revision bodies and unread exports called out by the lineage ledger remain blocked exports, not missing reconciliation rows.
- Catalog-only BCS-000059 and BCS-000068 still have no container on main.

## Deferred work

- PR #33 human-object expansion. Newly accessible material that makes that index especially useful includes Archavist Daysong, Rowing Oak, R.O.D. (existing BCS-000055, now companion-linked from Earthfall history), Fryvern, House of Measured Coin, Neris Quill, Vault Custodian, Monster Chess, Mirabelle, and Arcanian systems. This pass did not build those human objects.
- Phase 2A Earthfall/Saturday research.
- Phase 2B design-method work.
- Remaining Drive gaps and revision bodies.

## Superseded branches inspected

- PR #29 substrate audit is superseded by PR #31, which this integration branch is stacked on. Not merged.
- PR #24 and PR #26 were not merged. They are older Drive integration drafts and are not donors for this pass.
- `docs/readiness-and-phase2-lanes` (`c0edfe192db5bc64f17776e0108cfcfd78d5d935`) states the longitudinal-ready caveat and the Phase 2A/2B split. That material is already represented on PR #31, including the README Stage 2 lane split. No unique source container is on that branch. Treat it as superseded/redundant for this reconciliation. Not deleted.

