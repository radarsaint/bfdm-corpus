# Research Status

**Current as of:** 2026-10-04  
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

Primary current source-history/readiness files:
- `research/drive-integration/RESEARCH_READINESS_2026-10-05.md`;
- `research/drive-inventory/2026-10-03/TRIAGE_PASS_2026-10-05.md`;
- `scripts/query_source_history.py`.

### Readiness meanings

`SOURCE_RESEARCH_READY` means a researcher can tell what a source is, where it is placed (or that placement is explicitly unknown), its production stage (or explicit unknown), and whether live use has been tied to a message/channel. It does **not** mean the research has been done.

`LONGITUDINAL_RESEARCH_READY` means the family has a recorded trajectory through a revision relation or a bounded live-contact relation. Revision is not play. Publication is not play. A companion relation is not a trajectory.

A source can therefore be source-ready while still carrying a longitudinal research gap.

## IDENTIFIED BACKLOG — Drive candidates

The Drive candidate pool is no longer "134 unreviewed candidates."

Every candidate in the preserved 2026-10-03 ledger received a first-pass open attempt or a documented read failure. The result is a classified backlog, not admitted sources.

High-value campaign material remains for selective later containerization, including Ferrytown, Hampstead, Pigeon Lord, Mirabelle, Daysong, Rowing Oak, Arcanian material, and other items named in the triage report.

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

Phase 2 is reconstructing expert judgment through:
- decision contrasts;
- restraint;
- failure;
- correction;
- changed judgment;
- boundary conditions.

The current weakness is format concentration: S3 and S4 are both large Roanoke-lineage multi-DM campaigns. Earthfall was checked but does not yet have enough source-ready live evidence to support an honest confirmation.

Phase 2 is **not** precedent-card/runtime work.

## OPEN PR — older Drive branches

PR #24 and PR #26 remain open drafts.

Neither currently contains a source body missing from merged PR #25:
- #24 is the older relationship-registry/pilot path;
- #26 is an older Drive-history integration path whose useful candidate-ledger work was incorporated into #25.

They are retained as branch/PR history and should not be treated as the current integration path.

## Research roadmap

Current program position is the Stage 1 → Stage 2 transition:

1. **Stage 1 — Research substrate:** source accessibility, Drive integration, historical relationships, gap accounting, research usability.
2. **Stage 2 — Reconstruct judgment:** decision trajectories, contrasts, restraint, failures, corrections, boundary conditions.
3. **Stage 3 — Minimal cognition tests:** decision classification, precedent cards, simple retrieval, context assembly, deferred binding, attention representation.
4. **Stage 4 — Architect from observed failures:** campaign cognition, durable memory/workflows, strategic/local execution, entity cognition, learning/consolidation.

Do not build precedent-card infrastructure or finalize cognitive architecture while Phase 2 and remaining substrate hardening are still establishing what the system actually needs.
