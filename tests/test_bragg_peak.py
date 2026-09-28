import math

import numpy as np

from riemann_spectra.bragg_peak import (gaussian_surrogate_levels, kc_tau1, structure_from_sigma2)
from riemann_spectra.form_factor import compute_spectral_form_factor
from riemann_spectra.number_variance import sigma2_gue


def test_structure_endpoint_correction():
    s2 = np.array([0.5, 0.6, 0.7])
    assert np.allclose(structure_from_sigma2(s2, True), [0, 0.5 - 1 / 6, 0.6 - 1 / 6, 0.7 - 1 / 6])
    assert np.allclose(structure_from_sigma2(s2, False), [0, 0.5, 0.6, 0.7])


def test_surrogate_reproduces_structure():
    rng = np.random.default_rng(3)
    k = np.arange(1, 200)
    V = structure_from_sigma2(sigma2_gue(k.astype(float)))
    d = np.array([[x[j + kk] - x[j] - kk for kk in (1, 5, 50)]
                  for x in (gaussian_surrogate_levels(V, 200, rng) for _ in range(20000)) for j in (60,)])
    assert np.allclose(d.var(axis=0), V[[1, 5, 50]], rtol=0.04)


def test_kc_tau1_matches_form_factor():
    x = np.cumsum(np.random.default_rng(1).exponential(1.0, 3000))
    ref = compute_spectral_form_factor(x, np.array([1.0]), n_blocks=10)["k_connected"][0]
    assert kc_tau1(x) == ref


def test_rigid_limit_gives_coherent_peak():
    # V ≡ ε (quase rede): E|Z|² ≈ e^{-2π²ε}(Σw)² ; com Hann e 300 níveis, (Σw)²/Q ≈ 2·300/3
    eps = 0.01
    V = np.concatenate([[0.0], np.full(299, eps)])
    rng = np.random.default_rng(5)
    vals = [kc_tau1(np.concatenate([gaussian_surrogate_levels(V, 300, rng) + 300 * b for b in range(10)]))
            for _ in range(50)]
    expected = math.exp(-2 * math.pi**2 * eps) * 2 * 300 / 3
    assert abs(np.mean(vals) / expected - 1) < 0.1
