# Corpus Architecture Tracking Baseline

**Captured:** 2026-10-04  
**Canonical main SHA:** `9a34f6d418bbe15dbaf37a7add4ca8e335660e81`  
**Purpose:** track whether ongoing BFDM corpus work is moving toward the requirements identified by Kit cognitive-architecture research.

This is a status snapshot, not corpus doctrine.

## 1. Canonical main

Current main includes:

- archive-first governance;
- BCS/BCE/BCR evidence model;
- project/person/identity/Discord registries;
- Roanoke S3 canonical Discord harvest;
- Empire City live Discord harvest;
- Empire City Dev Corpus harvest;
- first deep S3/S4 research artifacts;
- canonical Season 5 / Legends Google Sites source family;
- readable Markdown projections for the Season 5 Sites;
- PR #10 model-accessibility framework:
  - `bfdm_inventory.jsonl`;
  - accessibility profiles;
  - deterministic Discord SQLite → JSONL exporter;
  - inventory validator;
  - GitHub Actions projection builder.

### Important current failure on main

PR #10's framework is merged, but its generated Discord text projection has **not yet landed**.

Observed on main:
- `bfdm_inventory.jsonl` still marks Roanoke S3 `model_cloud=OPAQUE`;
- `generated_mirrors=[]`;
- `model/` does not exist;
- repository connector reports `is_code_search_indexed=false`.

Therefore the original LFS accessibility failure is **not yet operationally resolved on main**, despite the framework existing.

## 2. Active Discord retrieval candidate

Branch: `ingest/discord-retrieval-v1`

This branch is materially more complete than the current main accessibility implementation.

It provides ordinary-Git text retrieval for all three canonical Discord harvests:

| Harvest | Messages | Attachments |
|---|---:|---:|
| Roanoke Season 3 | 197,013 | 1,421 |
| Empire City | 189,761 | 3,528 |
| Empire City Dev | 12,692 | 639 |
| Total | 399,466 | 5,588 |

Key mechanisms:
- `indexes/discord/catalog.json`;
- deterministic source-bearing JSONL shards;
- token lookup routers;
- channel navigation;
- entity/alias support;
- local disposable FTS cache;
- context/reply/attachment lookup;
- checksum/freshness verification;
- no-LFS consumer path;
- regression/acceptance tests.

Recorded validation includes:
- 13 tests passed;
- all 399,466 messages checked for field parity;
- all 5,588 attachment references checked;
- two full exports byte-identical;
- S3 Sandigil/Gil regression query passes;
- GitHub-only navigation works from ordinary text files.

This branch is strongly aligned with the research-access-plane requirement because it does **not** depend on GitHub code-search indexing being available.

It is not yet merged to main. Further Work GPT work on this retrieval layer is currently paused awaiting token refresh, not blocked by an unresolved architecture decision.

## 3. Active Drive/source ingestion

Branch: `ingest/drive-project-v3`

This branch is substantially ahead of main and currently records:

- legacy staging reconciliation complete for `BCS-000017`–`BCS-000067`;
- 51/51 legacy records reconciled;
- source/container bodies, originals, metadata, comments and staged assets preserved where present;
- `BCS-000001`–`BCS-000016` canonical Empire City source containers built;
- readable bodies and Google-native export snapshots preserved;
- native comments/replies and available revision metadata captured;
- 224 unique Drive search hits inventoried;
- 66 already represented;
- 158 uncataloged candidates remain to classify.

This branch is not yet merged.

Season 5 integration deliberately reserved `BCS-000069`–`BCS-000086` because they are allocated on this active branch, showing active collision avoidance between concurrent ingest work.

## 4. Season 5 / Legends state

Merged PRs #8 and #9 added and canonically integrated the Season 5 Google Sites family.

Current main includes:
- 26 published Sites;
- raw HTTP HTML snapshots;
- normalized readable Markdown;
- page/provider metadata;
- hashes;
- link relationships;
- BCS IDs `BCS-000087`–`BCS-000112`;
- `BCS-000113` S5 Site Changelog / To Change;
- `BCS-000114` Way of Gun Fu Drive extraction;
- chronology and source-coverage integration.

This is a good example of the desired archive pattern:
**source-faithful raw representation + directly searchable human-readable projection + provenance + version-family relationships.**

Season 5 development Discord remains pending canonical ingest/registration.

## 5. Current harvest coverage

Canonical registry now has three Discord servers, even though some narrative status docs remain stale:

1. Roanoke Season 3 — 197,013 messages.
2. Empire City live server — 189,761 messages.
3. Empire City Dev Server — 12,692 messages.

This means `research/STATUS.md` and parts of `research/NEXT_HANDOFF.md` on main are already behind current source state and should not be treated as exhaustive operational truth without checking registries/current branches.

## 6. Alignment against Kit/BFDM architecture

### A. Archive durability and source fidelity
**Direction: strong.**

Evidence:
- canonical raw/source separation;
- stable BCS IDs;
- hashes and native provider IDs;
- comments/revisions retained;
- LFS used for binary payloads;
- source/readable projections separated.

### B. Human/research-agent observability
**Direction: improving rapidly, not complete on main.**

Good:
- Season 5 Markdown projections are directly inspectable.
- `ingest/discord-retrieval-v1` implements a mature ordinary-text Discord access plane.
- PR #10 makes accessibility state explicit rather than silently assuming LFS is usable.

Gap:
- main still has no generated Discord mirror;
- code-search indexing is currently unavailable;
- current accessibility inventory covers only Roanoke S3.

### C. Provenance and identity
**Direction: strong.**

Evidence:
- BCS/BCE/BCR ontology;
- project, person, identity, Discord-server registries;
- native Discord IDs preserved;
- Drive/provider IDs and hashes retained;
- explicit authorship uncertainty;
- source activity distinguished from campaign live dates.

### D. Episodic/case research layer
**Direction: promising but still research-document heavy.**

Present:
- S3 decision cases;
- S3 longitudinal cases;
- 17 Empire City prep→play→aftermath cases;
- bounded creative-method synthesis.

Gap:
- no mature canonical machine-readable episode/case store yet;
- cases are not yet standardized into the typed episodic representation proposed for future Kit cognition.

### E. Semantic/procedural knowledge distillation
**Direction: early.**

Present:
- cross-case findings;
- creative-method leads;
- bounded design-method synthesis.

Gap:
- no explicit versioned method objects with scope, counterexamples, confidence, supersession, and runtime-export status.

### F. Private-to-portable Kit knowledge boundary
**Direction: conceptually identified, implementation not begun.**

The corpus remains the research archive.
There is not yet a separate published cognition/methodology runtime or export package.

### G. Evaluation
**Direction: partial.**

Present:
- held-out research directory;
- Kit evaluation artifacts;
- Area 6c scenario/evaluation work;
- Discord retrieval acceptance tests.

Gap:
- no unified trajectory-level cognitive evaluation harness spanning retrieval, salience, judgment, adjudication, state, and expression.

## 7. Tracking questions for future refreshes

On each future check, compare against this snapshot:

1. Has ordinary-text Discord retrieval reached `main`?
2. Can a GitHub-connected model retrieve S3 facts without LFS hydration?
3. Does retrieval cover every canonical Discord harvest automatically?
4. Has `bfdm_inventory.jsonl` expanded beyond one source?
5. Has `ingest/drive-project-v3` merged cleanly?
6. How many of the 158 uncataloged Drive candidates have been classified/ingested?
7. Has Season 5 development Discord been harvested and registered?
8. Are stale status/handoff docs reconciled with registry truth?
9. Is a typed machine-readable episode/case layer emerging?
10. Are research findings beginning to graduate into versioned procedural/method knowledge?
11. Is there a defined BFDM → portable Kit cognition export boundary?
12. Can humans and unspecialized research agents inspect every important machine representation?
13. Are new access mechanisms tested against real historical retrieval questions, not only unit fixtures?
14. Are authoritative source stores still independent of current Kit architecture?

## 8. Current judgment

The corpus is moving **toward** the proposed architecture.

The strongest movement is in:
- source fidelity;
- provenance;
- direct human-readable source preservation;
- explicit accessibility accounting;
- deterministic Discord retrieval;
- cross-era/source coverage.

The largest remaining structural gap is no longer "can we save the history?"

It is becoming:

> **Can we turn a broad, inspectable historical archive into typed episodes, precedents, concepts, methods, and evaluations without losing provenance or making the runtime dependent on the private archive?**

That is the next architecture-level question this tracker is meant to watch.
