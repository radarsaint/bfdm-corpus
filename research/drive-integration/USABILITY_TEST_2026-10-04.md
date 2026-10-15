# Drive Relationship Pilot — Research Usability Test

**Date:** 2026-10-04  
**Branch:** `ingest/drive-relations-reconcile-v1`

This test asks whether a researcher who did not reconstruct the history manually from filenames can traverse the pilot sources using explicit source metadata.

## Test sources

### Roanoke crafting family

- `BCS-000077` — Crafting with Class (Dev Doc)
- `BCS-000078` — Crafting with Class (Public Doc)
- `BCS-000079` — Brendon's copy of crafting.
- `BCS-000080` — Crafting, another attempt

### Season 5 publication bridge

- `BCS-000113` — S5 Site Changelog / To Change
- `BCS-000114` — Way of Gun Fu Drive PDF
- `BCS-000110` — published Season 5 Arcanian Monk Options page

## 1. What campaign does this source belong to?

**Pass, with uncertainty preserved.**

`BCS-000077`, `000078`, and `000079` explicitly resolve to `roanoke-s3`. The strongest case is `000079`, whose body says it outlines a crafting system for Roanoke Season 3.

`BCS-000080` deliberately has no `BELONGS_TO_PROJECT` assertion. It is clearly Roanoke crafting-system development and predates the S3 Crafting with Class documents, but the source does not establish exact season membership.

`BCS-000113` and `000114` resolve to `roanoke-s5-legends`.

## 2. What production stage does it represent?

**Pass.**

The crafting development sources expose `PREPRODUCTION` and/or `SYSTEM_DEVELOPMENT` where supported. The public crafting document exposes `PUBLIC_PLAYER_FACING_PUBLICATION`.

The Season 5 changelog and Drive subclass source expose `SYSTEM_DEVELOPMENT`; the public Google Site remains a separately preserved publication source.

## 3. What other sources are versions or companions?

**Pass without flattening drafts.**

`document_family_id: roanoke-crafting-system` groups the four crafting sources without claiming a false linear lineage.

Explicit links add only supported semantics:

- `BCS-000077 DEV_PUBLIC_PAIR -> BCS-000078`
- `BCS-000079 COMPANION_TO -> BCS-000077`
- `BCS-000080 PREDECESSOR_OF -> BCS-000077`

For Season 5, `BCS-000114` retains the established Way of Gun Fu version-family link and adds `PUBLISHED_AS -> BCS-000110`.

## 4. Is there corresponding live-play evidence?

**Pass for the public S3 crafting rules; intentionally unresolved elsewhere.**

`BCS-000078` has a confirmed `IMPLEMENTED_IN` link to the S3 `crafting-questions` Discord channel:

`discord://636012145204527125/channel/739240413269065890`

Support messages include:

- `739852380782198814` — live clarification that a +1 weapon costs 1,000 gold and 2 labor, plus wages;
- `739852509048340532` — the one-time 1,000 gold merchant-shop investment;
- `740216263934083112` — aristocrat sponsorship and unsponsored merchant behavior.

These are specific mechanics present in the public Drive source, so this is stronger than server-level co-occurrence.

No live-use edge was manufactured for sources where equivalent evidence has not yet been reviewed.

## 5. Was there a later public/player-facing version?

**Pass.**

The crafting family exposes the dev/public relationship directly, and the public source is separately staged as player-facing publication.

The Way of Gun Fu Drive source links directly to the published Season 5 Monk source.

## 6. Can I traverse prep -> play -> outcome when evidence exists?

**Partial pass; the missing layer is visible instead of being guessed.**

For crafting, a researcher can traverse:

`BCS-000077 / BCS-000079` development  
→ `BCS-000078` public rules  
→ S3 live `crafting-questions` evidence.

The pilot does **not** yet assert a canonical `OUTCOME_DOCUMENTED_IN` edge for the longer-term economic/social result of the crafting system. The Discord archive contains candidate downstream evidence, but that is a research question rather than an ingestion fact and should be reviewed before encoding.

That visible stop is desirable: the relationship layer identifies exactly where later episode/case research still has work to do.

## 7. Can I see uncertainty when the relationship is not established?

**Pass.**

`BCS-000080` is the direct test. It is retained in the crafting family and marked as system development, while exact campaign/season membership remains explicitly unresolved.

The same rule applies to live use: publication or family membership alone does not create `IMPLEMENTED_IN`.

## Result

The pilot supports useful traversal without turning the source archive into a speculative knowledge graph.

A researcher can now answer project placement, production stage, family/version context, publication state, and—where message-level evidence exists—live implementation from machine-readable source metadata.

The next scaling step should port additional donor source containers using this pattern, then add only evidence-backed relationships. At War's End is a strong next family for draft-lineage testing because it does not require a live-play claim.
