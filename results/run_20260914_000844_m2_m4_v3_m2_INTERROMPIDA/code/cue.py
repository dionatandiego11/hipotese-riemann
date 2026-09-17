"""
riemann_spectra.cue
Análise SECUNDÁRIA: correção de altura finita da distribuição de espaçamentos segundo
Bogomolny, Bohigas, Leboeuf & Monastra (2006), arXiv:math/0602270 (§2–3).

  CUE_N:   p_N(s) = p_0(s) + p_1(s) / N^2 + O(N^-4)                       (eq. 23)
           E_N(s) = det[ delta_jk - sin(pi s (j-k)/N) / (pi (j-k)) ],  p_N = E_N''   (eqs. 21–22)
  Zeros:   p(s) ~ p_0(s) + p_1(alpha s) / N_eff^2                          (eq. 24, heurístico)
           N_eff = log(E/2pi)/sqrt(12 Lambda), Lambda = 1.57314...          (eq. 19)
           alpha = 1 + C / log(E/2pi),         C = 1.4720...                (eq. 18)

A distribuição acumulada é F(s) = 1 + E'(s) (pois E(0) = 1 e E'(0) = -1).
O artigo valida a fórmula com N_eff ~ 7,7 e 11,3 (E ~ 1e15 e 1e22). Nas alturas deste projeto
N_eff ~ 2: fora do domínio validado; o erro O(N^-4) é medido em `expansion_domain_table`.
Esta análise não altera nenhuma decisão do experimento confirmatório.
"""

import math
from typing import Any, Dict, List

import numpy as np

LAMBDA_BBLM = 1.57314
C_BBLM = 1.4720


def n_eff(E: float | np.ndarray) -> float | np.ndarray:
    return np.log(np.asarray(E, dtype=np.float64) / (2 * math.pi)) / math.sqrt(12.0 * LAMBDA_BBLM)


def alpha_scale(E: float | np.ndarray) -> float | np.ndarray:
    return 1.0 + C_BBLM / np.log(np.asarray(E, dtype=np.float64) / (2 * math.pi))


# ---------------------------------------------------------------------------
# Probabilidades de lacuna
# ---------------------------------------------------------------------------

def gap_probability_cue(s: float, N: int) -> float:
    """E_N(s) exato para CUE_N (eq. 22), s em unidades de espaçamento médio, 0 <= s <= N."""
    j = np.arange(N)
    d = j[:, None] - j[None, :]
    with np.errstate(divide="ignore", invalid="ignore"):
        M = np.where(d == 0, s / N, np.sin(math.pi * s * d / N) / (math.pi * np.where(d == 0, 1, d)))
    return float(np.linalg.det(np.eye(N) - M))


def gap_probability_sine(s: float, m: int = 48) -> float:
    """
    E_0(s) = det(I - K_sine) em [0, s] por Gauss-Legendre (método de Bornemann), na forma
    M_ij = (s/2) sqrt(w_i w_j) sinc(s (xi_i - xi_j)/2), analítica em s (vale também para s < 0,
    o que permite diferenças centrais em s = 0).
    """
    xi, w = np.polynomial.legendre.leggauss(m)
    sw = np.sqrt(w)
    M = 0.5 * s * sw[:, None] * np.sinc(0.5 * s * (xi[:, None] - xi[None, :])) * sw[None, :]
    return float(np.linalg.det(np.eye(m) - M))


def _derivatives(fun, s_grid: np.ndarray, h: float = 2e-3) -> Dict[str, np.ndarray]:
    """E, E' e E'' por diferenças centrais de quarta ordem."""
    E = np.array([fun(s) for s in s_grid])
    fp = np.array([[fun(s + k * h) for k in (-2, -1, 1, 2)] for s in s_grid])  # E analítica: sem truncar em 0
    d1 = (fp[:, 0] - 8 * fp[:, 1] + 8 * fp[:, 2] - fp[:, 3]) / (12 * h)
    d2 = (-fp[:, 0] + 16 * fp[:, 1] - 30 * E + 16 * fp[:, 2] - fp[:, 3]) / (12 * h * h)
    return {"E": E, "dE": d1, "d2E": d2}


def spacing_distribution_cue(s_grid: np.ndarray, N: int) -> Dict[str, np.ndarray]:
    der = _derivatives(lambda s: gap_probability_cue(s, N), s_grid)
    return {"pdf": der["d2E"], "cdf": 1.0 + der["dE"]}


def spacing_distribution_limit(s_grid: np.ndarray, m: int = 48) -> Dict[str, np.ndarray]:
    der = _derivatives(lambda s: gap_probability_sine(s, m), s_grid)
    return {"pdf": der["d2E"], "cdf": 1.0 + der["dE"]}


def first_correction(s_grid: np.ndarray, N_values: List[int] = (32, 64)) -> Dict[str, np.ndarray]:
    """
    p_1 e P_1 = int_0^s p_1 por extrapolação de Richardson em 1/N^2:
      A_N = N^2 (p_N - p_0) = p_1 + p_2/N^2 + ...;  p_1 ~ (4 A_{2N} - A_N)/3 com N_values = (N, 2N).
    """
    N1, N2 = N_values
    if N2 != 2 * N1:
        raise ValueError("Richardson implementado para N_values = (N, 2N).")
    lim = spacing_distribution_limit(s_grid)
    a = spacing_distribution_cue(s_grid, N1)
    b = spacing_distribution_cue(s_grid, N2)
    A1p, A2p = N1 ** 2 * (a["pdf"] - lim["pdf"]), N2 ** 2 * (b["pdf"] - lim["pdf"])
    A1c, A2c = N1 ** 2 * (a["cdf"] - lim["cdf"]), N2 ** 2 * (b["cdf"] - lim["cdf"])
    return {
        "s": s_grid,
        "p0": lim["pdf"], "P0": lim["cdf"],
        "p1": (4 * A2p - A1p) / 3.0, "P1": (4 * A2c - A1c) / 3.0,
        "richardson_change_pdf_max": float(np.max(np.abs(A2p - A1p))),
    }


def zeros_prediction(corr: Dict[str, np.ndarray], E: float) -> Dict[str, Any]:
    """
    Predição heurística (eq. 24) em altura E:
      p(s) = p_0(s) + p_1(alpha s)/N_eff^2;   F(s) = P_0(s) + P_1(alpha s)/(alpha N_eff^2).
    """
    s = corr["s"]
    ne = float(n_eff(E))
    al = float(alpha_scale(E))
    # m4-v3: p_1 e P_1 avaliados exatamente em alpha·s (m4-v2 interpolava linearmente na malha de s,
    # erro de até 3,9e-5 na CDF; ver AUDITORIA_INDEPENDENTE §4)
    scaled = first_correction(al * s)
    p1_scaled = scaled["p1"]
    P1_scaled = scaled["P1"]
    return {
        "E": E, "N_eff": ne, "alpha": al,
        "pdf": corr["p0"] + p1_scaled / ne ** 2,
        "cdf": corr["P0"] + P1_scaled / (al * ne ** 2),
    }


def expansion_domain_table(s_grid: np.ndarray, corr: Dict[str, np.ndarray], N_values=(2, 3, 4, 6, 8, 12, 16)) -> List[Dict[str, float]]:
    """Erro da expansão truncada p_0 + p_1/N^2 contra o CUE_N exato, por N (domínio de validade)."""
    rows = []
    for N in N_values:
        ex = spacing_distribution_cue(s_grid[s_grid <= N], N)
        m = s_grid <= N
        approx_pdf = corr["p0"][m] + corr["p1"][m] / N ** 2
        approx_cdf = corr["P0"][m] + corr["P1"][m] / N ** 2
        rows.append({
            "N": int(N),
            "sup_abs_error_pdf_truncated": float(np.max(np.abs(ex["pdf"] - approx_pdf))),
            "sup_abs_error_cdf_truncated": float(np.max(np.abs(ex["cdf"] - approx_cdf))),
            "sup_abs_correction_cdf": float(np.max(np.abs(corr["P1"][m] / N ** 2))),
            "sup_abs_error_pdf_limit_only": float(np.max(np.abs(ex["pdf"] - corr["p0"][m]))),
        })
    return rows


# ---------------------------------------------------------------------------
# Simulação de Haar (validação independente das fórmulas)
# ---------------------------------------------------------------------------

def sample_cue_spacings(N: int, n_matrices: int, rng: np.random.Generator, batch: int = 2048) -> np.ndarray:
    """Espaçamentos normalizados (N/2pi) de autofases de matrizes CUE_N (QR com correção de fase de Mezzadri)."""
    out = []
    left = n_matrices
    while left > 0:
        b = min(batch, left)
        Z = (rng.normal(size=(b, N, N)) + 1j * rng.normal(size=(b, N, N))) / math.sqrt(2.0)
        Q, R = np.linalg.qr(Z)
        d = np.diagonal(R, axis1=1, axis2=2)
        Q = Q * (d / np.abs(d))[:, None, :]
        phases = np.sort(np.angle(np.linalg.eigvals(Q)), axis=1)
        gaps = np.diff(np.concatenate([phases, phases[:, :1] + 2 * math.pi], axis=1), axis=1)
        out.append((gaps * N / (2 * math.pi)).ravel())
        left -= b
    return np.concatenate(out)
