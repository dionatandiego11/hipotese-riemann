"""
Θ_k(U₂) = Σ_{U₁<log n≤U₂} χ(log n)c(n)Q_k(log n), conforme results/etapa11_r5/DECLARACAO_THETA.md (hash verificado).
Ponto flutuante de dupla precisão (classe B); erro numérico estimado, não certificado.
"""
import csv, glob, hashlib, json, math, sys
import numpy as np
sys.path.insert(0, "src")
from riemann_spectra.periods import window_response, measure_window_response
from riemann_spectra.arithmetic import prime_power_catalog

raw = open("results/etapa11_r5/DECLARACAO_THETA.md", "rb").read()
assert hashlib.sha256(raw).hexdigest() == open("results/etapa11_r5/DECLARACAO_THETA.sha256").read().split()[0]
TAU = 1e-6; DELTA_REL = 1e-9; EPS = np.finfo(float).eps
D1 = [1, 2, 4, 8]; DELTA = ["0.5", "1", "2"]; TMAX = 5.0
CHECK_COMB = [(8, "2"), (1, "0.5")]; CHECK_BLK = {("m4-v1", "b01"), ("m4-v2", "c01"), ("m4-v3", "d01")}

def W_closed(om, L):
    v = om*L/(2*math.pi)
    return -(L/(2*math.pi))*np.sin(math.pi*v)/(v*(v*v - 1))

def phi(x):
    x = np.asarray(x, float); out = np.zeros_like(x); out[x >= 1] = 1.0
    m = (x > 0) & (x < 1); a = np.exp(-1/x[m]); b = np.exp(-1/(1 - x[m])); out[m] = a/(a + b)
    return out

# potências de primo com 6 < log n ≤ 15
NMAX = int(math.exp(15.0)) + 1
sieve = np.ones(NMAX + 1, bool); sieve[:2] = False
for i in range(2, int(NMAX**0.5) + 1):
    if sieve[i]: sieve[i*i::i] = False
primes = np.nonzero(sieve)[0]
ns, lam = [], []
for p in primes:
    q = int(p)
    while q <= NMAX:
        ns.append(q); lam.append(math.log(p)); q *= int(p)
ns = np.array(ns, dtype=np.int64); lam = np.array(lam)
o = np.argsort(ns); ns = ns[o]; lam = lam[o]
logn = np.log(ns.astype(float)); sel = (logn > 6.0) & (logn <= 15.0)
ns, lam, logn = ns[sel], lam[sel], logn[sel]
cn = -lam/(math.pi*np.sqrt(ns.astype(float)))
assert np.all(np.abs(logn - np.log(ns.astype(float))) == 0)
print("potências de primo em (e^6, e^15]:", len(ns))

catalog = prime_power_catalog(0.5, 5.0); T = np.array([c["period_theoretical"] for c in catalog]); cth = np.array([c["coefficient_theoretical"] for c in catalog]); K = len(T)
runs = {"m4-v1": "results/run_20260913_144429_m3_b01*", "m4-v2": "results/run_20260913_173045_m3_c01*", "m4-v3": "results/run_20260913_220906_m3_d01*"}
elig = {(r["versao"], r["bloco"], int(r["p"]), int(r["r"])): r["eligible"] == "True" for r in csv.DictReader(open("results/etapa11_r5/cruzamento_tabela.csv"))}
Brel = {(r["versao"], r["bloco"], int(r["p"]), int(r["r"]), int(r["d1"]), r["Delta"]): float(r["B_rel_sup"]) for r in csv.DictReader(open("results/etapa11_r5/prh2_forca_tabela.csv"))}

def Qmat(Mp, t, Ec, L, u, W):
    out = np.empty((K, len(u)))
    for s0 in range(0, len(u), 4000):
        uu = u[s0:s0 + 4000]
        z = 0.5*(np.exp(1j*Ec*uu)[None, :]*W(t[:, None] - uu[None, :], L) + np.exp(-1j*Ec*uu)[None, :]*W(t[:, None] + uu[None, :], L))
        out[:, s0:s0 + 4000] = Mp[:K, :len(t)] @ z.real + Mp[:K, len(t):] @ z.imag
    return out

rows = []; check = []
w_ok = None
for ver, pat in runs.items():
    m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
    for name, blk in m["blocks"].items():
        ins = blk["instrument"]; L = ins["B"] - ins["A"]; Ec = ins["E_c"]
        if w_ok is None:
            om = np.linspace(7.0, 40.0, 1001); w_ok = float(np.max(np.abs(W_closed(om, L) - window_response(om, L))))
        h = 0.5*measure_window_response(L)["fwhm"]; t = np.unique(np.concatenate([np.linspace(x - h, x + h, 9) for x in T]))
        ph = np.exp(1j*Ec*T); G = 0.5*window_response(t[:, None] - T[None, :], L)*ph; H = 0.5*window_response(t[:, None] + T[None, :], L)*np.conj(ph)
        Mc = np.hstack([G + H, 1j*(G - H)]); M = np.vstack([Mc.real, Mc.imag]); U_, s, Vt = np.linalg.svd(M, full_matrices=False)
        assert int(np.sum(s > max(M.shape)*s[0]*EPS)) == 2*K
        Mp = (Vt.T/s) @ U_.T
        assert np.max(np.abs(t)) <= TMAX + h + 1e-12
        Q = Qmat(Mp, t, Ec, L, logn, W_closed)
        for d1 in D1:
            for Dl in DELTA:
                U1 = TMAX + d1; U2 = U1 + float(Dl)
                idx = (logn > U1) & (logn <= U2)
                wt = phi((logn[idx] - U1)/float(Dl))*cn[idx]
                terms = Q[:, idx]*wt[None, :]
                theta = terms.sum(axis=1); sabs = np.abs(terms).sum(axis=1)
                err = DELTA_REL*sabs + idx.sum()*EPS*np.abs(terms).max(axis=1)
                if (ver, name) in CHECK_BLK and (d1, Dl) in CHECK_COMB:
                    Q2 = Qmat(Mp, t, Ec, L, logn[idx], window_response)
                    th2 = (Q2*wt[None, :]).sum(axis=1)
                    check.append({"versao": ver, "bloco": name, "d1": d1, "Delta": Dl,
                                  "max_abs_dif": float(np.max(np.abs(th2 - theta))), "max_err_est": float(err.max()),
                                  "max_abs_dif_rel_c": float(np.max(np.abs(th2 - theta)/np.abs(cth)))})
                for k, c in enumerate(catalog):
                    ck = abs(cth[k]); key = (ver, name, c["prime"], c["repetition"])
                    b = Brel[key + (d1, Dl)]
                    rows.append({"versao": ver, "bloco": name, "p": c["prime"], "r": c["repetition"], "eligible": elig[key],
                                 "d1": d1, "Delta": Dl, "U1": U1, "U2": U2, "n_termos": int(idx.sum()), "abs_c": ck,
                                 "theta": float(theta[k]), "err_num_est": float(err[k]), "S_abs": float(sabs[k]),
                                 "theta_rel": float(theta[k]/ck), "margem": TAU*ck - abs(theta[k]),
                                 "margem_rel": TAU - abs(theta[k])/ck, "B_rel_sup": b,
                                 "orcamento_rel": b + abs(theta[k])/ck,
                                 "orcamento_rel_com_err": b + (abs(theta[k]) + err[k])/ck})
        print(ver, name, "ok", flush=True)

with open("results/etapa11_r5/theta_tabela.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

summ = {"tau": TAU, "delta_rel": DELTA_REL, "classe": "B (ponto flutuante; não certificado)",
        "max_dif_W_fechada_vs_window_response": w_ok, "checagem_consistencia": check, "por_U2": {}}
for d1 in D1:
    for Dl in DELTA:
        R = [r for r in rows if r["d1"] == d1 and r["Delta"] == Dl]; E = [r for r in R if r["eligible"]]
        def st(sub):
            tr = np.array([abs(r["theta_rel"]) for r in sub])
            return {"n": len(sub), "max_abs_theta_rel": float(tr.max()), "mediana_abs_theta_rel": float(np.median(tr)),
                    "max_S_abs_rel": max(r["S_abs"]/r["abs_c"] for r in sub),
                    "n_margem_pos": sum(r["margem"] > 0 for r in sub),
                    "n_margem_pos_com_err": sum(r["margem"] - r["err_num_est"] > 0 for r in sub),
                    "n_orcamento_le_tau": sum(r["orcamento_rel"] <= TAU for r in sub),
                    "n_orcamento_com_err_le_tau": sum(r["orcamento_rel_com_err"] <= TAU for r in sub),
                    "min_orcamento_rel": min(r["orcamento_rel"] for r in sub),
                    "mediana_orcamento_rel": float(np.median([r["orcamento_rel"] for r in sub])),
                    "max_err_rel": max(r["err_num_est"]/r["abs_c"] for r in sub)}
        summ["por_U2"][f"d1={d1},Delta={Dl}"] = {"U1": TMAX + d1, "U2": TMAX + d1 + float(Dl), "n_termos": R[0]["n_termos"], "todas": st(R), "elegiveis": st(E)}
json.dump(summ, open("results/etapa11_r5/theta_resumo.json", "w"), indent=1, default=lambda o: o.item())
print("W fechada vs window_response:", w_ok)
for c in check: print(c)
for k, v in summ["por_U2"].items():
    a, e = v["todas"], v["elegiveis"]
    print(f"{k} U2={v['U2']} nt={v['n_termos']} | |Θ|/|c| max {a['max_abs_theta_rel']:.3e} med {a['mediana_abs_theta_rel']:.3e} Sabs max {a['max_S_abs_rel']:.3e} | margem>0 {a['n_margem_pos']}/{a['n']} (eleg {e['n_margem_pos']}/{e['n']}) | orc<=tau {a['n_orcamento_le_tau']} (eleg {e['n_orcamento_le_tau']}) com err {a['n_orcamento_com_err_le_tau']} | min orc {a['min_orcamento_rel']:.3e} | err rel max {a['max_err_rel']:.1e}")
