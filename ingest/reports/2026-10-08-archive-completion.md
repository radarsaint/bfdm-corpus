# Archive completion — 2026-10-08

Physical completion pass. Not BFDM research, not Kit design.

## SHAs

- Starting `main`: `65513f294e72a3eb961d5699c21ddc1f14ceef2c`
- Ending branch SHA: the head of this pull request. It cannot be written inside the commit that creates it. The PR body records it after push.

## Already complete, skipped

- Discord model retrieval and canonical SQLite harvests. PR #27 still owns retrieval maintenance. It was not edited.
- Legacy 51-source migration.
- Merged Drive integration PR #25, substrate PR #31, and reconciled ingest PR #36. Canonical range on the starting main was BCS-000001–BCS-000172.
- First-pass Drive triage. This pass used the classified ledger. It did not rediscover Drive.
- PR #28 Phase 2, PR #33 human-object index, PR #38 semantic evidence audit, PR #39 coordination docs. Not edited.
- BCS-000059 is a context container at `context/exploration-impossible/BCS-000059`. It is not missing. The document index only scans `sources/`, so it stays out of `indexes/documents.sqlite` by the existing builder.
- BCS-000068 is a ChatGPT excerpt snapshot in `evidence/`. It is not a Drive container and was not treated as a missing file.

## Inventory

- Catalog BCS rows at start: 172, contiguous BCS-000001–BCS-000172.
- Source containers at start: 171. The only catalog id without a container was BCS-000068.
- SQLite `source_containers` at start, after rebuild from that tree, would have been 170 because the builder ignores `context/`.
- No duplicate catalog ids. No Drive native id maps to two BCS rows after this pass.
- Google Sites captures stay under `sources/roanoke-s5-legends/google-sites/`. They were not reclassified as ordinary Drive containers.

## Candidates examined and admitted

All 18 rows still labeled `HIGH_PRIORITY_INGEST` were read and admitted. The named unfinished targets were included.

| BCS | Title | Drive id | What was preserved | What was not |
| --- | --- | --- | --- | --- |
| BCS-000173 | Ferrytown Master Doc | `1M2Lj_bTH3fKQxAsnnyDg8C5p_jf59FEC4d4IOVIioJM` | Markdown export, 10 images | DOCX export rejected, size reported 19421214. Owner Darrylynn Penney. Comments empty. |
| BCS-000174 | Hampstead Module | `1J_ex2QXbL5UvrkZZgxw7N62vulHzZm51ekxn6ZZKYIc` | Markdown export, 20 images | DOCX export rejected, size reported 18961400. Owner Anthony S. Not BCS-000141. |
| BCS-000175 | Pigeon Lord v2 | `1wukQySSYeNcOJqWEV-Ij7Kl0dJmdY3H-AEvt07WNimI` | DOCX and paragraph text | Not marked superseded over BCS-000148. |
| BCS-000176 | Mirabelle (1) | `1ZEEvZIs_wxkWz0mCXUfgyN7l8ezAuv3k0opjVGCf9bY` | DOCX and paragraph text | Shorter than BCS-000147. Modified one day earlier. Not a supersession. |
| BCS-000177 | Bodfish Boom Town | `1-G0zOaSmA7dCAlBd8i7cWOBBazDJWFnxDso-WBfLdnk` | DOCX and text | Same-titled Google Site `1H09rehjbslQjAGfJGVaYIsPJkN50D1dg` was unreadable and was not ingested as this file. |
| BCS-000178 | Bodfish Boom Town Daily Breakdon. | `1m9CfO_PNT_zXmr0vAb3BNFPqY-i89p0jMaJ6v96O8xA` | DOCX and text | Day grid is mostly empty. |
| BCS-000179 | Weekly breakdown template. | `18rUCGpVznLSgH67lsHgh3TgWtl0tE09e1ODk_OzBIdg` | DOCX and text | Form, not a filled week. Not the 2020 Break down Template candidate. |
| BCS-000180 | Arcania Setting Book | `1Xgtbk9cJqlvwx7lCcRo3EPGuWuYzCd5zOoX_99BPo80` | DOCX and text | No Arcania project id was invented. Season not assigned. |
| BCS-000181 | Arcanian Lore Public Document. | `1KqFDUIV0de99qPXIbWRDYZRh8B1iE347-XZOlf4d_p8` | DOCX and text | Version family with BCS-000076 only. Not BCS-000144. Not a replacement. |
| BCS-000182 | Bowling Event: | `1bn1YBXqQyD22XfbyIme_S-AvBI7hLT92GCC2Jt4f5b4` | DOCX and text | Registry creation date left at 2018-08-30. Modified time on the file is 2020-08-22. Event delivery not established. |
| BCS-000183 | Season 5. | `1_wqsPUOwI5frqMz0uZ86-cx40pep44hTAxdt4PRCXTA` | DOCX and text | Framing, not a postmortem, not play. |
| BCS-000184 | Home Brew Backgrounds.S4 | `1CYh5-dADeBg23n3G35JDiycajoiAypQ2bBRui0FSL20` | DOCX and text | Not merged into Season 5 backgrounds. |
| BCS-000185 | The Speaker of the Dead's Epilogue | `1fgHlofwQPZSpDaaNGCDhwoq89LPC8TQC1gFvL_nsok4` | DOCX and text | Owner awesomeguy.vjr. Not Brendon evidence. |
| BCS-000186 | The big project | `1xGfCbKD7GyoJ6nzZ0jZ6iAouKK49ncZH1dvlRIVKxVQ` | DOCX and text | Origin essay. No season id. |
| BCS-000187 | Staaten Island brain storming | `1sF0xLGCrJiEK5wxp5V9NjxKXPj3gadVWw1JwGIjpixM` | DOCX, text, 7 comments | Comments are from the DOCX comments part. Authors Brendon Faulkner and Jack Hagey. |
| BCS-000188 | Elijah | `1ZDOarJzjMFEwYM025VrV_APxZvTVlSri-ydjprGsXC8` | DOCX and text | Owner larahazboun. Project unresolved. |
| BCS-000189 | Races for the isakei | `1NIK4fF4Zc676Q9zEWIN0KYjcirS3bTW4N6iSqYCskEg` | DOCX and text | 2026 reskin notes. Not a Season 3 verbatim. |
| BCS-000190 | Kore-A: THE CLOCK OF ETERNITY | `1Umg3gIBjuL6Mnr_hWLTZ-uQlF3fWlvBD5KZQWxk-hJw` | DOCX and text | Owner rhus93722. Session narrative. Not Brendon precedent. |
| BCS-000191 | CFS.pdf | `1VZE5UOP2PcUYUMZhlI2C5i6sEKMZFaBs` | Original PDF and pypdf text | Creator's note mentions colonists of Roanoke and does not name a season. |
| BCS-000192 | Content Rulings | `1XB5cnltZZkYerCBE4snXZsQa86vHaOW5aqY_l_Cgaeo` | XLSX and cell text | Owner bghooper88. Not a Brendon decision log. |
| BCS-000193 | Dec 28 2025 Allowed Content | `1CQp9bSkAf9TPL4IPpldE6-pKpFZlMJ-gYtw_9QhH64A` | XLSX and cell text | Owner jamesridgwayjr. Not superseded by the May sheet. |
| BCS-000194 | May 19 2026 Allowed Content | `19UAOSlMXh89R6Zi17J78X9ECApw1RqEsT7tpWAG1Ips` | XLSX and cell text | Owner jswycislak. Later title is not withdrawal of BCS-000193. |
| BCS-000195 | S5 Materials Draft | `1nb5pUk7G3EeTqtuXppXf1rZzi2gvJSrCtRpZ5D1puBc` | XLSX and cell text | Owner darknessemerald. |

New BCS records: BCS-000173–BCS-000195. Highest BCS: BCS-000195.

`LIKELY_FAMILY_MEMBER` and lower actions were not bulk-ingested. Wellsprings phb remains a candidate.

## Existing BCS repaired

- BCS-000114: original Way of Gun Fu PDF bytes stored at `sources/roanoke-s5-legends/BCS-000114/original/source.pdf` (816524 bytes). `source.md` was not regenerated.
- BCS-000132: the three style-guide hyperlinks now point at BCS-000177, BCS-000178, and BCS-000179.
- BCS-000147 and BCS-000176: version family only.
- BCS-000148 and BCS-000175: version family only. The draft is not marked replaced.
- Bowling registry anchor now names BCS-000182. Creation date unchanged. Coverage says the container is present and live use is not established.

## Gap ledger

`scripts/build_archive_gap_ledger.py` is still the generator. Regenerated `research/substrate/archive_gaps.jsonl` and `archive_gaps.md`.

Current bodies marked `RESOLVED`: Season 4 timeline, Season 5 style guide, Season 5 DM guide, player race edits, Tatankan verbatim, almanac, Arcania setting book, isekai race notes, bowling, Legends signup, Season 5 framing, Ferrytown schedule, elevator module.

`PARTIAL_CURRENT_BODY_ONLY`, earlier wording or omitted export still missing:

- Season 5 character creation, BCS-000145, April 2023 wording not recovered.
- House rules, BCS-000134, captured text is the 2023-04-30 state, not the 2020 release.
- Rowing Oak, BCS-000136, captured text is the 2019-03-13 export, not the July 2018 revision.
- Rowing Oak guide, BCS-000137, prose is present. DOCX export is still too large, so images stay omitted.

`research/drive-inventory/2026-10-03/candidates.jsonl` marks admitted rows `INGESTED`. `classify_drive_candidates.py --write` regenerated the triage. Unreviewed rows and the triage file are the same set. No `HIGH_PRIORITY_INGEST` row remains. `NEEDS_MANUAL_REVIEW` remains.

## Index and tests

`python scripts/build_documents_sqlite.py`

- containers 193
- `PRAGMA integrity_check` ok
- `PRAGMA foreign_key_check` no rows

Passed:

- `python ingest/validate_ingest.py`
- `python registry/validate_registry.py`
- `python scripts/validate_source_history.py`
- `python scripts/test_substrate_queries.py`
- `python scripts/test_source_readiness.py`
- `python scripts/test_query_source_history.py`

FTS smoke hits included Archavist (BCS-000142), Rowing Oak (BCS-000136 and BCS-000137), Master Timeline (BCS-000131), Way of Gun Fu (BCS-000114), Bodfish (BCS-000177 and BCS-000178), Fryvern (BCS-000156).

Representation checksums are checked by `validate_ingest.py`.

## Still blocked

- No Drive revision-list tool. No revision metadata and no historical revision bodies were fetched for any family, including BCS-000131–BCS-000151 and the new containers. Created timestamps were not returned by file search. Modified times above are from file search.
- Rowing Oak guide images. DOCX export still returns `exportSizeLimitExceeded`.
- Bodfish Boom Town Google Site `1H09rehjbslQjAGfJGVaYIsPJkN50D1dg`. Search returned it and marked it unreadable. It is not BCS-000177.
- ChatGPT Project/Library access is not available in this environment. Earthfall BCS-000152–BCS-000162 and Saturday D&D BCS-000163–BCS-000172 stay partial recoveries. No search excerpt was upgraded to a transcript.
- Native Drive comment lists were requested for Ferrytown and were empty. Other new files were not given a separate comment-list pass, except Staaten Island, whose seven comments were inside the DOCX export.
- Remaining `MISSING_KNOWN_SOURCE` rows were not recovered: S4 char gen, Player Races Final.pdf, Clerrook, the Arcania setting-book how-to, Jarvis class note, DCC-like classes, S5 crafting, Airship Rules (no Drive id), Manticore, artifacts list, week 4 cast list, hex drawings, week 2 audio, unfetched revision bodies, and the ambiguous Season 3 directory headings. Sane Magical Prices stays external.
- The rest of the classified backlog, including Wellsprings phb, was not admitted.

## Pull requests

- PR #27, Discord retrieval maintenance, author radarsaint, merge state DIRTY against current main. Not merge-ready. Left to its owner. This pass does not change Discord retrieval.
- PR #28, PR #33, PR #38, and PR #39 were inspected and not modified.

## Status of this pass

- Completed: inventory reconciliation, stale gap correction, admission of the named targets and the remaining high-priority candidates, Way of Gun Fu PDF, index rebuild, validators.
- Partial: house rules, character creation, Rowing Oak, and the Rowing Oak guide. Current bodies exist. Earlier revisions or omitted images do not.
- Blocked: revision lists, Rowing Oak guide images, Bodfish Site, ChatGPT project histories, the still-missing known Drive ids above.
- Not attempted: semantic verification, Phase 2, human-object expansion, precedent cards, Kit runtime, `dnd-solo`, Discord re-harvest, broad Drive rediscovery.
