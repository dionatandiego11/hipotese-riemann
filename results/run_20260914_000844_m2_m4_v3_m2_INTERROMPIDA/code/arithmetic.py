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

from riemann_spectra.periods import window_response


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
    window: str = "hann",
    sampling: str = "band",
    include_conjugate: bool = False,
) -> List[Dict[str, Any]]:
    """
    Medição DIRECIONADA (não cega) dos coeficientes complexos C_k de linhas de densidade
    Re[C_k e^{i E T_k}] nos períodos conhecidos T_k. O coeficiente teórico NÃO entra no ajuste.

    Modelo sem conjugado (linear complexo):
        F(t) ~ sum_k (C_k / 2) e^{i E_c T_k} W(t - T_k)
    Modelo com conjugado (linear real em Re C_k, Im C_k):
        F(t) ~ sum_k [ (C_k / 2) e^{i E_c T_k} W(t - T_k) + (conj C_k / 2) e^{-i E_c T_k} W(t + T_k) ]
    Amostragem: "band" = `points_per_line` pontos em |t - T_k| <= half_width; "centers" = só t = T_k.
    Para uma linha real c cos(E T), C = c.
    """
    T = np.array([c["period_theoretical"] for c in catalog])
    if sampling == "band":
        t_pts = np.unique(np.concatenate([np.linspace(t - half_width, t + half_width, points_per_line) for t in T]))
    elif sampling == "centers":
        t_pts = T.copy()
    else:
        raise ValueError(f"Amostragem desconhecida: {sampling!r}")
    F = evaluator(t_pts)
    ph = np.exp(1j * E_c * T)
    G = 0.5 * window_response(t_pts[:, None] - T[None, :], L, window) * ph[None, :]
    if not include_conjugate:
        coef, *_ = np.linalg.lstsq(G.astype(np.complex128), F, rcond=None)
        C = coef
        model = G @ C
        cond = float(np.linalg.cond(G))
    else:
        H = 0.5 * window_response(t_pts[:, None] + T[None, :], L, window) * np.conj(ph)[None, :]
        # F = (G + H) Re C + i (G - H) Im C  -> sistema real empilhando partes real e imaginária
        Mc = np.hstack([G + H, 1j * (G - H)])
        Mr = np.vstack([Mc.real, Mc.imag])
        rhs = np.concatenate([F.real, F.imag])
        sol, *_ = np.linalg.lstsq(Mr, rhs, rcond=None)
        K = len(T)
        C = sol[:K] + 1j * sol[K:]
        model = Mc @ sol
        cond = float(np.linalg.cond(Mr))
    resid = F - model
    rms_resid = float(np.sqrt(np.mean(np.abs(resid) ** 2)))
    results = []
    for k, c in enumerate(catalog):
        c_th = c["coefficient_theoretical"]
        results.append({
            "catalog_index": c["catalog_index"],
            "coefficient_real": float(np.real(C[k])),
            "coefficient_imag": float(np.imag(C[k])),
            "coefficient_modulus": float(np.abs(C[k])),
            "coefficient_phase": float(np.angle(C[k])),
            "ratio_to_theory": float(np.real(C[k]) / c_th),
            "phase_error_rad": float(np.angle(C[k] / c_th)),
            "fit_residual_rms": rms_resid,
            "design_condition_number": cond,
        })
    return results


def detection_limit_coefficient(noise_rms: float, threshold_z: float, gain_W0: float) -> float:
    """Menor |c| detectável com o limiar z: |F(T)| = |c| W(0) / 2 >= z sigma."""
    return 2.0 * threshold_z * noise_rms / gain_W0
