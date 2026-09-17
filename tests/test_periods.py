"""
Instrumento F_w, NUFFT, resposta da janela, injeção de linhas e detector sem catálogo.
"""

import inspect
import math

import numpy as np

from riemann_spectra import periods
from riemann_spectra.controls import inject_density_lines
from riemann_spectra.periods import (
    OscillatoryTransform,
    adjusted_p_values,
    calibrate_threshold,
    detect_blind_peaks,
    direct_exponential_sum,
    hann_response,
    measure_hann_response,
    nufft_uniform_t,
)
from riemann_spectra.unfolding import n_bar_rvm


def test_periods_module_has_no_arithmetic_dependency():
    import re

    src = inspect.getsource(periods).lower()
    for pattern in [r"\bprimes?\b", r"\bprimos?\b", r"sieve", r"crivo", r"arithmetic", r"log\((2|3|5|7)\)", r"sympy", r"isprime"]:
        assert re.search(pattern, src) is None, f"padrão proibido em periods.py: {pattern}"


def test_nufft_matches_direct_sum():
    rng = np.random.default_rng(1)
    u = rng.uniform(-2000, 2000, size=3000)
    c = rng.normal(size=3000) + 1j * rng.normal(size=3000)
    t0, dt, n = 0.5, 2 * math.pi / 4000 / 8, 5001
    fast = nufft_uniform_t(u, c, t0, dt, n)
    idx = rng.choice(n, 50, replace=False)
    ref = direct_exponential_sum(u, c, t0 + dt * idx)
    assert np.max(np.abs(fast[idx] - ref)) < 1e-9 * np.max(np.abs(ref))


def test_hann_response_normalization_and_width():
    L = 1234.5
    om = np.linspace(-0.05, 0.05, 20001)
    # comparação com a integral numérica da janela centrada
    u = np.linspace(-L / 2, L / 2, 200001)
    w = 0.5 * (1 + np.cos(2 * math.pi * u / L))
    for o in (0.0, 0.003, 0.011):
        num = np.trapezoid(w * np.exp(-1j * u * o), u)
        assert abs(num - hann_response(o, L)) < 1e-6 * L
    resp = measure_hann_response(L)
    assert math.isclose(resp["gain_W0"], L / 2)
    assert math.isclose(resp["fwhm_in_units_2pi_over_L"], 2.0, rel_tol=1e-6)
    assert -32.0 < resp["sidelobe_level_db"] < -31.0


def test_level_injection_recovers_amplitude_and_phase():
    """Picket fence (sem flutuações em t<5) + linhas conhecidas: C recuperado após toda a cadeia."""
    x0 = float(n_bar_rvm(1500.0))
    x = x0 + np.arange(3000) + 0.5
    T = np.array([1.3, 2.7, 4.1])
    C = np.array([-0.05, 0.03 * np.exp(1j * 1.0), 0.02 * np.exp(-2j)])
    E = inject_density_lines(x, T, C)
    tr = OscillatoryTransform(E[0], E[-1], 0.5, 5.0)
    F = tr.evaluate(E, T)
    C_hat = 2 * F * np.exp(-1j * tr.E_c * T) / tr.response["gain_W0"]
    assert np.max(np.abs(C_hat - C)) < 2e-3


def test_permuting_levels_leaves_transform_invariant():
    rng = np.random.default_rng(5)
    E = np.sort(rng.uniform(100, 900, 800))
    tr = OscillatoryTransform(E[0], E[-1], 0.5, 3.0)
    assert np.max(np.abs(tr.transform(E) - tr.transform(rng.permutation(E)))) < 1e-10


def test_detector_recovers_lines_with_null_noise_profile():
    rng = np.random.default_rng(11)
    t = np.linspace(0.5, 5.0, 20001)
    fwhm = 0.004
    sigma = np.full_like(t, 10.0)
    L = 4 * math.pi / fwhm
    # ruído com a mesma correlação que a janela impõe (convolução com a resposta de Hann)
    white = rng.normal(size=t.size) + 1j * rng.normal(size=t.size)
    dt = t[1] - t[0]
    kern = hann_response(np.arange(-400, 401) * dt, L)
    F = np.convolve(white, kern, mode="same")
    F *= 10.0 / np.sqrt(np.mean(np.abs(F) ** 2))
    true_T = [1.1, 2.3, 3.9]
    for T0, amp in zip(true_T, [120.0, 90.0, 70.0]):
        F += amp * np.exp(1j * 0.7) * hann_response(t - T0, L) / (L / 2)
    peaks = detect_blind_peaks(t, F, fwhm, sigma, candidate_z=5.0)
    found = np.array([p["period"] for p in peaks])
    for T0 in true_T:
        assert np.min(np.abs(found - T0)) < 0.15 * fwhm


def test_threshold_and_adjusted_p_are_consistent():
    rng = np.random.default_rng(3)
    null_max = rng.gumbel(3.0, 0.3, size=999)
    thr = calibrate_threshold(null_max, 0.05)
    assert adjusted_p_values([thr], null_max)[0] <= 0.05
    assert adjusted_p_values([np.nextafter(thr, 0) - 1e-9], null_max)[0] > 0.05 or thr == np.min(null_max)
    assert adjusted_p_values([1e9], null_max)[0] == 1 / 1000
