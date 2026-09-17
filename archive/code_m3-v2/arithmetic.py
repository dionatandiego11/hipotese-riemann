"""
riemann_spectra.arithmetic
Comparação aritmética posterior: potências de primos, matching e medição direcionada.

AVISO METODOLÓGICO:
Este módulo só é chamado DEPOIS de `blind_peaks.csv` ter sido gravado e ter seu hash
registrado. A medição direcionada (ajuste nos períodos r log p conhecidos) NÃO é detecção
cega e é relatada separadamente.

Referência formal (regularizada; não é série convergente na linha crítica):
    d_osc(E) ~ sum_{p, r>=1} c_{p,r} cos(E r log p),   c_{p,r} = -log(p) / (pi p^{r/2}).
"""

import math
from typing import Any, Callable, Dict, List, Tuple

import numpy as np

from riemann_spectra.periods import hann_response


def sieve_primes(max_val: int) -> List[int]:
    """Crivo de Eratóstenes."""
    if max_val < 2:
        return []
    is_prime = bytearray([1]) * (max_val + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(max_val) + 1):
        if is_prime[p]:
            is_prime[p * p::p] = bytearray(len(range(p * p, max_val + 1, p)))
    return [i for i in range(max_val + 1) if is_prime[i]]


def prime_power_catalog(t_min: float, t_max: float) -> List[Dict[str, Any]]:
    """
    Todos os pares (p, r), r >= 1, com r log p em [t_min, t_max], ordenados por período.
    Coeficiente de referência do cosseno: c = -log p / (pi p^{r/2}).
    """
    max_p = int(math.floor(math.exp(t_max))) + 1
    catalog = []
    for p in sieve_primes(max_p):
        lp = math.log(p)
        r = 1
        while r * lp <= t_max:
            T = r * lp
            if T >= t_min:
                catalog.append({
                    "prime": p,
                    "repetition": r,
                    "period_theoretical": T,
                    "coefficient_theoretical": -lp / (math.pi * p ** (r / 2.0)),
                })
            r += 1
    catalog.sort(key=lambda c: c["period_theoretical"])
    for i, c in enumerate(catalog):
        c["catalog_index"] = i
    return catalog


def flag_unresolved(catalog: List[Dict[str, Any]], resolution: float) -> None:
    """Marca linhas teóricas cujo vizinho está a menos de `resolution` (mistura potencial)."""
    T = np.array([c["period_theoretical"] for c in catalog])
    for i, c in enumerate(catalog):
        left = T[i] - T[i - 1] if i > 0 else np.inf
        right = T[i + 1] - T[i] if i < len(T) - 1 else np.inf
        c["nearest_neighbor_separation"] = float(min(left, right))
        c["resolved"] = bool(min(left, right) >= resolution)


def match_one_to_one(
    peak_periods: np.ndarray,
    catalog: List[Dict[str, Any]],
    tolerance: float,
) -> Tuple[Dict[int, int], Dict[str, Any]]:
    """
    Correspondência um a um: pares (pico, linha) com distância <= tolerance, atribuídos
    gulosamente por distância crescente (nenhum pico serve a duas linhas e vice-versa).
    Retorna {catalog_index: peak_index} e resumo.
    """
    peak_periods = np.asarray(peak_periods, dtype=np.float64)
    T = np.array([c["period_theoretical"] for c in catalog])
    pairs = []
    if len(peak_periods) and len(T):
        order = np.argsort(peak_periods)
        sorted_p = peak_periods[order]
        for ci, t in enumerate(T):
            lo = np.searchsorted(sorted_p, t - tolerance, side="left")
            hi = np.searchsorted(sorted_p, t + tolerance, side="right")
            for k in range(lo, hi):
                pairs.append((abs(sorted_p[k] - t), ci, int(order[k])))
    pairs.sort()
    used_c, used_p, assignment = set(), set(), {}
    for _, ci, pi in pairs:
        if ci in used_c or pi in used_p:
            continue
        used_c.add(ci)
        used_p.add(pi)
        assignment[ci] = pi
    summary = {
        "n_catalog": len(catalog),
        "n_peaks": int(len(peak_periods)),
        "n_matched": len(assignment),
        "n_unmatched_peaks": int(len(peak_periods) - len(assignment)),
        "tolerance": tolerance,
    }
    return assignment, summary


def targeted_joint_fit(
    evaluator: Callable[[np.ndarray], np.ndarray],
    catalog: List[Dict[str, Any]],
    L: float,
    E_c: float,
    half_width: float,
    points_per_line: int = 9,
) -> List[Dict[str, Any]]:
    """
    Medição DIRECIONADA (não cega): ajuste linear conjunto por mínimos quadrados
        F(t) ~ sum_k a_k W(t - T_k)
    em pontos t amostrados em |t - T_k| <= half_width, com W a resposta analítica da janela.
    Coeficiente corrigido do cosseno: C_k = 2 a_k e^{-i E_c T_k}, a comparar com c_{p,r} real.
    O sinal de uma linha real c cos(E T) satisfaz C = c (fase 0 se c > 0, pi se c < 0).
    """
    T = np.array([c["period_theoretical"] for c in catalog])
    t_pts = np.unique(np.concatenate([np.linspace(t - half_width, t + half_width, points_per_line) for t in T]))
    F = evaluator(t_pts)
    design = hann_response(t_pts[:, None] - T[None, :], L).astype(np.complex128)
    coef, *_ = np.linalg.lstsq(design, F, rcond=None)
    resid = F - design @ coef
    cond = float(np.linalg.cond(design))
    results = []
    for k, c in enumerate(catalog):
        C = 2.0 * coef[k] * np.exp(-1j * E_c * T[k])
        c_th = c["coefficient_theoretical"]
        results.append({
            "catalog_index": c["catalog_index"],
            "coefficient_real": float(np.real(C)),
            "coefficient_imag": float(np.imag(C)),
            "coefficient_modulus": float(np.abs(C)),
            "coefficient_phase": float(np.angle(C)),
            "ratio_to_theory": float(np.real(C) / c_th),
            "phase_error_rad": float(np.angle(C / c_th)),
        })
    rms_resid = float(np.sqrt(np.mean(np.abs(resid) ** 2)))
    for r in results:
        r["fit_residual_rms"] = rms_resid
        r["design_condition_number"] = cond
    return results


def detection_limit_coefficient(noise_rms: float, threshold_z: float, L: float) -> float:
    """
    Menor |c| detectável com o limiar z: |F(T)| = |c| W(0) / 2 = |c| L / 4 >= z sigma.
    """
    return 4.0 * threshold_z * noise_rms / L
