import math

import numpy as np

from riemann_spectra.discrete_moments import (A_q, arithmetic_factor, block_bootstrap_ratio, matched_expectation,
                                              normalized_reciprocal)


def test_arithmetic_factor_and_constants():
    assert arithmetic_factor(1) == 1.0
    assert math.isclose(arithmetic_factor(4), 2 / 3)
    assert math.isclose(arithmetic_factor(5), 5 / 6)
    assert math.isclose(arithmetic_factor(12), (2 / 3) * (3 / 4))
    # Gonek: A_1/2π = 3/π³; χ₋₄: 2/π³
    assert math.isclose(A_q(1) / (2 * math.pi), 3 / math.pi**3)
    assert math.isclose(A_q(4) / (2 * math.pi), 2 / math.pi**3)


def test_normalized_reciprocal():
    g = np.array([100.0, 1000.0])
    v = normalized_reciprocal(g, np.array([2.0, 0.5]), 4)
    assert np.allclose(v, [math.log(400 / (2 * math.pi)) / 4, math.log(4000 / (2 * math.pi)) / 0.25])


def test_matched_expectation_reweights_by_density():
    # referência com v dependente da densidade; o teste concentra-se na densidade alta
    dens_ref = np.repeat([1.0, 2.0], 500)
    v_ref = np.repeat([10.0, 20.0], 500)
    dens_test = np.array([2.0] * 90 + [1.0] * 10)
    edges = np.array([0.5, 1.5, 2.5])
    assert math.isclose(matched_expectation(dens_test, dens_ref, v_ref, edges), 0.9 * 20 + 0.1 * 10)


def test_bootstrap_recovers_known_ratio_with_heavy_tail():
    rng = np.random.default_rng(7)
    n = 20000
    dens = np.sort(rng.uniform(3, 8, n))
    base = rng.pareto(2.5, n) + 1.0            # cauda pesada, média finita
    v_ref = base * dens / 5
    v_test = (2 / 3) * (rng.pareto(2.5, 6000) + 1.0) * np.sort(rng.uniform(3, 8, 6000)) / 5
    r = block_bootstrap_ratio(v_test, np.sort(rng.uniform(3, 8, 6000)), v_ref, dens,
                              np.linspace(3, 8, 6), block=100, reps=300, rng=rng)
    assert r["q025"] < 2 / 3 < r["q975"] and r["q975"] < 1.0
