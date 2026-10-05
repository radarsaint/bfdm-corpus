# Historical source relationship model v1

## Purpose

This registry connects preserved BCS source containers to historical context needed for research without turning the archive into Kit's runtime or a speculative semantic graph.

Canonical relationship storage is `registry/source_relations.jsonl`. Source `metadata.json` continues to own source identity, native locators, representations, capture state, authorship status, and document-family hints. `registry/project_relations.jsonl` remains project-to-project only.

## Minimal edge model

Each relation has one BCS source, one typed target, a relation name, confidence, a short evidentiary basis, and support references.

Supported target kinds are SOURCE, PROJECT, PRODUCTION_PHASE, DISCORD_MESSAGE, DISCORD_SERVER, SOURCE_FAMILY, and EXTERNAL.

Initial relation vocabulary:
- BELONGS_TO_PROJECT / RELATES_TO_PROJECT
- HAS_PRODUCTION_PHASE
- VERSION_FAMILY_WITH / EARLIER_FAMILY_MEMBER_THAN / EARLIER_DRAFT_THAN
- DEV_PUBLIC_PAIR_WITH / PUBLISHED_AS
- REVISES / SUPERSEDES / RESPONDS_TO / COMPANION_TO
- IMPLEMENTED_IN / DISCUSSED_IN / ALTERED_DURING_PLAY / OUTCOME_DOCUMENTED_IN

The vocabulary is deliberately not schema-enumerated. New archival relationships may be added when evidence requires them, but they should be documented before broad use.

## Production phases

The pilot uses only phases supported by evidence:
- system-development
- preproduction
- public-player-facing-publication
- publication-revision

Unknown is represented by no phase relation, not a guessed value.

## Confidence

- CONFIRMED: directly established by source identity, explicit labels, or canonical registry evidence.
- STRONG: multiple pieces of evidence support the relationship but a direct identity statement is absent.
- TENTATIVE: plausible and useful to preserve for review, but not established.
- UNRESOLVED: used only when preserving the unresolved relationship itself is useful.

## Why a separate registry

Project membership, production stage, version/publication links, and live-evidence links are edges across archival objects. Storing them only inside individual metadata files would make traversal unnecessarily difficult. Duplicating them into project_relations would mix project-to-project and source-level semantics.

This registry is independent of Kit and does not create BCE/BCR claims automatically.

## Concept/entity layer

No general source-to-NPC/mechanic/faction knowledge graph is added in this pass. Stable concept/entity references should be introduced only when episode/case construction demonstrates a concrete retrieval need.
