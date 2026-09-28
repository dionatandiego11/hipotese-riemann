"""Análise MN-2 (hipoteses/FICHA_MOMENTOS_NEGATIVOS_C8.md; congelada antes do cálculo de L(2ρ,χ²)). Critérios §4."""
import json, math, hashlib
from pathlib import Path
import numpy as np
from riemann_spectra.discrete_moments import arithmetic_factor, block_bootstrap_ratio
OUT = Path(__file__).parent; ROOT = OUT.parents[1]
sha = lambda f: hashlib.sha256(Path(f).read_bytes()).hexdigest()
rng = np.random.default_rng(20260928)
def w_of(name, n, q):
    g, d = np.loadtxt(OUT / f"derivadas_{name}_{n}.txt", unpack=True)
    g2, L2 = np.loadtxt(OUT / f"L2rho_{name}_{n}.txt", unpack=True)
    assert np.allclose(g, g2)
    dens = np.log(q * g / (2 * math.pi))
    return dens * L2**2 / d**2, dens
wz, dz_ = w_of("zeta", 20000, 1)
res = {"ficha_sha256": sha(ROOT / "hipoteses/FICHA_MOMENTOS_NEGATIVOS_C8.md"), "zeta": {}, "chi": {}}
for a, b in ((0, 3000), (3000, 10000), (10000, 20000), (0, 20000)):
    res["zeta"][f"{a+1}-{b}"] = {"media_w": float(wz[a:b].mean()), "mediana_w": float(np.median(wz[a:b]))}
for name, q in (("chi_m4", 4), ("chi_5", 5)):
    w, dens = w_of(name, 3000, q)
    edges = np.quantile(dens, np.linspace(0, 1, 11)); edges[0] -= 1e-9; edges[-1] += 1e-9
    r = block_bootstrap_ratio(w, dens, wz, dz_, edges, 100, 2000, rng)
    pc8 = {4: 1 / 2, 5: 4 / 5}[q]; h0 = 1.0; h7 = arithmetic_factor(q)
    inside = lambda x: r["q025"] <= x <= r["q975"]
    ver = "Conjectura 8 contrariada" if not inside(pc8) else ("Conjectura 8 favorecida" if not inside(h0) else "inconclusivo")
    res["chi"][name] = {"R": r, "previsto_C8": pc8, "H0": h0, "H7_fator_da_C7": h7, "H7_no_IC": inside(h7), "veredito": ver,
                        "media_w": float(w.mean())}
(OUT / "analise_c8.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
print(json.dumps(res, indent=1, ensure_ascii=False))
