"""Validação da implementação independente com casos conhecidos (sem ler resultados de referência)."""
import ast
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import pytest

from riemann_indep import core, spectral, stats

PKG = Path(__file__).resolve().parents[1] / "riemann_indep"


def test_no_dependency_on_reference_package():
    for f in PKG.glob("*.py"):
        tree = ast.parse(f.read_text())
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                names = [a.name for a in node.names] + ([node.module] if isinstance(node, ast.ImportFrom) and node.module else [])
                assert not any("riemann_spectra" in (n or "") for n in names), f
        assert "src/riemann_spectra" not in f.read_text()


def test_smooth_term_matches_mpmath_quadrature():
    A, B = 4000.0, 6700.0
    L, Ec = B - A, 0.5 * (A + B)
    mp.mp.dps = 25
    for t in (0.55, 1.7, 4.2):
        f = lambda E: (0.5 - 0.5 * mp.cos(2 * mp.pi * (E - A) / L)) * mp.log(E / (2 * mp.pi)) * mp.exp(-1j * (E - Ec) * t) / (2 * mp.pi)
        ref = complex(mp.quad(f, mp.linspace(A, B, int(L * t / (2 * math.pi)) + 2)))
        assert abs(core.smooth_term(np.array([t]), A, B)[0] - ref) < 1e-11


def test_hann_response_integral_and_fwhm():
    L = 777.0
    u = np.linspace(-L / 2, L / 2, 400001)
    w = 0.5 + 0.5 * np.cos(2 * math.pi * u / L)
    for om in (0.0, 0.004, 0.02):
        assert abs(np.trapezoid(w * np.exp(-1j * u * om), u) - core.hann_response(om, L)) < 1e-6 * L
    assert core.fwhm_hann(L) == pytest.approx(2 * 2 * math.pi / L, rel=1e-12)


def test_recurrence_equals_direct_sum():
    rng = np.random.default_rng(0)
    g = np.sort(rng.uniform(1000, 3000, 2500))
    ins = core.Instrument(g)
    assert np.max(np.abs(ins.F(g) - core.instrument_F_fast(ins, g))) < 1e-9


def test_nbar_inverse_lambert():
    x = np.array([5.0, 123.4, 1e4, 7e4])
    assert np.max(np.abs(core.nbar(core.nbar_inverse(x)) - x)) < 1e-9


def test_line_injection_amplitude_and_phase():
    x = core.nbar(2000.0) + np.arange(3000) + 0.5
    T = np.array([1.3, 2.9])
    Cc = np.array([-0.04, 0.03 * np.exp(0.7j)])
    E = stats.inject_lines(x, T, Cc)
    ins = core.Instrument(E)
    got = stats.fit_band_conjugate(lambda tt: ins.F_at(E, tt), T, ins.L, ins.Ec, 0.5 * ins.fwhm)
    assert np.max(np.abs(got - Cc)) < 2e-3


def test_conjugate_fit_exact_on_model():
    L, Ec = 300.0, 500.0
    T = np.array([0.03, 0.08])
    Cc = np.array([-0.2 + 0.05j, 0.1 - 0.02j])
    ev = lambda t: (0.5 * Cc * np.exp(1j * Ec * T) * core.hann_response(np.subtract.outer(t, T), L)
                    + 0.5 * np.conj(Cc) * np.exp(-1j * Ec * T) * core.hann_response(np.add.outer(t, T), L)).sum(1)  # noqa: E731
    got = stats.fit_band_conjugate(ev, T, L, Ec, 2 * math.pi / L)
    assert np.max(np.abs(got - Cc)) < 1e-10


def test_gue_tridiagonal_matches_dense():
    from scipy.stats import ks_2samp
    rng = np.random.default_rng(2)
    sd = np.concatenate([np.diff(stats.gue_dense_eigs(200, rng)[70:130]) for _ in range(150)])
    st = np.concatenate([np.diff(stats.gue_tridiagonal_eigs(200, rng)[70:130]) for _ in range(150)])
    assert ks_2samp(sd, st).pvalue > 0.001


def test_order_statistic_interval_coverage():
    rng = np.random.default_rng(5)
    from scipy.stats import gumbel_r
    q = gumbel_r.ppf(0.95)
    cov = np.mean([(lambda iv: iv["z_low"] <= q <= iv["z_high"])(stats.order_stat_interval(rng.gumbel(size=999))) for _ in range(1000)])
    assert cov >= 0.94


def test_m2_estimators_on_poisson():
    rng = np.random.default_rng(6)
    tau = np.linspace(0.1, 1.9, 40)
    assert abs(np.mean([spectral.pair_correlation(stats.poisson_fixed(3000, rng)) for _ in range(10)]) - 1) < 0.02
    assert abs(np.mean([spectral.form_factor_connected(stats.poisson_fixed(3000, rng), tau) for _ in range(10)]) - 1) < 0.05


def test_cue_exact_N2_and_limit_variance():
    s = np.linspace(0, 2, 41)
    E2 = spectral.cheb_model(lambda v: spectral.gap_cue_toeplitz(v, 2), 0, 2)
    assert np.max(np.abs(1 + E2(s, 1) - (s / 2 - np.sin(np.pi * s) / (2 * np.pi)))) < 1e-9
    corr = spectral.CUECorrection()
    g = np.linspace(0, 4, 401)
    assert abs(np.trapezoid(g * g * corr.p0(g), g) - 1 - 0.18) < 1e-3


def test_reserved_range_refused(tmp_path):
    from riemann_indep.pipeline import run_block
    with pytest.raises(PermissionError):
        run_block("x", 70001, 73000, 1, tmp_path)


def test_access_limit_is_explicit(tmp_path):
    from riemann_indep.pipeline import run_block
    with pytest.raises(PermissionError):
        run_block("x", 99001, 100001, 1, tmp_path, max_allowed_index=100000)
