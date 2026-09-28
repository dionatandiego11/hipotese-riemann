"""Diagnóstico EXPLORATÓRIO pós-medição da PT-1 (não altera o veredito). Testa (E) V_k = Σ²_Berry(k) − 1/6 e
(G) |E e^{2πi D_k}| = exp(−2π² V_k) diretamente nos zeros, usando os mesmos blocos."""
import json, math
from pathlib import Path
import numpy as np
from riemann_spectra.unfolding import n_bar_rvm, inverse_n_bar
from riemann_spectra.number_variance import sigma2_berry
gam = np.loadtxt(Path(__file__).resolve().parents[3] / "data/processed/zeros_100k.csv", delimiter=",", skiprows=1)[:, 1]
ks = [1, 2, 5, 10, 20, 50, 100, 200]
out = {}
for name, i0 in (("b01", 10001), ("c05", 52001), ("d10", 97001), ("todos_10001_100000", 10001)):
    i1 = 100000 if name.startswith("todos") else i0 + 2999
    x = n_bar_rvm(gam[i0 - 1:i1]); E = float(inverse_n_bar((i0 + i1) / 2))
    rows = []
    for k in ks:
        D = x[k:] - x[:-k] - k
        D = D - D.mean()                      # remove deriva média (unfolding)
        V = D.var()
        c = abs(np.mean(np.exp(2j * math.pi * D)))
        Vb = float(sigma2_berry(float(k), E)) - 1 / 6
        rows.append({"k": k, "V_medido": V, "V_berry_menos_1_6": Vb, "coerencia_medida": c,
                     "gauss_com_V_medido": math.exp(-2 * math.pi**2 * V), "gauss_com_V_berry": math.exp(-2 * math.pi**2 * Vb)})
    out[name] = rows
    print(name, f"E~{E:.0f}")
    for r in rows:
        print("  k=%3d  V_med %.4f  V_B-1/6 %.4f | coer %.4f  gauss(V_med) %.4f  gauss(V_B) %.4f" % tuple(r[c] for c in r))
(Path(__file__).parent / "diagnostico.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
