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
        ps = ar["precision_sensitivity"]
        ph = ar["phase_coherence"]
        ns = res["null_summary"]
        inst = res["instrument"]
        diag = res["instrument_diagnostics"]
        cal = res["synthetic_calibration"]
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
            "ratio_dev": ps["median_abs_ratio_deviation_observed"],
            "pert": ps["median_abs_ratio_change_selected_lines"],
            "phase_err": tf["abs_phase_error_median_rad"],
        })
        missed = ", ".join(f"{p}^{r}" if r > 1 else str(p) for p, r in ar["missed_predicted_detectable"]) or "nenhuma"
        undetected_primes = sorted({(r["prime"], r["repetition"]) for r in rows if not r["detected"]})
        section = f"""### {title}

Protocolo de detecção cega: `blind_peaks.csv` SHA-256 `{res['freeze']['blind_peaks_sha256']}` gravado antes do módulo aritmético.

| Grandeza | Valor |
|---|---|
| Janela [A, B] | [{_fmt(inst['A'])}, {_fmt(inst['B'])}], L = {_fmt(inst['L'], 1)} |
| FWHM medida da janela de Hann | {_fmt(inst['response']['fwhm'])} ({_fmt(inst['response']['fwhm_in_units_2pi_over_L'], 3)} × 2π/L); lóbulo lateral {_fmt(inst['response']['sidelobe_level_db'], 1)} dB |
| Malha | {diag['n_t']} pontos, {_fmt(diag['points_per_fwhm'], 1)} por FWHM |
| NUFFT vs soma direta (máx. abs.) | {_fmt(diag['nufft_vs_direct_max_abs_error'])} (máx. |F| = {_fmt(diag['max_abs_F'], 1)}) |
| Quadratura: mudança ao reduzir painel pela metade | {_fmt(diag['quadrature_halving_max_abs_change'])} |
| Densidade média rvm vs θ (máx. abs.) | {_fmt(diag['density_rvm_vs_theta_max_abs_change'])} |
| Limiar FWER z (shuffle, B={ns['shuffle']['B_max']}) | {_fmt(ns['shuffle']['threshold_z'])} |
| Limiar FWER z (GUE, B={ns['gue']['B_max']}) | {_fmt(ns['gue']['threshold_z'])} |
| Mediana de |F|/σ nos zeros (toda a malha) | {_fmt(res['zeros_background']['median_abs_F_over_sigma_primary'])} |
| Tolerância de matching (quantil {cal['matching_tolerance_quantile']} do erro sintético) | {_fmt(cal['matching_tolerance'])} = {_fmt(cal['matching_tolerance_fwhm'])} FWHM |
| Separação para recuperar ≥90% das linhas de pares | {_fmt(cal['resolution_separation_fwhm'], 2)} FWHM |
| Linhas sintéticas isoladas usadas | {cal['n_isolated_lines']} |
| Detecções cegas (nulo primário / secundário) | {res['freeze']['n_detected_primary']} / {res['freeze']['n_detected_secondary']} |
| Catálogo r log p em [t_min, t_max] | {ar['catalog_size']} ({ar['catalog_primitive']} primitivas, {ar['catalog_repetitions']} repetições); {ar['catalog_resolved']} resolvidas |
| Linhas previstas detectáveis (|c| L/4 ≥ z σ) | {ar['predicted_detectable']} |
| Escore S (linhas com detecção correspondente) | {ar['matched_S']}; nulo: média {_fmt(ar['null_S_mean'])}, máx. {ar['null_S_max']} |
| Detecções sem correspondente no catálogo | {ar['unmatched_detections']} (detecções por realização nula: {_fmt(ar['null_detections_mean'])}) |
| p Monte Carlo global (B={ar['B_null']}) | {_fmt(ar['p_value_global_mc'])} (piso {_fmt(ar['p_value_floor'])}) |
| Recuperação entre previstas detectáveis | {_fmt(ar['recovery_among_predicted_detectable'])}; detectáveis perdidas: {missed} |
| Detectadas embora previstas indetectáveis | {ar['detected_but_predicted_undetectable']} |
| Ajuste direcionado: mediana |razão − 1| (resolvidas e detectáveis, n={tf['lines_resolved_and_detectable']}) | {_fmt(ps['median_abs_ratio_deviation_observed'])} |
| Ajuste direcionado: mediana |erro de fase| | {_fmt(tf['abs_phase_error_median_rad'])} rad |
| Sensibilidade: mediana |Δ razão| com zeros perturbados ±{ps['perturbation_half_width']:.0e} | {_fmt(ps['median_abs_ratio_change_selected_lines'])} |
| Coerência de fase R (controle de fase, B={ph.get('B')}) | {_fmt(ph.get('R_observed'))}; nulo q95 {_fmt(ph.get('R_null_q95'))}; p = {_fmt(ph.get('p_value_mc'))} |
| Linhas não detectadas | {len(undetected_primes)} |
| Tempo (s) | {', '.join(f'{k}: {v:.1f}' for k, v in res['timings_seconds'].items())} |

Figuras: {', '.join(f'`tables/{name}/{f.name}`' for f in figs)}.
"""
        block_sections.append(section)

    metrics = {"blocks": {k: {kk: vv for kk, vv in v.items()} for k, v in results.items()}, "summary": summary_rows}
    with open(run_dir / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False, default=str)
    with open(run_dir / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False, default=str)

    header = "| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | mediana |razão−1| | Δ perturbação | |fase| |\n|" + "---|" * 15
    lines = [header]
    for r in summary_rows:
        lines.append(
            f"| {r['block']} | {r['indices']} | {_fmt(r['L'], 0)} | {_fmt(r['fwhm'])} | {r['catalog']} | {r['detectable']} | {r['detected']} | {r['matched']} | {r['unmatched']} | {r['null_S_max']} | {_fmt(r['p'])} | {_fmt(r['recovery'])} | {_fmt(r['ratio_dev'])} | {_fmt(r['pert'])} | {_fmt(r['phase_err'])} |"
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

Definições: *Detecções* são máximos locais de |F|/σ_nulo acima do limiar FWER do nulo de permutação de espaçamentos,
obtidos sem catálogo. *S* conta linhas r log p com uma detecção a menos da tolerância calibrada (um a um).
*p* compara S com a mesma cadeia aplicada a cada realização nula. *Recuperação* é a fração das linhas cujo
coeficiente de referência excede o limite de detecção previsto pelo nulo. As colunas de razão e fase vêm da
**medição direcionada** nos períodos conhecidos (ajuste conjunto com a resposta da janela), que não é detecção cega.

## Interpretação e limites

- A análise mede a transformada de uma janela finita de zeros; a comparação usa a forma distribucional da fórmula
  explícita, válida para zeros na janela sobre a linha crítica, fato verificado numericamente nesta faixa de alturas.
  A concordância numérica não demonstra RH nem acrescenta zeros além dos tabelados.
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
