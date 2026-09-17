"""
riemann_indep.pipeline — cadeia M3/M4 e M2 para um bloco, a partir da especificação.
Ordem: instrumento → nulos (σ, limiar, escore; GUE) → sintéticos → detecção nos zeros e gravação
→ aritmética → M2 → CUE. Nenhum arquivo de referência é lido aqui.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
from multiprocessing import Pool
from pathlib import Path

import numpy as np

from . import core, spectral, stats

CFG = {
    "t_min": 0.5, "t_max": 5.0, "ppf": 8.0, "alpha": 0.05, "conf": 0.95, "floor": 3.0, "sigma_width": 0.05,
    "B_sigma": 200, "B_thr": 1999, "B_score": 1999, "gue_sigma": 100, "gue_thr": 199,
    "syn_real": 40, "syn_lines": 12, "pair_seps": [0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0],
    "tol_quantile": 0.99, "res_target": 0.9, "clear_margin": 1.5, "ratio_tol": 1e-6,
    "phase_B": 999, "m2_gue": 299, "m2_poisson": 299, "gue_fraction": 0.6,
}

_G: dict = {}


def _init(gammas, t0, dt, n_t, A, B, smooth):
    _G.update(gammas=gammas, t0=t0, dt=dt, n_t=n_t, A=A, B=B, smooth=smooth)


def _F(levels):
    return core.recurrence_sum(levels, _G["t0"], _G["dt"], _G["n_t"], _G["A"], _G["B"]) - _G["smooth"]


def _power(args):
    kind, seed = args
    rng = np.random.default_rng(seed)
    lv = stats.shuffle_null(_G["gammas"], rng) if kind == "shuffle" else stats.gue_null(_G["gammas"], rng)
    return np.abs(_F(lv)) ** 2


def _maxz(args):
    kind, seed, sigma = args
    rng = np.random.default_rng(seed)
    lv = stats.shuffle_null(_G["gammas"], rng) if kind == "shuffle" else stats.gue_null(_G["gammas"], rng)
    F = _F(lv)
    t = _G["t0"] + _G["dt"] * np.arange(_G["n_t"])
    peaks, zmax = stats.blind_peaks(t, F, sigma, 8, CFG["floor"])
    return zmax, np.array([p["t"] for p in peaks]), np.array([p["z"] for p in peaks])


def _synthetic(args):
    seed, sigma, thr, W0, fwhm, n_lines, zr, sep = args
    rng = np.random.default_rng(seed)
    g = _G["gammas"]
    t = _G["t0"] + _G["dt"] * np.arange(_G["n_t"])
    y = stats.gue_central_unfolded(len(g), rng, CFG["gue_fraction"])
    x0, x1 = core.nbar(g[0]), core.nbar(g[-1])
    x = x0 + (y - y[0]) * (x1 - x0) / (y[-1] - y[0])
    lo, hi = CFG["t_min"] + 0.05, CFG["t_max"] - 0.05
    if sep is None:
        T = []
        while len(T) < n_lines:
            c = rng.uniform(lo, hi)
            if all(abs(c - v) > 10 * fwhm for v in T):
                T.append(c)
        T = np.array(T)
    else:
        cen = rng.uniform(lo, hi, n_lines // 2)
        T = np.sort(np.concatenate([cen - 0.5 * sep * fwhm, cen + 0.5 * sep * fwhm]))
    zt = rng.uniform(zr[0], zr[1], len(T))
    mod = zt * np.interp(T, t, sigma) * 2.0 / W0
    Cc = mod * np.exp(1j * rng.uniform(0, 2 * math.pi, len(T)))
    budget = 0.8 * math.log(g[0] / core.TAU) / core.TAU
    keep = np.zeros(len(T), bool)
    used = 0.0
    step = 1 if sep is None else 2
    for k in range(0, len(T) - step + 1, step):
        cost = float(np.sum(mod[k:k + step]))
        if used + cost <= budget:
            keep[k:k + step] = True
            used += cost
    if not keep.any():
        return []
    T, zt, Cc = T[keep], zt[keep], Cc[keep]
    F = _F(stats.inject_lines(x, T, Cc))
    peaks, _ = stats.blind_peaks(t, F, sigma, 8, min(CFG["floor"], thr))
    det = np.array([p["t"] for p in peaks if p["z"] > thr])
    return [{"T": float(T[k]), "z_true": float(zt[k]), "err": float(det[np.argmin(np.abs(det - T[k]))] - T[k]) if len(det) else float("inf"),
             "sep": sep} for k in range(len(T))]


def _m2_member(args):
    kind, n, seed, grid, tau = args
    rng = np.random.default_rng(seed)
    x = stats.gue_central_unfolded(n, rng, CFG["gue_fraction"]) if kind == "gue" else stats.poisson_fixed(n, rng)
    return spectral.spacing_cdf(x, grid), spectral.pair_correlation(x), spectral.form_factor_connected(x, tau), float(np.var(np.diff(x), ddof=1))


def run_block(label: str, i0: int, i1: int, seed: int, out_root: Path, raw: str = "data/raw/zeros1", workers: int = 4,
              max_allowed_index: int = 70000) -> dict:
    """`max_allowed_index` (v2): limite explícito de acesso aos dados; o valor padrão preserva a reserva de v1."""
    if i1 > max_allowed_index:
        raise PermissionError(f"Índices > {max_allowed_index} não autorizados nesta execução.")
    out = out_root / label
    out.mkdir(parents=True, exist_ok=True)
    tim = {}
    t_start = time.perf_counter()
    g = core.read_raw_zeros(raw, i0, i1)
    ins = core.Instrument(g, CFG["t_min"], CFG["t_max"], CFG["ppf"])
    F = ins.F(g)  # soma direta
    tim["instrument"] = time.perf_counter() - t_start
    ss = np.random.SeedSequence(seed)
    s_sh, s_gue, s_syn, s_phase, s_m2 = ss.spawn(5)

    with Pool(workers, initializer=_init, initargs=(g, ins.t[0], ins.dt, ins.n_t, ins.A, ins.B, ins.smooth)) as pool:
        nulls = {}
        for kind, child, nb_sig, nb_thr, nb_score in (("shuffle", s_sh, CFG["B_sigma"], CFG["B_thr"], CFG["B_score"]),
                                                      ("gue", s_gue, CFG["gue_sigma"], CFG["gue_thr"], 0)):
            t0 = time.perf_counter()
            a, b, c = child.spawn(3)
            P = np.mean(pool.map(_power, [(kind, s) for s in a.spawn(nb_sig)], chunksize=8), axis=0)
            sigma = stats.sigma_profile(P, ins.dt, CFG["sigma_width"])
            thr_res = pool.map(_maxz, [(kind, s, sigma) for s in b.spawn(nb_thr)], chunksize=16)
            sc_res = pool.map(_maxz, [(kind, s, sigma) for s in c.spawn(nb_score)], chunksize=16) if nb_score else []
            iv = stats.order_stat_interval([r[0] for r in thr_res], CFG["alpha"], CFG["conf"])
            nulls[kind] = {"sigma": sigma, "null_max": np.array([r[0] for r in thr_res]), "iv": iv,
                           "score": [(r[1], r[2]) for r in sc_res], "score_max": np.array([r[0] for r in sc_res])}
            tim[f"null_{kind}"] = time.perf_counter() - t0
        sig, iv = nulls["shuffle"]["sigma"], nulls["shuffle"]["iv"]
        thr = iv["z_high"]
        t0 = time.perf_counter()
        a, b = s_syn.spawn(2)
        iso = [r for rows in pool.map(_synthetic, [(s, sig, thr, ins.W0, ins.fwhm, CFG["syn_lines"], (0.5 * thr, 4 * thr), None)
                                                   for s in a.spawn(CFG["syn_real"])]) for r in rows]
        seeds = b.spawn(CFG["syn_real"])
        pair = [r for k, sep in enumerate(CFG["pair_seps"]) for rows in pool.map(
            _synthetic, [(s, sig, thr, ins.W0, ins.fwhm, 6, (2 * thr, 4 * thr), sep) for s in seeds[k::len(CFG["pair_seps"])]]) for r in rows]
        tim["synthetic"] = time.perf_counter() - t0

        # ---- calibração sintética
        zt = np.array([r["z_true"] for r in iso])
        er = np.abs(np.array([r["err"] for r in iso]))
        rec = er[(er <= 0.5 * ins.fwhm) & (zt >= thr)]
        tol = min(float(np.quantile(rec, CFG["tol_quantile"])) if len(rec) else 0.5 * ins.fwhm, 0.5 * ins.fwhm)
        res_sep = None
        pair_curve = []
        for sep in CFG["pair_seps"]:
            rows = [r for r in pair if r["sep"] == sep]
            frac = float(np.mean([abs(r["err"]) <= tol for r in rows])) if rows else 0.0
            pair_curve.append((sep, len(rows), frac))
            if res_sep is None and rows and frac >= CFG["res_target"]:
                res_sep = sep
        res_sep = res_sep if res_sep is not None else max(CFG["pair_seps"])

        # ---- detecção nos zeros e gravação (antes da aritmética)
        peaks, zmax = stats.blind_peaks(ins.t, F, sig, 8, CFG["floor"])
        for p in peaks:
            p["class"] = stats.classify(p["z"], iv)
            p["z_gue"] = float(abs(F[p["i"]]) / nulls["gue"]["sigma"][p["i"]])
            p["class_gue"] = stats.classify(p["z_gue"], nulls["gue"]["iv"])
        np.savez_compressed(out / "arrays.npz", t=ins.t, F=F, smooth=ins.smooth, sigma=sig, null_max=nulls["shuffle"]["null_max"],
                            score_max=nulls["shuffle"]["score_max"], gue_sigma=nulls["gue"]["sigma"], gue_null_max=nulls["gue"]["null_max"])
        (out / "blind_peaks.json").write_text(json.dumps(peaks, indent=1))
        freeze = hashlib.sha256((out / "blind_peaks.json").read_bytes()).hexdigest()

        # ---- aritmética
        cat = stats.catalog(ins.t[0], ins.t[-1])
        T = np.array([c["T"] for c in cat])
        cc = np.array([c["c"] for c in cat])
        det = [p for p in peaks if p["class"] == "detected"]
        inc = [p for p in peaks if p["class"] == "inconclusive"]
        per = np.array([p["t"] for p in det])
        assign = stats.match_greedy(per, T, tol)
        assign_opt = stats.match_optimal(per, T, tol)
        S = len(assign)
        null_S = np.array([len(stats.match_greedy(pp[zz > thr], T, tol)) if len(pp) else 0 for pp, zz in nulls["shuffle"]["score"]])
        p_S = float((1 + np.sum(null_S >= S)) / (len(null_S) + 1))
        sep_nn = np.array([min(T[k] - T[k - 1] if k else np.inf, T[k + 1] - T[k] if k < len(T) - 1 else np.inf) for k in range(len(T))])
        resolved = sep_nn >= res_sep * ins.fwhm
        sigT = np.interp(T, ins.t, sig)
        z_pred = np.abs(cc) * ins.W0 / (2 * sigT)
        clear = z_pred >= CFG["clear_margin"] * thr
        detected = np.array([k in assign for k in range(len(T))])
        ev = lambda tt: ins.F_at(g, tt)  # noqa: E731
        half = 0.5 * ins.fwhm
        Cbc = stats.fit_band_conjugate(ev, T, ins.L, ins.Ec, half, sampling="band", conjugate=True)
        Cbn = stats.fit_band_conjugate(ev, T, ins.L, ins.Ec, half, sampling="band", conjugate=False)
        Ccc = stats.fit_band_conjugate(ev, T, ins.L, ins.Ec, half, sampling="centers", conjugate=True)
        ratio = np.real(Cbc) / cc
        elig = resolved & clear
        gi = np.clip(np.round((T - ins.t[0]) / ins.dt).astype(int), 0, ins.n_t - 1)
        R, Q = stats.phase_stats(F[gi][elig], T[elig], cc[elig], ins.Ec)
        prng = np.random.default_rng(s_phase)
        Qn = np.array([stats.phase_stats(np.abs(F[gi][elig]) * np.exp(1j * prng.uniform(0, 2 * math.pi, elig.sum())), T[elig], cc[elig], ins.Ec)[1]
                       for _ in range(CFG["phase_B"])])
        p_Q = float((1 + np.sum(Qn >= Q)) / (CFG["phase_B"] + 1))
        z_at_T = np.abs(F[gi]) / sig[gi]
        lines = []
        for k, c in enumerate(cat):
            pk = det[assign[k]] if k in assign else None
            near_inc = [p for p in inc if abs(p["t"] - T[k]) <= tol]
            lines.append({"p": c["p"], "r": c["r"], "T": T[k], "c": cc[k], "detected": bool(pk), "z_peak": pk["z"] if pk else None,
                          "t_peak": pk["t"] if pk else None, "inconclusive_near": bool(near_inc and not pk),
                          "z_inconclusive": near_inc[0]["z"] if near_inc and not pk else None, "z_grid_nearest_T": float(z_at_T[k]),
                          "z_pred": float(z_pred[k]), "clear": bool(clear[k]), "resolved": bool(resolved[k]),
                          "ratio_band_conjugate": float(ratio[k]), "ratio_band_no_conjugate": float(np.real(Cbn[k]) / cc[k]),
                          "ratio_centers_conjugate": float(np.real(Ccc[k]) / cc[k]), "C_imag_band_conjugate": float(np.imag(Cbc[k])),
                          "F_at_T": [float(v) for v in np.array([ev(np.array([T[k]]))[0]]).view(float)],
                          "matched_optimal": k in assign_opt})
        # ---- M2
        t0 = time.perf_counter()
        x = core.nbar(g)
        grid = np.linspace(0, 5, 1001)
        tau = np.linspace(0.02, 2.0, 100)
        obs = (spectral.spacing_cdf(x, grid), spectral.pair_correlation(x), spectral.form_factor_connected(x, tau))
        a, b = s_m2.spawn(2)
        ens = {"gue": pool.map(_m2_member, [("gue", len(g), s, grid, tau) for s in a.spawn(CFG["m2_gue"])], chunksize=4),
               "poisson": pool.map(_m2_member, [("poisson", len(g), s, grid, tau) for s in b.spawn(CFG["m2_poisson"])], chunksize=4)}
        m2 = {"spacing_variance": float(np.var(np.diff(x), ddof=1))}
        for ref, members in ens.items():
            for j, name in enumerate(("cdf", "r2", "k_connected")):
                m2[f"p_{ref}_{name}"] = spectral.symmetric_rank_p(obs[j], np.array([mm[j] for mm in members]))
            m2[f"{ref}_var_q025_q975"] = [float(v) for v in np.quantile([mm[3] for mm in members], [0.025, 0.975])]
        tim["m2"] = time.perf_counter() - t0
        # ---- CUE
        corr = spectral.CUECorrection()
        sg = np.linspace(0, 4, 161)
        pred = spectral.cue_prediction(corr, float(np.median(g)), sg)
        emp = spectral.spacing_cdf(x, sg)
        ens_cdf = np.array([np.interp(sg, grid, mm[0]) for mm in ens["gue"]])
        noise = float(np.median(np.sqrt(np.mean((ens_cdf - ens_cdf.mean(0)) ** 2, axis=1))))
        mu0 = np.trapezoid(sg * corr.p0(sg), sg)
        muc = np.trapezoid(sg * pred["pdf"], sg)
        cue = {"N_eff": pred["N_eff"], "alpha": pred["alpha"], "rms_limit": float(np.sqrt(np.mean((emp - corr.P0(sg)) ** 2))),
               "rms_corrected": float(np.sqrt(np.mean((emp - pred["cdf"]) ** 2))), "noise": noise,
               "var_limit": float(np.trapezoid(sg * sg * corr.p0(sg), sg) - mu0 ** 2),
               "var_corrected": float(np.trapezoid(sg * sg * pred["pdf"], sg) - muc ** 2)}
        np.savez_compressed(out / "m2_arrays.npz", grid=grid, tau=tau, cdf=obs[0], r2=obs[1], k=obs[2], cue_s=sg, cue_P0=corr.P0(sg),
                            cue_P1=corr.P1(sg), cue_pred_cdf=pred["cdf"], smooth=ins.smooth)

    rec_clear = float(detected[clear].mean()) if clear.any() else None
    frac_c2 = float(np.mean(np.abs(ratio[elig] - 1) <= CFG["ratio_tol"])) if elig.any() else None
    summary = {
        "label": label, "indices": [i0, i1], "A": ins.A, "B": ins.B, "L": ins.L, "fwhm": ins.fwhm, "dt": ins.dt, "n_t": ins.n_t, "W0": ins.W0,
        "seed": seed, "cfg": CFG, "freeze_sha256": freeze,
        "shuffle_interval": nulls["shuffle"]["iv"], "gue_interval": nulls["gue"]["iv"],
        "score_fraction_above": float(np.mean(nulls["shuffle"]["score_max"] > thr)),
        "tolerance": tol, "tolerance_fwhm": tol / ins.fwhm, "resolution_sep_fwhm": res_sep, "pair_curve": pair_curve,
        "n_synthetic_isolated": len(iso),
        "n_detected": len(det), "n_inconclusive": len(inc), "n_detected_gue": sum(p["class_gue"] == "detected" for p in peaks),
        "S": S, "S_optimal": len(assign_opt), "unmatched": len(det) - S, "p_S": p_S,
        "clear": int(clear.sum()), "recovery_clear": rec_clear, "eligible": int(elig.sum()), "C2_fraction": frac_c2,
        "C2_max": float(np.max(np.abs(ratio[elig] - 1))) if elig.any() else None, "R": R, "Q": Q, "p_Q": p_Q,
        "C1_block": bool(rec_clear is not None and rec_clear >= 0.95), "C2_block": bool(frac_c2 is not None and frac_c2 >= 0.95 and Q >= 0.9),
        "m2": m2, "cue": cue, "timings": tim, "total_seconds": time.perf_counter() - t_start,
    }
    (out / "lines.json").write_text(json.dumps(lines, indent=1))
    (out / "summary.json").write_text(json.dumps(summary, indent=1, default=float))
    return summary
