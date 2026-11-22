# Project Map

This file describes where current work belongs. It is project organization, not historical evidence.

## `radarsaint/bfdm-corpus` — canonical corpus and research

Use it for:
- canonical Discord harvests;
- model-facing corpus retrieval projections;
- machine-readable project/identity/source-history registries;
- normalized historical source containers;
- provenance, revisions, comments, and chronology;
- derived BFDM research;
- Kit evaluation records that belong with research history;
- cross-campaign comparison;
- portable research that could later inform Candy C, without creating that repository here.

Repository visibility may change during active work; visibility is not part of corpus authority.

Current canonical branch: `main`.

Current operational handoff:
- `research/NEXT_HANDOFF.md`

PR #28 merged. It is landed Phase 2 contrast-family research, not doctrine, and not an open draft. Do not treat this map's older "draft PR #28" wording as current queue state. Live `PROJECT_CONTROL.md` and `research/NEXT_HANDOFF.md` govern the open queue.

**Candy C** (candidste c) is the planned future GitHub repository for Kit's planned Bayesian drive. It is not a current repository, not another AI personality, and not created by this map.

## `radarsaint/dnd-solo` — Kit product/runtime

Use it for:
- Kit runtime;
- Dungeon of the Mad Mage/runtime integration;
- current game state, bridge, adjudication, memory, claims, procedures;
- tests/fixtures;
- active personality/product specifications;
- implementation experiments.

Historical public research scaffolding from `dnd-solo` is preserved/indexed in `bfdm-corpus/research/prior-dnd-solo/` where useful. `bfdm-corpus` is the canonical historical/research body.

## Current work boundaries

### Corpus/source work

Stage 1 is substantially landed. Remaining work is bounded:
- selective containerization from the triaged Drive backlog;
- explicit unreadable/archive gaps;
- missing live-contact evidence;
- broader live-play coverage.

Do not redo PR #25's source-history integration.

### Research work

Stage 2 reconstructs expert judgment from decision trajectories, contrasts, restraint, failures, corrections, and boundary conditions. Landed Phase 2 files are hypotheses/research, not confirmed practice.

Keep observed behavior, reconstructed judgment, evaluated effectiveness, and transferable knowledge distinct. Do not turn Stage 2 directly into runtime infrastructure or into Candy C.

### Runtime/cognition work

Stage 3 and Stage 4 are later experimental/architectural work:
- precedent cards and simple retrieval;
- decision classification;
- context assembly;
- deferred binding;
- attention representation;
- only then heavier campaign cognition/memory architecture if experiments justify it;
- the planned Bayesian drive / Candy C, which remains unimplemented.

Current research may gather knowledge those later stages would need. It must not implement them.

## Current open PRs

Open PRs are proposed state. Do not copy a stale numbered list into new work.

At the time this map was first written, #28 was an active Phase 2 draft and #24/#26 were older Drive paths. **#28, #25, #24, and #26 are no longer in that state:** #25 and #28 merged; #24 and #26 were closed as superseded. Use `research/NEXT_HANDOFF.md` for the live queue.

Unapproved research PRs, including #58, are not doctrine and are not restamped by orientation updates.

## Non-duplication rule

Before creating a new source or research artifact:
1. check current `main`;
2. check legacy staging/history;
3. check the Drive candidate ledger/triage;
4. check relevant prior research branches;
5. preserve stable IDs and explicit uncertainty.

## Authority distinction

- Source archive: **what exists?**
- Historical/evidence layer: **what can be attributed or linked?**
- Research layer: **what might it mean?**
- Runtime: **what is true/actionable in the current game?**
- Planned Candy C: **does not exist yet.** Naming it does not create it.

Inside the research layer, keep distinct:
- observed behavior;
- reconstructed judgment;
- evaluated effectiveness;
- transferable knowledge.

No layer should silently impersonate another.
