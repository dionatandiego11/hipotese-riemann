"""
Decomposição da majorante Z_ν (Lema 4) conforme results/etapa11_r5/DECLARACAO_ZDEC.md (hash verificado).
Mesmos parâmetros de PRH2; aritmética intervalar; ‖a_k‖₁ em ponto flutuante (híbrida). Sem dados de zeros nem de C2.
"""
import csv, glob, hashlib, json, sys
import numpy as np
from mpmath import iv
sys.path.insert(0, "results/etapa11_3b")
from interval_export import sup_str

raw = open("results/etapa11_r5/DECLARACAO_ZDEC.md", "rb").read()
assert hashlib.sha256(raw).hexdigest() == open("results/etapa11_r5/DECLARACAO_ZDEC.sha256").read().split()[0]
iv.dps = 30; TAU = 1e-6
_prev = json.load(open("results/etapa11_r5/prh_forca_resumo.json"))
c1 = iv.mpf(_prev["c1_sup"]); c2 = iv.mpf(_prev["c2_sup"])
EPS0 = iv.mpf("0.1"); TMAX = iv.mpf(5); PI = iv.pi; N6 = 31 + iv.mpf("10.5")*iv.log(13)
runs = {"m4-v1": "results/run_20260913_144429_m3_b01*", "m4-v2": "results/run_20260913_173045_m3_c01*", "m4-v3": "results/run_20260913_220906_m3_d01*"}
PARTS = ["P0", "P1a", "P1b", "P2", "P3"]

def parts_unit(L, nus, d1, Dl):
    """Partes de (1/π)Σ_ν Z_ν/2 com a = 1 (L₀, L₂ ∝ a)."""
    L = iv.mpf(L); d1 = iv.mpf(d1); Dl = iv.mpf(Dl)
    CP = 4*PI**2/L**2; rho1 = 1 + TMAX/d1; L0 = CP/(2*d1**2)
    def mn(x, y): return iv.mpf(min(x.b, y.b))
    L2 = CP*( c2/Dl**2*mn(Dl/d1**3, 1/(2*d1**2)) + 24/d1**4 + 12*c1/Dl*mn(Dl/d1**4, 1/(3*d1**3))
             + EPS0**2*(1/(2*d1**2) + 2*c1*rho1/Dl*mn(Dl/d1**2, 1/d1) + 6*rho1/d1**2)
             + rho1**2*(1/(4*iv.e*d1**4) + EPS0**4*iv.sqrt(PI/2)) )
    P = {k: iv.mpf(0) for k in PARTS}
    for nu in nus:
        nu = iv.mpf(nu); lg = iv.log(nu + 8)
        P["P0"] += iv.mpf("10.5")*lg*L0
        P["P1a"] += 21*(lg + iv.log(3))*L2
        P["P1b"] += 21*(lg/2 + 2*iv.sqrt(2) - iv.log(3))*L2
        P["P2"] += 3*N6/(nu - 6)**2*L2
        P["P3"] += (2*N6/nu**2 + iv.mpf("5.25")*(iv.log(nu + 2) + 1)/(nu + 2))*L2
    return {k: v/PI for k, v in P.items()}, L0, L2

prh2 = {(r["versao"], r["bloco"], int(r["p"]), int(r["r"]), int(r["d1"]), r["Delta"]): r for r in csv.DictReader(open("results/etapa11_r5/prh2_forca_tabela.csv"))}
theta = {(r["versao"], r["bloco"], int(r["p"]), int(r["r"]), int(r["d1"]), r["Delta"]): r for r in csv.DictReader(open("results/etapa11_r5/theta_tabela.csv"))}
rows = []; maxdev = 0.0; maxabs = 0.0
for ver, pat in runs.items():
    m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
    for name, blk in m["blocks"].items():
        ins = blk["instrument"]; L = ins["B"] - ins["A"]
        for d1 in [1, 2, 4, 8]:
            for Dl in ["0.5", "1", "2"]:
                Pu, L0, L2 = parts_unit(repr(L), [repr(ins["A"]), repr(ins["B"])], d1, Dl)
                keys = [k for k in prh2 if k[0] == ver and k[1] == name and k[4] == d1 and k[5] == Dl]
                for key in keys:
                    r = prh2[key]; a = iv.mpf(r["a_l1"]); ck = float(r["abs_c"])
                    vals = {k: float(sup_str(Pu[k]*a/ck, 12)) for k in PARTS}
                    tot = sum(vals.values()); zr = float(r["zeros_rel_sup"])
                    maxdev = max(maxdev, abs(tot - zr)/zr); maxabs = max(maxabs, abs(tot - zr))
                    row = {"versao": ver, "bloco": name, "p": key[2], "r": key[3], "eligible": r["eligible"], "d1": d1, "Delta": Dl,
                           "L2_sobre_L0": float(sup_str(L2/L0, 8)), "zeros_rel_sup": zr,
                           "orcamento_rel": float(theta[key]["orcamento_rel"])}
                    for k in PARTS:
                        row[k + "_rel"] = vals[k]; row["fr_" + k] = vals[k]/tot
                    row["fr_proximos"] = (vals["P0"] + vals["P1a"])/tot; row["fr_distantes"] = 1 - row["fr_proximos"]
                    row["fr_L0"] = vals["P0"]/tot; row["fr_L2"] = 1 - row["fr_L0"]
                    rows.append(row)
    print(ver, "ok", flush=True)
# Conferência declarada (desvio relativo < 1e-9) NÃO satisfeita: a tabela PRH2 exporta sup com 12 casas decimais (+1 unidade),
# granularidade até 2e-12 por valor. Conferência posterior à declaração (registrada como desvio): |Σ partes − zeros_rel_sup| ≤ 6×2e-12.
DECL_OK = maxdev < 1e-9
assert maxabs <= 12e-12, maxabs
with open("results/etapa11_r5/zdec_tabela.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
FR = ["fr_" + k for k in PARTS] + ["fr_proximos", "fr_distantes", "fr_L0", "fr_L2"]
def stats(sub):
    return {"n": len(sub), "L2_sobre_L0": [min(r["L2_sobre_L0"] for r in sub), max(r["L2_sobre_L0"] for r in sub)],
            **{f: [min(r[f] for r in sub), max(r[f] for r in sub)] for f in FR},
            "zeros_rel_sobre_orcamento_min": min(r["zeros_rel_sup"]/r["orcamento_rel"] for r in sub)}
summ = {"conferencia_declarada_rel_1e-9_satisfeita": DECL_OK, "conferencia_max_desvio_rel": maxdev, "conferencia_posterior_max_desvio_abs": maxabs, "conferencia_posterior_limite_abs": 12e-12, "combinacoes": {}}
for d1 in [1, 2, 4, 8]:
    for Dl in ["0.5", "1", "2"]:
        R = [r for r in rows if r["d1"] == d1 and r["Delta"] == Dl]
        summ["combinacoes"][f"d1={d1},Delta={Dl}"] = {"todas": stats(R)}
Rx = [r for r in rows if r["d1"] == 8 and r["Delta"] == "2" and r["eligible"] == "True" and r["orcamento_rel"] > TAU]
summ["elegiveis_acima_tau_8_2"] = stats(Rx)
json.dump(summ, open("results/etapa11_r5/zdec_resumo.json", "w"), indent=1)
print("desvio rel max", maxdev, "declarada ok", DECL_OK, "desvio abs max", maxabs)
for k, v in summ["combinacoes"].items():
    t = v["todas"]; print(k, "L2/L0 %.2f" % t["L2_sobre_L0"][0], " ".join("%s %.3f-%.3f" % (f[3:], *t[f]) for f in FR))
t = summ["elegiveis_acima_tau_8_2"]; print("eleg>tau (8,2) n", t["n"], " ".join("%s %.3f-%.3f" % (f[3:], *t[f]) for f in FR), "zeros/orc min %.4f" % t["zeros_rel_sobre_orcamento_min"])
