import json, sys
from pathlib import Path
h=Path('/workspace/kit-6c-rerun2/run/handoff'); r=Path((h/'WAITING').read_text()); d=json.loads(Path(str(r).replace('.reply','.digest')).read_text())
if d.get('rejection'): print('REJECTION:', {k:v for k,v in d['rejection'].items() if k not in ('host_retry','degraded_instruction')})
p=d['packet']; pr=p['input']['private']; pu=p['input']['public']
print(r.parent.name, r.name, '|', pr['player_action']); print('EVENT:',pr['accepted_public_event'], '|', pr['action_kind'])
known=('personality_core','dm_context','kit_state','player_action','accepted_public_event','table_read','action_kind','dialogue_history','discernment_candidates','claims_here')
for k in pr:
    if k not in known: print('PRIV', k, json.dumps(pr[k], ensure_ascii=False)[:1800])
for k in (pu if isinstance(pu,dict) else {}):
    if k not in ('player_action','accepted_public_event','action_kind','performance_reference','speakers','shared_with_private'): print('PUB', k, json.dumps(pu[k], ensure_ascii=False)[:1500])
dc=pr['dm_context'] if isinstance(pr.get('dm_context'),dict) else {}
for k in ('player_perceivable','tolls_here','supported_procedures'):
    if dc.get(k) not in (None,'=ref'): print('DC', k, json.dumps(dc[k], ensure_ascii=False)[:1500])
t=(dc.get('dm_only') or {}).get('tolls_here') if isinstance(dc.get('dm_only'),dict) else None
if isinstance(t,dict): print('TOLL', json.dumps({k:v['state'] for k,v in t.items()}))
if p.get('instructions')!='=ref': print('INSTRUCTIONS CHANGED')
if p.get('schema')!='=ref': print('SCHEMA CHANGED')
if isinstance(pu,dict) and pu.get('performance_reference')!='=ref': print('PERF_REF CHANGED keys', list(pu['performance_reference']) if isinstance(pu['performance_reference'],dict) else '')
