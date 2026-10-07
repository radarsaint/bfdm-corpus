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

## Active draft state that materially affects trust

Open draft PRs are not canonical main, but some are important current work:

- **#38 — forensic derived-research integrity audit.** Active as of 2026-10-07. It tests whether cited derived claims actually reconstruct from primary/source evidence. Treat prior polished derived research as unverified unless the underlying evidence has been semantically checked at the claimed scope.
- **#28 — Phase 2 decision contrast families.** Draft live-judgment research; not doctrine and not merged.
- **#33 — human-object index prototype.** Draft projection, not source truth and not complete.
- **#37 — strategic BFDM / Kit planning handoff.** Project direction/planning, not historical BFDM evidence and not canonical main.

Any worker relying on one of these must name the PR and branch explicitly.

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

## Product relationship

BFDM research exists to improve Kit's craft and understanding, but BFDM is not the product.

**Kit is the product. The total experience is the acceptance layer.**

Research should improve what Kit can recognize, understand, decide, create, remember, or avoid. A research artifact succeeding on its own terms does not prove that Kit's player experience improved.

## Current temporary parallel work

Another GPT is already doing mechanical corpus preparation. Do not duplicate ingestion, normalization, indexing, source-container cleanup, or retrieval-layer preparation.

Temporary audits:

- GPT 1 — project truth / contradiction audit;
- GPT 2 — Kit quality / failure-localization audit;
- GPT 3 — BFDM research-readiness / ChatGPT Work queue;
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
