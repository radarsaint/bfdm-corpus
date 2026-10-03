"""Schema-check a draft, dry-run `complete` on a COPY of the scenario's kit.sqlite, and hand it in
only if the dry run commits (or --force). usage: submit.py <handoff_dir> <draft.json> [--force]"""
import json, sys, time, shutil, sqlite3, subprocess, os
from pathlib import Path
import jsonschema
h = Path(sys.argv[1]); draft = json.loads(Path(sys.argv[2]).read_text())
reply = Path((h / 'WAITING').read_text())
req = json.loads(Path(str(reply).replace('.reply.json', '.request.json')).read_text())
errs = sorted(jsonschema.Draft202012Validator(req['packet']['schema']).iter_errors(draft), key=str)
if errs:
    for e in errs[:8]: print('SCHEMA:', list(e.path), e.message[:200])
    sys.exit(1)
db = h.parent / reply.parent.name / 'kit.sqlite'
shutil.copy(db, '/tmp/dry.sqlite')
tid = sqlite3.connect('/tmp/dry.sqlite').execute('select turn_id from kit_pending').fetchone()[0]
env = {k: v for k, v in os.environ.items() if k != 'OPENAI_API_KEY'}
r = subprocess.run([sys.executable, '-m', 'runtime.kit_agent', 'complete', '--db', '/tmp/dry.sqlite', '--turn-id', tid,
                    '--input-file', sys.argv[2]], capture_output=True, text=True, cwd='/workspace/dnd-solo-rerun2', env=env)
try: res = json.loads(r.stdout or r.stderr)
except Exception: res = {'stage': 'unparsed', 'message': (r.stdout + r.stderr)[-800:]}
if 'spoken' not in res and '--force' not in sys.argv:
    print('DRY RUN REJECTED:', (res.get('message') or '')[:600]); sys.exit(3)
reply.write_text(json.dumps(draft, ensure_ascii=False))
print('submitted', reply.name)
time.sleep(3)
w = h / 'WAITING'
print('now waiting:', w.read_text() if w.exists() else '(none)')
