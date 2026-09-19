"""
P-R1 — DESENVOLVIMENTO em dados T0 (Maass execucao_v3 S1/S2; ζ bloco d01 de m4-v3). Não é teste.
Modelo: erro previsto do estimador = fit(F_modelo) − c, com F_modelo(t) = Σ_linhas (c/2)[e^{iE_cT}W(t−T) + e^{−iE_cT}W(t+T)]
sobre TODAS as linhas conhecidas com T ≤ T_corte (inclusive fora do catálogo do ajuste), e o MESMO ajuste
(targeted_joint_fit, band, conjugado, meia-largura ½ FWHM) com o catálogo do bloco.
"""
import csv, json, math, sys
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src")); sys.path.insert(0, str(ROOT / "results/etapa11_6_controles/maass"))
from riemann_spectra.arithmetic import targeted_joint_fit, prime_power_catalog
from riemann_spectra.periods import window_response, measure_window_response
import catalogo_g1 as g1

def model_eval(lines, L, Ec):
    T = np.array([l[0] for l in lines]); C = np.array([l[1] for l in lines], dtype=complex)
    def F(t):
        t = np.atleast_1d(t)[:, None]
        return (0.5 * C * np.exp(1j * Ec * T) * window_response(t - T, L, "hann")
                + 0.5 * np.conj(C) * np.exp(-1j * Ec * T) * window_response(t + T, L, "hann")).sum(axis=1)
    return F

def predict(lines_all, cat, L, Ec):
    fwhm = measure_window_response(L, "hann")["fwhm"]
    fit = targeted_joint_fit(model_eval(lines_all, L, Ec), cat, L, Ec, half_width=0.5 * fwhm, window="hann",
                             sampling="band", include_conjugate=True)
    return np.array([f["coefficient_real"] for f in fit]), np.array([f["coefficient_imag"] for f in fit])

def maass_lines(nmax):
    out = []
    for delta, rng_n in ((-1, range(1, nmax + 1)), (1, range(3, nmax + 1))):
        for n in rng_n:
            D = n * n - 4 * delta
            c = 0.0
            for cyc in g1.cycles(D):
                k, _, _ = g1.primitive_root(min(cyc), n, delta, None)
                c += g1.coefficient(n, delta, k)[1]
            l = 2 * (math.acosh(n / 2) if delta == 1 else math.asinh(n / 2))
            out.append((l, c))
    return sorted(out)

res = {}
for Tcut in (5.2, 6.5, 8.0):
    nmax = int(2 * math.cosh(Tcut / 2)) + 1
    lines = [l for l in maass_lines(nmax) if l[0] <= Tcut]
    for b in ("S1", "S2"):
        bd = ROOT / f"results/etapa11_6_controles/maass/execucao_v3/{b}"
        m = json.loads((bd / "block_metrics.json").read_text()); L, Ec = m["instrument"]["L"], m["instrument"]["E_c"]
        rows = list(csv.DictReader(open(bd / "arithmetic_matches.csv")))
        cat = [{"catalog_index": i, "period_theoretical": float(r["period_theoretical"]), "coefficient_theoretical": float(r["coefficient_theoretical"])} for i, r in enumerate(rows)]
        pre, pim = predict(lines, cat, L, Ec)
        c = np.array([x["coefficient_theoretical"] for x in cat]); obs = np.array([float(r["fit_coefficient_real"]) for r in rows])
        e_obs, e_pre = obs - c, pre - c
        res[(b, Tcut)] = (np.array([x["period_theoretical"] for x in cat]), e_obs, e_pre)
for b in ("S1", "S2"):
    T, eo, _ = res[(b, 8.0)]
    print(f"== {b}: T | erro observado | previsto (corte 5,2 / 6,5 / 8,0)")
    for k in range(len(T)):
        print("  %.4f  %+.3e  |  %+.3e  %+.3e  %+.3e" % (T[k], eo[k], res[(b,5.2)][2][k], res[(b,6.5)][2][k], res[(b,8.0)][2][k]))
    for Tc in (5.2, 6.5, 8.0):
        _, eo, ep = res[(b, Tc)]
        print(f"  corte {Tc}: soma dos quadrados observada {np.sum(eo**2):.3e}; do resíduo (obs−prev) {np.sum((eo-ep)**2):.3e}; "
              f"sinais concordantes onde |prev|>1e-3: {int(np.sum((np.sign(eo)==np.sign(ep)) & (np.abs(ep)>1e-3)))}/{int(np.sum(np.abs(ep)>1e-3))}")

# ---- ζ, bloco d01 de m4-v3 (T0) ----
run = ROOT / "results/run_20260913_220906_m3_d01-d02-d03-d04-d05-d06-d07-d08-d09-d10/tables/d01"
rows = list(csv.DictReader(open(run / "arithmetic_matches.csv")))
bm = json.loads((run / "block_metrics.json").read_text()) if (run / "block_metrics.json").exists() else None
if bm is None:
    import glob
    cand = glob.glob(str(run.parent.parent / "**/d01*metrics*.json"), recursive=True)
    bm = json.loads(open(cand[0]).read())
L, Ec = bm["instrument"]["L"], bm["instrument"]["E_c"]
cat = [{"catalog_index": i, "period_theoretical": float(r["period_theoretical"]), "coefficient_theoretical": float(r["coefficient_theoretical"])} for i, r in enumerate(rows)]
c = np.array([x["coefficient_theoretical"] for x in cat]); obs = np.array([float(r["fit_coefficient_real"]) for r in rows])
print("== zeta d01 (L=%.2f)" % L)
for Tcut in (5.2, 6.5, 8.0):
    lines = [(x["period_theoretical"], x["coefficient_theoretical"]) for x in prime_power_catalog(0.3, Tcut)]
    pre, _ = predict(lines, cat, L, Ec)
    eo, ep = obs - c, pre - c
    big = np.abs(ep) > 1e-7
    print(f"  corte {Tcut}: SQ observada {np.sum(eo**2):.3e}; SQ resíduo {np.sum((eo-ep)**2):.3e}; máx|erro obs| {np.max(np.abs(eo)):.2e}; "
          f"sinais concordantes onde |prev|>1e-7: {int(np.sum((np.sign(eo)==np.sign(ep)) & big))}/{int(big.sum())}")
