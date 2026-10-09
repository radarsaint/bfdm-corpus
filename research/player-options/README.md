# Player options

Research index for the Warden creations consumer. Read this, then [INVENTORY.md](INVENTORY.md), then [options.jsonl](options.jsonl).

Current `main` is the authority (`6795362e`). This directory does not replace a BCS source. If a sentence here and a source disagree, the source wins. Quote the source line named on the record.

## How to look up one option

1. Find the name in the index table in `INVENTORY.md`, or search `options.jsonl` for `"name"`.
2. Open `primary_path` at `anchor_line`. The `anchor_quote` is a short extract so you can confirm you are on the right passage.
3. Use `rules_overview` and `mechanics` as a map. They are not a rebalanced rewrite. Missing numbers stay missing.
4. Read `conflicts` before you pick a spelling or a version.
5. `design_relation` `RESKIN` means the file keeps another race's mechanics and renames features. `BESPOKE_ALSO_PRESENTED_AS_RESKIN` means char-gen maps the name onto a published species and a different page prints its own traits. Keep both.
6. Discord ids are in `discord-mentions.jsonl` and on the record. Do not expect message text in git. `play_observed` `NOT_ESTABLISHED` means this inventory did not prove live use.

## Files

| File | Role |
|---|---|
| `INVENTORY.md` | Human index and one section per option, except At War's End archetype names, which are a table. |
| `options.jsonl` | Same records, one JSON object per line. |
| `COVERAGE.md` | What was searched, what a zero means, what was inaccessible. |
| `discord-mentions.jsonl` | Phrase counts, channels, message ids, attachment filenames. No message bodies. |

## Not in this index on purpose

- External species, classes, and feats that appear only as allow or deny rows in BCS-000192, BCS-000193, and BCS-000194.
- Catalog items, day-one scene text, and server or house rules that do not create a race, class, subclass, feat, background, life path, or spell.
- Clerrook rules. The body is not on this main. See the gap record `gap-clerrook`.

