# Research Status

**Current as of:** 2026-10-05  
**Canonical branch:** `main`

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

PR #31 and PR #36 are merged. Canonical source containers now run through `BCS-000172`.

Landed additions:
- research-critical historical Drive sources, `BCS-000131`–`BCS-000151`;
- Earthfall contemporary DM-workbench Project history, `BCS-000152`–`BCS-000162`, partial recovery, same Earthfall project;
- Saturday D&D contemporary DM-workbench Project history, `BCS-000163`–`BCS-000172`, partial recovery, separate project.

Donor PRs #32, #34, and #35 were closed without merge. Their provisional numbering must not be reintroduced. #36 is the canonical integration path. Combined `indexes/documents.sqlite` is the rebuilt non-Discord index.


Primary current source-history/readiness files:
- `research/drive-integration/RESEARCH_READINESS_2026-10-05.md`;
- `research/drive-inventory/2026-10-03/TRIAGE_PASS_2026-10-05.md`;
- `scripts/query_source_history.py`.

### Readiness meanings

`SOURCE_RESEARCH_READY` means a researcher can tell what a source is, where it is placed (or that placement is explicitly unknown), its production stage (or explicit unknown), and whether live use has been tied to a message/channel. It does **not** mean the research has been done, and it does **not** mean a history can be followed.

`LONGITUDINAL_RESEARCH_READY` currently establishes the presence of at least one qualifying trajectory edge: a revision relation or a bounded live-contact relation. It does not establish a complete longitudinal chain. It does not mean every version is ordered, that prep, play, and aftermath are all present, or that the family is representative enough to sample as a finished history. Revision is not play. Publication is not play. A companion relation is not a trajectory. `REVISION_CONTEXT_FOR_SOURCE_FAMILY` is a weaker, separate path and does not by itself make a family longitudinally ready.

A source can therefore be source-ready while still carrying a longitudinal research gap.

## IDENTIFIED BACKLOG — Drive candidates

The Drive candidate pool is no longer "134 unreviewed candidates."

Every candidate in the preserved 2026-10-03 ledger received a first-pass open attempt or a documented read failure. The result is a classified backlog, not admitted sources.

The research-critical names from that triage pass — Ferrytown, Hampstead, Pigeon Lord, Mirabelle, Daysong, Rowing Oak, and the Arcanian almanac/lore — are now containers in BCS-000131–BCS-000151. Other triaged candidates remain a classified backlog, not admitted sources.

Five candidates remain unreadable/unavailable for documented reasons:
- three Drive 404s;
- one image-style PDF with no text layer;
- one DOCX the connector would not return as text.

Candidate ≠ source. Do not assign BCS IDs merely because a triage row looks useful.

## EVIDENCE / ARCHIVE GAPS

Important current gaps include:
- broader live-play coverage outside S3/S4;
- Season 5 live play;
- Season 2 live play;
- Earthfall live-play evidence sufficient for honest decision-trajectory confirmation;
- passage-level authorship in collaborative material where not established;
- exact prep→live links for many source families;
- unreadable/404 Drive candidates above;
- known blank source `BCS-000022`;
- later Area 6c human-test transcript remains unrecovered in full.

Archive gap and evidence gap are not interchangeable.

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

PR #33 (`research/human-object-index-v0`) is the human-object index draft. Its seed is architectural. Expansion across BCS-000131–BCS-000172 has not been done.

PR #28 (`research/phase2-decision-trajectories`) is the Phase 2 contrast-family draft. Earthfall and Saturday D&D workbench sources are now on main for a later cross-format pass. That pass has not been done.

## OPEN PR — older Drive branches

PR #24 and PR #26 remain open drafts.

Neither currently contains a source body missing from merged PR #25:
- #24 is the older relationship-registry/pilot path;
- #26 is an older Drive-history integration path whose useful candidate-ledger work was incorporated into #25.

They are retained as branch/PR history and should not be treated as the current integration path.

## Research roadmap

Current program position is the Stage 1 → Stage 2 transition:

1. **Stage 1 — Research substrate:** source accessibility, Drive integration, historical relationships, gap accounting, research usability.
2. **Stage 2 — Reconstruct judgment,** in two lanes. **Phase 2A** is live judgment and needs live-decision evidence. **Phase 2B** is creative method and worldbuilding. Design artifacts can support design claims without live-play confirmation. No Phase 2B result set has landed.
3. **Stage 3 — Minimal cognition tests:** decision classification, precedent cards, simple retrieval, context assembly, deferred binding, attention representation.
4. **Stage 4 — Architect from observed failures:** campaign cognition, durable memory/workflows, strategic/local execution, entity cognition, learning/consolidation.

Do not build precedent-card infrastructure or finalize cognitive architecture while Phase 2 and remaining substrate hardening are still establishing what the system actually needs.
