"""
riemann_spectra.inference
Testes de significância estatística de Monte Carlo contra controles nulos e correção de comparações múltiplas.
"""

from typing import Any, Dict, List, Tuple

import numpy as np


def compute_monte_carlo_p_value(observed_score: float, null_scores: List[float] | np.ndarray) -> float:
    """
    Calcula valor-p exato de Monte Carlo:
    p_MC = (1 + #{S_nulo >= S_obs}) / (B + 1).
    Garante calibração exata e evita p = 0 numérico para B replicações finitas.
    """
    null_arr = np.asarray(null_scores, dtype=np.float64)
    B = len(null_arr)
    if B == 0:
        return 1.0
    count_geq = int(np.sum(null_arr >= observed_score))
    return float((1.0 + count_geq) / (B + 1.0))


def benjamini_hochberg_fdr(p_values: List[float], alpha: float = 0.05) -> Tuple[List[bool], List[float]]:
    """
    Ajuste de taxa de falsas descobertas (False Discovery Rate - Benjamini-Hochberg).
    Retorna máscara booleana de significância e valores-p ajustados (q-values).
    """
    p_arr = np.asarray(p_values, dtype=np.float64)
    m = len(p_arr)
    if m == 0:
        return [], []

    order = np.argsort(p_arr)
    sorted_p = p_arr[order]
    rank = np.arange(1, m + 1)

    # q_i = min_{j >= i} (m * p_j / j)
    q_factors = (m / rank) * sorted_p
    # Monotonicidade reversa
    q_vals = np.minimum.accumulate(q_factors[::-1])[::-1]
    q_vals = np.clip(q_vals, 0.0, 1.0)

    # Desfazer ordenação
    adjusted = np.empty(m, dtype=np.float64)
    adjusted[order] = q_vals

    significant = adjusted <= alpha
    return significant.tolist(), adjusted.tolist()
