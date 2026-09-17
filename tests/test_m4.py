"""Testes das regras m4-v1: faixa inconclusiva, Holm, critérios de família, CUE e travas."""

import math

import numpy as np
import pytest

from riemann_spectra.periods import classify_detection, threshold_interval
from riemann_spectra.replication import evaluate_m2_family, evaluate_m3_family, holm_adjust


def test_threshold_interval_coverage_of_true_quantile():
    rng = np.random.default_rng(2)
    from scipy.stats import gumbel_r

    q = gumbel_r.ppf(0.95)
    hits = [(lambda ti: ti["z_low"] <= q <= ti["z_high"])(threshold_interval(rng.gumbel(size=999), 0.05)) for _ in range(1500)]
    assert np.mean(hits) >= 0.94
    ti = threshold_interval(rng.gumbel(size=999), 0.05)
    assert ti["coverage_exact"] >= 0.95 and ti["z_low"] <= ti["point_threshold"] <= ti["z_high"]
    assert classify_detection(ti["z_high"] + 1e-9, ti) == "detected"
    assert classify_detection(ti["z_high"], ti) == "inconclusive"
    assert classify_detection(ti["z_low"] - 1e-9, ti) == "not_detected"


def test_holm_matches_reference_values():
    adj = holm_adjust([0.01, 0.04, 0.03, 0.005])
    assert np.allclose(adj, [0.03, 0.06, 0.06, 0.02])
    assert holm_adjust([]) == []


def _block(pS, rec, unmatched, frac, Q, pQ, inc=0):
    return {"arithmetic": {
        "p_value_global_mc": pS, "recovery_among_clearly_detectable": rec, "unmatched_detections": unmatched,
        "inconclusive_candidates": inc,
        "coefficient_agreement": {"fraction_within_tolerance": frac, "n_eligible": 20},
        "phase_coherence": {"Q_observed": Q, "p_value_Q": pQ},
    }}


def test_family_criteria_logic():
    crit = {"alpha_family": 0.05, "recovery_min": 0.95, "max_blocks_with_unmatched": 2, "coefficient_fraction_min": 0.95,
            "q_min": 0.9, "ratio_tolerance": 1e-6, "clear_margin": 1.25}
    good = {f"b{i}": _block(1e-4, 1.0, 0, 1.0, 1.0, 1e-3) for i in range(10)}
    fam = evaluate_m3_family(good, crit)
    assert fam["C1_replicated_all_blocks"] and fam["C2_replicated_all_blocks"]
    bad = dict(good)
    bad["b3"] = _block(0.2, 1.0, 1, 1.0, 1.0, 1e-3)    # maior p: Holm multiplica por 1 -> 0.2 > 0.05, C1 falha
    bad["b4"] = _block(1e-4, 0.9, 1, 0.9, 1.0, 1e-3)   # recuperação e coeficientes abaixo do mínimo
    bad["b5"] = _block(1e-4, 1.0, 1, 1.0, 1.0, 1e-3)   # terceiro bloco com detecção sem correspondência
    fam = evaluate_m3_family(bad, crit)
    assert not fam["blocks"]["b3"]["C1_block_pass"] and not fam["blocks"]["b4"]["C1_block_pass"]
    assert not fam["blocks"]["b4"]["C2_block_pass"]
    assert fam["C1_blocks_with_unmatched_detection"] == 3 and not fam["C1_family_unmatched_ok"]
    assert not fam["C1_replicated_all_blocks"]


def test_m2_family_reports_min_attainable_holm():
    blocks = {f"b{i}": {"envelope_tests": {r: {s: {"p_value_mc": 0.001} for s in ("cdf", "r2", "k_connected")} for r in ("gue", "poisson")}}
              for i in range(10)}
    fam = evaluate_m2_family(blocks, 0.05)
    assert fam["gue_cdf"]["n_rejected"] == 10 and fam["gue_cdf"]["min_attainable_p_holm"] == pytest.approx(0.01)


def test_cue_exact_formulas_and_limit():
    from riemann_spectra import cue

    s = np.linspace(0, 2, 81)
    d = cue.spacing_distribution_cue(s, 2)
    assert np.max(np.abs(d["pdf"] - np.sin(np.pi * s / 2) ** 2)) < 1e-8
    assert np.max(np.abs(d["cdf"] - (s / 2 - np.sin(np.pi * s) / (2 * np.pi)))) < 1e-8
    grid = np.linspace(0, 4, 161)
    corr = cue.first_correction(grid)
    assert abs(np.trapezoid(corr["p0"], grid) - 1) < 1e-6
    assert abs(np.trapezoid(grid ** 2 * corr["p0"], grid) - 1 - 0.1800) < 2e-3
    table = {r["N"]: r for r in cue.expansion_domain_table(grid, corr, N_values=(3, 12))}
    # expansão truncada converge como N^-4: erro em N=12 ~ (3/12)^4 do erro em N=3
    assert table[12]["sup_abs_error_cdf_truncated"] < 0.05 * table[3]["sup_abs_error_cdf_truncated"]
    assert cue.n_eff(2.5041178e15) == pytest.approx(7.7376, abs=2e-3)   # valor citado na fonte
    assert cue.alpha_scale(2.5041178e15) == pytest.approx(1.0438, abs=1e-3)


def test_cue_haar_sampler_matches_exact_distribution():
    from riemann_spectra import cue

    rng = np.random.default_rng(4)
    N = 5
    sp = cue.sample_cue_spacings(N, 60000, rng)
    g = np.linspace(0, 4, 81)
    emp = np.searchsorted(np.sort(sp), g, side="right") / len(sp)
    ex = cue.spacing_distribution_cue(g, N)["cdf"]
    # espaçamentos de uma mesma matriz são dependentes; DKW com n efetivo = número de matrizes
    assert np.max(np.abs(emp - ex)) < math.sqrt(math.log(2 / 0.001) / (2 * 60000))


def test_run_requires_matching_lock(tmp_path, monkeypatch):
    from riemann_spectra import cli

    cfg = tmp_path / "c.toml"
    cfg.write_text('lock_scope = "package"\nrequires_lock = true\n')
    with pytest.raises(PermissionError):
        cli.require_matching_lock(str(cfg))
    monkeypatch.setattr(cli, "logger", cli.logger)
    assert cli.cmd_protocol_freeze(type("A", (), {"config": str(cfg), "note": ""})()) == 0
    assert cli.require_matching_lock(str(cfg))["lock_scope"] == "package"
    cfg.write_text('lock_scope = "package"\nrequires_lock = true\n# alterado\n')
    with pytest.raises(PermissionError):
        cli.require_matching_lock(str(cfg))


def test_m4v3_fwhm_is_exact_for_hann():
    """m4-v3: FWHM de Hann = 4π/L com precisão de máquina (corrige D1 da auditoria independente)."""
    from riemann_spectra.periods import measure_window_response

    for L in (1405.3, 2519.1, 2325.21046654, 2190.1):
        r = measure_window_response(L, "hann")
        assert abs(r["fwhm"] / (4 * math.pi / L) - 1) < 1e-14
        assert abs(r["first_null_in_units_2pi_over_L"] - 2.0) < 1e-13


def test_m4v3_cue_prediction_without_interpolation():
    """m4-v3: predição CUE avaliada exatamente em alpha·s (corrige D8)."""
    from riemann_spectra import cue

    s = np.linspace(0, 4, 81)
    corr = cue.first_correction(s)
    E = 20000.0
    pred = cue.zeros_prediction(corr, E)
    al, ne = float(cue.alpha_scale(E)), float(cue.n_eff(E))
    direct = cue.first_correction(al * s)
    assert np.max(np.abs(pred["cdf"] - (corr["P0"] + direct["P1"] / (al * ne * ne)))) < 1e-12


def test_m4v3_smooth_term_accuracy_at_large_height():
    """m4-v3: quadratura em coordenadas locais; termo suave × forma fechada independente (Si/Ci) ≤ 1e-9 em E ~ 5e4."""
    from scipy.special import sici
    from riemann_spectra.periods import OscillatoryTransform

    A, B = 50000.0, 52190.0
    tr = OscillatoryTransform(A, B, 0.5, 5.0, points_per_fwhm=8.0)
    t = tr.t_grid[::37]
    L, Ec, k, TAU = B - A, 0.5 * (A + B), 2 * math.pi / (B - A), 2 * math.pi

    def J(Om):
        a = np.abs(Om)
        sA, cA = sici(a * A)
        sB, cB = sici(a * B)
        inner = (cB - cA) + 1j * np.sign(Om) * (sB - sA)
        bnd = (math.log(B / TAU) * np.exp(1j * Om * B) - math.log(A / TAU) * np.exp(1j * Om * A)) / (1j * Om)
        return bnd - inner / (1j * Om)

    exact = np.exp(1j * Ec * t) * (0.5 * J(-t) - 0.25 * np.exp(-1j * k * A) * J(k - t) - 0.25 * np.exp(1j * k * A) * J(-k - t)) / TAU
    assert np.max(np.abs(tr.smooth[::37] - exact)) < 1e-9
