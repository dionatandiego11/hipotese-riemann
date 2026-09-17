"""
R5 — cálculo finito do estimador direcionado primário (band_conjugate), conforme results/etapa11_r5/DECLARACAO.md
(SHA-256 em DECLARACAO.sha256, gravada antes desta execução). Classe B; sem dados de zeros.
"""
import glob, hashlib, json, math, sys
import numpy as np
sys.path.insert(0, "src")
from riemann_spectra.periods import window_response, measure_window_response
from riemann_spectra.arithmetic import prime_power_catalog

decl = open("results/etapa11_r5/DECLARACAO.md", "rb").read()
assert hashlib.sha256(decl).hexdigest() == open("results/etapa11_r5/DECLARACAO.sha256").read().split()[0], "declaração alterada"

T_MIN, T_MAX, PTS, HALF_FWHM = 0.5, 5.0, 9, 0.5
U_LIST = [5.5, 6.0, 7.0, 8.0, 10.0]
TAU = 1e-6
runs = {"m4-v1": "results/run_20260913_144429_m3_b01*", "m4-v2": "results/run_20260913_173045_m3_c01*",
        "m4-v3": "results/run_20260913_220906_m3_d01*"}

def prime_powers_between(lo, hi):
    nmax = int(math.floor(math.exp(hi)))
    sieve = np.ones(nmax + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(nmax ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    out = []
    for p in np.nonzero(sieve)[0]:
        lp = math.log(p); pk = p; r = 1
        while pk <= nmax:
            if lo < r * lp <= hi:
                out.append((r * lp, -lp / (math.pi * p ** (r / 2.0))))
            pk *= p; r += 1
    return out

catalog = prime_power_catalog(T_MIN, T_MAX)
T = np.array([c["period_theoretical"] for c in catalog]); c_th = np.array([c["coefficient_theoretical"] for c in catalog])
K = len(T)
extra = {U: prime_powers_between(T_MAX, U) for U in U_LIST}
results = {"declaracao_sha256": hashlib.sha256(decl).hexdigest(), "K": K, "U_list": U_LIST,
           "n_linhas_extra_por_U": {str(U): len(extra[U]) for U in U_LIST}, "blocos": []}

for ver, pat in runs.items():
    metrics = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
    for name, blk in metrics["blocks"].items():
        ins = blk["instrument"]; L = ins["B"] - ins["A"]; E_c = ins["E_c"]
        fwhm = measure_window_response(L, "hann")["fwhm"]; h = HALF_FWHM * fwhm
        t = np.unique(np.concatenate([np.linspace(Tk - h, Tk + h, PTS) for Tk in T]))
        J = len(t)
        ph = np.exp(1j * E_c * T)
        G = 0.5 * window_response(t[:, None] - T[None, :], L, "hann") * ph[None, :]
        H = 0.5 * window_response(t[:, None] + T[None, :], L, "hann") * np.conj(ph)[None, :]
        Mc = np.hstack([G + H, 1j * (G - H)])
        M = np.vstack([Mc.real, Mc.imag])                                   # 2J × 2K
        Usv, s, Vt = np.linalg.svd(M, full_matrices=False)
        tol = max(M.shape) * s[0] * np.finfo(float).eps
        rank = int(np.sum(s > tol))
        Mp = (Vt[:rank].T / s[:rank]) @ Usv[:, :rank].T                    # pseudoinversa pela SVD truncada
        theta = np.concatenate([c_th, np.zeros(K)])
        exact_err = float(np.max(np.abs(Mp @ (M @ theta) - theta)))
        rx = Mp[:K, :]; ry = Mp[K:, :]
        rc = rx + 1j * ry
        l1_ratio = np.sum(np.abs(rx), axis=1); l2_ratio = np.linalg.norm(rx, axis=1)
        l1_cplx = np.sum(np.abs(rc), axis=1); l2_cplx = np.linalg.norm(rc, axis=1)
        contam = {}
        for U in U_LIST:
            rho_c = np.zeros(J, dtype=complex)
            for Tn, cn in extra[U]:
                rho_c += cn * 0.5 * (np.exp(1j * E_c * Tn) * window_response(t - Tn, L, "hann")
                                     + np.exp(-1j * E_c * Tn) * window_response(t + Tn, L, "hann"))
            rho = np.concatenate([rho_c.real, rho_c.imag])
            ex = rx @ rho; ey = ry @ rho
            rel_ratio = np.abs(ex) / np.abs(c_th); rel_cplx = np.abs(ex + 1j * ey) / np.abs(c_th)
            kmax = int(np.argmax(rel_ratio))
            contam[str(U)] = {"max_rel_ratio": float(rel_ratio.max()), "linha_max_ratio": [catalog[kmax]["prime"], catalog[kmax]["repetition"]],
                              "mediana_rel_ratio": float(np.median(rel_ratio)), "max_rel_complexo": float(rel_cplx.max()),
                              "n_linhas_rel_ratio_acima_tau": int(np.sum(rel_ratio > TAU)),
                              "sup_rho_lin": float(np.max(np.abs(rho_c)))}
        results["blocos"].append({
            "versao": ver, "bloco": name, "L": L, "E_c": E_c, "J": J, "dim_M": list(M.shape),
            "sigma_max": float(s[0]), "sigma_min": float(s[-1]), "cond": float(s[0] / s[-1]), "tol_posto": float(tol), "posto": rank,
            "posto_completo": rank == 2 * K, "exatidao_Mp_M_theta": exact_err,
            "norma_linha_ratio_l1": {"min": float(l1_ratio.min()), "max": float(l1_ratio.max())},
            "norma_linha_ratio_l2": {"min": float(l2_ratio.min()), "max": float(l2_ratio.max())},
            "norma_linha_complexa_l1": {"min": float(l1_cplx.min()), "max": float(l1_cplx.max())},
            "escala_suficiente_linf_ratio": {"min_sobre_k_de_tau|c_k|/||row||_1": float(np.min(TAU * np.abs(c_th) / l1_ratio)),
                                             "max": float(np.max(TAU * np.abs(c_th) / l1_ratio))},
            "contaminacao": contam})
json.dump(results, open("results/etapa11_r5/r5_resultados.json", "w"), indent=1)
b = results["blocos"]
print("K =", K, "linhas extra por U:", results["n_linhas_extra_por_U"])
print("posto completo em todos:", all(x["posto_completo"] for x in b))
print("cond: min %.3e max %.3e" % (min(x["cond"] for x in b), max(x["cond"] for x in b)))
print("exatidão max: %.2e" % max(x["exatidao_Mp_M_theta"] for x in b))
print("norma linha l1 (ratio): min %.3e max %.3e" % (min(x["norma_linha_ratio_l1"]["min"] for x in b), max(x["norma_linha_ratio_l1"]["max"] for x in b)))
print("escala suficiente tau|c|/||row||1: min %.3e max %.3e" % (min(x["escala_suficiente_linf_ratio"]["min_sobre_k_de_tau|c_k|/||row||_1"] for x in b), max(x["escala_suficiente_linf_ratio"]["max"] for x in b)))
for U in U_LIST:
    vals = [x["contaminacao"][str(U)] for x in b]
    worst = max(vals, key=lambda v: v["max_rel_ratio"])
    print("U=%s: max rel ratio %.3e (linha %s), max rel complexo %.3e, blocos com alguma linha > tau: %d, sup rho_lin max %.3e" %
          (U, worst["max_rel_ratio"], worst["linha_max_ratio"], max(v["max_rel_complexo"] for v in vals),
           sum(v["n_linhas_rel_ratio_acima_tau"] > 0 for v in vals), max(v["sup_rho_lin"] for v in vals)))
