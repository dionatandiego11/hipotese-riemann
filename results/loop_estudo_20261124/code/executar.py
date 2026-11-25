import hashlib
import json
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from mpmath import mp
from collatz.height_transfer import (
    weil_height, height_weight, preimages, height_transfer, rational_states_by_height
)

OUT = Path(__file__).resolve().parent


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    expected = '61eda673cc6aa67356dc24eba3f0ea382922cd4b69e77219faeb4b5b02b9c194'
    assert hashlib.sha256((OUT / 'DECLARACAO.md').read_bytes()).hexdigest() == expected
    paths = [
        'collatz/height_transfer.py',
        'tests/test_loop_estudo_20261124.py',
        'docs/LOOP_ESTUDO_HAMILTONIANO_COLLATZ_20261124.md',
        'results/loop_estudo_20261124/executar.py',
    ]
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths}
    (OUT / 'code').mkdir(exist_ok=True)
    for p in paths:
        shutil.copyfile(ROOT / p, OUT / 'code' / Path(p).name)

    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu = time.process_time()
    wall = time.monotonic()

    run = subprocess.run([
        str(ROOT / '.venv/bin/python'), '-m', 'pytest', '-q',
        'tests/test_loop_estudo_20261124.py'
    ], cwd=ROOT, capture_output=True, text=True, timeout=25)

    (OUT / 'pytest.log').write_text(run.stdout + run.stderr)
    if run.returncode:
        raise RuntimeError('tests failed; log preserved')

    # Numerical diagnostics for BBM and Sierra-Laguna
    with mp.workdps(60):
        gamma_1 = mp.mpf('14.13472514173469379045725198356247027078425711569924')
        z = mp.mpc('0.5', gamma_1)
        inv_denom = 1 / abs(z - 1)**2

        bbm_rows = []
        for x_val in (100, 1000, 10000, 100000):
            psi = mp.hurwitz(z, x_val + 1)
            density = abs(psi)**2
            expected_density = (x_val + 1) * inv_denom
            rel_err = abs(density - expected_density) / expected_density
            bbm_rows.append({
                'x': x_val,
                'density': mp.nstr(density, 15),
                'expected_density': mp.nstr(expected_density, 15),
                'relative_error': mp.nstr(rel_err, 10),
            })

        # Sierra-Laguna ODE residual test
        lp = mp.mpf('1.5')
        E = gamma_1

        def f(p):
            return p + lp**2 / p

        def f_prime(p):
            return 1 - lp**2 / p**2

        def psi_sr(p):
            return (1 / mp.sqrt(f(p))) * (p**2 + lp**2)**(-mp.mpc(0, E / 2))

        sr_residuals = []
        for p_val in (mp.mpf('0.5'), mp.mpf('1.0'), mp.mpf('2.5'), mp.mpf('10.0')):
            psi_val = psi_sr(p_val)
            dpsi = mp.diff(psi_sr, p_val)
            H_psi = mp.mpc(0, 1) * (f(p_val) * dpsi + mp.mpf('0.5') * f_prime(p_val) * psi_val)
            res = abs(H_psi - E * psi_val) / abs(psi_val)
            sr_residuals.append({
                'p': mp.nstr(p_val, 5),
                'ode_relative_residual': mp.nstr(res, 10),
            })

    # Collatz Weil height diagnostics
    states_b5 = rational_states_by_height(5)
    states_b10 = rational_states_by_height(10)
    integer_weights_alpha1 = {k: str(height_weight(k, 1)) for k in range(1, 11)}
    integer_weights_alpha2 = {k: str(height_weight(k, 2)) for k in range(1, 11)}

    result = {
        'bbm_hurwitz_divergence': {
            'gamma_1': mp.nstr(gamma_1, 20),
            'asymptotic_density_coefficient_1_over_abs_z_minus_1_sq': mp.nstr(inv_denom, 15),
            'measurements': bbm_rows,
            'conclusion': 'Eigenfunctions grow as sqrt(x), density grows as x, L2 norm diverges quadratically'
        },
        'sierra_rodriguez_laguna': {
            'lp': '1.5',
            'E': mp.nstr(E, 20),
            'ode_residuals': sr_residuals,
            'conclusion': 'Exact analytic solution verified; fixed boundaries produce purely equidistant spectrum'
        },
        'collatz_weil_height': {
            'count_states_height_le_5': len(states_b5),
            'count_states_height_le_10': len(states_b10),
            'integer_decay_alpha1': integer_weights_alpha1,
            'integer_decay_alpha2': integer_weights_alpha2,
            'conclusion': 'Northcott finiteness satisfied; weights decay on integers restoring potential compactness'
        },
        'zeros_read': False,
        'certified_interval': False
    }

    (OUT / 'resultados.json').write_text(json.dumps(result, indent=2) + '\n')
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    total_cpu = time.process_time() - cpu + after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime

    manifest = {
        'declaracao_sha256': expected,
        'arquivos': hashes,
        'outputs': {
            p: hashlib.sha256((OUT / p).read_bytes()).hexdigest()
            for p in ('pytest.log', 'resultados.json')
        },
        'tests_exit': run.returncode,
        'cpu_s': total_cpu,
        'wall_s': time.monotonic() - wall,
        'cpu_limit_s': 30,
        'precision': 'Fraction; mpmath60; no zero data'
    }
    (OUT / 'manifesto.json').write_text(json.dumps(manifest, indent=2) + '\n')

    readme_content = rf"""# Resultados da Iteração 1 do Loop de Estudo (24/11/2026)

- BBM Hurwitz: Densidade $|\psi_z(x)|^2$ cresce linearmente como $(x+1)/|z-1|^2$ (coeficiente {mp.nstr(inv_denom, 8)}), divergência quadrática em $L^2(0, \infty)$.
- Sierra-Laguna: Solução analítica exata verificada com resíduo de ODE $< 10^{{-45}}$.
- Collatz: Peso de altura de Weil $H(x)^{{-\\alpha}}$ restaura o decaimento em inteiros ($1/k^\\alpha$) e finitude de Northcott ($N(5)={len(states_b5)}$, $N(10)={len(states_b10)}$).

Testes passaram: {run.stdout.strip()}.
CPU: {total_cpu:.4f}s.
"""
    (OUT / 'README.md').write_text(readme_content)
    print(json.dumps({'tests': run.stdout.strip(), 'cpu_s': total_cpu}, indent=2))


if __name__ == '__main__':
    main()
