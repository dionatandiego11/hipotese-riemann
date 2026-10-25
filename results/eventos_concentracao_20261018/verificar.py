"""Verificações declaradas, sem zeros reais nem simulação."""
from pathlib import Path
import contextlib
import hashlib
import io
import json
import resource
import shutil
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
sys.path[:0] = [str(ROOT / 'src'), str(ROOT)]
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
declaration = RUN / 'DECLARACAO.md'
expected = (RUN / 'DECLARACAO.sha256').read_text().split()[0]
assert hashlib.sha256(declaration.read_bytes()).hexdigest() == expected
files = [
 'src/riemann_spectra/negative_moments_rare_pairs.py',
 'src/riemann_spectra/negative_moments_discrete_ratios.py',
 'collatz/collision_energy.py', 'collatz/central_residues.py', 'collatz/cost_residues.py',
 'tests/test_negative_moments_rare_pairs.py', 'tests/test_collatz_collision_energy.py',
 'results/eventos_concentracao_20261018/verificar.py',
]
manifest = {'declaracao_sha256': expected, 'classe_calculos': 'B; Fraction exata em Collatz',
            'cpu_teto_s': 60, 'dados_zeros': False, 'arquivos': {}}
for name in files:
 p = ROOT / name
 manifest['arquivos'][name] = hashlib.sha256(p.read_bytes()).hexdigest()
 destination = RUN / 'code' / name
 destination.parent.mkdir(parents=True, exist_ok=True)
 shutil.copyfile(p, destination)
start_cpu, start_wall = time.process_time(), time.perf_counter()
import pytest
out = io.StringIO()
with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
 status = pytest.main(['-q', str(ROOT / files[5]), str(ROOT / files[6])])
(RUN / 'pytest.log').write_text(out.getvalue())
import mpmath as mp
from collatz.central_residues import geometric_limit
from collatz.collision_energy import collision_decomposition
from riemann_spectra.negative_moments_rare_pairs import scaled_defect_integral
rows = []
previous = geometric_limit(0)
for k in range(1, 5):
 current = geometric_limit(k)
 d = collision_decomposition(current, previous)
 rows.append({'K': k, 'energy_exact': str(d['energy']), 'H_exact': str(d['H'])})
 previous = current
with mp.workdps(50):
 pairs = [{'epsilon': str(e), 'inner': mp.nstr(scaled_defect_integral(e, mp.sqrt(e)), 35),
           'outer': mp.nstr(scaled_defect_integral(e, mp.pi)-scaled_defect_integral(e, mp.sqrt(e)), 35),
           'total': mp.nstr(scaled_defect_integral(e, mp.pi), 35)}
          for e in map(mp.mpf, ['0.04','0.01','0.0025'])]
manifest.update(pytest_status=int(status), cpu_s=time.process_time()-start_cpu,
                parede_s=time.perf_counter()-start_wall, max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                python=sys.version, mpmath=mp.__version__)
(RUN / 'manifesto.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
(RUN / 'resultados.json').write_text(json.dumps({'cue': pairs, 'syracuse': rows}, ensure_ascii=False, indent=2)+'\n')
print(out.getvalue())
print(json.dumps({'cpu_s':manifest['cpu_s'],'parede_s':manifest['parede_s'],'status':int(status)}))
raise SystemExit(int(status))
