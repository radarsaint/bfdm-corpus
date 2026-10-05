# Research substrate audit — current main addendum

This is not the PR #29 snapshot. That snapshot remains [RESEARCH_SUBSTRATE_AUDIT_2026-10-05.md](RESEARCH_SUBSTRATE_AUDIT_2026-10-05.md), written against `ingest/drive-history-v1` at `ffd4ec2c`. This addendum is the same questions rerun against canonical main after PR #25 and PR #30, plus the tooling ported from PR #29.

The snapshot's blanket `NOT_READY` is not the current research policy.

## Verdict

| Scope | Status |
| --- | --- |
| Broad BFDM judgment claims | `NOT_READY` |
| Bounded live-judgment research | `READY_WITH_SCOPE_LIMITS` |
| Creative-method / worldbuilding research | `READY_WITH_SOURCE_LIMITS` |

Broad claims are not ready because S3 and S4 are one Roanoke-lineage multi-DM format, and the named design files below are still outside the corpus.

Bounded live-judgment research may continue on source-traceable S3/S4 cases if that lineage limit and the missing evidence stay written next to the claim. That is Phase 2A. Its draft is PR #28. This addendum does not edit it.

Creative-method research may use design artifacts that have no live-play edge. Earthfall, Bastion/Redoubt, and At War's End can support design claims now. Those claims are not evidence the material was run. No Phase 2B research artifact has landed.

## What the labels guarantee

`SOURCE_RESEARCH_READY` means the source or family can be oriented: what it is, where it is placed or that placement is unknown, its stage or that the stage is unknown, and whether live use has been tied to a message or channel. It does not mean the research has been done.

`LONGITUDINAL_RESEARCH_READY` currently establishes at least one qualifying trajectory edge. It does not establish a complete longitudinal chain. Seven families still carry that label. Sampling them as finished histories is the mistake the snapshot identified.

`REVISION_CONTEXT_FOR_SOURCE_FAMILY` is visible from `query_source_history.py` as `revision_context`. It is not rewritten as `REVISES` or `SUPERSEDES`. The Season 5 changelog still has no before/after edge, so its family stays a longitudinal gap. That is intentional.

`live_contact` is this source's own live edge. `family_live_contact` is another member's edge. They do not overlap. The crafting dev doc `BCS-000077` has no live edge of its own. The public doc `BCS-000078` does.

## Week 5 map

`BCS-000053` no longer asks `referenced_source_absent` for the map. The map is the companion `BCS-000130`. The JPEG has no text layer, and room names are not invented. The remaining archive question on that sheet is `week_4_cast_list_absent`. Live use of the week sheet is still not established.

## Regenerated counts

Archive-gap ledger, 36 rows, regenerated from the explicit ledger rather than by re-opening Drive:

| Status | Rows |
| --- | --- |
| `MISSING_KNOWN_SOURCE` | 21 |
| `POSSIBLE_CANDIDATE_MATCH` | 12 |
| `RESOLVED` | 1 (week 5 map) |
| `EXTERNAL_OR_UNAVAILABLE` | 1 |
| `AMBIGUOUS_REFERENCE` | 1 |

The high-cost missing queue is unchanged: Season 4 Master Timeline, Season 5 style guide, Season 5 Dungeon Master's guide, player race edits, The Rowing Oak and its guide, the 2020 house-rules release, Ferrytown schedule, elevator gauntlet, Hampstead, the Almanac, and Season 5 framing material. 259 revision bodies are still unfetched. This queue does not block bounded research. It blocks treating the present containers as the whole record.

Candidate actions, still 132 rows marked `UNREVIEWED_CANDIDATE`, labeled from the existing first-pass notes and not re-read here: 28 `HIGH_PRIORITY_INGEST`, 42 `LIKELY_FAMILY_MEMBER`, 20 `CONTEXT_ONLY`, 10 `LIKELY_DUPLICATE_OR_VERSION`, 10 `LOW_RESEARCH_VALUE`, 5 `UNRELATED`, 17 `NEEDS_MANUAL_REVIEW`.

Integration check: 1 catalog row without a container, 1 unreadable body (`BCS-000022`, blank at the source), 259 unfetched revision bodies.

## Discord zero

`zero_match_means_absence` means the phrase is absent from the exhaustively searched Discord projection. It does not mean a Drive document does not exist. The Season 4 Master Timeline was posted as a bare URL in messages `748279131455881360` and `752645676260917248`. The title is not in the message text. Retrieval semantics stay with PR #27. This branch does not change them.
