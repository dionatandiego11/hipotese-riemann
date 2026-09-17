"""
Testes dos modelos de controle: Poisson, GUE (denso e Dumitriu-Edelman), shuffle e fases.
"""

import math
import numpy as np
import pytest

from riemann_spectra.controls import (
    generate_gue_dense,
    generate_gue_tridiagonal,
    generate_poisson_spectrum,
    randomize_fourier_phases,
    semicircle_cdf,
    shuffle_spacings,
)


def test_semicircle_cdf_properties():
    """Testa valores limite e monotonicidade da CDF do semicírculo."""
    y = np.linspace(-1.0, 1.0, 100)
    cdf = semicircle_cdf(y)
    assert math.isclose(cdf[0], 0.0, abs_tol=1e-6)
    assert math.isclose(cdf[-1], 1.0, abs_tol=1e-6)
    assert math.isclose(cdf[len(y) // 2], 0.5, abs_tol=1e-2)
    assert np.all(np.diff(cdf) >= 0.0)


def test_poisson_spectrum_statistics():
    """Testa média e variância do processo Poisson."""
    rng = np.random.default_rng(42)
    levels = generate_poisson_spectrum(2000, rng=rng)
    spacings = np.diff(levels)
    # Média deve ser próxima de 1.0
    assert abs(np.mean(spacings) - 1.0) < 0.05
    # Variância deve ser próxima de 1.0 (propriedade exponencial)
    assert abs(np.var(spacings) - 1.0) < 0.15


def test_gue_dense_and_tridiagonal_agree():
    """Mesma normalização (raio 1) e mesma estatística local de espaçamentos (beta = 2)."""
    rng = np.random.default_rng(123)
    n, reps = 300, 40
    sd, st, rd, rt = [], [], [], []
    for _ in range(reps):
        b, ev = generate_gue_dense(n, bulk_fraction=1.0, rng=rng)
        sd.append(np.diff(b)); rd.append(np.max(np.abs(ev)))
        b, ev = generate_gue_tridiagonal(n, bulk_fraction=1.0, rng=rng)
        st.append(np.diff(b)); rt.append(np.max(np.abs(ev)))
    sd, st = np.concatenate(sd), np.concatenate(st)
    assert abs(np.mean(rd) - 1.0) < 0.03 and abs(np.mean(rt) - 1.0) < 0.03
    assert abs(np.mean(sd) - 1.0) < 0.03 and abs(np.mean(st) - 1.0) < 0.03
    # variância GUE de grande N ~ 0.180; GOE ~ 0.286, GSE ~ 0.104
    assert 0.16 < np.var(sd) < 0.20 and 0.16 < np.var(st) < 0.20
    assert abs(np.var(sd) - np.var(st)) < 0.015


def test_gue_energy_control_matches_count_and_range():
    from riemann_spectra.controls import gue_energy_levels_like
    rng = np.random.default_rng(9)
    g = np.linspace(1000.0, 3000.0, 2500)
    e = gue_energy_levels_like(g, rng=rng)
    assert len(e) == len(g) and np.all(np.diff(e) > 0)
    assert abs(e[0] - g[0]) < 1e-8 and abs(e[-1] - g[-1]) < 1e-6


def test_shuffle_spacings_invariance():
    """Verifica que o shuffle preserva o conjunto exato dos espaçamentos."""
    rng = np.random.default_rng(777)
    s_orig = np.array([0.5, 1.2, 0.8, 2.1, 0.3])
    x_rec = shuffle_spacings(s_orig, origin_x=10.0, rng=rng)
    s_rec = np.diff(x_rec)
    # Conjunto ordenado dos espaçamentos deve ser idêntico
    np.testing.assert_allclose(np.sort(s_rec), np.sort(s_orig))


def test_phase_randomization_preserves_power():
    """Verifica que a aleatorização de fases conserva exatamente os módulos |F(t)|."""
    rng = np.random.default_rng(999)
    signal = np.array([1.0 + 2.0j, -0.5 + 3.0j, 4.0 - 1.0j])
    rand_sig = randomize_fourier_phases(signal, preserve_hermitian=False, rng=rng)
    np.testing.assert_allclose(np.abs(rand_sig), np.abs(signal), atol=1e-12)
