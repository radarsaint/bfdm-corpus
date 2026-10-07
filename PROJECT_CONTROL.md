# Project Control — BFDM corpus and research

**Updated:** 2026-10-07  
**Canonical main inspected:** `65513f294e72a3eb961d5699c21ddc1f14ceef2c`  
**Sibling repo:** `radarsaint/dnd-solo`

Read `COORDINATION.md` before substantial cross-agent work.

This file is deliberately short and rewritable. Git history, issues, PRs, and dated research artifacts preserve history.

## What this repo is

`bfdm-corpus` is the durable research archive of Brendon's D&D creative history and the environment for source-grounded BFDM research.

It is not primarily a training dataset.

Kit is one consumer.

## Canonical main state

At the inspected `main`:

- canonical source containers run through **BCS-000172**;
- Discord model-facing retrieval is complete and validated;
- historical Drive/source integration is substantially landed;
- Earthfall and Saturday D&D workbench recoveries are canonical but partial;
- Stage 1 is substantially landed with bounded hardening/gaps;
- broad BFDM judgment claims are **NOT_READY**;
- bounded S3/S4 live-judgment research is only ready with lineage/scope limits;
- creative-method/worldbuilding research is ready only for bounded design claims;
- Stage 3 minimal cognition tests and Stage 4 architecture are intentionally later.

Use `research/NEXT_HANDOFF.md`, `research/STATUS.md`, and `research/RESEARCH_STATE.json` for detailed canonical state.

## Friday research posture

The current research bottleneck is increasingly **epistemic rather than mechanical**.

Friday ChatGPT Work should not be spent on broad ingestion, searchability, generic BFDM principles, human-object expansion, precedent infrastructure, GraphRAG, or final cognition design.

Highest-value Work targets are:

1. semantically verify only the high-leverage derived propositions that downstream Phase 2 / Stage 3 work actually depends upon;
2. adversarially attack PR #28's candidate families with independently reconstructed Earthfall/Saturday workbench evidence;
3. search for deliberate restraint / non-intervention cases that visible-action-heavy research is likely to miss;
4. reconstruct bounded failure -> diagnosis -> correction -> later-behavior trajectories;
5. only after enough cases are semantically trusted, build structural contrast/recognition benchmarks.

Every Work task should have a finite question, finite evidence domain, explicit stopping rule, scope limit, and invalidation condition.

If PR #38 has already completed a needed semantic review by launch time, do not duplicate it.

## Active draft state that materially affects trust

Open draft PRs are not canonical main, but some are important current work:

- **#38 — forensic derived-research integrity audit.** Active as of 2026-10-07; head observed at `db69c938d26416f062cc68c8930bd2e10aef0b80`. Its first tranche stages 20 S3 decision cases / 120 propositions, all currently `UNVERIFIED`. This does not mean those propositions are false; it means semantic trust has not yet been earned. BDC-S3-004 already demonstrates a broken prep-evidence reconstruction chain while leaving the live Discord event recoverable.
- **#28 — Phase 2 decision contrast families.** Draft live-judgment research; not doctrine and not merged.
- **#33 — human-object index prototype.** Draft projection, not source truth and not complete.
- **#37 — strategic BFDM / Kit planning handoff.** Project direction/planning, not historical BFDM evidence and not canonical main.

Any worker relying on one of these must name the PR and branch explicitly.

Important refinement: `READY_WITH_SCOPE_LIMITS` in source/readiness documentation means the evidence surface can be researched. It does **not** certify that existing derived summaries/cases over that evidence have passed semantic review.

## Authority traps

- Historical/pinned Kit or BFDM documents may call themselves canonical while describing an older state.
- The in-repo BFDM mirror inside `dnd-solo` is not canonical research truth.
- BFDM PRs #24 and #26 remain open but are older Drive-integration paths superseded in substance by merged PR #25.
- PR #28 and PR #33 are active drafts, not landed research products.
- Repository visibility is not part of corpus authority; stale “private” wording in Kit-side artifacts must not affect which repo is canonical.

## Research discipline

Preserve these distinctions:

- source present != live use established;
- preparation != play;
- publication != play;
- revision trajectory != live trajectory;
- candidate != admitted source;
- archive gap != evidence gap;
- open PR != canonical main;
- citation != semantic verification;
- generated AI text != Brendon authorship;
- request != acceptance != implementation.

Prefer explicit UNKNOWN over invented continuity.

## Relationship to current Kit quality evidence

The 2026-10-07 Kit quality audit found that current runtime implementation has advanced significantly beyond the last serious human player-facing evaluation.

BFDM research does **not** close that gap. Even excellent source-grounded research cannot establish that current Kit has acquired or successfully expresses the corresponding DM skill.

Current rule:

> do not use BFDM research quality as a proxy for current Kit play quality.

Where a BFDM finding is proposed as useful DM intelligence, later Kit evaluation should test whether it changes the right decision or improves the lived experience in a held-out/current-build situation.

## Four-audit synthesis

The October 7 runtime, quality, research-readiness, and project-truth audits converge on one governing correction:

> **proxy evidence is not demonstrated truth.**

For BFDM specifically:
- retrievable source != verified derived claim;
- polished/cited research != semantically trusted research;
- research trust != evidence that current Kit performs the skill;
- current planning docs != canonical history.

Keep executable truth, player-experience evidence, research trust, and coordination authority distinct.

## Product relationship

BFDM research exists to improve Kit's craft and understanding, but BFDM is not the product.

**Kit is the product. The total experience is the acceptance layer.**

Research should improve what Kit can recognize, understand, decide, create, remember, or avoid. A research artifact succeeding on its own terms does not prove that Kit's player experience improved.

## Current temporary parallel work

Another GPT is already doing mechanical corpus preparation. Do not duplicate ingestion, normalization, indexing, source-container cleanup, or retrieval-layer preparation.

Temporary audits:

- GPT 1 — project truth / contradiction audit (complete; incorporated);
- GPT 2 — Kit quality / failure-localization audit (complete; incorporated);
- GPT 3 — BFDM research-readiness / ChatGPT Work queue (complete; preserved in `research/audits/2026-10-07-chatgpt-work-readiness.md`);
- Grok Build — executable `dnd-solo` runtime audit (complete);
- control-room thread — cross-report synthesis.

These assignments are temporary. Future ownership lives in current issues/PRs.

## Cross-repo rules

Use `dnd-solo main` for executable runtime truth.

Do not infer current Kit behavior from corpus planning artifacts, old runtime mirrors, Project ZIPs, or historical playtest branches.

When research is proposed for runtime hardening, preserve the evidence/provenance chain and current confidence/scope.

## Start points

For corpus/research state: this file -> `research/NEXT_HANDOFF.md` -> owning issue/PR.

For cross-agent protocol: `COORDINATION.md`.

For machine-readable research state: `research/RESEARCH_STATE.json`.

For historical context: dated audits/handoffs only when needed.
