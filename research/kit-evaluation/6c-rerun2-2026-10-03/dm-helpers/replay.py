"""Reuse the previous rerun's committed DM reply for the same scenario/step when the engine read
is unchanged (same public event). Otherwise print old vs new so the reply is rewritten by hand.
usage: replay.py [--force]"""
import json, sys, subprocess, glob
from pathlib import Path
H = Path('/workspace/kit-6c-rerun2/run/handoff')
OLD = Path('/workspace/bfdm-corpus/research/kit-evaluation/6c-rerun-2026-10-03/runs')
reply = Path((H/'WAITING').read_text()); sid = reply.parent.name; step = int(reply.name.split('.')[0])
req = json.loads(Path(str(reply).replace('.reply.json', '.request.json')).read_text())
pub = req['packet']['input']['public']; pr = req['packet']['input']['private']
ev = pub['accepted_public_event']
old_turns = [json.loads(l) for l in open(OLD/sid/'turns.jsonl')]
old = next((t for t in old_turns if t['step'] == step), None)
old_ev = (old or {}).get('result_excerpt', {}).get('public_event') if old else None
files = sorted(glob.glob(str(OLD/sid/'dm-replies'/f'reply-{step:02d}-a*.json')))
print(sid, step, 'attempt', reply.name, '| kind:', pub.get('action_kind'), '| old kind:', (old or {}).get('action_kind'), '| old outcome:', (old or {}).get('outcome'))
print('PLAYER:', pr.get('player_action'))
print('NEW EVENT:', ev)
if req.get('rejection'): print('REJECTION:', json.dumps({k:v for k,v in req['rejection'].items() if k not in ('host_retry','degraded_instruction')})[:1500])
same = old_ev == ev and files and (old or {}).get('outcome') == 'committed'
if not same and '--force' not in sys.argv:
    print('OLD EVENT:', old_ev); print('OLD SPOKEN:', (old or {}).get('spoken', '')[:1500]); sys.exit(2)
d = json.loads(Path(files[-1]).read_text())
d['decision']['observed_event'] = ev
Path('/tmp/draft.json').write_text(json.dumps(d, ensure_ascii=False))
r = subprocess.run([sys.executable, str(Path(__file__).parent/'submit.py'), str(H), '/tmp/draft.json'], capture_output=True, text=True)
print(r.stdout, r.stderr); print(Path('/workspace/kit-6c-rerun2/run.log').read_text().strip().splitlines()[-1])
sys.exit(r.returncode)
