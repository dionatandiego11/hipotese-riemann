from pathlib import Path
from fractions import Fraction
from math import comb,isqrt
from itertools import combinations,product
import hashlib,json,resource,time
from collatz.cost_residues import cost_counts
folder=Path(__file__).resolve().parent
expected=(folder/'DECLARACAO.sha256').read_text().split()[0]
assert hashlib.sha256((folder/'DECLARACAO.md').read_bytes()).hexdigest()==expected
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
wall,cpu=time.monotonic(),time.process_time()
checks=0
for level in range(2,6):
    caps=[2*3**i for i in range(level)]
    subset_sums=[sum(caps[i] for i in range(level) if mask>>i&1) for mask in range(2**level)]
    q=cost_counts(level,2*level)
    for cost in range(1,2*level+1):
        theta=Fraction(cost,cost+level-1)
        a=Fraction(1)
        for cap in caps:
            a*=1-theta**cap
        actual=Fraction(q[cost],comb(cost+level-1,level-1))
        bound=sum((theta**d*d*(d-1) for d in subset_sums),Fraction(0))/(2*cost)
        assert abs(actual-a)<=bound
        checks+=1
rows=[]
for level in (16,32,64,128):
    costs=[level-isqrt(level),level,level+isqrt(level)]
    maxcost=max(costs)
    counts={r:cost_counts(level-r,maxcost) for r in range(4)}
    for cost in costs:
        for length in (1,2,3):
            partial=Fraction(0)
            conditional_mass=Fraction(0)
            for prefix in product(range(4),repeat=length):
                s=sum(prefix)
                actual=Fraction(counts[length][cost-s],counts[0][cost])
                reference=Fraction(1,2**(length+s))
                partial+=abs(actual-reference)/2
                conditional_mass+=actual
            rows.append({'level':level,'cost':cost,'prefix_length':length,
                         'partial_half_l1_exact':str(partial),
                         'partial_half_l1_display':float(partial),
                         'conditional_mass_in_box_exact':str(conditional_mass),
                         'reference_mass_in_box_exact':str(Fraction(15,16)**length)})
result={'status':'validado na majorante finita; diagnóstico parcial',
        'declaration_sha256':expected,'coefficient_bound_checks':checks,'rows':rows,
        'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-wall,
        'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'limits':'Tabela de prefixos não é TV completa, não prova limite nem fornece constantes assintóticas.'}
(folder/'resultados.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
