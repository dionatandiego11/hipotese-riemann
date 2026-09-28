"""Diagnóstico EXPLORATÓRIO 2 (pós-medição): média sobre k ∈ [30, 299] de Re E[e^{2πi D_k}] (sem centrar, como no
estimador) nos 30 blocos, contra exp(−2π² V_k) com V_k medido e com V_k = Σ²_Berry − 1/6."""
import json, math
from pathlib import Path
import numpy as np
from riemann_spectra.unfolding import n_bar_rvm, inverse_n_bar
from riemann_spectra.number_variance import sigma2_berry
gam = np.loadtxt(Path(__file__).resolve().parents[3] / "data/processed/zeros_100k.csv", delimiter=",", skiprows=1)[:, 1]
K = np.arange(30, 300)
acc = {"re_medido": [], "gauss_V_medido": [], "gauss_V_berry": []}
for b in range(30):
    i0 = 10001 + 3000 * b
    x = n_bar_rvm(gam[i0 - 1:i0 + 2999]); E = float(inverse_n_bar(i0 + 1499.5))
    Vb = sigma2_berry(K.astype(float), E) - 1 / 6
    re, gm = [], []
    for sub in range(10):                       # pares dentro de cada sub-bloco de 300, como no estimador
        xs = x[300 * sub:300 * (sub + 1)]
        for k in K:
            D = xs[k:] - xs[:-k] - k
            re.append(np.mean(np.cos(2 * math.pi * D))); gm.append(math.exp(-2 * math.pi**2 * D.var()))
    acc["re_medido"].append(np.mean(re)); acc["gauss_V_medido"].append(np.mean(gm))
    acc["gauss_V_berry"].append(float(np.mean(np.exp(-2 * math.pi**2 * Vb))))
r = {k: float(np.mean(v)) for k, v in acc.items()}
r["razao_medido_sobre_gauss_berry"] = r["re_medido"] / r["gauss_V_berry"]
r["dp_entre_blocos_re_medido"] = float(np.std(acc["re_medido"], ddof=1) / math.sqrt(30))
print(json.dumps(r, indent=1))
(Path(__file__).parent / "diagnostico2.json").write_text(json.dumps({"resumo": r, "por_bloco": acc}, indent=1), encoding="utf-8")
