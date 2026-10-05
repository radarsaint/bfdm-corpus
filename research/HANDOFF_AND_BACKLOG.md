# Research Handoff and Backlog

**Status date:** 2026-10-02  
**STATUS: SUPERSEDED**

**Current handoff:** `research/NEXT_HANDOFF.md`

This file is preserved as a dated historical handoff. It described the workstream split, PR #5 state, Drive-ingestion expectations, and preservation priorities as they existed on 2026-10-02.

Do **not** use the instructions below as current assignments. In particular:
- PR #5 has since been reviewed and merged;
- the historical Drive/source integration advanced substantially and PR #25 has since merged to `main`;
- the 51-source binary-transfer blocker described by later 2026-10-04 audits is no longer the current state;
- Phase 2 decision-contrast research has begun on draft PR #28;
- current operational truth is maintained in `research/NEXT_HANDOFF.md`.

---

## Historical snapshot follows

### Work streams

### Work GPT
Expected to resume:
- ingesting Google Drive documents and project files into the private `bfdm-corpus`;
- storing material in machine-searchable form (including SQLite/indexed form where appropriate);
- preserving human-readable forms;
- retaining IDs, timestamps, authorship, provenance, and revision relationships.

**Binding Work GPT contract:** `INGESTION_CONTRACT.md`

**Executable assignment:** `ingest/WORK_GPT_TASK.md`

Do not accept an ingestion PR that substitutes a different ID/dedup/layout/schema strategy without deliberate review.

### Grok
Expected to resume:
- lower-level Kit / GitHub/runtime work;
- harvesting additional Discord game servers into the corpus.

Remaining Discord servers still require Brendon to assign/provide access to Grok as needed.

### Research GPT
Current useful scope:
- research methodology;
- source-gap identification;
- organization of existing findings;
- cross-campaign research questions;
- evidence review;
- longitudinal / revision-aware analysis;
- synthesis only when source coverage supports it.

Avoid duplicating ingestion/runtime work unless a gap blocks research.

## Governing numbered cleanup sequence

The then-current cleanup sequence was authoritative in `research/NEXT_HANDOFF.md` at the time of this snapshot:

- Points 1–3: completed;
- Point 4: reconcile the 51-source legacy staging body into canonical `bfdm-corpus`;
- Point 5: deliberately review and integrate PR #5;
- Point 6: recover the later Area 6c verbatim human-test transcript;
- Point 7: archive-first invariant, completed and governing.

## Immediate preservation priorities

1. Migrate/reconcile earlier staged source containers.
2. Reconcile S3 staged containers while preserving BCS IDs.
3. Complete remaining Discord harvests.
4. Complete Drive/project ingestion with revisions/comments/provenance.
5. Refine machine-readable campaign registry as coverage improves.
6. Preserve mechanical/worldbuilding lineages.
7. Preserve early Roanoke revision family.

## Research backlog after coverage improves

Historical priorities included:
- cross-era DM judgment;
- negative-space/restraint;
- emergence and formalization;
- creative-method research;
- mechanical-design lineage;
- campaign-architecture research.

## Historical GitHub workspace

At the time of this snapshot:
- branch: `research/organize-current-work-v1`;
- draft PR: #5.

That PR state is historical and has been superseded by later merged work.
