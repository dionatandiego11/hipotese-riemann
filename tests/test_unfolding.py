"""
Testes de unfolding, inversão numérica e fase de Riemann-Siegel.
"""

import math
import numpy as np
import pytest

from riemann_spectra.unfolding import (
    d_bar_rvm,
    fold_spectrum,
    inverse_n_bar,
    n_bar_rvm,
    n_bar_theta,
    riemann_siegel_theta,
    unfold_spectrum,
)


def test_rvm_smooth_density_derivative():
    """Verifica se d_bar_rvm é a derivada analítica exata de n_bar_rvm."""
    E_vals = np.array([20.0, 50.0, 100.0, 500.0, 1000.0])
    h = 1e-5
    num_deriv = (n_bar_rvm(E_vals + h) - n_bar_rvm(E_vals - h)) / (2.0 * h)
    analyt_deriv = d_bar_rvm(E_vals)
    np.testing.assert_allclose(analyt_deriv, num_deriv, rtol=1e-6)


def test_inverse_n_bar_precision():
    """Verifica se inverse_n_bar(n_bar_rvm(E)) recupera E com altíssima precisão (< 1e-10)."""
    E_test = np.array([14.134725, 21.022040, 50.0, 100.0, 1000.0, 10000.0])
    x_test = n_bar_rvm(E_test)
    E_rec = inverse_n_bar(x_test)
    np.testing.assert_allclose(E_rec, E_test, atol=1e-10, rtol=1e-10)


def test_theta_rvm_asymptotic_agreement():
    """Verifica se N_theta(E) concorda assintoticamente com N_rvm(E) para E grande."""
    E_large = np.array([100.0, 500.0, 1000.0, 5000.0])
    rvm = n_bar_rvm(E_large)
    theta_n = n_bar_theta(E_large)
    # A diferença deve decair como O(1/E)
    diff = np.abs(rvm - theta_n)
    assert np.all(diff < 0.05)
    assert diff[-1] < diff[0]  # Decaimento assintótico


def test_unfold_and_fold_spectrum_roundtrip():
    """Verifica ciclo completo unfold -> fold."""
    gammas = np.array([14.1347, 21.0220, 25.0108, 30.4248, 32.9350])
    x, s = unfold_spectrum(gammas)
    assert np.all(s > 0)
    recovered = fold_spectrum(x)
    np.testing.assert_allclose(recovered, gammas, atol=1e-10)
