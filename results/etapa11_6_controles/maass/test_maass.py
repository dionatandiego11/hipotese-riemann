"""
Testes do controle ctrl-maass-v1 (sem rede). Nenhum teste aplica o instrumento aos autovalores reais: só a conferência
B dos dados (declaração §2) lê o arquivo. Rodar a partir da raiz:

  .venv/bin/python3 -m pytest -q results/etapa11_6_controles/maass/test_maass.py
"""
import math
import sys
from pathlib import Path

import numpy as np
import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import catalogo_g1 as g1  # noqa: E402
import instrumento_maass as im  # noqa: E402
from riemann_spectra.arithmetic import targeted_joint_fit  # noqa: E402

DATA = HERE.parents[2] / "Mass-Forms" / "lmfdb_maass_rigor_0919_1121.txt"
SP0 = {"beta": 0.0, "gamma": 0.0, "delta": 0.0}


# --- dados e catálogo ---------------------------------------------------------------------------

@pytest.mark.skipif(not DATA.exists(), reason="arquivo do LMFDB ausente")
def test_data_checks_B():
    d = im.load_maass(DATA)
    c = d["checks"]
    assert c["passed"] and c["n_forms"] == 2202 and c["n_odd"] == 1092 and c["n_even"] == 1110
    # ADENDO_MAASS_3: exatamente uma lacuna ímpar, entre os índices 341 e 342
    assert [(gp["after_index"], round(gp["R_left"], 4), round(gp["R_right"], 4)) for gp in c["odd_gaps"]] == [(341, 99.5791, 110.1701)]
    assert np.all(np.diff(d["odd"]) > 0)


def test_g1_lines_and_catalog_module():
    lines = im.load_g1_lines()
    cat = im.g1_catalog_module(lines).prime_power_catalog(0.5, 5.0)
    assert len(cat) == 22
    assert abs(cat[0]["period_theoretical"] - 2 * math.asinh(0.5)) < 1e-12
    assert abs(cat[0]["coefficient_theoretical"] + 0.137003421011) < 1e-11 and cat[0]["delta"] == -1
    assert all(c["catalog_index"] == i for i, c in enumerate(cat))
    assert all((c["coefficient_theoretical"] > 0) == (c["delta"] == 1) for c in cat)


def test_g1_small_discriminants_two_algorithms_agree():
    for D in (5, 8, 12, 13, 20, 21, 32, 45):
        cyc = g1.cycles(D)
        n_comp, comp, _ = g1.count_by_components(D)
        assert n_comp == len(cyc)
    assert [len(g1.cycles(D)) for D in (5, 8, 12, 21, 32)] == [1, 1, 2, 2, 3]


def test_absence_lines_do_not_coincide_with_g1():
    lines = [ln["length"] for ln in im.load_g1_lines()]
    for tl in im.absence_lines(0.5, 5.0).values():
        for t in tl:
            assert min(abs(t - L) for L in lines) > 1e-6


# --- contagem suave e unfolding ------------------------------------------------------------------

def test_fit_smooth_recovers_parameters():
    true = {"beta": -0.35, "gamma": 0.8, "delta": 1.5}
    R = np.linspace(10, 180, 400)
    j_float = im.n_bar(R, true) + 0.5
    X = np.column_stack([R * np.log(R), R, np.ones_like(R)])
    y = j_float - 0.5 - R * R / 24
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    assert np.allclose(coef, [true["beta"], true["gamma"], true["delta"]], atol=1e-9)


def test_inverse_n_bar_roundtrip():
    sp = {"beta": -0.3, "gamma": 0.5, "delta": 0.2}
    R = np.linspace(10, 185, 500)
    back = im.inverse_n_bar(im.n_bar(R, sp), sp)
    assert np.max(np.abs(back - R)) < 1e-9


def test_smooth_term_matches_direct_integral():
    sp = {"beta": -0.3, "gamma": 0.5, "delta": 0.2}
    tr = im.MaassTransform(20.0, 120.0, 0.5, 5.0, sp)
    E = np.linspace(20.0, 120.0, 400001)
    w = np.sin(math.pi * (E - 20.0) / 100.0) ** 2
    for k in (0, len(tr.t_grid) // 3, len(tr.t_grid) - 1):
        t = tr.t_grid[k]
        direct = np.trapezoid(w * im.d_bar(E, sp) * np.exp(-1j * (E - tr.E_c) * t), E)
        assert abs(direct - tr.smooth[k]) < 1e-6 * max(1.0, abs(direct))


# --- linhas sintéticas com sinais conhecidos sobre fundo de Poisson ------------------------------

def _levels(lines=None, seed=11, n=None):
    """Fundo de Poisson com contagem coerente com N̄ = R²/24 em [25, 180] (densidade mínima ≈ 2,1)."""
    rng = np.random.default_rng(seed)
    R0, R1 = 25.0, 180.0
    if n is None:
        n = int(round(float(im.n_bar(R1, SP0) - im.n_bar(R0, SP0)))) + 1
    x = im.poisson_unfolded(n, float(im.n_bar(R0, SP0)), float(im.n_bar(R1, SP0)), rng)
    if not lines:
        return im.inverse_n_bar(x, SP0)
    T = np.array([t for t, _ in lines])
    C = np.array([c for _, c in lines], dtype=np.complex128)
    return im.inject_lines(x, T, C, SP0)


def test_targeted_fit_recovers_injected_signs_differential():
    """
    Diferencial (mesmo fundo com e sem linhas). Com fundo de Poisson (sem rigidez), o termo cruzado entre o
    deslocamento dos níveis e o fundo dá ruído de ~5-10% por realização (medido: 8 sementes); o teste exige sinal
    correto em todas e média sem viés (|média − 1| < 0,06).
    """
    lines = [(0.962424, -0.4), (1.762747, -0.4), (1.924847, +0.4), (2.633916, +0.4)]
    cat = [{"catalog_index": k, "period_theoretical": t, "coefficient_theoretical": c} for k, (t, c) in enumerate(lines)]
    ratios = []
    for seed in range(8):
        g0, g1_ = _levels(seed=seed), _levels(lines, seed=seed)
        tr = im.MaassTransform(g0[0], g0[-1], 0.5, 5.0, SP0)

        def fit(g):
            return targeted_joint_fit(lambda t: tr.evaluate(g, t), cat, tr.L, tr.E_c, half_width=0.5 * tr.response["fwhm"],
                                      window="hann", sampling="band", include_conjugate=True)

        base, withl = fit(g0), fit(g1_)
        r = [(f1["coefficient_real"] - f0["coefficient_real"]) / c for (t, c), f0, f1 in zip(lines, base, withl)]
        assert all(x > 0 for x in r)            # sinal correto em todas as linhas e sementes
        ratios.append(r)
    assert np.all(np.abs(np.mean(ratios, axis=0) - 1.0) < 0.06), np.mean(ratios, axis=0)


def test_run_block_and_criteria_smoke(tmp_path):
    lines_g1 = im.load_g1_lines()
    inj = [(ln["length"], 1.5 * ln["coefficient"]) for ln in lines_g1 if ln["length"] <= 2.7]
    R = _levels(inj)
    cfg = im.load_config(HERE / "ctrl_maass_v1.toml")
    cfg.update({"shuffle_sigma_realizations": 8, "shuffle_threshold_realizations": 40, "shuffle_score_realizations": 20,
                "poisson_sigma_realizations": 4, "poisson_threshold_realizations": 20, "poisson_score_realizations": 0,
                "synthetic_realizations": 7, "phase_control_realizations": 20, "precision_perturbations": 2,
                "smooth_fit_max_rms": 100.0})   # fundo sintético de Poisson puro: escada oscila ~√N (só no teste)
    block = {"name": "smoke", "first_index": 1, "last_index": len(R)}
    res = im.run_block_maass(R, block, cfg, lines_g1, tmp_path, np.random.SeedSequence(3), workers=1)
    for fname in ("blind_peaks.csv", "freeze.json", "arithmetic_matches.csv", "block_metrics.json"):
        assert (tmp_path / "smoke" / fname).exists()
    ev = im.evaluate_block(res, tmp_path / "smoke", cfg, lines_g1)
    assert set(("M_C1", "M_C2s", "M_C2a_plus", "M_C2a_minus", "M_C4", "M_C4s", "passes")) <= set(ev)
    assert abs(res["smooth_fit"]["beta"]) < 1.0


def test_smoke_at_S2_resolution(tmp_path):
    """ADENDO_MAASS_4 §3: bloco inteiro em R ∈ [110, 178] (FWHM de S2), com linhas de G1 injetadas, roda até o fim."""
    rng = np.random.default_rng(5)
    R0, R1 = 110.0, 178.0
    n = int(round(float(im.n_bar(R1, SP0) - im.n_bar(R0, SP0)))) + 1
    x = im.poisson_unfolded(n, float(im.n_bar(R0, SP0)), float(im.n_bar(R1, SP0)), rng)
    lines_g1 = im.load_g1_lines()
    inj = [(ln["length"], 3.0 * ln["coefficient"]) for ln in lines_g1 if ln["length"] <= 2.7]
    R = im.inject_lines(x, [t for t, _ in inj], [c for _, c in inj], SP0)
    cfg = im.load_config(HERE / "ctrl_maass_v1.toml")
    cfg.update({"shuffle_sigma_realizations": 8, "shuffle_threshold_realizations": 40, "shuffle_score_realizations": 20,
                "poisson_sigma_realizations": 4, "poisson_threshold_realizations": 20, "poisson_score_realizations": 0,
                "synthetic_realizations": 2, "phase_control_realizations": 20, "precision_perturbations": 2,
                "smooth_fit_max_rms": 100.0})
    res = im.run_block_maass(R, {"name": "s2like", "first_index": 1, "last_index": len(R)}, cfg, lines_g1, tmp_path,
                             np.random.SeedSequence(9), workers=1)
    assert res["synthetic_isolated_design"]["n_iso_per_realization"] == 1
    ev = im.evaluate_block(res, tmp_path / "s2like", cfg, lines_g1)
    assert "passes" in ev

