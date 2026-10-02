# Identity Resolution

Purpose: resolve Brendon's changing screen names across seasons and platforms without losing evidence or falsely attributing other users.

Operational machine registry:
- `registry/people.jsonl`
- `registry/identities.jsonl`
- `registry/discord_servers.jsonl`

This document defines the policy; the registry contains scoped machine-readable assertions.

## Canonical person

Canonical research identity:
- Brendon Faulkner

User-confirmed alias:
- DM radar

Known Roanoke Season 3 Discord identity:
- Discord user ID: 313689699627696139
- username: bfdm
- display name: DM radar

The S3 mapping is supported by the harvested database plus Brendon's explicit confirmation that he is also DM radar.

## Names are contextual; IDs are preferred

Screen names and server nicknames may change from season to season.

Therefore:

1. Prefer immutable platform account IDs when available.
2. Store server-specific nicknames/display names with date ranges.
3. Preserve historical aliases rather than rewriting raw source text.
4. Use alias mappings for retrieval, not for normalizing the source itself.
5. Do not assume a handle found in another server belongs to Brendon solely because it matches a known alias.

## Identity assertion record

Future ingestion should support fields equivalent to:

- canonical_person_id
- canonical_name
- platform
- account_id
- server_or_project_id
- username
- display_name
- valid_from
- valid_to
- basis
- confidence
- notes

Recommended basis values:
- USER_CONFIRMED
- PLATFORM_ACCOUNT_ID
- PROFILE_METADATA
- SIGNED_SOURCE
- CROSS_SOURCE_MATCH
- ANALYST_INFERENCE

## Confidence

Confirmed:
direct user confirmation and/or stable platform identity.

Strong:
multiple independent metadata/source links.

Tentative:
plausible contextual match without stable identity evidence.

Tentative matches must not create attributable Brendon evidence without further review.

## Multiple accounts

Do not assume Brendon used only one account over the lifetime of the corpus.

If a later server exposes a different account ID but Brendon confirms it is his, add a second platform identity under the same canonical person.

Never rewrite distinct historical account IDs into one synthetic account ID.

## Collaborators

Apply the same machinery to collaborators when attribution matters.

Project ownership or DM hierarchy does not collapse identities. A collaborator-authored message remains authored by that collaborator even when it belongs to a Brendon-run campaign.

## Retrieval behavior

A search for Brendon evidence should expand through confirmed identity mappings relevant to that source, server, and date.

It should not globally search every remembered nickname without context.

This matters especially for Discord because:
- server nicknames can differ
- usernames can change
- display names can be duplicated

## Retrospective identity statements

Brendon's current statement that he is also DM radar is preserved as `BCE-000011` and is a USER_CONFIRMED retrospective identity assertion.

That is enough to establish the alias relationship for research.

For each specific server harvest, still preserve the actual account/user ID and historical display name present in that server.


## Current unresolved seasonal mapping

Roanoke Season 4 / Empire City now has a harvested Discord server:

- server ID: `850779382791536640`
- server label: `Empire City.`
- campaign label in harvest README: `Season 4, Empire City`

Brendon's account/user ID inside that server has **not yet been resolved in this registry**.

Do not copy the S3 Discord account mapping into Season 4 merely because Brendon used `DM radar` in S3 or has confirmed that alias generally.

The Season 4 identity should be added only after inspecting that server's users/messages or receiving direct account-level confirmation.
