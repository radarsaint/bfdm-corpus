# Source Lead — Tales from Aracania on World Anvil

**Status:** public-source family identified; canonical world URL known; full crawl/archive pending.  
**Source surface:** World Anvil.  
**User-supplied entry link:** `https://share.google/58ynOnaIQtDqH2Z8h`  
**Canonical world URL:** `https://www.worldanvil.com/w/tales-from-aracania-roanokerpg`  
**Empire City campaign dashboard UUID:** `d330377d-a94e-46d0-9a5b-6389dc6a4523`  
**Known public campaign URL:** `https://www.worldanvil.com/epic/EmpireCity`  
**Known public article:** `https://www.worldanvil.com/w/tales-from-aracania-roanokerpg/a/a-brief-introduction-to-empire-city-article`  
**Known world map:** `https://www.worldanvil.com/w/tales-from-aracania-roanokerpg/map/e72022ed-db53-4a53-88ca-7fce26fe6c15`  
**Admission status:** discovery lead only; do not allocate a BCS ID until the World Anvil world/article identities and authorship/provenance boundaries are resolved.

## What is currently confirmed

Public web indexing exposes an **Empire City** campaign page on World Anvil and identifies it as:

> A Dungeons & Dragons 5e game In the world of Tales from Aracania

The indexed campaign page exposes a player-facing publication structure including:
- lore;
- a brief introduction to Empire City;
- Our Lady Columbia art;
- a Season 3 Discord tutorial;
- server guidelines;
- supporting cast;
- scheduled sessions;
- Empire City Opening Day on July 10, 2021;
- a link to explore the broader Tales from Aracania world.

The page is presented under the World Anvil storyteller/account label **RoanokeRPG**.

The authenticated Empire City dashboard supplied by Brendon is:
`https://www.worldanvil.com/heroes/campaign/d330377d-a94e-46d0-9a5b-6389dc6a4523/dashboard`

This establishes World Anvil as a real publication/delivery surface connected to Roanoke/Empire City, not merely an unrelated reference site.

## Why this matters to BFDM

World Anvil may preserve a different layer of the creative record than Drive or Discord:

`private planning / source drafts -> selected public lore -> player-facing campaign presentation -> live play`

That makes it potentially useful for studying:
- what prep was selected for publication;
- how private material was simplified or reframed for players;
- what lore was considered important enough to expose before play;
- continuity between early Aracania setting work and later Roanoke seasons;
- player-facing onboarding and information architecture;
- differences between internal campaign documents and durable public canon;
- publication chronology where article timestamps/revisions survive.

It may also provide a public-facing bridge among the existing Arcania source family:
- 2018 early Roanoke / Rowing Oak;
- 2019 *Arcanian Almanac*;
- 2020 race-edit/final material;
- Roanoke S3;
- 2021 Empire City / S4;
- later Arcania setting-book work.

## Preferred acquisition path

World Anvil provides an owner-controlled **Export World** function. Its advanced export can produce a structured ZIP containing world metadata/content serialized as JSON plus a basic human-readable HTML representation. This is preferable to reconstructing the source family from search-engine crawl fragments because it preserves the owner's world as a coherent package and gives BFDM both machine-readable and human-readable representations.

Preferred workflow:
1. obtain a World Anvil owner export for **Tales from Aracania**;
2. preserve the original export ZIP unchanged as the source-faithful representation;
3. inventory its objects and native identifiers before allocating BCS IDs;
4. preserve the supplied JSON as machine-readable provider data rather than creating a competing canonical rewrite;
5. preserve/extract the supplied HTML as the human-readable representation;
6. deduplicate exported objects against existing Drive/public-export material;
7. retain public URLs such as the article and map deep-links as provider locators;
8. keep private/draft/public state and chronology where the export exposes them.

## Required archival pass

After export acquisition (or, failing that, when the public World Anvil surface can be crawled reliably):

1. enumerate all accessible articles, timelines, maps, images, campaign pages, character pages, handouts, and other public records;
2. preserve article title, canonical URL/native identifier, publication/update timestamps when exposed, category/folder structure, and outbound/internal relationships;
3. archive readable bodies in human-readable form;
4. preserve linked images/assets when technically and legally appropriate;
5. determine whether article authorship is attributable to Brendon, collaborative, account-level only, or unknown rather than inferring authorship from the RoanokeRPG label;
6. deduplicate against existing Drive/public-export sources before allocating BCS IDs;
7. model draft/private-source -> World Anvil publication relationships where evidence supports them.

## Current access limitation

Testing on 2026-10-04 found:
- the canonical world URL is valid but the research web fetch path returns a cache miss rather than the rendered homepage;
- the authenticated `/heroes/.../dashboard` surface is not publicly crawlable;
- the public `/epic/EmpireCity` campaign page is indexed and readable through search results;
- exact-title searches for the visible Empire City lore links currently collapse back to the campaign page rather than exposing the underlying article URLs;
- generic site search does not yet enumerate the broader `tales-from-aracania-roanokerpg` article graph;
- a direct public article deep-link and a direct map deep-link are now known, but the research fetch path still receives World Anvil cache misses on those object pages.

This is an access/discovery limitation, not evidence that the underlying World Anvil articles are absent.

Do not mistake the currently indexed Empire City page for the full World Anvil source family.

## Research caution

A public World Anvil article is evidence of what was published to players/readers at that time. It is not automatically:
- the complete private design;
- proof of passage-level sole authorship;
- the final live-delivered state;
- independent confirmation when it is merely a publication/export of an already archived Drive source.

Treat publication state, private prep, development discussion, and live delivery as distinct evidence layers.
