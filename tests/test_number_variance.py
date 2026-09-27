import math

import numpy as np
from scipy.special import sici

from riemann_spectra.controls import generate_gue_central_levels
from riemann_spectra.number_variance import (EULER_GAMMA, number_variance, prime_powers, sigma2_berry,
                                             sigma2_gue)


def test_gue_formula_limits():
    # L → 0: Σ²(L) ≈ L (um nível ou nenhum); L grande: (log 2πL + γ + 1)/π² a menos de O(1/L)
    assert abs(sigma2_gue(1e-3) - 1e-3) < 1e-5
    big = 200.0
    assert abs(sigma2_gue(big) - (math.log(2 * math.pi * big) + EULER_GAMMA + 1) / math.pi**2) < 2e-3


def test_prime_powers():
    pp = prime_powers(30)
    assert [x[2] for x in pp if x[0] == 2] == [2, 4, 8, 16]
    assert (29, 1, 29) in pp and all(x[2] < 30 for x in pp)


def test_berry_reduces_to_gue_for_small_L():
    for E in (1e3, 1e5):
        assert abs(sigma2_berry(0.02, E) - sigma2_gue(0.02)) < 1e-3


def test_berry_without_primes_removes_short_tau_part():
    L = np.array([1.0, 5.0, 20.0])
    tau = 0.5
    y = 2 * math.pi * L * tau
    expected = sigma2_gue(L) + (sici(y)[1] - np.log(y) - EULER_GAMMA) / math.pi**2
    got = sigma2_berry(L, 1e4, tau_star=tau, weight=lambda p: 0)
    assert np.allclose(got, expected, atol=1e-12)


def test_character_weight_removes_exactly_the_excluded_prime():
    # χ₋₄: χ(2) = 0. Com q igual, a diferença para "todos os primos" é exatamente a soma das potências de 2.
    L = np.array([2.0, 6.0, 12.0])
    E, q, tau = 5000.0, 4, 0.5
    lam = math.log(q * E / (2 * math.pi))
    X = math.exp(tau * lam)
    all_p = sigma2_berry(L, E, tau_star=tau, q=q, weight=lambda p: 1)
    no2 = sigma2_berry(L, E, tau_star=tau, q=q, weight=lambda p: 0 if p == 2 else 1)
    two = sum(np.sin(math.pi * L * r * math.log(2) / lam) ** 2 / (r * r * 2**r)
              for r in range(1, 60) if 2**r < X)
    assert np.allclose(all_p - no2, 2 * two / math.pi**2, atol=1e-14)


def test_estimator_poisson_gives_L():
    rng = np.random.default_rng(1)
    x = np.sort(rng.uniform(0, 20000, 20000))
    r = number_variance(x, [0.5, 2.0, 8.0])
    assert np.all(np.abs(r["V"] - r["L"]) < 5 * r["sigma"] + 0.02 * r["L"])


def test_estimator_lattice_integer_L_is_rigid():
    x = np.arange(5000) + 0.123
    r = number_variance(x, [1.0, 3.0, 10.0], step=0.037)
    assert np.all(r["V"] < 1e-2)


def test_estimator_recovers_gue_on_gue_levels():
    rng = np.random.default_rng(20260926)
    L = [0.5, 1.0, 2.0, 4.0]
    Vs = [number_variance(generate_gue_central_levels(3000, rng=rng)[0], L)["V"] for _ in range(20)]
    m = np.mean(Vs, axis=0)
    se = np.std(Vs, axis=0, ddof=1) / math.sqrt(len(Vs))
    assert np.all(np.abs(m - sigma2_gue(np.array(L))) < 4 * se + 0.01)
