# Machine-Readable Project and Identity Registry

This directory turns the human-readable chronology and identity notes into structured records.

It is an index over evidence, not a replacement for evidence.

## Files

- `projects.jsonl` — campaigns, experiments, creative projects, and product projects.
- `project_relations.jsonl` — explicit relationships between project records.
- `people.jsonl` — canonical people.
- `identities.jsonl` — platform/account/alias assertions scoped by server/project/date.
- `discord_servers.jsonl` — harvested Discord server identities and project links.
- `project.schema.json` — project-record schema.
- `identity.schema.json` — identity-assertion schema.
- `validate_registry.py` — structural/reference validator.

## Registry rule

A registry field is a structured claim and must carry uncertainty honestly.

Do not convert:
- a document creation date into a live campaign start;
- a general Roanoke player-scale retrospective into a season-specific count;
- a display-name match into a person identity;
- a sequence-number inference into a missing formal title.

Unknown values remain null/UNKNOWN and are filled only when evidence supports them.

## Identity rule

Brendon's names vary between seasons.

The registry therefore resolves a person through scoped identity assertions rather than global string matching.

For Discord, prefer:
- immutable account/user ID;
- server ID;
- observed username/display name;
- observed or harvested date window.

A confirmed alias can expand retrieval, but a nickname alone does not authorize attribution in a new server.

## Update ownership

### Work GPT

When Drive/Project ingestion establishes:
- a new project;
- planning/date anchors;
- source-family relationships;
- Drive revision identity metadata;

update these registries conservatively.

### Grok / Discord harvesting

When a new server is harvested:
- add/update `discord_servers.jsonl`;
- link it to a project only when supported;
- add account identity assertions from immutable Discord IDs;
- do not assume the S3 account/name mapping applies to another server without checking.

### Research

Research may refine:
- live windows;
- format/scale;
- project relationships;
- uncertainty status;

but must preserve support references and avoid replacing source evidence with registry prose.
