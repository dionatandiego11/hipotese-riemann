"""
riemann_spectra.cli
Interface de linha de comando para execução reproduzível das etapas da investigação.
"""

import argparse
import csv
import json
import logging
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import numpy as np

from riemann_spectra.data import (
    build_data_manifest,
    check_validation_matches_dataset,
    dataset_paths,
    fetch_zeros,
    parse_raw_zeros,
    save_processed_csv,
    validate_with_mpmath,
)
from riemann_spectra.utils import (
    ExecutionTimer,
    code_fingerprint,
    compute_file_sha256,
    get_system_metadata,
    load_config,
    setup_logging,
)

logger = logging.getLogger("riemann_spectra.cli")

# Módulos cujo conteúdo define o protocolo científico do M3 (entram no hash de congelamento)
M3_PROTOCOL_MODULES = ["periods.py", "arithmetic.py", "inverse_spectroscopy.py", "controls.py", "unfolding.py"]



def load_zeros_csv(path: Path) -> np.ndarray:
    values = []
    with open(path, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            values.append(float(row["gamma_n"]))
    return np.asarray(values, dtype=np.float64)


def new_run_dir(tag: str) -> Path:
    """Cria a pasta da execução e guarda uma cópia integral dos fontes usados (recuperável, não só o hash)."""
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    run_dir = Path("results") / f"run_{ts}_{tag}"
    for sub in ("tables", "figures", "logs", "code"):
        (run_dir / sub).mkdir(parents=True, exist_ok=True)
    pkg = Path(__file__).resolve().parent
    for f in sorted(pkg.glob("*.py")):
        shutil.copy2(f, run_dir / "code" / f.name)
    return run_dir


def check_dataset_validation(config: Dict[str, Any], processed_file: Path, n_loaded: int) -> Dict[str, Any]:
    """Exige manifesto e validação mpmath do MESMO conjunto de dados carregado."""
    paths = dataset_paths(config)
    for key in ("manifest", "validation"):
        if not paths[key].exists():
            raise FileNotFoundError(f"{paths[key]} não existe; execute 'data fetch' e 'data validate' para {config['dataset_id']}.")
    with open(paths["validation"], encoding="utf-8") as f:
        val = json.load(f)
    check_validation_matches_dataset(val, processed_file, n_loaded)
    if not val.get("all_within_tolerance"):
        raise RuntimeError(f"Validação de {config['dataset_id']} não passou.")
    return val


# ---------------------------------------------------------------------------
# data
# ---------------------------------------------------------------------------

def cmd_data_fetch(args: argparse.Namespace) -> int:
    config = load_config(args.config)
    paths = dataset_paths(config)
    url = config["zeros_source_url"]
    fetch_zeros(url, paths["raw_file"])
    zeros, stats = parse_raw_zeros(paths["raw_file"], max_zeros=config.get("max_zeros"))
    if paths["processed_file"].exists():
        existing = load_zeros_csv(paths["processed_file"])
        if len(existing) != len(zeros) or np.max(np.abs(existing - zeros)) > 5e-13:
            logger.error(f"{paths['processed_file']} existe com conteúdo diferente; recusado sobrescrever.")
            return 1
        logger.info(f"{paths['processed_file']} já existe e coincide com o arquivo bruto.")
    else:
        save_processed_csv(zeros, paths["processed_file"])
    manifest = build_data_manifest(paths["raw_file"], paths["processed_file"], url, stats)
    manifest["dataset_id"] = config["dataset_id"]
    paths["manifest"].parent.mkdir(parents=True, exist_ok=True)
    if paths["manifest"].exists():
        with open(paths["manifest"], encoding="utf-8") as f:
            old = json.load(f)
        if old["processed_file"]["sha256"] != manifest["processed_file"]["sha256"] or old["raw_file"]["sha256"] != manifest["raw_file"]["sha256"]:
            logger.error(f"{paths['manifest']} existe com hashes diferentes; recusado sobrescrever.")
            return 1
        logger.info(f"Manifesto {paths['manifest']} já existe com os mesmos hashes; mantido.")
        return 0
    with open(paths["manifest"], "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    logger.info(f"Manifesto de dados salvo em {paths['manifest']}.")
    return 0


def cmd_data_validate(args: argparse.Namespace) -> int:
    config = load_config(args.config)
    paths = dataset_paths(config)
    if not paths["processed_file"].exists():
        logger.error(f"{paths['processed_file']} não encontrado. Execute 'data fetch' primeiro.")
        return 1
    zeros = load_zeros_csv(paths["processed_file"])
    report = validate_with_mpmath(zeros, sample_size=config.get("validation_sample_size", 20), dps=config.get("validation_dps", 40))
    report["dataset_id"] = config["dataset_id"]
    report["processed_file"] = str(paths["processed_file"])
    report["processed_sha256"] = compute_file_sha256(paths["processed_file"])
    report["n_zeros_in_file"] = int(len(zeros))
    paths["validation"].parent.mkdir(parents=True, exist_ok=True)
    if paths["validation"].exists() and not args.force_new_record:
        logger.error(f"{paths['validation']} já existe; use --force-new-record para gravar um registro datado ao lado.")
        return 1
    dest = paths["validation"]
    if dest.exists():
        dest = dest.with_name(dest.stem + "_" + datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S") + ".json")
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    logger.info(f"Validação salva em {dest}.")
    if not report.get("all_within_tolerance", False):
        logger.error("Validação mpmath FALHOU: erro superior ao erro declarado pela fonte.")
        return 1
    return 0


# ---------------------------------------------------------------------------
# run M1 / M2
# ---------------------------------------------------------------------------

def cmd_run(args: argparse.Namespace) -> int:
    milestone = args.milestone.upper()
    if milestone not in ("M1", "M2"):
        logger.error("Use o subcomando 'm3' para as Etapas 7-9 (protocolo congelado por hash).")
        return 2
    from riemann_spectra.spectral_pipeline import run_m1, run_m2

    config = load_config(args.config)
    profile = config.get("profile", "pilot")
    run_dir = new_run_dir(f"{milestone.lower()}_{profile}")
    setup_logging(log_file=run_dir / "logs" / "execution.log")
    shutil.copy(args.config, run_dir / "config_resolved.toml")
    proc_file = dataset_paths(config)["processed_file"]
    zeros = load_zeros_csv(proc_file)
    check_dataset_validation(config, proc_file, len(zeros))
    max_zeros = config.get("max_zeros")
    if max_zeros is not None:
        if max_zeros > len(zeros):
            logger.error(f"{proc_file} tem {len(zeros)} zeros; configuração pede max_zeros={max_zeros}.")
            return 1
        if max_zeros < len(zeros):
            logger.info(f"Usando o prefixo de {max_zeros} zeros do conjunto validado ({len(zeros)}).")
        zeros = zeros[:max_zeros]
    logger.info(f"=== {run_dir.name}: {len(zeros)} zeros ===")

    with ExecutionTimer() as timer:
        rng_seq = np.random.SeedSequence(config.get("seed", 20260912))
        metrics, findings, limitations = run_m1(zeros, config, run_dir, rng_seq.spawn(1)[0])
        if milestone == "M2":
            m2_metrics, m2_findings, m2_limits = run_m2(zeros, config, run_dir, rng_seq.spawn(2)[1], workers=args.workers)
            metrics.update(m2_metrics)
            findings += m2_findings
            limitations += m2_limits

    manifest = build_run_manifest(run_dir, args.config, config, proc_file, len(zeros), timer)
    metrics["performance"] = manifest["performance"]
    from riemann_spectra.reporting import save_tables_and_report

    save_tables_and_report(
        run_dir, manifest, metrics, milestone,
        f"Execução {milestone} com {len(zeros)} zeros em {timer.duration_seconds:.1f} s (pico de memória {manifest['performance']['peak_memory_mb']:.0f} MB).",
        findings, limitations,
    )
    return 0


def build_run_manifest(run_dir: Path, config_path: str, config: Dict[str, Any], data_file: Path, n_zeros: int, timer: ExecutionTimer) -> Dict[str, Any]:
    return {
        "run_id": run_dir.name,
        "command": " ".join(sys.argv),
        "config_path": str(config_path),
        "config_sha256": compute_file_sha256(config_path),
        "config": config,
        "data_file": str(data_file),
        "data_sha256": compute_file_sha256(data_file),
        "zeros_count": n_zeros,
        "code": code_fingerprint(),
        "metadata": get_system_metadata(),
        "profile": config.get("profile", config.get("protocol_version")),
        "performance": {
            "duration_seconds": timer.duration_seconds,
            "peak_memory_mb": timer.peak_memory_bytes / (1024 * 1024),
            "peak_memory_largest_child_mb": timer.peak_children_bytes / (1024 * 1024),
            "memory_note": "RSS máximo do processo principal e do maior processo filho; o pico agregado dos processos simultâneos não é medido.",
        },
    }


# ---------------------------------------------------------------------------
# protocolo M3
# ---------------------------------------------------------------------------

def lock_path_for(config_path: str) -> Path:
    p = Path(config_path)
    return p.with_suffix(".lock.json")


def current_protocol_fingerprint(config_path: str) -> Dict[str, Any]:
    fp = code_fingerprint(M3_PROTOCOL_MODULES)
    return {"config_sha256": compute_file_sha256(config_path), "modules_sha256": fp["modules"], "combined_sha256": fp["combined_sha256"]}


def cmd_protocol_freeze(args: argparse.Namespace) -> int:
    lock = lock_path_for(args.config)
    fp = current_protocol_fingerprint(args.config)
    if lock.exists():
        with open(lock, encoding="utf-8") as f:
            old = json.load(f)
        if old["config_sha256"] == fp["config_sha256"] and old["combined_sha256"] == fp["combined_sha256"]:
            logger.info(f"Protocolo já congelado com o mesmo hash em {lock}.")
            return 0
        logger.error(f"{lock} existe com hash diferente. Crie uma nova versão do protocolo em vez de sobrescrever.")
        return 1
    record = {
        "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
        "config_path": str(args.config),
        **fp,
        "note": args.note,
    }
    with open(lock, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, ensure_ascii=False)
    logger.info(f"Protocolo congelado: {lock} (config {fp['config_sha256'][:12]}…, código {fp['combined_sha256'][:12]}…)")
    return 0


def cmd_m3(args: argparse.Namespace) -> int:
    from riemann_spectra.inverse_spectroscopy import run_block
    from riemann_spectra.m3_report import write_m3_run_report

    cfg = load_config(args.config)
    requested = [b.strip() for b in args.blocks.split(",") if b.strip()]
    blocks = [b for b in cfg["blocks"] if b["name"] in requested]
    missing = set(requested) - {b["name"] for b in blocks}
    if missing:
        logger.error(f"Blocos desconhecidos: {sorted(missing)}")
        return 2
    lock_record = None
    locked = {b["name"] for b in cfg["blocks"] if b.get("requires_lock", False)}
    if locked & set(requested):
        lock = lock_path_for(args.config)
        if not lock.exists():
            logger.error(f"Blocos {sorted(locked & set(requested))} exigem protocolo congelado ({lock}). Execute 'protocol freeze'.")
            return 3
        with open(lock, encoding="utf-8") as f:
            lock_record = json.load(f)
        fp = current_protocol_fingerprint(args.config)
        if fp["config_sha256"] != lock_record["config_sha256"] or fp["combined_sha256"] != lock_record["combined_sha256"]:
            logger.error("Configuração ou código do protocolo diferem do congelado. Execução do bloco reservado recusada.")
            return 3

    run_dir = new_run_dir("m3_" + "-".join(requested))
    setup_logging(log_file=run_dir / "logs" / "execution.log")
    shutil.copy(args.config, run_dir / "config_resolved.toml")
    data_file = dataset_paths(cfg)["processed_file"]
    zeros = load_zeros_csv(data_file)
    check_dataset_validation(cfg, data_file, len(zeros))
    logger.info(f"=== {run_dir.name}: blocos {requested}, workers={args.workers} ===")

    root_seq = np.random.SeedSequence(cfg["seed"])
    # uma SeedSequence por bloco, indexada pela posição do bloco no protocolo (independe da seleção)
    block_seqs = root_seq.spawn(len(cfg["blocks"]))
    results = {}
    with ExecutionTimer() as timer:
        for b in blocks:
            pos = [x["name"] for x in cfg["blocks"]].index(b["name"])
            results[b["name"]] = run_block(zeros, b, cfg, run_dir / "tables", block_seqs[pos], workers=args.workers)

    manifest = build_run_manifest(run_dir, args.config, cfg, data_file, len(zeros), timer)
    manifest["protocol_lock"] = lock_record
    manifest["blocks"] = requested
    write_m3_run_report(run_dir, manifest, results)
    logger.info(f"Execução {run_dir.name} concluída em {timer.duration_seconds:.1f} s.")
    return 0


# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------

def cmd_report(args: argparse.Namespace) -> int:
    report_file = Path("results") / args.run_id / "report.md"
    if not report_file.exists():
        logger.error(f"Relatório {report_file} não encontrado.")
        return 1
    print(report_file.read_text(encoding="utf-8"))
    return 0


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="riemann-spectra", description="Espectroscopia inversa dos zeros da zeta.")
    sub = parser.add_subparsers(dest="command", required=True)

    data_p = sub.add_parser("data", help="Aquisição e auditoria dos zeros.")
    data_sub = data_p.add_subparsers(dest="data_action", required=True)
    p = data_sub.add_parser("fetch", help="Baixar e processar a tabela de Odlyzko.")
    p.add_argument("--config", default="configs/main.toml")
    p = data_sub.add_parser("validate", help="Validar amostra com mpmath.")
    p.add_argument("--config", default="configs/main.toml")
    p.add_argument("--force-new-record", action="store_true", help="Gravar novo registro datado se já existir um.")

    p = sub.add_parser("run", help="Executar M1 ou M2.")
    p.add_argument("--config", required=True)
    p.add_argument("--milestone", required=True, choices=["M1", "M2"])
    p.add_argument("--workers", type=int, default=1)

    proto = sub.add_parser("protocol", help="Congelamento do protocolo M3.")
    proto_sub = proto.add_subparsers(dest="protocol_action", required=True)
    p = proto_sub.add_parser("freeze", help="Registrar hash da configuração e dos módulos científicos.")
    p.add_argument("--config", default="configs/m3_protocol.toml")
    p.add_argument("--note", default="")

    p = sub.add_parser("m3", help="Etapas 7-9 por bloco (holdout/full exigem protocolo congelado).")
    p.add_argument("--config", default="configs/m3_protocol.toml")
    p.add_argument("--blocks", required=True, help="Lista separada por vírgulas: pilot,dev,val,holdout,full")
    p.add_argument("--workers", type=int, default=1)

    p = sub.add_parser("report", help="Exibir relatório de uma execução.")
    p.add_argument("--run-id", required=True)

    args = parser.parse_args(argv)
    setup_logging()
    if args.command == "data":
        return cmd_data_fetch(args) if args.data_action == "fetch" else cmd_data_validate(args)
    if args.command == "run":
        return cmd_run(args)
    if args.command == "protocol":
        return cmd_protocol_freeze(args)
    if args.command == "m3":
        return cmd_m3(args)
    if args.command == "report":
        return cmd_report(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
