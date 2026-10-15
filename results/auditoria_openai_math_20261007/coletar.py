import urllib.request, json, hashlib, datetime, re, concurrent.futures
from pathlib import Path
SHA='adc7f1241b42e322a6451854ab7e4b4c146bf78a'
OUT=Path('results/auditoria_openai_math_20261007')
ARCH=Path('archive/fontes_etapa11/openai_math_adc7f124')
BASE=f'https://raw.githubusercontent.com/openai/math/{SHA}/'
records=[]
def fetch(path):
 url=BASE+path;p=ARCH/path
 if p.exists(): b=p.read_bytes()
 else:
  with urllib.request.urlopen(url,timeout=35) as r:b=r.read(150_000_001)
  if len(b)>150_000_000:raise ValueError('size limit')
  p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
 rec={'path':path,'url':url,'commit':SHA,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'collected_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 return rec,b
paths=['README.md','CONTENTS.md','LICENSE','lean/README.md','lean/docs/003.md','lean/lakefile.lean','lean/lake-manifest.json','lean/lean-toolchain','lean/ComparatorChallenges/README.md']
for name in ['QuasiRiemannHypothesis','DirichletSevenEighths','HeckeSevenEighths','SiegelZeros']:
 paths += [f'lean/ComparatorChallenges/{name}.{ext}' for ext in ['lean','json']]
for name,tree in [('The-Quasi-Riemann-Hypothesis-September-30-2026','8a3427fa6360eb9bb1234a75cb1a0327b2b35165'),('The-Quasi-Riemann-Hypothesis-October-5-2026','b46286acfa00dca1008962a0276b3fa1c3679404'),('Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026','c074e8ce90584cf18844c216d660d9b74bdfd2ed')]:
 tree=json.load(urllib.request.urlopen('https://api.github.com/repos/openai/math/git/trees/'+tree))
 paths += ['preprints/'+name+'/'+f['path'] for f in tree['tree'] if f['type']=='blob']
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for rec,b in ex.map(fetch,paths):records.append(rec)
seen=set(); todo={'OAI.NumberTheory.DirichletL.Nonvanishing'};imports={};failures=[]
while todo:
 batch=sorted(todo-seen);todo=set()
 if not batch:break
 if len(seen)+len(batch)>2000:failures.append({'limit':'2000 modules','pending':batch});break
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
  futures={ex.submit(fetch,'lean/'+m.replace('.','/')+'.lean'):m for m in batch}
  for fut in concurrent.futures.as_completed(futures):
   m=futures[fut];seen.add(m)
   try:rec,b=fut.result()
   except Exception as e:failures.append({'module':m,'error':str(e)});continue
   records.append(rec);t=b.decode();imp=re.findall(r'^import\s+([\w.]+)',t,re.M);imports[m]=imp
   todo.update(x for x in imp if x.startswith('OAI.') and x not in seen)
 if sum(r['bytes'] for r in records)>150_000_000:failures.append({'limit':'150MB'});break
 print('modules',len(seen),'pending',len(todo),flush=True)
 (OUT/'fontes.json').write_text(json.dumps(records,indent=2)+'\n')
 (OUT/'imports.json').write_text(json.dumps(imports,indent=2)+'\n')
(OUT/'falhas_coleta.json').write_text(json.dumps(failures,indent=2)+'\n')
print('DONE',len(records),sum(r['bytes'] for r in records),'failures',failures,flush=True)
