"""
H-004 (P-R1) — preditor congelado do erro do estimador e avaliação. Ver DECLARACAO.md nesta pasta.

Erro previsto da linha k:  e_prev,k = Re fit(F_modelo)_k − c_k, com o MESMO ajuste do instrumento
(targeted_joint_fit, Hann, band, conjugado, meia-largura ½ FWHM, catálogo do bloco) aplicado a

  F_modelo(t) = Σ_{linhas conhecidas, T ≤ T_corte} (c/2)[e^{iE_cT} W(t−T) + e^{−iE_cT} W(t+T)]  +  F_Δ(t),
  F_Δ(t)      = ∫_A^B w(E) (d_exata(E) − d̄(E)) e^{−i(E−E_c)t} dE     (termo suave conhecido omitido pelo instrumento).

Ruído de arredondamento da linha k: desvio-padrão, sobre N_pert perturbações das ordenadas do bloco por U(−ε, ε), da
mudança de Re fit dos DADOS (não usa e_obs). Seleção: |e_prev,k| > 5·ruído_k (não usa e_obs).
Erro observado: e_obs,k = fit_coefficient_real − coefficient_theoretical, lido de arithmetic_matches.csv do controle.
"""
from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))
from riemann_spectra.arithmetic import prime_power_catalog, targeted_joint_fit  # noqa: E402
from riemann_spectra.periods import local_gauss_legendre_panels, measure_window_response, window_response  # noqa: E402

T_CUT = 8.0
N_PERT = 20
EPS = 5e-10
SEL_FACTOR = 5.0


def model_eval(lines, L, Ec, conj=True, delta=None):
    T = np.array([l[0] for l in lines])
    C = np.array([l[1] for l in lines], dtype=complex)

    def F(t):
        t = np.atleast_1d(np.asarray(t, dtype=float))
        v = (0.5 * C * np.exp(1j * Ec * T) * window_response(t[:, None] - T, L, "hann")).sum(axis=1)
        if conj:
            v = v + (0.5 * np.conj(C) * np.exp(-1j * Ec * T) * window_response(t[:, None] + T, L, "hann")).sum(axis=1)
        if delta is not None:
            v = v + delta(t)
        return v
    return F


def smooth_delta_term(A, B, d_exact, d_bar, panel=0.5, order=16):
    """F_Δ(t) por quadratura de Gauss–Legendre em painéis (janela de Hann em [A, B])."""
    L, Ec = B - A, 0.5 * (A + B)
    off, wts = local_gauss_legendre_panels(L, panel, order)
    E = A + off
    wHann = np.sin(math.pi * off / L) ** 2
    g = wHann * (d_exact(E) - d_bar(E)) * wts

    def F(t):
        t = np.atleast_1d(np.asarray(t, dtype=float))
        return (g[None, :] * np.exp(-1j * (E[None, :] - Ec) * t[:, None])).sum(axis=1)
    return F


def fit_real(evaluator, cat, L, Ec):
    fwhm = measure_window_response(L, "hann")["fwhm"]
    fit = targeted_joint_fit(evaluator, cat, L, Ec, half_width=0.5 * fwhm, window="hann", sampling="band", include_conjugate=True)
    return np.array([f["coefficient_real"] for f in fit])


def dirichlet_lines(ch, t_cut=T_CUT):
    out = []
    for c in prime_power_catalog(0.3, t_cut):
        chi = ch(c["prime"]) ** c["repetition"]
        if chi:
            out.append((c["period_theoretical"], c["coefficient_theoretical"] * chi))
    return out


def predict_block(cat, A, B, lines, d_exact=None, d_bar=None, conj=True):
    L, Ec = B - A, 0.5 * (A + B)
    delta = smooth_delta_term(A, B, d_exact, d_bar) if (d_exact is not None and d_bar is not None) else None
    c = np.array([x["coefficient_theoretical"] for x in cat])
    return fit_real(model_eval(lines, L, Ec, conj=conj, delta=delta), cat, L, Ec) - c


def rounding_noise(transform, levels, cat, seed, eps=EPS, n=N_PERT):
    rng = np.random.default_rng(seed)
    base = fit_real(lambda t: transform.evaluate(levels, t), cat, transform.L, transform.E_c)
    dif = [fit_real(lambda t, lp=levels + rng.uniform(-eps, eps, size=len(levels)): transform.evaluate(lp, t), cat,
                    transform.L, transform.E_c) - base for _ in range(n)]
    return np.std(np.array(dif), axis=0)


def metrics(e_obs, e_prev, noise, sel):
    eo, ep, s = e_obs[sel], e_prev[sel], noise[sel]
    if len(eo) == 0:
        return {"n_selected": 0}
    z_obs, z_res = eo / s, (eo - ep) / s
    return {"n_selected": int(len(eo)),
            "explained_fraction": float(1.0 - np.sum(z_res ** 2) / np.sum(z_obs ** 2)),
            "sign_agreement": float(np.mean(np.sign(eo) == np.sign(ep))),
            "median_abs_obs_over_noise": float(np.median(np.abs(z_obs))),
            "median_abs_residual_over_noise": float(np.median(np.abs(z_res)))}


# ------------------------------------------------------------------ avaliação do controle Dirichlet (H-004)

def evaluate_dirichlet(control_dir: Path, zeros_file: Path, char_name: str, blocks, seed=20260923):
    sys.path.insert(0, str(ROOT / "results/etapa11_6_controles/dirichlet"))
    import instrumento_chi as ic
    from dirichlet_zeros import CHARACTERS
    ch = CHARACTERS[char_name]
    zeros = np.loadtxt(zeros_file, dtype=np.float64)
    lines = dirichlet_lines(ch)
    d_exact = lambda E: ic.d_theta_chi(E, ch.q, ch.kappa)   # noqa: E731
    d_bar = lambda E: ic.d_bar_chi(E, ch.q)                  # noqa: E731
    per_block = {}
    for k, b in enumerate(blocks):
        bd = Path(control_dir) / b["name"]
        rows = list(csv.DictReader(open(bd / "arithmetic_matches.csv", encoding="utf-8")))
        cat = [{"catalog_index": i, "period_theoretical": float(r["period_theoretical"]),
                "coefficient_theoretical": float(r["coefficient_theoretical"])} for i, r in enumerate(rows)]
        g = zeros[b["first_index"] - 1:b["last_index"]]
        A, B = float(g[0]), float(g[-1])
        tr = ic.ChiTransform(A, B, 0.5, 5.0, ch.q, ch.kappa)
        e_prev = predict_block(cat, A, B, lines, d_exact, d_bar, conj=True)
        e_prev_noconj = predict_block(cat, A, B, lines, d_exact, d_bar, conj=False)
        noise = rounding_noise(tr, g, cat, seed + k)
        sel = np.abs(e_prev) > SEL_FACTOR * noise
        e_obs = np.array([float(r["fit_coefficient_real"]) - float(r["coefficient_theoretical"]) for r in rows])
        per_block[b["name"]] = {"A": A, "B": B, "e_prev": e_prev.tolist(), "e_prev_noconj": e_prev_noconj.tolist(),
                                "noise": noise.tolist(), "selected": sel.tolist(), "e_obs": e_obs.tolist(),
                                "metrics": metrics(e_obs, e_prev, noise, sel),
                                "metrics_noconj_model": metrics(e_obs, e_prev_noconj, noise, sel)}
    return per_block


def classify(all_blocks):
    """Regras da DECLARACAO.md §4 sobre o conjunto de blocos reservados."""
    eo = np.concatenate([np.array(v["e_obs"])[np.array(v["selected"])] for v in all_blocks.values()])
    ep = np.concatenate([np.array(v["e_prev"])[np.array(v["selected"])] for v in all_blocks.values()])
    s = np.concatenate([np.array(v["noise"])[np.array(v["selected"])] for v in all_blocks.values()])
    pooled = metrics(eo, ep, s, np.ones(len(eo), dtype=bool))
    per_ok = sum(1 for v in all_blocks.values() if v["metrics"].get("explained_fraction", -1) >= 0.5)
    if pooled["n_selected"] < 30:
        verdict = "inconclusivo (menos de 30 linhas selecionadas)"
    elif pooled["explained_fraction"] >= 0.9 and pooled["sign_agreement"] >= 0.9 and per_ok >= 5:
        verdict = "sucesso"
    elif pooled["explained_fraction"] < 0.5 or pooled["sign_agreement"] < 0.7:
        verdict = "falha"
    else:
        verdict = "inconclusivo"
    return {"pooled": pooled, "blocks_with_EF_ge_0.5": per_ok, "n_blocks": len(all_blocks), "verdict": verdict}


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description="H-004 (P-R1): avaliação após a execução do controle Dirichlet.")
    ap.add_argument("--controle", type=Path, required=True, help="pasta de saída do instrumento_chi (contém e02/, …)")
    ap.add_argument("--zeros-m4", type=Path, required=True)
    ap.add_argument("--zeros-5", type=Path, required=True)
    ap.add_argument("--saida", type=Path, required=True)
    a = ap.parse_args(argv)
    res = {}
    res.update(evaluate_dirichlet(a.controle, a.zeros_m4, "chi_m4",
                                  [{"name": "e02", "first_index": 3001, "last_index": 6000},
                                   {"name": "e03", "first_index": 6001, "last_index": 9000},
                                   {"name": "e04", "first_index": 9001, "last_index": 12000}]))
    res.update(evaluate_dirichlet(a.controle, a.zeros_5, "chi_5",
                                  [{"name": "f02", "first_index": 3001, "last_index": 6000},
                                   {"name": "f03", "first_index": 6001, "last_index": 9000},
                                   {"name": "f04", "first_index": 9001, "last_index": 12000}], seed=20260924))
    out = {"blocks": res, "classification": classify(res)}
    a.saida.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out["classification"], indent=2))


if __name__ == "__main__":
    main()
