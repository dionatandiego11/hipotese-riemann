"""
Testes que expõem os defeitos apontados na auditoria de 13/09/2026 (protocolo m3-v3).
"""

import csv
import json
import math
from pathlib import Path

import numpy as np
import pytest

from riemann_spectra.arithmetic import prime_power_catalog, targeted_joint_fit
from riemann_spectra.controls import generate_gue_central_levels, inject_density_lines
from riemann_spectra.periods import (
    OscillatoryTransform,
    detect_blind_peaks,
    max_statistic,
    measure_window_response,
    window_response,
    window_values,
)
from riemann_spectra.unfolding import n_bar_rvm


# --- simetria da estatística de decisão ----------------------------------------

def test_decision_z_is_grid_value_and_ignores_evaluator():
    """Pico fora da malha: a decisão usa |F| na malha, com ou sem refinamento por soma direta."""
    L = 3000.0
    t = np.arange(0.5, 1.5, 2 * math.pi / L / 8)
    T0 = t[1900] + 0.37 * (t[1] - t[0])          # linha entre dois pontos da malha
    F = 10.0 * window_response(t - T0, L).astype(complex) / (L / 2)
    sigma = np.full_like(t, 2.0)
    fwhm = 2 * (2 * math.pi / L)
    refined_eval = lambda tt: 10.0 * window_response(tt - T0, L).astype(complex) / (L / 2)  # noqa: E731
    with_eval = detect_blind_peaks(t, F, fwhm, sigma, candidate_z=1.0, evaluator=refined_eval)
    without = detect_blind_peaks(t, F, fwhm, sigma, candidate_z=1.0)
    assert len(with_eval) == len(without) == 1
    pk = with_eval[0]
    assert pk["z"] == without[0]["z"] == pytest.approx(abs(F[pk["grid_index"]]) / 2.0, rel=1e-15)
    assert pk["z"] == pytest.approx(max_statistic(F, sigma), rel=1e-15)
    assert pk["z_refined"] > pk["z"]  # o refinamento existe, mas é só descritivo


# --- propagação de configuração ------------------------------------------------

def test_instrument_params_require_and_propagate_window_and_density():
    from riemann_spectra.inverse_spectroscopy import _instrument, instrument_params

    g = np.linspace(1000.0, 3000.0, 2000)
    cfg = {"t_min": 0.5, "t_max": 2.0, "points_per_fwhm": 8.0, "window": "blackman_harris", "density": "theta",
           "quadrature_panel_length": 0.5, "quadrature_order": 8}
    tr = _instrument(instrument_params(g, cfg))
    assert tr.window == "blackman_harris" and tr.density == "theta"
    assert tr.to_metadata()["window"] == "blackman_harris"
    assert tr.response["fwhm_in_units_2pi_over_L"] == pytest.approx(2.6664, abs=1e-3)
    bad = dict(cfg)
    del bad["density"]
    with pytest.raises(KeyError):
        instrument_params(g, bad)
    with pytest.raises(ValueError):
        OscillatoryTransform(1000.0, 3000.0, 0.5, 2.0, window="kaiser")
    with pytest.raises(ValueError):
        OscillatoryTransform(1000.0, 3000.0, 0.5, 2.0, density="lowess")


def test_blackman_harris_response_matches_numerical_integral():
    L = 1500.0
    u = np.linspace(0.0, L, 400001)
    w = window_values(u + 100.0, 100.0, 100.0 + L, "blackman_harris")
    uc = u - L / 2
    for om in (0.0, 0.004, 0.013):
        num = np.trapezoid(w * np.exp(-1j * uc * om), u)
        assert abs(num - window_response(om, L, "blackman_harris")) < 1e-6 * L
    resp = measure_window_response(L, "blackman_harris")
    assert resp["first_null_in_units_2pi_over_L"] == pytest.approx(4.0, abs=1e-6)
    assert resp["sidelobe_level_db"] < -90


def test_level_injection_recovered_with_alternative_window():
    x = float(n_bar_rvm(1500.0)) + np.arange(3000) + 0.5
    T = np.array([1.3, 2.7])
    C = np.array([-0.05, 0.03 * np.exp(1j * 1.0)])
    E = inject_density_lines(x, T, C)
    tr = OscillatoryTransform(E[0], E[-1], 0.5, 4.0, window="blackman_harris")
    Fv = tr.evaluate(E, T)
    C_hat = 2 * Fv * np.exp(-1j * tr.E_c * T) / tr.response["gain_W0"]
    assert np.max(np.abs(C_hat - C)) < 2e-3


# --- estimador direcionado com lóbulo conjugado -----------------------------------

def test_conjugate_lobe_estimator_is_exact_when_conjugate_leaks():
    L, Ec = 300.0, 800.0
    cat = [{"period_theoretical": 0.03, "coefficient_theoretical": -0.2, "catalog_index": 0},
           {"period_theoretical": 0.07, "coefficient_theoretical": 0.1, "catalog_index": 1}]
    C = np.array([-0.2 + 0.03j, 0.1 - 0.02j])
    T = np.array([c["period_theoretical"] for c in cat])

    def evaluator(t):
        t = np.asarray(t)[:, None]
        return (0.5 * C * np.exp(1j * Ec * T) * window_response(t - T, L)
                + 0.5 * np.conj(C) * np.exp(-1j * Ec * T) * window_response(t + T, L)).sum(axis=1)

    hw = 0.5 * 2 * (2 * math.pi / L)
    with_c = targeted_joint_fit(evaluator, cat, L, Ec, hw, include_conjugate=True)
    without = targeted_joint_fit(evaluator, cat, L, Ec, hw, include_conjugate=False)
    got = np.array([f["coefficient_real"] + 1j * f["coefficient_imag"] for f in with_c])
    bad = np.array([f["coefficient_real"] + 1j * f["coefficient_imag"] for f in without])
    assert np.max(np.abs(got - C)) < 1e-10
    assert np.max(np.abs(bad - C)) > 1e-4
    centers = targeted_joint_fit(evaluator, cat, L, Ec, hw, include_conjugate=True, sampling="centers")
    got_c = np.array([f["coefficient_real"] + 1j * f["coefficient_imag"] for f in centers])
    assert np.max(np.abs(got_c - C)) < 1e-10


# --- dados: critério estrito e vínculo validação/conjunto ------------------------

def test_mpmath_validation_uses_declared_error_without_factor():
    from riemann_spectra.data import validate_with_mpmath

    good = np.array([14.134725142])
    bad = np.array([14.134725141734695 + 4.0e-9])  # dentro de 2x, fora de 1x o erro declarado
    assert validate_with_mpmath(good, sample_size=1, dps=30)["all_within_tolerance"] is True
    assert validate_with_mpmath(bad, sample_size=1, dps=30)["all_within_tolerance"] is False


def test_validation_must_match_loaded_dataset(tmp_path: Path):
    from riemann_spectra.data import check_validation_matches_dataset, save_processed_csv
    from riemann_spectra.utils import compute_file_sha256

    f = tmp_path / "z.csv"
    save_processed_csv(np.array([14.1, 21.0, 25.0]), f)
    val = {"processed_sha256": compute_file_sha256(f), "n_zeros_in_file": 3}
    check_validation_matches_dataset(val, f, 3)
    with pytest.raises(RuntimeError):
        check_validation_matches_dataset(val, f, 2)
    with pytest.raises(RuntimeError):
        check_validation_matches_dataset({**val, "processed_sha256": "0" * 64}, f, 3)


def test_m2_blocks_must_be_declared():
    from riemann_spectra.spectral_pipeline import m2_blocks

    with pytest.raises(KeyError):
        m2_blocks({})
    assert m2_blocks({"m2_blocks": [{"name": "a", "first_index": 10001, "last_index": 20000}]}) == [("a", 10001, 20000)]


# --- calibração do teste de envelope --------------------------------------------

def test_symmetric_envelope_test_is_calibrated_under_exchangeability():
    from riemann_spectra.spectral_pipeline import _envelope_test

    rng = np.random.default_rng(0)
    B, trials = 19, 2000
    ps = []
    for _ in range(trials):
        scale = rng.uniform(0.5, 2.0, size=30)
        obs = {"k": rng.normal(size=30) * scale}
        ens = [{"k": rng.normal(size=30) * scale} for _ in range(B)]
        ps.append(_envelope_test(obs, ens, "k")["p_value_mc"])
    ps = np.array(ps)
    # p discreto em {1/20, ..., 1}: sob permutabilidade, P(p <= k/20) = k/20
    assert abs(np.mean(ps <= 0.05) - 0.05) < 0.015
    assert abs(np.mean(ps <= 0.25) - 0.25) < 0.03


# --- integração M3: conjuntos nulos independentes e artefatos congelados ----------

def test_run_block_uses_independent_null_sets(tmp_path: Path):
    from riemann_spectra.inverse_spectroscopy import run_block

    rng = np.random.default_rng(5)
    y, _ = generate_gue_central_levels(1500, 0.6, rng)
    x = float(n_bar_rvm(2000.0)) + y - y[0]
    E = inject_density_lines(x, np.array([1.1, 2.2]), np.array([-0.08, 0.06]))
    cfg = {
        "protocol_version": "test", "t_min": 0.5, "t_max": 2.5, "window": "hann", "density": "rvm",
        "points_per_fwhm": 8.0, "quadrature_panel_length": 0.5, "quadrature_order": 8,
        "primary_null": "shuffle", "candidate_z": 3.0, "noise_smooth_window": 0.05, "alpha": 0.2,
        "shuffle_sigma_realizations": 10, "shuffle_threshold_realizations": 19, "shuffle_score_realizations": 19,
        "gue_sigma_realizations": 3, "gue_threshold_realizations": 4, "gue_score_realizations": 0,
        "gue_retained_fraction": 0.6, "synthetic_realizations": 2, "synthetic_lines_per_realization": 4,
        "synthetic_pair_separations_fwhm": [1.0, 2.0], "matching_tolerance_quantile": 0.99,
        "recovery_curve_z_edges": [0.5, 1.0, 4.0], "resolution_recovery_target": 0.9,
        "targeted_fit_half_width_fwhm": 0.5, "targeted_fit_primary": "band_conjugate",
        "targeted_fit_variants": {"band_conjugate": {"sampling": "band", "include_conjugate": True},
                                  "band_no_conjugate": {"sampling": "band", "include_conjugate": False}},
        "phase_control_realizations": 19, "declared_table_error": 3e-9, "precision_perturbations": 2,
        "threshold_confidence": 0.95,
        "criteria": {"clear_margin": 1.25, "ratio_tolerance": 1e-6},
    }
    block = {"name": "t", "first_index": 1, "last_index": len(E)}
    res = run_block(E, block, cfg, tmp_path, np.random.SeedSequence(1), workers=1)
    data = np.load(tmp_path / "t" / "nulls.npz")
    assert len(data["shuffle_null_max"]) == 19 and len(data["shuffle_score_set_max"]) == 19
    assert not np.any(np.isin(data["shuffle_score_set_max"], data["shuffle_null_max"]))
    assert res["arithmetic"]["B_score"] == 19
    freeze = json.loads((tmp_path / "t" / "freeze.json").read_text())
    assert freeze["decision_statistic"].startswith("z na malha")
    ti = res["null_summary"]["shuffle"]["threshold_interval"]
    assert ti["z_low"] <= ti["point_threshold"] <= ti["z_high"]
    for p in csv.DictReader(open(tmp_path / "t" / "blind_peaks.csv")):
        z = float(p["z"])
        expected = "detected" if z > ti["z_high"] else ("not_detected" if z < ti["z_low"] else "inconclusive")
        assert p["class_primary"] == expected
    assert (tmp_path / "t" / "inconclusive_candidates.csv").exists()
    header = (tmp_path / "t" / "blind_peaks.csv").read_text().splitlines()[0]
    assert "z_refined" in header and "grid_period" in header
    with pytest.raises(ValueError):
        run_block(E, {"name": "x", "first_index": 1, "last_index": len(E) + 1}, cfg, tmp_path, np.random.SeedSequence(1))
