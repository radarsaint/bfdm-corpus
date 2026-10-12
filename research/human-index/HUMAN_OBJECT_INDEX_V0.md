# BFDM Human-Object Index v0

**Status:** experimental substrate design  
**Branch:** `research/human-object-index-v0`  
**Purpose:** make the corpus navigable by the people, places, organizations, systems, events, items, creatures, and concepts Brendon actually remembers.

## Problem

The corpus is increasingly source-addressable: BCS ids, Drive ids, Discord message ids, document families, project ids, and revision edges.

That is necessary for provenance. It is not a sufficient human interface.

A human normally approaches this body of work through nouns and concepts:

- Daysong
- Sandigil / Gil
- R.O.D.
- Lamplighters
- Ferrytown
- Golden Dawn
- Fryvern
- crafting
- The Rowing Oak
- the World's Cornerstone

The archive should not require a researcher to know where those things are stored before asking about them.

## Design rule

> **Resolve the human thing first. Then traverse to the sources.**

This layer is a derived projection over source truth. It never replaces BCS/BCE/BCR provenance.

The index must support movement in both directions:

```text
high-level concept
    -> literal people / places / systems / events
    -> source-backed assertions and relationships
    -> exact source evidence

exact source
    -> human objects mentioned or established there
    -> relationships
    -> broader concepts where those concepts are explicitly curated
```

## Scope

The index is corpus-wide from the beginning.

Coverage may be uneven, but no campaign is the default mental universe. Empire City and Roanoke S3 are not privileged merely because their current retrieval substrate is dense.

Expected source domains include, among others:

- early Roanoke
- Roanoke S2/S3/S4/S5
- Empire City
- Earthfall
- Saturday D&D
- Bastion/Redoubt
- At War's End
- experimental events
- homebrew mechanics
- Kit/project-development material where it describes human-meaningful objects

## Files

Prototype registry:

- `registry/human_objects.jsonl` — stable object identity
- `registry/human_object_assertions.jsonl` — provenance-backed facts/unknowns/conflicts
- `registry/human_object_relations.jsonl` — typed links between objects or projects
- `scripts/query_human_object.py` — human-facing resolver/traversal

These files are projections. Source material remains authoritative.

## Object types

v0 allows these primary types:

- `CHARACTER`
- `PERSON`
- `PLACE`
- `ORGANIZATION`
- `FACTION`
- `ITEM`
- `ARTIFACT`
- `CREATURE`
- `SPECIES`
- `MECHANIC`
- `SYSTEM`
- `EVENT`
- `ARC`
- `CONCEPT`
- `ENTITY`

A primary type is for routing. `facets` may preserve important secondary identities without forcing false exclusivity.

Example: R.O.D. can be `ENTITY` with facets `SYSTEM_PERSONA` and `BROADCAST_INTELLIGENCE`.

## Object identity

An object record contains:

```json
{
  "object_id": "hobj:earthfall:rod",
  "canonical_name": "R.O.D.",
  "object_type": "ENTITY",
  "facets": ["SYSTEM_PERSONA", "BROADCAST_INTELLIGENCE"],
  "project_ids": ["earthfall"],
  "aliases": [],
  "source_refs": ["BCS-000054", "BCS-000055"],
  "status": "ESTABLISHED"
}
```

The object id is a registry identity, not historical evidence.

Aliases must retain scope and provenance when ambiguity is possible.

A matching string is not sufficient to collapse two objects.

## Assertions

Literal facts belong in assertion records rather than being buried in prose summaries.

Each assertion records:

- object
- predicate
- typed value
- epistemic status
- confidence
- support refs
- basis
- optional conflict set

Allowed epistemic states:

- `KNOWN`
- `UNKNOWN`
- `CONFLICTING`
- `INFERRED`

`INFERRED` should be uncommon in the literal index and must carry a basis. Research interpretation belongs elsewhere.

Example:

```json
{
  "object_id": "hobj:bastion-redoubt:aric-altovolo",
  "predicate": "role",
  "value": {"kind": "TEXT", "text": "head of patrol"},
  "epistemic_status": "KNOWN",
  "confidence": "CONFIRMED",
  "support_refs": ["BCS-000056"]
}
```

Unknowns are first-class. They prevent generation systems from silently turning absence into canon.

## Relationships

Relationships connect human objects to one another or to registered projects.

Examples:

- `MEMBER_OF`
- `OPERATES_IN`
- `LOCATED_IN`
- `FOUNDED_BY`
- `OPPOSES`
- `CREATED_BY`
- `INSCRIBES`
- `ERODES`
- `USES_SYSTEM`
- `ASSOCIATED_WITH`
- `APPEARS_IN_PROJECT`
- `GROUNDS_CONCEPT`

A relation must have support refs and a basis.

This is not permission to infer an RPG knowledge graph from co-occurrence.

## High-level concepts

High-level discussion should remain grounded in literal referents.

A derived research concept such as "institutions as campaign machinery" may later be represented as a `CONCEPT` object, but it must be visibly research-layer material and link downward to literal objects such as organizations, player roles, mechanics, locations, and source-backed examples.

The desired interaction is:

> "How do institutions function in these campaigns?"

followed by a grounded set of actual institutions and their source-backed roles, not a free-floating personality summary.

Concept objects must never silently become source canon.

## Established-character rendering

The human-object index is the canonical starting point for an eventual Established Character Render workflow.

Before generating an established character, Kit should resolve the character object and build an identity packet from assertions and canonical assets.

Identity information and style information remain separate.

Identity may include:

- species/race
- sex/gender when known
- build/anatomy
- role/class/job
- clothing/equipment
- visual markers
- behavioral markers relevant to depiction
- current scene facts
- canonical art references
- explicit unknowns
- conflicts

Style references may influence rendering, composition, finish, color handling, and layout.

Style references must not supply character identity facts.

## Human-use acceptance tests

The index succeeds only if ordinary remembered-language queries work.

Examples:

```text
query_human_object.py "R.O.D."
query_human_object.py "rod"
query_human_object.py "Lamplighters"
query_human_object.py "Aric Altovolo"
query_human_object.py "World's Cornerstone"
```

A useful result should show:

1. what object was resolved;
2. aliases;
3. project associations;
4. known literal assertions;
5. explicit unknown/conflicting assertions;
6. relationships;
7. exact supporting source refs.

The user should not need to know a BCS id first.

## Ambiguity rule

If one string can resolve to multiple objects, the resolver must return ambiguity rather than choosing whichever object is most common in the corpus.

Project scope may disambiguate.

This is important for repeated names, titles, species names, and recycled concepts.

## Coverage rule

Absence from the human-object registry means:

> "not indexed as a human object yet"

It does not mean:

> "does not exist in Brendon's work."

This distinction must remain visible until corpus-wide indexing is mature.

## Construction strategy

Do not attempt a one-shot ontology extraction.

Build the finite index iteratively:

1. seed from strongly established source material across multiple projects;
2. extract obvious proper nouns and named systems;
3. resolve aliases;
4. add source-backed assertions;
5. add relationships only where explicit evidence supports them;
6. add human review for ambiguous collisions;
7. expose unindexed/high-frequency names as a backlog;
8. later connect art/assets and derived research concepts.

Automation should propose objects. It should not silently canonize identity merges.

## v0 seed policy

The initial seed deliberately uses Earthfall, Bastion/Redoubt, and At War's End rather than concentrating on S3/Empire.

This is an architectural test, not a claim that these projects are more important.

The purpose is to verify that the representation works across substantially different material before broad extraction.

## Non-goals for v0

Do not:

- replace BCS/BCE/BCR;
- make one giant graph database;
- infer every co-occurrence as a relation;
- flatten fictional characters and real humans together;
- treat research concepts as source facts;
- resolve every object in the corpus immediately;
- use embeddings as the canonical identity layer;
- make S3/Empire the default namespace.

## Immediate next experiments

After the schema/query prototype works:

1. seed 25-50 objects across at least five projects/eras;
2. run remembered-name tests supplied by Brendon;
3. test alias collisions and same-name objects;
4. connect canonical art/assets for a handful of established characters;
5. produce an Established Character identity packet from registry data;
6. extract a candidate-object backlog from source text and Discord projections;
7. compare automated extraction against human review before scaling.

## Product-level success condition

Brendon should be able to name something from his own history in ordinary language and receive the right literal object, its relationships, its uncertainties, and the evidence behind it.

That literal model should then support higher-level discussion without forcing either Brendon or Kit to rediscover the underlying corpus every time.
