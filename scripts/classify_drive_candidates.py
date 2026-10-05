#!/usr/bin/env python3
"""First-pass labels for unreviewed Drive discovery rows.

Title, search query, and the 2026-10-05 glance are the evidence. This does
not open the remaining files and does not admit them.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def row(action, value, confidence, project, role, relation, duplicate, basis):
    return {
        "recommended_action": action,
        "historical_research_value": value,
        "confidence": confidence,
        "probable_project": project,
        "probable_source_role": role,
        "likely_relation_to_existing_sources": relation,
        "duplicate_or_version_likelihood": duplicate,
        "basis": basis,
    }


BY_ID = {
    "12x9hz_mOEGvEf3boTpggrd1xPvnRUoZrHOx7pxzaoSA": row(
        "LIKELY_DUPLICATE_OR_VERSION", "MEDIUM", "MEDIUM", "roanoke-s3", "week cast",
        "Compare with BCS-000049 before a second week-1 cast container.", "HIGH",
        "Opened 2026-10-05: the file says Roanoke S3 V2.1 and is a week-one cast list.",
    ),
    "13YMPowhu9zAQh3ZN0jrf_ORRCC4W22iIeomQRBUE9Q8": row(
        "LOW_RESEARCH_VALUE", "LOW", "MEDIUM", "UNRESOLVED", "stub",
        "No family claim from a three-line opening.", "LOW",
        "Opened 2026-10-05: three-line Roanoke stub.",
    ),
    "14r_9Sq46QSgswZik0qaBv_xZeXxKuxfNZkTIdF6VU0I": row(
        "LOW_RESEARCH_VALUE", "LOW", "MEDIUM", "roanoke-s4", "setting fragment",
        "Not a substitute for the Season 4 directory or timeline.", "LOW",
        "Opened 2026-10-05: short Empire City founding paragraph.",
    ),
    "1cICMcrUkYvrcOzylUcaKrveGGY71JVH4E1JMXR_HN-Y": row(
        "LIKELY_DUPLICATE_OR_VERSION", "HIGH", "MEDIUM", "roanoke-s3", "public lore",
        "Compare with BCS-000076 before a second public-lore container.", "HIGH",
        "Opened 2026-10-05: titled in the body as Roanoke Season 3 Public Lore Dump.",
    ),
    "1CS0BHuuUGT6K8QD1d62mFkMcAeBuDDV-y4u1cQePj5M": row(
        "LIKELY_FAMILY_MEMBER", "HIGH", "MEDIUM", "roanoke-s3", "map working notes",
        "Hex lines match the Season 3 map key BCS-000081.", "MEDIUM",
        "Opened 2026-10-05: a working Gaps list, not a second bestiary.",
    ),
    "1FU3wM280ZKvRHic9aF4XbSJeFkZ80AWcDZqBM9KBamY": row(
        "UNRELATED", "LOW", "MEDIUM", "UNRESOLVED", "essay",
        "No campaign-operations claim from the opening.", "LOW",
        "Opened 2026-10-05: essay on radio, film, and television.",
    ),
    "1KKWpjcJs1Bfi-wqjO7gY0BNVuW_CE6tplF4ZWdoETEA": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "player FAQ",
        "Dates differ from the Season 3 FAQ BCS-000021. Do not assign that season.", "LOW",
        "Opened 2026-10-05: player FAQ dated July 10–30 and August 13–20.",
    ),
    "1MRB4vk13UdbGbaIYX4AWFegHtTyabjxyYuqXdIsAuTY": row(
        "CONTEXT_ONLY", "LOW", "MEDIUM", "UNRESOLVED", "third-party module notes",
        "Not a Roanoke or Empire City design document on the evidence of the opening.", "LOW",
        "Opened 2026-10-05: notes on D&D's Mad Mage.",
    ),
    "1oJxfLF66bNPa7NPQjwW6GDzUVjJLRs30PWdvuQatrMU": row(
        "LIKELY_DUPLICATE_OR_VERSION", "HIGH", "MEDIUM", "roanoke-s3", "week breakdown",
        "Opening links the same three documents as BCS-000048.", "HIGH",
        "Opened 2026-10-05: begins as RoanokeS3 Week 1.",
    ),
    "1PN5cqTatq6o9c2vSyfQVriLT4p15NRCnEoL3I6MuIIo": row(
        "LOW_RESEARCH_VALUE", "LOW", "MEDIUM", "roanoke-s3", "location note",
        "Cape Antler is already a hex on the ingested map key.", "LOW",
        "Opened 2026-10-05: five lines on Cape Antler.",
    ),
    "1rmvauuB8RYk9nW8cDyMN11FRrC1nR-U0XEyuLnwa8F4": row(
        "CONTEXT_ONLY", "LOW", "MEDIUM", "UNRESOLVED", "collaborator chat",
        "Not a postmortem of a harvested campaign.", "LOW",
        "Opened 2026-10-05: pasted chat about a Warehouse 13 setup.",
    ),
    "1W_f8hohY2jW9d0QmLPy6C8eWbuKy0y4K_oZEaiOhLhU": row(
        "LOW_RESEARCH_VALUE", "LOW", "MEDIUM", "UNRESOLVED", "poem",
        "Not identified as the ingested Roanoke song.", "LOW",
        "Opened 2026-10-05: a poem.",
    ),
    "1WtXK2UuWqa5YjK5HOk3tvAENRJVyr7SAJpH4t04BuKg": row(
        "NEEDS_MANUAL_REVIEW", "UNKNOWN", "LOW", "UNRESOLVED", "three-act outline",
        "Project is not established from the opening.", "LOW",
        "Opened 2026-10-05: outline for Alan, Kaliope, and Cait. Left unread beyond that.",
    ),
    "1x7x8Eo2683LcC-oPohu_BUQy9L-amqyDpUeSbmNCCr8": row(
        "UNRELATED", "LOW", "MEDIUM", "UNRESOLVED", "essay",
        "No campaign record in the opening.", "LOW",
        "Opened 2026-10-05: essay on news framing.",
    ),
    "1AV4piqqYZHTJFP66_zjhQQwD1zHGaxrhhxZgUquoDOo": row(
        "CONTEXT_ONLY", "LOW", "HIGH", "roanoke-s3", "empty week form",
        "Not the missing week 4 cast. The form has those headings and is unfilled.", "LOW",
        "Opened 2026-10-05: empty week form dated 08/01/2020.",
    ),
    "1oXbwcummGVyxPqx0pWBGFyc49RtunTJHne3teo2fhXo": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "roanoke-s3", "link list",
        "Points at the public-lore document already ingested. Other links were not resolved here.", "MEDIUM",
        "Opened 2026-10-05: week 3 resources link list.",
    ),
    "1_wqsPUOwI5frqMz0uZ86-cx40pep44hTAxdt4PRCXTA": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "roanoke-s5-legends", "season framing",
        "Registry planning anchor for 2023-04-20. Not a substitute for the published Sites.", "LOW",
        "Opened 2026-10-05: 'The way to Legend' and a justice-or-mercy question. Not a postmortem.",
    ),
    "1xGfCbKD7GyoJ6nzZ0jZ6iAouKK49ncZH1dvlRIVKxVQ": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "UNRESOLVED", "setting origin essay",
        "Possible predecessor to later Arcania setting books. Project season is not established.", "LOW",
        "Opened 2026-10-05: Arcania began as a fantasy retelling of early American history.",
    ),
    "1JVh2UM0Ka33X70aUamnKBRc9DTFyBBnI-XFIBDHYdxA": row(
        "LOW_RESEARCH_VALUE", "LOW", "MEDIUM", "UNRESOLVED", "product pitch",
        "Four lines do not record a campaign decision.", "LOW",
        "Opened 2026-10-05: four-line Kickstarter pitch.",
    ),
    "1F-MN26HhvSJoqrudfwihTX_qo6SDBGQTfc-Unb78Sp8": row(
        "LOW_RESEARCH_VALUE", "LOW", "HIGH", "at-wars-end", "fiction",
        "Full open lists Nocturne fiction under not campaign material.", "LOW",
        "It can sit beside the novel later. It is not a DM-operations source.",
    ),
    "1qyfc7XC0qMIhDIjGb05Ognp-anXofgx8oHQPyCCAQoU": row(
        "NEEDS_MANUAL_REVIEW", "UNKNOWN", "HIGH", "UNRESOLVED", "unreadable",
        "No family claim.", "UNKNOWN",
        "Full open: Drive returned 404.",
    ),
    "1AI2WK3wtQyykHBfVILKj9Er8de7nwBZE": row(
        "NEEDS_MANUAL_REVIEW", "UNKNOWN", "HIGH", "UNRESOLVED", "unreadable pdf",
        "Not the ingested Spelljammer lodestone.", "UNKNOWN",
        "Full open: Drive returned 404.",
    ),
    "1e8SOv_8nenpRnWdVwH_m88RaTlL17yVzyxBTjdwJLIs": row(
        "NEEDS_MANUAL_REVIEW", "UNKNOWN", "HIGH", "UNRESOLVED", "unreadable",
        "No family claim.", "UNKNOWN",
        "Full open: Drive returned 404.",
    ),
    "174l3B6vFI77IaXciz0cAJPx5pHxZEydT": row(
        "NEEDS_MANUAL_REVIEW", "UNKNOWN", "HIGH", "UNRESOLVED", "image pdf",
        "Text was not extracted.", "UNKNOWN",
        "Full open: image-style PDF, extraction failed.",
    ),
    "1GdV1jwvujK8WX5Z0eaBMCkmWKdBewyW7": row(
        "NEEDS_MANUAL_REVIEW", "UNKNOWN", "HIGH", "UNRESOLVED", "handout",
        "Other player-handout files were readable. This DOCX was not.", "UNKNOWN",
        "Full open: connector would not return text.",
    ),
    "0B7TcIEIiRnBZQmZmRjBNVzZlVm8": row(
        "LIKELY_DUPLICATE_OR_VERSION", "LOW", "HIGH", "UNRESOLVED", "duplicate letter",
        "Same letter as the shoemaker's daughter, which the full open sets aside.", "HIGH",
        "TRIAGE_PASS_2026-10-05.md",
    ),
    "134nblLb3PbfnnWj72rFstSzA17X39dOKapaFn6s3IEM": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "roanoke-s4", "borough event schedule",
        "Comment on the Season 4 directory quotes the word Schedule and links this file.", "LOW",
        "Cited from BCS-000072. Title is Ferrytown Main Event Schedule.",
    ),
    "1fpuTPkVyJzE5n9gxIcBMZ_J3q_mOXHq6uwpCKnKxQGU": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "roanoke-s3", "encounter module",
        "Week 3 breakdown BCS-000052 links it as the elevator gauntlet.", "LOW",
        "A prepared module cited by an ingested week sheet and still only a candidate.",
    ),
    "1To_48fHi0RuYoeov-qWBXUgSDaB8LN7WkXkX8hJFREI": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "early Roanoke / pre-Season-3", "setting and race design",
        "Source lead records it as the Arcanian Almanac playtest, with race material later revised.", "LOW",
        "Named in research/source-leads/homebrew-mechanics-worldbuilding.md with revision modifiers.",
    ),
    "11QDOazLzTM3Mv0E4hnPyFpY1wyYweeCoG-ZX8eyX6ho": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "roanoke-early-2018", "campaign architecture",
        "Registry planning anchor. Season 2 guide describes a previous incarnation with the same economy.", "LOW",
        "The Rowing Oak is not a container. Search hit alone is not the evidence; the registry source_ref is.",
    ),
    "1JqDKaRTEx89rAUcNrtSg4I6ZD7XAHRkFTWqDRRCroHw": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "roanoke-early-2018", "multi-DM operations guide",
        "Companion to The Rowing Oak. Announces the July 2018 live opening in the source lead.", "LOW",
        "Registry live-window source_ref. Still unreviewed as a container.",
    ),
    "1bn1YBXqQyD22XfbyIme_S-AvBI7hLT92GCC2Jt4f5b4": row(
        "HIGH_PRIORITY_INGEST", "MEDIUM", "HIGH", "bowling-event-2018", "format experiment",
        "The registry has a project and no container.", "LOW",
        "Title matches the registry project Bowling Event.",
    ),
    "12xmsqaB6x09sOn2wBvsWAFpEsAM5fFukKBH5h9eC5UA": row(
        "HIGH_PRIORITY_INGEST", "MEDIUM", "HIGH", "roanoke-s5-legends", "signup / operations",
        "Registry planning anchor. Published Sites are not this spreadsheet.", "LOW",
        "Title is Legends sign up.",
    ),
    "1g6ZQhzVoAWzFikAoTYJfqUJIyBwMmpgZojidn57tOu0": row(
        "LIKELY_FAMILY_MEMBER", "HIGH", "HIGH", "at-wars-end", "rules companion",
        "BCS-000066 is Wellsprings in At War's End. This file is the separate Wellsprings PHB named in the source lead.", "MEDIUM",
        "Do not treat it as a duplicate until the two texts are compared.",
    ),
    "1NIK4fF4Zc676Q9zEWIN0KYjcirS3bTW4N6iSqYCskEg": row(
        "HIGH_PRIORITY_INGEST", "MEDIUM", "HIGH", "2026 design, project unresolved", "race reskin notes",
        "Source lead contrasts it with earlier bespoke Arcanian races. Not a Season 3 source.", "LOW",
        "Later contrast document. Useful after the earlier race line is ingestible.",
    ),
    "1Xgtbk9cJqlvwx7lCcRo3EPGuWuYzCd5zOoX_99BPo80": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "Arcania setting, season unresolved", "setting book",
        "Named beside the Almanac in the source lead. Not matched to an ingested container.", "LOW",
        "Title match only plus the source-lead drive id.",
    ),
    "1r1OUHeNxVIIueMWtsQ7J5xwL2szoHMa5": row(
        "NEEDS_MANUAL_REVIEW", "MEDIUM", "LOW", "UNRESOLVED", "homebrewery pdf",
        "Source lead says not to assume authorship from Drive presence.", "UNKNOWN",
        "Provenance check before any family link.",
    ),
}

BY_TITLE = {
    "Ferrytown Master Doc": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "roanoke-s4", "borough master",
        "Directory names Ferrytown as a location with a schedule. This title is the master doc, not the schedule already cited.", "LOW",
        "Title only. The cited schedule is a different drive id.",
    ),
    "Hampstead Module": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "roanoke-s4", "borough module",
        "Season 4 directory lists Hampstead as a location still in progress.", "LOW",
        "Title only.",
    ),
    "Hampstead Players Guide": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "roanoke-s4", "player-facing borough guide",
        "Pairs with the Hampstead module title. Not yet compared.", "MEDIUM",
        "Title only.",
    ),
    "Hampsteed updated info": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "roanoke-s4", "borough notes",
        "Spelling variant of Hampstead. May be a revision of the module or guide.", "MEDIUM",
        "Title only.",
    ),
    "Home Brew Backgrounds.S4": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "roanoke-s4", "player options",
        "Season label is in the title. Published Season 5 backgrounds are a later site.", "LOW",
        "Title only. Do not merge it into the Season 5 site family without reading it.",
    ),
    "Staaten Island brain storming": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "roanoke-s4", "borough brainstorm",
        "Directory lists Isle Staaten as a scheduled location.", "LOW",
        "Title only.",
    ),
    "s4 valentines day one shot.": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "roanoke-s4", "one-shot",
        "Side event, not the five-week borough structure, unless the text says otherwise.", "LOW",
        "Title only.",
    ),
    "Arcanian Lore": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "UNRESOLVED", "setting lore",
        "Possible predecessor or public pair of Arcanian Lore Public Document. Both are still candidates.", "MEDIUM",
        "Title only. Season not established.",
    ),
    "Arcanian Lore Public Document.": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "UNRESOLVED", "player-facing lore",
        "Title marks a public version. Compare with BCS-000076 and BCS-000075 before linking.", "MEDIUM",
        "Title only.",
    ),
    "The Urucokra": row(
        "LIKELY_DUPLICATE_OR_VERSION", "HIGH", "MEDIUM", "roanoke-s3", "race lore",
        "BCS-000120 is The Urucokra Verbatim. This may be another version.", "MEDIUM",
        "Title only. Do not drop either until compared.",
    ),
    "S5 Materials Draft": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "roanoke-s5-legends", "materials draft",
        "Season 5 crafting and gathering pages exist as Sites. This spreadsheet may be the internal draft.", "MEDIUM",
        "Title only.",
    ),
    "Content Rulings": row(
        "HIGH_PRIORITY_INGEST", "HIGH", "LOW", "UNRESOLVED", "rulings sheet",
        "A rulings sheet would be operational judgment. The search query was At War's End, which is not a season assignment.", "LOW",
        "Title only. Read before treating it as precedent.",
    ),
    "Crui's Essence Crafting Spreadsheet": row(
        "LIKELY_FAMILY_MEMBER", "HIGH", "MEDIUM", "roanoke-s4", "crafting operations sheet",
        "Empire City crafting BCS-000001 is an essence economy. This may be the tracking sheet.", "MEDIUM",
        "Title only. Authorship is not established by the name Crui.",
    ),
    "Archavist Daysong Timeline.": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "UNRESOLVED", "timeline",
        "Not the Season 3 Master Timeline BCS-000070.", "LOW",
        "Title only.",
    ),
    "S4 Jack's. Weapons": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "roanoke-s4", "item list",
        "Possible companion to Empire City custom items named in the directory.", "LOW",
        "Title only.",
    ),
    "Solo Player Primer": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "UNRESOLVED", "player primer",
        "No ingested primer has this title.", "LOW",
        "Title only.",
    ),
    "Pudwudgie Enforcer": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "UNRESOLVED", "race or class option",
        "Halfwudgie lore is ingested. This title may be a later option or a subclass.", "LOW",
        "Title only.",
    ),
    "Kimmelian": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "roanoke-s4", "homebrew race",
        "Season 4 directory names Kimmelian as a draft race.", "MEDIUM",
        "Title only. A Homebrewery PDF with the same name is a separate candidate.",
    ),
    "Kimmelian - The Homebrewery.pdf": row(
        "LIKELY_DUPLICATE_OR_VERSION", "MEDIUM", "LOW", "roanoke-s4", "published race export",
        "May be the export of the Kimmelian doc. Provenance still required.", "MEDIUM",
        "Title only.",
    ),
    "Pigeon Lord v2": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "roanoke-s4", "creature or subclass draft",
        "Version title implies an earlier attempt. The draft file is a separate candidate.", "MEDIUM",
        "Title only.",
    ),
    "Pigeon Lord- draft": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "roanoke-s4", "creature or subclass draft",
        "Pair with Pigeon Lord v2. Order is not established by the titles alone.", "MEDIUM",
        "Title only.",
    ),
    "Journal of the Red Ram.pdf": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "roanoke-s4", "in-world or faction document",
        "Red Coats lore is BCS-000075. This PDF was not compared.", "LOW",
        "Title only.",
    ),
    "Poor richard's letter": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "roanoke-s4", "in-world letter",
        "Possible companion to Empire City Post or faction lore.", "LOW",
        "Title only.",
    ),
    "The treaty of the wilds.": row(
        "LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "roanoke-s4", "in-world treaty",
        "No ingested treaty of that name.", "LOW",
        "Title only.",
    ),
    "The Speaker of the Dead's Epilogue": row(
        "NEEDS_MANUAL_REVIEW", "UNKNOWN", "LOW", "UNRESOLVED", "epilogue",
        "Could be fiction, a one-shot, or a campaign ending. Title does not settle which.", "LOW",
        "Title only.",
    ),
    "player handout": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "UNRESOLVED", "player handout", "One of several handout files. Compare before ingesting all of them.", "HIGH", "Title only."),
    "Player handouts.docx": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "UNRESOLVED", "player handout", "One of several handout files.", "HIGH", "Title only."),
    "Player handouts.pdf": row("LIKELY_DUPLICATE_OR_VERSION", "LOW", "LOW", "UNRESOLVED", "player handout export", "Likely an export of a handout doc.", "HIGH", "Title only."),
    "Player handouts and backgrounds.pdf": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "LOW", "UNRESOLVED", "player handout", "May overlap BCS-000085 player backgrounds.", "MEDIUM", "Title only."),
    "Beta Readers": row(
        "LOW_RESEARCH_VALUE", "LOW", "MEDIUM", "at-wars-end", "fiction",
        "Full open lists Nocturne fiction under not campaign material. Both ledger rows share this title.", "LOW",
        "Not a DM-operations source.",
    ),
    "Mirabelle – A Tragedy in Five Acts": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "HIGH", "at-wars-end", "five-act play", "Full open identifies Mirabelle as an At War's End play. Not a campaign-operations source.", "MEDIUM", "TRIAGE_PASS_2026-10-05.md"),
    "Mirabelle – A Tragedy in Five Acts (1)": row("LIKELY_DUPLICATE_OR_VERSION", "LOW", "LOW", "UNRESOLVED", "copy", "Filename marks a second copy.", "HIGH", "Title only."),
    "Copy of 5th Edition Magic Items Purchasing Catalogue": row("LIKELY_DUPLICATE_OR_VERSION", "LOW", "MEDIUM", "UNRESOLVED", "reference spreadsheet", "Copy of another candidate catalogue.", "HIGH", "Title only."),
    "Copy of [Template] 5E D&D Character Sheet (Tintagel) v2.92": row("CONTEXT_ONLY", "LOW", "MEDIUM", "UNRESOLVED", "character sheet template", "Blank or template sheet. Not a decision record by title.", "MEDIUM", "Title only."),
    "Copy of Copy of [Template] 5E D&D Character Sheet (Tintagel) v2.92": row("LIKELY_DUPLICATE_OR_VERSION", "LOW", "MEDIUM", "UNRESOLVED", "character sheet template", "Second copy of the template.", "HIGH", "Title only."),
    "Copy of Pokemon Personality Quiz - Master Copy": row("UNRELATED", "LOW", "MEDIUM", "UNRESOLVED", "unrelated quiz", "Search hit, not a campaign source, on the title.", "LOW", "Title only."),
    "FFXV Stat Master List (Weapons, Accessories, Attire, Food, Levels)": row("UNRELATED", "LOW", "MEDIUM", "UNRESOLVED", "other game stats", "Final Fantasy XV reference, not an Arcanian rules document, on the title.", "LOW", "Title only."),
    "D&D 5e SRD magic items table": row("CONTEXT_ONLY", "LOW", "MEDIUM", "UNRESOLVED", "third-party reference table", "SRD table. Annotations are not established.", "LOW", "Title only."),
    "5th Edition Magic Items Purchasing Catalogue": row("CONTEXT_ONLY", "LOW", "LOW", "UNRESOLVED", "reference catalogue", "May be a tool used at the table. Not established as Brendon's design.", "LOW", "Title only."),
    "23 Spelljammer Ships and 7 Helms.pdf": row("CONTEXT_ONLY", "LOW", "LOW", "UNRESOLVED", "third-party supplement", "Spelljammer lodestone BCS-000128 is a different document.", "LOW", "Title only."),
    "Spelljammer_Giff.pdf": row("CONTEXT_ONLY", "LOW", "LOW", "UNRESOLVED", "third-party supplement", "Not the ingested lodestone.", "LOW", "Title only."),
    "Tarokka Resources.pdf": row("CONTEXT_ONLY", "LOW", "LOW", "UNRESOLVED", "third-party module aid", "Curse of Strahd aid on the title.", "LOW", "Title only."),
    "Mad mage": row("CONTEXT_ONLY", "LOW", "MEDIUM", "UNRESOLVED", "third-party module notes", "Opened sibling is Mad Mage notes. This title is the same module.", "MEDIUM", "Title only."),
    "Mad mage.pdf": row("CONTEXT_ONLY", "LOW", "MEDIUM", "UNRESOLVED", "third-party adventure pdf", "Published adventure file. Four copies share the title.", "HIGH", "Title only."),
    "Subclass - Druid - Circle of the Storm - The Homebrewery.pdf": row(
        "NEEDS_MANUAL_REVIEW", "MEDIUM", "LOW", "UNRESOLVED", "subclass pdf",
        "Source lead warns that Homebrewery PDFs in Drive are not automatically Brendon's.", "UNKNOWN",
        "Provenance check.",
    ),
    "Wellsprings phb": row(
        "LIKELY_FAMILY_MEMBER", "HIGH", "HIGH", "at-wars-end", "rules companion",
        "Same file as the source-lead Wellsprings PHB.", "MEDIUM",
        "Kept beside the drive-id override.",
    ),
}


# Titles the 2026-10-05 full open placed in TRIAGE_PASS_2026-10-05.md.
# That pass is the evidence. These rows do not re-read the files.
PASS_TITLE = {
    "100 random quick city encounters": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "encounter table", "Full open lists 100 city encounters as campaign material.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Budget 2022": row("LOW_RESEARCH_VALUE", "LOW", "HIGH", "UNRESOLVED", "household budget", "Full open lists the household budget under not campaign material.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "calico": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "filled character sheet", "Full open says Calico is a filled sheet, not a blank template.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "ADWD:DAD Share Copy": row("UNRELATED", "LOW", "MEDIUM", "UNRESOLVED", "other-book index", "Full open lists a Game of Thrones index under not campaign material.", "LOW", "Title is the only ADWD row. Treated as that index."),
    "CFS.pdf": row("HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "UNRESOLVED", "class text", "Full open names a Combat Field Scholar class text.", "LOW", "TRIAGE_PASS_2026-10-05.md. Title is CFS.pdf."),
    "Charter.pdf": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "roanoke", "in-world charter", "Full open names an in-world Roanoke charter. Season is not assigned here.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Coney Island": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "roanoke-s4", "location text", "Full open: Coney Island / Illo'fae location text.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Dec 28 2025 Allowed Content": row("HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "later play, project unresolved", "content rulings", "Full open names the Dec 2025 allowed-content sheet as campaign material.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "May 19 2026 Allowed Content": row("HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "later play, project unresolved", "content rulings", "Full open names the May 2026 allowed-content sheet.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Content Rulings": row("HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "UNRESOLVED", "species allowance rulings", "Full open reports a species-allowance rulings sheet. This is the only ledger title that says Rulings.", "LOW", "Confirm the drive id before treating the match as certain."),
    "Familiar Crimes Report": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "in-world report", "Named in the full open as campaign material.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Gil's Rebirth v1": row("HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "UNRESOLVED", "design notes", "Full open calls this design notes.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Highgate hunt club.pdf": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "location or faction", "Full open names Highgate Hunting Club.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Johnny apple seed.": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "episode", "Full open names a Johnny Appleseed episode.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Kore-A: THE CLOCK OF ETERNITY": row("HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "2026 session, project unresolved", "session log", "Full open dates this as a session log on 30 Apr 2026.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Lilia's Ending": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "ending", "Named in the full open.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Manuscript for anna": row("LIKELY_FAMILY_MEMBER", "HIGH", "HIGH", "roanoke race lore", "manuscript", "Full open: Urucokra / Canticle of the Canopy. Not the ingested verbatim.", "MEDIUM", "TRIAGE_PASS_2026-10-05.md"),
    "Monster Chess": row("HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "UNRESOLVED", "rules", "Full open lists Monster Chess rules as campaign material.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Order of Kairo- Collection of Works": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "faction sheet", "Full open names an Order of Kairo member sheet.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Sacrificing love": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "outline", "Full open: Iceland / Roanoke crossing outline.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Starlight Rails Campaign Basic Information": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "HIGH", "UNRESOLVED", "campaign primer", "Full open names the Starlight Rails primer and does not place the project.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Tales from Arcania- Items": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "item list", "Named in the full open.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "The Amber-Mound: Master-Doc": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "setting master", "Full open pairs Guide to the gods with a separate Amber-Mound master doc.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "The city and Noir items": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "roanoke-s4", "item list", "Full open names Kingsbridge Noir items.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "The catalog": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "roanoke-s4", "item catalog", "Full open: The catalog (Fatass Brand Guns).", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "The Mender's story": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "story notes", "Named in the full open.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "The Speaker of the Dead's Epilogue": row("HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "roanoke-s4", "epilogue", "Full open calls this an Empire City epilogue.", "LOW", "Aftermath evidence. Not yet a container."),
    "The treaty of the wilds.": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "HIGH", "UNRESOLVED", "in-world treaty", "Named in the full open.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Welcome to Tyboria": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "HIGH", "UNRESOLVED", "setting intro", "Full open: Year 15 of a 3rd Age, not tied to an existing project.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "5/18/24": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "HIGH", "bastion-redoubt", "prose", "Full open: Bastion and Redoubt prose dated 5/18/24 in the file.", "MEDIUM", "May be a sibling of BCS-000056. Not compared here."),
    "Elijah": row("HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "UNRESOLVED", "character handoff", "Full open names an Elijah character handoff.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "POPULATION OF FORT FELLION": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "HIGH", "UNRESOLVED", "population sheet", "Named in the full open.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "The Vigil.pdf": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "HIGH", "UNRESOLVED", "scenario", "Full open names The Vigil of Siege Perilous.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Subclass - Druid - Circle of the Storm - The Homebrewery.pdf": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "subclass", "Full open lists Circle of the Storm with campaign material. Authorship is still not proven by Drive presence alone.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Mortem: chapter 2": row("LOW_RESEARCH_VALUE", "LOW", "HIGH", "UNRESOLVED", "fiction chapter", "Full open lists Mortem chapter 2 under not campaign material.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "the shoemaker's daughter.docx": row("LOW_RESEARCH_VALUE", "LOW", "HIGH", "UNRESOLVED", "letter", "Full open lists this letter under not campaign material.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "Guide to the gods": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "cosmology", "Full open names Guide to the gods.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
    "𝔾𝕦𝕚𝕕𝕖 𝕥𝕠 𝕋𝕙𝕖 𝕘𝕠𝕕𝕤": row("LIKELY_FAMILY_MEMBER", "MEDIUM", "MEDIUM", "UNRESOLVED", "cosmology", "Presentation whose title is Guide to the gods.", "MEDIUM", "TRIAGE_PASS_2026-10-05.md"),
    "S5 Materials Draft": row("HIGH_PRIORITY_INGEST", "HIGH", "MEDIUM", "roanoke-s5-legends", "craft notes", "Full open lists Season 5 non-canon craft notes. This is the S5 materials spreadsheet in the ledger.", "MEDIUM", "Confirm it is the non-canon notes before a family link."),
    "Staaten Island brain storming": row("HIGH_PRIORITY_INGEST", "HIGH", "HIGH", "roanoke-s4", "NPC table", "Full open calls the Staaten Island file an NPC table.", "LOW", "TRIAGE_PASS_2026-10-05.md"),
}


def pattern(title: str) -> dict | None:
    if title.startswith("TEMP SRD"):
        return row(
            "CONTEXT_ONLY", "LOW", "MEDIUM", "UNRESOLVED", "SRD excerpt",
            "Systems Reference Document text. Comments inside the copy are not established.", "LOW",
            "Title is TEMP SRD 5.1.",
        )
    return None


def classify(candidate: dict) -> dict:
    title = candidate["title"].strip()
    found = (
        BY_ID.get(candidate["drive_id"])
        or PASS_TITLE.get(title)
        or PASS_TITLE.get(candidate["title"])
        or BY_TITLE.get(title)
        or BY_TITLE.get(candidate["title"])
        or pattern(title)
    )
    if found is None:
        queries = candidate.get("queries") or []
        project = queries[0] if len(queries) == 1 else "UNRESOLVED"
        found = row(
            "NEEDS_MANUAL_REVIEW",
            "UNKNOWN",
            "LOW",
            project if project != "At War's End" else "UNRESOLVED",
            "unread",
            "Search query is not project membership.",
            "UNKNOWN",
            "The 2026-10-05 full open did not give this title its own role. It stays unread-by-this-audit rather than guessed.",
        )
        if len(queries) != 1:
            found["probable_project"] = "UNRESOLVED"
    out = {
        "candidate": candidate["drive_id"],
        "title": candidate["title"],
        "queries": candidate.get("queries") or [],
        "mime_type": candidate.get("mime_type"),
    }
    out.update(found)
    if candidate["drive_id"] == "1NIK4fF4Zc676Q9zEWIN0KYjcirS3bTW4N6iSqYCskEg":
        pass
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    repo = Path(args.repo).resolve()
    ledger = repo / "research" / "drive-inventory" / "2026-10-03" / "candidates.jsonl"
    rows = [json.loads(line) for line in ledger.read_text(encoding="utf-8").splitlines() if line.strip()]
    classified = [classify(row) for row in rows if row.get("status") == "UNREVIEWED_CANDIDATE"]
    if args.write:
        dest = repo / "research" / "substrate"
        dest.mkdir(parents=True, exist_ok=True)
        text = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in classified)
        (dest / "candidate_triage.jsonl").write_text(text, encoding="utf-8")
        counts: dict[str, int] = {}
        for row in classified:
            counts[row["recommended_action"]] = counts.get(row["recommended_action"], 0) + 1
        lines = [
            "# Drive candidate triage — research substrate audit, 2026-10-05",
            "",
            "Action labels for the 132 rows still marked `UNREVIEWED_CANDIDATE`. The openings are in `research/drive-inventory/2026-10-03/TRIAGE_PASS_2026-10-05.md`. This file does not re-read them and does not assign BCS ids.",
            "",
            "A Drive search query is not a project assignment.",
            "",
            "## Counts",
            "",
        ]
        for key in (
            "HIGH_PRIORITY_INGEST",
            "LIKELY_FAMILY_MEMBER",
            "LIKELY_DUPLICATE_OR_VERSION",
            "CONTEXT_ONLY",
            "LOW_RESEARCH_VALUE",
            "UNRELATED",
            "NEEDS_MANUAL_REVIEW",
        ):
            lines.append(f"- `{key}`: {counts.get(key, 0)}")
        lines.extend(["", "## High priority", ""])
        for row in classified:
            if row["recommended_action"] == "HIGH_PRIORITY_INGEST":
                lines.append(f"- `{row['title'].strip()}` `{row['candidate']}` — {row['basis']}")
        lines.append("")
        (dest / "candidate_triage.md").write_text("\n".join(lines), encoding="utf-8")
        print(counts)
    else:
        print(len(classified))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
