# Historical Source Relationship Model v1

## Decision

Use the existing source-container metadata as the canonical home for source placement and historical source links. Do not create a competing source-relations registry.

This reuses mechanisms already present in the corpus:

- `document_family_id` remains the non-chronological family/grouping key.
- source `metadata.json` remains the canonical human-inspectable record for source-specific provenance.
- `source_links` already exists in the non-Discord document SQLite schema and in current Season 5 metadata.
- `registry/project_relations.jsonl` remains project-to-project only.
- SQLite remains a derived/searchable representation, not source truth.

## Canonical fields

### historical_context.project_links

Explicit source-to-project placement. A source may use:

- `BELONGS_TO_PROJECT`
- `RELATES_TO_PROJECT`
- `CROSS_PROJECT`

Every asserted placement carries confidence, basis, and support references. Unknown project placement stays unknown.

### historical_context.production_stages

Zero or more source-backed stages:

- `RESEARCH_INSPIRATION`
- `BRAINSTORMING`
- `PREPRODUCTION`
- `SYSTEM_DEVELOPMENT`
- `CAMPAIGN_OPERATIONS`
- `LIVE_USE_ARTIFACT`
- `PUBLIC_PLAYER_FACING_PUBLICATION`
- `POSTMORTEM_CORRECTION`
- `LATER_RETROSPECTIVE`

Stages are not inferred merely from file names or dates.

### document_family_id

Retained for sources that are clearly members of one technical/design family. Family membership does not itself claim ordering, supersession, or direct derivation.

### source_links

Cross-source or source-to-live-evidence relationships. v1 supports a deliberately small relation set: version/predecessor/successor, revises/supersedes, publication/dev-public/derived/copy/response/companion, and live-evidence links such as implemented/discussed/altered/abandoned/outcome-documented.

A link has one canonical record on the source where the assertion is most natural. Reciprocal duplicate edges are not required; traversal tools should query both outgoing and incoming links.

Each link must carry:

- target kind;
- target BCS ID or stable external locator;
- confidence;
- evidence basis;
- support references.

## Live Discord locators

When a stable Discord message or channel ID is available, use immutable native IDs, for example:

`discord://636012145204527125/channel/739240413269065890`

Support refs may point to individual messages:

`discord:636012145204527125:739852380782198814`

Do not treat a server-level archive as proof that a prepared rule was used in play. Use a live-evidence relationship only when message-level/channel-level evidence supports it.

## Concept/entity layer

Do not add a general NPC/faction/location/mechanic ontology in this pass. Stable concepts should remain in source text and existing research until a demonstrated episode/case construction need requires identifiers. Premature entity extraction would turn the source layer into speculative semantic research.

## Uncertainty rule

Relationship metadata records what is supported, including uncertainty. It does not resolve ambiguity for convenience.

If exact campaign membership is unproven, use `RELATES_TO_PROJECT` or omit the project link. If live implementation is unproven, do not use `IMPLEMENTED_IN`.

## Query model

Canonical truth is the source metadata. The existing document SQLite `source_links` table is a derived index and can be rebuilt/extended when the broader Drive reconciliation is scaled. This pilot does not make the database the only copy of relationship provenance.
