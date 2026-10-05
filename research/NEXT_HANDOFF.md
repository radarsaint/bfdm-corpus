# Next Handoff

**Current as of:** 2026-10-05  
**Canonical branch:** `main`

This is the current operational handoff. Older dated handoffs/audits are historical unless this file explicitly points to them.

## What is complete on main

### Discord model retrieval

Complete and validated.

Use:
- `MODEL_RETRIEVAL.md`;
- `model-index/discord/`;
- `scripts/search_corpus.py` where shell access exists.

Do not restart the Git-LFS/Sandigil retrieval problem. Canonical SQLite remains source truth; the model-facing projection is the retrieval layer.

### Historical Drive/source integration

PR #25 (`ingest/drive-history-v1`) is **merged**.

The old Point 4 "51-source staging body / binary transfer pending" handoff is superseded. The reconciled legacy/source-history work is now on `main`.

Important landed capabilities/material:
- legacy BCS containers reconciled without renumbering canonical IDs;
- donor collisions resolved while keeping main authoritative;
- source metadata carries project/stage/family placement or explicit unknowns;
- source-history traversal with `scripts/query_source_history.py`;
- `SOURCE_RESEARCH_READY` vs `LONGITUDINAL_RESEARCH_READY`. The second currently establishes at least one qualifying trajectory edge. It does not establish a complete longitudinal chain;
- Empire City operational/source families;
- Roanoke week operations and cited modules;
- bounded prep→live links where supported;
- Season 5 publication relationships;
- Week 5 map as `BCS-000130`;
- `BCS-000022` documented as genuinely blank at the source.

### Drive candidate triage

The 2026-10-03 candidate ledger has received a first-pass triage.

Read:
`research/drive-inventory/2026-10-03/TRIAGE_PASS_2026-10-05.md`

The candidate pool is a classified backlog. It is not "134 unreviewed files" anymore. Significant campaign material remains for selective containerization; five candidates are explicitly unreadable/unavailable.

## Stage 1 after the 2026-10-05 consolidation

PR #31 (substrate/readiness hardening) and PR #36 (reconciled source ingests) are merged. Canonical BCS range is BCS-000001–BCS-000172.

The reconciled additions are research-critical historical Drive sources (BCS-000131–BCS-000151), Earthfall contemporary DM-workbench Project history (BCS-000152–BCS-000162), and Saturday D&D contemporary DM-workbench Project history (BCS-000163–BCS-000172). Earthfall and Saturday histories remain partial recoveries. Donor PRs #32, #34, and #35 are closed without merge and are not active ingestion paths.

Remaining source gaps are bounded and should not block the next research stages:
- selectively containerize high-value campaign material from the triaged Drive backlog;
- preserve/resolve the five unreadable/404 cases without inventing content;
- close source-family gaps where additional evidence supports a relationship;
- expand live-play coverage beyond S3/S4 where possible;
- keep archive gaps separate from evidence gaps;
- recover the complete later Area 6c human-test transcript if it becomes available.

Readiness discipline:
- source present ≠ live use established;
- preparation ≠ play;
- publication ≠ play;
- revision trajectory ≠ live trajectory;
- candidate ≠ admitted source;
- source research ready ≠ longitudinal research ready;
- one trajectory edge ≠ a complete longitudinal chain;
- a Discord zero ≠ historical nonexistence outside that searched projection;
- context source ≠ BFDM precedent;
- later version ≠ automatically superseding.

## Current open PRs relevant to this handoff

### PR #33 — OPEN DRAFT

Branch: `research/human-object-index-v0`  
Title: **Prototype corpus-wide human-object index**

The original seed is architectural. It has not been expanded across the reconciled corpus. Next GPT work can expand it across BCS-000001–BCS-000172. Do not treat the seed as a completed human-object index.

### PR #28 — OPEN DRAFT

Branch: `research/phase2-decision-trajectories`  
Title: **Phase 2: decision contrast families**

Primary artifact:
`research/phase2/contrast-families-v1.md`

Phase 2A is the live-judgment draft. Its current contrast families are not yet updated for the newly canonical Earthfall and Saturday D&D workbench sources. Those sources are partial recoveries and are available for a later SUPPORT / LIMIT / BREAK / NEW_DIMENSION / NOT_COMPARABLE pass. That pass has not been done. Bastion/Redoubt and At War's End remain eligible for Phase 2B design-method claims. A design claim is not evidence the material was run.

`zero_match_means_absence` on a Discord phrase search means the phrase is absent from the exhaustively searched projection. The Season 4 Master Timeline was posted as a bare URL (`748279131455881360`, `752645676260917248`). A zero for the title does not prove the Drive document does not exist. PR #27 owns retrieval maintenance. Do not change its semantics from a substrate branch.

Do not merge, rewrite, or expand PR #28 as part of ordinary substrate cleanup unless the task explicitly targets Phase 2.

### PR #24 — OPEN DRAFT, older path

Older Drive relationship-registry/pilot approach. It contains no source body missing from merged PR #25.

### PR #26 — OPEN DRAFT, older path

Older Drive-history integration approach. Its useful candidate-ledger material was incorporated into merged PR #25.

Do not treat #24 or #26 as the active Drive integration path.

## Research program sequence

### Stage 1 — Research substrate
Source accessibility, Drive integration, historical relationships, gap accounting, research usability.

**State:** substantially landed; bounded hardening/backlog remains.

### Stage 2 — Reconstruct expert judgment

Two lanes. No Phase 2B research artifact has landed.

**Phase 2A — Live judgment.** What conditions make one intervention happen rather than another during actual play? Requires live-decision evidence. Underway on draft PR #28. Do not edit `research/phase2/contrast-families-v1.md` or `contrast-families-v1-stress.md` from substrate work.

**Phase 2B — Creative method / worldbuilding.** How are concepts, constraints, lore, places, institutions, mechanics, and premises turned into playable worlds? Earthfall, Bastion/Redoubt, and At War's End can support design claims from the texts that exist. They cannot establish table performance without separate live evidence.

### Stage 3 — Minimal cognition tests
Decision classification, precedent cards, simple retrieval, context assembly, deferred binding, attention representation.

**State:** not current implementation work.

### Stage 4 — Architect from observed failures
Campaign cognition, long-term memory architecture, strategic/local execution, durable workflows, entity cognition, learning/consolidation.

**State:** later. Do not commit to heavy architecture before Stage 3 experiments reveal the need.

## Immediate next work

For substrate work:
1. use the Drive triage as a selective backlog, not as a mandate to ingest everything;
2. prioritize source families that materially improve cross-format/cross-era decision research;
3. record unreadable sources and explicit unknowns rather than inferring;
4. maintain the readiness distinction in `research/drive-integration/RESEARCH_READINESS_2026-10-05.md`.

For research work:
1. continue Phase 2A only on its dedicated draft branch/PR;
2. Phase 2B may use Earthfall, Bastion/Redoubt, and At War's End for design-method claims without waiting for live play, and must not present those claims as live confirmation;
3. do not treat broad BFDM judgment claims as ready. Bounded S3/S4 live-judgment research may continue only with the lineage limit written down;
4. keep cases source-traceable and falsifiable;
5. do not convert Phase 2 directly into precedent cards yet.

## Explicitly do not redo

- Discord LFS/model-retrieval infrastructure;
- the 51-source legacy staging migration;
- broad Drive integration already merged via PR #25;
- the first-pass Drive candidate triage;
- broad Empire City discovery;
- Phase 2 contrast-family work unless working directly on PR #28;
- precedent cards/runtime retrieval infrastructure;
- Kit cognitive architecture.

The next agent should add missing evidence or harden the substrate, not solve yesterday's blockers again.
