import json, sys, subprocess
from pathlib import Path
H = Path('/workspace/kit-6c-rerun2/run/handoff')

def waiting_request():
    reply = Path((H / 'WAITING').read_text())
    return reply, json.loads(Path(str(reply).replace('.reply.json', '.request.json')).read_text())

NO_DETAIL = {"request": "none", "slot": "none", "choice": "none", "candidates": [], "typical": -1, "chosen": -1,
             "owner": "none", "handle": "none", "because": "none", "price_quote": [], "inventions": []}

def turn(*, segs, reply_to, objective, tactic, cue, opening, focus_txt, focus="uktarl", goal="npc_embodiment",
         move="npc_reply", scope="exchange", presence="brief", tone="curious", mode=None,
         mood=("neutral", "none"), mirror="steady energy, standard, no humor: answer what was said and hand the scene back",
         notice="none", bid="", anchor="level", basis="pressure_here", abasis="motive", connection="",
         choice="", label="interest", intensity=1, cause="", effect="advances", target="player",
         memory=None, callback="none", detail=None, extra=None):
    reply, req = waiting_request()
    pub = req['packet']['input']['public']
    if mode is None:
        ak=pub.get('action_kind'); mode = 'banter' if ak in ('social','social_check') else ('combat' if ak=='combat_round' else 'description')
    if req.get('previous_reply') and (req.get('rejection') or {}).get('decision_fixed'):
        dec = req['previous_reply']['decision']
    else:
        dec = {
         "observed_event": pub['accepted_public_event'], "goal": goal,
         "appraisal": {"label": label, "intensity": intensity, "cause": cause or bid, "goal_effect": effect, "target": target},
         "memory_refs": memory or [],
         "improv_read": {"player_bid": bid, "story_anchor": anchor, "story_basis": basis if anchor != 'none' else 'none',
                          "actor_ref": focus, "actor_basis": abasis if focus != 'none' else 'none',
                          "connection": connection, "kit_choice": choice},
         "move": move,
         "public_brief": {"objective": objective, "tactic": tactic, "visible_cue": cue, "player_opening": opening,
                          "reply_to": reply_to, "kit_focus": focus_txt, "callback": callback, "mirror": mirror,
                          "npc_notice": notice, "scope": scope},
         "focus_actor": focus, "table_presence": presence, "tone": tone,
         "player_note": {"note": "none", "evidence_turns": [], "replaces": "none"},
         "player_mood": {"read": mood[0], "cue": mood[1]}, "turn_mode": mode,
         "detail": detail or NO_DETAIL}
        if extra: dec.update(extra)
    perf = {"segments": [dict(speaker=s[0], text=s[1], **({"reacts_to": s[2]} if len(s) > 2 else {})) for s in segs]}
    Path('/tmp/draft.json').write_text(json.dumps({"decision": dec, "performance": perf}, ensure_ascii=False))
    r = subprocess.run([sys.executable, '/workspace/kit-6c-rerun2/dm/submit.py', str(H), '/tmp/draft.json'],
                       capture_output=True, text=True)
    print(r.stdout, r.stderr)
    log = Path('/workspace/kit-6c-rerun2/run.log').read_text().strip().splitlines()
    print('\n'.join(log[-2:]))
