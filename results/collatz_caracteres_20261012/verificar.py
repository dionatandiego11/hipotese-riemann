from pathlib import Path
import hashlib,json,resource,time
from collatz.cost_residues import tuple_oracle
from collatz.residue_characters import character_sum,character_from_counts,haar_character
folder=Path(__file__).resolve().parent
expected=(folder/'DECLARACAO.sha256').read_text().split()[0]
assert hashlib.sha256((folder/'DECLARACAO.md').read_bytes()).hexdigest()==expected
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
wall,cpu=time.monotonic(),time.process_time()
identities=haar=0
for level in range(1,5):
    for cost in range(2*level+1):
        counts=tuple_oracle(level,cost)
        for k in range(1,level+1):
            for h in range(3**k):
                assert character_sum(level,cost,k,h)==character_from_counts(counts,k,h)
                identities+=1
for k in range(1,5):
    n=3**k
    units={a:1 for a in range(n) if a%3}
    for h in range(n):
        value=character_from_counts(units,k,h)
        assert value==(haar_character(k,h)*len(units),)+(0,)*(len(value)-1)
        haar+=1
result={'status':'validado','declaration_sha256':expected,'character_identities':identities,
        'haar_identities':haar,'cpu_seconds':time.process_time()-cpu,
        'wall_seconds':time.monotonic()-wall,
        'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'limits':'Identidades finitas, não equidistribuição ou cota relativa uniforme.'}
(folder/'resultados.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
