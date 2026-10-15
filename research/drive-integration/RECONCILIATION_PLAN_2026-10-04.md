# Drive v3 reconciliation inventory and BCS collision plan — 2026-10-04

## Branch posture

`ingest/drive-project-v3` is a donor/source branch, not a merge candidate. It is diverged from current `main`; its archival source artifacts must be selectively reconciled onto a fresh branch rooted at current main.

Fresh integration branch: `ingest/drive-relations-reconcile-v1`.

## Valuable donor work that must survive

The donor branch contains archival source material, not merely analysis:

- BCS-000001–BCS-000016: Empire City source containers, including normalized bodies, Google-native export snapshots, and substantial revision/comment captures on several sources.
- BCS-000017–BCS-000053: legacy Roanoke source-body reconciliation, including originals, human-readable bodies, comments, and embedded assets where present.
- BCS-000054–BCS-000055: Earthfall source containers.
- BCS-000056–BCS-000058: Bastion/Redoubt source containers.
- BCS-000059: Exploration Impossible context container and native comment context.
- BCS-000060–BCS-000067: At War's End source/draft lineage containers.
- BCS-000069–BCS-000093: newly admitted Drive sources, including directories, planning, crafting, bestiary/cartography, public lore, and other S3/Empire City material.
- Drive discovery ledger: 158 candidates at donor review state (23 `INGESTED`, 1 `INGESTED_PARTIAL`, 134 `UNREVIEWED_CANDIDATE`).
- Legacy reconciliation report and Drive discovery documentation.

The port must preserve source bodies, native Drive IDs, original/export snapshots, comments, revision metadata/bodies already captured, checksums/hashes where recorded or reconstructed, document-family IDs, and provenance. Do not replace these containers with summaries.

## Canonical-ID rule

Current main is authoritative for IDs already merged. IDs BCS-000069–BCS-000086 were intentionally left reserved for the active Drive work and can retain their donor allocation.

Current main has independently allocated Season 5 sources at BCS-000087–BCS-000114.

Only the unmerged donor records that collide with those canonical IDs are renumbered.

## Deterministic mapping

| Donor ID | Donor title | Canonical reconciled ID |
| --- | --- | --- |
| BCS-000087 | Timeline disambiguation | BCS-000115 |
| BCS-000088 | RS3 Public docs copy editing. | BCS-000116 |
| BCS-000089 | Island games draft | BCS-000117 |
| BCS-000090 | Golden Dawn quest arc | BCS-000118 |
| BCS-000091 | The Halfwudgie Verbatim | BCS-000119 |
| BCS-000092 | The Urucokra Verbatim | BCS-000120 |
| BCS-000093 | The Jackalope Verbatim | BCS-000121 |

Every future port of these seven records must update container paths, `corpus_id`, catalog entries, source links, document-family references that contain BCS IDs, SQLite rows, reports, and any research/support refs that refer to the old donor BCS number. Native Drive IDs and source bytes do not change.

## Pilot boundary

The first port is BCS-000077–BCS-000080, the Roanoke crafting-system family. These IDs do not collide and therefore retain their donor BCS IDs.

Scaling the rest of the donor branch waits until this pilot proves:

1. canonical metadata can be reconciled to current-main contracts;
2. binary/source representations survive intact;
3. comments and revision metadata survive intact;
4. relationship metadata validates;
5. live evidence can be linked without inventing use.
