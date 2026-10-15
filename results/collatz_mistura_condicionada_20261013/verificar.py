from pathlib import Path
from collections import Counter
from fractions import Fraction
import hashlib,json,resource,time
from collatz.cost_residues import generator_counts
folder=Path(__file__).resolve().parent
expected=(folder/'DECLARACAO.sha256').read_text().split()[0]
assert hashlib.sha256((folder/'DECLARACAO.md').read_bytes()).hexdigest()==expected
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
wall,cpu=time.monotonic(),time.process_time()


def compositions(total, caps):
    if not caps:
        if total==0:
            yield ()
        return
    for j in range(min(total,caps[0]-1)+1):
        for tail in compositions(total-j,caps[1:]):
            yield (j,)+tail


def offset(costs):
    x=Fraction(0)
    for j in reversed(costs):
        x=(3*x+1)/2**(j+1)
    return x


def residue(x,n):
    return x.numerator*pow(x.denominator,-1,n)%n

checks=0
for level in range(2,6):
    caps=[2*3**(level-i-1) for i in range(level)]
    n=3**level
    for cost in (level-1,level,level+1):
        tuples=list(compositions(cost,caps))
        for length in range(1,level):
            suffix=generator_counts(level-length,cost)
            for prefix_cost in range(cost+1):
                actual=Counter(residue(offset(t),n) for t in tuples if sum(t[:length])==prefix_cost)
                prefix=Counter(residue(offset(t),n) for t in compositions(prefix_cost,caps[:length]))
                factor=3**length*pow(2,-(length+prefix_cost),n)
                predicted=Counter()
                for a,na in prefix.items():
                    for b,nb in suffix[cost-prefix_cost].items():
                        predicted[(a+factor*b)%n]+=na*nb
                assert actual==predicted
                checks+=1
rational=modular=0
for length in range(1,5):
    for total_a in range(length,length+9):
        costs=list(compositions(total_a-length,[total_a+1]*length))
        values=[offset(t) for t in costs]
        assert len(set(values))==len(values)
        rational+=len(values)
        small=[x for x in values if 0<2**total_a*x<3**8]
        assert len({residue(x,3**8) for x in small})==len(small)
        modular+=len(small)
result={'status':'validado nas identidades finitas','declaration_sha256':expected,
        'conditional_block_checks':checks,'rational_offsets_checked':rational,
        'modular_offsets_checked':modular,'cpu_seconds':time.process_time()-cpu,
        'wall_seconds':time.monotonic()-wall,
        'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'limits':'Não certifica constantes assintóticas, oscilação L1 ou prova profunda de Tao.'}
(folder/'resultados.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
