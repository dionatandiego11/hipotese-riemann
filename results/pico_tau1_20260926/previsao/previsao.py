"""
Previsão de K_c(τ = 1) nos 30 blocos do C3 (zeros 10.001–100.000, 3.000 por bloco, 10 sub-blocos de 300, Hann),
ANTES de medir. Usa só primos (Σ² de Berry), alturas por inversão da contagem suave e substitutos gaussianos.
Modelos: B (Berry, τ* = 0,5, correção 1/6: principal), B25/B75 (banda de τ*), U (Berry sem correção: amostragem
uniforme), G (GUE com correção). Semente explícita.
"""
import json, time
from pathlib import Path
import numpy as np
from riemann_spectra.number_variance import sigma2_berry, sigma2_gue
from riemann_spectra.unfolding import inverse_n_bar
from riemann_spectra.bragg_peak import structure_from_sigma2, predictive_kc_tau1, realized_structure_error

OUT = Path(__file__).parent
SEED, N_SUB, N_BLOCKS = 20260927, 300, 10
k = np.arange(1, N_SUB, dtype=float)
names = [f"b{i:02d}" for i in range(1, 11)] + [f"c{i:02d}" for i in range(1, 11)] + [f"d{i:02d}" for i in range(1, 11)]
rng = np.random.default_rng(SEED)
t0 = time.time()
res = {"seed": SEED, "n_sub": N_SUB, "n_blocks": N_BLOCKS, "blocos": {}}
VG = structure_from_sigma2(sigma2_gue(k), True)
for i, name in enumerate(names):
    i0 = 10001 + 3000 * i
    E = float(inverse_n_bar(i0 + 1499.5))
    d = {"indices": [i0, i0 + 2999], "E_meio": E}
    models = {"B": (0.5, True, 300), "B25": (0.25, True, 200), "B75": (0.75, True, 200), "U": (0.5, False, 200)}
    for m, (tau, corr, reps) in models.items():
        V = structure_from_sigma2(sigma2_berry(k, E, tau_star=tau), corr)
        d[m] = predictive_kc_tau1(V, N_SUB, N_BLOCKS, reps, rng)
        d[m]["erro_estrutura"] = realized_structure_error(V, N_SUB)
    d["G"] = predictive_kc_tau1(VG, N_SUB, N_BLOCKS, 200, rng)
    res["blocos"][name] = d
    print(name, round(E), {m: round(d[m]["media"], 2) for m in ("B", "B25", "B75", "U", "G")}, flush=True)
res["segundos"] = round(time.time() - t0, 1)
(OUT / "previsao.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
print("ok", res["segundos"], "s")
