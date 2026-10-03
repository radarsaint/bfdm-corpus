# V8: Deal me in, blackjack, and I'm betting fifty

PC: Wren (Human Rogue), sheet `example_pc.json`. DM backend: handoff. Times are wall-clock per turn (prepare + DM + complete).

## Opening (committed, 6.5s)

**Kit:**

> Narrator: Candle stubs gutter on a worn table just inside the door, where four pale figures in faded finery sit over cards and little towers of coin. The dealer's hand stops mid-deal. Three heads turn toward you; the fourth player keeps staring at the cards. Beyond them, a carved mountain covers the whole north wall, its tunnels crowded with tiny dwarves under spreading rays of sun, and below it a long stone tub is sunk into the floor. When the dealer speaks, his voice comes out raspy and slow, shaped by some far eastern country.
> Dealer: Ah, a visitor, at this hour, in this deep place. Come closer, into the candlelight, so we may see what the night has brought us. There is an empty chair, and the cards are always warm here, though little else is. Tell me, stranger, are you lost, or are you looking for a game?
> Kit: Do you answer him?

## Turn 1 (committed, 11.5s)

**Player:** I pull up a chair. 'Do you lot play blackjack? I don't know your fancy games.'

**Kit:**

> Narrator: The chair legs scrape and Wren drops into the empty seat. The dealer looks at her over his cards for a moment, then shrugs one elegant shoulder and squares the deck.
> Dealer: Blackjack. Yes, yes, we play it, though here we call it Twenty-One Coffins, because it sounds better by candlelight. Same game: get near twenty-one, never over, and beat the house. What will you stake, my plain-spoken guest?
> Kit: How much do you bet?

## Turn 2 (committed, 26.7s)

**Player:** 'I'll bet fifty gold.'

_Rejected 2x before commit: kit_focus sets how an NPC talks. Kit's direction may choose which tactic plays out, the pacing, and the framing; the NPC's words and humor come from their own c; Public text paraphrases a private fact (keyword set 'false_vampires'). Stay with what the player can perceive. Degraded mode is available for this turn. Resubmi_

**Kit:**

> Narrator: The most this table plays is 25 gp a round, so the bet is 25 gp. You want in. Two ways to play a round: settle it with one check, or play it out as twenty-one (blackjack), closest to 21 without going over. The stake is your 25 gp. Which way?
> Narrator: The fourth player whistles low. The dealer only smiles and taps the table twice with one long nail.
> Dealer: Fifty! A generous heart. Alas, this humble table tops out at twenty-five a hand, or the dead grow jealous of the living. Twenty-five it is, then. Shall I deal it out card by card, or will you settle the round on a single test of nerve?
> Kit: Twenty-five on the table. Card by card, or one check?

## Turn 3 (committed, 20.3s)

**Player:** 'Fine, twenty, and I'll play it out. Hit.'

_Rejected 1x before commit: Exchange scope: the Dealer spoke 29 words (floor 30). Answer the words in reply_to and let the actor pursue the brief tactic; do not pad with generic banter._

**Kit:**

> Narrator: Twenty-one, 20 gp a side. Your cards: 6 of diamonds and queen of spades, 16. The dealer shows the queen of hearts. You take the 8 of hearts: 24. Bust. You lose 20 gp to the house.
> Narrator: Twenty gold each goes into the middle. The dealer flicks her the six of diamonds and the queen of spades, and turns up his own queen of hearts. Wren taps for another: the eight of hearts lands on top. Twenty-four. Bust. The dealer rakes her twenty gold across the wood without a word, and the fresco-side player chuckles into his collar.
> Fresco-side player: The queen always comes for you.
> Dealer: Unkind of her, and so early in the evening. Twenty-one is a fickle mistress, my bold guest, but she rewards those who come back to her. Shall we try another round, and see whether she has forgiven you?
> Kit: You're down twenty. Another hand?

## Turn 4 (committed, 21.3s)

**Player:** 'Just roll for this one, I'm tired of counting.'
Wren makes a Sleight of Hand check! 1d20 (6) + 7 = `13`

_Rejected 1x before commit: NPC voice: the Fourth player ran 9 words in one sentence; their card's rhythm allows 8. Keep their clipped cadence._

**Kit:**

> Narrator: One round, 6 gp a side, settled on Insight. You lose 6 gp to the house.
> Narrator: Six gold a side this time, and no counting: the round comes down to reading the dealer across the table. Wren studies his face and finds nothing there she can trust. He turns his card, she turns hers, and the house takes six more gold. The fourth player leans back and laughs, a little too loudly.
> Fourth player: Tired of counting. Tired of winning too!
> Dealer: Hush. Our guest is having an unlucky night, and luck is a tide, my weary friend; it always turns. The cards will be here when you are rested, and so shall we. One more, or will you rest your eyes a while?
> Kit: You're down twenty-six. Another hand, or done for now?
