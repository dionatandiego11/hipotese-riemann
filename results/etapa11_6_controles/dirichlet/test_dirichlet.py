"""
Testes do controle ctrl-dirichlet-v1 (sem rede). Rodar a partir da raiz do repositório:

  .venv/bin/python3 -m pytest -q results/etapa11_6_controles/dirichlet/test_dirichlet.py
"""

import math
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import dirichlet_zeros as dz  # noqa: E402
import instrumento_chi as ic  # noqa: E402
from riemann_spectra.arithmetic import targeted_joint_fit  # noqa: E402
from riemann_spectra.controls import generate_gue_central_levels  # noqa: E402
from riemann_spectra.periods import OscillatoryTransform  # noqa: E402

CH4, CH5 = dz.CHARACTERS["chi_m4"], dz.CHARACTERS["chi_5"]


# --- caracteres (declaração §2; D1 §1) ------------------------------------------------------

def test_character_values():
    assert [CH4(n) for n in range(1, 9)] == [1, 0, -1, 0, 1, 0, -1, 0]
    assert [CH5(n) for n in range(1, 11)] == [1, -1, -1, 1, 0, 1, -1, -1, 1, 0]
    assert CH4(-1) == -1 and CH4.kappa == 1
    assert CH5(-1) == 1 and CH5.kappa == 0


@pytest.mark.parametrize("ch", [CH4, CH5])
def test_completely_multiplicative_and_real(ch):
    for m in range(1, 40):
        for n in range(1, 40):
            assert ch(m * n) == ch(m) * ch(n)


@pytest.mark.parametrize("ch", [CH4, CH5])
def test_Z_is_real_on_critical_line(ch):
    """V4 / D1 §2: ε(χ) = 1 ⇒ e^{iθ}L(½+it) real."""
    for t in (7.0, 50.0, 300.0):
        with mp.workdps(30):
            z = dz.Z_complex(t, ch)
            assert abs(mp.im(z)) / abs(z) < 1e-20


@pytest.mark.parametrize("ch", [CH4, CH5])
def test_hurwitz_matches_mpmath_dirichlet(ch):
    with mp.workdps(30):
        for t in (3.0, 40.0):
            s = mp.mpf("0.5") + 1j * t
            assert abs(dz.L_hurwitz(s, ch) - dz.L_dirichlet(s, ch)) < mp.mpf("1e-25")


def test_first_zeros_and_sign_changes():
    f = dz.ZeroFinder(CH5)
    zeros = f.scan(0.0, n_max=3)
    assert len(zeros) == 3 and all(b > a for a, b in zip(zeros, zeros[1:]))
    for g in zeros:
        with mp.workdps(40):
            assert (dz.Z_real(g - 1e-8, CH5, dz.L_dirichlet) > 0) != (dz.Z_real(g + 1e-8, CH5, dz.L_dirichlet) > 0)
    # V1 no próprio conjunto: contagem compatível com θ_χ/π
    assert dz.v1_completeness(zeros, CH5)["passed"]


def test_v4_points_are_midpoints_between_zeros():
    """Adendo 1: nenhum ponto de V4 cai num zero; o último é o ponto médio entre os dois últimos zeros."""
    zeros = [6.0, 10.2, 13.0, 16.4, 18.3, 21.0, 25.5, 27.9, 30.1, 33.0]
    pts = dz.v4_points(zeros, n_points=10)
    assert len(pts) == 10
    assert pts[-1] == 0.5 * (zeros[-2] + zeros[-1])
    for t in pts:
        j = int(np.searchsorted(zeros, t))
        assert 0 < j < len(zeros) and zeros[j - 1] < t < zeros[j]
        assert min(abs(t - z) for z in zeros) >= 0.5 * min(b - a for a, b in zip(zeros, zeros[1:])) - 1e-12


def test_v4_passes_on_computed_zeros():
    f = dz.ZeroFinder(CH4)
    zeros = f.scan(0.0, n_max=4)
    assert dz.v4_reality(CH4, zeros, n_points=4)["passed"]


def test_mean_spacing_step_not_larger_than_declared():
    for q in (4, 5):
        for t in (6.0, 100.0, 1e4):
            lg = math.log(q * t / (2 * math.pi))
            if lg > 0:
                assert dz.mean_spacing(t, q) <= 2 * math.pi / lg + 1e-12


# --- densidade e unfolding (P2; D1 §4) --------------------------------------------------------

@pytest.mark.parametrize("ch", [CH4, CH5])
def test_density_error_bound(ch):
    a = ch.a
    C_a = (2 * a * a + 2 * a + 2 * math.sqrt(2) / 3) / (2 * math.pi)
    E = np.linspace(6.0, 12000.0, 4000)
    err = np.abs(ic.d_theta_chi(E, ch.q, ch.kappa) - ic.d_bar_chi(E, ch.q))
    assert np.all(err <= C_a / E ** 2 + 1e-15)


@pytest.mark.parametrize("ch", [CH4, CH5])
def test_n_bar_inverse_roundtrip(ch):
    E = np.concatenate([np.linspace(6.0, 20.0, 50), np.geomspace(20.0, 12000.0, 200)])
    x = ic.n_bar_chi(E, ch.q, ch.kappa)
    back = ic.inverse_n_bar_chi(x, ch.q, ch.kappa)
    assert np.max(np.abs(back - E) / E) < 1e-10


def test_chi_transform_q1_reproduces_frozen_instrument():
    """Com q = 1, d̄_χ = d̄_rvm: o construtor copiado deve reproduzir o termo suave congelado."""
    A, B = 2000.0, 4000.0
    frozen = OscillatoryTransform(A, B, 0.5, 5.0, points_per_fwhm=8.0, panel_length=0.5, quad_order=8, density="rvm", window="hann")
    chi = ic.ChiTransform(A, B, 0.5, 5.0, q=1, kappa=0, points_per_fwhm=8.0, panel_length=0.5, quad_order=8, window="hann")
    assert np.array_equal(frozen.t_grid, chi.t_grid)
    assert np.max(np.abs(frozen.smooth - chi.smooth)) < 1e-12 * max(1.0, np.max(np.abs(frozen.smooth)))
    levels = np.linspace(A + 0.3, B - 0.3, 2500)
    assert np.max(np.abs(frozen.transform(levels) - chi.transform(levels))) < 1e-9


def test_chi_transform_accepts_window_below_2pi():
    tr = ic.ChiTransform(6.0, 3000.0, 0.5, 5.0, q=4, kappa=1)
    assert tr.A == 6.0
    with pytest.raises(ValueError):
        ic.ChiTransform(1.0, 3000.0, 0.5, 5.0, q=4, kappa=1)


# --- catálogo com χ (P1; D1 §3) ------------------------------------------------------------------

def _cat(ch):
    return {c["prime"] ** c["repetition"]: c for c in ic.chi_catalog_module(ch).prime_power_catalog(0.5, 5.0)}


def test_catalog_chi_m4():
    cat = _cat(CH4)
    for n in (2, 4, 8, 16, 32, 64, 128):
        assert cat[n]["coefficient_theoretical"] == 0 and cat[n]["chi"] == 0
    for n in (3, 7, 11, 19, 23):   # p ≡ 3 (mod 4): sinal trocado
        assert cat[n]["coefficient_theoretical"] > 0 and cat[n]["coefficient_theoretical"] == -cat[n]["coefficient_zeta"]
    for n in (5, 13, 9, 49):       # p ≡ 1 (mod 4) e quadrados de p ≡ 3: sinal de ζ
        assert cat[n]["coefficient_theoretical"] == cat[n]["coefficient_zeta"] < 0
    assert abs(cat[3]["coefficient_theoretical"] - math.log(3) / (math.pi * math.sqrt(3))) < 1e-15


def test_catalog_chi_5():
    cat = _cat(CH5)
    for n in (5, 25, 125):
        assert cat[n]["coefficient_theoretical"] == 0
    for n in (2, 3, 7, 8, 13, 17):  # χ(n) = −1
        assert cat[n]["coefficient_theoretical"] > 0
    for n in (4, 9, 11, 16, 19):   # χ(n) = +1
        assert cat[n]["coefficient_theoretical"] < 0


# --- cadeia sintética com linhas de sinais conhecidos ---------------------------------------------

def _synthetic_levels(ch, n=3000, seed=7, lines=None):
    rng = np.random.default_rng(seed)
    y, _ = generate_gue_central_levels(n, 0.6, rng)
    x0, x1 = float(ic.n_bar_chi(1500.0, ch.q, ch.kappa)), float(ic.n_bar_chi(3500.0, ch.q, ch.kappa))
    x0, x1 = x0, x0 + (n - 1)
    x = x0 + (y - y[0]) * (x1 - x0) / (y[-1] - y[0])
    if not lines:
        return ic.fold_chi(x, ch.q, ch.kappa)
    T = np.array([t for t, _ in lines])
    C = np.array([c for _, c in lines], dtype=np.complex128)
    return ic.inject_lines_chi(x, T, C, ch.q, ch.kappa)


def test_targeted_fit_recovers_injected_signs():
    """
    Resposta do instrumento a linhas injetadas com sinais conhecidos. O fundo GUE sintético não é uma fórmula explícita,
    então a comparação é diferencial: mesmos níveis base (mesma semente) com e sem as linhas.
    """
    lines = [(math.log(3), +0.20), (math.log(5), -0.15), (math.log(7), +0.10)]
    g0 = _synthetic_levels(CH4, lines=None)
    g1 = _synthetic_levels(CH4, lines=lines)
    cat = [{"catalog_index": k, "period_theoretical": t, "coefficient_theoretical": c} for k, (t, c) in enumerate(lines)]

    def fit(g):
        tr = ic.ChiTransform(g0[0], g0[-1], 0.5, 5.0, q=4, kappa=1)
        return targeted_joint_fit(lambda t: tr.evaluate(g, t), cat, tr.L, tr.E_c, half_width=0.5 * tr.response["fwhm"],
                                  window="hann", sampling="band", include_conjugate=True)

    base, withl = fit(g0), fit(g1)
    for (t, c), f0, f1 in zip(lines, base, withl):
        delta = f1["coefficient_real"] - f0["coefficient_real"]
        assert np.sign(delta) == np.sign(c)
        # 5%: os níveis com linhas deslocam as bordas da janela (efeito de borda observado ~1–2,5%)
        assert abs(delta / c - 1.0) < 0.05, (t, c, delta)


def test_run_block_smoke(tmp_path):
    """Execução completa de um bloco com poucas realizações (só verifica que a cadeia roda e grava tudo)."""
    ch = CH4
    lines = [(math.log(3), +0.20), (math.log(5), -0.15)]
    g = _synthetic_levels(ch, n=1500, lines=lines)
    cfg = ic.load_config(HERE / "ctrl_dirichlet_v1.toml")
    cfg = {k: v for k, v in cfg.items() if k != "characters"}
    cfg.update({"shuffle_sigma_realizations": 8, "shuffle_threshold_realizations": 40, "shuffle_score_realizations": 20,
                "gue_sigma_realizations": 4, "gue_threshold_realizations": 20, "gue_score_realizations": 0,
                "synthetic_realizations": 7, "phase_control_realizations": 20, "precision_perturbations": 2})
    block = {"name": "smoke", "first_index": 1, "last_index": len(g)}
    res = ic.run_block_chi(g, block, cfg, ch, tmp_path, np.random.SeedSequence(1), workers=1)
    for fname in ("blind_peaks.csv", "freeze.json", "arithmetic_matches.csv", "block_metrics.json"):
        assert (tmp_path / "smoke" / fname).exists()
    summary = ic.evaluate_criteria({"smoke": res}, tmp_path, cfg, ch)
    assert set(("D_C1", "D_C1z", "D_C2", "D_C2s", "D_C2z", "passes")) <= set(summary)


# --- Adendo 2: aceitação do refinamento, salvamento e retomada -----------------------------------------------------

import json as _json
import os as _os
import signal as _signal
import subprocess as _sp
import time as _time

PILOT = HERE.parent / "dados_piloto"


def _zeros_file(d, name, n):
    return (Path(d) / f"zeros_{name}_{n}.txt").read_bytes()


def test_T3_refinement_rejects_unconverged_interval():
    f = dz.ZeroFinder(CH5, illinois_max=1, bisect_max=1)
    with pytest.raises(dz.RefinementError):
        f.scan(0.0, n_max=1)


def test_T3_run_stops_without_writing_zero(tmp_path):
    with pytest.raises(dz.RefinementError):
        dz.run(CH5, 3, tmp_path, _finder_kw={"illinois_max": 1, "bisect_max": 1})
    assert not (tmp_path / "zeros_chi_5_3.txt").exists()
    st = _json.loads((tmp_path / "progresso_chi_5_3.json").read_text())
    assert st["phase"] == "scan" and st["scan"]["zeros"] == []


def test_refine_bisection_fallback_converges():
    f = dz.ZeroFinder(CH5, illinois_max=2)
    z = f.scan(0.0, n_max=2)
    ref = dz.ZeroFinder(CH5).scan(0.0, n_max=2)
    assert f.stats.bisection_fallbacks >= 1
    assert max(abs(a - b) for a, b in zip(z, ref)) <= 1e-10


def test_regression_first_zeros_match_pilot():
    """Adendo 2, §4 (regressão): o código novo reproduz as linhas do piloto (9 casas)."""
    for name in ("chi_m4", "chi_5"):
        path = PILOT / f"zeros_{name}_500.txt"
        if not path.exists():
            pytest.skip("arquivo do piloto ausente")
        pilot = path.read_text().split()[:25]
        new = [f"{g:.9f}" for g in dz.ZeroFinder(dz.CHARACTERS[name]).scan(0.0, n_max=25)]
        assert new == pilot


@pytest.mark.parametrize("stop", [{"scan": 5}, {"v2": 4}])
def test_T1_internal_interrupt_and_resume_is_bitwise_identical(tmp_path, stop):
    ref_dir, int_dir = tmp_path / "ref", tmp_path / "int"
    dz.run(CH4, 12, ref_dir, every_zeros=3)
    with pytest.raises(dz.Interrupted):
        dz.run(CH4, 12, int_dir, every_zeros=3, _stop_after=stop)
    st = _json.loads((int_dir / "progresso_chi_m4_12.json").read_text())
    assert st["phase"] in ("scan", "V2")
    m = dz.run(CH4, 12, int_dir, every_zeros=3)
    assert m["resumes"] == 1
    assert _zeros_file(ref_dir, "chi_m4", 12) == _zeros_file(int_dir, "chi_m4", 12)
    ref_m = _json.loads((ref_dir / "manifest_chi_m4_12.json").read_text())
    for k in ("V1", "V2", "V3", "V4"):
        assert m["checks"][k]["passed"] == ref_m["checks"][k]["passed"]
    assert m["checks"]["V2"]["max_abs_difference"] == ref_m["checks"]["V2"]["max_abs_difference"]


def test_T2_resume_refuses_changed_parameters(tmp_path):
    with pytest.raises(dz.Interrupted):
        dz.run(CH4, 6, tmp_path, every_zeros=1, _stop_after={"scan": 2})
    p = tmp_path / "progresso_chi_m4_6.json"
    for key, val in (("script_sha256", "0" * 64), ("character", "chi_5"), ("n", 7), ("dps", 40), ("refine_tol", 1e-9)):
        st = _json.loads(p.read_text())
        good = st["params"][key]
        st["params"][key] = val
        p.write_text(_json.dumps(st))
        with pytest.raises(RuntimeError, match="retomada recusada"):
            dz.run(CH4, 6, tmp_path)
        st["params"][key] = good
        p.write_text(_json.dumps(st))


def test_T2_resume_refuses_changed_Z_at_saved_point(tmp_path):
    with pytest.raises(dz.Interrupted):
        dz.run(CH4, 6, tmp_path, every_zeros=1, _stop_after={"scan": 2})
    p = tmp_path / "progresso_chi_m4_6.json"
    st = _json.loads(p.read_text())
    st["scan"]["fa"] = st["scan"]["fa"] * (1 + 1e-12) + 1e-300
    p.write_text(_json.dumps(st))
    with pytest.raises(RuntimeError, match="difere do valor gravado"):
        dz.run(CH4, 6, tmp_path)


def test_lock_blocks_second_live_process(tmp_path):
    (tmp_path / ".lock_chi_m4_6").write_text(str(_os.getppid()))   # processo vivo que não é este
    with pytest.raises(RuntimeError, match="outra execução"):
        dz.run(CH4, 6, tmp_path)


def test_T1_real_process_sigterm_and_resume(tmp_path):
    """Processo real terminado por SIGTERM no meio da varredura e reiniciado: arquivo final idêntico ao contínuo."""
    root = HERE.parents[2]
    py = root / ".venv" / "bin" / "python3"
    script = HERE / "dirichlet_zeros.py"
    n = 20
    ref_dir, int_dir = tmp_path / "ref", tmp_path / "int"
    cmd = lambda d: [str(py), str(script), "--carater", "chi_5", "--n", str(n), "--saida", str(d), "--salvar-a-cada", "2"]
    assert _sp.run(cmd(ref_dir), cwd=root, capture_output=True, timeout=900).returncode == 0
    proc = _sp.Popen(cmd(int_dir), cwd=root, stdout=_sp.PIPE, stderr=_sp.PIPE)
    prog = int_dir / f"progresso_chi_5_{n}.json"
    deadline = _time.time() + 600
    while _time.time() < deadline:
        try:
            st = _json.loads(prog.read_text())
            if st.get("phase") == "scan" and len(st.get("scan", {}).get("zeros", [])) >= 6:
                break
        except (FileNotFoundError, ValueError):
            pass
        _time.sleep(0.2)
    proc.send_signal(_signal.SIGTERM)
    _, err = proc.communicate(timeout=120)
    assert proc.returncode == 130, err.decode()
    st = _json.loads(prog.read_text())
    assert st["phase"] == "scan" and 6 <= len(st["scan"]["zeros"]) < n
    assert not (int_dir / f".lock_chi_5_{n}").exists()
    r = _sp.run(cmd(int_dir), cwd=root, capture_output=True, timeout=900)
    assert r.returncode == 0, r.stderr.decode()
    assert _zeros_file(ref_dir, "chi_5", n) == _zeros_file(int_dir, "chi_5", n)
    m = _json.loads((int_dir / f"manifest_chi_5_{n}.json").read_text())
    assert m["resumes"] == 1 and m["all_checks_passed"]
