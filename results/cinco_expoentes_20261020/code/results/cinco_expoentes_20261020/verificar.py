"""Identidade pós-exploratória de cinco expoentes: domínio declarado."""
from pathlib import Path
import contextlib,hashlib,io,json,resource,shutil,sys,time
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT),str(ROOT/"src")]
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
expected=(RUN/"DECLARACAO.sha256").read_text().split()[0]
assert hashlib.sha256((RUN/"DECLARACAO.md").read_bytes()).hexdigest()==expected
files=["collatz/five_block_rewrites.py","collatz/affine_rewrites.py","collatz/balanced_seed.py","collatz/cost_residues.py","tests/test_collatz_five_blocks.py","results/cinco_expoentes_20261020/verificar.py"]
hashes={}
for name in files:
 source=ROOT/name;hashes[name]=hashlib.sha256(source.read_bytes()).hexdigest()
 target=RUN/"code"/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
start_cpu,start_wall=time.process_time(),time.perf_counter()
import pytest
out=io.StringIO()
with contextlib.redirect_stdout(out),contextlib.redirect_stderr(out):
 status=pytest.main(["-q","-s",str(ROOT/files[4])])
(RUN/"pytest.log").write_text(out.getvalue())
manifest=dict(declaracao_sha256=expected,arquivos=hashes,pytest_status=int(status),cpu_s=time.process_time()-start_cpu,parede_s=time.perf_counter()-start_wall,cpu_teto_s=30,python=sys.version,pytest=pytest.__version__,selecao="após diagnóstico da semente4",dados_zeros=False,orbitas_positivas=False)
(RUN/"manifesto.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
print(out.getvalue());print(json.dumps(manifest,ensure_ascii=False))
raise SystemExit(int(status))
