"""Implementação independente (reprodução) nos blocos d01–d10 de m4-v3. Não lê resultados da primária."""
import hashlib, json, platform, sys, time
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, "independent")
import numpy, scipy  # noqa: E401
from riemann_indep import pipeline

OUT = Path("results/m4_v3_independent")
lock = json.loads(Path("independent/M4V3_PLAN.lock.json").read_text())
for f, h in lock["files"].items():
    assert hashlib.sha256(Path(f).read_bytes()).hexdigest() == h, f"arquivo alterado após congelamento: {f}"
manifest = {"started_utc": datetime.now(timezone.utc).isoformat(), "plan_lock": lock, "python": platform.python_version(),
            "numpy": numpy.__version__, "scipy": scipy.__version__,
            "raw_data_sha256": hashlib.sha256(Path("data/raw/zeros1").read_bytes()).hexdigest(), "blocks": {}}
for i in range(10):
    label, i0, i1, seed = f"d{i + 1:02d}", 70001 + 3000 * i, 73000 + 3000 * i, 9001 + i
    t = time.time()
    s = pipeline.run_block(label, i0, i1, seed, OUT, max_allowed_index=100000)
    manifest["blocks"][label] = {"indices": [i0, i1], "seed": seed, "seconds": time.time() - t, "freeze_sha256": s["freeze_sha256"]}
    print(label, "ok", round(time.time() - t), "s", flush=True)
manifest["finished_utc"] = datetime.now(timezone.utc).isoformat()
(OUT / "manifest_independent.json").write_text(json.dumps(manifest, indent=2))
