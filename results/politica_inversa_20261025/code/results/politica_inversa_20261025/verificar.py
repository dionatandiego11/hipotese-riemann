"""Certificados, políticas independentes e construtores nos domínios declarados."""
from pathlib import Path
import contextlib,hashlib,io,json,resource,shutil,sys,time
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT),str(ROOT/"src")]
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
locks={}
for name,lock in [("DECLARACAO.md","DECLARACAO.sha256"),("ADENDO_CONSTRUTOR.md","ADENDO_CONSTRUTOR.sha256")]:
 expected=(RUN/lock).read_text().split()[0]
 assert hashlib.sha256((RUN/name).read_bytes()).hexdigest()==expected
 locks[name]=expected
files=["collatz/inverse_cost_policy.py","collatz/uniform_coverage.py","collatz/affine_rewrites.py","collatz/cost_residues.py","tests/test_collatz_inverse_cost_policy.py","results/politica_inversa_20261025/verificar.py"]
hashes={}
for name in files:
 source=ROOT/name;hashes[name]=hashlib.sha256(source.read_bytes()).hexdigest()
 target=RUN/"code"/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
inputs={name:hashlib.sha256((RUN/name).read_bytes()).hexdigest() for name in ["certificado_base.json","politicas.json","politicas_resumo.json"]}
start_cpu,start_wall=time.process_time(),time.perf_counter()
from collatz.inverse_cost_policy import base_certificate,inverse_policies
base,_=base_certificate();policies=inverse_policies()
assert {int(k):tuple(v) for k,v in json.loads((RUN/"certificado_base.json").read_text()).items()}==base
loaded=[{int(k):(v[0],tuple(v[1])) for k,v in table.items()} for table in json.loads((RUN/"politicas.json").read_text())]
assert loaded==policies
import pytest
out=io.StringIO()
with contextlib.redirect_stdout(out),contextlib.redirect_stderr(out):
 status=pytest.main(["-q","-s",str(ROOT/files[4])])
(RUN/"pytest.log").write_text(out.getvalue())
manifest=dict(declaracoes=locks,arquivos=hashes,entradas=inputs,pytest_status=int(status),cpu_s=time.process_time()-start_cpu,parede_s=time.perf_counter()-start_wall,cpu_teto_s=30,python=sys.version,pytest=pytest.__version__,aritmetica="inteiros/Fraction",dados_zeros=False,orbitas_T=False,selecao="bloco4 escolhido após exploração finita")
(RUN/"manifesto_verificacao.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
print(out.getvalue());print(json.dumps(manifest,ensure_ascii=False))
raise SystemExit(int(status))
