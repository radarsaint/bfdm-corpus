# Project Decisions and Guardrails

**Purpose:** Preserve current project-level decisions from active planning.  
**Evidence status:** These are directives/guardrails, not historical corpus findings.

## Governing corpus invariant

> **bfdm-corpus is not primarily a training dataset. It is the durable research archive of Brendon's D&D creative history. Kit is one consumer of it.**

Operational interpretation:
- corpus preservation/provenance precede model convenience;
- Kit integration is downstream;
- no current architecture determines what historical material survives;
- model-facing datasets are rebuildable derivatives; the historical archive is canonical.

## Desired outcome for Kit

**Kit is the product. The total experience is the acceptance layer.**

The target is not merely competent DM judgment or successful retrieval. Kit should become an exceptionally satisfying Dungeon Master and creative partner across moment-to-moment play, sessions, campaigns, long-term relationship/continuity, campaign co-design, and eventually large-scale operation.

Judgment, cognition, memory, BFDM fidelity, runtime correctness, personality, latency, visuals, and UI are means. None is allowed to become the project goal by proxy.

BFDM should help Kit reason across Brendon's historical work without cloning its prose, while preserving source truth and uncertainty independently of whatever Kit architecture exists at the time.

## Current research sequence

The project has deliberately moved away from jumping directly from "archive" to "cognitive architecture."

### Stage 1 — Make history researchable
- Discord access;
- Drive integration;
- provenance;
- cross-source relationships;
- source-gap accounting;
- research usability.

**Current state:** substantially landed on `main`; bounded candidate/source-gap hardening remains.

### Stage 2 — Reconstruct expert judgment

Two lanes. No Phase 2B result set has landed.

**Phase 2A — Live judgment.** Requires appropriate live-decision evidence. The useful unit is a contrastable decision trajectory: what happened, what intervention or restraint occurred, what changed, and which condition explains the difference. Underway on draft PR #28. Not more generic "Brendon DM principles."

**Phase 2B — Creative method / worldbuilding.** Design artifacts can support bounded design claims without a live-play edge. Earthfall's R.O.D. documents, Bastion/Redoubt, and At War's End are eligible now. They do not establish how those designs performed at the table.

Research scope, kept separate from the readiness labels:

- Broad BFDM judgment claims: `NOT_READY`.
- Bounded live-judgment research: `READY_WITH_SCOPE_LIMITS` for source-traceable S3/S4 work that keeps its lineage limit explicit.
- Creative-method / worldbuilding research: `READY_WITH_SOURCE_LIMITS`. Design is not play.

### Stage 3 — Build and test minimal cognition
- decision recognition/classification;
- compact precedent cards derived from richer research cases;
- simple typed retrieval;
- structural applicability testing;
- context assembly;
- deferred binding experiments;
- attention representation.

**Current state:** future work. Build the benchmark before building precedent infrastructure.

Start with the cheapest system that can falsify the hypothesis. No GraphRAG, learned reranker, spreading activation, or elaborate precedent graph unless simple methods fail.

### Stage 4 — Architect from observed failures
Potential later concerns:
- campaign cognition;
- long-term memory architecture;
- strategic/local execution;
- durable workflows;
- entity cognition;
- learning/consolidation;
- large-scale operation.

**Current state:** architectural hypothesis space, not committed implementation.

The governing correction is that Stage 3 experiments come before committing to most Stage 4 architecture.

## Representation rule

When Stage 3 begins, preserve two representations:
- the rich research case with chronology, evidence, uncertainty, alternatives, retrospective interpretation, and counterfactuals;
- a compact precedent card containing only what comparison needs.

The card never replaces the case.

## Historical disagreement

Future precedent work should be able to represent relationships such as:
- `CORRECTED_BY`;
- `SUPERSEDED_BY`;
- `DIFFERS_BECAUSE`;
- `CONTRADICTS`;
- `COUNTEREXAMPLE_TO`;
- `NEGATIVE_PRECEDENT_FOR`.

A later different choice does not automatically prove an earlier choice was wrong.

## Epistemic guardrails

Keep these distinctions explicit:
- source present ≠ live use established;
- preparation ≠ play;
- publication ≠ play;
- revision trajectory ≠ live trajectory;
- archive gap ≠ evidence gap;
- unknown project ≠ missing source;
- candidate ≠ admitted source;
- source research ready ≠ longitudinal research ready;
- context source ≠ BFDM precedent;
- later version ≠ automatically superseding;
- open PR ≠ canonical main.

## Development over time

Do not flatten early and later Brendon into an average.

Research should distinguish:
- persistent traits;
- evolved practices;
- format-specific adaptations;
- abandoned/superseded practices;
- explicit later corrections.

S3/S4 evidence density must not masquerade as universal importance.

## Human-readable synthesis

A broad synthesis remains desirable, but not yet. Current work should build stronger cross-format decision trajectories before hardening a comprehensive model.

## Implementation restraint

Do not prematurely decide that Kit's corpus use must be RAG, fine-tuning, a static prompt, a graph, a simulated apprenticeship, or any other single mechanism.

The next architecture should be earned by experiments that expose actual failure modes.

## Layer separation

Keep separate:
1. raw sources;
2. attributable evidence/chronology;
3. research interpretation;
4. current project directives;
5. later runtime/precedent representations.

This lets conclusions change without rewriting history.
