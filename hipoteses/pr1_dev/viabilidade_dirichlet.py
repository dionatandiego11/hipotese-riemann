"""
P-R1 — viabilidade ANTES dos dados reservados (nenhum zero de L(s,χ) é lido). Para os blocos e02–e04 e f02–f04, com
bordas nominais (N̄_χ), calcula (i) o erro previsto pelo modelo de vazamento em cada linha do catálogo c_χ e (ii) o ruído
causado pelo arredondamento das ordenadas a 9 casas (±5e-10 uniforme), medido em níveis substitutos GUE com as mesmas
bordas e densidade: desvio-padrão, sobre 20 perturbações, da mudança do coeficiente ajustado.
"""
import math, sys, json
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[2]
for p in ("src", "results/etapa11_6_controles/dirichlet", "results/etapa11_6_controles/poder", "hipoteses/pr1_dev"):
    sys.path.insert(0, str(ROOT / p))
from riemann_spectra.arithmetic import targeted_joint_fit, prime_power_catalog
from riemann_spectra.periods import measure_window_response
import instrumento_chi as ic, analise_poder as ap
from dirichlet_zeros import CHARACTERS
from dev_maass_zeta import model_eval  # noqa (o import executa o desenvolvimento T0; aceitável aqui)

out = {}
for chn, pref in (("chi_m4", "e"), ("chi_5", "f")):
    ch = CHARACTERS[chn]
    cat = [{"catalog_index": i, "period_theoretical": c["period_theoretical"], "coefficient_theoretical": c["coefficient_theoretical"]}
           for i, c in enumerate(ic.chi_catalog_module(ch).prime_power_catalog(0.5, 5.0))]
    lines = []
    for c in prime_power_catalog(0.3, 8.0):
        chi_n = ch(c["prime"]) ** c["repetition"]
        if chi_n:
            lines.append((c["period_theoretical"], c["coefficient_theoretical"] * chi_n))
    cth = np.array([x["coefficient_theoretical"] for x in cat])
    for j, (i0, i1) in enumerate(((3001, 6000), (6001, 9000), (9001, 12000)), start=2):
        A, B = (float(v) for v in ic.inverse_n_bar_chi(np.array([i0 - 0.5, i1 - 0.5]), ch.q, ch.kappa))
        L, Ec = B - A, 0.5 * (A + B)
        fwhm = measure_window_response(L, "hann")["fwhm"]
        kw = dict(half_width=0.5 * fwhm, window="hann", sampling="band", include_conjugate=True)
        pred = np.array([f["coefficient_real"] for f in targeted_joint_fit(model_eval(lines, L, Ec), cat, L, Ec, **kw)]) - cth
        # ruído de arredondamento em níveis substitutos
        rng = np.random.default_rng(100 + j)
        nbar = lambda E: ic.n_bar_chi(E, ch.q, ch.kappa); dbar = lambda E: ic.d_bar_chi(E, ch.q)
        lev = ap.fold(nbar(np.array([A]))[0] + ap.proxy_unfolded(i1 - i0 + 1, "gue", rng), nbar, dbar, np.linspace(A, B, i1 - i0 + 1))
        tr = ap.DensityTransform(lev[0], lev[-1], 0.5, 5.0, dbar)
        base = np.array([f["coefficient_real"] for f in targeted_joint_fit(lambda t: tr.evaluate(lev, t), cat, tr.L, tr.E_c, **kw)])
        dif = []
        for _ in range(20):
            lp = lev + rng.uniform(-5e-10, 5e-10, size=len(lev))
            dif.append(np.array([f["coefficient_real"] for f in targeted_joint_fit(lambda t: tr.evaluate(lp, t), cat, tr.L, tr.E_c, **kw)]) - base)
        noise = np.std(np.array(dif), axis=0)
        above5 = np.abs(pred) > 5 * noise
        out[f"{pref}0{j}"] = {"A": A, "B": B, "n_lines": len(cat), "median_abs_pred": float(np.median(np.abs(pred))),
                              "max_abs_pred": float(np.max(np.abs(pred))), "median_noise": float(np.median(noise)),
                              "n_pred_above_5noise": int(above5.sum()),
                              "n_pred_above_5noise_nonzero_c": int((above5 & (cth != 0)).sum())}
        print(f"{pref}0{j}: |erro previsto| mediana {np.median(np.abs(pred)):.2e}, máx {np.max(np.abs(pred)):.2e}; "
              f"ruído de arredondamento mediano {np.median(noise):.2e}; linhas com |prev| > 5·ruído: {int(above5.sum())}/{len(cat)}")
(Path(__file__).parent / "viabilidade_dirichlet.json").write_text(json.dumps(out, indent=2))
