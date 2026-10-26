# Next Handoff

**Current as of:** 2026-10-16 for the stage narrative below.  
**Queue corrected:** 2026-10-26 against `main` `a12d854c9089b9565d59f08552c11e61f185a4d7`. The ready pull requests were merged. #29 was closed without merge and its branch was kept. This does not rewrite historical reports, and it does not advance the shared Gardener checkpoint.  
**Canonical branch:** `main`

This is the current operational handoff. Older dated handoffs/audits are historical unless this file explicitly points to them.

## Cross-repository coordination

For any task that can affect Kit/runtime decisions, read repository-root `PROJECT_CONTROL.md` and `COORDINATION.md` first, then verify live `main` in both this repo and `radarsaint/dnd-solo` when the task crosses the boundary.

GitHub issues/PRs own live task state. Dated handoffs are orientation/history and must not silently outrank newer `main` or an explicitly named active draft.

### First-tranche integrity review — merged

PR #38 merged to `main` as `2b68820d445e9f6d99d021463bfd76b2f7bb257d`.

The reviewed set is 20 cases and 120 propositions: 78 `PARTIALLY_SUPPORTED`, 38 `SCOPE_OVERCLAIMED`, and 4 `CONTEXT_CHANGES_INTERPRETATION`. All 20 reusable judgments are `SCOPE_OVERCLAIMED`. None is a certified standing practice. The sample boundary in `research/integrity/README.md` still holds: this is not a model of how Brendon runs a game, and it does not authorize Kit.

A citation is still not semantic verification. BDC-S3-004's prep locators remain unrecovered. Do not restamp the ledger because a later edit is nearby. Untouched research stays `UNVERIFIED`.

The old audit branch is history. The gate that checks a pull request is `.github/workflows/research-integrity.yml` once that repair is on `main`. Until then, run `scripts/validate_research_evidence.py` against the revision you changed, with the Discord database left as its Git LFS pointer.

### Strategic planning draft — PR #37

PR #37 merged as `fc3376c1fa3a02a5cda061768b172008352bd2dd`. `research/STRATEGIC_HANDOFF_2026-10-05.md` is a dated planning snapshot. It is not current direction and not historical BFDM evidence. The catalog ceiling it records, BCS-000172, is not current.

## Friday ChatGPT Work queue

Use scarce Work capacity for evidence-heavy investigations that ordinary GPT should not do interactively.

Priority order:

1. **Do not reopen the finished first tranche.** Those 120 propositions are reviewed. A new case is a new tranche, not a restamp. Skip work that repeats PR #38.
2. **Earthfall/Saturday adversarial attack.** The first pass landed with PR #28: `research/phase2/earthfall-saturday-crossformat-tranche-2026-10-25.md`. It is not doctrine and not a restamp of PR #38. Do not quote its dispositions as verified practice. A further pass may still classify SUPPORT / LIMIT / BREAK / NEW_DIMENSION / NOT_COMPARABLE against containers this tranche did not cite.
3. **Restraint / negative-space sweep.** Find bounded cases where Brendon had an apparent opportunity to intervene, elaborate, rescue, promote, or intensify and deliberately did not. Absence claims require a defined searched surface.
4. **Failure -> diagnosis -> correction -> later behavior trajectories.** Require chronology and evidence that the later behavior is actually analogous; do not infer `CORRECTED_BY` from mere difference. A draft consolidation of the repeated cases, including the CF-04 qualification, is [PR #52](https://github.com/radarsaint/bfdm-corpus/pull/52): `research/phase2/consolidation-longitudinal-2026-10-26.md`. It is not merged and not doctrine.
5. **Phase 2B cross-format creative-method contrast.** Use direct design/revision evidence and do not claim table success.
6. **Selective authorship/acceptance reconstruction** only for workbench claims used by the substantive research above.

Wait until dependencies are satisfied before:
- structural same-nouns/different-decision benchmarks;
- decision recognition/classification experiments;
- scaled context-blindfold studies;
- precedent cards or retrieval systems.

Wrong use of Work:
- human-object index expansion;
- generic object lookup;
- normal source checks;
- corpus mechanics;
- GraphRAG/vector/reranker work;
- final cognition architecture.

Every Work run must have:
- exact repo/PR refs;
- finite evidence domain;
- exact stopping rule;
- required output artifact;
- scope limit;
- invalidation conditions;
- explicit do-not-duplicate instruction for active corpus-prep and PR #38 work.

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

PR #31 (substrate/readiness hardening) and PR #36 (reconciled source ingests) are merged. That consolidation's range is BCS-000001–BCS-000172. The catalog has since continued through BCS-000195. `BCS-000172` is not the current ceiling.

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

### PR #33 — MERGED

Merge: `97909f8168cdf36414158d6d2e0db03d032e52b3`  
Title: **Prototype corpus-wide human-object index**

The landed seed is 10 objects, 15 assertions, and 5 relations. It is not an inventory of the reconciled corpus. Expansion is not current scarce-Work. Do not treat the seed as a completed human-object index.

### PR #28 — MERGED

Merge: `a6a84d902a995e53b3ceb72bd535b909429493f9`  
Title: **Phase 2: decision contrast families**

Landed artifacts:
- `research/phase2/contrast-families-v1.md`
- `research/phase2/contrast-families-v1-stress.md`
- `research/phase2/earthfall-saturday-crossformat-tranche-2026-10-25.md`

Phase 2A is on `main` and is not confirmed practice. The ten contrast families and the stress pass were not rewritten by the 2026-10-25 tranche. That tranche records zero BREAK inside its cited Earthfall and Saturday spans, ten dispositions, and explicit UNKNOWN endings. It does not confirm the families. Bastion/Redoubt design claims and five Phase 2B hypotheses sit in labeled sections of the same file. They are not table results and they are not principles. At War's End was not read for the tranche and remains eligible for a later design-method claim. A design claim is not evidence the material was run.

`zero_match_means_absence` on a Discord phrase search means the phrase is absent from the exhaustively searched projection. The Season 4 Master Timeline was posted as a bare URL (`748279131455881360`, `752645676260917248`). A zero for the title does not prove the Drive document does not exist. PR #27 merged as `305588490f0148169dd42ec0f9b35531423f6081`. Do not redo retrieval maintenance, and do not change its semantics from a substrate branch.

Do not rewrite the landed contrast files from substrate cleanup. A new Phase 2 pass is a new artifact. Do not edit `contrast-families-v1.md` or `contrast-families-v1-stress.md` except to preserve their history.

### PR #24 — CLOSED WITHOUT MERGE

Closed 2026-10-07, not an open draft. Superseded by merged PR #25. The branch remains readable. It has no source body missing from #25. The landed relationship model rejects #24's competing source-relations registry.

### PR #26 — CLOSED WITHOUT MERGE

Closed 2026-10-07, not an open draft. Superseded by merged PR #25. Useful candidate-ledger material from that path was incorporated into #25. Do not revive it.

## Queue resolved on 2026-10-26

Inspected after the merges below. `main` at the correction was `a12d854c9089b9565d59f08552c11e61f185a4d7`. No open issues. None of these merges approves Kit. Repeated readings of one event are not independent corroboration. `KIT_CONSUMPTION` stays unapproved, including where dnd-solo #126 names a subset of #43. That Kit pull request was open and unmerged at this correction, and it pins corpus commit `bf56ca4f`, not #43's head.

| PR | Result |
| --- | --- |
| #27 | Merged `305588490f0148169dd42ec0f9b35531423f6081`. Retrieval maintenance. |
| #29 | Closed without merge. Branch `cursor/research-substrate-audit-081d` at `f2b1c27` is kept. Do not delete it. The 132-row triage stays there. |
| #33 | Merged `97909f8168cdf36414158d6d2e0db03d032e52b3`. Ten-object seed. Not an inventory. |
| #37 | Merged `fc3376c1fa3a02a5cda061768b172008352bd2dd`. Dated 2026-10-05 snapshot. Not current direction. |
| #42 | Merged `92acc3000ea204141281f782e9742a473f2542d5`. Player-option inventory. Publication is not play. |
| #43 | Merged `74df26ff90413d965189da8a97acf3bdf0750f68`. Bounded judgments. Not demonstrated Kit use. |
| #46 | Merged. Resurrection follow-through. Same announcement as BJ-003, plus the scroll limit. |
| #47 | Merged. Worker 2 payload. `FULL_REPORT_NOT_IMPORTED`. |
| #48 | Merged. Worker 4 capsules. The report text was restored in #55 after a stub replaced it. Not a certified practice. |
| #49 | Merged. GPT-6 preservation. Most rows are pointers. |
| #50 | Merged `a12d854c9089b9565d59f08552c11e61f185a4d7`. Ordinary-post sample. Validators re-ran on `37b0674c`. DR-20261016-41 is RL-03, not a second event. |
| #52 | Merged `e0ab29027a8b4f4697b808b130060cf24f081c6d`. Consolidation. The full researcher report was not imported. |

## Research program sequence

### Stage 1 — Research substrate
Source accessibility, Drive integration, historical relationships, gap accounting, research usability.

**State:** substantially landed; bounded hardening/backlog remains.

### Stage 2 — Reconstruct expert judgment

Two lanes. Both are on `main` after PR #28. The Phase 2B section is hypotheses, not a confirmed method.

**Phase 2A — Live judgment.** What conditions make one intervention happen rather than another during actual play? Requires live-decision evidence. Landed. Not confirmed practice. Do not edit `research/phase2/contrast-families-v1.md` or `contrast-families-v1-stress.md` from substrate work.

**Phase 2B — Creative method / worldbuilding.** How are concepts, constraints, lore, places, institutions, mechanics, and premises turned into playable worlds? The tranche's Part C is a hypothesis set on `main`, not a confirmed method. Earthfall, Bastion/Redoubt, and At War's End can support design claims from the texts that exist. They cannot establish table performance without separate live evidence. Saturday workbench design corrections in the tranche are partial recoveries, not session transcripts.

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
1. Phase 2A is on `main`. Further attacks are new artifacts, not edits that rewrite the ten families;
2. Phase 2B hypotheses are on `main`. Further design-method claims may use Earthfall, Bastion/Redoubt, and At War's End, and must not present those claims as live confirmation;
3. do not treat broad BFDM judgment claims as ready. Bounded S3/S4 live-judgment research may continue only with the lineage limit written down;
4. keep cases source-traceable and falsifiable;
5. do not convert Phase 2 directly into precedent cards yet.

## Explicitly do not redo

- Discord LFS/model-retrieval infrastructure;
- the 51-source legacy staging migration;
- broad Drive integration already merged via PR #25;
- the first-pass Drive candidate triage;
- broad Empire City discovery;
- Phase 2 contrast-family files, except a new pass that does not rewrite the landed families;
- precedent cards/runtime retrieval infrastructure;
- Kit cognitive architecture.

The next agent should add missing evidence or harden the substrate, not solve yesterday's blockers again.
