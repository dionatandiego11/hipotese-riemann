"""Executa a implementação independente nos três blocos pré-registrados (COMPARISON_PLAN.md)."""
import hashlib, json, sys, time, platform
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, "independent")
import numpy, scipy  # noqa: E401
from riemann_indep import pipeline

OUT = Path("results/independent_audit_20260913")
code = {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(Path("independent/riemann_indep").glob("*.py"))}
plan = json.loads(Path("independent/PLAN.lock.json").read_text())
assert hashlib.sha256(Path("independent/COMPARISON_PLAN.md").read_bytes()).hexdigest() == plan["COMPARISON_PLAN.md"]
assert hashlib.sha256(Path("independent/SPEC_REVIEW.md").read_bytes()).hexdigest() == plan["SPEC_REVIEW.md"]
manifest = {"started_utc": datetime.now(timezone.utc).isoformat(), "code_sha256": code, "plan_lock": plan,
            "python": platform.python_version(), "numpy": numpy.__version__, "scipy": scipy.__version__,
            "raw_data_sha256": hashlib.sha256(Path("data/raw/zeros1").read_bytes()).hexdigest(), "blocks": {}}
for label, i0, i1, seed in [("baixo_b01", 10001, 13000, 7001), ("intermediario_b05", 22001, 25000, 7002), ("alto_c10", 67001, 70000, 7003)]:
    t = time.time()
    s = pipeline.run_block(label, i0, i1, seed, OUT)
    manifest["blocks"][label] = {"indices": [i0, i1], "seed": seed, "seconds": time.time() - t, "freeze_sha256": s["freeze_sha256"]}
    print(label, "ok", round(time.time() - t), "s", flush=True)
manifest["finished_utc"] = datetime.now(timezone.utc).isoformat()
(OUT / "manifest_independent.json").write_text(json.dumps(manifest, indent=2))
