"""
riemann_indep.spectral — estatísticas M2 (A24) e análise CUE secundária (A25), caminhos independentes.
"""

from __future__ import annotations

import math

import numpy as np
from numpy.polynomial import chebyshev as C

TAU = 2.0 * math.pi


# ============================================================================ M2
def spacing_cdf(x_unfolded: np.ndarray, grid: np.ndarray) -> np.ndarray:
    s = np.sort(np.diff(np.asarray(x_unfolded, float)))
    return np.searchsorted(s, grid, side="right") / len(s)


def pair_correlation(x: np.ndarray, s_max: float = 5.0, bins: int = 50) -> np.ndarray:
    """R₂ com normalização de contagem fixa: contagem·L²/(n(n−1)·∫_bin (L − s) ds)."""
    x = np.sort(np.asarray(x, float))
    n = len(x)
    L = x[-1] - x[0]
    hi = np.searchsorted(x, x + s_max, side="right")
    diffs = np.concatenate([x[i + 1:hi[i]] - x[i] for i in range(n) if hi[i] > i + 1])
    edges = np.linspace(0.0, s_max, bins + 1)
    counts = np.bincount(np.clip(np.searchsorted(edges, diffs, side="right") - 1, 0, bins - 1), minlength=bins)
    a, b = edges[:-1], edges[1:]
    exposure = L * (b - a) - 0.5 * (b * b - a * a)
    return counts * L * L / (n * (n - 1) * exposure)


def form_factor_connected(x: np.ndarray, tau: np.ndarray, n_sub: int = 10) -> np.ndarray:
    """K_c = Σ_b |Z_b − μ_b|² / Σ_b Q_b, sub-blocos contíguos, Hann por sub-bloco, μ analítico."""
    x = np.sort(np.asarray(x, float))
    num = np.zeros(len(tau))
    Qtot = 0.0
    for part in np.array_split(x, n_sub):
        a, b = part[0], part[-1]
        L = b - a
        w = 0.5 - 0.5 * np.cos(TAU * (part - a) / L)
        ph = np.exp(-1j * TAU * np.multiply.outer(tau, part))
        Z = ph @ w
        # μ = ∫_a^b w e^{-2πiτx} dx = e^{-2πiτ(a+L/2)} ∫_{-L/2}^{L/2} (1/2 + cos(2πu/L)/2) e^{-2πiτu} du
        om = TAU * tau
        k = TAU / L

        def S(v):
            vs = np.where(np.abs(v) < 1e-14, 1.0, v)
            return np.where(np.abs(v) < 1e-14, L, 2 * np.sin(vs * L / 2) / vs)

        mu = np.exp(-1j * om * (a + L / 2)) * (0.5 * S(om) + 0.25 * S(om - k) + 0.25 * S(om + k))
        num += np.abs(Z - mu) ** 2
        Qtot += 3.0 * L / 8.0
    return num / Qtot


def symmetric_rank_p(obs: np.ndarray, ensemble: np.ndarray) -> float:
    """p = #{membros com d ≥ d_obs}/(B+1), d = RMS até a média dos outros B membros."""
    pool = np.vstack([obs[None, :], ensemble])
    B = len(ensemble)
    tot = pool.sum(axis=0)
    d = np.sqrt(np.mean((pool - (tot[None, :] - pool) / B) ** 2, axis=1))
    return float(np.mean(d >= d[0]) * (B + 1) / (B + 1))


# ============================================================================ CUE (Bogomolny et al. 2006)
LAMBDA = 1.57314
CB = 1.4720


def clenshaw_curtis(m: int):
    """Nós e pesos de Clenshaw–Curtis em [−1, 1] (m+1 pontos)."""
    th = math.pi * np.arange(m + 1) / m
    x = np.cos(th)
    w = np.zeros(m + 1)
    for j in range(m + 1):
        s = 0.0
        for k in range(1, m // 2 + 1):
            bk = 1.0 if 2 * k == m else 2.0
            s += bk * math.cos(2 * k * th[j]) / (4 * k * k - 1)
        cj = 1.0 if j in (0, m) else 2.0
        w[j] = cj / m * (1.0 - s)
    return x, w


_CC = clenshaw_curtis(64)


def gap_sine(s: float) -> float:
    """E₀(s) = det(I − K_seno) em [0, s] com quadratura de Clenshaw–Curtis."""
    if s <= 0:
        return 1.0
    xi, wi = _CC
    x = 0.5 * s * (xi + 1.0)
    w = 0.5 * s * wi
    K = np.sinc(np.subtract.outer(x, x))
    sw = np.sqrt(w)
    return float(np.linalg.det(np.eye(len(x)) - sw[:, None] * K * sw[None, :]))


def gap_cue_toeplitz(s: float, N: int) -> float:
    """E_N(s) = det[(1/2π)∫_θ^{2π} e^{i(j−k)φ}dφ], θ = 2πs/N (fórmula de Heine/Toeplitz)."""
    th = TAU * s / N
    m = np.subtract.outer(np.arange(N), np.arange(N))
    with np.errstate(divide="ignore", invalid="ignore"):
        M = np.where(m == 0, (TAU - th) / TAU, (1.0 - np.exp(1j * m * th)) / (TAU * 1j * np.where(m == 0, 1, m)))
    return float(np.real(np.linalg.det(M)))


def cheb_model(fun, a: float, b: float, deg: int = 90):
    k = np.arange(deg + 1)
    nodes = np.cos(math.pi * (k + 0.5) / (deg + 1))
    s = 0.5 * (b - a) * nodes + 0.5 * (a + b)
    vals = np.array([fun(v) for v in s])
    coef = C.chebfit(nodes, vals, deg)
    scale = 2.0 / (b - a)

    def evaluate(u, der=0):
        z = (2 * np.asarray(u, float) - (a + b)) / (b - a)
        c = coef
        for _ in range(der):
            c = C.chebder(c) * scale
        return C.chebval(z, c)

    return evaluate


class CUECorrection:
    """p₀, P₀, p₁, P₁ por modelos de Chebyshev de E₀, E₃₂, E₆₄ em [0, 5]; Richardson em 1/N²."""

    def __init__(self, s_hi: float = 5.0):
        self.E0 = cheb_model(gap_sine, 0.0, s_hi)
        self.E32 = cheb_model(lambda v: gap_cue_toeplitz(v, 32), 0.0, s_hi)
        self.E64 = cheb_model(lambda v: gap_cue_toeplitz(v, 64), 0.0, s_hi)

    def P0(self, s):
        return 1.0 + self.E0(s, 1)

    def p0(self, s):
        return self.E0(s, 2)

    def P1(self, s):
        A32 = 32 ** 2 * (self.E32(s, 1) - self.E0(s, 1))
        A64 = 64 ** 2 * (self.E64(s, 1) - self.E0(s, 1))
        return (4 * A64 - A32) / 3.0

    def p1(self, s):
        A32 = 32 ** 2 * (self.E32(s, 2) - self.E0(s, 2))
        A64 = 64 ** 2 * (self.E64(s, 2) - self.E0(s, 2))
        return (4 * A64 - A32) / 3.0


def n_eff(E):
    return np.log(np.asarray(E, float) / TAU) / math.sqrt(12 * LAMBDA)


def alpha_bblm(E):
    return 1.0 + CB / np.log(np.asarray(E, float) / TAU)


def cue_prediction(corr: CUECorrection, E: float, s: np.ndarray):
    ne, al = float(n_eff(E)), float(alpha_bblm(E))
    return {"N_eff": ne, "alpha": al,
            "cdf": corr.P0(s) + corr.P1(al * s) / (al * ne * ne),
            "pdf": corr.p0(s) + corr.p1(al * s) / (ne * ne)}
