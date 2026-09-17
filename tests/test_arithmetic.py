"""Catálogo de potências de primos, matching um a um e ajuste direcionado."""

import math

import numpy as np

from riemann_spectra.arithmetic import match_one_to_one, prime_power_catalog, targeted_joint_fit
from riemann_spectra.periods import hann_response


def test_catalog_contents():
    cat = prime_power_catalog(0.5, 5.0)
    pairs = {(c["prime"], c["repetition"]) for c in cat}
    assert (2, 1) in pairs and (2, 7) in pairs and (2, 8) not in pairs  # 8 log 2 = 5.545
    assert (139, 1) in pairs and (149, 1) not in pairs                  # log 149 = 5.004
    assert all(0.5 <= c["period_theoretical"] <= 5.0 for c in cat)
    assert math.isclose(next(c for c in cat if c["prime"] == 3 and c["repetition"] == 2)["coefficient_theoretical"],
                        -math.log(3) / (math.pi * 3.0))


def test_match_is_one_to_one():
    cat = [{"period_theoretical": 1.0, "catalog_index": 0}, {"period_theoretical": 1.001, "catalog_index": 1}]
    assign, summary = match_one_to_one(np.array([1.0004]), cat, tolerance=0.01)
    assert summary["n_matched"] == 1 and list(assign.values()) == [0]


def test_targeted_fit_separates_overlapping_lines():
    L, Ec = 3000.0, 5000.0
    cat = [
        {"period_theoretical": 2.0, "coefficient_theoretical": -0.2, "catalog_index": 0},
        {"period_theoretical": 2.0 + 1.5 * 2 * math.pi / L, "coefficient_theoretical": -0.1, "catalog_index": 1},
    ]
    true_C = np.array([-0.2, 0.08 + 0.05j])

    def evaluator(t):
        return sum(0.5 * true_C[k] * np.exp(1j * Ec * c["period_theoretical"]) * hann_response(t - c["period_theoretical"], L)
                   for k, c in enumerate(cat))

    fit = targeted_joint_fit(evaluator, cat, L, Ec, half_width=2 * math.pi / L)
    got = np.array([f["coefficient_real"] + 1j * f["coefficient_imag"] for f in fit])
    assert np.max(np.abs(got - true_C)) < 1e-10
