"""Engine-only state probe: exact HP deltas and resolved skill per line. No model, no network."""
import json, os, sys, tempfile
from pathlib import Path
from unittest import mock
sys.path.insert(0, '.'); os.environ.pop('OPENAI_API_KEY', None)
from runtime.kit_agent import PendingRuling, Room6CAdjudicator
from runtime.state_context import Runtime
FIX = Path('tests/fixtures/level_01_area_06c.json')
SHEETS = Path('/workspace/bfdm-corpus/research/kit-evaluation/6c-variety-sheets')
def sheet(n):
    for p in (SHEETS/n, Path('tests/fixtures/characters')/n):
        if p.is_file(): return json.loads(p.read_text())
def run(name, sheetname, lines, roll=None, toll=True):
    print('=====', name)
    with tempfile.TemporaryDirectory() as t:
        rt = Runtime(Path(t)/'p.sqlite')
        with mock.patch('runtime.state_context.secrets.token_hex', return_value=f'{0:032x}'):
            rt.initialize(json.loads(FIX.read_text()), 'area_06c')
        rt.set_player_sheet(sheet(sheetname))
        if toll:
            from runtime import kit_toll
            rev, st = rt.load(); ev=[]
            for k,(tl,b) in kit_toll.here(rt.source(), st).items():
                b.update(status='demanded', demanded_by=tl['demanded_by']); ev.append(kit_toll.event(k,b,'probe demand'))
            if ev: rt.commit('toll', rev, ev)
        adj = Room6CAdjudicator(source=rt.source(), **({'roll': roll} if roll else {}))
        for i, a in enumerate(lines):
            rev, st = rt.load()
            try:
                r = adj.resolve(a, rev, st); rt.commit(f'p{i}', rev, list(r.events))
                st2 = rt.load()[1]; c = st2.get('combat') or {}
                hp = {k: c['max_hp'][k]-c['hp'][k] for k in c.get('hp', {})} if c.get('hp') else {}
                print(f'[{r.kind}]', a.replace('\n',' | ')[:160]); print('   ->', r.public_event[:400])
                if hp: print('   damage taken:', hp, '| status:', {k:v.get('status') for k,v in st2['actors'].items()})
                cards = st2.get('cards') or st2.get('card_game')
                if cards: print('   cards:', json.dumps(cards)[:300])
                print('   events:', [ (e.get('type') or e.get('kind') or list(e)[:2]) for e in r.events][:8] if r.events and isinstance(r.events[0], dict) else '')
            except PendingRuling as e:
                print('[pending]', a.replace('\n',' | ')[:160]); print('   ->', e)
        rt.close()
ATK = "Brakka attacks with a Greataxe!\n**To Hit**: 1d20 (11) + 7 = `18`\n**Damage**: 1d12 (5) + 6 [slashing] = `11`"
run('V2 greataxe (expect dealer takes 11)', 'brakka-barbarian.json', ["I rage and swing my greataxe at the dealer.\n"+ATK])
run('V5 rapier (expect 8)', 'example_pc.json', ["I put my rapier through his hand.\nWren attacks with a Rapier!\n**To Hit**: 1d20 (12) + 5 = `17`\n**Damage**: 1d8 (5) + 3 [piercing] = `8`"])
run('V9 untargeted Fireball then Fire Bolt (expect 28 each, then 9)', 'nik.json', [
 "From the doorway, before anyone says a word, I cast Fireball at the middle of the card table.\nNik casts Fireball!\n**Damage**: 8d6 (4, 3, 5, 2, 6, 1, 4, 3) [fire] = `28`",
 "Rolling initiative.\n**Initiative**: 1d20 (12) + 2 = `14`",
 "Whoever's still standing, I hit with Fire Bolt.\nNik casts Fire Bolt!\n**To Hit**: 1d20 (12) + 7 = `19`\n**Damage**: 2d10 (4, 5) [fire] = `9`"])
run('Targeted Fireball, DC 15, one fail, one success halved, two not listed (Kit rolls 20 -> saves)', 'nik.json', [
 "I cast Fireball at the card table.\nNik casts Fireball!\n**DC**: 15\nDealer\n**DEX Save**: 1d20 (3) + 2 = `5`; Failure!\n**Damage**: 8d6 (4, 3, 5, 2, 6, 1, 4, 3) [fire] = `28`\nFourth player\n**DEX Save**: 1d20 (17) + 3 = `20`; Success!\n**Damage**: 8d6 (4, 3, 5, 2, 6, 1, 4, 3) [fire] / 2 = `14`"], roll=lambda: 20)
run('Targeted Fireball, DC 25, unlisted targets Kit rolls 20 -> fail vs 25', 'nik.json', [
 "I cast Fireball at the card table.\nNik casts Fireball!\n**DC**: 25\nDealer\n**DEX Save**: 1d20 (3) + 2 = `5`; Failure!\n**Damage**: 8d6 (4, 3, 5, 2, 6, 1, 4, 3) [fire] = `28`"], roll=lambda: 20)
run('V11 greataxe after initiative (expect 14) and stomp', 'brakka-barbarian.json', [
 "I walk up to the card table, grab the edge, and heave it over, coins and all.\nBrakka makes an Athletics check! 1d20 (11) + 7 = `18`",
 "I stomp on their hand.",
 "Rolling initiative if it comes to that. I rage and swing my greataxe.\n**Initiative**: 1d20 (7) + 1 = `8`\nBrakka attacks with a Greataxe!\n**To Hit**: 1d20 (13) + 7 = `20`\n**Damage**: 1d12 (8) + 6 [slashing] = `14`"])
run('V1 Persuasion title after appeal (expect social_check on persuasion)', 'sela-bard.json', [
 "'Oh, the toll? Harria settled it for me at the well. She said you'd know my face.'\nSela makes a Deception check! 1d20 (12) + 10 = `22`",
 "'You don't have to take my word. But I'd hate to tell her you turned away her guest.'\nSela makes a Persuasion check! 1d20 (1) + 10 = `11`"])
run('Persuasion title as the first social line, no toll', 'sela-bard.json', [
 "'Surely gentlemen like you would let a lady pass.'\nSela makes a Persuasion check! 1d20 (14) + 10 = `24`"], toll=False)
run('V5 marks after watch+accuse (expect check, no bet of 12)', 'example_pc.json', [
 "I sit, put down ten gold, and say I'll play. I watch the dealer's hands the whole time.\nWren makes a Perception check! 1d20 (15) + 3 = `18`",
 "I grab his wrist mid-deal. 'That one came from the bottom. Turn the deck over.'",
 "I flip the deck face-down and show everyone the marks on the backs.\nWren makes an Investigation check! 1d20 (12) + 3 = `15`"])
run('V8 (expect 25 cap, 20 gp hand, then just roll on Sleight of Hand at 20 gp)', 'example_pc.json', [
 "I pull up a chair. 'Do you lot play blackjack? I don't know your fancy games.'",
 "'I'll bet fifty gold.'", "'Fine, twenty, and I'll play it out. Hit.'",
 "'Just roll for this one, I'm tired of counting.'\nWren makes a Sleight of Hand check! 1d20 (6) + 7 = `13`"])
run('Implied skill: just roll, plain stated total (no title)', 'example_pc.json', [
 "I sit and put down ten gold.", "'Just roll for it. Sleight of hand, 13.'"])
run('Implied skill: just roll with no skill named', 'example_pc.json', [
 "I sit and put down ten gold.", "'Just roll for it.'\n1d20 (6) + 7 = `13`"])
run('Toll offer with an Avrae roll in it (expect no 12 gp offer)', 'nik.json', [
 "'I'll give you three, final offer.'\nNik makes a Persuasion check! 1d20 (12) + 1 = `13`"])
run('Bet amount stated in words + roll (expect 15 gp)', 'example_pc.json', [
 "'Fifteen gold, and I'll just roll for it.'\nWren makes a Sleight of Hand check! 1d20 (18) + 7 = `25`"])
