"""
riemann_spectra.statistics
Estatísticas de espaçamentos (Wigner, Poisson, Wasserstein) e função de correlação de pares (Montgomery/GUE).
"""

import math
from typing import Any, Dict, Tuple

import numpy as np
from scipy.special import erf
from scipy.stats import wasserstein_distance


def wigner_gue_pdf(s: np.ndarray | float) -> np.ndarray | float:
    """
    Aproximação de Wigner para o GUE (distribuição de espaçamentos consecutivos):
    P_W(s) = (32 / pi^2) * s^2 * exp(-4 * s^2 / pi).
    Média exata = 1.
    """
    s_arr = np.asarray(s, dtype=np.float64)
    factor = 32.0 / (math.pi**2)
    val = factor * (s_arr**2) * np.exp(-4.0 * (s_arr**2) / math.pi)
    return float(val) if isinstance(s, (int, float)) else val


def wigner_gue_cdf(s: np.ndarray | float) -> np.ndarray | float:
    """
    CDF analítica exata da aproximação de Wigner para GUE:
    CDF_W(s) = erf(2 * s / sqrt(pi)) - (4 * s / pi) * exp(-4 * s^2 / pi).
    """
    s_arr = np.asarray(s, dtype=np.float64)
    term1 = erf(2.0 * s_arr / math.sqrt(math.pi))
    term2 = (4.0 * s_arr / math.pi) * np.exp(-4.0 * (s_arr**2) / math.pi)
    val = term1 - term2
    return float(val) if isinstance(s, (int, float)) else val


def poisson_pdf(s: np.ndarray | float) -> np.ndarray | float:
    """PDF de Poisson para espaçamentos: P(s) = exp(-s)."""
    s_arr = np.asarray(s, dtype=np.float64)
    val = np.exp(-s_arr)
    return float(val) if isinstance(s, (int, float)) else val


def poisson_cdf(s: np.ndarray | float) -> np.ndarray | float:
    """CDF de Poisson para espaçamentos: CDF(s) = 1 - exp(-s)."""
    s_arr = np.asarray(s, dtype=np.float64)
    val = 1.0 - np.exp(-s_arr)
    return float(val) if isinstance(s, (int, float)) else val


def compute_spacing_statistics(
    spacings: np.ndarray,
    s_bins: int = 50,
    s_max: float = 5.0,
) -> Dict[str, Any]:
    """
    Calcula métricas estatísticas dos espaçamentos normalizados s_n:
    - Média, variância, desvio padrão, assimetria (skewness), curtose
    - Distâncias de Wasserstein e Kolmogorov-Smirnov em relação a Wigner-GUE e Poisson
    - Histograma empírico e curvas teóricas
    """
    s = np.asarray(spacings, dtype=np.float64)
    n = len(s)
    if n < 2:
        raise ValueError("São necessários pelo menos 2 espaçamentos para estatísticas.")

    mean_s = float(np.mean(s))
    var_s = float(np.var(s, ddof=1))
    std_s = float(np.std(s, ddof=1))

    # Momentos superiores
    centered = s - mean_s
    skew_s = float(np.mean(centered**3) / (std_s**3)) if std_s > 0 else 0.0
    kurt_s = float(np.mean(centered**4) / (std_s**4) - 3.0) if std_s > 0 else 0.0

    # Histograma
    bin_edges = np.linspace(0.0, s_max, s_bins + 1)
    hist_counts, _ = np.histogram(s, bins=bin_edges)
    bin_widths = np.diff(bin_edges)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    # Normalização em densidade de probabilidade
    hist_density = hist_counts / (n * bin_widths)

    # Teóricos nos centros dos bins
    wigner_vals = wigner_gue_pdf(bin_centers)
    poisson_vals = poisson_pdf(bin_centers)

    # Distâncias empíricas vs teóricas
    # Distância de Kolmogorov-Smirnov contra CDF contínua
    sorted_s = np.sort(s)
    empirical_cdf = np.arange(1, n + 1) / n

    ks_wigner = float(np.max(np.abs(empirical_cdf - wigner_gue_cdf(sorted_s))))
    ks_poisson = float(np.max(np.abs(empirical_cdf - poisson_cdf(sorted_s))))

    # Wasserstein-1 (via integração de CDFs em grade fina)
    eval_grid = np.linspace(0.0, s_max, 1000)
    emp_on_grid = np.searchsorted(sorted_s, eval_grid, side="right") / n
    w1_wigner = float(np.trapezoid(np.abs(emp_on_grid - wigner_gue_cdf(eval_grid)), eval_grid))
    w1_poisson = float(np.trapezoid(np.abs(emp_on_grid - poisson_cdf(eval_grid)), eval_grid))

    # Teoria GUE Wigner: variância teórica = 3*pi/8 - 1 ≈ 0.178087
    wigner_var_theor = 3.0 * math.pi / 8.0 - 1.0

    return {
        "n_spacings": n,
        "mean": mean_s,
        "variance": var_s,
        "std": std_s,
        "skewness": skew_s,
        "kurtosis": kurt_s,
        "wigner_theoretical_variance": wigner_var_theor,
        "poisson_theoretical_variance": 1.0,
        "ks_distance_wigner": ks_wigner,
        "ks_distance_poisson": ks_poisson,
        "wasserstein_distance_wigner": w1_wigner,
        "wasserstein_distance_poisson": w1_poisson,
        "relative_preference_gue": bool(w1_wigner < w1_poisson and ks_wigner < ks_poisson),
        "bins": {
            "edges": bin_edges.tolist(),
            "centers": bin_centers.tolist(),
            "density": hist_density.tolist(),
            "wigner": wigner_vals.tolist(),
            "poisson": poisson_vals.tolist(),
        }
    }


def montgomery_gue_r2(s: np.ndarray | float) -> np.ndarray | float:
    """
    Função teórica de correlação de pares do GUE / Conjectura de Montgomery:
    R_2(s) = 1 - (sin(pi * s) / (pi * s))^2.
    Para s -> 0, R_2(0) = 0 (repulsão quadrática perfeita).
    Para s -> inf, R_2(s) -> 1.
    """
    s_arr = np.asarray(s, dtype=np.float64)
    # Evitar divisão por zero usando sinc normalizado: sinc(u) = sin(pi*u)/(pi*u) no numpy
    sinc_val = np.sinc(s_arr)  # numpy sinc é sin(pi*x)/(pi*x)
    val = 1.0 - sinc_val**2
    return float(val) if isinstance(s, (int, float)) else val


def montgomery_bin_average(edges: np.ndarray, points_per_bin: int = 64) -> np.ndarray:
    """Média de 1 - sinc^2 dentro de cada bin (Gauss-Legendre), em vez do valor no centro."""
    xg, wg = np.polynomial.legendre.leggauss(points_per_bin)
    lo, hi = edges[:-1], edges[1:]
    half = 0.5 * (hi - lo)
    mid = 0.5 * (hi + lo)
    nodes = mid[:, None] + half[:, None] * xg[None, :]
    return 0.5 * np.sum(wg[None, :] * montgomery_gue_r2(nodes), axis=1)


def pair_separation_histogram(levels: np.ndarray, edges: np.ndarray) -> np.ndarray:
    """
    Contagem de pares não ordenados i<j com 0 < x_j - x_i <= edges[-1], por offset k = j - i
    vetorizado (sem matriz N x N). Para cada k, as diferenças x[k:] - x[:-k] são calculadas e
    o laço termina quando todas excedem s_max.
    """
    x = np.sort(np.asarray(levels, dtype=np.float64))
    s_max = float(edges[-1])
    counts = np.zeros(len(edges) - 1, dtype=np.int64)
    k = 1
    while k < len(x):
        d = x[k:] - x[:-k]
        if np.min(d) > s_max:
            break
        counts += np.histogram(d[d <= s_max], bins=edges)[0]
        k += 1
    return counts


def compute_pair_correlation(
    unfolded_levels: np.ndarray,
    s_max: float = 5.0,
    n_bins: int = 50,
) -> Dict[str, Any]:
    """
    R_2(s) para separações positivas 0 < s <= s_max, pares não ordenados, diagonal excluída.
    Normalização de contagem fixa: para n pontos em janela de comprimento L,
        E[# pares no bin] = n (n - 1) / L^2 * int_bin (L - s) R_2(s) ds,
    que dá R_2 = 1 exatamente para n pontos uniformes independentes. A referência GUE é
    a média de 1 - (sin pi s / pi s)^2 em cada bin.
    """
    x = np.sort(np.asarray(unfolded_levels, dtype=np.float64))
    n = len(x)
    if n < 2:
        raise ValueError("São necessários pelo menos 2 níveis para correlação de pares.")
    L = float(x[-1] - x[0])
    if L <= s_max:
        raise ValueError(f"Comprimento da sequência ({L:.2f}) deve ser maior que s_max ({s_max}).")

    edges = np.linspace(0.0, s_max, n_bins + 1)
    counts = pair_separation_histogram(x, edges)
    lo, hi = edges[:-1], edges[1:]
    exposure = L * (hi - lo) - 0.5 * (hi**2 - lo**2)  # int_bin (L - s) ds
    r2_emp = counts * L**2 / (n * (n - 1) * exposure)
    centers = 0.5 * (lo + hi)
    r2_gue = montgomery_bin_average(edges)
    res = r2_emp - r2_gue
    return {
        "n_levels": n,
        "window_length_L": L,
        "mean_density": (n - 1) / L,
        "s_max": s_max,
        "n_bins": n_bins,
        "normalization": "contagem fixa: n(n-1)/L^2 * int (L - s) ds",
        "mse_gue": float(np.mean(res**2)),
        "mse_poisson": float(np.mean((r2_emp - 1.0) ** 2)),
        "relative_preference_gue": bool(np.mean(res**2) < np.mean((r2_emp - 1.0) ** 2)),
        "bins": {
            "edges": edges.tolist(),
            "centers": centers.tolist(),
            "counts": counts.tolist(),
            "r2_empirical": r2_emp.tolist(),
            "r2_gue": r2_gue.tolist(),
            "r2_poisson": np.ones_like(centers).tolist(),
            "residuals_gue": res.tolist(),
        },
    }
