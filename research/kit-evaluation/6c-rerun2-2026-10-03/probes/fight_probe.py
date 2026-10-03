"""Resolve one action on a COPY of a run DB with the engine adjudicator and print fight state."""
import json, sys, shutil, os
sys.path.insert(0, '.'); os.environ.pop('OPENAI_API_KEY', None)
from runtime.kit_agent import Room6CAdjudicator, PendingRuling
from runtime.state_context import Runtime
src, act = sys.argv[1], open(sys.argv[2]).read()
shutil.copy(src, '/tmp/fp.sqlite'); rt = Runtime('/tmp/fp.sqlite')
rev, st = rt.load(); adj = Room6CAdjudicator(source=rt.source())
r = adj.resolve(act, rev, st); rt.commit('probe', rev, list(r.events)); s = rt.load()[1]; c = s.get('combat', {})
print('EVENT:', r.public_event)
print('COMBAT:', json.dumps({k: c.get(k) for k in ('status', 'round', 'order', 'turn', 'pc_damage', 'pc_initiative', 'acted')}))
print('PC status keys:', [k for k in c if 'death' in k or 'dying' in k or 'stable' in k], '| actors:', {k: v.get('status') for k, v in s['actors'].items()})
