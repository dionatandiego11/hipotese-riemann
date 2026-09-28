"""Medição PT-1 (hipoteses/FICHA_PICO_TAU1.md, congelada antes desta execução). Critérios da ficha §5, sem alteração."""
import json, math, time, hashlib
from pathlib import Path
import numpy as np
from scipy.stats import spearmanr
from riemann_spectra.unfolding import n_bar_rvm
from riemann_spectra.bragg_peak import kc_tau1

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).parent
P = json.loads((OUT.parent / "previsao" / "previsao.json").read_text())["blocos"]
sha = lambda f: hashlib.sha256(Path(f).read_bytes()).hexdigest()
t0 = time.time()
zf = ROOT / "data/processed/zeros_100k.csv"
gam = np.loadtxt(zf, delimiter=",", skiprows=1)[:, 1]
out = {"ficha_sha256": sha(ROOT / "hipoteses/FICHA_PICO_TAU1.md"), "zeros": {"arquivo": str(zf.relative_to(ROOT)),
       "sha256": sha(zf)}, "blocos": {}}
inB = above = 0
obs, predB, sds = [], [], []
for name, d in P.items():
    i0, i1 = d["indices"]
    kc = kc_tau1(n_bar_rvm(gam[i0 - 1:i1]), n_blocks=10)
    lo = min(d[m]["q025"] for m in ("B", "B25", "B75")); hi = max(d[m]["q975"] for m in ("B", "B25", "B75"))
    alt = max(d[m]["q975"] for m in ("U", "G"))
    ok_b, ok_a = lo <= kc <= hi, kc > alt
    inB += ok_b; above += ok_a
    obs.append(kc); predB.append(d["B"]["media"]); sds.append((d["B"]["q975"] - d["B"]["q025"]) / 3.92)
    out["blocos"][name] = {"kc1": kc, "faixa_B": [lo, hi], "limiar_alt": alt, "na_faixa_B": bool(ok_b), "acima_alt": bool(ok_a),
                           "B_media": d["B"]["media"], "U_media": d["U"]["media"], "G_media": d["G"]["media"]}
n = len(obs)
ver = "sucesso" if (inB >= 27 and above >= 27) else ("falha do modelo B" if n - inB >= 6 else "inconclusivo")
mB = [np.mean([P[b][m]["media"] for b in P]) for m in ("B25", "B", "B75")]
sd_mean = math.sqrt(sum(s * s for s in sds)) / n
tol = 2 * sd_mean + 0.5 * (max(mB) - min(mB))
diff = float(np.mean(obs) - mB[1])
rho = spearmanr(obs, predB)
out["resumo"] = {"n_na_faixa_B": int(inB), "n_acima_alt": int(above), "veredito": ver,
                 "media_medida": float(np.mean(obs)), "media_B": mB[1], "medias_banda": mB, "diferenca": diff,
                 "tolerancia_agregada": tol, "agregado_compativel": bool(abs(diff) <= tol),
                 "spearman_rho": float(rho.statistic), "spearman_p": float(rho.pvalue), "segundos": round(time.time() - t0, 1)}
(OUT / "medicao.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print(json.dumps(out["resumo"], indent=1, ensure_ascii=False))
