# Author-intent discovery — 2026-10-26

**Discovery inventory. Not research guidance. Not doctrine. Not a Kit prompt, memory, or precedent. Not a satisfaction score. Not a claim that every intention in his life, or even every intention in the archive, was found.**

Read this before treating any line below as a conclusion. The row files next to this report are the searchable inventory. This page is the reading of those rows.

Corpus main used: `cf65ec04572b2a033383344d1f2583e3380686f7`.

## What was searched

Brendon's confirmed Discord account is user id `313689699627696139`, username `bfdm`, display name `DM radar`. The registry scopes that id to three harvested servers and does not record another Discord account for him. A scan of all three projections found no other author whose username or display name is `bfdm` or `DM radar`.

| Source | What was readable | Brendon text messages |
| --- | --- | ---: |
| Roanoke Season 3 `636012145204527125` | model-index JSONL, 197013 messages, matching the registry | 18621 |
| Empire City `850779382791536640` | model-index JSONL, 189761 messages | 9399 |
| Empire City Dev `746645778352832542` | model-index JSONL, 12692 messages | 4862 |

Canonical `discord/<server>/<server>.sqlite` and `indexes/documents.sqlite` are Git LFS pointers in this checkout. They were not queried. The Discord search used the model-facing projection described in `MODEL_RETRIEVAL.md`. Message counts match the registry, so the projection covers the harvested text of those three servers. It does not cover voice, deleted or unharvested messages, or the pixels inside attachments.

No other Discord harvest is in the registry. Co-DM and player messages were not treated as his.

Document search used `sources/**/source.md` for catalog containers whose authorship is `BRENDON` (owner attestation of 2026-10-09, which is creator-and-copyright, not a line-by-line claim). ChatGPT snapshot files were limited to `USER` blocks. Drive comments whose author display name is `Brendon Faulkner` were read: 42 non-empty comments. Historical revision diffs were not compared sentence by sentence. Image-only files were not read.

The Discord pass is lexical. A message was kept when his text matched one of: want, need, hope, plan, intend, trying, going to / gonna, would like / rather / prefer, goal / aim, decided / set out, won't allow, I'll allow, meant, wish, refuse / not going to, on purpose / deliberately, so that, from now on, house rule, we should / have to, let's. That produced **800** messages. A sentence with none of those shapes was not retrieved. Absence from this inventory is not absence from the archive.

Tiers on the 800:

| Tier | n | Rule |
| --- | ---: | --- |
| author | 364 | Table, announcement, admin, or dev-staff channel, or a parenthetical aside |
| ambiguous | 316 | Live or dev channel, no parenthesis. 38 of these also use words like player, rule, scene, week, or story |
| character_voice | 120 | Inside quotes, or a long all-caps performance |

Character speech was not converted into his intention. Examples that the pattern caught and this report does not treat as his aim: `(I'm not going to throw away my shot! Hamilton replies)` (message `734209949537665059`); Mason all-caps "WE ARE GOING TO ARCANIA"; an unquoted "I'd like to check on my daughter."

Fiction inside attested documents was the same kind of miss. *At War's End* drafts, Empire City newspaper posts, and Bastion/Redoubt dialogue examples say "I want" and "we need" in a character's mouth. Those lines are in `document-pattern-hits.jsonl` and are not listed below as his intentions. A spreadsheet inside an attested container can also contain someone else's row. Season 5 materials notes that say "my npc" were not treated as his.

## How to read a row

Discord locator: server id, channel id, message id, timestamp, all on the JSONL row. Example: Season 3 server `636012145204527125`, channel `636012145204527127` (`out-of-character`), message `734131617584382013`, 2020-07-18.

Stance labels below mean only what the wording itself establishes. A plan is not recorded here as something that then happened.

## Season 3, July–August 2020 — what he said he was doing

The live window is dense. Most of the explicit aims are in `out-of-character` and `announcements`, plus parenthetical asides in play channels.

**Table attention.** 2020-07-18, message `734131617584382013`: "please @ them so that they don't miss your post. ... I don't want anyone to feel ignored." 2020-07-26, `737029187679813705`: he missed about ten pings while taking partner time "so that my wife doesn't feel left out," and offered a first-come list. 2020-08-04, `740015870843289680`: "I just want you all to know that I'm hearing you."

**Accommodation, with a limit.** 2020-07-19, `734251203935993957`: a secret society may be switched once within 24 hours. "We would like to accommodate your fun in any reasonable way." 2020-07-20, `734858688107642990`: "I'm trying to leave you guys with choices." The same week he also refuses a brute-force solution for a simple obstacle, `734849024561250304`: "I don't want to have to have you brute force rolls to do something simple."

**Consent and the right to stop.** 2020-07-23, `735726761437823086`: no PVP without a DM and both players. 2020-07-28, `737761939299762207`: he offers to recuse and will not continue "with out consent." The same night, `737778576102916116`: "I wont allow anymore shenanigan's until this matter is settled. ... if this ceases being fun, I'll have to cease dming." `737779131583954976`: the conflict "was meant to be resolved and bring people together as once enemies who become friends."

**The shape of the season, said while it was running.** 2020-07-24, `736011659683954729`: "My writing in London is meant to be like a Dark Fairy Tale. ... I consider the server 75% yours and 25% mine. But the 25% that is mine has to be shared amongst you." He describes stories that "connect together over multiple days" across "a 35 day run time," and says he has been putting pressure on himself "to protect both the game and the players." 2020-08-04, `740071292127936623`, after harm landed on Web and Baeshra: "The pressure of the ship and now the haven of your home are meant to turn you from survivors to capable adventuring parties. It was never my intention to cause Web or Baeshra harm." `740071531841060934`: "but I need trust to tell a story." `740069552678895668`: "except to where I wanted to tell a good story." `740069506965045338`: "Never have I been anywhere near anything where I was trying to controlling." That last one is a denial of an aim, not a measurement of whether control happened.

**Inclusion.** 2020-07-29, `738127994463191070`: the game world includes non-binary people "as a fully normal and culturally acceptable," and he asks for pronoun edits and shorter tags so non-binary players are not marked as different. 2020-07-31, `738907862457253909`: "So that no one culture would be singled out." 2020-08-20, `746088772046946324`: looking for a genderless word in the vein of Matriarch for Web.

**Rails he named as rails.** 2020-07-22, `735293497627902046`: one initiative for the whole adventure, teams of three, meta kept in OOC, voice for talk and questions rather than action. "Thanks for trying this with me." 2020-08-11, `742806909660168193`: the day's trouble follows what the town focuses on, internal or external. He is "not going to be running a main event perse." 2020-08-12, `743199116489916486`: "Set your intentions. Don't be reactionary." `743206606967406643`: "I'm on your side. And I want you to win. But infighting at this point will leave you homeless." `743248182640902235`: a deadly encounter, "I want you to live."

**Things he said were not for exploring, or that he closed on purpose.** 2020-07-20, `734909628986687529`: Victor "is the monster's backstory and not meant to be exploreable," with an invitational offered if it matters. 2020-08-19, `745437918977327154`: "i broke them so that option would be off the table. week 5 is flying island week. its not a problem that needs to be solved." 2020-08-15, `744056939096571924`: "I made a genuine mistake with my res rule. I'm going to have to nerf that ability for game balance reasons. Tonight's rez's still stand."

**Governance was not the story he said he was telling.** 2020-08-17, `745054916850221076`: "The masons were designed to be further away from politics. ... I set the cornerstone on the pub, because our story was meant to be about something other than governance. But the mayoral race became bipartisan."

**A mechanic he was dropping.** 2020-08-19, `745753934861303849`: he had planned that souls from the soulforge become a barrier after the game, and that destroying tools mid-combat would poison the hunger. "lets just go ahead and strike the 'destroy your tools during the fight' mechanic because it no longer makes sense." He says he is "rethinking the issue." The message does not say the strike was later reversed.

**Week 4 as a test, said in advance.** 2020-08-08, `741445787250327574`: week 4 is where characters are "tested the most," a three-act island whose second act is "the most fraught," and he asks them to consider resolve. He explicitly says this is not a warning of more mental anguish.

**End of the season, still prospective.** 2020-08-14, `743981601188216975`: "I'm already thinking about how much I'm gonna miss the game when its over." `743982681624412332`: "I'm going to need lots of help though." 2020-08-15, `744320116178681956`: "I'd like to start encouraging more exploration." 2020-08-17, `744838064232202301`: "I'm still trying to figure out what roanoke is without hiram." `744839374981562380`: "I'm going to need to pick a new tinker by the end of the season."

Logistics from the same weeks, kept because they are aims and not discarded: drug use limited (`734318988154241066`); a master inventory of submarine storage (`736067105782235187`); don't delete posts to hide them (`736910238552424500`); house rule that birthdays get a wish (`739334132903182366`); optional side quest of commoners named Chad (`740419034218102884`, repeated `742123530136584284`); he wants DMs about what people wish to explore (`742807517721133056`).

## Between seasons — Empire City Dev, from 2020-08-22

**One story, not competing DM stories.** 2020-08-22, dev server, message `746823073835253850`: collaboration was "an absolute blast" and "telling competing story solidifies cliques and drama." He wants "a single narrative with a more open world feel," each DM designing a borough and running what happens there. `746843997984522301` is the debrief he wants that week. 2020-08-23, `747224098266021898`: "I don't want to rehash this year's cliques." 2020-08-24, `747245626584072214`: "I want to accommodate, and it seems like gangs are a thing that we want. Maybe I'm being too gunshy."

**Staffing and kindness.** 2020-08-23, `746933618386927616`: ideally two DMs per district, and one who can share "global duties" and homebrew. 2020-08-28, `748767990757195867`: complaints included lack of agency when corrections were made, favoritism, nepotism, long combat waits. "We didn't ask anyone to leave this year when maybe we should have. It's always been my goal to try and retain people with kindness." `748771618305605714` is a retrospective on his own bluntness and on intervention versus inaction. It is his account of the weighing, not a finding that the weighing was correct.

**Design tasks he named.** An evil god for the redcoats (`746843997984522301`). An art-bible channel (`746845324341018674`). King George as a designed villain and a positive public story (`761757035683119116`, `761759563711512586`). Levels must be chosen before building, because higher play is more fun and more intense (`748068031091179632`). Hardboiled writing's question is "why do they care?" (`748335813237932043`). Domesticated cryptids as critters, and illusory script "so we don't need to have people hurt cute things" (`747984666409304176`, `747985822833180803`). World Anvil as the place content is aggregated, with a price and a crowd-fund ask that is not to feel like pressure (`750806511793471578`, `750882502691913760`). "we just need to build a better world" (`750100693171306546`), next to "we don't need to right wotc's wrongs" (`750100655162523810`). Multi-team encounters like the prior year's kraken fight (`815168928845398026`). Two people remembering one event differently (`816185682170085406`). "like I want them to rp" (`819364511076843521`). Save new pacts for next year (`819389822052859915`). Dating sim: "Dating Sim was never an intended part of the game. Its here now. And its here to stay, but if we are going to look at the mechanics, it needs a full overhaul" (`807799467339808768`). That sentence is both retrospective and prospective, and it does not say the overhaul was done.

**A story worth telling, said when he did not yet have the plot.** 2020-10-09, `763926520833638431`: "Right now I just want to focus on making a story worth telling."

## Empire City live, summer 2021

**The written rules, in his voice, on 2021-06-05.** Message `850796324478517250`: hateful language will not be tolerated; the game should be "a haven from the real world" and a place to deal with anxiety "in a healthy, mutually consensual way." `850797149025468506`: tell the DMs about an exploitable loophole "so that we can rectify it," in private, not in public where others can exploit it. `850798571888312320`: a long rest is leaving the server for the day, "a built in mechanic to help you take time off," so fear of missing out does not replace taking care of life and mental health. He reposts that house rule on 2021-07-19, `866740486822690836`.

**What the season is for, said mid-season.** 2021-07-15, `865189260877758485`: "the social aspect of this system is the point of what I write. Last year everything I wrote I wrote with the hopes that people would band together. This year I hope people learn to love themselves enough to not trade away who they are." `865186566318063626`: "I hope that by the end, people will be clinging to the last scraps of what makes them who they are." These are hopes. They are not a report of what players did.

**Equal references, no private houses.** 2021-07-14, `864911042601811980`: he has been saying no to links back to particular Season 3 people; "references belong to the dms to give out in equal measure." Croatoan in a backstory is open; the sub and England are "not specifically baned." 2021-07-10, `863492563784040539`: "we aren't giving out houses this year. Your home is meant to be vulnerable and there is meant to be risk." One exception would become "a million others."

**A 25/75 rule restated as a plea, not as dominion.** 2021-07-16, `#fountain-of-esteem`, message `865744435732283392` (the channel is not the OOC channel; the wording is his): "The 25% 75% percent rule is my way of begging the community to understand that this is not dominion level play. That we have to have some linear rails. That we are telling a story and that story sometimes means that despite their exploits and tricks, the game must move forward and can't always swing to adjust for players who can out wit us." He names Noah, Devon, and Ethan as players he may not outwit on the fly, and asks whether major plans should be scrapped on the fly. The message asks. It does not answer itself.

**He does not want to play a DM character if there is a Season 5.** 2021-07-16, `#a-fountain-of-player-tears`, `865563292747563008`: "If an when s5 happens I don't think I want a dm's char. Just a director's chair."

**Plans he changed or paused in public.** 2021-07-19, `866737179837333534`: "This is meant to be a fun trope. If you hate the idea. We can abandon it." 2021-07-20, `866777909787623465`: the airships-versus-Kong fight is canceled; the group has one armed ship and he will not be ready. 2021-07-22, `867566349278380042`: he is "going to (very obviously, I hope)" lie about removing penalty effects. 2021-07-26, `869309519640010852`: "My plan was to have them restored after my airship event," and another DM had run a ley-line repair. The message asks; it does not settle which plan won. 2021-07-31, `870902309830410300`: "I'm not going to let folks farm essence for 2 weeks and craft for two weeks." 2021-08-07, `873356284462768198`: Empire City is off limits for play; Kingsbridge and most of the city are on pause; the pause "is meant to be a break from the game for you too."

**Attendance.** 2021-08-19, `877727568147677214`: "There is a clear drop off in attendance. I want to talk about whether or not to wrap up in week four or continue on to week 5." The message is a question to the DM role, not a decision.

**A villain built to frustrate, for a later subclass.** 2021-08-23, `879231795567140874`: "The encounter was designed to be frustrating, because that particular villian is recurring but I wanted a set up for a warlock sub class for next year."

**He wants people actually to play.** 2021-07-16, `865472571772502036`: "you are my friend, and I want you to play." `865474003006128128`: "I am more likely to hand wave joining so that you can play." 2021-07-22, `867805010410864702`: he hopes more people write the walk through Manhattan "instead of just rolling damage and showing up."

**Neurodivergence, said to the table.** 2021-07-27, `869645913390448671`: more than half the server is neurodivergent; meta-gaming and theorycrafting are "some of the most gratifying things a dm can read," and newer players feel pressure when a choice is called suboptimal. He points them at server rule 1.

## Planning documents and comments

These are owner-attested containers or comments signed with his Drive name. Imperative bullets are plans he wrote down. They are not evidence the task was finished.

**BCS-000002, "Draft to do list," created 2021-01-07.** Make a calendar from the Kingsbridge Noir template so others can build a five-week game. Design the five main events. Schedule an all-hands. One-on-one meetings. Get World Anvil running, including a donation system. Art assets, maps. Economy with Rob. Items with Jack. Vehicles and people's houses.

**Crafting, repeated in BCS-000024 (Roanoke S2), BCS-000045 (Season 3 rough draft), and BCS-000080 ("Crafting, another attempt").** "I wanted to keep it very simple." Points per week or per day. "I still want to keep most totals under 7." "I would like to keep all dimensions under 7." "I want to keep crafting professions simple, and if I merge them, it could be too complicated." Profession text "about the same as a spell, or magic item."

**BCS-000052, Season 3 week 3 breakdown.** "The goal is to get to Roostloft."

**BCS-000174, Hampstead Module, modified 2021-07-16.** "The goal is to get the players to the secret basement, so let them explore some, but don't waste forever on red herrings and dead ends." Later: "Once they succeed the plan is they go to a landing pad, steal a ship and fly away."

**Comments on Roanoke planning docs, April–May 2020.**

- BCS-000085, 2020-04-18: "We need to edit this down and turn some of it into just straight lore dump. ... its just too long at the moment for a 1 page pdf."
- BCS-000076, 2020-04-20: he is "finalizing page one of each of the player races."
- BCS-000043: "design arcanian spell schools to be discoverable," so Detect Magic can show which effects "are not circumventable." Also: tying cp to rest is attractive "except that some one could stack short rests infinitely."
- BCS-000077, 2020-04-30: "Planed gold scarcity." He also writes that aristocrat bookkeeping may be his "weakest point of understanding."
- BCS-000079, 2020-04-25: cash as bank interest or a weekly stipend "to prevent vice from overwhelming the colony"; unchosen professions go to one NPC shop; "Week 3 common. Week 4 uncommon. Week 5 rare."
- BCS-000037: "I need the Hag coven to tell the party that Oleander knows where Hiram is hiding." That is a plot delivery he says he needs, not a claim the coven did it.
- BCS-000061 (*At War's End*): "This chapter needs more work. The action sequence isn't right yet." and "I need to add more of the soveld Spires army earlier in the story."
- BCS-000187, 2021-02-03: production notes — ferry-town script, a battle map, navigation checks, art of fins and spines.

**BCS-000145, "Season 5 character creation," dated 2023-04-29 in the catalog.** One line is first person and may be his: "In previous seasons I haven't taken part in any character creation, but this year I would like to take the time to understand the mechanics of your build." Neighboring lines in the same normalized file talk about "my npc" as an alchemist. This report does not decide that every row of that sheet is his.

## Recurrence, change, conflict, unresolved

These relationships are between statements. They are not a verdict.

**Recurs.** He keeps saying he does not want people ignored, and he keeps offering a queue when he cannot answer. He keeps a split in which most of the server is theirs and a smaller share is the story he is responsible for. He keeps asking for choice, and he also keeps naming rails, closed options, and pauses. He keeps tying rest, partner time, and mental health to the rules of play. He keeps inclusion language from Season 3 pronouns into the Season 4 hate-speech rule. He keeps crafting and tracking rules short on purpose (the 7s in the drafts; the arcane pouch "so that people wouldn't have to track minor things," message `865950355175243776`).

**Changes in his own wording.** Season 3, while London is running: a dark fairy tale, hints, a 35-day movie, pressure to protect. The August 2020 debrief, before Season 4 is built: competing DM stories made cliques; he wants one narrative and boroughs. July 2021: last year's hope was that people would band together; this year's hope is that they love themselves enough not to trade away who they are. July 2021, about a possible Season 5: a director's chair, not a DM character. February 2021, about the dating sim: it was never intended, it is staying, and the mechanics need an overhaul.

**Conflict inside the statements.** "I'm trying to leave you guys with choices" sits next to "i broke them so that option would be off the table." "I want you to win" and "I want you to live" sit next to deadly encounters and "I wont allow anymore shenanigan's." "It's always been my goal to try and retain people with kindness" sits next to "We didn't ask anyone to leave this year when maybe we should have." He wants to accommodate gangs and also does not want to rehash cliques. He says he was not trying to be controlling, and he also describes the ship as pressure meant to change the characters. "not meant to be exploreable" sits next to, near the end of Season 3, "I'd like to start encouraging more exploration."

**Not settled by the sentences that raise them.** Whether Season 4 wrapped in week 4 or went to week 5 (`877727568147677214`). Whether the dating-sim overhaul happened (`807799467339808768`). Whether the struck "destroy your tools" mechanic stayed struck (`745753934861303849`). Whether the airship-restoration plan or the other DM's ley-line event is the one that stood (`869309519640010852`). Whether the director's chair was later adopted. Whether "Planed gold scarcity" and the week-3/4/5 item rarity were the rules that reached the table. Whether private houses stayed barred after `863492563784040539`.

## Questions this pass does not answer

These are gaps in what was read, not guesses.

1. Which intentions from the January 2021 to-do list (BCS-000002) were later marked done, and in which revision?
2. Did any later message reverse the Season 3 rez-rule nerf, the tool-destruction strike, or the house ban?
3. Where, if anywhere, does he say what was decided about ending Season 4 in week 4?
4. Do the partial ChatGPT workbench snapshots (Earthfall, Saturday) contain aims that this lexical pass under-counted because the USER turns are short imperatives ("make it") rather than "I want"?
5. Which lines in mixed spreadsheets (BCS-000195, BCS-000145) are his and which are another writer's?
6. What did he intend in voice, in unharvested DMs, or in Drive revisions whose bodies were not fetched?
7. Do co-DM statements (Noah, Rob, Jack, Veronica, the DM role called DMD) contradict a plan he stated, in a message this pass did not attribute to him?

## What this is not

No score of how often players got what he hoped. No sorting of these sentences into a preference model. No instruction for Kit. Nothing here is approved for runtime. Promoting any of it into research guidance is a later decision, and it is not this file.
