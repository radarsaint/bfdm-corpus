# Research Status

## Source archive

### Roanoke Season 3 Discord
Available in the private corpus:

`discord/roanoke-season-3/roanoke-season-3.sqlite`

Verified harvest:
- 197,013 messages;
- 194 text channels;
- 1,421 / 1,421 attachments;
- window: 2020-07-18 through 2020-08-22;
- Brendon identity used in research: `DM radar` / `bfdm`, Discord user `313689699627696139`.

### Google Drive / project material
A large body of campaign planning, worldbuilding, homebrew races/classes, writing, revision history, and other D&D work is available through connected sources. Full ingestion into the private corpus is still in progress.

The intended next archive step is to store Google/project material in:
- machine-searchable form (including SQLite/indexed metadata where appropriate);
- human-readable form;
- with source IDs, Drive IDs, timestamps, authorship, provenance, and revision relationships retained.

### Roanoke Season 4 / Empire City Discord
Available in the private corpus:

`discord/empire-city/empire-city.sqlite`

Verified harvest:
- server ID: `850779382791536640`;
- 189,761 messages;
- 247 text channels;
- 52 threads;
- 3,528 / 3,528 attachments;
- observed server message range: 2021-06-05 through 2026-10-01.

The server README explicitly identifies the campaign as **Season 4, Empire City**.

Do not treat the observed server message range as the campaign live window. The server contains later activity that can outlive the campaign. Brendon's account/user identity inside this server remains unresolved in the identity registry.

### Remaining Discord servers
Additional game servers still need harvesting. S3 and Empire City now provide two major live/server datasets, but cross-season conclusions should still remain provisional until broader coverage exists.

## Completed research passes

### S3 decision cases v1
Branch: `derived/s3-decision-cases-v1`  
PR #2 — closed as superseded by PR #5; unmerged

Focus:
- single decision moments;
- what Brendon noticed;
- values in tension;
- intervention;
- result;
- reusable judgment.

### S3 longitudinal cases v2
Branch: `derived/s3-longitudinal-cases-v2`  
PR #3 — closed as superseded by PR #5; unmerged

Focus:
- prepared expectation;
- live signal;
- adaptation;
- downstream consequence.

### S3 revision-family pass v3
Branch: `derived/s3-revision-family-v3`  
PR #4 — closed as superseded by PR #5; unmerged

Focus:
- prep-driven change vs live response;
- Google Drive revision history;
- causal classification;
- source-of-truth rules.

Important correction produced by this pass:
Week 5's lower authored density was substantially **prepared adaptability**, not merely an emergency decompression during live play.

## S3 source reconciliation correction

The revision-family pass initially described Week 2 and Week 4 as source-container gaps. The legacy staging manifest later confirmed they were already normalized:

- `BCS-000029` — Roanoke S3 v2 W2 Breakdown;
- `BCS-000037` — Roanoke s3w4 Break down.

The remaining task is to **reconcile/migrate those staged containers into the canonical `bfdm-corpus` source layout**, not to create new BCS records.

## Newly surfaced non-S3 evidence

### Bowling Event
Google Drive document: `Bowling Event:`  
Drive ID: `1bn1YBXqQyD22XfbyIme_S-AvBI7hLT92GCC2Jt4f5b4`

This is a 2018 Brendon-authored conversion of real-world bowling into a D&D resolution system.

Observed design features include:
- pins knocked down become damage to the enemy;
- pins left standing become damage to the player;
- strikes become critical damage;
- spares generate gold;
- encounters occupy bowling frames;
- monster abilities key off bowling states;
- D&D class abilities become physical bowling behaviors;
- five groups of five were intended to compete over a ten-frame adventure.

Research value:
This may be evidence about how Brendon experiments with the **boundary and physical form of D&D**, not merely how he adjudicates ordinary play.

Do not generalize from it yet. It should enter a broader creative-method research pass after more of the archive is normalized.

## Numbered cleanup state

- Points 1–3 are complete: attributable retrospective evidence, the Work GPT ingestion contract, and machine-readable project/identity registries.
- Point 4 is next: reconcile the full 51-source legacy staging body into canonical `bfdm-corpus` while preserving BCS IDs.
- Point 5 remains open: deliberate review/integration of draft PR #5.
- Point 6 remains open: recover the complete later Area 6c human-test transcript.
- Point 7 is complete and governing: archive-first corpus preservation; Kit is one consumer.

## Current constraints / handoff state

- Work GPT is expected to resume Google/project-file ingestion.
- Grok is expected to resume lower-level Kit/GitHub work and Discord harvesting.
- Current GPT research should avoid competing with those ingestion/runtime tasks.
- The useful work now is organization, methodology, source-gap identification, and preparing cross-campaign research questions.

## Next research phases after source coverage improves

1. Finish remaining ingestion/harvest coverage.
2. Refine the now-machine-readable campaign/source chronology as stronger live-date and scale evidence arrives.
3. Run comparable research passes across multiple eras, including Empire City.
4. Search for persistence, evolution, abandonment, and format-specific behavior.
5. Only then write a broad human-readable synthesis for Kit and Brendon to discuss.

S3 should remain a methodology testbed until those comparisons exist.

## Legacy staging verification

The 51-record legacy staging manifest is now preserved under `research/legacy-staging/manifest.all.jsonl` for source-ID reconciliation. The old handoff's proposed `radarsaint/brendon-corpus` target is superseded; `radarsaint/bfdm-corpus` is canonical.
