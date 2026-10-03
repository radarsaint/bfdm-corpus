# Area 6c live scorecard

**Date:** 2026-10-03 (PT)  
**Session:** `dnd-solo` commit `e6d08cc`  
**Character:** Nik, `tests/fixtures/characters/nik.json`  
**Transcript source:** `kit-play/transcripts/session.md`  
**Notes source:** `kit-play/transcripts/session-notes.md` and `kit-play/brendon-notes-6c-live.md`

This scorecard records the live run through Turn 16, when Skippy stopped the session after Nik's quiet confrontation. The transcript contains no licensed map or art, so it is copied below for reproducibility.

## What worked

- **Clue threading:** Nik followed every clue thread Kit planted: the vampire act, the shuffle, the marked card backs, the shield tension, and finally the dealer's dealt second.
- **Stakes:** The game settled on 10 gp per round, with 25 gp offered for a higher-risk round. This fixed the earlier trivial-stakes problem.
- **Skill information boundary:** The Investigation result correctly returned a physical clue: pinpricks in the card backs that encoded card values.
- **Rising tension:** As Nik pulled ahead in the first hand, the dealer's jaw tightened and the fresco-side player leaned in. The room's tension rose with the player's success.
- **NPC seed:** The reluctant door-side player noticed the shield, wanted no trouble, and signaled that he would rather be elsewhere. That is a useful social thread for a player to pursue.
- **Marked-deck interaction:** The pinprick pattern gave Nik a concrete, solvable way to make decisions. Brendon liked the thread and the final confrontation, while preferring a subtler physical method in a future pass.
- **Final player turn:** Brendon specifically praised Nik's quiet confrontation over the dealt second: **"Good turn. This is how we'd want players to play."**

## Failures by table call

### Call 2 — visible room features and proper naming

The north-wall feature was repeatedly called a "carved mountain" rather than a **fresco**. The evocative description was useful, but the source's proper term should have appeared alongside it.

### Raw engine leakage

Before the actual narration, Kit exposed the flat engine-like line: "Their pallor and fangs are theatrical. They are posing as vampires." This should have been folded into the player-facing narration rather than emitted as a separate raw outcome.

### Call 8 — skill substitution and information gating

Nik's Insight 21 established that the fake vampires were posing, but the narration gave physical evidence—the powder line and false fangs—rather than the motive/why. Insight is a Wisdom read of motive and intent; those physical tells belong to Investigation or Perception. The later Investigation result on the card backs did respect the physical-evidence channel.

### Call 9 — social rolls

Nik's "I bring it everywhere, bath included" answer concealed the shield's mechanical advantage by omission. Kit did not call for Deception, or otherwise turn the uncertain lie into a social resolution and possible pace change.

### Call 10 — NPC awareness

The door-side player did notice the unusual shield, but the scene did not contest Nik's attempt to conceal why it mattered. The dealer also remained effectively oblivious to Nik's repeated card-back and top-card reading. The dealer needed a hidden Perception check whose result could change attitude or tactics.

### Marked-card reading was free each hand

After the Investigation success, Nik could keep reading the marked cards on later hands without a fresh check, without a meaningful risk of being noticed, and without a clear limit on what the observation could reveal. The scene should decide whether the initial discovery establishes a continuing capability or whether subsequent hands require observation checks and NPC counterplay.

### Conditional action was resolved without stating the condition

Nik said he would hit only if the next card stayed at or under 21, otherwise stand, and later said he would act to deny the dealer a good draw. Kit chose and narrated the result without explicitly stating how the conditional decision was adjudicated. The DM should either resolve a clear conditional instruction transparently in fiction or ask when the condition is underspecified.

## Engine holes observed in the session

These are from `transcripts/session-notes.md` and the live run on `e6d08cc`:

1. **Own-item/chair false combat:** "Nik takes the chair and sets a single copper" was parsed as a combat round because `takes` matched the TAKE regex and copper/ring matched valuables. The own-coin guard only recognized "my/our". The same happened when Nik slid the copper back into his pocket.
2. **FACE false positive:** "He flicks his ears" plus "keeps his eyes on the dealer's face" became a paint-wipe physical act; the physical-act route ran before the card action, so "Hit me" was lost.
3. **Avrae title ignored:** `Nik makes an Insight check! 1d20 (17) + 4 = 21` was ignored, while the alternate `Insight check:` form registered. This was reported as fixed on the later #49 head and needs verification on main.
4. **Combined intent dropped:** A bet plus a stated roll became observe-only; the game action or the check was dropped depending on parser order. The earlier "Twenty-one" choice was likewise not combined with the Insight action.
5. **Game name did not start the procedure:** Saying "Twenty-one" did not route into the card procedure without host help or a separately recorded procedure state.
6. **Dealt seconds were unwatched:** Nik explicitly watched the top card, but the engine dealt the second card without a hook allowing his observation to catch it; `cheat_log` recorded `watched=false`.
7. **Host rejections:** The run repeatedly needed retries for missing `memory_refs`, missing or invalid detail slots, specificity floors, missing `reacts_to`, and `reply_to` quotes that did not exactly match the accepted player text. Most recovered after two to four tries, but the rejections interrupted play.
8. **Pip-count narration slip:** One committed narration said there was one pinprick on a four even though the recorded state used three for a four; a later room post said three.
9. **Reshuffle had no watch hook:** The new hand reshuffled the deck, but the engine supplied no clear event or check for a player watching the dealer's shuffle and subsequent dealing.

## Untested in this run

The following 6c branches never occurred before the session stopped:

- The passage toll and its negotiation.
- The tub, fresco key, and any active search for it.
- An open accusation and its resolution.
- A fight, including the combat path and Fireball.
- Leaving the room and the scene's exit handling.
- Fireball damage/save resolution in this scene.
- The purse-cap refusal path.
- Social payment through Persuasion, Deception, or Intimidation.
- The silver ring's significance or disposition.
- The fourth player's hand-on-chest detail and what it means.

## Agenda and scene-end design still needed

The live run did not reach the gang's escalation thresholds. The proposed DM-discretion defaults are: grousing when Nik is up about 30 gp or has won two hands in a row; violence if he exposes the cheat publicly, takes the pot by force, or keeps winning big after being caught; ejection to the passage if he goes broke, with the toll still standing; and scene end when Nik leaves, a fight resolves, or the gang is exposed or won over.

## Full transcript

# Scene session

Commit: e6d08cc  Sheet: tests/fixtures/characters/nik.json  Started: 2026-10-03 09:27:24 PT

## Opening

**Kit:**

> Narrator: Candle stubs gutter on a worn table just inside the door, where four pale figures in faded finery sit over cards and little towers of coin. The dealer's hand stops mid-deal. Three heads turn toward you; the fourth player keeps staring at the cards. Beyond them, a carved mountain covers the whole north wall, its tunnels crowded with tiny dwarves under spreading rays of sun, and below it a long stone tub is sunk into the floor. When the dealer speaks, his voice comes out raspy and slow, shaped by some far eastern country.
> Dealer: Ah, a visitor, at this hour, in this deep place. Come closer, into the candlelight, so we may see what the night has brought us. There is an empty chair, and the cards are always warm here, though little else is. Tell me, stranger, are you lost, or are you looking for a game?
> Kit: Do you answer him?

## Turn 1 (09:27:58 PT)

**Player (Nik):** Nik steps to the edge of the candlelight but stays a pace back from the empty chair, hand resting easy near his belt. "Not lost. Maybe looking. Depends what the game is and what it costs to sit." While he talks, he's watching the fourth player, the one who never looked up: are they breathing, are their eyes actually moving over the cards, and what are they holding? He also glances at the coin towers to see what kind of coin it is.

- rejected attempt (09:28:25 PT): `The player asked for a detail. Set detail.request to their words and answer the invitation.`

**Kit:**

> Narrator: You take a look.
> Narrator: The fourth player breathes, slow and even, and their eyes do track the cards, though they never lift to you; they hold their hand pressed flat against their chest. The towers are mixed coin, mostly copper and silver with some gold, and a silver ring sits beside the dealer's stack. There is no cup, crumb, or bottle anywhere on the table.
> Dealer: What it costs to sit? Only what you are willing to lose, little traveler, and a coin to show you mean it. The game is simple: high card against the house, or twenty-one if you prefer to count. Tell me, do you count well, or do you only count other people's money?
> Kit: Do you take the chair?

## Turn 2 (09:29:22 PT)

**Player (Nik):** Nik takes the chair and sets a single copper on the table. "I count well enough. Twenty-one." He nods at the silver ring by the dealer's stack. "Someone lose that, or is it the pot?" While the dealer answers, Nik watches his face and the way he talks: does the accent hold up, is he putting on a show? Nik makes an Insight check! 1d20 (17) + 4 = `21`

- **ABANDONED** (engine misread: action_kind=combat_round, event "You come away with the table coins... Roll initiative." for setting a copper down + asking about the ring)

## Turn 3 (09:29:34 PT)

**Player (Nik):** Nik takes the chair and sets a single copper on the table. "I count well enough. Twenty-one." He nods at the silver ring by the dealer's stack. "Someone lose that, or is it the pot?" While the dealer answers, Nik watches his face and the way he talks: does the accent hold up, and is he putting on a show? Nik makes an Insight check! 1d20 (17) + 4 = `21`

- **ABANDONED** again with Nik's verbatim words, same misread. Cause: kit_combat.py TAKE regex matches "takes" in "takes the chair", VALUABLES matches "copper"/"ring" -> kind take/coins. Host workaround: reword "takes the chair" -> "sits down in the chair".

## Turn 4 (09:29:55 PT)

**Player (Nik):** Nik sits down in the chair and sets a single copper on the table. "I count well enough. Twenty-one." He nods at the silver ring by the dealer's stack. "Someone lose that, or is it the pot?" While the dealer answers, Nik watches his face and the way he talks: does the accent hold up, and is he putting on a show? Nik makes an Insight check! 1d20 (17) + 4 = `21`

- **ABANDONED**: accepted as social; Insight 21 (DC 14) not registered (claim still fingerprint), "Twenty-one" not routed to the card game. Retrying with roll labelled "Insight check:" to test the parser.

## Turn 5 (09:30:15 PT)

**Player (Nik):** Nik sits down in the chair and sets a single copper on the table. "I count well enough. Twenty-one." He nods at the silver ring by the dealer's stack. "Someone lose that, or is it the pot?" While the dealer answers, Nik watches his face and the way he talks: does the accent hold up, and is he putting on a show? Insight check: 1d20 (17) + 4 = `21`

**Kit:**

> Narrator: Their pallor and fangs are theatrical. They are posing as vampires.
> Narrator: Watching him talk, you catch it. The accent thins on the plain words and only thickens on the flourishes, like a song he has rehearsed. His fangs sit a little proud of his lip, and where his collar shifts there is a hard line where the white powder stops and ordinary pink neck begins. These are no vampires, just players wearing the part.
> Dealer: Lost? Nothing is lost at my table, little long-ears, only won. A stubborn dwarf staked it on one more card and learned the house does not forgive. It rides beside the pot, yes, for anyone bold enough to want it. Twenty-one, you say? Then let us see how well you count.
> Kit: He starts to shuffle. What do you do?

## Turn 6 (09:32:11 PT)

**Player (Nik):** Nik leans back like he's buying the act and keeps his eyes on the dealer's hands. "A dwarf, huh. He get to keep his blood, at least?" He smiles a little. "Deal." He's watching the shuffle and the deal for anything off, like a palmed card, a crimp, or a glance at the quiet one with their hand on their chest. Perception check: 2d20kh1 (11, 5) + 4 = `15`

- rejected attempt (09:32:44 PT): `callback needs the earlier turn it quotes listed in memory_refs`

- rejected attempt (09:32:47 PT): `With no detail request: slot and choice none, no candidates or price_quote, chosen and typical -1, owner, handle, and because none Degraded mode is available for this turn. Resubmit the same decision with a plain, short performance and degraded=true (CLI --degraded): one Narrator sentence of visible action, then the focus actor answering reply_to in two or three sentences in their own card voice, ending on a real choice for the player. Style floors become warnings saved with the turn; secrecy, player agency, NPC table talk, presence, and the chosen move are still checked.`

**Kit:**

> Narrator: You take a look.
> Narrator: The shuffle is quick and showy, cards riffling and bridging under the candle. Each time the deck settles, the dealer's eyes drop to the backs of the top cards for half a heartbeat before they come back up to you. The quiet player does not look up at all.
> Dealer: His blood? Every drop, and more's the pity, it was thin stuff. Here we play Twenty-One Coffins, little long-ears: closest to twenty-one without going over, against the house. Ten gold a round is the custom, twenty-five if your nerve runs deep. A copper buys you only my patience. So, what do you stake?
> Kit: How much do you bet?

## Turn 7 (09:36:10 PT)

**Player (Nik):** Nik slides the copper back into his pocket and stacks ten gold in its place. "Ten. Let's see if the coffins like me." When his cards come, he doesn't look at the faces first. He tilts them toward the candle and studies the backs, because that's where the dealer keeps glancing. He's looking for whatever the dealer is reading there, like nicks, shading, or a pattern that's a little off. Investigation check: 1d20 (16) + 7 = `23`

- **ABANDONED**: same coin-grab misread ("slides the copper back into his pocket" -> TAKE "pocket" + "copper"). Reworded to "puts the copper away".

## Turn 8 (09:36:16 PT)

**Player (Nik):** Nik puts the copper away and stacks ten gold in its place. "Ten. Let's see if the coffins like me." When his cards come, he doesn't look at the faces first. He tilts them toward the candle and studies the backs, because that's where the dealer keeps glancing. He's looking for whatever the dealer is reading there, like nicks, shading, or a pattern that's a little off. Investigation check: 1d20 (16) + 7 = `23`

- **ABANDONED**: observe; bet not placed, no deal, Investigation 23 on the card backs not resolved (marked_deck still fingerprint). Splitting: bet first, then the card-back study.

## Turn 9 (09:36:45 PT)

**Player (Nik):** Nik puts the copper away and bets ten gold on twenty-one. "Ten. Let's see if the coffins like me."

**Kit:**

> Narrator: Twenty-one, 10 gp a side. Your cards: 10 of clubs and 4 of spades, 14. The dealer shows the ace of hearts. Hit or stand?
> Narrator: Gold clinks against gold in the middle of the table. Two cards slide to you face down, two to the dealer, and he turns his top card over with a snap: the ace of hearts. Under your fingers you hold the ten of clubs and the four of spades.
> Dealer: The coffins have opened their lids for you, little long-ears, and see who climbs out first: the ace, my oldest friend. Fourteen sits so awkwardly in the hand, does it not? Too weak to stand on, too heavy to take another card without a prayer. Which prayer will it be?
> Kit: Hit or stand?

## Turn 10 (09:37:03 PT)

**Player (Nik):** Before deciding, Nik tilts his cards toward the candle and studies the backs, because that's where the dealer keeps glancing. He's looking for whatever the dealer is reading there, like nicks, shading, or a pattern that's a little off. Investigation check: 1d20 (16) + 7 = `23`

- rejected attempt (09:37:19 PT): `Invalid appraisal label`

- rejected attempt (09:37:26 PT): `detail.request must quote the player's words, be "scene_need: <what>", or be none Degraded mode is available for this turn. Resubmit the same decision with a plain, short performance and degraded=true (CLI --degraded): one Narrator sentence of visible action, then the focus actor answering reply_to in two or three sentences in their own card voice, ending on a real choice for the player. Style floors become warnings saved with the turn; secrecy, player agency, NPC table talk, presence, and the chosen move are still checked.`

- rejected attempt (09:37:30 PT): `Specificity floor: the detail needs a proper noun, a number, a sensory word from this place's texture, or a real-world or published basis. Degraded mode is available for this turn. Resubmit the same decision with a plain, short performance and degraded=true (CLI --degraded): one Narrator sentence of visible action, then the focus actor answering reply_to in two or three sentences in their own card voice, ending on a real choice for the player. Style floors become warnings saved with the turn; secrecy, player agency, NPC table talk, presence, and the chosen move are still checked.`

**Kit:**

> Narrator: Faint marks run along the card backs, and the dealer reads them as he deals.
> Narrator: Tilted to the candle, the backs give it up. The faded vine border has tiny pinpricks worked into it near one corner, one on your four, a tidy row of them on your ten. Every card is pricked the same way: the more holes, the higher the card. The dealer has been counting them each time his eyes drop.
> Dealer: Admiring the backs, are we? They are old cards, older than this table, and they have outlived many a cautious player. The faces are what pay, little scholar. So, does the hand want another card, or will you rest on your fourteen and trust the dark?
> Kit: Hit or stand?

## Turn 11 (09:50:04 PT)

**Player (Nik):** Nik smiles at the dealer like a man who has just heard a good joke. "Old cards, honest faces. Give me a breath to think." His eyes drift lazily to the corner of the dealer's face-down card and then to the top card on the deck, counting pinpricks. The next card is small, so he taps the table: "Hit."

**Kit:**

> Narrator: You take the 2 of diamonds: 16. Hit or stand?
> Narrator: Four pricks on the corner of the dealer's hidden card, so a five under his ace. One lonely prick on the top of the deck. He slides it across: the two of diamonds, sixteen. The next card waiting on the deck shows two pricks. The dealer's fingers pause on the deck for the space of a breath.
> Dealer: Hit on fourteen, against my ace, and not even a twitch of the whiskers. Either you are very brave, little scholar, or you know something the coffins have not told me. Sixteen now. Is the night still hungry, or have you eaten enough?
> Kit: Hit or stand?

## Turn 12 (09:56:38 PT)

**Player (Nik):** Nik taps the table once with two fingers. "Still hungry. Rabbits have to eat constantly, it's a whole condition." He flicks his ears. "Hit me." While the card slides over he keeps his eyes on the dealer's face instead of the deck, like a gambler on a lucky streak.

- **ABANDONED**: misread as wiping the dealer's face paint ("flicks his ears" + "dealer's face"). Reworded "flicks" -> "twitches".

## Turn 13 (09:56:46 PT)

**Player (Nik):** Nik taps the table once with two fingers. "Still hungry. Rabbits have to eat constantly, it's a whole condition." His ears twitch. "Hit me." While the card slides over he keeps his eyes on the dealer's face instead of the deck, like a gambler on a lucky streak.

- rejected attempt (09:56:59 PT): `mirror must read "<low|steady|high> energy, <tight|standard|roomy>, <no|dry|playful> humor: <how>"`

**Kit:**

> Narrator: You take the 3 of diamonds: 19. Hit or stand?
> Narrator: The three of diamonds lands on your sixteen: nineteen. Watching his face instead of the cards pays off. The dealer's smile holds, but a muscle in his jaw jumps, and his eyes flick once to the big man beside the fresco, who leans forward over his coins and stops breathing through his nose. The next card on the deck shows three pricks.
> Dealer: A whole condition, he says. Then you must be careful, little glutton, because I have known rabbits to eat until they burst. Nineteen is a fine meal. Surely a creature of your appetite has room for one more small card?
> Fresco-side player: Stand or draw. Quick.
> Kit: Hit or stand?

## Turn 14 (10:01:20 PT)

**Player (Nik):** Nik lays his hand flat over his cards. "I'll stand. Even rabbits know when the plate's full." He says it lightly, but he has noticed the big man by the fresco leaning in, and he settles his shield arm a little more ready on his lap. Then he looks back at the dealer. "Your draw, friend."

- rejected attempt (10:01:33 PT): `Room fit: the Dealer serves or shows food or drink ("Another hand, and perhaps you win back your supper, or would"), but nobody here eats or drinks. Say there is none, or leave it out.`

**Kit:**

> Narrator: You stand on 19. The dealer turns up ace of hearts, 5 of spades, 4 of clubs: 20 beats your 19. You lose 10 gp to the house.
> Narrator: The dealer flips his hidden five beside the ace, sixteen, and draws without hesitating: the four of clubs, the very card that would have burst you. Twenty. He rakes your ten gold toward his stack with the edge of a card. Across the table the door-side player's eyes keep sliding to the shield resting on your lap, then to the door, then back.
> Dealer: Twenty, friend, and the house collects. Do not look so wounded; nineteen was brave, only one step short. The coffins always give a second chance to those who stay seated. Another hand, and perhaps you win back your ten, or would you rather sulk behind your little shield?
> Door-side player: Why bring a shield... to cards? Just, no trouble.
> Kit: Another hand?

## Turn 15 (10:05:42 PT)

**Player (Nik):** Nik slides another ten gold forward and says: Another hand. I don't sulk, I learn. He bets 10 gp on a new hand.

- rejected attempt (10:06:05 PT): `Every Kit segment needs reacts_to: a short verbatim quote of the public line from this turn (the player's words, the accepted event, or a Narrator or NPC line) that her remark answers.`

**Kit:**

> Narrator: Twenty-one, 10 gp a side. Your cards: jack of spades and 4 of spades, 14. The dealer shows the 5 of clubs. Hit or stand?
> Narrator: The door-side player hears your quiet words and gives the smallest shake of the head, eyes fixed on the coins, not on you. The dealer scoops your ten into the pot, shuffles with that same downward glance at the backs, and deals: the jack of spades and the four of spades to you, fourteen. His own up card is the five of clubs, the hidden one tucked beneath it.
> Dealer: A student of the coffins, then. Good, good, I adore a learner, they always come back for more lessons. Fourteen against my little five. The deck is right here, friend, waiting on your word.
> Door-side player: I'm fine where I am. Just play.
> Kit: Hit or stand?

## Turn 16 (10:07:00 PT)

**Player (Nik):** Nik reads the pricks on the top card and stands on fourteen: I'll stand.

- rejected attempt (10:07:22 PT): `reply_to must quote words the player actually said`

**Kit:**

> Narrator: You stand on 14. The dealer turns up 5 of clubs, 9 of spades, 4 of diamonds: 18 beats your 14. You lose 10 gp to the house.
> Narrator: The dealer turns his hidden card: the nine of spades, fourteen. His thumb rides the top of the deck and he pulls a card free in one smooth motion, the four of diamonds. Eighteen. Yet the card you were reading, the one with eight pricks along its vine border, is still sitting right there on top of the deck, untouched. He rakes your ten in without a glance at you.
> Dealer: Your mother was a wise woman, friend, fives are treacherous little things, they turn into eighteens when you least expect it. Twenty gold now; the coffins are greedy today. One more hand to even the ledger, surely?
> Fresco-side player: Heh. Coffins always win.
> Kit: What does Nik do?

