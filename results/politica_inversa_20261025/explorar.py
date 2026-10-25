"""Cálculo declarado das políticas finitas; sem ampliar a busca."""
from pathlib import Path
import hashlib,json,resource,shutil,sys,time
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT),str(ROOT/"src")]
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
expected=(RUN/"DECLARACAO.sha256").read_text().split()[0]
assert hashlib.sha256((RUN/"DECLARACAO.md").read_bytes()).hexdigest()==expected
files=["collatz/inverse_cost_policy.py","collatz/affine_rewrites.py","results/politica_inversa_20261025/explorar.py"]
hashes={}
for name in files:
 source=ROOT/name;hashes[name]=hashlib.sha256(source.read_bytes()).hexdigest()
 target=RUN/"code"/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
start_cpu,start_wall=time.process_time(),time.perf_counter()
from collatz.inverse_cost_policy import base_certificate,inverse_policies
certificate,counts=base_certificate();policies=inverse_policies()
summary=[]
for r in range(1,5):
 table=policies[r];maximum=max(cost for cost,_ in table.values())
 summary.append(dict(r=r,estados=len(table),mu=maximum,pior_classe=min(x for x,(c,_) in table.items() if c==maximum)))
(RUN/"certificado_base.json").write_text(json.dumps({str(k):v for k,v in sorted(certificate.items())},indent=2)+"\n")
(RUN/"politicas.json").write_text(json.dumps([{str(k):v for k,v in sorted(table.items())} for table in policies],indent=2)+"\n")
(RUN/"politicas_resumo.json").write_text(json.dumps(summary,indent=2)+"\n")
manifest=dict(declaracao_sha256=expected,arquivos=hashes,cpu_s=time.process_time()-start_cpu,parede_s=time.perf_counter()-start_wall,cpu_teto_s=30,python=sys.version,dados_zeros=False,orbitas_T=False)
(RUN/"manifesto_exploracao.json").write_text(json.dumps(manifest,indent=2)+"\n")
print(json.dumps(dict(base_unidades=len(certificate),politicas=summary,cpu_s=manifest['cpu_s'])))
