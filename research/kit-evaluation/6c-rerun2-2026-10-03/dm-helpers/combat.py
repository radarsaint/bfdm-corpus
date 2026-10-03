"""Combat-turn helper: turn_mode combat, tight mirror, short beats."""
import sys
from kitlib import turn
def fight(narr, line, kit, react, reply_to, bid, cue, opening='Roll initiative, or act.', focus='uktarl', speaker='Dealer', **kw):
    segs = [('Narrator', narr), (speaker, line), ('Kit', kit, react)]
    args = dict(segs=segs, reply_to=reply_to,
        objective=kw.pop('objective', 'Survive the fight without taking more risk himself.'),
        tactic=kw.pop('tactic', 'Shout the others forward while he backs away.'),
        cue=cue, opening=opening,
        focus_txt=kw.pop('focus_txt', 'Short, physical beats: the blow, the room erupting, then initiative.'),
        focus=focus, bid=bid,
        connection=kw.pop('connection', 'Uktarl avoids personal risk; once blood is drawn he pushes the others in front of him.'),
        choice=kw.pop('choice', 'Kit narrates only what the table resolved and hands the fight back.'),
        move='npc_reply', abasis='immediate_goal', mood=kw.pop('mood', ('tense', reply_to[:30])),
        mirror='high energy, tight, no humor: fast and physical', tone='threatening', label='concern', intensity=2,
        cause=kw.pop('cause', 'The PC draws blood.'), effect='threatens', mode='combat')
    args.update(kw)
    turn(**args)
