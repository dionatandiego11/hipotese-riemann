"""
Extrapolação do orçamento do instrumento `ctrl-dirichlet-v1` a partir das medições sintéticas de
`bench_instrumento_chi.py`. Ajuste linear por etapa no número de realizações; nenhum dado real é usado.

  .venv/bin/python3 results/etapa11_6_controles/dirichlet/orcamento/extrapola_orcamento.py bench_*.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

DECL = {"shuffle": 200 + 9999 + 9999, "gue": 100 + 199, "synthetic": 40, "phase": 999, "precision": 20}


def counts(r):
    u = r["realizacoes_usadas"]
    return {"shuffle": u["shuffle_sigma_realizations"] + u["shuffle_threshold_realizations"] + u["shuffle_score_realizations"],
            "gue": u["gue_sigma_realizations"] + u["gue_threshold_realizations"] + u["gue_score_realizations"],
            "synthetic": u["synthetic_realizations"], "phase": u["phase_control_realizations"],
            "precision": u["precision_perturbations"]}


def fit(x, y, names):
    """Mínimos quadrados com intercepto; devolve (intercepto, coeficientes)."""
    A = np.column_stack([np.ones(len(y))] + [np.asarray(c, dtype=float) for c in x])
    beta, *_ = np.linalg.lstsq(A, np.asarray(y, dtype=float), rcond=None)
    res = np.asarray(y) - A @ beta
    return beta, float(np.sqrt(np.mean(res ** 2))), names


def main(paths):
    rows = [json.loads(Path(p).read_text(encoding="utf-8")) for p in paths]
    rows = [r for r in rows if r["bloco"] == "e02"]
    rows.sort(key=lambda r: r["escala"])
    c = [counts(r) for r in rows]
    t = {k: [r["segundos_por_etapa"][k] for r in rows] for k in rows[0]["segundos_por_etapa"]}
    out = {"pontos": [{"escala": r["escala"], "realizacoes": counts(r), "segundos": r["segundos_por_etapa"]} for r in rows]}
    est = {}
    # etapas com uma variável só
    for stage, key in (("null_shuffle", "shuffle"), ("null_gue", "gue"), ("synthetic", "synthetic")):
        b, rms, _ = fit([[x[key] for x in c]], t[stage], [key])
        est[stage] = {"intercepto_s": b[0], "s_por_realizacao": b[1], "rms_ajuste_s": rms,
                      "realizacoes_declaradas": DECL[key], "segundos_por_bloco": b[0] + b[1] * DECL[key]}
    # aritmética: base + fase + precisão
    b, rms, _ = fit([[x["phase"] for x in c], [x["precision"] for x in c]], t["arithmetic"], ["phase", "precision"])
    est["arithmetic"] = {"intercepto_s": b[0], "s_por_fase": b[1], "s_por_perturbacao": b[2], "rms_ajuste_s": rms,
                         "segundos_por_bloco": b[0] + b[1] * DECL["phase"] + b[2] * DECL["precision"]}
    est["instrument"] = {"segundos_por_bloco": float(np.mean(t["instrument"])),
                         "nota": "custo fixo, independente das realizações"}
    total = sum(v["segundos_por_bloco"] for v in est.values())
    out["por_etapa"] = est
    out["bloco"] = {"segundos": total, "minutos": total / 60}
    out["oito_blocos"] = {"horas_cpu": 8 * total / 3600,
                          "parede_h_1_processo": 8 * total / 3600,
                          "parede_h_4_processos": 8 * total / 3600 / 4}
    out["h004_somente"] = {"etapas": ["instrument", "arithmetic"],
                           "segundos_por_bloco": est["instrument"]["segundos_por_bloco"] + est["arithmetic"]["segundos_por_bloco"],
                           "horas_cpu_6_blocos": 6 * (est["instrument"]["segundos_por_bloco"] + est["arithmetic"]["segundos_por_bloco"]) / 3600}
    print(json.dumps(out, indent=2, ensure_ascii=False))
    Path(__file__).with_name("orcamento_extrapolado.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
