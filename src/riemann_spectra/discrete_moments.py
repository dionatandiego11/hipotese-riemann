"""
riemann_spectra.discrete_moments
Momentos negativos discretos Σ_{0<γ≤T} 1/|L′(ρ,χ)|² e o teste da Conjectura 7 de Pearce-Crump (arXiv:2606.25094).

Normalização por zero: v_n = log(qγ_n/2π) / |L′(ρ_n,χ)|². Como dN/dT = log(qT/2π)/2π, a conjectura
Σ 1/|L′|² ∼ (A_q/2π)T equivale, em primeira ordem, a média de v_n → A_q, com A_q = (6/π²)∏_{p|q} p/(p+1).
Para ζ (q = 1), A_1 = 6/π² (Gonek: 3/π³ = A_1/2π).
O teste diferencial compara χ com ζ na mesma densidade local log(qγ/2π) (bins), cancelando em primeira ordem o viés de
altura finita comum; prevê R = A_q/A_1 = ∏_{p|q} p/(p+1).
"""

from __future__ import annotations

import math
from typing import Dict, Sequence

import numpy as np


def arithmetic_factor(q: int) -> float:
    """∏_{p|q} p/(p+1)."""
    f, n, p = 1.0, q, 2
    while n > 1 and p * p <= n:
        if n % p == 0:
            f *= p / (p + 1)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        f *= n / (n + 1)
    return f


def A_q(q: int) -> float:
    return 6.0 / math.pi**2 * arithmetic_factor(q)


def normalized_reciprocal(gammas: np.ndarray, derivs: np.ndarray, q: int) -> np.ndarray:
    """v_n = log(qγ/2π)/|L′|²."""
    g = np.asarray(gammas, dtype=np.float64)
    return np.log(q * g / (2 * math.pi)) / np.asarray(derivs, dtype=np.float64) ** 2


def matched_expectation(dens_test: np.ndarray, dens_ref: np.ndarray, v_ref: np.ndarray, edges: np.ndarray) -> float:
    """Média de v_ref reponderada para a distribuição de densidades de dens_test (bins em `edges`)."""
    it = np.digitize(dens_test, edges) - 1
    ir = np.digitize(dens_ref, edges) - 1
    tot, n = 0.0, 0
    for b in np.unique(it):
        sel = ir == b
        if not np.any(sel):
            raise ValueError(f"bin {b} sem referência")
        k = int(np.sum(it == b))
        tot += k * float(np.mean(v_ref[sel]))
        n += k
    return tot / n


def block_bootstrap_ratio(v_test: np.ndarray, dens_test: np.ndarray, v_ref: np.ndarray, dens_ref: np.ndarray,
                          edges: np.ndarray, block: int, reps: int, rng: np.random.Generator) -> Dict[str, float]:
    """
    R = média(v_test) / E_ref[v | densidades do teste]. IC por bootstrap de blocos contíguos (reamostra blocos nos
    dois conjuntos, de forma independente). Percentis 2,5 e 97,5.
    """
    def resample(x, d):
        nb = len(x) // block
        idx = rng.integers(0, nb, nb)
        sel = np.concatenate([np.arange(i * block, (i + 1) * block) for i in idx])
        return x[sel], d[sel]

    R0 = float(np.mean(v_test)) / matched_expectation(dens_test, dens_ref, v_ref, edges)
    Rs = []
    for _ in range(reps):
        vt, dt = resample(v_test, dens_test)
        vr, dr = resample(v_ref, dens_ref)
        try:
            Rs.append(float(np.mean(vt)) / matched_expectation(dt, dr, vr, edges))
        except ValueError:
            continue
    Rs = np.array(Rs)
    return {"R": R0, "q025": float(np.quantile(Rs, 0.025)), "q975": float(np.quantile(Rs, 0.975)),
            "reps_validas": int(len(Rs))}
