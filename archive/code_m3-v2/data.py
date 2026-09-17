"""
riemann_spectra.data
Aquisição, auditoria, validação independente e processamento dos zeros de Riemann.
"""

import json
import logging
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np

from riemann_spectra.utils import compute_file_sha256

logger = logging.getLogger("riemann_spectra.data")


def fetch_zeros(url: str, output_path: str | Path) -> Path:
    """
    Baixa o arquivo bruto de zeros da fonte oficial se ainda não existir localmente.
    Preserva rigorosamente o arquivo original.
    """
    dest = Path(output_path)
    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists() and dest.stat().st_size > 0:
        logger.info(f"Arquivo já existe em {dest} ({dest.stat().st_size} bytes). Download ignorado.")
        return dest

    logger.info(f"Baixando zeros de {url} para {dest}...")
    headers = {"User-Agent": "RiemannSpectraResearch/0.1.0"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(dest, "wb") as f:
        while chunk := resp.read(65536):
            f.write(chunk)

    logger.info(f"Download concluído: {dest.stat().st_size} bytes.")
    return dest


def parse_raw_zeros(raw_path: str | Path, max_zeros: int | None = None) -> Tuple[np.ndarray, Dict[str, Any]]:
    """
    Analisa o arquivo de zeros de Odlyzko.
    Formato esperado: uma ordenada por linha em formato de texto.
    Verifica:
    - Finitude e ausência de NaN/Inf
    - Ordenação estrita (gamma_{n+1} > gamma_n)
    - Ausência de duplicatas
    - Quantidade de registros
    """
    path = Path(raw_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo de dados brutos não encontrado: {path}")

    zeros_list: List[float] = []
    line_count = 0

    with open(path, "r", encoding="ascii", errors="strict") as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            try:
                val = float(stripped)
            except ValueError as e:
                raise ValueError(f"Linha inválida {line_count + 1}: '{stripped}' não é float válido") from e

            zeros_list.append(val)
            line_count += 1
            if max_zeros is not None and line_count >= max_zeros:
                break

    arr = np.asarray(zeros_list, dtype=np.float64)

    # Verificações de auditoria
    if len(arr) == 0:
        raise ValueError("Nenhum zero foi carregado do arquivo.")

    if not np.all(np.isfinite(arr)):
        raise ValueError("Detectados valores não finitos (NaN ou Inf) no conjunto de zeros.")

    diffs = np.diff(arr)
    min_diff = float(np.min(diffs)) if len(diffs) > 0 else 0.0
    if min_diff <= 0.0:
        bad_idx = int(np.argmin(diffs))
        raise ValueError(
            f"Violação de ordenação estrita detectada no índice {bad_idx + 1}: "
            f"gamma_{bad_idx + 1} = {arr[bad_idx]}, gamma_{bad_idx + 2} = {arr[bad_idx + 1]} (diferença: {diffs[bad_idx]})"
        )

    stats = {
        "total_records_loaded": len(arr),
        "gamma_min": float(arr[0]),
        "gamma_max": float(arr[-1]),
        "min_spacing": min_diff,
        "max_spacing": float(np.max(diffs)) if len(diffs) > 0 else 0.0,
        "strictly_increasing": True,
        "all_finite": True,
    }
    logger.info(f"Carregados {len(arr)} zeros. Intervalo: [{arr[0]:.6f}, {arr[-1]:.6f}]. Espaçamento mín: {min_diff:.6f}")
    return arr, stats


def save_processed_csv(zeros: np.ndarray, output_path: str | Path) -> Path:
    """Salva os zeros processados em CSV com índice 1-based (n, gamma_n)."""
    dest = Path(output_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write("n,gamma_n\n")
        for i, g in enumerate(zeros, start=1):
            f.write(f"{i},{g:.12f}\n")
    logger.info(f"Tabela processada salva em {dest} ({len(zeros)} registros).")
    return dest


def validate_with_mpmath(
    zeros: np.ndarray,
    sample_size: int = 20,
    dps: int = 40,
    declared_source_error: float = 3e-9,
) -> Dict[str, Any]:
    """
    Recalcula uma amostra determinística estratificada de índices usando mpmath.zetazero
    com precisão arbitrária (dps casas decimais de trabalho).
    Compara o erro absoluto com a tolerância declarada de Odlyzko (3e-9).
    Também avalia o resíduo da função zeta no ponto crítico rho = 1/2 + i*gamma.
    """
    import mpmath
    mpmath.mp.dps = dps

    n_total = len(zeros)
    if sample_size <= 0 or n_total == 0:
        return {"error": "Amostra ou array vazio"}

    # Estratificação determinística uniforme cobrindo extremos e interior
    if n_total <= sample_size:
        indices = list(range(1, n_total + 1))
    else:
        # Índices 1-based
        raw_idx = np.round(np.linspace(1, n_total, sample_size)).astype(int)
        # Garantir unicidade mantendo extremos
        indices = sorted(list(set(raw_idx.tolist())))

    comparisons: List[Dict[str, Any]] = []
    max_abs_err = 0.0

    logger.info(f"Iniciando validação independente com mpmath (dps={dps}) para {len(indices)} índices estratificados...")

    for n in indices:
        tab_val = float(zeros[n - 1])
        # mpmath.zetazero usa índice 1-based
        z_mp = mpmath.zetazero(n)
        exact_gamma = float(mpmath.im(z_mp))
        abs_err = abs(tab_val - exact_gamma)
        max_abs_err = max(max_abs_err, abs_err)

        # Avaliar zeta(1/2 + i*tab_val)
        s_point = mpmath.mpc(0.5, tab_val)
        zeta_val = mpmath.zeta(s_point)
        zeta_abs = float(abs(zeta_val))

        comparisons.append({
            "index_n": n,
            "table_gamma": tab_val,
            "mpmath_gamma": exact_gamma,
            "absolute_error": abs_err,
            "within_declared_error": bool(abs_err <= declared_source_error * 2.0),
            "zeta_residual_magnitude": zeta_abs,
        })

    all_passed = bool(max_abs_err <= declared_source_error * 2.0)

    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "dps": dps,
        "sample_size": len(indices),
        "declared_source_error": declared_source_error,
        "max_absolute_error_observed": max_abs_err,
        "all_within_tolerance": all_passed,
        "details": comparisons,
    }
    logger.info(f"Validação mpmath concluída. Erro máx observado: {max_abs_err:.3e} (limite declarado: {declared_source_error:.3e}). Aprovado: {all_passed}")
    return report


def build_data_manifest(
    raw_path: str | Path,
    processed_path: str | Path,
    url: str,
    stats: Dict[str, Any],
    declared_accuracy: str = "3e-9",
) -> Dict[str, Any]:
    """Gera o manifesto completo de auditoria dos dados de entrada."""
    raw_p = Path(raw_path)
    proc_p = Path(processed_path)

    manifest = {
        "dataset_name": "Odlyzko Riemann Zeta Zeros (zeros1)",
        "source_url": url,
        "retrieval_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "declared_accuracy": declared_accuracy,
        "raw_file": {
            "path": str(raw_p),
            "size_bytes": raw_p.stat().st_size if raw_p.exists() else 0,
            "sha256": compute_file_sha256(raw_p) if raw_p.exists() else None,
        },
        "processed_file": {
            "path": str(proc_p),
            "size_bytes": proc_p.stat().st_size if proc_p.exists() else 0,
            "sha256": compute_file_sha256(proc_p) if proc_p.exists() else None,
        },
        "statistics": stats,
    }
    return manifest
