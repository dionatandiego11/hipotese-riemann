"""Compara as duas rotas do detector usando apenas artefatos já salvos.

Executar na raiz: .venv/bin/python results/audit_20260913_resultados/check_detection_routes.py
Não é recalibração completa dos nulos.
"""
import csv
import hashlib
import json
from pathlib import Path

import numpy as np

from riemann_spectra.periods import detect_blind_peaks

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
RUN = ROOT / "results/run_20260913_024706_m3_holdout-full/tables"

result = {}
for block in ("holdout", "full"):
    folder = RUN / block
    metrics = json.loads((folder / "block_metrics.json").read_text())
    arrays = np.load(folder / "nulls.npz")
    F = arrays["F_real"] + 1j * arrays["F_imag"]
    peaks = detect_blind_peaks(
        arrays["t_grid"], F, metrics["instrument"]["response"]["fwhm"],
        arrays["shuffle_sigma"], candidate_z=3,
    )
    threshold = metrics["null_summary"]["shuffle"]["threshold_z"]
    changed = []
    with open(folder / "arithmetic_matches.csv") as f:
        for row in csv.DictReader(f):
            if row["detected"] != "True":
                continue
            peak = min(peaks, key=lambda p: abs(p["period"] - float(row["period_observed"])))
            if peak["z"] < threshold:
                changed.append({
                    "prime": int(row["prime"]), "repetition": int(row["repetition"]),
                    "period": float(row["period_theoretical"]),
                    "grid_route_z": peak["z"], "refined_route_z": float(row["z_primary"]),
                    "threshold": threshold, "original_adjusted_p": float(row["p_adjusted"]),
                })
    result[block] = {
        "grid_route_detections": sum(p["z"] >= threshold for p in peaks),
        "recorded_refined_route_detections": metrics["freeze"]["n_detected_primary"],
        "detections_changed": changed,
        "N_eff_at_energy_center_using_2006_formula": float(
            np.log(metrics["instrument"]["E_c"] / (2 * np.pi)) / np.sqrt(12 * 1.57314)
        ),
        "input_nulls_sha256": hashlib.sha256((folder / "nulls.npz").read_bytes()).hexdigest(),
    }
record = {
    "command": ".venv/bin/python results/audit_20260913_resultados/check_detection_routes.py",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "note": "Diagnóstico com limiar salvo; não fornece valores-p recalibrados.",
    "results": result,
}
(OUT / "detection_routes.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(record, indent=2, ensure_ascii=False))
