"""
riemann_spectra.utils
Utilitários de configuração, hashing, medição de recursos e manifesto de execução.
"""

import hashlib
import json
import logging
import os
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

# Garantir que o Matplotlib use um diretório gravável para cache
os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

logger = logging.getLogger("riemann_spectra")


def setup_logging(level: int = logging.INFO, log_file: Path | None = None) -> None:
    """Configura logging estruturado no console e opcionalmente em arquivo."""
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    root = logging.getLogger()
    root.setLevel(level)

    # Limpar handlers existentes
    for h in list(root.handlers):
        root.removeHandler(h)

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    root.addHandler(console)

    if log_file is not None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setFormatter(formatter)
        root.addHandler(fh)


def compute_file_sha256(filepath: str | Path) -> str:
    """Calcula o hash SHA-256 de um arquivo em blocos de 64 KiB."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado para hash: {filepath}")
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            sha.update(chunk)
    return sha.hexdigest()


def compute_string_sha256(text: str) -> str:
    """Calcula o hash SHA-256 de uma string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_config(config_path: str | Path) -> Dict[str, Any]:
    """Carrega configuração TOML e valida presença de chaves essenciais."""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {path}")

    # Python 3.11+ tem tomllib nativo
    try:
        import tomllib
    except ImportError:
        import tomli as tomllib  # type: ignore

    with open(path, "rb") as f:
        config = tomllib.load(f)

    return config


def get_system_metadata() -> Dict[str, Any]:
    """Versões de Python, bibliotecas e configuração BLAS/LAPACK do NumPy."""
    import numpy as np
    import scipy
    import mpmath
    import matplotlib

    try:
        np_cfg = np.show_config(mode="dicts")
        blas = np_cfg.get("Build Dependencies", {})
    except Exception as exc:  # pragma: no cover - depende da versão do NumPy
        blas = {"error": str(exc)}
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": sys.version,
        "platform": platform.platform(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
        "libraries": {
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "mpmath": mpmath.__version__,
            "matplotlib": matplotlib.__version__,
        },
        "numpy_build_dependencies": blas,
    }


def code_fingerprint(modules: list | None = None) -> Dict[str, Any]:
    """SHA-256 de cada módulo de src/riemann_spectra (ou da lista dada) e hash combinado."""
    pkg = Path(__file__).resolve().parent
    files = sorted(pkg.glob("*.py")) if modules is None else [pkg / m for m in sorted(modules)]
    per = {f.name: compute_file_sha256(f) for f in files}
    combined = hashlib.sha256("".join(f"{k}:{v}\n" for k, v in per.items()).encode()).hexdigest()
    return {"modules": per, "combined_sha256": combined}


class ExecutionTimer:
    """Context manager e medidor de tempo e memória de execuções."""

    def __init__(self):
        self.start_time = 0.0
        self.end_time = 0.0
        self.duration_seconds = 0.0
        self.peak_memory_bytes = 0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter()
        self.duration_seconds = self.end_time - self.start_time
        try:
            import resource
            # ru_maxrss é em KiB no Linux
            self.peak_memory_bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
        except Exception:
            self.peak_memory_bytes = 0
