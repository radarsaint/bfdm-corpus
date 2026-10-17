# Bounded judgment tranche — 2026-10-15

This is one cross-case reading of primary records. It is not a model of how Brendon runs a game, not a frequency claim, and not Kit doctrine. The twenty Roanoke Season 3 decision cases merged in PR #38 (`2b68820d445e9f6d99d021463bfd76b2f7bb257d`) are a different sample. Their reusable judgments were overclaimed. This file does not promote them.

Draft PR #28 is a hypothesis map. Nothing here treats it as merged or as a gold label.

A current wish to add hindsight is not evidence that a 2020 or 2021 decision is now endorsed. Each case has `later_judgments: []`. Append a later judgment as a new object with its own source. Do not edit `historical` to make the past match the later view.

Statuses used here:

- `VERIFIED_NARROW` — the cited lines support this wording and not a wider rule.
- `NARROWED` — a familiar lesson was checked and does not survive at that width.
- `UNPROVEN` — the outcome, or the later season, is not in the evidence.
- `NOT_CONSUMED` — kept in the research record and not given to Kit.

Kit's runtime reads a smaller curated subset through `dnd-solo` `runtime/kit_judgment.py`. Presence in this file is not that consumption.

## BJ-001 — Unplanned repair

**Kind.** Positive adaptation.

**Historical.** On 2021-07-16 in Empire City admin chat, hekiryuu relays that a player asks to clear rubble at the money changer (`865565663296225280`). Brendon, `865565818481279018`: "I mean, I hadn't planned on it. But players helping rebuild the server is a healing thing." He agrees the player may post (`865565932783796255`), says "this has all the support" (`865566464831258674`), then "Don't worry I'm going to drive this narative" and "just waiting for his post" (`865567436970786836`). Hekiryuu later says the player posted without being prodded. Brendon agrees he saw the same.

**What is supported.** He allowed an unplanned repair he had not prepared, and he waited for the player's post rather than describing the result first. The next post in `#money-changer` is versil, 2021-07-16 12:28Z, `865570499333062677`: Roy starts moving the rubble. Brendon then narrates people joining that work (`865571955645874226`, `865572445783457832`). The same day at 23:09Z he writes "The money changer is now back to service the people of empire. The exchange rate is lowered to 3 %" (`865731824340566046`).

**What is not supported.** That every offer to build should be allowed. The housing refusal below is the counterexample. The admin chat says "V" and does not name versil; the sequence is the permission to post in that channel, then versil's post. The 3% rate is this reopening, not a rate for every shop. Kit card BJ-001 still stops at the admin chat.

**Status.** `VERIFIED_NARROW`. The evidence list stays the admin messages. The rebuild posts are follow-through.

## BJ-002 — Designed vulnerability kept

**Kind.** Counterexample. A creative request that removes a designed constraint.

**Historical.** `863492563784040539`, 2021-07-10, DM transparency log. Brendon pastes a player's ask for a spare bedroom above a restaurant and answers: "Sadly no, we aren't giving out houses this year. Your home is meant to be vulnerable and there is meant to be risk associated with. And if I give out one, a million others will ask for the same thing."

**What is supported.** He refused a private exception that would erase a vulnerability the season was using, and he named fairness across later asks.

**What is not supported.** A ban on every homeward detail, or on the rubble-clearing in BJ-001. A later grant of the spare room. This search did not find one.

**Follow-through.** The same night, 23:24Z, thatpersonlogan posts in `#the-vestige`, `863561461930655744`: the Vestige is a small airship, restaurant below, and Adon rents the top floor as a studio. No post of his in that channel answers the rental. His next post there, the next morning, `863675853232537601`, is a painted pigeon, not the room. The transparency log has no second entry granting the house.

**Status.** `VERIFIED_NARROW`. The evidence list stays the one log post. The rental is the player's later description, not his reversal and not his approval.

## BJ-003 — Resurrection corrected forward only

**Kind.** Correction of his own rule.

**Historical.** `744056939096571924`, 2020-08-15, Roanoke announcements: "I made a genuine mistake with my res rule. I'm going to have to nerf that ability for game balance reasons. Tonight's rez's still stand but the once per day rule can't stay in the game."

Before that post he scheduled the order: "Clover will res Viola, then percy, then abbadon" and "one hour per" (`744034814075600899`, `744034861823557694`). After the announcement, Percival's player narrates "Percival Gasps back to life" (`744064912656957481`). Viola's return is a player report from before the announcement (`744053132228558898`). Abbadon's return is not in these lines.

`BDC-S3-019` names no preparation locator. The merged review says none was added. This row cites the Discord messages.

**What is supported.** He called that rule a mistake, ended the once-per-day version going forward, and left that night's resurrections in place. The scheduled return of Percival is then played by the player. That is follow-through on the commitment, not a second ruling from him.

**What is not supported.** A policy for every failed house rule. The replacement rule's frequency, cost, or a later ruling that cites it. Later Revivify scroll use, which players were already asking for before this announcement. Kit card BJ-003 on dnd-solo #126 still describes only the announcement. This note does not change that card.

**Status.** `VERIFIED_NARROW`. The evidence list on the record stays the announcement. The schedule and the played return are follow-through, recorded here, and are not a wider status.

## BJ-004 — Prepared fight against the live party

**Kind.** Reconsideration, then a corrected read. Not a proven encounter change.

**Historical.** `746253583552479272`, 2020-08-21: "So 4 at depleted resources. My gut says don't take you into the preplanned fight." Eloise says Rockman and Copper are basically full. DCJJ says he is topped up. Web has one spell slot of each level. Brendon: "I could run this mostly rp" / "but only if thats satisfying." / "otherwise, I can throw mobs instead of bosses, but it will be too long for vee" (`746253900490735686`, `746254025883779113`, `746254092011175968`). Eloise wants some kind of fight (`746254154774872094`). He says "got it."

The v1 prep locator for this case is the broken BCS-000045 chain recorded by PR #38, now on main at `2b68820d`. The Discord lines above were read directly.

**What is supported.** He reconsidered a prepared boss from a gut read of the party, and he treated that offer as conditional on whether it would be satisfying. Players corrected the depleted read in the next lines. Eloise says they are meeting in the outskirts. He answers "got it" (`746254506500554762`). At 06:31Z in `hex-n-outskirts-of-new-roanoke` he writes "There is rustling in the woods behind you" (`746255033196216371`) and later "(escort quest accepted. escort flivver through leviathans call)" (`746257514823417897`). In `hex-b-leviathans-call` he then runs tooth fairies and a bear, including "The bear uses SHARKENFIST" (`746271322312802304`).

**What is not supported.** That this scene is the preplanned boss, or the mobs he offered instead. He does not say which. That "skip the prepared fight" is the lesson. Applying that simplification to a party the table says is fresh would contradict this window. Kit card BJ-004 still says the encounter after the window is not in the record.

**Status.** `NARROWED`. The scene after "got it" is these posts. Which fight it was remains unstated. The evidence list is unchanged.

## BJ-005 — Do not give the NPC a fact the table did not give

**Kind.** Correction of an AI draft. Not proof of play.

**Historical.** `sources/chatgpt-project-history/saturday-dnd/BCS-000172/source.md`. Brendon says the party missed the clues to Tasha's portfolio and proposes a way forward. The draft then has Neris realize they know the name Tasha. Brendon: "you are asuming they mentioned tasha. they didnt and they are just baricaded him in a room." The next draft drops that inference.

**What is supported.** He refused a draft in which the NPC acted on a name the players had not said. The next draft in the same file drops that inference: Neris does not know anything about Tasha and acts because they lied and barricaded him.

**What is not supported.** That the replacement draft was run at the table. The file is a partial project recovery. On August 8 he asks for a boss at "the end of the bank heist" while about to recover Tasha's documents. That says the heist had reached the vault. It does not quote the corrected Neris scene as played. No harvested Discord shard in this repo contains the token "neris". Kit card BJ-005 is unchanged.

**Status.** `VERIFIED_NARROW` for the correction of the draft. Table outcome of that correction: `UNPROVEN`.

## BJ-006 — Dating-sim apology

**Kind.** In-the-moment apology. Not a demonstrated change of practice.

**Historical.** `736688057113378928`, 2020-07-25, after he offered to write a dating-sim module and nut_wizard said the dating sim was the players' job: "right. sorry. player agency. I just get excited trying to accommodate." The next lines are jokes. No message in that window shows a module started or withdrawn. Draft PR #38 reached the same limit on BDC-S3-011. That review is now on main at `2b68820d`.

**Status.** The apology is `VERIFIED_NARROW`. Downstream change: `UNPROVEN`. `NOT_CONSUMED`. One apology is not a rule about accommodation.

## BJ-007 — Web's choice

**Kind.** He stops himself before choosing for a player.

**Historical.** `737569808396058654`, 2020-07-28, Golden Dawn: "(lets let web have some player agency I'm meta gaming and its a slippery slope)". He had just been shaping whether Web could be a witness. The following lines do not show the scene's result. The BDC-S3-013 review, now on main at `2b68820d`, is the same window.

**Status.** The self-stop is `VERIFIED_NARROW`. The scene after it: `UNPROVEN`. `NOT_CONSUMED`. It is not a general metagame policy.

## BJ-008 — Faction finale announced

**Kind.** Announced redesign. Success not shown.

**Historical.** `743967418824523836` states a theme of coming together as friends rather than through governance. `745737396804518020`, 2020-08-19, announces that two DMs becoming less active left a winner-take-all faction game, and that he and Noah are changing the ending so the town has a reason to work together. The announcement is not a finished finale. The BDC-S3-017 review, now on main at `2b68820d`, matches the announcement and does not show the finale being played.

**Status.** Announcement `VERIFIED_NARROW`. Successful finale: `UNPROVEN`. `NOT_CONSUMED`.

## BJ-009 — Tags instead of the manticore

**Kind.** Workbench, partial.

**Historical.** `sources/chatgpt-project-history/earthfall-live/BCS-000153/source.md`. He reports that the players are tagging themselves and trying to avoid the animatronic manticore combat, "which is good", and that he wants a puzzle so they can make it theirs, with some urgency. Later lines in the same partial log report coke on the manticore, a reboot command, and a natural 20 on an RFID machine. Assistant replies are missing. This is not a full transcript.

**Status.** `NARROWED`. `NOT_CONSUMED`. "Avoiding the fight was good" is his note about that room, not a rule for every combat.

## BJ-010 — Fryvern fizzle

**Kind.** Post-session self-report.

**Historical.** `BCS-000161`. "last session finished the fryvern fight. it ended in fizzle with the players being OP." He asks for a transition and for Rod to rant that it was too easy. `BCS-000156` is earlier Fryvern art direction, not the session. Both files are partial project recoveries.

**Status.** The disappointment is his own immediate report: `NARROWED`. The fight itself is not re-read from a transcript: `UNPROVEN`. `NOT_CONSUMED`.

## BJ-011 — Attendance, finale date, next season

**Kind.** Diagnosis, one announced correction, one unproven intention.

**Historical.** `877727568147677214` and `877728873230520370`, 2021-08-19: attendance has dropped, and 5–8 players a quest has killed events he planned. `877729415042322464`: not advertising was a mistake. `878397426619260968`: the finale moves to Wednesday because the late game was designed for more people; the server stays open for play. `879447556667633675`: he is starting the next-season server, will advertise, and will cut it to three weeks.

**Status.** The diagnosis and the moved finale are `VERIFIED_NARROW` as announcements. The next season's result: `UNPROVEN`. `NOT_CONSUMED`.

## What a runtime may consult

BJ-001, BJ-002, BJ-003, BJ-004, and BJ-005 are the only records eligible to be pinned. Eligibility is not injection. A player sentence does not establish the situation. BJ-004 does not order a fight to be run or skipped: the window does not show which encounter was played. The other records stay in this file so a rejected or unfinished reading is not deleted. Nothing here is a standing practice.
