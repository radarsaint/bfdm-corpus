exec(open('/workspace/kit-6c-rerun2/probes/state_probe.py').read().split("ATK = ")[0])
run('Targeted Fireball: Fourth player listed as failing, Kit roll 20 (expect doppelganger 28)', 'nik.json', [
 "I cast Fireball at the card table.\nNik casts Fireball!\n**DC**: 15\nFourth player\n**DEX Save**: 1d20 (2) + 3 = `5`; Failure!\n**Damage**: 8d6 (4, 3, 5, 2, 6, 1, 4, 3) [fire] = `28`\nDealer\n**DEX Save**: 1d20 (19) + 2 = `21`; Success!\n**Damage**: 8d6 (4, 3, 5, 2, 6, 1, 4, 3) [fire] / 2 = `14`"], roll=lambda: 20)
run('Card context: just roll, skill named in words, plain total', 'example_pc.json', [
 "'I'll bet ten gold.'", "'Just roll for it. Sleight of hand, 13.'"])
run('Card context: just roll, bare Avrae line, no skill', 'example_pc.json', [
 "'I'll bet ten gold.'", "'Just roll for it.'\n1d20 (6) + 7 = `13`"])
run('Card context: just roll, implied skill (palming)', 'example_pc.json', [
 "'I'll bet ten gold.'", "'Just roll it, I'll palm a card if I have to.'\n1d20 (6) + 7 = `13`"])
run('Card context: bet in words + roll title (expect 15 gp, not 18/25)', 'example_pc.json', [
 "'Deal me in.'", "'Fifteen gold, and I'll just roll for it.'\nWren makes a Sleight of Hand check! 1d20 (18) + 7 = `25`"])
run('Bet with Avrae roll only, no amount (expect house 10, not 18)', 'example_pc.json', [
 "'Deal me in.'", "'Just roll it.'\nWren makes a Sleight of Hand check! 1d20 (18) + 7 = `25`"])
