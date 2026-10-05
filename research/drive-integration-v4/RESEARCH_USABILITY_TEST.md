# Source relationship pilot — research usability test

## Pilot families

- Roanoke S3 crafting system: BCS-000077 through BCS-000080.
- At War's End draft lineage: BCS-000060 through BCS-000063.
- Season 5 Drive-to-publication bridge: BCS-000113, BCS-000114, and BCS-000110.

## Questions and results

1. **What campaign does this source belong to?**
   Query `BELONGS_TO_PROJECT`. Crafting dev/public/working sources resolve to `roanoke-s3`. BCS-000080 deliberately has no exact-project relation because current evidence establishes earlier Roanoke crafting lineage but not an exact season.

2. **What production stage does it represent?**
   Query `HAS_PRODUCTION_PHASE`. Dev/working crafting is `system-development`; public crafting is `public-player-facing-publication`; the At War's End first draft is `preproduction`; the S5 changelog is `publication-revision`.

3. **What other sources are versions or companions?**
   Query `VERSION_FAMILY_WITH`, `EARLIER_FAMILY_MEMBER_THAN`, `EARLIER_DRAFT_THAN`, and `DEV_PUBLIC_PAIR_WITH`.

4. **Is there corresponding live-play evidence?**
   BCS-000078 has a STRONG `IMPLEMENTED_IN` relation into the S3 Discord projection. At War's End intentionally has no live relation because live delivery is not established.

5. **Was there a later public/player-facing version?**
   BCS-000077 links to BCS-000078 as a dev/public pair. BCS-000114 links to published BCS-000110 with `PUBLISHED_AS`.

6. **Can a researcher traverse prep → play → outcome where evidence exists?**
   For S3 crafting, development/public source → exact S3 project → publication phase → live Discord message cluster is now traversable. No outcome edge is asserted yet because the pilot has not established a bounded later outcome source.

7. **Can uncertainty remain visible?**
   Yes. BCS-000080 has no forced season assignment. The live crafting link is STRONG rather than CONFIRMED because the Discord evidence establishes use of the Roanoke system and matching mechanics but does not name the Drive document.

## Result

The pilot answers project, stage, family/version, publication, and live-evidence questions through explicit machine-readable edges rather than filenames. It also demonstrates omission as the correct representation of unknown relationships.
