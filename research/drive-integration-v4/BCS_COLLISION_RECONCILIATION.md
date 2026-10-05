# Drive donor reconciliation — collision and port plan

Branch: `ingest/drive-integration-v4`
Base main at branch creation: `0788f3d45b784a4b52c6c4645932267ccafc53ff`
Donor: `ingest/drive-project-v3`

## Authority rule

Current `main` owns every BCS ID already merged there. The donor branch is an archival donor, not a merge target. Existing donor source containers, native Drive IDs, comments, revision metadata, bodies, and binary exports must survive reconciliation.

## Current collision boundary

At branch creation, current main's highest BCS is `BCS-000114`.

Donor `BCS-000069` through `BCS-000086` were explicitly reserved by current main for the active Drive work and remain available to keep their donor IDs.

Donor IDs that collide with canonical Season 5 IDs on main are renumbered deterministically:

| Donor ID | Donor title | Canonical new ID |
|---|---|---|
| BCS-000087 | Timeline disambiguation | BCS-000115 |
| BCS-000088 | RS3 Public docs copy editing. | BCS-000116 |
| BCS-000089 | Island games draft | BCS-000117 |
| BCS-000090 | Golden Dawn quest arc | BCS-000118 |
| BCS-000091 | The Halfwudgie Verbatim | BCS-000119 |
| BCS-000092 | The Urucokra Verbatim | BCS-000120 |
| BCS-000093 | The Jackalope Verbatim | BCS-000121 |

Before scaling the port, refresh main's maximum BCS. If main allocates 115–121 first, regenerate this mapping rather than altering any merged canonical ID.

Every renumbered container must update directory path, metadata corpus_id, evidence/catalog row, discovery-ledger corpus_id, portable_snapshot paths, internal BCS references, source-relation refs, and any copied index/database row. Native Drive IDs and source content do not change.

## Donor material to preserve

The donor contains:
1. canonical legacy BCS identities already present in main whose source bodies/originals/comments/assets are still absent from canonical source directories;
2. newly admitted Drive sources and their comments/revision metadata/source bodies, including reserved 069–086 and conflicting 087–093;
3. the Drive discovery ledger and reconciliation work needed to prove provenance.

These are archival artifacts. They must not be replaced by summaries.

## Pilot transport finding

The exact source/body/comment/revision/original Git blob SHAs on the donor branch can be enumerated. Git tree creation accepts the current main commit as a base tree-ish, so exact donor blobs can be assembled into a new tree without re-uploading their bytes. The connector's ref-update action is currently rejecting otherwise valid arguments, so the low-level binary transplant is documented but not yet attached to this branch. Ordinary text changes are being committed through the contents API.

Do not treat this connector limitation as permission to abandon the donor binaries.
