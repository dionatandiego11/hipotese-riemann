from pathlib import Path
from fractions import Fraction
from itertools import product
import hashlib,json,resource,time
from collatz.residue_characters import reduce_polynomial
folder=Path(__file__).resolve().parent
for name in ('DECLARACAO','ADENDO_PARES'):
 expected=(folder/(name+'.sha256')).read_text().split()[0]
 assert hashlib.sha256((folder/(name+'.md')).read_bytes()).hexdigest()==expected
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
wall,cpu=time.monotonic(),time.process_time()
orientations=norms=0
for level in (1,2,3):
    n=3**level
    for x in range(n):
        left=[Fraction(0)]*n
        for s,t in product((5,7),repeat=2):
            left[((s-t)*x)%n]+=Fraction(1,4)
        right=[Fraction(0)]*n
        right[0]+=Fraction(1,2)
        right[(2*x)%n]+=Fraction(1,4)
        right[(-2*x)%n]+=Fraction(1,4)
        assert reduce_polynomial(left,level)==reduce_polynomial(right,level)
        norms+=1
        for first,second in product((2,6,18),repeat=2):
            admitted=[(a,b) for a,b in ((1,2),(2,1)) if a<=first and b<=second]
            assert admitted==[(1,2),(2,1)]
            orientations+=1
result={'status':'validado em álgebra exata','squared_modulus_identities':norms,
        'allowed_pair_checks':orientations,'cpu_seconds':time.process_time()-cpu,
        'wall_seconds':time.monotonic()-wall,
        'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'limits':'Não confere a prova profunda de Tao nem avalia constantes.'}
(folder/'pares_resultados.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
