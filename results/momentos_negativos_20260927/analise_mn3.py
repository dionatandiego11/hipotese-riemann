"""Análise MN-3 (hipoteses/FICHA_MOMENTOS_NEGATIVOS_MN3.md, congelada antes dos cálculos). Critérios §5."""
import json, math, hashlib
from pathlib import Path
import numpy as np
from riemann_spectra.discrete_moments import block_bootstrap_ratio
OUT = Path(__file__).parent; ROOT = OUT.parents[1]
sha = lambda f: hashlib.sha256(Path(f).read_bytes()).hexdigest()
rng = np.random.default_rng(20260929)
def load(name, n, q):
    g, d = np.loadtxt(OUT / f"derivadas_{name}_{n}.txt", unpack=True)
    g2, L2 = np.loadtxt(OUT / f"L2rho_{name}_{n}.txt", unpack=True); assert np.allclose(g, g2)
    dens = np.log(q * g / (2 * math.pi))
    return dens / d**2, dens * L2**2 / d**2, dens
vz, wz, dz_ = load("zeta", 27000, 1)
PRED = {"chi_8": {"q": 8, "C7": 2/3, "C8": 1/2, "alt7": {"H0": 1.0, "HE": 4/3}, "alt8": {"H0": 1.0, "H7": 2/3}},
        "chi_12": {"q": 12, "C7": 1/2, "C8": 1/3, "alt7": {"H0": 1.0, "HE": 3/2}, "alt8": {"H0": 1.0, "H7": 1/2}}}
res = {"ficha_sha256": sha(ROOT / "hipoteses/FICHA_MOMENTOS_NEGATIVOS_MN3.md"), "chi": {}}
for name, P in PRED.items():
    v, w, dens = load(name, 2000, P["q"])
    edges = np.quantile(dens, np.linspace(0, 1, 11)); edges[0] -= 1e-9; edges[-1] += 1e-9
    out = {}
    for conj, x_test, x_ref, alts in (("C7", v, vz, P["alt7"]), ("C8", w, wz, P["alt8"])):
        r = block_bootstrap_ratio(x_test, dens, x_ref, dz_, edges, 100, 2000, rng)
        inside = lambda x: r["q025"] <= x <= r["q975"]
        ver = f"{conj} contrariada" if not inside(P[conj]) else (f"{conj} favorecida" if not inside(1.0) else "inconclusivo")
        out[conj] = {"R": r, "previsto": P[conj], "alternativas_no_IC": {k: inside(a) for k, a in alts.items()}, "veredito": ver}
    out["max_densidade_teste"] = float(dens.max()); out["max_densidade_ref"] = float(dz_.max())
    res["chi"][name] = out
(OUT / "analise_mn3.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
print(json.dumps(res, indent=1, ensure_ascii=False))
