"""
Avaliação da força da cota P-RH conforme results/etapa11_r5/DECLARACAO_PRH.md (hash verificado). Sem dados de zeros.
a_k em ponto flutuante (B); aritmética da cota intervalar (mpmath.iv), exportação arredondada para fora.
"""
import csv, glob, hashlib, json, math, sys
import numpy as np
from mpmath import iv
sys.path.insert(0, "src"); sys.path.insert(0, "results/etapa11_3b")
from riemann_spectra.periods import window_response, measure_window_response
from riemann_spectra.arithmetic import prime_power_catalog
from interval_export import sup_str

raw = open("results/etapa11_r5/DECLARACAO_PRH.md", "rb").read()
assert hashlib.sha256(raw).hexdigest() == open("results/etapa11_r5/DECLARACAO_PRH.sha256").read().split()[0]
iv.dps = 30
TAU = 1e-6

# ---- c1, c2 por enclosure intervalar ----
def f(x): return iv.exp(-1/x)
def f1(x): return iv.exp(-1/x) / x**2
def f2(x): return iv.exp(-1/x) * (1 - 2*x) / x**4
delta = iv.mpf("0.01"); NSUB = 20000
c1 = iv.mpf(0); c2 = iv.mpf(0)
a0 = iv.mpf("0.01"); step = (iv.mpf(1) - 2*a0) / NSUB
for i in range(NSUB):
    x = iv.mpf([(a0 + step*i).a, (a0 + step*(i+1)).b])
    y = 1 - x
    S = f(x) + f(y); N = f1(x)*f(y) + f(x)*f1(y); Np = f2(x)*f(y) - f(x)*f2(y); Sp = f1(x) - f1(y)
    d1 = N / S**2; d2 = (Np*S - 2*N*Sp) / S**3
    c1 = iv.mpf(max(c1.b, abs(d1).b)); c2 = iv.mpf(max(c2.b, abs(d2).b))
# pontas (0, δ] (e simétrica): cotas grosseiras
fmax = iv.exp(-1/delta); f1max = iv.exp(-1/delta)/delta**2; f2max = iv.exp(-1/delta)/delta**4
gmin = iv.exp(-1/(1-delta)); hmax = iv.exp(-1)/(1-delta)**2; h2max = iv.exp(-1)*(1+2)/(1-delta)**4  # |f''(1-x)| ≤ e^{-1/(1-x)}|1-2(1-x)|/(1-x)^4 ≤ 3e^{-1}/(1-δ)^4
Nb = f1max*1 + fmax*hmax; Npb = f2max*1 + fmax*h2max; Spb = f1max + hmax
tip1 = Nb / gmin**2; tip2 = Npb/gmin**2 + 2*Nb*Spb/gmin**3
c1 = iv.mpf(max(c1.b, tip1.b)); c2 = iv.mpf(max(c2.b, tip2.b))
print("c1 <=", sup_str(c1, 6), " c2 <=", sup_str(c2, 6))

catalog = prime_power_catalog(0.5, 5.0); T = np.array([c["period_theoretical"] for c in catalog]); cth = np.array([c["coefficient_theoretical"] for c in catalog]); K = len(T)
runs = {"m4-v1": "results/run_20260913_144429_m3_b01*", "m4-v2": "results/run_20260913_173045_m3_c01*", "m4-v3": "results/run_20260913_220906_m3_d01*"}
elig = {(r["versao"], r["bloco"], int(r["p"]), int(r["r"])): r["eligible"] == "True" for r in csv.DictReader(open("results/etapa11_r5/cruzamento_tabela.csv"))}
D1 = [1, 2, 4, 8]; DELTA = ["0.5", "1", "2"]; EPS0 = iv.mpf("0.1"); TMAX = iv.mpf(5)
N6 = 31 + iv.mpf("10.5")*iv.log(13); PI = iv.pi

def bound(a, L, nus, d1, Dl):
    a = iv.mpf(a); L = iv.mpf(L); d1 = iv.mpf(d1); Dl = iv.mpf(Dl)
    lam = L/(2*PI); kap = L/(8*PI); CP = 4*PI**2*a/L**2
    U1 = TMAX + d1; U2 = U1 + Dl; rho1 = 1 + TMAX/d1
    L0 = CP/(2*d1**2)
    def mn(x, y): return iv.mpf(min(x.b, y.b))  # cota superior do mínimo
    L2 = CP*( c2/Dl**2*mn(Dl/d1**3, 1/(2*d1**2)) + 24/d1**4 + 12*c1/Dl*mn(Dl/d1**4, 1/(3*d1**3))
             + EPS0**2*(1/(2*d1**2) + 2*c1*rho1/Dl*mn(Dl/d1**2, 1/d1) + 6*rho1/d1**2)
             + rho1**2*(1/(4*iv.e*d1**4) + EPS0**4*iv.sqrt(PI/2)) )
    Arq = iv.exp(-U1/2)*(1 + 1/(1 - iv.exp(-U1)))*L0
    zeros = iv.mpf(0); poles = iv.mpf(0)
    for nu in nus:
        nu = iv.mpf(nu)
        nnu = iv.mpf("10.5")*iv.log(nu + 8)
        Z = 2*(nnu*L0 + L2*(21*(iv.mpf("1.5")*iv.log(nu + 8) + 2*iv.sqrt(2)) + 3*N6/(nu - 6)**2 + 2*N6/nu**2 + iv.mpf("5.25")*(iv.log(nu + 2) + 1)/(nu + 2)))
        Pol = (iv.exp(-U1/2) + iv.exp(U2/2))*L0 + 2*kap*a*(4*iv.exp(U2/2)/(nu*(lam*(U2 - TMAX))**3) + 2*iv.sqrt(2*PI)*(lam*nu)**(-3)*EPS0**5*iv.exp(-(nu**2 - iv.mpf(1)/4)/(2*EPS0**2)))
        zeros += Z/2; poles += Pol
    zeros /= PI; poles /= PI; arq = Arq/PI
    return zeros, poles, arq, zeros + poles + arq, L0, L2

rows = []
for ver, pat in runs.items():
    m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
    for name, blk in m["blocks"].items():
        ins = blk["instrument"]; L = ins["B"] - ins["A"]; Ec = ins["E_c"]
        assert all(d >= math.sqrt(2)*2*math.pi/L for d in D1)
        h = 0.5*measure_window_response(L)["fwhm"]; t = np.unique(np.concatenate([np.linspace(x - h, x + h, 9) for x in T]))
        ph = np.exp(1j*Ec*T); G = 0.5*window_response(t[:, None] - T[None, :], L)*ph; H = 0.5*window_response(t[:, None] + T[None, :], L)*np.conj(ph)
        Mc = np.hstack([G + H, 1j*(G - H)]); M = np.vstack([Mc.real, Mc.imag]); U_, s, Vt = np.linalg.svd(M, full_matrices=False)
        assert int(np.sum(s > max(M.shape)*s[0]*np.finfo(float).eps)) == 2*K
        Mp = (Vt.T/s) @ U_.T; a_norm = np.sum(np.abs(Mp[:K, :]), axis=1)
        for k, c in enumerate(catalog):
            for d1 in D1:
                for Dl in DELTA:
                    z, p, ar, B, L0, L2 = bound(repr(float(a_norm[k])), repr(L), [repr(ins["A"]), repr(ins["B"])], d1, Dl)
                    ck = abs(cth[k])
                    rows.append({"versao": ver, "bloco": name, "p": c["prime"], "r": c["repetition"], "eligible": elig[(ver, name, c["prime"], c["repetition"])],
                                 "d1": d1, "Delta": Dl, "a_l1": float(a_norm[k]), "abs_c": ck,
                                 "zeros_rel_sup": float(sup_str(z/ck, 12)), "polos_rel_sup": float(sup_str(p/ck, 12)),
                                 "arq_rel_sup": float(sup_str(ar/ck, 12)), "B_rel_sup": float(sup_str(B/ck, 12)),
                                 "B_rel_sup_str": sup_str(B/ck, 12)})
with open("results/etapa11_r5/prh_forca_tabela.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

summ = {"c1_sup": sup_str(c1, 6), "c2_sup": sup_str(c2, 6), "tau": TAU, "combinacoes": {}}
for d1 in D1:
    for Dl in DELTA:
        R = [r for r in rows if r["d1"] == d1 and r["Delta"] == Dl]
        def mm(key, sub): 
            v = [r[key] for r in sub]; return {"max": max(v), "min": min(v)}
        summ["combinacoes"][f"d1={d1},Delta={Dl}"] = {
            "todas": {k: mm(k, R) for k in ["zeros_rel_sup", "polos_rel_sup", "arq_rel_sup", "B_rel_sup"]},
            "elegiveis": {k: mm(k, [r for r in R if r["eligible"]]) for k in ["zeros_rel_sup", "polos_rel_sup", "arq_rel_sup", "B_rel_sup"]},
            "n_pares_B_le_tau": sum(r["B_rel_sup"] <= TAU for r in R)}
best = {}
for r in rows:
    key = (r["versao"], r["bloco"], r["p"], r["r"])
    if key not in best or r["B_rel_sup"] < best[key]["B_rel_sup"]:
        best[key] = r
bv = list(best.values())
summ["minimo_sobre_grade"] = {
    "todas": {"max_B_rel": max(r["B_rel_sup"] for r in bv), "min_B_rel": min(r["B_rel_sup"] for r in bv), "n_le_tau": sum(r["B_rel_sup"] <= TAU for r in bv), "n": len(bv)},
    "elegiveis": {"max_B_rel": max(r["B_rel_sup"] for r in bv if r["eligible"]), "min_B_rel": min(r["B_rel_sup"] for r in bv if r["eligible"]),
                  "n_le_tau": sum(r["B_rel_sup"] <= TAU for r in bv if r["eligible"]), "n": sum(r["eligible"] for r in bv)},
    "combinacao_mais_frequente_no_minimo": max(set((r["d1"], r["Delta"]) for r in bv), key=lambda c: sum((r["d1"], r["Delta"]) == c for r in bv))}
json.dump(summ, open("results/etapa11_r5/prh_forca_resumo.json", "w"), indent=1)
print(json.dumps(summ["minimo_sobre_grade"], indent=1, default=str))
for k, v in summ["combinacoes"].items():
    print(k, "B max %.3e min %.3e | zeros max %.3e polos max %.3e arq max %.3e | n<=tau %d" % (v["todas"]["B_rel_sup"]["max"], v["todas"]["B_rel_sup"]["min"], v["todas"]["zeros_rel_sup"]["max"], v["todas"]["polos_rel_sup"]["max"], v["todas"]["arq_rel_sup"]["max"], v["n_pares_B_le_tau"]))
