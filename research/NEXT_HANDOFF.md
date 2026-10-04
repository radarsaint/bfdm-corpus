# Next Handoff

**Status:** Points 1–3 and 7 completed. Point 4 remains next. Empire City / S4 has a completed first deep research pass. Model-facing Discord retrieval infrastructure is now complete and validated.

## Point 1 — retrospective/current-project statements as attributable evidence
**Status: completed.**

Key additions:
- `BCS-000068`;
- `BCE-000005` through `BCE-000013`;
- `BCR-000005` through `BCR-000013`;
- retrospective claims and current-project directives now have bounded attributable evidence rather than surviving only as research paraphrase.

This includes the preserved retrospective/self-report evidence for:
- emergent interpersonal / "dating sim" play;
- changing screen names across seasons;
- Brendon ↔ `DM radar`;
- Roanoke sometimes reaching roughly 30–100 concurrent players;
- desired future Kit/corpus roles;
- the archive-first corpus directive.

## Point 2 — precise Work GPT ingestion contract
**Status: completed.**

Binding files:
- `INGESTION_CONTRACT.md`;
- `ingest/WORK_GPT_TASK.md`;
- `ingest/document_archive_schema.sql`;
- `ingest/source_metadata.schema.json`;
- `ingest/ingest_report.schema.json`;
- `ingest/validate_ingest.py`.

The contract covers legacy BCS reuse, native-ID/hash deduplication, Drive IDs, checksums, revisions/comments, source-form separation, version families, collaborative-authorship safeguards, validation, and ingest reporting.

## Point 3 — machine-readable campaign/project and identity registries
**Status: completed.**

Primary files:
- `registry/projects.jsonl`;
- `registry/series.jsonl`;
- `registry/project_relations.jsonl`;
- `registry/people.jsonl`;
- `registry/identities.jsonl`;
- `registry/discord_servers.jsonl`;
- schemas under `registry/*.schema.json`;
- `registry/validate_registry.py`.

Current counts:
- 11 projects;
- 1 series;
- 4 project relations;
- 4 canonical people;
- 4 identity assertions;
- 3 harvested Discord servers.

Important invariants:
- source-activity dates remain distinct from live campaign windows;
- the retrospective Roanoke 30–100 concurrency range is series-level only;
- early Roanoke remains pre-Season-2 / likely Season 1 lineage rather than being silently renamed;
- Season 5 / Legends retains naming uncertainty;
- S3 Brendon identity is immutable-account-ID scoped;
- Empire City / Season 4 is harvested and linked to `roanoke-s4`; Brendon is now account-ID confirmed there as Discord user `313689699627696139`, username `bfdm`, display name `DM radar`;
- source anchors are project relationships, not passage-level authorship claims;
- developmental ordering is chronology, not a quality/importance score.



## Model-facing corpus retrieval infrastructure
**Status: COMPLETE AND VALIDATED.**

The Git-LFS accessibility failure exposed by the Roanoke Season 3 Sandigil/Gil retrieval case is resolved without changing archive authority.

Canonical source remains:
- `discord/<server>/<server>.sqlite` in Git LFS.

Model-facing retrieval now lives under:
- `model-index/discord/<server>/manifest.json`;
- byte-capped `messages-NNNN.jsonl` shards;
- deterministic `terms/<prefix>.jsonl` term-to-shard routing files.

Operational files:
- `MODEL_RETRIEVAL.md`;
- `bfdm_inventory.jsonl`;
- `scripts/export_discord_model_index.py`;
- `scripts/search_corpus.py`;
- `scripts/sync_inventory_from_model_index.py`;
- `scripts/validate_model_index.py`;
- `.github/workflows/refresh-model-index.yml`.

Current mirrored Discord archives:
- Roanoke Season 3 — 197,013 messages;
- Empire City live server — 189,761 messages;
- Empire City Dev Corpus — 12,692 messages.

Important retrieval rule:
- do **not** depend on GitHub code search for Discord-message discovery;
- route a normalized term through `terms/<first-three-characters>.jsonl`, fetch the listed message shard(s), then expand local context;
- environments with shell access may use `scripts/search_corpus.py` for exhaustive projection search and a `coverage_report`;
- a zero result must not become a claim of absence when intended source families were inaccessible or only non-exhaustive discovery was attempted.

Original failure proof:
- `sandigil` resolves through `model-index/discord/roanoke-season-3/terms/san.jsonl`;
- the term index reports 81 S3 messages containing the exact token and routes to exact message shards;
- fetching routed shards returns original Discord rows with stable message IDs, timestamps, channels, authors, and adjacent context;
- `gil` similarly resolves through `terms/gil.jsonl`.

Automation:
- the workflow hydrates only Discord SQLite LFS objects, not attachment payloads;
- refresh runs are serialized;
- generated commits rebase onto current `main` before push to avoid non-fast-forward races;
- accessibility inventory is synchronized from actual generated mirrors;
- publication is blocked unless model-index integrity and inventory validation pass.

Validated CI run:
- workflow run `37243125394` completed successfully on 2026-10-04;
- checkout, targeted LFS hydration, export, inventory synchronization, model-index validation, inventory audit, commit, rebase, and push all passed.

Treat this as infrastructure, not derived research. The raw archive remains canonical; the model index is disposable/rebuildable retrieval machinery.


## Empire City / S4 research handoff
**Status: FIRST DEEP PASS COMPLETE; targeted gaps remain.**

Start here:
1. `research/empire-city/design-method-synthesis-v1.md`
2. `research/empire-city/longitudinal-decision-cases-v1.md`
3. `research/empire-city/decision-cases-v1.md`
4. `research/empire-city/source-fragment-map-v1.md`
5. `research/creative-method/historical-mythologization-v1.md`
6. `research/creative-method/cryptids-s3-s4-v1.md`

The longitudinal file contains 17 prep→play→aftermath cases plus cross-case distillation. Do not restart broad Empire City discovery.

Primary live source: `discord/empire-city/empire-city.sqlite`. Brendon attribution is resolved as Discord account `313689699627696139` / `bfdm` / `DM radar` and is recorded in `registry/identities.jsonl`.

High-value findings include:
- source seed → mythic transformation → game function → live adaptation;
- player attention/promotion rules through Invitationals;
- participation → responsibility → jurisdiction;
- recovery over reset;
- public media as shared memory;
- scene/thread/system/architecture intervention levels;
- identity embedded mechanically before being explicitly named;
- historical outcomes made contestable without losing recognizable hooks.

Resolved during the deep pass:
- Stock-market implementation is now resolved from Rob's **Wall Street Stock Market** Sheet plus the bot-development Discord: random baseline movement + authored plot adjustments, with the bot reloading sheet prices daily at 6 AM Pacific.

Targeted remaining gaps:
- direct final Congress ratification/result source;
- passage-level authorship in collaborative borough docs;
- exact “seat of the empire” wording is live by July 11; pre-launch June 9 material says “heart of Empire,” but no pre-launch copy of the exact naming line has been found;
- broader S2 comparison;
- voice/off-platform evidence remains unavailable.

`BCE-000014` preserves Brendon's retrospective statement about historical mysteries/details, *Neverwhere*, secret societies/institutions, and cryptids as source families.

Temporary branch `analysis/empire-city-distill` was used only to hydrate the LFS database. Do not merge its temporary workflow into main/research.


## Point 4 — reconcile the old 51-source staging body into canonical bfdm-corpus
**Status: IN PROGRESS — exact Library archive recovered and independently validated; binary-safe Git transfer remains pending.**

The 51-record legacy manifest is preserved, but the actual historical source containers/originals/assets remain incompletely reconciled with the canonical private repository.

Requirements:
- preserve every existing BCS ID;
- use `research/legacy-staging/manifest.all.jsonl` as the reconciliation map;
- reconcile originals, normalized/human-readable forms, assets, comments, and provenance where they exist;
- deduplicate against native Drive IDs/checksums rather than minting replacement source IDs;
- do not maintain the Library staging archive as a second canonical source store;
- produce an explicit reconciliation report showing migrated, already-present, duplicate, missing, and unresolved records.

The old Library staging archive remains a source for reconciliation, not a competing canonical corpus.

Current audited state:
- exact Library archive recovered: `brendon-corpus-staging.zip`, 86,948,434 bytes;
- archive SHA-256 independently reverified: `cebe18692ba3b8a2fe220d164cb722e18d81766edcc03f39ae0f18174350ea7a`;
- archive manifest contains exactly 51 unique BCS records across Roanoke (37), At War's End (8), Bastion/Redoubt (3), Earthfall (2), and Exploration Impossible context (1);
- all 51 normalized-body hashes match the archive manifest;
- all 51 original-file hashes match the archive manifest;
- every declared asset and every declared Brendon-native-comment file is present;
- 0 missing bundle files and 0 declared-hash mismatches were found;
- the previously reported 284 pending bundle files are independently reproduced: 51 `source.md`, 51 `metadata.json`, 51 `comments.json`, 5 `brendon-comments.native.json`, 51 originals, and 75 assets;
- those 284 canonical bundle files total 88,791,012 bytes;
- 51/51 legacy IDs already exist in the evidence catalog;
- 0/51 actual source-container bodies are present in canonical `sources/` / `context/`;
- `ingest/reconcile_legacy_staging.py` remains the canonical checkout migrator;
- `ingest/audit_legacy_staging_archive.py` now independently validates the staging archive before a checkout is involved and can emit an exact file-level transfer manifest;
- `research/legacy-staging/TRANSFER_AUDIT_2026-10-04.md` records the recovered-archive and transport state;
- the remaining blocker is specifically authenticated binary transfer into Git/GitHub. The Work shell has no GitHub credential and no outbound network; the GitHub connector has no local-file/file-reference upload action for arbitrary repository blobs. Source identification, archive identity, layout, and checksums are resolved.

Do not mark Point 4 complete until a final dry-run against the canonical checkout reports all 51 records `ALREADY_RECONCILED`.

## Point 5 — deliberate review and integration of PR #5
**Status: COMPLETE — PR #5 MERGED INTO `main`.**

Durable PR state:
- PR #5 was deliberately reviewed and merged into `main`;
- historical head branch: `research/organize-current-work-v1`;
Deliberate review is recorded in `research/PR5_REVIEW_2026-10-02.md`.

Reviewed for:
- archive-first consistency;
- stale status/provenance statements;
- schema/validator coherence;
- accidental derived-as-source promotion;
- private/public boundary problems;
- duplicated or superseded research files.

The review passed and PR #5 was merged. Agents should now treat current `main` as the canonical organizational/research baseline.

## Point 6 — recover the later Area 6c human-test transcript
**Status: OPEN.**

Current preserved artifact:
- `research/kit-evaluation/playtest-02-followup-human-findings.md`

Current limitation:
- later human findings are preserved;
- one exact quote is retained;
- the complete verbatim test transcript has not been recovered into the workspace.

If recovered:
- archive the transcript separately as source/evaluation evidence;
- preserve timestamps/source locator;
- reconcile the current summary against the transcript;
- do not silently rewrite the historical summary.

## Point 7 — archive-first governing principle
**Status: completed and governing.**

> **bfdm-corpus is not primarily a training dataset. It is the durable research archive of Brendon's D&D creative history. Kit is one consumer of it.**

Preserved as `BCE-000013` and hardened into corpus governance.

Operational consequence:
- archive fidelity outranks current model convenience;
- model-facing/training/RAG/personality artifacts are downstream derivatives;
- a current Kit architecture never determines what historical material survives.

## Current canonical baseline

PR #5 has been deliberately reviewed and merged.

New work should branch from current `main` unless a task-specific handoff says otherwise.

Historical integration branch:
- `research/organize-current-work-v1`

Merged PR:
- #5 — Organize current BFDM research and Kit evaluation


## Season 5 / Legends source integration
**Status: GOOGLE SITES CANONICALLY INTEGRATED; DEV DISCORD PENDING.**

Current canonical source chain:
- existing Season 5 Drive planning anchors in `registry/projects.jsonl`;
- `BCS-000113` — S5 Site Changelog / To Change;
- `BCS-000087`–`BCS-000112` — 26 linked player-facing Google Sites;
- `BCS-000114` — Way of Gun Fu Drive version-family source.

The Google Sites are no longer merely a source-lead archive: each has canonical BCS metadata/catalog admission, raw + normalized representations, project-registry anchors, chronology/coverage integration, and preserved capture metadata.

BCS IDs `000069`–`000086` remain reserved because they are already allocated on active branch `ingest/drive-project-v3`; the Season 5 integration starts at `BCS-000087` to avoid collision.

Do not infer live use from publication. Next high-value step after the Season 5 dev Discord lands is:
`Drive planning -> dev deliberation -> Site changelog/revision -> published Site -> partial live evidence`.
