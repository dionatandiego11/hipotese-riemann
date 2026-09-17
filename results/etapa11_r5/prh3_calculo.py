"""
Avaliação isolada do Lema 4′ (P-RH com Lema 5′), conforme results/etapa11_r5/DECLARACAO_PRH3.md (hash verificado).
Aritmética intervalar; ‖a_k‖₁ (SVD) e Θ_k em ponto flutuante (avaliação híbrida). Sem dados de zeros.
"""
import csv, glob, hashlib, json, sys
import numpy as np
from mpmath import iv, mpf
sys.path.insert(0, "results/etapa11_3b")
from interval_export import sup_str

raw = open("results/etapa11_r5/DECLARACAO_PRH3.md", "rb").read()
assert hashlib.sha256(raw).hexdigest() == open("results/etapa11_r5/DECLARACAO_PRH3.sha256").read().split()[0]
iv.dps = 30; TAU = 1e-6; TOL_EXPORT = 3e-12
_prev = json.load(open("results/etapa11_r5/prh_forca_resumo.json"))
c1 = iv.mpf(_prev["c1_sup"]); c2 = iv.mpf(_prev["c2_sup"])
EPS0 = iv.mpf("0.1"); TMAX = iv.mpf(5); PI = iv.pi; N6 = 31 + iv.mpf("10.5")*iv.log(13); LOG3 = iv.log(3)
runs = {"m4-v1": "results/run_20260913_144429_m3_b01*", "m4-v2": "results/run_20260913_173045_m3_c01*", "m4-v3": "results/run_20260913_220906_m3_d01*"}
D1 = [1, 2, 4, 8]; DELTA = ["0.5", "1", "2"]

def S1(J): return 1/iv.mpf(2*J - 1)**2 + 1/iv.mpf(2*(2*J - 1))
def sig(J):
    if J == 1: return LOG3/9 + (LOG3 + 1)/6
    y = iv.mpf(2*J - 1); return iv.log(y)/y**2 + (iv.log(y) + 1)/(2*y)
def S2(J): return LOG3*S1(J) + sig(J)

def unit_bound(L, nus, d1, Dl):
    """Partes com a = 1 (todas lineares em a)."""
    L = iv.mpf(L); d1 = iv.mpf(d1); Dl = iv.mpf(Dl)
    lam = L/(2*PI); kap = L/(8*PI); CP = 4*PI**2/L**2
    U1 = TMAX + d1; U2 = U1 + Dl; rho1 = 1 + TMAX/d1; L0 = CP/(2*d1**2)
    def mn(x, y): return iv.mpf(min(x.b, y.b))
    L2 = CP*( c2/Dl**2*mn(Dl/d1**3, 1/(2*d1**2)) + 24/d1**4 + 12*c1/Dl*mn(Dl/d1**4, 1/(3*d1**3))
             + EPS0**2*(1/(2*d1**2) + 2*c1*rho1/Dl*mn(Dl/d1**2, 1/d1) + 6*rho1/d1**2)
             + rho1**2*(1/(4*iv.e*d1**4) + EPS0**4*iv.sqrt(PI/2)) )
    ratio = (L2/L0).b
    J = 1
    while (2*J - 1)**2 < ratio: J += 1
    Arq = iv.exp(-U1/2)*(1 + 1/(1 - iv.exp(-U1)))*L0
    Z = iv.mpf(0); Zp = iv.mpf(0); Pol = iv.mpf(0)
    for nu in nus:
        nu = iv.mpf(nu); lg = iv.log(nu + 8)
        far = L2*(3*N6/(nu - 6)**2 + 2*N6/nu**2 + iv.mpf("5.25")*(iv.log(nu + 2) + 1)/(nu + 2))
        Z += 2*(iv.mpf("10.5")*lg*L0 + L2*21*(iv.mpf("1.5")*lg + 2*iv.sqrt(2)) + far)
        inner = sum((lg + iv.log(1 + 2*j) for j in range(1, J)), iv.mpf(0))
        Zp += 2*(iv.mpf("10.5")*lg*L0 + 21*(L0*inner + L2*(lg*S1(J) + S2(J))) + far)
        s2 = U2 - TMAX
        Pol += (iv.exp(-U1/2)*L0
                + iv.exp(U2/2)*(CP/s2**3/nu + (EPS0**2*U2*CP/s2**3 + 6*CP/s2**4 + L2)/nu**2)
                + 2*kap*(4*iv.exp(U2/2)/(nu*(lam*s2)**3) + 2*iv.sqrt(2*PI)*(lam*nu)**(-3)*EPS0**5*iv.exp(-(nu**2 - iv.mpf(1)/4)/(2*EPS0**2))))
    return {"Z": Z/2/PI, "Zp": Zp/2/PI, "Pol": Pol/PI, "Arq": 2*Arq/2/PI, "J": J}
# nota: (1/π)Σ_ν ½[Z_ν + 2Pol_ν + Arq] = (1/π)[Σ Z_ν/2 + Σ Pol_ν + Arq] (Arq somado duas vezes com peso ½)

prh2 = {(r["versao"], r["bloco"], int(r["p"]), int(r["r"]), int(r["d1"]), r["Delta"]): r for r in csv.DictReader(open("results/etapa11_r5/prh2_forca_tabela.csv"))}
theta = {(r["versao"], r["bloco"], int(r["p"]), int(r["r"]), int(r["d1"]), r["Delta"]): r for r in csv.DictReader(open("results/etapa11_r5/theta_tabela.csv"))}
def up(x): return float(mpf(x.b))
rows = []; dev_z = [0.0, 0.0]; dev_b = [0.0, 0.0]; zp_le_z = True
for ver, pat in runs.items():
    m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
    for name, blk in m["blocks"].items():
        ins = blk["instrument"]; L = ins["B"] - ins["A"]
        for d1 in D1:
            for Dl in DELTA:
                u = unit_bound(repr(L), [repr(ins["A"]), repr(ins["B"])], d1, Dl)
                for key in [k for k in prh2 if k[0] == ver and k[1] == name and k[4] == d1 and k[5] == Dl]:
                    r = prh2[key]; a = iv.mpf(r["a_l1"]); ck = float(r["abs_c"])
                    z = u["Z"]*a/ck; zp = u["Zp"]*a/ck; p = u["Pol"]*a/ck; ar = u["Arq"]*a/ck
                    B = z + p + ar; Bp = zp + p + ar
                    for dev, rec, tab in ((dev_z, up(z), float(r["zeros_rel_sup"])), (dev_b, up(B), float(r["B_rel_sup"]))):
                        dev[0] = min(dev[0], tab - rec); dev[1] = max(dev[1], tab - rec)
                    if zp.b > z.b: zp_le_z = False
                    th = abs(float(theta[key]["theta"]))/ck
                    Bp_s = float(sup_str(Bp, 15))
                    rows.append({"versao": ver, "bloco": name, "p": key[2], "r": key[3], "eligible": r["eligible"], "d1": d1, "Delta": Dl,
                                 "J": u["J"], "zeros_rel_sup": float(sup_str(zp, 15)), "razao_Zp_Z": up(zp)/up(z),
                                 "polos_rel_sup": float(sup_str(p, 15)), "arq_rel_sup": float(sup_str(ar, 15)),
                                 "B2_rel_sup": Bp_s, "theta_rel": th, "orcamento2": Bp_s + th,
                                 "orcamento_anterior": float(theta[key]["orcamento_rel"])})
    print(ver, "ok", flush=True)

conf = {"dev_zeros_tab_menos_rec": dev_z, "dev_B_tab_menos_rec": dev_b, "tol": TOL_EXPORT, "Zp_le_Z": zp_le_z}
conf["conferencia1_ok"] = all(-1e-15 <= d[0] and d[1] <= TOL_EXPORT for d in (dev_z, dev_b))
conf["conferencia2_ok"] = zp_le_z
print("conferências:", conf, flush=True)
with open("results/etapa11_r5/prh3_tabela.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
summ = {"conferencias": conf, "tau": TAU, "combinacoes": {}}
if conf["conferencia1_ok"] and conf["conferencia2_ok"]:
    for d1 in D1:
        for Dl in DELTA:
            R = [r for r in rows if r["d1"] == d1 and r["Delta"] == Dl]; E = [r for r in R if r["eligible"] == "True"]
            o = np.array([r["orcamento2"] for r in R])
            summ["combinacoes"][f"d1={d1},Delta={Dl}"] = {
                "J": sorted(set(r["J"] for r in R)), "razao_Zp_Z": [min(r["razao_Zp_Z"] for r in R), max(r["razao_Zp_Z"] for r in R)],
                "orcamento2": {"max": float(o.max()), "min": float(o.min()), "mediana": float(np.median(o))},
                "orcamento2_elegiveis": {"max": max(r["orcamento2"] for r in E), "mediana": float(np.median([r["orcamento2"] for r in E]))},
                "n_le_tau": {"todas": sum(r["orcamento2"] <= TAU for r in R), "elegiveis": sum(r["orcamento2"] <= TAU for r in E)},
                "n_le_tau_anterior": {"todas": sum(r["orcamento_anterior"] <= TAU for r in R), "elegiveis": sum(r["orcamento_anterior"] <= TAU for r in E)},
                "polos_rel_max": max(r["polos_rel_sup"] for r in R), "zeros_fracao_min": min(r["zeros_rel_sup"]/r["orcamento2"] for r in R)}
    best = {}
    for r in rows:
        k = (r["versao"], r["bloco"], r["p"], r["r"])
        if k not in best or r["orcamento2"] < best[k]["orcamento2"]: best[k] = r
    bv = list(best.values())
    from collections import Counter
    summ["minimo_sobre_grade"] = {
        "todas": {"n": len(bv), "n_le_tau": sum(r["orcamento2"] <= TAU for r in bv), "max": max(r["orcamento2"] for r in bv)},
        "elegiveis": {"n": sum(r["eligible"] == "True" for r in bv), "n_le_tau": sum(r["orcamento2"] <= TAU for r in bv if r["eligible"] == "True"),
                      "max": max(r["orcamento2"] for r in bv if r["eligible"] == "True"),
                      "mediana": float(np.median([r["orcamento2"] for r in bv if r["eligible"] == "True"])),
                      "por_versao_le_tau": dict(Counter(r["versao"] for r in bv if r["eligible"] == "True" and r["orcamento2"] <= TAU))},
        "combinacoes_no_minimo": {f"{c[0]},{c[1]}": n for c, n in Counter((r["d1"], r["Delta"]) for r in bv).items()}}
json.dump(summ, open("results/etapa11_r5/prh3_resumo.json", "w"), indent=1, default=lambda o: o.item())
if summ["combinacoes"]:
    for k, v in summ["combinacoes"].items():
        print(k, "J", v["J"], "Z'/Z %.3f-%.3f" % tuple(v["razao_Zp_Z"]), "orc max %.3e min %.3e | <=tau %s (antes %s) | polos max %.2e zeros frac min %.4f" % (v["orcamento2"]["max"], v["orcamento2"]["min"], v["n_le_tau"], v["n_le_tau_anterior"], v["polos_rel_max"], v["zeros_fracao_min"]))
    print(json.dumps(summ["minimo_sobre_grade"], indent=1))
