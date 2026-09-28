"""MN-3: zeros 1–N de L(s,χ₈) e L(s,χ₁₂) com o dirichlet_zeros.run congelado (V1–V4, retomada). Teto por RLIMIT_CPU."""
import argparse, resource, json
from pathlib import Path
from mn3_caracteres import CHARS, dz
ap = argparse.ArgumentParser(); ap.add_argument("--carater", choices=list(CHARS), required=True)
ap.add_argument("--n", type=int, required=True); ap.add_argument("--teto-cpu", type=int, required=True); a = ap.parse_args()
resource.setrlimit(resource.RLIMIT_CPU, (a.teto_cpu, a.teto_cpu + 60))
m = dz.run(CHARS[a.carater], a.n, Path(__file__).parent / "mn3_zeros")
print(json.dumps({"all_checks_passed": m.get("all_checks_passed"), "checks": {k: v.get("passed") for k, v in m["checks"].items()}}))
