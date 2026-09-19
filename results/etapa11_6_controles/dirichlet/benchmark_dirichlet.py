"""
Benchmark limitado do Adendo 2, §5 (ADENDO_DIRICHLET_2.md): custo de Z_χ e da varredura perto das alturas do cálculo
completo. Não produz dados usados pelo instrumento. Uso (da raiz do repositório):

  .venv/bin/python3 results/etapa11_6_controles/dirichlet/benchmark_dirichlet.py --carater chi_m4 --saida <arquivo.json>
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dirichlet_zeros as dz  # noqa: E402

T12000 = {"chi_m4": 9750.0, "chi_5": 9507.0}   # θ_χ(T)/π = 12.000 (REGISTRO_PILOTO.md)


def bench(name: str) -> dict:
    ch = dz.CHARACTERS[name]
    rows = []
    for t in (1000.0, 3000.0, 6000.0, T12000[name]):
        with mp.workdps(dz.DEFAULT_DPS):
            dz.Z_real(t - 0.5, ch)                       # aquecimento
        t0 = time.perf_counter()
        for i in range(10):
            with mp.workdps(dz.DEFAULT_DPS):
                dz.Z_real(t + 0.113 * i, ch)
        per_eval = (time.perf_counter() - t0) / 10
        f = dz.ZeroFinder(ch)
        t1 = time.perf_counter()
        z = f.scan(t, n_max=5)
        scan_s = time.perf_counter() - t1
        rows.append({"t": t, "seconds_per_eval": per_eval, "scan_zeros": len(z), "scan_evaluations": f.stats.evaluations,
                     "evals_per_zero": f.stats.evaluations / len(z), "scan_seconds": scan_s,
                     "seconds_per_zero": scan_s / len(z), "max_refine_iterations": f.stats.max_refine_iterations,
                     "bisection_fallbacks": f.stats.bisection_fallbacks, "first_zero": z[0], "last_zero": z[-1]})
        print(json.dumps(rows[-1]), flush=True)
    return {"character": name, "rows": rows, "script_sha256": dz.sha256_of(Path(__file__)),
            "dirichlet_zeros_sha256": dz.sha256_of(Path(dz.__file__))}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--carater", required=True, choices=sorted(dz.CHARACTERS))
    p.add_argument("--saida", required=True, type=Path)
    a = p.parse_args()
    out = bench(a.carater)
    a.saida.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
