"""Verificação finita declarada; não constitui prova geral."""
from pathlib import Path
import contextlib, hashlib, io, json, resource, shutil, sys, time
ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
sys.path[:0] = [str(ROOT), str(ROOT / "src")]
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
expected = (RUN / "DECLARACAO.sha256").read_text().split()[0]
assert hashlib.sha256((RUN / "DECLARACAO.md").read_bytes()).hexdigest() == expected
files = ["collatz/conditioned_energy.py", "tests/test_collatz_conditioned_energy.py", "results/energia_condicionada_20261019/verificar.py"]
hashes = {}
for name in files:
    p = ROOT / name
    hashes[name] = hashlib.sha256(p.read_bytes()).hexdigest()
    destination = RUN / "code" / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(p, destination)
start_cpu, start_wall = time.process_time(), time.perf_counter()
import pytest
out = io.StringIO()
with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
    status = pytest.main(["-q", "-s", str(ROOT / files[1])])
(RUN / "pytest.log").write_text(out.getvalue())
manifest = dict(declaracao_sha256=expected, arquivos=hashes, pytest_status=int(status),
    cpu_s=time.process_time()-start_cpu, parede_s=time.perf_counter()-start_wall,
    cpu_teto_s=30, python=sys.version, pytest=pytest.__version__,
    max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    dados_zeros=False, orbitas_positivas=False, aritmetica="inteiros e Fraction exatos")
(RUN / "manifesto.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n")
print(out.getvalue())
print(json.dumps(manifest, ensure_ascii=False))
raise SystemExit(int(status))
