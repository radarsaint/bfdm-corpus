# Corpus access

Readable, non-Discord query surface for this checkout. It does not replace
canonical files and it does not search Discord message bodies.

```bash
python -m access coverage
python -m access audit
python -m access search "Golden Dawn"
python -m access search "Golden Dawn" --project "Roanoke S3"
python -m access search cryptid --limit 20
python -m access entity "DM radar"
python -m access sources roanoke-s5-legends
python -m access evidence BDC-S3-001
python -m access evidence BCS-000045
python -m access related BCS-000045
python -m access timeline cryptid
python -m access record BCE-000014
python -m access export "Golden Dawn" --project roanoke-s3 --out /tmp/golden-dawn.json
python -m access build
```

Every command prints JSON. `search` / `evidence` / `related` / `timeline` /
`export` include a `coverage` object. `coverage.coverage_report.status` is
`EXHAUSTIVE`, `PARTIAL`, `INACCESSIBLE`, or `UNKNOWN`.
`zero_match_means_absence` is true only when that status is `EXHAUSTIVE`.
`absence_is_not_evidence` is the inverse. A zero hit is not absence while any
relevant family was partial, excluded, or unread.

`python -m access audit` counts searchable records, catalog-only records,
pointer databases versus databases whose bytes are present, intentionally
excluded files, and open gaps.

Reason codes apply only to the state they describe:

| Code | Meaning |
|---|---|
| `lfs_pointer_only` | That path is a Git LFS pointer in this checkout. |
| `missing_readable_projection` | No text projection was searched for that material. |
| `external_auth` | The other copy is an external document this checkout cannot open. |
| `missing_target` | A recorded path is not in the checkout. |
| `intentionally_excluded` | The files are on disk and left out of the default search. |
| `unmerged_workstream` | `ingest/discord-retrieval-v1` or `ingest/drive-project-v3` still owns the missing piece. |

`drive_bcs_bodies` is `PARTIAL` when some BCS rows have bodies and others are
`catalog_only`. Hydrated SQLite is `NOT_SEARCHED` with an empty reason list.
A pointer is `INACCESSIBLE` / `lfs_pointer_only`. There is no size cutoff and
no "binary database" reason. See [COVERAGE_DECISIONS.md](COVERAGE_DECISIONS.md).

`--project` accepts a `project_id` (`roanoke-s3`) or a unique registry alias
(`Roanoke S3`, `Empire City`, `Season 5`). An unknown or ambiguous filter
exits 2 and lists the project ids.

## What a hit is

Each hit keeps its authority. Do not treat these as the same kind of evidence.

| `authority` | What it is |
|---|---|
| `source_catalog` | A `BCS-*` row in `evidence/catalog.jsonl`. `body_status: present` means a markdown or text body in this checkout was attached (Season 5 Google Sites, `BCS-000113`, `BCS-000114`, the BCS-000068 snapshot). `catalog_only` means the container is registered and the body is not here. |
| `attributable_evidence` | A `BCE-*` row. |
| `relation` | A `BCR-*` row. |
| `normalized_source` | A body that has no BCS id yet. Current Season 5 pages keep their canonical BCS ids instead of `access:site:` ids. |
| `derived_case` | One JSONL decision/revision case (`BDC-*`). |
| `research_note` | A research markdown note. Id `access:note:<path>`. |
| `registry` | Project, series, person, identity, or project-relation row. |
| `harvest_metadata` | Discord server registry plus that server's README. This is harvest scope, not message text. |

`body_status` is `present`, `catalog_only`, or `not_applicable`. Discord message
cites use `discord-message:<snowflake>` and resolve as
`discord_message_candidate` / `inaccessible`. Those snowflakes are extracted
from derived-case text. They are not confirmed by opening the database.
Known Discord account ids and server ids are not turned into message cites.

## Families this command searches

Default search covers:

- `registry/`
- `evidence/catalog.jsonl`, `evidence.jsonl`, `relations.jsonl`, and portable snapshots
- `sources/**` readable bodies: Google Sites `pages/*.md` when a BCS id points at them, plus `source.md` / `source.txt`
- Roanoke S3 case JSONL: `decision-cases-v1`, `longitudinal-decision-cases-v2`, `revision-family-v3`
- `research/**/*.md` except the two optional trees below, and except markdown that only renders one of those JSONL files
- Discord server READMEs, as harvest metadata

Season slicing uses `registry/projects.jsonl`. A catalog row labeled only
`Roanoke` is not forced into one season. It is included in an unfiltered
search and omitted from `--project roanoke-s3` (and the other seasons) unless
that project's `source_anchors` name the BCS id. `sources` reports the omitted
count. Cross-campaign notes whose filename is in the small span table
(`cryptids-s3-s4-v1.md`, `mythic-institutions-s3-s4-v1.md`,
`roanoke-s3-to-s4-judgment-v1.md`, `roanoke-economy-2018-to-s2.md`) carry both
project ids with `project_resolution: filename_span`. That is a navigation aid,
not a scope finding.

Dates:

- registry windows, identity `valid_from` / `valid_to`, and `BCE` `date_start` are structured
- derived cases expose the earliest and latest ISO dates **cited in the case**, `date_kind: cited_in_case`
- research-note prose is not mined for dates
- Google Sites `fetched_at` is `captured_at` only. `timeline` lists those hits under `capture_time_only`

## Families this command does not search

`coverage` reports each of these. Do not fill the gap by guessing.

| Family | Status in the default checkout |
|---|---|
| Discord message bodies | `not_searched`. The `discord/*/*.sqlite` files are Git LFS pointers here. |
| Discord text export | `absent` until `indexes/discord/catalog.json` exists. That export and `python -m retrieval.discord_search` live on `ingest/discord-retrieval-v1`. This tool does not call it. |
| Discord attachment bytes | `not_searched` (Git LFS). |
| Drive / legacy BCS bodies | Mostly `catalog_only`. The 51-container staging bodies are not in `sources/` or `context/`. Reconciliation is on `ingest/drive-project-v3`. |
| `research/kit-evaluation/` | Present, excluded. `--include-evaluation` adds it. |
| `research/prior-dnd-solo/` | Present, excluded. `--include-imported` adds it. |
| `campaigns/` | No document bodies. |

A hydrated SQLite file is still `not_searched` by this tool. Message search
stays with `retrieval.discord_search` so there is one Discord implementation.

## Rebuild

```bash
python -m access build
python -m unittest access.tests.test_access -v
```

`indexes/access/records.jsonl` and `indexes/access/manifest.json` are generated.
No timestamps. `manifest.inputs_sha256` covers the input files. Query commands
rebuild when that hash changes. The committed JSONL is the last built snapshot;
if you change a source, run `build` before committing the index.

Record JSON keeps `record_id`, `record_class`, `authority`, `title`,
`project_ids`, `project_labels`, `project_resolution`, `date_start`,
`date_end`, `date_kind`, `captured_at`, `path`, `body_status`, `cites`,
`attributes`, and `text`. Search results omit `text` unless `--full`, and add
`snippet`, `match`, and `score`.

Stdlib only. Python 3.10+.
