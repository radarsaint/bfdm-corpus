import sys; sys.path.insert(0,'.')
from runtime import kit_rolls as k
cases = {
 'persuasion_title': "Sela makes a Persuasion check! 1d20 (12) + 10 = `22`",
 'sleight_title': "Wren makes a Sleight of Hand check! 1d20 (6) + 7 = `13`",
 'plain': "Persuasion: 22",
 'atk_block': "Brakka attacks with a Greataxe!\n**To Hit**: 1d20 (11) + 7 = `18`\n**Damage**: 1d12 (5) + 6 [slashing] = `11`",
 'crit_block': "Brakka attacks with a Greataxe!\n**To Hit**: 1d20 (20) + 7 = `27`\n**Damage (CRIT!)**: 2d12 (5, 9) + 6 [slashing] = `20`",
 'fireball': "Nik casts Fireball!\n**Damage**: 8d6 (4, 3, 5, 2, 6, 1, 4, 3) [fire] = `28`",
 'firebolt': "Nik casts Fire Bolt!\n**To Hit**: 1d20 (12) + 7 = `19`\n**Damage**: 2d10 (4, 5) [fire] = `9`",
 'init': "**Initiative**: 1d20 (12) + 2 = `14`",
 'bet_with_roll': "I flip the deck face-down and show everyone the marks.\nWren makes an Investigation check! 1d20 (12) + 3 = `15`",
}
for n,t in cases.items():
    out={}
    for f in ('check_roll','stated_skill','initiative','attack_total','damage','damage_total','without_rolls','number_words'):
        try: out[f]=getattr(k,f)(t)
        except Exception as e: out[f]='ERR '+repr(e)
    try: out['avrae']=k.avrae(t)
    except Exception as e: out['avrae']='ERR '+repr(e)
    print('##',n); [print('  ',f,'=>',repr(v)[:200]) for f,v in out.items()]
