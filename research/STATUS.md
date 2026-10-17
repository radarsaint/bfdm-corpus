# Research Status

**Current as of:** 2026-10-17  
**Canonical branch:** `main`

> **Judgment status: NOT_A_STANDING_PRACTICE.** A citation, a confidence label, or a reusable-judgment sentence is derived wording. It is not a semantic verdict and it does not authorize Kit to use the claim. The contrast-family record is `research/integrity/contrast-family-verdicts.jsonl`.

This file describes current state. Dated audits and historical handoffs may intentionally describe older states.

## State legend

- **LANDED ON MAIN** — canonical repository state.
- **OPEN PR** — work exists but is not canonical until merged.
- **IDENTIFIED BACKLOG** — known candidate work, not yet admitted source material.
- **EVIDENCE GAP** — source exists but does not establish the desired historical fact.
- **ARCHIVE GAP** — a known artifact/source representation is missing or unreadable.

## LANDED ON MAIN — source substrate

### Discord retrieval

Model-facing Discord retrieval is complete and validated.

Canonical SQLite remains under `discord/`; model-facing retrieval uses `model-index/discord/<server>/` with byte-capped JSONL message shards and deterministic term-to-shard routing. GitHub code search is not required.

Major mirrored archives:
- Roanoke Season 3 — 197,013 messages;
- Empire City / Season 4 — 189,761 messages;
- Empire City Dev — 12,692 messages.

See `MODEL_RETRIEVAL.md`.

### Drive/source-history integration

PR #25 — **Connect Drive documents into campaign source histories** — merged into `main` at merge commit `3310c19cce17a04cea87562118b7e3b8e871c459`.

The old state "51-source staging body blocked on binary transfer" is obsolete.

Landed work includes:
- reconciliation/preservation of legacy source containers;
- stable BCS identity reuse and donor-collision cleanup;
- exact project/stage/family placement where evidence supports it;
- explicit unknowns where placement is not established;
- source-history traversal tooling;
- source-readiness vs longitudinal-readiness reporting;
- Empire City operations and publication material;
- Roanoke week operations and cited event modules;
- bounded prep→live links where message/channel evidence exists;
- Season 5 Drive→publication relationships;
- Week 5 map `BCS-000130`;
- explicit recognition that `BCS-000022` is blank at the source rather than a failed extraction.

### Reconciled source corpus (2026-10-05)

PR #31 and PR #36 merged the initial canonical source-container family through `BCS-000172`. That was the earlier milestone, not the current corpus ceiling.

Landed additions:
- research-critical historical Drive sources, `BCS-000131`–`BCS-000151`;
- Earthfall contemporary DM-workbench Project history, `BCS-000152`–`BCS-000162`, partial recovery, same Earthfall project;
- Saturday D&D contemporary DM-workbench Project history, `BCS-000163`–`BCS-000172`, partial recovery, separate project.

Donor PRs #32, #34, and #35 were closed without merge. Their provisional numbering must not be reintroduced. #36 is the canonical integration path. Combined `indexes/documents.sqlite` is the rebuilt non-Discord index.


### Scoped archive completion (2026-10-08)

PR #40 merged to main at `dc0d558188c3e492f69c34a8e278e0cf9e17373b`. That pass left **195 BCS identities through BCS-000195** and **193 indexed source containers**. BCS-000059 is context-only and BCS-000068 is an excerpt, not a missing pair of indexed source bodies. The repaired builder retrieves available source modification times, indexes historical comment sidecars (99 comments) and 90 preserved revision bodies; **259 revision rows lack fetched bodies**, with explicit warning/status rather than fabricated text. Authorship and Pigeon Lord provenance were corrected, and recoverable document structure was restored.

On 2026-10-17 the retrievable campaign backlog was admitted as **BCS-000196–BCS-000257** (62 containers). The catalog is **257** identities. The index count is **255** source containers. New containers are authorship UNKNOWN. They are sources, not judgments. Two Drive files that repeat an admitted text (the Kimmelian PDF, and Player handouts.pdf) share the container of that text. The week-1 file `1oJxfLF66bNPa7NPQjwW6GDzUVjJLRs30PWdvuQatrMU` repeats BCS-000048 and did not get a second id. The record is `research/drive-inventory/2026-10-17/admission.json`.

These repairs preserve, but do not solve, the missing historical revisions, Rowing Oak guide images, unreadable Bodfish Google Site, partial Earthfall/Saturday Project histories, and known-source gaps. They are capability-dependent archival follow-ups, not reasons to redo PR #40. Source readiness remains distinct from source-verified BFDM research and demonstrated Kit quality. The project's missing-consumer/early-completion repair is tracked in dnd-solo issue #118; the Project Gardener still requires an actual invoked reconciliation, not merely a status checker.

Primary current source-history/readiness files:
- `research/drive-integration/RESEARCH_READINESS_2026-10-05.md`;
- `research/drive-inventory/2026-10-03/TRIAGE_PASS_2026-10-05.md`;
- `scripts/query_source_history.py`.

### Readiness meanings

`SOURCE_RESEARCH_READY` means a researcher can tell what a source is, where it is placed (or that placement is explicitly unknown), its production stage (or explicit unknown), and whether live use has been tied to a message/channel. It does **not** mean the research has been done, and it does **not** mean a history can be followed.

`LONGITUDINAL_RESEARCH_READY` currently establishes the presence of at least one qualifying trajectory edge: a revision relation or a bounded live-contact relation. It does not establish a complete longitudinal chain. It does not mean every version is ordered, that prep, play, and aftermath are all present, or that the family is representative enough to sample as a finished history. Revision is not play. Publication is not play. A companion relation is not a trajectory. `REVISION_CONTEXT_FOR_SOURCE_FAMILY` is a weaker, separate path and does not by itself make a family longitudinally ready.

A source can therefore be source-ready while still carrying a longitudinal research gap.

## IDENTIFIED BACKLOG — Drive candidates

The 2026-10-03 ledger is no longer an unreviewed pool. Campaign bodies that could be retrieved are containers (BCS-000131–BCS-000151, then BCS-000173–BCS-000195, then BCS-000196–BCS-000257).

What was not given a container, and why, is in `research/drive-inventory/2026-10-17/admission.json`:

- household, quiz, audio-library, and non-campaign fiction rows;
- SRD chapters, magic-item catalogues, blank Tintagel templates, Mad Mage copies, Spelljammer Giff, Tarokka, and the Spelljammer ships PDF (third-party text was not copied);
- `1oJxfLF66bNPa7NPQjwW6GDzUVjJLRs30PWdvuQatrMU`, the same week-1 text as BCS-000048;
- `Player Races Final.pdf` (`1pvXV2yqH_oVtk16i5rRTQFY2KPKllcHg`), 52,351,233 bytes, over the 10 MB download cap;
- `Journal of the Red Ram.pdf` (`174l3B6vFI77IaXciz0cAJPx5pHxZEydT`), 22,742,795 bytes, over the 10 MB download cap.

No text was invented for the two files over the cap.

## EVIDENCE / ARCHIVE GAPS

Important current gaps include:
- broader live-play coverage outside S3/S4;
- Season 5 live play;
- Season 2 live play;
- Earthfall live-play evidence sufficient for honest decision-trajectory confirmation;
- passage-level authorship in collaborative material where not established;
- exact prep→live links for many source families;
- Player Races Final.pdf and Journal of the Red Ram.pdf, both over the 10 MB download cap;
- known blank source `BCS-000022`;
- later Area 6c human-test transcript remains unrecovered in full.

Archive gap and evidence gap are not interchangeable.

## LANDED ON MAIN — first-tranche derived-research integrity staging

PR #38 — **Audit and repair BFDM derived-research evidence chains** — merged to main as `2b68820d445e9f6d99d021463bfd76b2f7bb257d` (2026-10-16).

One audited tranche of 20 Roanoke S3 cases, inside the container set. The 20 are not the corpus. No corpus-wide semantic certification. Mechanically valid locators/citations are not semantic verification. BDC-S3-004 prep locators remain ORIGINAL_REPRESENTATION_UNAVAILABLE / SUPPORT_NOT_FOUND; the live Discord event is recoverable but does not repair the citations. Several propositions are PARTIALLY_SUPPORTED or SCOPE_OVERCLAIMED. Reusable judgments in the tranche are not verified for transfer and do not go into Kit. Untouched research stays UNVERIFIED.

## OPEN PR — strategic planning handoff

PR #37 — **Preserve strategic BFDM and Kit planning handoff** — is an open draft containing project direction, architecture sequencing, and operational planning. It is not historical BFDM evidence and is not canonical until merged.

## OPEN PR — Phase 2

PR #28 — **Phase 2: decision contrast families** — is open as a draft on branch `research/phase2-decision-trajectories`.

Primary artifact:
- `research/phase2/contrast-families-v1.md`

The draft also contains a stress pass and updates the research index.

Phase 2 has two lanes. No Phase 2B research artifact has landed.

**Phase 2A — Live judgment.** What conditions make one intervention happen rather than another during actual play? Claims about table decisions require live-decision evidence. The current draft is PR #28, `research/phase2/contrast-families-v1.md` and its stress pass, on `research/phase2-decision-trajectories`. S3 and S4 are the same large Roanoke-lineage multi-DM format. Do not edit those contrast files from substrate work.

**Phase 2B — Creative method / worldbuilding.** How are concepts, constraints, lore, places, institutions, mechanics, and premises turned into playable worlds? A design artifact does not need a live-play edge to support a bounded design-method claim. Earthfall's R.O.D. documents can support claims about how the broadcast premise is made systemic. Bastion/Redoubt can support claims about institutions, player role, public and private truth, requisition, and drop-in/drop-out design. At War's End can support world-model and revision claims. None of those texts establish how the design performed at the table.

Three research scopes, which are not the same word "ready":

- Broad BFDM judgment claims: `NOT_READY`. The corpus is not representative across eras and formats.
- Bounded live-judgment research: `READY_WITH_SCOPE_LIMITS`. Source-traceable S3/S4 work may continue if the lineage concentration and the missing evidence stay explicit.
- Creative-method / worldbuilding research: `READY_WITH_SOURCE_LIMITS`. Design artifacts may support design claims. They are not evidence of live implementation.

A Discord phrase search that returns zero, with `zero_match_means_absence`, establishes that the phrase is absent from the exhaustively searched Discord projection. It does not establish that a Drive document does not exist. The Season 4 Master Timeline was posted as a bare URL. The title is not in the message text.

## OPEN PR — next research drafts

PR #33 (`research/human-object-index-v0`) is the human-object index draft. Its seed is architectural. Broad expansion through the canonical BCS-000195 corpus has not been done and is not the immediate scarce-Work priority.

PR #28 (`research/phase2-decision-trajectories`) is the Phase 2 contrast-family draft. Its confidence labels are not verdicts and were not adopted. The Earthfall and Saturday workbench pass is on main in `research/integrity/contrast-family-adversarial-v1.md`. CF-08 is LIMIT. The other nine families are NOT_COMPARABLE on that partial surface. No family is certified, standing practice, or authorized for Kit.

## OPEN PR — older Drive branches

PR #24 and PR #26 are **closed without merge** as superseded by merged PR #25; their history remains readable. Neither contains a source body missing from merged PR #25:
- #24 is the older relationship-registry/pilot path;
- #26 is an older Drive-history integration path whose useful candidate-ledger work was incorporated into #25.

They are retained as branch/PR history and should not be treated as the current integration path.

## Immediate owning work after the completion correction

First prove the Project Gardener actually reconciles the PR #40/#115 semantic changes and that a fresh collaborator uses the revised Brain (dnd-solo #118). In parallel only where appropriate, resolve PR #27's Discord retrieval conflicts separately through Grok Build. The first-tranche audit and the contrast-family adversarial pass are on main. Neither certifies a standing practice. Leave image/revision/Project-history/other source gaps as explicit blocked archive tasks until needed access arrives. Do not promote a contrast family, a reusable judgment, or a high confidence label without a new integrity verdict.

## Research roadmap

Current program position is the Stage 1 → Stage 2 transition:

1. **Stage 1 — Research substrate:** source accessibility, Drive integration, historical relationships, gap accounting, research usability.
2. **Stage 2 — Reconstruct judgment,** in two lanes. **Phase 2A** is live judgment and needs live-decision evidence. **Phase 2B** is creative method and worldbuilding. Design artifacts can support design claims without live-play confirmation. No Phase 2B result set has landed.
3. **Stage 3 — Minimal cognition tests:** decision classification, precedent cards, simple retrieval, context assembly, deferred binding, attention representation.
4. **Stage 4 — Architect from observed failures:** campaign cognition, durable memory/workflows, strategic/local execution, entity cognition, learning/consolidation.

Do not build precedent-card infrastructure or finalize cognitive architecture while Phase 2 and remaining substrate hardening are still establishing what the system actually needs.
