from pathlib import Path
from fractions import Fraction
import hashlib,json,resource,time
from collatz.central_residues import geometric_limit
folder=Path(__file__).resolve().parent
expected=(folder/'DECLARACAO.sha256').read_text().split()[0]
assert hashlib.sha256((folder/'DECLARACAO.md').read_bytes()).hexdigest()==expected
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
wall,cpu=time.monotonic(),time.process_time()
previous=[Fraction(1)]
identities=0
rows=[]
for level in (1,2,3):
    n,period=3**level,2*3**(level-1)
    law=[]
    # Fonte: Tao Lema 1.12, fórmula de pré-imagens; diferente do push usado antes.
    for x in range(n):
        value=Fraction(0)
        for a in range(1,period+1):
            numerator=2**a*x-1
            if numerator%3==0:
                value+=Fraction(1,2**a)*previous[(numerator//3)%(n//3)]
        law.append(value/(1-Fraction(1,2**period)))
    assert law==geometric_limit(level)
    assert sum(law)==1
    assert law[-1]>=Fraction(1,2**level)
    identities+=n
    rows.append({'level':level,'mass_minus_one':str(law[-1]),
                 'lower_bound':str(Fraction(1,2**level)),
                 'relative_mass':str(2*3**(level-1)*law[-1])})
    previous=law
fixed=0
for k in range(13):
    for x in (0,1,2,-1):
        value=Fraction(x)
        for _ in range(k):
            value=(3*value+1)/2
        assert value+1==Fraction(3,2)**k*(x+1)
        assert (value+1).numerator%3**k==0
        fixed+=1
result={'status':'validado nas identidades finitas','declaration_sha256':expected,
        'tao_recursion_components':identities,'fixed_point_identities':fixed,
        'rows':rows,'cpu_seconds':time.process_time()-cpu,
        'wall_seconds':time.monotonic()-wall,
        'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'limits':'Não é teste de minorante uniforme, de Lp ou do teorema completo de Tao.'}
(folder/'resultados.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
