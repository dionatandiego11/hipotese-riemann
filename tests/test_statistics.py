"""
Testes das funções estatísticas: Wigner, Poisson, correlação de pares e SFF.
"""

import math
import numpy as np
import pytest

from riemann_spectra.controls import generate_gue_tridiagonal, generate_poisson_spectrum
from riemann_spectra.statistics import (
    compute_pair_correlation,
    compute_spacing_statistics,
    montgomery_gue_r2,
    poisson_cdf,
    wigner_gue_cdf,
    wigner_gue_pdf,
)


def test_wigner_cdf_analytical_matches_numerical_integral():
    """Verifica se a fórmula analítica de wigner_gue_cdf bate com a integral de wigner_gue_pdf."""
    s_points = np.linspace(0.1, 3.0, 30)
    for s_val in s_points:
        grid = np.linspace(0.0, s_val, 1000)
        pdf_vals = wigner_gue_pdf(grid)
        num_int = np.trapezoid(pdf_vals, grid)
        analyt_val = wigner_gue_cdf(s_val)
        assert abs(num_int - analyt_val) < 1e-4


def test_montgomery_r2_limits():
    """Testa limites assintóticos da fórmula de Montgomery."""
    assert math.isclose(montgomery_gue_r2(0.0), 0.0, abs_tol=1e-8)
    assert abs(montgomery_gue_r2(10.0) - 1.0) < 0.01


def test_pair_correlation_algorithm_gue_vs_poisson():
    """Testa se o algoritmo de dois ponteiros de R_2(s) distingue claramente GUE de Poisson."""
    rng = np.random.default_rng(2026)
    # GUE
    gue_unfolded, _ = generate_gue_tridiagonal(1500, bulk_fraction=0.6, rng=rng)
    r2_gue = compute_pair_correlation(gue_unfolded, s_max=3.0, n_bins=30)
    assert r2_gue["relative_preference_gue"] is True

    # Poisson
    poi_unfolded = generate_poisson_spectrum(1500, rng=rng)
    r2_poi = compute_pair_correlation(poi_unfolded, s_max=3.0, n_bins=30)
    # Para Poisson, r2_empirical ~ 1.0, então mse_poisson deve ser menor que mse_gue
    assert r2_poi["mse_poisson"] < r2_poi["mse_gue"]


def test_pair_correlation_fixed_count_poisson_is_flat():
    rng = np.random.default_rng(4)
    vals = []
    for _ in range(20):
        lv = generate_poisson_spectrum(3000, length=2999.0, rng=rng)
        vals.append(compute_pair_correlation(lv, s_max=5.0, n_bins=10)["bins"]["r2_empirical"])
    assert abs(np.mean(vals) - 1.0) < 0.01


def test_form_factor_poisson_plateau_and_gue_ramp():
    from riemann_spectra.controls import generate_gue_central_levels
    from riemann_spectra.form_factor import compute_spectral_form_factor
    rng = np.random.default_rng(8)
    tau = np.concatenate([np.linspace(0.1, 0.3, 40), np.linspace(1.3, 1.7, 40)])
    kp, kg = [], []
    for _ in range(10):
        kp.append(compute_spectral_form_factor(generate_poisson_spectrum(4000, length=3999.0, rng=rng), tau, n_blocks=4)["k_connected"])
        y, _ = generate_gue_central_levels(4000, 0.6, rng)
        kg.append(compute_spectral_form_factor(y, tau, n_blocks=4)["k_connected"])
    kp, kg = np.array(kp), np.array(kg)
    assert abs(kp.mean() - 1.0) < 0.05
    ramp = kg[:, :40].mean(axis=0)
    assert abs(ramp.mean() - tau[:40].mean()) < 0.03 and np.corrcoef(ramp, tau[:40])[0, 1] > 0.5
    assert abs(kg[:, 40:].mean() - 1.0) < 0.07
