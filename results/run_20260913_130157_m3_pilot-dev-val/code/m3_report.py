"""
riemann_spectra.m3_report
Relatório do M3 gerado exclusivamente a partir dos artefatos gravados de cada bloco.
"""

import csv
import json
import logging
from pathlib import Path
from typing import Any, Dict

from riemann_spectra.reporting import plot_m3_coefficients, plot_m3_recovery, plot_m3_spectrum

logger = logging.getLogger("riemann_spectra.m3_report")


def _fmt(x, nd=3):
    if x is None:
        return "—"
    if isinstance(x, float):
        if x != 0 and (abs(x) < 1e-3 or abs(x) >= 1e5):
            return f"{x:.{nd}e}"
        return f"{x:.{nd}f}"
    return str(x)


def _read_rows(path: Path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out = {}
            for k, v in r.items():
                if v in ("True", "False"):
                    out[k] = v == "True"
                else:
                    try:
                        out[k] = float(v) if v != "" else None
                    except ValueError:
                        out[k] = v
            out["prime"] = int(out["prime"])
            out["repetition"] = int(out["repetition"])
            rows.append(out)
    return rows


def write_m3_run_report(run_dir: Path, manifest: Dict[str, Any], results: Dict[str, Dict[str, Any]]) -> None:
    tables = run_dir / "tables"
    summary_rows = []
    block_sections = []
    for name, res in results.items():
        bdir = tables / name
        rows = _read_rows(bdir / "arithmetic_matches.csv")
        title = f"bloco {name} (zeros {res['block']['first_index']}–{res['block']['last_index']})"
        figs = [
            plot_m3_spectrum(bdir, rows, title),
            plot_m3_coefficients(bdir, rows, title),
            plot_m3_recovery(bdir, res["synthetic_calibration"], title),
        ]
        ar = res["arithmetic"]
        tf = ar["targeted_fit"]
        prim = tf["primary_estimator"]
        vsum = tf["variants"]
        ps = ar["precision_sensitivity"]
        ph = ar["phase_coherence"]
        ns = res["null_summary"]
        inst = res["instrument"]
        diag = res["instrument_diagnostics"]
        cal = res["synthetic_calibration"]
        sel = vsum[prim]["resolved_and_detectable"]
        summary_rows.append({
            "block": name,
            "indices": f"{res['block']['first_index']}–{res['block']['last_index']}",
            "L": inst["L"],
            "fwhm": inst["response"]["fwhm"],
            "catalog": ar["catalog_size"],
            "detectable": ar["predicted_detectable"],
            "detected": ar["detected_peaks_primary"],
            "matched": ar["matched_S"],
            "unmatched": ar["unmatched_detections"],
            "null_S_max": ar["null_S_max"],
            "p": ar["p_value_global_mc"],
            "recovery": ar["recovery_among_predicted_detectable"],
            "refined_flip": res["freeze"]["n_candidates_whose_decision_would_change_with_refined_z"],
            "ratio_dev": {v: vsum[v]["resolved_and_detectable"].get("median_abs_ratio_minus_1") for v in vsum},
            "pert": ps["median_abs_ratio_change_selected_lines"],
        })
        missed = ", ".join(f"{p}^{r}" if r > 1 else str(p) for p, r in ar["missed_predicted_detectable"]) or "nenhuma"
        n_undet = sum(1 for r in rows if not r["detected"])
        variant_lines = "\n".join(
            f"| Ajuste direcionado `{v}`{' (primário)' if v == prim else ''}: mediana / máx. |razão−1| (n={d['resolved_and_detectable'].get('n_lines')}); todas as {ar['catalog_size']} linhas | "
            f"{_fmt(d['resolved_and_detectable'].get('median_abs_ratio_minus_1'))} / {_fmt(d['resolved_and_detectable'].get('max_abs_ratio_minus_1'))}; "
            f"{_fmt(d['all_catalog_lines'].get('median_abs_ratio_minus_1'))} / {_fmt(d['all_catalog_lines'].get('max_abs_ratio_minus_1'))} |"
            for v, d in vsum.items()
        )
        section = f"""### {title}

Protocolo `{res.get('protocol_version')}`. `blind_peaks.csv` SHA-256 `{res['freeze']['blind_peaks_sha256']}` gravado antes do módulo aritmético.
Estatística de decisão: {res['freeze']['decision_statistic']}.

| Grandeza | Valor |
|---|---|
| Janela / densidade média | {inst['window']} / {inst['density']} |
| Intervalo [A, B] | [{_fmt(inst['A'])}, {_fmt(inst['B'])}], L = {_fmt(inst['L'], 1)} |
| FWHM medida | {_fmt(inst['response']['fwhm'])} ({_fmt(inst['response']['fwhm_in_units_2pi_over_L'], 3)} × 2π/L); lóbulo lateral {_fmt(inst['response']['sidelobe_level_db'], 1)} dB |
| Malha | {diag['n_t']} pontos, {_fmt(diag['points_per_fwhm'], 1)} por FWHM |
| NUFFT vs soma direta (máx. abs.) | {_fmt(diag['nufft_vs_direct_max_abs_error'])} (máx. |F| = {_fmt(diag['max_abs_F'], 1)}) |
| Quadratura: mudança ao reduzir painel pela metade | {_fmt(diag['quadrature_halving_max_abs_change'])} |
| Termo suave: densidade rvm vs θ (máx. abs.) | {_fmt(diag['density_rvm_vs_theta_max_abs_change'])} |
| Nulo shuffle: B σ / limiar / escore | {ns['shuffle']['B_sigma']} / {ns['shuffle']['B_threshold']} / {ns['shuffle']['B_score']}; limiar z = {_fmt(ns['shuffle']['threshold_z'], 4)} |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | {_fmt(ns['shuffle']['score_set_fraction_max_above_threshold'])} |
| Nulo GUE: B σ / limiar | {ns['gue']['B_sigma']} / {ns['gue']['B_threshold']}; limiar z = {_fmt(ns['gue']['threshold_z'], 4)} |
| Candidatos cuja decisão mudaria usando z refinado | {res['freeze']['n_candidates_whose_decision_would_change_with_refined_z']} |
| Tolerância de matching (quantil {cal['matching_tolerance_quantile']}) | {_fmt(cal['matching_tolerance'])} = {_fmt(cal['matching_tolerance_fwhm'])} FWHM |
| Separação de pares com ≥90% recuperado | {_fmt(cal['resolution_separation_fwhm'], 2)} FWHM ({cal['resolution_separation_status']}) |
| Linhas sintéticas isoladas | {cal['n_isolated_lines']} |
| Detecções (nulo primário / secundário) | {res['freeze']['n_detected_primary']} / {res['freeze']['n_detected_secondary']} |
| Catálogo r log p | {ar['catalog_size']} ({ar['catalog_primitive']} primitivas, {ar['catalog_repetitions']} repetições); {ar['catalog_resolved']} resolvidas |
| Previstas detectáveis | {ar['predicted_detectable']} |
| Escore S; nulo (conjunto independente, B={ar['B_score']}) | {ar['matched_S']}; média {_fmt(ar['null_S_mean'])}, máx. {ar['null_S_max']} |
| Detecções sem correspondente; detecções por realização nula | {ar['unmatched_detections']}; {_fmt(ar['null_detections_mean'])} |
| p Monte Carlo global | {_fmt(ar['p_value_global_mc'])} (resolução {_fmt(ar['p_value_floor'])}) |
| Recuperação entre previstas detectáveis | {_fmt(ar['recovery_among_predicted_detectable'])}; detectáveis perdidas: {missed} |
| Detectadas embora previstas indetectáveis | {ar['detected_but_predicted_undetectable']} |
{variant_lines}
| Maior diferença entre variantes (razão, linhas selecionadas) | {_fmt(tf['max_abs_difference_between_variants_ratio_selected'])} |
| Sensibilidade ±{ps['perturbation_half_width']:.0e} (estimador primário): mediana / máx. |Δ razão| | {_fmt(ps['median_abs_ratio_change_selected_lines'])} / {_fmt(ps['max_abs_ratio_change_selected_lines'])} |
| Alinhamento de fase R (invariante a rotação comum) | {_fmt(ph.get('R_observed'))}; nulo q95 {_fmt(ph.get('R_null_q95'))}; p = {_fmt(ph.get('p_value_R'))} |
| Sinal absoluto Q = média cos(erro de fase) | {_fmt(ph.get('Q_observed'))}; nulo q95 {_fmt(ph.get('Q_null_q95'))}; p = {_fmt(ph.get('p_value_Q'))} |
| Linhas não detectadas | {n_undet} |
| Tempo (s) | {', '.join(f'{k}: {v:.1f}' for k, v in res['timings_seconds'].items())} |

Figuras: {', '.join(f'`tables/{name}/{f.name}`' for f in figs)}.
"""
        block_sections.append(section)

    metrics = {"blocks": {k: {kk: vv for kk, vv in v.items()} for k, v in results.items()}, "summary": summary_rows}
    with open(run_dir / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False, default=str)
    with open(run_dir / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False, default=str)

    vnames = list(summary_rows[0]["ratio_dev"].keys()) if summary_rows else []
    header = ("| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | Decisões alteráveis por z refinado | "
              + " | ".join(f"mediana abs(razão−1) `{v}`" for v in vnames) + " | Δ perturbação |\n|" + "---|" * (14 + len(vnames)))
    lines = [header]
    for r in summary_rows:
        lines.append(
            f"| {r['block']} | {r['indices']} | {_fmt(r['L'], 0)} | {_fmt(r['fwhm'])} | {r['catalog']} | {r['detectable']} | {r['detected']} | {r['matched']} | "
            f"{r['unmatched']} | {r['null_S_max']} | {_fmt(r['p'])} | {_fmt(r['recovery'])} | {r['refined_flip']} | "
            + " | ".join(_fmt(r['ratio_dev'][v]) for v in vnames) + f" | {_fmt(r['pert'])} |"
        )
    lock = manifest.get("protocol_lock")
    lock_txt = (f"Protocolo congelado em {lock['frozen_at_utc']} (config `{lock['config_sha256'][:16]}…`, módulos `{lock['combined_sha256'][:16]}…`)."
                if lock else "Execução sem blocos reservados; congelamento não exigido.")
    report = f"""# Relatório M3 — espectroscopia inversa por blocos

**ID:** `{run_dir.name}`
**Blocos:** {', '.join(results.keys())}
**Duração:** {manifest['performance']['duration_seconds']:.1f} s; pico de memória {manifest['performance']['peak_memory_mb']:.0f} MB
**Comando:** `{manifest['command']}`

{lock_txt}

## Resumo por bloco

{chr(10).join(lines)}

Definições: *Detecções* são máximos locais de z = |F|/σ_nulo, avaliado na malha para zeros, controles e sintéticos,
acima do limiar FWER do nulo de permutação de espaçamentos, obtidos sem catálogo. O limiar e o escore global usam
conjuntos nulos independentes. *S* conta linhas r log p com uma detecção a menos da tolerância calibrada (um a um).
*p* compara S com a mesma cadeia aplicada a cada realização nula. *Recuperação* é a fração das linhas cujo
coeficiente de referência excede o limite de detecção previsto pelo nulo. As colunas de razão e fase vêm da
**medição direcionada** nos períodos conhecidos (ajuste conjunto com a resposta da janela), que não é detecção cega.

## Interpretação e limites

- A análise mede a transformada de uma janela finita de zeros e compara com a referência −log p/(π p^{{r/2}}).
  A concordância é um resultado numérico (categoria B). A justificativa exata da observável finita pela fórmula
  explícita — classe de funções-teste, termos e erros — ainda não foi estabelecida no projeto.
  A concordância não demonstra RH nem identifica um Hamiltoniano.
- O "fundo" entre linhas nos zeros não é ruído estatístico: é vazamento determinístico de outras linhas pelos lóbulos
  laterais da janela. A escala de ruído usada para decidir detecções vem, portanto, dos controles nulos.
- Linhas abaixo do limite de detecção do nulo não são evidência de ausência; ver colunas de detectabilidade prevista.
- Os valores-p são limitados inferiormente por 1/(B+1) e medem incompatibilidade com o nulo declarado.

## Detalhes por bloco

{chr(10).join(block_sections)}
"""
    with open(run_dir / "report.md", "w", encoding="utf-8") as f:
        f.write(report)
    logger.info(f"Relatório M3 salvo em {run_dir / 'report.md'}")
