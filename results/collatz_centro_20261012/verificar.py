from pathlib import Path
import hashlib,json,math,resource,time
from fractions import Fraction
from collatz.central_residues import projected_generators,geometric_limit,stationary_half
folder=Path(__file__).resolve().parent
expected=(folder/'DECLARACAO.sha256').read_text().split()[0]
assert hashlib.sha256((folder/'DECLARACAO.md').read_bytes()).hexdigest()==expected
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
wall,cpu=time.monotonic(),time.process_time()
laws={k:geometric_limit(k) for k in (1,2)}
assert all(laws[k]==stationary_half(k) for k in laws)
assert [sum(laws[2][a::3]) for a in range(3)]==laws[1]
rows=[]
for level in (16,32,64,128):
    costs=(level-math.isqrt(level),level,level+math.isqrt(level))
    for resolution in (1,2):
        counts=projected_generators(level,max(costs),resolution)
        for cost in costs:
            total=sum(counts[cost].values())
            law=[Fraction(counts[cost].get(a,0),total) for a in range(3**resolution)]
            tv=sum(abs(a-b) for a,b in zip(law,laws[resolution]))/2
            rows.append({'level':level,'cost':cost,'resolution':resolution,
                         'tv_exact':str(tv),'tv_display':float(tv),
                         'probabilities_exact':[str(p) for p in law]})
result={'status':'validado nas identidades; diagnóstico de convergência',
        'declaration_sha256':expected,'limits_exact':{str(k):[str(v) for v in p] for k,p in laws.items()},
        'rows':rows,'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-wall,
        'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(folder/'resultados.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
print('TV central k=ℓ:',[(r['level'],r['resolution'],r['tv_display']) for r in rows if r['cost']==r['level']])
