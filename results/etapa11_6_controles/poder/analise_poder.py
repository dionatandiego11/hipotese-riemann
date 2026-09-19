"""
Análise de poder dos controles da 11.6 com níveis SUBSTITUTOS sintéticos (19/09/2026). Não lê nenhum zero de L(s, χ)
nem nenhum nível do estádio. Lição do ctrl-maass-v1: o critério "claramente detectável" compara |c| com o ruído do
nulo shuffle, e esse ruído depende só da distribuição de espaçamentos, da densidade e da faixa do bloco, que se
conhecem antes dos dados.

Para cada bloco: níveis substitutos (GUE, GOE ou Poisson, unfolded e dobrados pela N̄ do controle) → instrumento com a
densidade do controle → nulo shuffle (B_sigma, B_thr realizações) → σ(t) e limiar z → z previsto de cada linha do
catálogo, z = |c|·W(0)/(2σ(T)); "clara" se z ≥ 1,5·limiar; "resolvida" se a vizinha mais próxima está a ≥ 2 FWHM
(aproximação da separação de resolução calibrada, que foi 2,00 FWHM nos blocos S1 e S2 do Maass).

Validação do método (resultados já conhecidos): bloco d01 de ζ (m4-v3) e blocos S2 e S1 do ctrl-maass-v1.
Uso (da raiz):  .venv/bin/python3 results/etapa11_6_controles/poder/analise_poder.py
"""
import csv
import hashlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy.linalg import eigvalsh_tridiagonal

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "results/etapa11_6_controles/dirichlet"))
sys.path.insert(0, str(ROOT / "results/etapa11_6_controles/maass"))
from riemann_spectra import arithmetic as ar                                    # noqa: E402
from riemann_spectra.controls import generate_gue_central_levels, semicircle_cdf, shuffle_spacings  # noqa: E402
from riemann_spectra.periods import (OscillatoryTransform, local_gauss_legendre_panels, max_statistic,  # noqa: E402
                                     measure_window_response, null_noise_profile, nufft_uniform_t,
                                     threshold_interval, window_coefficients)
import instrumento_chi as ic                                                   # noqa: E402
import instrumento_maass as im                                                 # noqa: E402
from dirichlet_zeros import CHARACTERS                                         # noqa: E402

TWO_PI = 2 * math.pi


class DensityTransform(OscillatoryTransform):
    """Construtor de OscillatoryTransform com densidade suave dada por função (mesmo desenho de MaassTransform)."""

    def __init__(self, A, B, t_min, t_max, dbar, points_per_fwhm=8.0, panel_length=0.5, quad_order=8, window="hann"):
        window_coefficients(window)
        self.window, self.A, self.B = window, float(A), float(B)
        self.L, self.E_c = self.B - self.A, 0.5 * (self.A + self.B)
        self.response = measure_window_response(self.L, window)
        self.dt = self.response["fwhm"] / points_per_fwhm
        self.n_t = int(math.floor((t_max - t_min) / self.dt)) + 1
        self.t_grid = t_min + self.dt * np.arange(self.n_t)
        self.density, self.panel_length, self.quad_order = "custom", panel_length, quad_order
        self._quad_offsets, self._quad_weights = local_gauss_legendre_panels(self.L, panel_length, quad_order)
        self._quad_nodes = self.A + self._quad_offsets
        self._quad_u = self._quad_offsets - 0.5 * self.L
        self._quad_coeffs = self._window_at_offsets(self._quad_offsets) * dbar(self._quad_nodes) * self._quad_weights
        self.smooth = nufft_uniform_t(self._quad_u, self._quad_coeffs, self.t_grid[0], self.dt, self.n_t)


def fold(x, nbar, dbar, guess):
    E = np.asarray(guess, dtype=np.float64).copy()
    for _ in range(100):
        step = (nbar(E) - x) / dbar(E)
        E = E - step
        if np.max(np.abs(step)) < 1e-11 * max(1.0, float(np.max(np.abs(E)))):
            break
    return E


def goe_central_levels(n, retained_fraction, rng):
    """β-Hermite tridiagonal (Dumitriu–Edelman) com β = 1; mesma construção do gerador GUE congelado, com β trocado."""
    dim = int(math.ceil(n / retained_fraction))
    diag = rng.normal(0.0, 1.0, size=dim)
    k = 1.0 * np.arange(dim - 1, 0, -1, dtype=np.float64)          # χ_{β(n−i)}, β = 1
    sub = np.sqrt(rng.gamma(shape=k / 2.0, scale=2.0)) / math.sqrt(2.0)
    scale = 1.0 / math.sqrt(2.0 * dim)                             # raio do semicírculo √(2βN)
    ev = eigvalsh_tridiagonal(diag * scale, sub * scale)
    u = dim * semicircle_cdf(ev)
    s = (dim - n) // 2
    return u[s:s + n]


def proxy_unfolded(n, kind, rng):
    if kind == "gue":
        y = generate_gue_central_levels(n, 0.6, rng)[0]
    elif kind == "goe":
        y = goe_central_levels(n, 0.6, rng)
    elif kind == "poisson":
        y = np.concatenate([[0.0], np.cumsum(rng.exponential(1.0, n - 1))])
    else:
        raise ValueError(kind)
    return (y - y[0]) * (n - 1) / (y[-1] - y[0])


def power_block(A, B, n, nbar, dbar, catalog, kind, seed, B_sigma=200, B_thr=999, t_min=0.5, t_max=5.0):
    rng = np.random.default_rng(seed)
    x0, x1 = float(nbar(np.array([A]))[0]), float(nbar(np.array([B]))[0])
    guess = np.linspace(A, B, n)
    lev = fold(x0 + proxy_unfolded(n, kind, rng) * (x1 - x0) / (n - 1), nbar, dbar, guess)
    tr = DensityTransform(lev[0], lev[-1], t_min, t_max, dbar)
    fwhm, W0 = tr.response["fwhm"], tr.response["gain_W0"]
    xs = nbar(lev)
    s = np.diff(xs)

    def shuffled():
        return fold(shuffle_spacings(s, origin_x=float(xs[0]), rng=rng), nbar, dbar, lev)

    powers = np.array([np.abs(tr.transform(shuffled())) ** 2 for _ in range(B_sigma)])
    sigma = null_noise_profile(np.sqrt(powers), tr.t_grid, 0.05)
    null_max = np.array([max_statistic(tr.transform(shuffled()), sigma) for _ in range(B_thr)])
    thr = threshold_interval(null_max, 0.05, 0.95)["z_high"]
    T = np.array([c[0] for c in catalog])
    sig_T = np.interp(T, tr.t_grid, sigma)
    rows = []
    for k, (t, c, tag) in enumerate(catalog):
        nb = np.min(np.abs(np.delete(T, k) - t)) if len(T) > 1 else np.inf
        z = abs(c) * W0 / (2.0 * sig_T[k])
        rows.append({"T": float(t), "abs_c": float(abs(c)), "tag": tag, "z_pred": float(z), "clear": bool(z >= 1.5 * thr),
                     "resolved_2fwhm": bool(nb >= 2 * fwhm), "sigma_c": float(2 * sig_T[k] / W0)})
    return {"A": float(lev[0]), "B": float(lev[-1]), "n": n, "kind": kind, "fwhm": fwhm, "threshold_z": float(thr),
            "n_clear": sum(r["clear"] for r in rows), "n_clear_resolved": sum(r["clear"] and r["resolved_2fwhm"] for r in rows),
            "z_pred_max": max(r["z_pred"] for r in rows), "lines": rows}


# ------------------------------------------------------------------ densidades e catálogos

def zeta_block():
    nbar = lambda E: (E / TWO_PI) * (np.log(E / TWO_PI) - 1.0) + 7.0 / 8.0           # noqa: E731
    dbar = lambda E: np.log(E / TWO_PI) / TWO_PI                                       # noqa: E731
    cat = [(c["period_theoretical"], c["coefficient_theoretical"], f"{c['prime']}^{c['repetition']}")
           for c in ar.prime_power_catalog(0.5, 5.0)]
    return nbar, dbar, cat


def dirichlet_blocks(name):
    ch = CHARACTERS[name]
    nbar = lambda E: ic.n_bar_chi(E, ch.q, ch.kappa)                                   # noqa: E731
    dbar = lambda E: ic.d_bar_chi(E, ch.q)                                             # noqa: E731
    cat = [(c["period_theoretical"], c["coefficient_theoretical"], f"n={c['prime']**c['repetition']},chi={c['chi']}")
           for c in ic.chi_catalog_module(ch).prime_power_catalog(0.5, 5.0)]
    blocks = []
    for j, (i0, i1) in enumerate(((1, 3000), (3001, 6000), (6001, 9000), (9001, 12000))):
        A, B = (float(v) for v in ic.inverse_n_bar_chi(np.array([i0 - 0.5, i1 - 0.5]), ch.q, ch.kappa))
        blocks.append((("e" if name == "chi_m4" else "f") + f"0{j + 1}", A, B, i1 - i0 + 1))
    return nbar, dbar, cat, blocks


def stadium():
    Aq, Lq = 1 + math.pi / 4, 4 + math.pi / 2
    nbar = lambda k: Aq * k * k / (4 * math.pi) - Lq * k / (4 * math.pi)               # noqa: E731
    dbar = lambda k: Aq * k / TWO_PI - Lq / (4 * math.pi)                              # noqa: E731
    d1e = json.loads((ROOT / "results/etapa11_6_controles/estadio/d1e_verificacoes.json").read_text())
    blocks = []
    for name, b in d1e["blocks"].items():
        C = abs(complex(*b["C_fit"]))
        cat = [(2.0, C, "bb m=1"), (4.0, C / math.sqrt(2), "bb m=2 (descritiva)")]
        blocks.append((name, b["A"], b["B"], 3000, cat))
    return nbar, dbar, blocks


def main():
    t0 = time.time()
    out = {"script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "blocks": {}}

    # validação 1: ζ, bloco d01 de m4-v3 (execução run_20260913_220906, Hann): 15 linhas claras, z máx 8,40
    nbar, dbar, cat = zeta_block()
    out["blocks"]["zeta_d01_validacao"] = power_block(54512.241266402, 56585.923346771, 3000, nbar, dbar, cat, "gue", 1)
    # validação 2: Maass S2 e S1 (ctrl-maass-v1, execucao_v3), densidade ajustada registrada
    lines = im.load_g1_lines()
    catm = [(ln["length"], ln["coefficient"], f"d={ln['delta']},n={ln['trace']}") for ln in lines if 0.5 <= ln["length"] <= 5]
    for name, i0, i1 in (("S2", 342, 1092), ("S1", 1, 341)):
        bm = json.loads((ROOT / f"results/etapa11_6_controles/maass/execucao_v3/{name}/block_metrics.json").read_text())
        sp = bm["smooth_fit"]
        out["blocks"][f"maass_{name}_validacao"] = power_block(bm["instrument"]["A"], bm["instrument"]["B"], i1 - i0 + 1,
                                                               lambda R, sp=sp: im.n_bar(R, sp), lambda R, sp=sp: im.d_bar(R, sp),
                                                               catm, "poisson", 2)
    # previsão: Dirichlet (GUE) e estádio (GOE)
    for chn in ("chi_m4", "chi_5"):
        nbar, dbar, cat, blocks = dirichlet_blocks(chn)
        for bname, A, B, n in blocks:
            out["blocks"][f"dirichlet_{bname}"] = power_block(A, B, n, nbar, dbar, cat, "gue", 3)
    nbar, dbar, blocks = stadium()
    for bname, A, B, n, cat in blocks:
        out["blocks"][f"estadio_{bname}"] = power_block(A, B, n, nbar, dbar, cat, "goe", 4)
    out["seconds"] = round(time.time() - t0, 1)
    (HERE / "analise_poder.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    for k, v in out["blocks"].items():
        print(f"{k:24s} n={v['n']:5d} FWHM={v['fwhm']:.4f} limiar={v['threshold_z']:.2f}  claras={v['n_clear']:3d}  "
              f"claras+resolvidas={v['n_clear_resolved']:3d}  z_max={v['z_pred_max']:.2f}")
    print("segundos:", out["seconds"])


if __name__ == "__main__":
    main()
