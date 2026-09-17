"""Auditoria de leitura: não modifica código, protocolo nem execuções anteriores.

Executar na raiz: .venv/bin/python results/audit_20260913_resultados/run_audit.py
"""
import csv
import hashlib
import json
import math
import platform
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
RUN = ROOT / "results/run_20260913_024706_m3_holdout-full"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def read_csv(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def independent_transform(g, frequencies):
    """Soma explícita; integral suave por QUADPACK oscilatória (não usa periods.py)."""
    A, B = float(g[0]), float(g[-1])
    L, center = B - A, (A + B) / 2
    u = g - center
    weights = (1 + np.cos(2 * np.pi * u / L)) / 2

    def amplitude(v):
        return (1 + math.cos(2 * math.pi * v / L)) / 2 * math.log((v + center) / (2 * math.pi)) / (2 * math.pi)

    values, quadrature_errors = [], []
    for t in frequencies:
        cosine, ce = quad(amplitude, -L / 2, L / 2, weight="cos", wvar=t, epsabs=1e-9, epsrel=1e-10, limit=300)
        sine, se = quad(amplitude, -L / 2, L / 2, weight="sin", wvar=t, epsabs=1e-9, epsrel=1e-10, limit=300)
        discrete = np.sum(weights * np.exp(-1j * u * t))
        values.append(discrete - cosine + 1j * sine)
        quadrature_errors.append(ce + se)
    return np.array(values), max(quadrature_errors)


def independent_fit(g, frequencies):
    """Coeficientes livres: 47 equações complexas, incluindo lóbulos +/-T.

    Os valores teóricos das amplitudes não entram no ajuste.
    """
    L, center = g[-1] - g[0], (g[-1] + g[0]) / 2

    def response(delta):
        q = delta * L / (2 * np.pi)
        return L * (np.sinc(q) / 2 + (np.sinc(q - 1) + np.sinc(q + 1)) / 4)

    F, quad_error = independent_transform(g, frequencies)
    positive = response(frequencies[:, None] - frequencies[None, :]) * np.exp(1j * center * frequencies)
    negative = response(frequencies[:, None] + frequencies[None, :]) * np.exp(-1j * center * frequencies)
    D = np.column_stack(((positive + negative) / 2, 1j * (positive - negative) / 2))
    M = np.vstack((D.real, D.imag))
    coefficients = np.linalg.solve(M, np.concatenate((F.real, F.imag)))
    n = len(frequencies)
    return coefficients[:n] + 1j * coefficients[n:], quad_error, float(np.linalg.cond(M))


def independent_fit_original_sampling(g, frequencies):
    """Mesma amostragem/estimador do relatório, com soma e quadratura independentes."""
    L, center = g[-1] - g[0], (g[-1] + g[0]) / 2
    half_width = 2 * np.pi / L
    points = np.unique(np.concatenate([np.linspace(t - half_width, t + half_width, 9) for t in frequencies]))
    F, qe = independent_transform(g, points)
    v = (points[:, None] - frequencies[None, :]) * L / (2 * np.pi)
    matrix = L * (np.sinc(v) / 2 + (np.sinc(v - 1) + np.sinc(v + 1)) / 4)
    coef, *_ = np.linalg.lstsq(matrix, F, rcond=None)
    return 2 * coef * np.exp(-1j * center * frequencies), qe


def main():
    started = time.perf_counter()
    # Ler apenas os primeiros 10.000 valores; a nova faixa permanece sem análise.
    raw = np.loadtxt(ROOT / "data/raw/zeros1", max_rows=10000)
    csv_zeros = np.array([float(r["gamma_n"]) for r in read_csv(ROOT / "data/processed/zeros_10k.csv")])
    data_manifest = read_json(ROOT / "data/raw/data_manifest.json")
    lock = read_json(ROOT / "configs/m3_protocol.lock.json")
    checks = {
        "raw_processed_equal_first_10000": bool(np.array_equal(raw, csv_zeros)),
        "n_zeros_reviewed": len(raw),
        "gamma_range": [float(raw[0]), float(raw[-1])],
        "strict_order": bool(np.all(np.diff(raw) > 0)),
        "raw_hash_matches": sha(ROOT / data_manifest["raw_file"]["path"]) == data_manifest["raw_file"]["sha256"],
        "processed_hash_matches": sha(ROOT / data_manifest["processed_file"]["path"]) == data_manifest["processed_file"]["sha256"],
        "protocol_config_hash_matches": sha(ROOT / "configs/m3_protocol.toml") == lock["config_sha256"],
        "protocol_modules_hash_match": {f: sha(ROOT / "src/riemann_spectra" / f) == h for f, h in lock["modules_sha256"].items()},
    }
    results = {"integrity": checks, "blocks": {}}
    rows_out = []
    for block, start in (("holdout", 7000), ("full", 0)):
        g = raw[start:]
        folder = RUN / "tables" / block
        rows = read_csv(folder / "arithmetic_matches.csv")
        T = np.array([float(r["period_theoretical"]) for r in rows])
        C, qe, cond = independent_fit(g, T)
        theory = np.array([float(r["coefficient_theoretical"]) for r in rows])
        original = np.array([complex(float(r["fit_coefficient_real"]), float(r["fit_coefficient_imag"])) for r in rows])
        selected = np.array([r["resolved"] == "True" and r["predicted_detectable"] == "True" for r in rows])
        original_sampling, original_sampling_qe = independent_fit_original_sampling(g, T)
        detected = [r for r in rows if r["detected"] == "True"]
        freeze = read_json(folder / "freeze.json")
        x = g / (2 * np.pi) * (np.log(g / (2 * np.pi)) - 1) + 7 / 8
        results["blocks"][block] = {
            "blind_hash_matches": sha(folder / "blind_peaks.csv") == freeze["blind_peaks_sha256"],
            "nulls_hash_matches": sha(folder / "nulls.npz") == freeze["nulls_npz_sha256"],
            "catalog_lines": len(rows),
            "detected_lines": len(detected),
            "max_detection_period_error": max(float(r["absolute_error"]) for r in detected),
            "median_detection_period_error": float(np.median([float(r["absolute_error"]) for r in detected])),
            "independent_spacing_mean": float(np.mean(np.diff(x))),
            "independent_spacing_variance": float(np.var(np.diff(x), ddof=1)),
            "independent_fit_median_abs_ratio_minus_one_selected": float(np.median(np.abs((C.real / theory - 1)[selected]))),
            "independent_fit_max_abs_ratio_minus_one_all": float(np.max(np.abs(C.real / theory - 1))),
            "independent_fit_max_abs_coefficient_difference_from_saved": float(np.max(np.abs(C - original))),
            "independent_fit_condition_number": cond,
            "quadpack_max_reported_abs_error": qe,
            "same_sampling_fit_median_abs_ratio_minus_one_selected": float(np.median(np.abs((original_sampling.real / theory - 1)[selected]))),
            "same_sampling_fit_max_coefficient_difference_from_saved": float(np.max(np.abs(original_sampling - original))),
            "same_sampling_quadpack_max_reported_abs_error": original_sampling_qe,
        }
        for i, r in enumerate(rows):
            rows_out.append({"block": block, "prime": r["prime"], "repetition": r["repetition"],
                             "period": T[i], "C_real": C[i].real, "C_imag": C[i].imag,
                             "theory": theory[i], "ratio_error": C[i].real / theory[i] - 1,
                             "difference_from_saved": abs(C[i] - original[i]),
                             "same_sampling_C_real": original_sampling[i].real,
                             "same_sampling_C_imag": original_sampling[i].imag,
                             "same_sampling_difference_from_saved": abs(original_sampling[i] - original[i])})
        print(block, json.dumps(results["blocks"][block]), flush=True)

    # Reprodução mínima da diferença no refinamento: o mesmo sinal em ambas as rotas.
    from riemann_spectra.periods import detect_blind_peaks, hann_response, max_statistic
    L = 3000.0
    fwhm = 4 * np.pi / L
    dt = fwhm / 8
    ts = 0.5 + np.arange(3000) * dt
    center = ts[1500] + 0.49 * dt

    def signal(t):
        return 4.0 * hann_response(t - center, L) / (L / 2) + 0j

    F = signal(ts)
    sigma = np.ones_like(ts)
    null_peak = detect_blind_peaks(ts, F, fwhm, sigma)[0]
    obs_peak = detect_blind_peaks(ts, F, fwhm, sigma, evaluator=signal)[0]
    results["refinement_counterexample"] = {
        "description": "Mesmo sinal Hann: rota dos zeros usa evaluator, rota dos nulos usa valor da malha.",
        "null_route_z": null_peak["z"],
        "observed_route_z": obs_peak["z"],
        "null_max_grid": max_statistic(F, sigma),
        "relative_increase": obs_peak["z"] / null_peak["z"] - 1,
    }

    # Reproduzir cinco máximos shuffle salvos e medir o efeito do refinamento no mesmo nulo.
    from riemann_spectra.controls import shuffled_energy_levels_like
    from riemann_spectra.periods import OscillatoryTransform
    saved = np.load(RUN / "tables/holdout/nulls.npz")
    tr = OscillatoryTransform(raw[7000], raw[-1], 0.5, 5.0)
    root = np.random.SeedSequence(20260912)
    child = root.spawn(5)[3].spawn(3)[0]
    seeds = child.spawn(1199)[200:205]
    comparisons = []
    for i, seed in enumerate(seeds):
        levels = shuffled_energy_levels_like(raw[7000:], np.random.default_rng(seed))
        F = tr.transform(levels)
        coarse = max_statistic(F, saved["shuffle_sigma"])
        refined = detect_blind_peaks(tr.t_grid, F, tr.response["fwhm"], saved["shuffle_sigma"],
                                    candidate_z=0, evaluator=lambda t: tr.evaluate(levels, t))
        ref_max = max(p["z"] for p in refined)
        comparisons.append({"replicate": i, "saved_max": float(saved["shuffle_null_max"][i]),
                            "recomputed_grid_max": coarse, "refined_max": ref_max,
                            "relative_refinement_increase": ref_max / coarse - 1})
    results["null_reproduction_first_five_holdout_shuffle"] = comparisons

    with open(OUT / "coefficients_independent.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows_out[0]))
        writer.writeheader()
        writer.writerows(rows_out)
    (OUT / "metrics.json").write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n")
    manifest = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "command": ".venv/bin/python results/audit_20260913_resultados/run_audit.py",
        "duration_seconds": time.perf_counter() - started,
        "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
        "audit_script_sha256": sha(__file__),
        "input_processed_sha256": sha(ROOT / "data/processed/zeros_10k.csv"),
        "scope": "Auditoria limitada dos primeiros 10.000 zeros; não é nova execução completa de M2/M3.",
        "code_sha256": {p.name: sha(p) for p in sorted((ROOT / "src/riemann_spectra").glob("*.py"))},
        "artifacts_sha256": {name: sha(OUT / name) for name in ("metrics.json", "coefficients_independent.csv")},
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(results["refinement_counterexample"]), flush=True)
    print(json.dumps(comparisons), flush=True)
    print("Completed in", manifest["duration_seconds"], "seconds", flush=True)


if __name__ == "__main__":
    main()
