# Derived research integrity

**Status:** first-tranche staging only. No corpus-wide semantic certification has been performed.

**Audit baseline:** canonical `main` at `65513f294e72a3eb961d5699c21ddc1f14ceef2c`.  
**Audit branch:** `audit/derived-research-integrity-2026-10-05`.  
**First tranche:** `research/roanoke-s3/decision-cases-v1.md` and `.jsonl`.

This layer exists because a citation can resolve syntactically while failing to reconstruct the evidence chain for the proposition that cites it. Source/substrate validity is therefore not semantic verification.

## Contract

The canonical audit state is `audit_ledger.jsonl`. It is bookkeeping about derived research, not a historical provenance namespace. Audit identifiers use the derived identifier they inspect, for example `audit:BDC-S3-004:intervention`. Historical proof continues to use BCS, BCE, BCR, native Discord IDs, Drive IDs, and existing identity/project IDs.

An audit judgment is a **versioned transaction between one proposition and the evidence representations actually reviewed**. Each ledger record binds:

- artifact path, derived case/section/field, exact proposition text, normalized SHA-256 digest, and repository state;
- historical evidence/native references;
- source representation path and content digest;
- bounded excerpt coordinates and excerpt digest when line-addressed evidence is used;
- canonical Discord database identity plus projection/message identity when Discord evidence is used;
- dependency identities such as authorship/identity mappings;
- semantic status, evidence confidence, claim scope, flags, and packet state.

Line numbers are convenience coordinates, not evidence identity.

## Fail closed

The safe defaults are:

- new/unreviewed proposition -> `UNVERIFIED`;
- materially changed proposition -> `REQUIRES_REVALIDATION`;
- materially changed reviewed evidence -> `REQUIRES_REVALIDATION`;
- missing evidence -> `SOURCE_UNAVAILABLE`;
- unresolved attribution -> `ATTRIBUTION_UNRESOLVED`.

The validator is deterministic. It can establish existence, versions, hashes, locator/excerpt drift, identity mismatches, representation divergence, dependency breakage, and stale review state. It **cannot** certify motive, meaning, causality, expert principle, transfer, or generalization.

Semantic-review vocabulary prepared for this tranche:

`VERIFIED_DIRECT`, `VERIFIED_STRONG_RECONSTRUCTION`, `PARTIALLY_SUPPORTED`, `LOCATOR_BROKEN_SUPPORT_RECOVERED`, `LOCATOR_BROKEN_CLAIM_UNSUPPORTED`, `ATTRIBUTION_UNRESOLVED`, `CHRONOLOGY_UNRESOLVED`, `CAUSALITY_OVERCLAIMED`, `SCOPE_OVERCLAIMED`, `CONTEXT_CHANGES_INTERPRETATION`, `CONTRADICTED`, `SOURCE_UNAVAILABLE`, `DERIVED_ONLY_NO_PRIMARY_CHAIN`, `REQUIRES_REVALIDATION`, and `UNVERIFIED`.

Evidence confidence and claim scope remain separate. The audit does not translate legacy labels such as `high` into a stronger methodology status without review.

## Bounded source-version forensics

For a failed locator, inspect only the obvious lineage:

1. current Git history and prior path history;
2. the derived artifact's own Git/PR lineage;
3. known legacy staging;
4. explicitly related donor/reconciliation branches;
5. stored source metadata and known preserved exports/revisions.

Then stop. `ORIGINAL_REPRESENTATION_UNAVAILABLE` is a valid result. Do not invent a historical rendering or search unrelated branches indefinitely.

Mechanical locator-forensics outcomes are:

`CURRENTLY_VALID`, `MOVED_EXACT_EVIDENCE`, `REPRESENTATION_DRIFT_RECOVERED`, `WRONG_ORIGINAL_LOCATOR`, `WRONG_SOURCE`, `ORIGINAL_REPRESENTATION_UNAVAILABLE`, `SUPPORT_NOT_FOUND`, and `UNRESOLVED`.

These labels describe the evidence-link forensics, not semantic truth of the derived proposition.

## First regression: BDC-S3-004

The disputed prep locators `BCS-000045:L1573-L1579` and `BCS-000045:L4420-L4422` first appear in commit `22c1b645db850fc4934680c569ba6adc9b1b0bb8` (PR #2, 2026-10-02).

That PR changed only the v1 Markdown and JSONL derived artifacts. Its base, first commit, and final head contain no preserved BCS-000045 source representation. The exact representation against which those line numbers were originally selected therefore cannot be reconstructed from the bounded Git lineage.

The later preserved Library/Drive snapshot is stable across legacy staging, the Drive donor branch, and current canonical source:

- normalized `source.md`: SHA-256 `adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166`, 4,476 lines;
- export snapshot `original/source.txt`: SHA-256 `9ba280ea54b9c13312db5ced664f3bcff48b3c3b8640568fec2f42ea7bf4edcb`, 4,469 lines.

In the normalized representation, 1573-1579 describe what Roanoke is and 4420-4422 are Brendon's creative-team bio. In the export snapshot, the same coordinates are settings and the Rob Hubbard bio. Neither is limb-loss/mechanical-resolution prep evidence. Searches of both preserved representations find no relevant limb-loss/handwave prep passage.

Therefore the bounded forensic result is:

- original representation: `ORIGINAL_REPRESENTATION_UNAVAILABLE`;
- current cited support: `SUPPORT_NOT_FOUND`;
- representation drift: **not established**.

The live Discord message itself is reconstructable from the canonical S3 harvest projection and carries Brendon's confirmed immutable author ID. Semantic review must decide how much of the case survives without the claimed prep link.

## Markdown and JSONL

The first tranche currently contains the same 20 case IDs and the same case-field values in Markdown and JSONL. Neither file declares itself generated from the other; treat them as manually synchronized equivalent representations. Divergence is a coherence failure, not permission to silently choose one.

This pass does not redesign research serialization.

## Review packets

`scripts/build_research_review_packet.py` builds a bounded UTF-8 view from canonical source/evidence, the synchronized tranche, and audit state. Packets are generated views, not historical truth. A packet records repository state, proposition/evidence dependency digests, and its own digest. Verdict integration is rejected when the packet state is stale.

Generated packets may be deleted after the audit and rebuilt from canonical state.

## Automatic guard

`.github/workflows/research-integrity.yml` is the automatic first-tranche gate. It runs the validator and adversarial tests when the audited artifacts, audit ledger, relevant evidence/source representations, identity dependencies, projection tooling/state, or integrity tooling change.

This is deliberately narrow. It does not claim the whole corpus is audited.

## Relationship to Kit

BFDM remains a research system. An audited finding does not automatically become Kit behavior. This layer only makes later curation able to ask what proposition/version was reviewed, against what evidence/version, with what confidence/scope/status, and whether that judgment is stale.
