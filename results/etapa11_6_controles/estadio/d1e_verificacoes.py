"""
Verificações numéricas da derivação D1-E (controle ctrl-estadio-v1). Classe B. Não usa níveis do bilhar.

  (1) identidade de Poisson: eq. (52) de Bäcker  ==  (ak/2π) Σ_m J₁(2bmk)/m  (forma de Tanner, eq. (4));
  (2) amplitude complexa C(k) da linha L = 2 (forma exata com Hankel contra a assintótica);
  (3) C̄_bb previsto: o estimador congelado (targeted_joint_fit, band, conjugado) aplicado ao sinal analítico
      F_bb(t) = ∫_A^B w(k) e^{-i(k-E_c)t} d_bb(k) dk, nos blocos nominais g01–g04 da declaração.

Uso (da raiz):  .venv/bin/python3 results/etapa11_6_controles/estadio/d1e_verificacoes.py
"""
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy import special

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))
from riemann_spectra.arithmetic import targeted_joint_fit          # noqa: E402
from riemann_spectra.periods import measure_window_response, window_response  # noqa: E402

A_RECT, B_RAD = 1.0, 1.0            # a = comprimento do retângulo no quarto; b = raio (qust:2)
BLOCKS = {"g01": (85.4699, 169.3579), "g02": (169.3579, 223.5316), "g03": (223.5316, 266.8648),
          "g04": (266.8648, 304.0528)}


def backer_52(k, a=A_RECT):
    """N_fl^bb pela eq. (52) de Bäcker (caixa de comprimento 1: E_n = π²n²), com E = k²."""
    nmax = int(math.floor(k / math.pi))
    n = np.arange(1, nmax + 1)
    return (a / math.pi) * np.sum(np.sqrt(k * k - (math.pi * n) ** 2)) - (a / (4 * math.pi)) * k * k + (a / (2 * math.pi)) * k


def tanner_bessel(k, a=A_RECT, b=B_RAD, M=2_000_000):
    m = np.arange(1, M + 1, dtype=np.float64)
    return (a * k / (2 * math.pi)) * np.sum(special.j1(2 * b * m * k) / m)


def d_bb(k, a=A_RECT, b=B_RAD, M=10):
    """Densidade bouncing ball: d/dk de (ak/2π)Σ J₁(2bmk)/m = (abk/π) Σ_m J₀(2bmk)."""
    k = np.asarray(k, dtype=np.float64)
    return (a * b * k / math.pi) * sum(special.j0(2 * b * m * k) for m in range(1, M + 1))


def C_exact(k, a=A_RECT, b=B_RAD):
    """Linha m = 1: d₁(k) = (abk/π) J₀(2bk) = Re[C(k) e^{2ibk}], C(k) = (abk/π) H₀⁽¹⁾(2bk) e^{-2ibk}."""
    return (a * b * k / math.pi) * special.hankel1(0, 2 * b * k) * np.exp(-2j * b * k)


def C_asym(k, a=A_RECT, b=B_RAD):
    return (a * math.sqrt(b) / math.pi ** 1.5) * np.sqrt(k) * np.exp(-1j * math.pi / 4)


def predicted_block(A, B, catalog_T=(2.0, 4.0), n_quad=400_001):
    L = B - A
    Ec = 0.5 * (A + B)
    resp = measure_window_response(L, "hann")
    k = np.linspace(A, B, n_quad)
    w = np.sin(math.pi * (k - A) / L) ** 2
    dens = d_bb(k)
    hk = (B - A) / (n_quad - 1)
    wt = np.full(n_quad, hk); wt[0] = wt[-1] = hk / 2       # trapézio (integrando suave, nulo nas bordas)

    def F(t):
        t = np.atleast_1d(t)
        return np.array([np.sum(wt * w * dens * np.exp(-1j * (k - Ec) * tt)) for tt in t])

    cat = [{"catalog_index": i, "period_theoretical": T, "coefficient_theoretical": 1.0} for i, T in enumerate(catalog_T)]
    fit = targeted_joint_fit(F, cat, L, Ec, half_width=0.5 * resp["fwhm"], window="hann", sampling="band",
                             include_conjugate=True)
    C_fit = fit[0]["coefficient_real"] + 1j * fit[0]["coefficient_imag"]
    Cw = np.sum(wt * w * C_exact(k)) / np.sum(wt * w)          # média ponderada pela janela
    return {"A": A, "B": B, "L": L, "E_c": Ec, "fwhm": resp["fwhm"], "C_fit": [C_fit.real, C_fit.imag],
            "abs_C_fit": abs(C_fit), "arg_C_fit_over_pi": math.atan2(C_fit.imag, C_fit.real) / math.pi,
            "C_weighted_mean": [Cw.real, Cw.imag], "C_asym_at_Ec": [C_asym(Ec).real, C_asym(Ec).imag],
            "rel_diff_fit_vs_weighted": abs(C_fit / Cw - 1), "C4_fit": [fit[1]["coefficient_real"], fit[1]["coefficient_imag"]]}


def main():
    out = {"script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    rows = []
    for k in (20.3, 85.47, 150.0, 223.53, 304.05):
        s1, s2 = backer_52(k), tanner_bessel(k)
        rows.append({"k": k, "backer_52": s1, "tanner_bessel_M2e6": s2, "diff": s1 - s2})
    out["poisson"] = rows
    out["C_exact_vs_asym"] = [{"k": k, "C_exact": [C_exact(k).real, C_exact(k).imag],
                               "rel_diff": abs(C_exact(k) / C_asym(k) - 1)} for k in (85.47, 127.4, 304.05)]
    out["blocks"] = {name: predicted_block(*ab) for name, ab in BLOCKS.items()}
    print(json.dumps(out, indent=2))
    (Path(__file__).parent / "d1e_verificacoes.json").write_text(json.dumps(out, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
