"""
riemann_spectra.bragg_peak
Previsão do fator de forma conectado em τ = 1 ("pico de Bragg") a partir da variância numérica.

Em τ = 1, Z(1) = Σ w_n e^{−2πi x_n}; com x_n = n − ½ − S_n (unfolding pela contagem suave e convenção do ponto médio),
|Z(1)|² depende só das diferenças S_n − S_m, isto é, dos desvios dos k-espaçamentos: D_k = x_{n+k} − x_n − k.
Modelo (heurístico, testado em GUE antes de usar nos zeros):
  (G) os D_k são gaussianos, com E[e^{2πi D_k}] = exp(−2π² V_k);
  (E) V_k = Var(D_k) ≈ Σ²(k) − 1/6: amostrar nos próprios níveis tira 1/12 de variância por extremidade em relação
      à amostragem uniforme, porque E_unif[F'(S)] = E_níveis[F(S+½) − F(S−½)] (identidade de integração por partes
      para S com saltos unitários), que com F = s³/3 dá E_unif[S²] = E_níveis[S²] + 1/12.
O substituto gaussiano sorteia S ~ N(0, C) com C_k = (V_∞ − V_k)/2 + c, o que reproduz Var(S_n − S_m) = V_{|n−m|},
e mede K_c(1) com o mesmo estimador dos dados.
"""

from __future__ import annotations

import math
from typing import Dict

import numpy as np
from scipy.linalg import toeplitz

from riemann_spectra.form_factor import compute_spectral_form_factor


def structure_from_sigma2(sigma2_at_k: np.ndarray, endpoint_correction: bool = True) -> np.ndarray:
    """V_k para k = 0..K a partir de Σ²(k) (k ≥ 1); V_0 = 0. Com endpoint_correction, subtrai 1/6."""
    v = np.asarray(sigma2_at_k, dtype=np.float64) - (1.0 / 6.0 if endpoint_correction else 0.0)
    v = np.maximum(v, 1e-12)
    return np.concatenate([[0.0], v])


_FACTOR_CACHE: Dict[tuple, np.ndarray] = {}


def _factor(V: np.ndarray, n: int) -> np.ndarray:
    key = (n, V[:n].tobytes())
    if key not in _FACTOR_CACHE:
        Vn = V[:n]
        c0 = 0.5 * float(np.max(Vn)) + 1e-6
        w, U = np.linalg.eigh(toeplitz(c0 - 0.5 * Vn))
        if w.min() < -1e-2 * w.max():
            raise ValueError(f"estrutura V não é realizável (autovalor {w.min():.3e})")
        # autovalores negativos pequenos (estrutura quase realizável) são zerados; ver realized_structure_error
        _FACTOR_CACHE[key] = U * np.sqrt(np.clip(w, 0, None))
    return _FACTOR_CACHE[key]


def gaussian_surrogate_levels(V: np.ndarray, n: int, rng: np.random.Generator) -> np.ndarray:
    """Níveis x_n = n − ½ − S_n com S gaussiano de estrutura V (V[k] = Var(S_{n+k} − S_n))."""
    S = _factor(V, n) @ rng.standard_normal(n)
    return np.arange(n) + 0.5 - S


def kc_tau1(levels: np.ndarray, n_blocks: int = 10) -> float:
    """K_c(τ = 1) com o mesmo estimador do C3 (Hann por sub-bloco, sub-blocos disjuntos)."""
    return float(compute_spectral_form_factor(levels, np.array([1.0]), n_blocks=n_blocks)["k_connected"][0])


def predictive_kc_tau1(V_blocks, n_sub: int, n_blocks: int, reps: int, rng: np.random.Generator) -> Dict[str, float]:
    """
    Distribuição preditiva de K_c(1) para um bloco com n_blocks sub-blocos de n_sub níveis, cada sub-bloco com sua
    estrutura V (lista) ou a mesma V para todos. Sub-blocos sorteados de modo independente (aproximação declarada).
    """
    vals = []
    for _ in range(reps):
        parts = []
        for b in range(n_blocks):
            V = V_blocks[b] if isinstance(V_blocks, (list, tuple)) else V_blocks
            parts.append(gaussian_surrogate_levels(V, n_sub, rng) + b * n_sub)
        vals.append(kc_tau1(np.concatenate(parts), n_blocks=n_blocks))
    vals = np.array(vals)
    return {"media": float(vals.mean()), "q025": float(np.quantile(vals, 0.025)), "q975": float(np.quantile(vals, 0.975)),
            "q50": float(np.median(vals)), "reps": reps}


def realized_structure_error(V: np.ndarray, n: int) -> float:
    """Maior |V_realizado(k) − V(k)| do substituto (após zerar autovalores negativos), medido no centro do bloco."""
    F = _factor(V, n)
    C = F @ F.T
    j = n // 4
    ks = np.arange(1, n - j)
    real = C[j, j] + np.diag(C)[j + ks] - 2 * C[j, j + ks]
    return float(np.max(np.abs(real - V[ks])))
