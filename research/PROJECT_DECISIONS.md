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

Kit should eventually be useful as both:
1. a competent solo/small-table Dungeon Master;
2. a creative design partner capable of reasoning across Brendon's historical work rather than cloning its prose.

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
- decision trajectories;
- contrasts;
- failures;
- restraint;
- corrections;
- changed judgment;
- scope/boundary conditions.

**Current state:** underway experimentally on draft PR #28.

The priority is no longer to extract more generic "Brendon DM principles." The useful research unit is a contrastable decision trajectory: what happened, what intervention/restraint occurred, what changed, and which condition explains the difference.

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
