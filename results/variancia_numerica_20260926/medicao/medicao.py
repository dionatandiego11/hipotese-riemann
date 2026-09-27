"""
Medição VN-1 (FICHA_VARIANCIA_NUMERICA.md, congelada antes desta execução). Critérios da ficha §6, sem alteração.
Para a alternativa "todos os primos" em Q3, usa-se a mesma incerteza de modelo m(L) da previsão correta
(só τ* = 0,5 foi calculado para ela).
"""
import json, math, time, hashlib
from pathlib import Path
import numpy as np
from scipy.special import loggamma
from riemann_spectra.number_variance import number_variance
from riemann_spectra.unfolding import n_bar_theta

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).parent
P = json.loads((OUT.parent / "previsao" / "previsao.json").read_text())
L = np.array(P["L"]); G = np.array(P["gue"])
sha = lambda f: hashlib.sha256(Path(f).read_bytes()).hexdigest()
t0 = time.time()

def band(d, key):
    b = np.array(d[f"{key}0.5"])
    return b, np.maximum(abs(np.array(d[f"{key}0.25"]) - b), abs(np.array(d[f"{key}0.75"]) - b))

def zs(V, sig, pred, m):
    return (V - pred) / np.sqrt(sig**2 + m**2)

rms = lambda z: float(np.sqrt(np.mean(z**2)))
out = {"ficha_sha256": sha(ROOT / "hipoteses/FICHA_VARIANCIA_NUMERICA.md"), "L": L.tolist(), "zeta": {}, "chi": {}}

# --- ζ ---
zf = ROOT / "data/processed/zeros_100k.csv"
gam = np.loadtxt(zf, delimiter=",", skiprows=1)[:, 1]
out["zeta_arquivo"] = {"arquivo": str(zf.relative_to(ROOT)), "sha256": sha(zf), "n": len(gam)}
dp10 = np.array(P["ruido_gue"]["10000"]["dp_replicas"])
for b in range(10):
    name = f"b{b+1:02d}"
    x = n_bar_theta(gam[10000 * b:10000 * (b + 1)])
    r = number_variance(x, L)
    sig = np.maximum(r["sigma"], dp10)
    B, m = band(P["zeta"][name], "berry_tau")
    zB, zG = zs(r["V"], sig, B, m), zs(r["V"], sig, G, 0 * m)
    out["zeta"][name] = {"V": r["V"].tolist(), "sigma_sub": r["sigma"].tolist(), "sigma_eff": sig.tolist(),
                         "vies_medio": r["bias"].tolist(), "berry": B.tolist(), "m": m.tolist(),
                         "z_berry": zB.tolist(), "z_gue": zG.tolist(), "rms_berry": rms(zB), "rms_gue": rms(zG)}
prim = [f"b{i:02d}" for i in range(2, 11)]
ok = sum(out["zeta"][b]["rms_berry"] <= 2 and out["zeta"][b]["rms_gue"] >= 4 for b in prim)
bad = sum(out["zeta"][b]["rms_berry"] > 3 for b in prim)
out["Q1"] = {"blocos_sucesso": ok, "blocos_berry_gt3": bad,
             "veredito": "sucesso" if ok >= 8 else ("falha de Berry nesta altura" if bad >= 5 else "inconclusivo")}

# --- χ ---
chars = {"chi_m4": ("zeros_chi_m4_12000_completo.txt", 4, 1, [1.5, 2, 3, 4, 5, 6]),
         "chi_5": ("zeros_chi_5_12000_completo.txt", 5, 0, [1, 1.5, 2])}
dp3 = np.array(P["ruido_gue"]["3000"]["dp_replicas"])
for name, (fn, q, kappa, R) in chars.items():
    f = ROOT / "results/etapa11_6_controles/dirichlet/completude" / fn
    g = np.loadtxt(f)[:3000]          # corte imediato: blocos reservados não entram em cálculo algum
    a = 0.25 + 0.5 * kappa
    x = (np.imag(loggamma(a + 0.5j * g)) + 0.5 * g * math.log(q / math.pi)) / math.pi
    r = number_variance(x, L)
    sig = np.maximum(r["sigma"], dp3)
    d = P["chi"][name]
    Bc, m = band(d, "berry_chi_tau")
    Ba = np.array(d["berry_todos_primos_tau0.5"])
    zc, za, zG = zs(r["V"], sig, Bc, m), zs(r["V"], sig, Ba, m), zs(r["V"], sig, G, 0 * m)
    idx = [int(np.where(np.isclose(L, v))[0][0]) for v in R]
    dchi2 = float(np.sum(za[idx] ** 2 - zc[idx] ** 2))
    ver = "conjunto correto preferido" if dchi2 >= 9 else ("conjunto errado preferido" if dchi2 <= -9 else "inconclusivo")
    out["chi"][name] = {"arquivo": str(f.relative_to(ROOT)), "sha256_arquivo": sha(f), "n_usado": len(g),
                        "V": r["V"].tolist(), "sigma_eff": sig.tolist(), "vies_medio": r["bias"].tolist(),
                        "berry_correto": Bc.tolist(), "berry_todos": Ba.tolist(), "m": m.tolist(),
                        "z_correto": zc.tolist(), "z_todos": za.tolist(), "z_gue": zG.tolist(),
                        "R": R, "delta_chi2": dchi2, "rms_correto": rms(zc), "rms_todos": rms(za), "rms_gue": rms(zG),
                        "veredito": ver, "concordancia_quantitativa": rms(zc) <= 2}
out["segundos"] = round(time.time() - t0, 1)
(OUT / "medicao.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print(json.dumps({"Q1": out["Q1"], **{k: {kk: v[kk] for kk in ("delta_chi2", "rms_correto", "rms_todos", "rms_gue", "veredito")}
                                        for k, v in out["chi"].items()}, "segundos": out["segundos"]}, indent=1, ensure_ascii=False))
