"""Análise MN-1 (hipoteses/FICHA_MOMENTOS_NEGATIVOS.md; congelada antes do cálculo das derivadas). Critérios §6."""
import json, math, hashlib
from pathlib import Path
import numpy as np
from riemann_spectra.discrete_moments import A_q, arithmetic_factor, normalized_reciprocal, block_bootstrap_ratio

OUT = Path(__file__).parent
ROOT = OUT.parents[1]
sha = lambda f: hashlib.sha256(Path(f).read_bytes()).hexdigest()
SEED, BLOCK, REPS, NBINS = 20260927, 100, 2000, 10
rng = np.random.default_rng(SEED)
zg, zd = np.loadtxt(OUT / "derivadas_zeta_20000.txt", unpack=True)
vz, dz_ = normalized_reciprocal(zg, zd, 1), np.log(zg / (2 * math.pi))
res = {"ficha_sha256": sha(ROOT / "hipoteses/FICHA_MOMENTOS_NEGATIVOS.md"), "zeta": {}, "chi": {}}
# descritivo ζ: média de v por faixa de índice, contra 6/π²
for a, b in ((0, 3000), (3000, 10000), (10000, 20000), (0, 20000)):
    v = vz[a:b]; srt = np.sort(v)[::-1]
    res["zeta"][f"{a+1}-{b}"] = {"media_v": float(v.mean()), "razao_A1": float(v.mean() / A_q(1)),
                                 "mediana_v": float(np.median(v)), "fracao_top1pct": float(srt[:max(1, len(v)//100)].sum() / v.sum())}
for name, q in (("chi_m4", 4), ("chi_5", 5)):
    g, d = np.loadtxt(OUT / f"derivadas_{name}_3000.txt", unpack=True)
    v, dens = normalized_reciprocal(g, d, q), np.log(q * g / (2 * math.pi))
    edges = np.quantile(dens, np.linspace(0, 1, NBINS + 1)); edges[0] -= 1e-9; edges[-1] += 1e-9
    r = block_bootstrap_ratio(v, dens, vz, dz_, edges, BLOCK, REPS, rng)
    pc, h0, he = arithmetic_factor(q), 1.0, math.prod(p * p / (p * p - 1) for p in ({4: [2], 5: [5]}[q]))
    inside = lambda x: r["q025"] <= x <= r["q975"]
    ver = ("Conjectura 7 contrariada" if not inside(pc) else
           ("Conjectura 7 favorecida" if not inside(h0) else "inconclusivo"))
    top = np.argsort(v)[::-1][:5]; keep = np.setdiff1d(np.arange(len(v)), top)
    from riemann_spectra.discrete_moments import matched_expectation
    R_sem_top5 = float(v[keep].mean()) / matched_expectation(dens[keep], dz_, vz, edges)
    # frágil: tirar os 5 maiores termos de χ muda o lado de R em relação ao ponto médio entre PC e H0
    fragil = (R_sem_top5 < (pc + h0) / 2) != (r["R"] < (pc + h0) / 2)
    res["chi"][name] = {"q": q, "R": r, "previsto_PC": pc, "H0_sem_fator": h0, "HE_remove_fatores": he,
                        "HE_no_IC": inside(he), "veredito": ver, "R_sem_5_maiores": R_sem_top5,
                        "decisao_fragil": bool(fragil), "media_v": float(v.mean()), "razao_absoluta_Aq": float(v.mean() / A_q(q)),
                        "mediana_v": float(np.median(v)), "fracao_top1pct": float(np.sort(v)[::-1][:30].sum() / v.sum())}
(OUT / "analise.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
print(json.dumps(res, indent=1, ensure_ascii=False))
