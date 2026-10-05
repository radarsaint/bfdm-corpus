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
- cross-campaign comparison.

Repository visibility may change during active work; visibility is not part of corpus authority.

Current canonical branch: `main`.

Current operational handoff:
- `research/NEXT_HANDOFF.md`

Current open research branch:
- `research/phase2-decision-trajectories`
- draft PR #28 — Phase 2 decision contrast families.

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

Stage 2 is active on draft PR #28:
- decision trajectories;
- contrasts;
- restraint;
- failures;
- corrections;
- boundary conditions.

Do not turn Stage 2 directly into runtime infrastructure.

### Runtime/cognition work

Stage 3 and Stage 4 are later experimental/architectural work:
- precedent cards and simple retrieval;
- decision classification;
- context assembly;
- deferred binding;
- attention representation;
- only then heavier campaign cognition/memory architecture if experiments justify it.

## Current open PRs

- **#28** — active draft Phase 2 research.
- **#24** — older Drive relationship/pilot path; source bodies are not uniquely ahead of merged #25.
- **#26** — older Drive-history path; useful candidate-ledger material was incorporated into merged #25.

PR #25 is merged and is the canonical Drive-history baseline.

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

No layer should silently impersonate another.
