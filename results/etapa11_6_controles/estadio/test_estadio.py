"""Testes do ctrl-estadio-v1 (sem rede, sem nenhum nível real do bilhar). Rodar da raiz:
   .venv/bin/python3 -m pytest -q results/etapa11_6_controles/estadio/test_estadio.py
"""
import json, math, sys
from pathlib import Path
import numpy as np
import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import instrumento_estadio as ie  # noqa: E402


def proxy_levels(k0, k1, seed=0, injected=False):
    rng = np.random.default_rng(seed)
    n = int(round(float(ie.n_bar(k1) - ie.n_bar(k0))))
    y = ie.goe_central_levels(n, 0.6, rng)
    x0, x1 = float(ie.n_bar(k0)), float(ie.n_bar(k1))
    x = x0 + (y - y[0]) * (x1 - x0) / (y[-1] - y[0])
    guess = np.linspace(k0, k1, n)
    return ie.inject_bouncing_ball(x, k_guess=guess) if injected else ie.inverse_n_bar(x, k_guess=guess)


def test_weyl_roundtrip():
    k = np.linspace(85.0, 305.0, 500)
    assert np.max(np.abs(ie.inverse_n_bar(ie.n_bar(k), k_guess=k) - k)) < 1e-9
    d = np.gradient(ie.n_bar(k), k)
    assert np.max(np.abs(d - ie.d_bar(k))[5:-5]) < 1e-6


def test_bb_density_is_derivative_of_counting():
    k = np.linspace(100.0, 100.5, 20001)
    num = np.gradient(ie.n_fl_bb(k), k)
    assert np.max(np.abs(num - ie.d_bb(k))[50:-50]) < 1e-3 * np.max(np.abs(ie.d_bb(k)))


def test_C_bb_matches_D1E():
    d1e = json.loads((HERE / "d1e_verificacoes.json").read_text())
    for name, b in d1e["blocks"].items():
        C = ie.C_bb_predicted(b["A"], b["B"], [2.0, 4.0])[2.0]
        ref = complex(*b["C_fit"])
        assert abs(C / ref - 1) < 1e-4, (name, C, ref)


def test_goe_has_level_repulsion():
    rng = np.random.default_rng(1)
    s = np.diff(ie.goe_central_levels(3000, 0.6, rng))
    s = s / s.mean()
    assert abs(s.mean() - 1) < 0.05
    assert np.mean(s < 0.1) < 0.02          # Poisson daria ~0,095


def test_injection_reproduces_counting_and_line():
    k = proxy_levels(85.5, 169.0, seed=3, injected=True)
    x = ie.n_bar(k) + ie.n_fl_bb(k)
    s = np.diff(x)
    assert abs(s.mean() - 1.0) < 0.01                       # densidade correta após unfolding com a família
    i = np.arange(len(x))
    assert np.max(np.abs(x - x[0] - i)) < 10.0              # rigidez: a escada não se afasta da reta (GOE)
    tr = ie.StadiumTransform(k[0], k[-1], 0.5, 5.0)
    F = np.abs(tr.evaluate(k, np.array([2.0, 3.3])))
    assert F[0] > 3 * F[1]                                  # pico em L = 2 bem acima de um t sem linha
    C = abs(ie.C_bb_predicted(k[0], k[-1], [2.0, 4.0])[2.0]) * tr.response['gain_W0'] / 2
    assert abs(F[0] / C - 1) < 0.3                          # amplitude compatível com a previsão da D1-E


def test_o1_catalog_module():
    lines = ie.load_o1()
    C = ie.C_bb_predicted(85.5, 304.0, [ln["length"] for ln in lines if ln["length"] <= 5.0])
    cat = ie.o1_catalog_module(lines, C).prime_power_catalog(0.5, 5.0)
    assert [round(c["period_theoretical"], 6) for c in cat] == [2.0, 4.0, 4.472136, 4.828427, 4.889432, 5.0]
    assert cat[0]["coefficient_theoretical"] > 0 and all(c["coefficient_theoretical"] == 0 for c in cat[1:])


def test_run_block_smoke(tmp_path):
    k = proxy_levels(85.5, 150.0, seed=5, injected=True)
    cfg = ie.load_config(HERE / "ctrl_estadio_v1.toml")
    cfg.update({"shuffle_sigma_realizations": 8, "shuffle_threshold_realizations": 40, "shuffle_score_realizations": 20,
                "goe_sigma_realizations": 4, "goe_threshold_realizations": 20, "goe_score_realizations": 0,
                "synthetic_realizations": 4, "phase_control_realizations": 20, "precision_perturbations": 2})
    res = ie.run_block_estadio(k, {"name": "smoke"}, cfg, ie.load_o1(), tmp_path, np.random.SeedSequence(7), workers=1)
    for f in ("blind_peaks.csv", "freeze.json", "arithmetic_matches.csv", "block_metrics.json"):
        assert (tmp_path / "smoke" / f).exists()
    ev = ie.evaluate_block(res, tmp_path / "smoke", cfg, ie.load_o1())
    assert {"E_C1", "E_C1o", "E_C4"} <= set(ev) and "E_C2bb" in res
