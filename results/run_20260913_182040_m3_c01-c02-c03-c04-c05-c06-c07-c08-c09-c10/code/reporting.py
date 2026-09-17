"""
riemann_spectra.reporting
Geração de gráficos, tabelas e relatórios estruturados em Markdown e JSON.
"""

import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, List

import numpy as np

# Garantir que matplotlib rode em ambiente headless sem display
os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

logger = logging.getLogger("riemann_spectra.reporting")


def plot_spacings(
    spacing_stats: Dict[str, Any],
    output_path: str | Path,
    title: str = "Distribuição dos Espaçamentos Consecutivos s_n",
) -> Path:
    """Gera gráfico do histograma de espaçamentos comparado com Wigner-GUE e Poisson."""
    dest = Path(output_path)
    dest.parent.mkdir(parents=True, exist_ok=True)

    bins_data = spacing_stats["bins"]
    centers = np.array(bins_data["centers"])
    density = np.array(bins_data["density"])
    wigner = np.array(bins_data["wigner"])
    poisson = np.array(bins_data["poisson"])

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True, gridspec_kw={"height_ratios": [3, 1]})

    ax1.bar(centers, density, width=centers[1] - centers[0], alpha=0.5, color="steelblue", edgecolor="black", label="Empírico (zeros da zeta)")
    ax1.plot(centers, wigner, "r-", linewidth=2, label="Wigner Surmise (GUE)")
    ax1.plot(centers, poisson, "k--", linewidth=1.5, label="Poisson (Aleatório)")

    ax1.set_ylabel("Densidade de probabilidade P(s)")
    ax1.set_title(title, fontsize=12, fontweight="bold")
    ax1.legend(loc="upper right")
    ax1.grid(True, alpha=0.3)

    # Subgráfico de resíduos
    res_wigner = density - wigner
    ax2.plot(centers, res_wigner, "r.-", label="Resíduo vs GUE")
    ax2.axhline(0, color="gray", linestyle="--")
    ax2.set_xlabel("Espaçamento normalizado s")
    ax2.set_ylabel("Resíduo")
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc="upper right")

    plt.tight_layout()
    fig.savefig(dest, dpi=200)
    plt.close(fig)
    logger.info(f"Gráfico de espaçamentos salvo em {dest}.")
    return dest


def plot_pair_correlation(
    r2_stats: Dict[str, Any],
    output_path: str | Path,
    title: str = "Função de Correlação de Pares R_2(s)",
) -> Path:
    """Gera gráfico da correlação de pares empírica comparada com Montgomery GUE e Poisson."""
    dest = Path(output_path)
    dest.parent.mkdir(parents=True, exist_ok=True)

    bins_data = r2_stats["bins"]
    centers = np.array(bins_data["centers"])
    r2_emp = np.array(bins_data["r2_empirical"])
    r2_gue = np.array(bins_data["r2_gue"])
    r2_poi = np.array(bins_data["r2_poisson"])

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True, gridspec_kw={"height_ratios": [3, 1]})

    ax1.plot(centers, r2_emp, "bo-", markersize=4, label="Empírico (zeros da zeta)")
    ax1.plot(centers, r2_gue, "r-", linewidth=2, label=r"Montgomery / GUE: $1 - (\sin \pi s / \pi s)^2$")
    ax1.plot(centers, r2_poi, "k--", linewidth=1.5, label="Poisson: 1.0")

    ax1.set_ylabel("R_2(s)")
    ax1.set_title(title, fontsize=12, fontweight="bold")
    ax1.legend(loc="lower right")
    ax1.grid(True, alpha=0.3)

    # Resíduos
    residuals = np.array(bins_data["residuals_gue"])
    ax2.plot(centers, residuals, "r.-", label="Resíduo vs GUE")
    ax2.axhline(0, color="gray", linestyle="--")
    ax2.set_xlabel("Separação normalizada s")
    ax2.set_ylabel("Resíduo")
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc="upper right")

    plt.tight_layout()
    fig.savefig(dest, dpi=200)
    plt.close(fig)
    logger.info(f"Gráfico de correlação de pares salvo em {dest}.")
    return dest


def plot_spectral_form_factor(
    sff_data: Dict[str, Any],
    output_path: str | Path,
    title: str = "Spectral Form Factor K(tau)",
) -> Path:
    """Gera gráfico do spectral form factor conectado e total."""
    dest = Path(output_path)
    dest.parent.mkdir(parents=True, exist_ok=True)

    tau = np.array(sff_data["tau"])
    k_conn = np.array(sff_data["k_connected"])
    k_tot = np.array(sff_data["k_total"])
    k_gue = np.array(sff_data["k_gue_theoretical"])

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(tau, k_conn, "b-", alpha=0.8, label=r"Conectado $\widehat K_c(\tau)$")
    ax.plot(tau, k_tot, "c--", alpha=0.5, label=r"Total $\widehat K(\tau)$ (com termo diagonal)")
    ax.plot(tau, k_gue, "r-", linewidth=2, label=r"Limite GUE: $\min(|\tau|, 1)$")

    ax.set_xlabel(r"Tempo adimensional $\tau$")
    ax.set_ylabel(r"$K(\tau)$")
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_yscale("log")
    ax.set_xscale("linear")
    ax.legend(loc="best")
    ax.grid(True, alpha=0.3, which="both")

    plt.tight_layout()
    fig.savefig(dest, dpi=200)
    plt.close(fig)
    logger.info(f"Gráfico do spectral form factor salvo em {dest}.")
    return dest


def save_tables_and_report(
    run_dir: Path,
    manifest: Dict[str, Any],
    metrics: Dict[str, Any],
    milestone: str,
    summary_text: str,
    findings: List[str] | None = None,
    limitations: List[str] | None = None,
) -> None:
    """
    Salva manifest.json, metrics.json e report.md. O relatório só contém afirmações passadas
    explicitamente em `findings` (derivadas das métricas medidas); nada é afirmado por padrão.
    """
    run_dir.mkdir(parents=True, exist_ok=True)
    with open(run_dir / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False, default=str)
    with open(run_dir / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False, default=str)

    findings_md = "\n".join(f"- {x}" for x in (findings or ["Nenhuma afirmação derivada automaticamente; consulte as métricas."]))
    limits_md = "\n".join(f"- {x}" for x in (limitations or ["Consulte docs/ANDAMENTO.md para o estado das etapas."]))
    report_content = f"""# Relatório de execução — {milestone}

**ID:** `{run_dir.name}`
**Data UTC:** `{manifest.get('metadata', {}).get('timestamp_utc', 'N/A')}`
**Perfil:** `{manifest.get('profile', 'N/A')}`
**Zeros analisados:** `{manifest.get('zeros_count', 'N/A')}`

## Resumo

{summary_text}

## Afirmações sustentadas por esta execução

{findings_md}

## Limitações

{limits_md}

## Métricas

```json
{json.dumps(metrics, indent=2, ensure_ascii=False, default=str)}
```
"""
    with open(run_dir / "report.md", "w", encoding="utf-8") as f:
        f.write(report_content)
    logger.info(f"Relatório e métricas salvos em {run_dir}.")


# ---------------------------------------------------------------------------
# M3
# ---------------------------------------------------------------------------

def plot_m3_spectrum(block_dir: Path, catalog_rows: List[Dict[str, Any]], title: str) -> Path:
    """|F|/sigma_nulo com limiar, detecções congeladas e (depois) linhas r log p."""
    data = np.load(block_dir / "nulls.npz")
    t = data["t_grid"]
    F = data["F_real"] + 1j * data["F_imag"]
    sigma = data["shuffle_sigma"]
    with open(block_dir / "block_metrics.json", encoding="utf-8") as f:
        bm = json.load(f)
    thr = bm["null_summary"]["shuffle"]["threshold_z"]
    z = np.abs(F) / sigma
    fig, axes = plt.subplots(2, 1, figsize=(12, 7), sharex=True, gridspec_kw={"height_ratios": [2, 1]})
    ax = axes[0]
    ax.semilogy(t, np.maximum(z, 1e-6), lw=0.6, color="tab:blue", label=r"zeros: $|F_w(t)|/\sigma_{\rm nulo}(t)$")
    ax.axhline(thr, color="tab:red", ls="--", lw=1, label=f"limiar FWER (nulo shuffle) z={thr:.2f}")
    det = [r for r in catalog_rows if r["detected"]]
    miss = [r for r in catalog_rows if not r["detected"]]
    ax.plot([r["period_theoretical"] for r in det], [thr * 1.8] * len(det), "v", color="tab:green", ms=4, label="r log p detectado")
    ax.plot([r["period_theoretical"] for r in miss], [thr * 1.8] * len(miss), "x", color="gray", ms=4, label="r log p não detectado")
    ax.set_ylim(1e-5, None)
    ax.set_ylabel("z")
    ax.set_title(title)
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(alpha=0.3, which="both")
    ax2 = axes[1]
    ax2.plot(t, sigma, color="tab:orange", lw=1, label=r"$\sigma$ nulo shuffle")
    ax2.plot(t, data["gue_sigma"], color="tab:purple", lw=1, label=r"$\sigma$ nulo GUE")
    ax2.set_xlabel("t (período, convenção $e^{-iEt}$)")
    ax2.set_ylabel(r"$\sigma(t)$")
    ax2.legend(fontsize=8)
    ax2.grid(alpha=0.3)
    plt.tight_layout()
    dest = block_dir / "spectrum_z.png"
    fig.savefig(dest, dpi=150)
    plt.close(fig)
    return dest


def plot_m3_coefficients(block_dir: Path, catalog_rows: List[Dict[str, Any]], title: str) -> Path:
    """Coeficientes ajustados (direcionados) versus -log p / (pi p^{r/2})."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    for rep_mask, color, label in [(1, "tab:blue", "r = 1"), (2, "tab:orange", "r >= 2")]:
        rows = [r for r in catalog_rows if (r["repetition"] == 1) == (rep_mask == 1)]
        if not rows:
            continue
        th = np.array([r["coefficient_theoretical"] for r in rows])
        fit = np.array([r["fit_coefficient_real"] for r in rows])
        det = np.array([r["detected"] for r in rows])
        axes[0].plot(-th[det], -fit[det], "o", color=color, ms=4, label=f"{label} detectado")
        axes[0].plot(-th[~det], -fit[~det], "o", mfc="none", color=color, ms=4, label=f"{label} não detectado")
        dev = np.abs(np.array([r["fit_ratio_to_theory"] for r in rows]) - 1.0)
        axes[1].semilogy([r["period_theoretical"] for r in rows], np.maximum(dev, 1e-16), "o", color=color, ms=4, label=label)
    lim = [0, 0.25]
    axes[0].plot(lim, lim, "k:", lw=1)
    axes[0].set_xlabel(r"$\log p/(\pi p^{r/2})$ (referência)")
    axes[0].set_ylabel(r"$-\mathrm{Re}\,C$ ajustado")
    axes[0].legend(fontsize=8)
    axes[0].grid(alpha=0.3)
    axes[1].set_xlabel("período r log p")
    axes[1].set_ylabel("|razão ajustado/teórico - 1|")
    axes[1].grid(alpha=0.3, which="both")
    axes[1].legend(fontsize=8)
    fig.suptitle(title + " — medição direcionada (não cega)")
    plt.tight_layout()
    dest = block_dir / "coefficients.png"
    fig.savefig(dest, dpi=150)
    plt.close(fig)
    return dest


def plot_m3_recovery(block_dir: Path, calib: Dict[str, Any], title: str) -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    curve = calib["recovery_curve"]
    if curve:
        x = [0.5 * (c["z_true_low"] + c["z_true_high"]) for c in curve]
        axes[0].plot(x, [c["recovery_rate"] for c in curve], "o-")
    axes[0].set_xlabel("z verdadeiro da linha injetada")
    axes[0].set_ylabel("taxa de recuperação")
    axes[0].set_ylim(-0.05, 1.05)
    axes[0].grid(alpha=0.3)
    pc = calib["pair_resolution_curve"]
    if pc:
        axes[1].plot([c["separation_fwhm"] for c in pc], [c["fraction_lines_recovered"] for c in pc], "o-")
    axes[1].set_xlabel("separação do par (FWHM)")
    axes[1].set_ylabel("fração de linhas recuperadas")
    axes[1].set_ylim(-0.05, 1.05)
    axes[1].grid(alpha=0.3)
    fig.suptitle(title + " — calibração sintética (níveis GUE com linhas injetadas)")
    plt.tight_layout()
    dest = block_dir / "synthetic_calibration.png"
    fig.savefig(dest, dpi=150)
    plt.close(fig)
    return dest


# ---------------------------------------------------------------------------
# M2
# ---------------------------------------------------------------------------

def plot_m2_block(fig_dir: Path, name: str, grid, obs, tests, edges, r2, tau) -> Path:
    """CDF de espaçamentos, R2 e K_c dos zeros com envelopes GUE e Poisson do mesmo estimador."""
    from riemann_spectra.statistics import poisson_cdf, wigner_gue_cdf

    fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))
    g = tests["gue"]
    p = tests["poisson"]
    ax = axes[0]
    ax.fill_between(grid, g["cdf"]["q025"] - g["cdf"]["mean"], g["cdf"]["q975"] - g["cdf"]["mean"], color="tab:red", alpha=0.25, label="envelope GUE 95%")
    ax.plot(grid, obs["cdf"] - g["cdf"]["mean"], color="tab:blue", lw=1, label="zeros − média GUE")
    ax.plot(grid, wigner_gue_cdf(grid) - g["cdf"]["mean"], "k--", lw=1, label="Wigner surmise − média GUE")
    ax.set_xlim(0, 3)
    ax.set_xlabel("s")
    ax.set_ylabel("diferença de CDF")
    ax.set_title(f"{name}: espaçamentos (p_GUE={g['cdf']['p_value_mc']:.3f})")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3)

    centers = 0.5 * (edges[:-1] + edges[1:])
    ax = axes[1]
    ax.fill_between(centers, g["r2"]["q025"], g["r2"]["q975"], color="tab:red", alpha=0.25, label="envelope GUE 95%")
    ax.plot(centers, obs["r2"], "o", color="tab:blue", ms=3, label="zeros")
    ax.plot(centers, r2["bins"]["r2_gue"], "k-", lw=1, label="Montgomery (média no bin)")
    ax.plot(centers, p["r2"]["mean"], ":", color="gray", label="Poisson (média)")
    ax.set_xlabel("s")
    ax.set_ylabel("R2(s)")
    ax.set_title(f"{name}: correlação de pares (p_GUE={g['r2']['p_value_mc']:.3f})")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3)

    ax = axes[2]
    ax.fill_between(tau, g["k_connected"]["q025"], g["k_connected"]["q975"], color="tab:red", alpha=0.25, label="envelope GUE 95%")
    ax.plot(tau, obs["k_connected"], color="tab:blue", lw=1, label="zeros")
    ax.plot(tau, np.minimum(tau, 1.0), "k--", lw=1, label="min(τ,1)")
    ax.plot(tau, p["k_connected"]["mean"], ":", color="gray", label="Poisson (média)")
    ax.set_xlabel("τ")
    ax.set_ylabel("K_c(τ)")
    ax.set_title(f"{name}: form factor conectado (p_GUE={g['k_connected']['p_value_mc']:.3f})")
    ax.legend(fontsize=7)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    dest = Path(fig_dir) / f"m2_{name}.png"
    fig.savefig(dest, dpi=150)
    plt.close(fig)
    return dest
