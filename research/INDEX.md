# BFDM Research Index

This index points to current research artifacts and distinguishes canonical main from open draft research.

## Current state and method

- [NEXT_HANDOFF.md](NEXT_HANDOFF.md) — current operational state, active PRs, and immediate next work.\n- [STRATEGIC_HANDOFF_2026-10-05.md](STRATEGIC_HANDOFF_2026-10-05.md) — project-wide north star, architecture direction, human-object layer, evidence-model corrections, campaign-simulation strategy, tool allocation, and sequencing distilled from the high-level planning thread.
- [STATUS.md](STATUS.md) — current source/research status.
- [SOURCE_COVERAGE.md](SOURCE_COVERAGE.md) — source-family coverage, backlog, archive gaps, and evidence gaps.
- [PROJECT_DECISIONS.md](PROJECT_DECISIONS.md) — current program guardrails; not historical evidence.
- [METHOD.md](METHOD.md) — research discipline and causality rules.
- [KNOWN_UNCERTAINTIES.md](KNOWN_UNCERTAINTIES.md) — explicit unresolved questions.
- [PROJECT_MAP.md](PROJECT_MAP.md) — where corpus, research, and runtime work belong.
- [CHRONOLOGY.md](CHRONOLOGY.md) — provisional source-anchored chronology.
- [CORRECTIONS_LOG.md](CORRECTIONS_LOG.md) — preserved corrections so errors do not harden into doctrine.
- [RESEARCH_STATE.json](RESEARCH_STATE.json) — machine-readable current-state snapshot.

[HANDOFF_AND_BACKLOG.md](HANDOFF_AND_BACKLOG.md) is a **superseded 2026-10-02 historical handoff**. It is retained for history; use NEXT_HANDOFF for current instructions.

## Stage 1 — Research substrate

### Discord retrieval

- [../MODEL_RETRIEVAL.md](../MODEL_RETRIEVAL.md) — model-facing Discord retrieval protocol.
- `model-index/discord/` — generated message shards and deterministic term routing.

Status: landed and validated on `main`.

### Drive/source-history integration

- [drive-integration/RESEARCH_READINESS_2026-10-05.md](drive-integration/RESEARCH_READINESS_2026-10-05.md) — source readiness, longitudinal readiness, archive/evidence gaps.
- [drive-inventory/2026-10-03/TRIAGE_PASS_2026-10-05.md](drive-inventory/2026-10-03/TRIAGE_PASS_2026-10-05.md) — classified Drive candidate backlog.
- `scripts/query_source_history.py` — source-family/history traversal.
- [legacy-staging/README.md](legacy-staging/README.md) and [legacy-staging/manifest.all.jsonl](legacy-staging/manifest.all.jsonl) — staging provenance/history, no longer the current migration blocker.

Status: PR #25, PR #31, and PR #36 are merged. Canonical containers run through BCS-000172, including historical Drive recovery and partial Earthfall/Saturday DM-workbench histories. Stage 1 is substantially broader and hardened, not exhaustive. Unreadable candidates, missing live evidence, and broader live coverage remain. Donor PRs #32, #34, and #35 are closed without merge.

## Stage 2 — Reconstruct expert judgment

Phase 2 has two lanes. The contrast files are on draft PR #28 until it merges. No Phase 2B research artifact has landed.

**Phase 2A — Live judgment** is the open draft. It asks what condition makes one intervention happen rather than another during play. It needs live-decision evidence. Current files, on the draft branch until PR #28 merges:
- `research/phase2/contrast-families-v1.md`;
- `research/phase2/contrast-families-v1-stress.md`.

**Phase 2B — Creative method / worldbuilding** has no research artifact yet. Design texts may support design claims without a live-play edge. Earthfall, Bastion/Redoubt, and At War's End are eligible. Those claims are not table results.

Broad BFDM judgment claims are `NOT_READY`. Bounded S3/S4 live-judgment work is `READY_WITH_SCOPE_LIMITS`. Creative-method research is `READY_WITH_SOURCE_LIMITS`.

Substrate queries on main:
- `scripts/query_source_history.py`
- `scripts/query_source_family.py`
- `scripts/query_project_history.py`
- `scripts/query_archive_gaps.py`
- `scripts/query_research_readiness.py`

## Stage 3 — Minimal cognition tests

Planned only after enough strong decision trajectories exist:
- decision recognition/classification;
- precedent cards derived from rich research cases;
- simple typed retrieval;
- structural applicability tests;
- context-blindfold/context-assembly experiments;
- deferred binding;
- multiplayer attention representation.

Do not build a heavy retrieval/precedent architecture before the benchmark exposes a need.

## Stage 4 — Architect from observed failures

Later hypothesis space:
- campaign cognition;
- long-term memory architecture;
- strategic/local execution;
- durable workflows;
- entity cognition;
- learning/consolidation;
- large-scale operation.

This is not current implementation work.

## Existing S3 research

- [roanoke-s3/decision-cases-v1.md](roanoke-s3/decision-cases-v1.md)
- [roanoke-s3/longitudinal-decision-cases-v2.md](roanoke-s3/longitudinal-decision-cases-v2.md)
- [roanoke-s3/revision-family-v3.md](roanoke-s3/revision-family-v3.md)
- [roanoke-s3/README.md](roanoke-s3/README.md)

Historical draft PRs #2–#4 remain provenance; their useful products were organized into the merged research baseline.

## Empire City / Season 4

Read in this order:
1. `empire-city/design-method-synthesis-v1.md`;
2. `empire-city/longitudinal-decision-cases-v1.md`;
3. `empire-city/decision-cases-v1.md`;
4. `empire-city/source-fragment-map-v1.md`;
5. `empire-city/player-feedback-v1.md`;
6. `empire-city/README.md`.

Do not restart broad Empire City discovery; return to primary sources for named gaps or a new research question.

## Current synthesis and creative-method leads

- [current-synthesis/working-model-2026-10-01.md](current-synthesis/working-model-2026-10-01.md) — provisional historical synthesis; not an answer key.
- [creative-method/bowling-event.md](creative-method/bowling-event.md)
- [creative-method/historical-mythologization-v1.md](creative-method/historical-mythologization-v1.md)
- [creative-method/cryptids-s3-s4-v1.md](creative-method/cryptids-s3-s4-v1.md)
- [creative-method/mythic-institutions-s3-s4-v1.md](creative-method/mythic-institutions-s3-s4-v1.md)

## Kit evaluation

- [kit-evaluation/README.md](kit-evaluation/README.md)
- [kit-evaluation/playtest-01-character-onboarding.md](kit-evaluation/playtest-01-character-onboarding.md)
- [kit-evaluation/playtest-02-area-6c-gambling.md](kit-evaluation/playtest-02-area-6c-gambling.md)
- [kit-evaluation/playtest-02-followup-human-findings.md](kit-evaluation/playtest-02-followup-human-findings.md)
- [kit-evaluation/REGRESSION_TARGETS.md](kit-evaluation/REGRESSION_TARGETS.md)

## Rule for future research additions

Every new artifact should answer:
1. what sources support it;
2. whether it is observation, interpretation, hypothesis, or developmental conclusion;
3. what campaign/format constraints limit transfer;
4. what evidence could falsify it.
