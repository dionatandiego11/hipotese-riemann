"""
riemann_spectra.number_variance
Variância numérica Σ²(L) de níveis unfolded: estimador, fórmula GUE e fórmula semiclássica de Berry (1988).

Convenções (unidades unfolded, espaçamento médio 1):
- n(L; y) = #{x_m ∈ [y − L/2, y + L/2]};  V(L) = média em y de [n(L; y) − L]²  (definição de Berry; não subtrai
  a média amostral de n, de modo que um viés de unfolding aparece em V).
- GUE:  Σ²(L) = (1/π²)[log(2πL) + γ₀ + 1 − cos(2πL) − Ci(2πL)] + L[1 − (2/π) Si(2πL)].
- Berry (1988), eq. (19), tal como transcrita em Lugar, Milinovich e Quesada-Herrera (arXiv:2211.14918, §1.4):
      V ≈ Σ²_GUE(L) + (1/π²)[ 2 Σ_{n = p^r < X} w(n) sin²(π L r log p / Λ) / (r² p^r)
                               + Ci(2πLτ*) − log(2πLτ*) − γ₀ ],
  com Λ = log(E/2π) (o "tempo de Heisenberg" em unidades de log n) e X = (E/2π)^{τ*}. O último colchete troca a
  parte τ < τ* do fator de forma GUE, (2/π²)∫₀^{τ*} sin²(πLτ)/τ dτ = (1/π²)[γ₀ + log(2πLτ*) − Ci(2πLτ*)], pela
  soma diagonal sobre potências de primos (órbitas periódicas curtas).
- Extensão a L(s, χ) com χ real primitivo mod q (derivação própria, a conferir em fonte): Λ = log(qE/2π),
  X = (qE/2π)^{τ*} e peso w(p^r) = χ(p)^{2r} ∈ {0, 1}, isto é, primos que dividem q não contribuem.
"""

from __future__ import annotations

import math
from typing import Callable, Dict, Iterable, List, Optional, Sequence

import numpy as np
from scipy.special import sici

EULER_GAMMA = 0.5772156649015329


# --- fórmulas ------------------------------------------------------------------------------------------------------
def sigma2_gue(L: np.ndarray | float) -> np.ndarray | float:
    """Σ²(L) do GUE no limite N → ∞ (Mehta), em unidades unfolded."""
    L_arr = np.asarray(L, dtype=np.float64)
    x = 2.0 * math.pi * L_arr
    si, ci = sici(x)
    val = (np.log(x) + EULER_GAMMA + 1.0 - np.cos(x) - ci) / math.pi**2 + L_arr * (1.0 - 2.0 * si / math.pi)
    return float(val) if np.ndim(L) == 0 else val


def prime_powers(limit: float) -> List[tuple]:
    """Lista de (p, r, p**r) com p**r < limit."""
    n = int(math.floor(limit))
    if n < 2:
        return []
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    out = []
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        pr, r = p, 1
        while pr < limit:
            out.append((p, r, pr))
            pr *= p
            r += 1
    return out


def sigma2_berry(L: np.ndarray | float, E: float, tau_star: float = 0.5, q: int = 1,
                 weight: Optional[Callable[[int], float]] = None) -> np.ndarray | float:
    """
    Fórmula semiclássica de Berry na altura E. Para ζ: q = 1 e weight = None (todos os primos com peso 1).
    Para L(s, χ) real: q = condutor e weight(p) = χ(p)² (0 se p | q, 1 caso contrário).
    """
    L_arr = np.atleast_1d(np.asarray(L, dtype=np.float64))
    lam = math.log(q * E / (2.0 * math.pi))
    if lam <= 0:
        raise ValueError("altura baixa demais: log(qE/2π) ≤ 0")
    X = math.exp(tau_star * lam)
    s = np.zeros_like(L_arr)
    for p, r, pr in prime_powers(X):
        w = 1.0 if weight is None else float(weight(p)) ** r  # χ(p^r)² = (χ(p)²)^r
        if w == 0.0:
            continue
        s += w * np.sin(math.pi * L_arr * r * math.log(p) / lam) ** 2 / (r * r * pr)
    y = 2.0 * math.pi * L_arr * tau_star
    ci = sici(y)[1]
    val = sigma2_gue(L_arr) + (2.0 * s + ci - np.log(y) - EULER_GAMMA) / math.pi**2
    return float(val[0]) if np.ndim(L) == 0 else val


def sigma2_berry_averaged(L: np.ndarray, E_values: Sequence[float], **kw) -> np.ndarray:
    """Média da fórmula de Berry sobre as alturas locais (espelha a média em y do estimador)."""
    return np.mean([sigma2_berry(L, float(E), **kw) for E in E_values], axis=0)


# --- estimador -----------------------------------------------------------------------------------------------------
def number_variance(x: np.ndarray, L_values: Iterable[float], step: float = 0.05,
                    n_sub: int = 10) -> Dict[str, np.ndarray]:
    """
    Estima V(L) em níveis unfolded ordenados x. Centros y numa grade regular de passo `step` em
    [x₀ + L/2, x_fim − L/2]. Incerteza: a faixa de y é dividida em `n_sub` sub-blocos contíguos; sigma = desvio-padrão
    entre sub-blocos / √n_sub (janelas sobrepostas não são tratadas como independentes).
    Retorna V, sigma, viés (média de n − L) e o número de centros, para cada L.
    """
    x = np.asarray(x, dtype=np.float64)
    if np.any(np.diff(x) <= 0):
        raise ValueError("níveis precisam estar estritamente ordenados")
    L_values = np.asarray(list(L_values), dtype=np.float64)
    V, sig, bias, ncent = [], [], [], []
    for L in L_values:
        y = np.arange(x[0] + L / 2.0, x[-1] - L / 2.0, step)
        if len(y) < n_sub * 10:
            raise ValueError(f"poucos centros para L = {L}")
        n = np.searchsorted(x, y + L / 2.0, side="right") - np.searchsorted(x, y - L / 2.0, side="left")
        d = n - L
        d2 = d * d
        subs = np.array([c.mean() for c in np.array_split(d2, n_sub)])
        V.append(d2.mean())
        sig.append(subs.std(ddof=1) / math.sqrt(n_sub))
        bias.append(d.mean())
        ncent.append(len(y))
    return {"L": L_values, "V": np.array(V), "sigma": np.array(sig), "bias": np.array(bias),
            "n_centers": np.array(ncent)}
