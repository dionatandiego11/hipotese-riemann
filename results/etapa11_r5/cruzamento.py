"""
R5 — cruzamento descritivo com C2, conforme results/etapa11_r5/DECLARACAO_CRUZAMENTO.md (hash verificado).
Exploratório, classe B; sem testes de significância; sem alteração de critérios ou conclusões de m4.
"""
import csv, glob, hashlib, json, math, sys
import numpy as np
sys.path.insert(0, "src")
from riemann_spectra.periods import window_response, measure_window_response
from riemann_spectra.arithmetic import prime_power_catalog

for dfile in ["DECLARACAO", "DECLARACAO_CRUZAMENTO"]:
    raw = open(f"results/etapa11_r5/{dfile}.md", "rb").read()
    assert hashlib.sha256(raw).hexdigest() == open(f"results/etapa11_r5/{dfile}.sha256").read().split()[0], dfile

T_MIN, T_MAX, PTS, HALF_FWHM, TAU = 0.5, 5.0, 9, 0.5, 1e-6
U_LIST = [5.5, 6.0, 7.0, 8.0, 10.0]
runs = {"m4-v1": "results/run_20260913_144429_m3_b01*", "m4-v2": "results/run_20260913_173045_m3_c01*",
        "m4-v3": "results/run_20260913_220906_m3_d01*"}

def prime_powers_between(lo, hi):
    nmax = int(math.floor(math.exp(hi)))
    sieve = np.ones(nmax + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(nmax ** 0.5) + 1):
        if sieve[i]: sieve[i * i::i] = False
    out = []
    for p in np.nonzero(sieve)[0]:
        lp = math.log(p); pk = p; r = 1
        while pk <= nmax:
            if lo < r * lp <= hi: out.append((r * lp, -lp / (math.pi * p ** (r / 2.0))))
            pk *= p; r += 1
    return out

catalog = prime_power_catalog(T_MIN, T_MAX)
T = np.array([c["period_theoretical"] for c in catalog]); c_th = np.array([c["coefficient_theoretical"] for c in catalog]); K = len(T)
key = {(c["prime"], c["repetition"]): i for i, c in enumerate(catalog)}
extra = {U: prime_powers_between(T_MAX, U) for U in U_LIST}
rows = []
for ver, pat in runs.items():
    rd = glob.glob(pat)[0]
    metrics = json.load(open(rd + "/metrics.json"))
    for name, blk in metrics["blocks"].items():
        ins = blk["instrument"]; L = ins["B"] - ins["A"]; E_c = ins["E_c"]
        z_high = blk["arithmetic"]["threshold_interval"]["z_high"]; cm = blk["arithmetic"].get("clear_margin", 1.5)
        fwhm = measure_window_response(L, "hann")["fwhm"]; h = HALF_FWHM * fwhm
        t = np.unique(np.concatenate([np.linspace(Tk - h, Tk + h, PTS) for Tk in T]))
        ph = np.exp(1j * E_c * T)
        G = 0.5 * window_response(t[:, None] - T[None, :], L, "hann") * ph[None, :]
        H = 0.5 * window_response(t[:, None] + T[None, :], L, "hann") * np.conj(ph)[None, :]
        Mc = np.hstack([G + H, 1j * (G - H)]); M = np.vstack([Mc.real, Mc.imag])
        Us, s, Vt = np.linalg.svd(M, full_matrices=False)
        rank = int(np.sum(s > max(M.shape) * s[0] * np.finfo(float).eps)); assert rank == 2 * K
        Mp = (Vt.T / s) @ Us.T
        rx = Mp[:K, :]; l1 = np.sum(np.abs(rx), axis=1)
        elin = {}
        for U in U_LIST:
            rho = np.zeros(len(t), dtype=complex)
            for Tn, cn in extra[U]:
                rho += cn * 0.5 * (np.exp(1j * E_c * Tn) * window_response(t - Tn, L, "hann") + np.exp(-1j * E_c * Tn) * window_response(t + Tn, L, "hann"))
            elin[U] = (rx @ np.concatenate([rho.real, rho.imag])) / c_th
        tab = list(csv.DictReader(open(f"{rd}/tables/{name}/arithmetic_matches.csv")))
        assert len(tab) == K
        for x in tab:
            k = key[(int(x["prime"]), int(x["repetition"]))]
            assert abs(float(x["coefficient_theoretical"]) - c_th[k]) <= 1e-15 * abs(c_th[k])
            res = x["resolved"] == "True"; clr = x["clearly_detectable"] == "True"
            e_rec = float(x["fit_ratio_to_theory"]) - 1.0
            row = {"versao": ver, "bloco": name, "p": int(x["prime"]), "r": int(x["repetition"]), "T": T[k], "c": c_th[k],
                   "resolved": res, "clearly_detectable": clr, "eligible": res and clr,
                   "margin": float(x["z_predicted"]) / (cm * z_high), "e_rec": e_rec,
                   "escala_suficiente_F": TAU * abs(c_th[k]) / l1[k], "tau": TAU}
            for U in U_LIST:
                row[f"e_lin_U{U}"] = float(elin[U][k]); row[f"d_U{U}"] = e_rec - float(elin[U][k])
            rows.append(row)

with open("results/etapa11_r5/cruzamento_tabela.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader()
    for r in rows: w.writerow({k: (repr(v) if isinstance(v, float) else v) for k, v in r.items()})

summary = {"declaracoes": {"DECLARACAO": open("results/etapa11_r5/DECLARACAO.sha256").read().split()[0],
                           "DECLARACAO_CRUZAMENTO": open("results/etapa11_r5/DECLARACAO_CRUZAMENTO.sha256").read().split()[0]},
           "n_pares": len(rows), "grupos": {}}
for gname, sel in [("elegiveis", True), ("nao_elegiveis", False)]:
    G_ = [r for r in rows if r["eligible"] == sel]
    er = np.array([abs(r["e_rec"]) for r in G_])
    g = {"n_pares": len(G_), "n_blocos_com_linhas": len({(r["versao"], r["bloco"]) for r in G_}),
         "max_abs_e_rec": float(er.max()), "mediana_abs_e_rec": float(np.median(er)), "n_abs_e_rec_gt_tau": int(np.sum(er > TAU)), "por_U": {}}
    for U in U_LIST:
        el = np.array([r[f"e_lin_U{U}"] for r in G_]); dd = np.array([r[f"d_U{U}"] for r in G_]); ee = np.array([r["e_rec"] for r in G_])
        big = np.abs(el) > 1e-9
        g["por_U"][str(U)] = {"max_abs_e_lin": float(np.abs(el).max()), "mediana_abs_e_lin": float(np.median(np.abs(el))),
                              "n_abs_e_lin_gt_tau": int(np.sum(np.abs(el) > TAU)),
                              "max_abs_d": float(np.abs(dd).max()), "mediana_abs_d": float(np.median(np.abs(dd))), "n_abs_d_gt_tau": int(np.sum(np.abs(dd) > TAU)),
                              "concordancia_sinal_e_rec_e_lin(|e_lin|>1e-9)": f"{int(np.sum(np.sign(ee[big]) == np.sign(el[big])))}/{int(big.sum())}"}
    summary["grupos"][gname] = g
# pares com |e_lin(6)| > tau, listados
summary["pares_abs_e_lin_U6_gt_tau"] = [{k: r[k] for k in ["versao", "bloco", "p", "r", "eligible", "margin", "e_rec", "e_lin_U6.0", "d_U6.0"]}
                                        for r in rows if abs(r["e_lin_U6.0"]) > TAU]
json.dump(summary, open("results/etapa11_r5/cruzamento_resumo.json", "w"), indent=1)
print(json.dumps({k: v for k, v in summary.items() if k != "pares_abs_e_lin_U6_gt_tau"}, indent=1))
for p in summary["pares_abs_e_lin_U6_gt_tau"]:
    print(p)
