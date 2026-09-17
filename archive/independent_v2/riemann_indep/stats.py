"""
riemann_indep.stats — ensembles, detector, limiares, catálogo, matching e medição direcionada.
Escrito a partir de PROTOCOLO §7.2, §8.2–8.3, §9.2–9.3 e das resoluções A5–A23 de SPEC_REVIEW.md.
"""

from __future__ import annotations

import math

import numpy as np
from scipy import linalg as sla
from scipy.optimize import linear_sum_assignment
from scipy.stats import binom

from .core import TAU, hann_response, nbar, nbar_inverse


# ============================================================================ ensembles
def shuffle_null(gammas: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """A7: permuta os espaçamentos unfolded e reconstrói em energia."""
    x = nbar(gammas)
    s = rng.permutation(np.diff(x))
    return nbar_inverse(np.concatenate([[x[0]], x[0] + np.cumsum(s)]))


def gue_tridiagonal_eigs(n: int, rng: np.random.Generator) -> np.ndarray:
    """
    Dumitriu–Edelman (β = 2): H = (1/√2)·tridiag(diag N(0,2), off χ_{2(n−1)},…,χ_2).
    Equivale a GUE com E|H_ij|² = 1 fora da diagonal ⇒ raio do semicírculo 2√n. Retorna autovalores / (2√n).
    """
    d = rng.normal(0.0, math.sqrt(2.0), n) / math.sqrt(2.0)
    dof = 2.0 * np.arange(n - 1, 0, -1)
    e = np.sqrt(rng.chisquare(dof)) / math.sqrt(2.0)
    ev = sla.eigh_tridiagonal(d, e, eigvals_only=True)
    return np.sort(ev) / (2.0 * math.sqrt(n))


def gue_dense_eigs(n: int, rng: np.random.Generator) -> np.ndarray:
    """GUE denso: G complexo com E|G_ij|² = 1, H = (G + G*)/√2 ⇒ E|H_ij|² = 1 (i≠j), H_ii ~ N(0,1)."""
    G = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / math.sqrt(2.0)
    H = (G + G.conj().T) / math.sqrt(2.0)
    return np.sort(np.linalg.eigvalsh(H)) / (2.0 * math.sqrt(n))


def semicircle_cdf(y: np.ndarray) -> np.ndarray:
    y = np.clip(y, -1.0, 1.0)
    return 0.5 + (y * np.sqrt(1 - y * y) + np.arcsin(y)) / math.pi


def gue_central_unfolded(n: int, rng: np.random.Generator, fraction: float = 0.6) -> np.ndarray:
    dim = int(math.ceil(n / fraction))
    ev = gue_tridiagonal_eigs(dim, rng)
    x = dim * semicircle_cdf(ev)
    i0 = (dim - n) // 2
    return x[i0:i0 + n]


def gue_null(gammas: np.ndarray, rng: np.random.Generator, fraction: float = 0.6) -> np.ndarray:
    """A8."""
    y = gue_central_unfolded(len(gammas), rng, fraction)
    x0, x1 = nbar(gammas[0]), nbar(gammas[-1])
    return nbar_inverse(x0 + (y - y[0]) * (x1 - x0) / (y[-1] - y[0]))


def poisson_fixed(n: int, rng: np.random.Generator) -> np.ndarray:
    return np.sort(rng.uniform(0.0, float(n - 1), n))


def inject_lines(x_levels: np.ndarray, T: np.ndarray, C: np.ndarray, iters: int = 80) -> np.ndarray:
    """Resolve N̄(E) + Σ Re[C e^{iET}/(iT)] = x por Newton salvaguardado a partir de N̄^{-1}(x)."""
    E = nbar_inverse(x_levels)
    T = np.asarray(T, float)
    C = np.asarray(C, complex)
    for _ in range(iters):
        ph = np.exp(1j * np.multiply.outer(E, T))
        G = nbar(E) + np.real(ph @ (C / (1j * T))) - x_levels
        dG = np.log(E / TAU) / TAU + np.real(ph @ C)
        if np.any(dG <= 0):
            raise ValueError("densidade modulada não positiva")
        stepv = G / dG
        E = E - np.clip(stepv, -0.5, 0.5)
        if np.max(np.abs(stepv)) < 1e-12:
            break
    return E


# ============================================================================ detector
def sigma_profile(powers_mean: np.ndarray, dt: float, width: float = 0.05) -> np.ndarray:
    """A5/A6: média móvel (ímpar mais próximo de width/dt) da potência média, bordas refletidas, raiz."""
    m = int(round(width / dt))
    if m % 2 == 0:
        m += 1
    half = m // 2
    padded = np.concatenate([powers_mean[1:half + 1][::-1], powers_mean, powers_mean[-half - 1:-1][::-1]])
    cs = np.concatenate([[0.0], np.cumsum(padded)])
    return np.sqrt((cs[m:] - cs[:-m]) / m)


def local_peaks(z: np.ndarray, min_sep: int, floor: float) -> np.ndarray:
    """A9: máximos locais com z ≥ floor; supressão gulosa de não-máximos com separação ≥ min_sep pontos."""
    inner = np.arange(1, len(z) - 1)
    cand = inner[(z[inner] > z[inner - 1]) & (z[inner] >= z[inner + 1]) & (z[inner] >= floor)]
    order = cand[np.argsort(-z[cand], kind="stable")]
    kept: list[int] = []
    for i in order:
        if all(abs(i - j) >= min_sep for j in kept):
            kept.append(int(i))
    return np.array(sorted(kept), dtype=int)


def refine_period(t: np.ndarray, F: np.ndarray, i: int) -> float:
    """A14: vértice da parábola por |F|² em (i−1, i, i+1)."""
    y0, y1, y2 = (abs(F[i - 1]) ** 2, abs(F[i]) ** 2, abs(F[i + 1]) ** 2)
    den = y0 - 2 * y1 + y2
    off = 0.5 * (y0 - y2) / den if den < 0 else 0.0
    return float(t[i] + np.clip(off, -0.5, 0.5) * (t[1] - t[0]))


def order_stat_interval(null_max: np.ndarray, alpha: float = 0.05, conf: float = 0.95) -> dict:
    """A11/A12."""
    x = np.sort(np.asarray(null_max, float))
    B = len(x)
    p = 1 - alpha
    tail = (1 - conf) / 2
    ks = np.arange(0, B + 2)
    cdf = binom.cdf(ks - 1, B, p)          # P(K <= k-1)
    l = int(np.max(ks[(ks >= 1) & (cdf <= tail)])) if np.any((ks >= 1) & (cdf <= tail)) else 1
    sf = binom.sf(ks - 1, B, p)            # P(K >= k)
    u = int(np.min(ks[(ks <= B) & (sf <= tail)])) if np.any((ks <= B) & (sf <= tail)) else B
    # limiar pontual: menor s com (1 + #{x >= s})/(B+1) <= alpha
    kmax = int(math.floor(alpha * (B + 1) + 1e-9)) - 1
    point = float(np.nextafter(x[B - 1 - kmax], np.inf))
    return {"B": B, "l": l, "u": u, "z_low": float(x[l - 1]), "z_high": float(x[u - 1]), "point": point,
            "coverage": float(binom.cdf(u - 1, B, p) - binom.cdf(l - 1, B, p))}


def classify(z: float, iv: dict) -> str:
    if z > iv["z_high"]:
        return "detected"
    if z < iv["z_low"]:
        return "not_detected"
    return "inconclusive"


def blind_peaks(t, F, sigma, fwhm_points: int = 8, floor: float = 3.0):
    z = np.abs(F) / sigma
    idx = local_peaks(z, fwhm_points, floor)
    return [{"i": int(i), "t_grid": float(t[i]), "t": refine_period(t, F, int(i)), "z": float(z[i])} for i in idx], float(np.max(z))


# ============================================================================ aritmética (após congelamento)
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def catalog(t_lo: float, t_hi: float) -> list[dict]:
    """A16 por divisão por tentativa."""
    out = []
    for p in range(2, int(math.exp(t_hi)) + 2):
        if not is_prime(p):
            continue
        r = 1
        while r * math.log(p) <= t_hi:
            if r * math.log(p) >= t_lo:
                out.append({"p": p, "r": r, "T": r * math.log(p), "c": -math.log(p) / (math.pi * p ** (r / 2))})
            r += 1
    out.sort(key=lambda d: d["T"])
    return out


def match_greedy(periods: np.ndarray, T: np.ndarray, tol: float) -> dict[int, int]:
    pairs = sorted((abs(pp - tt), ci, pi) for ci, tt in enumerate(T) for pi, pp in enumerate(periods) if abs(pp - tt) <= tol)
    used_c, used_p, out = set(), set(), {}
    for _, ci, pi in pairs:
        if ci not in used_c and pi not in used_p:
            out[ci] = pi
            used_c.add(ci)
            used_p.add(pi)
    return out


def match_optimal(periods: np.ndarray, T: np.ndarray, tol: float) -> dict[int, int]:
    """Sensibilidade A18: atribuição que maximiza o número de pares e minimiza a distância total."""
    if len(periods) == 0:
        return {}
    D = np.abs(np.subtract.outer(T, periods))
    big = 1e6
    cost = np.where(D <= tol, D, big)
    r, c = linear_sum_assignment(cost)
    return {int(a): int(b) for a, b in zip(r, c) if D[a, b] <= tol}


def fit_band_conjugate(evaluate, T: np.ndarray, L: float, Ec: float, half: float, points: int = 9,
                       sampling: str = "band", conjugate: bool = True) -> np.ndarray:
    """A21: coeficientes complexos C_k; sistema real resolvido com LAPACK gelsy."""
    T = np.asarray(T, float)
    if sampling == "band":
        ts = np.unique(np.concatenate([np.linspace(x - half, x + half, points) for x in T]))
    else:
        ts = T.copy()
    Fv = evaluate(ts)
    P = np.exp(1j * Ec * T)
    Gm = 0.5 * hann_response(np.subtract.outer(ts, T), L) * P
    if conjugate:
        Hm = 0.5 * hann_response(np.add.outer(ts, T), L) * np.conj(P)
        cols_re = Gm + Hm            # multiplica Re C
        cols_im = 1j * (Gm - Hm)     # multiplica Im C
        M = np.vstack([np.hstack([cols_re.real, cols_im.real]), np.hstack([cols_re.imag, cols_im.imag])])
        rhs = np.concatenate([Fv.real, Fv.imag])
        sol = sla.lstsq(M, rhs, lapack_driver="gelsy")[0]
        K = len(T)
        return sol[:K] + 1j * sol[K:]
    Mc = Gm
    M = np.vstack([np.hstack([Mc.real, -Mc.imag]), np.hstack([Mc.imag, Mc.real])])
    rhs = np.concatenate([Fv.real, Fv.imag])
    sol = sla.lstsq(M, rhs, lapack_driver="gelsy")[0]
    K = len(T)
    return sol[:K] + 1j * sol[K:]


def phase_stats(Fgrid_at_T: np.ndarray, T: np.ndarray, c: np.ndarray, Ec: float):
    err = np.angle(Fgrid_at_T * np.exp(-1j * Ec * T) / np.sign(c))
    return float(abs(np.mean(np.exp(1j * err)))), float(np.mean(np.cos(err)))


def holm(p):
    p = np.asarray(p, float)
    m = len(p)
    o = np.argsort(p)
    adj = np.empty(m)
    run = 0.0
    for k, i in enumerate(o):
        run = max(run, min(1.0, (m - k) * p[i]))
        adj[i] = run
    return adj
