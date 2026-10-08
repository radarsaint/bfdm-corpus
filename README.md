# BFDM Corpus

> **Governing invariant:** `bfdm-corpus` is not primarily a training dataset. It is the durable research archive of Brendon's D&D creative history. **Kit is one consumer of it.**

Canonical corpus and research repository for Brendon's D&D creative work and the live-play context around it.

Repository visibility may change during active work; visibility is not part of corpus authority.

This repository must remain useful even if Kit's architecture changes completely or Kit is replaced. Training, retrieval, prompting, evaluation, and voice distillation are downstream uses of the archive—not the archive's organizing purpose.

It preserves and makes researchable:

- campaign planning and operations;
- Discord activity and attachments;
- Google Drive/project documents;
- revisions and comments;
- homebrew races, classes, subclasses, items, and systems;
- worldbuilding and lore;
- writing and abandoned experiments;
- playtests, corrections, and postmortems;
- derived research that remains traceable to source evidence.

## Start here

- **Project-wide GPT bootstrap:** `radarsaint/dnd-solo/PROJECT_BOOTSTRAP.md` on the paired coordination branch until it lands on `main`. Use it for durable project understanding, agent/tool identity, current-state routing, and context continuity.
- [PROJECT_CONTROL.md](PROJECT_CONTROL.md) — short current cross-project/research orientation.
- [COORDINATION.md](COORDINATION.md) — shared truth, ownership, staleness, and handoff rules for `bfdm-corpus` + `dnd-solo`.
- [CORPUS_CHARTER.md](CORPUS_CHARTER.md) — project boundary and research layers.
- [research/NEXT_HANDOFF.md](research/NEXT_HANDOFF.md) — current operational state, active PRs, and immediate next work.
- [research/STATUS.md](research/STATUS.md) — current source and research status.
- [research/SOURCE_COVERAGE.md](research/SOURCE_COVERAGE.md) — what source families are represented and what gaps remain.
- [research/INDEX.md](research/INDEX.md) — research artifacts by stage.
- [REPO_HYGIENE.md](REPO_HYGIENE.md) — branch/artifact/duplication rules.
- [INGESTION_CONTRACT.md](INGESTION_CONTRACT.md) — Drive/Project ingestion contract.

## Current storage

- `campaigns/` — campaign-level registry/metadata and cross-links; canonical document bodies live under `sources/` or `context/`.
- `discord/` — canonical SQLite Discord harvests. See [discord/SCHEMA.md](discord/SCHEMA.md).
- `sources/` — canonical human-readable non-Discord BCS source containers.
- `context/` — context-only BCS source containers.
- `indexes/` — rebuildable local indexes such as `documents.sqlite`.
- `model-index/` — rebuildable, non-LFS model-facing Discord projections and deterministic term-routing indexes. See [MODEL_RETRIEVAL.md](MODEL_RETRIEVAL.md).
- `registry/` — machine-readable project/campaign, Discord-server, person, identity, and source-relationship mappings.
- `evidence/` — BCS/BCE/BCR source/evidence registry and portable evidence snapshots.
- `research/` — derived analysis, methodology, evaluation records, readiness reports, and source leads. Research is not source truth.

`.sqlite` databases and Discord attachment files are stored with Git LFS. Canonical Discord SQLite remains source truth; model-facing JSONL is a downstream retrieval layer.

## Current program position

Stage 1 source accessibility/integration is substantially broader and hardened on `main`: model-facing Discord retrieval works, PR #25, PR #31, and PR #36 are merged, and canonical source containers run through BCS-000172. The reconciled additions include research-critical historical Drive sources plus partial Earthfall and Saturday D&D DM-workbench Project histories. Remaining Drive candidates are a classified backlog. Donor PRs #32, #34, and #35 are closed without merge.

Stage 2 has two lanes and neither is complete. Phase 2A, live judgment, is the open draft PR #28. The next cross-format pass can use the newly canonical Earthfall and Saturday D&D workbench sources; that pass has not been done. Phase 2B, creative method and worldbuilding, may use design artifacts without treating them as proof the material was run. No Phase 2B result set has landed. The human-object index draft is PR #33 and has not been expanded across the reconciled corpus. Broad judgment claims are not ready.

Stage 3 precedent cards/runtime retrieval and Stage 4 cognitive architecture are intentionally later work. Do not skip ahead merely because the source substrate is now much stronger.

## Provenance

Maintain compatibility with the existing corpus IDs:

- `BCS-######` — source container;
- `BCE-######` — attributable Brendon evidence;
- `BCR-######` — supported relation.

A source may belong in this archive without being Brendon-authored or eligible to shape Kit.

## Canonical-repo rule

This is the canonical corpus repository.

Do not create a parallel Brendon-corpus repository. Reconcile older staging/donor material here while preserving stable IDs and provenance.
