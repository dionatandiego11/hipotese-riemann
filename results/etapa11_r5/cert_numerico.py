"""
Camada numérica ρ_num, conforme results/etapa11_r5/DECLARACAO_CERT_NUMERICO.md (hash verificado).

(N) incondicional: enclausura de X_k/c_k (estimador matemático a_k de M^math sobre F^tab = D − S) e
    ε_k^sup = sup |r̂_k − X_k/c_k|, com r̂_k = fit_ratio_to_theory registrado em m4.
(T) sob RH, F5, J1 e H-tab: certificado ⇔ ε_k^sup + total^γ_k ≤ 10⁻⁶.
Alarme de consistência: inf|X_k/c_k − 1| > total^γ_k ⇒ execução interrompida, nenhum par lido como certificado.

D(t) = Σ_{n∈I} w(γ_n^tab) e^{−i(γ_n^tab − E_c)t}  (decimais brutos; zeros fora de [A*, B*] contribuem 0)
S(t) = (1/2π)[ln(E_c/2π)·M_0 + Σ_{m=1}^{K}(−1)^{m+1}M_m/(m E_c^m)] ± ρ_K,  M_m = ½J_m(t) + ¼J_m(t−β) + ¼J_m(t+β)
J_m(ω) = C_m − i S_m,  C_m = ∫x^m cos ωx,  S_m = ∫x^m sin ωx  em [−a, a]  (recorrência por partes; dps 60)
Execução só com --executar.
"""
import csv, glob, hashlib, json, math, sys, time
from fractions import Fraction
from multiprocessing import Pool
import numpy as np
from mpmath import iv

BASE = "results/etapa11_r5/"
DOCS = [("DECLARACAO_CERT.md", "DECLARACAO_CERT.sha256"),
        ("DECLARACAO_CERT_CORRECAO1.md", "DECLARACAO_CERT_CORRECAO1.sha256"),
        ("DECLARACAO_CERT_CORRECAO2.md", "DECLARACAO_CERT_CORRECAO2.sha256"),
        ("DECLARACAO_CERT_RECONF_C1C2.md", "DECLARACAO_CERT_RECONF_C1C2.sha256"),
        ("DECLARACAO_CERT_CONTAMINACAO.md", "DECLARACAO_CERT_CONTAMINACAO.sha256"),
        ("DECLARACAO_CERT_DENSIDADE.md", "DECLARACAO_CERT_DENSIDADE.sha256"),
        ("DECLARACAO_CERT_ORDENADAS.md", "DECLARACAO_CERT_ORDENADAS.sha256"),
        ("DECLARACAO_CERT_NUMERICO.md", "DECLARACAO_CERT_NUMERICO.sha256")]
for f, h in DOCS:
    assert hashlib.sha256(open(BASE + f, "rb").read()).hexdigest() == open(BASE + h).read().split()[0], f
SHAS = {"cert_calculo.py": "95bec52820df9a8fa9830a6283576e6a3afacb6962f2cf38b546a93d4222aeb2",
        "cert_contaminacao.py": "4baff93389cea085c690567fadc8c20c87ab951d4e88a214988457e953885945",
        "cert_densidade.py": "598871cf3efbf2bd6641b18ac5a8a4590b9cba119427bee13f349aff3fa9afe7",
        "cert_ordenadas.py": "884de08776a8f46c384f6fd882093a3cdefe19d4adb2a3384f9f20e252d0ec08"}
for f, h in SHAS.items():
    assert hashlib.sha256(open(BASE + f, "rb").read()).hexdigest() == h, f

sys.path.insert(0, BASE)
import cert_ordenadas as co       # tabela bruta, geometria, reconstrução (via cx), primitivas (cc)
cc = co.cc; cx = co.cx
sys.path.insert(0, "results/etapa11_3b")
from interval_export import inf_str
K_CAT = cc.K
TAU = Fraction(1, 10**6)
RHO_TOL = Fraction(1, 10**20)
WIDTH_S_MAX = 1e-18
DPS_MOM = 60


def inf_chk(x, digits):
    st = inf_str(x, digits); assert Fraction(st) <= cc.lo_q(x), "exportação acima do extremo inferior"
    return st


def frac_to_iv(q):
    return iv.mpf(q.numerator)/iv.mpf(q.denominator)


# ---------------------------------------------------------------- termo suave S(t_j)
def K_rule(a, Ec):
    """Menor K ≥ 1 com ρ_K = (1/2π)·a·y^{K+1}/((K+1)(1−y)) ≤ 1e-20, y = a/E_c; frações exatas, π inferior."""
    y = a/Ec; assert 0 < y < 1
    pi_inf = cc.lo_q(cc.PI)
    K = 1
    while True:
        rho = a*y**(K + 1)/((K + 1)*(1 - y))/(2*pi_inf)
        if rho <= RHO_TOL: return K, rho
        K += 1


def moments_CS(omega, a_iv, K):
    """C_m, S_m (m = 0..K) de ∫_{−a}^{a} x^m {cos, sin}(ωx) dx, por recorrência; ω intervalo com ω > 0."""
    sa = iv.sin(omega*a_iv); ca = iv.cos(omega*a_iv)
    C = [2*sa/omega]; S = [iv.mpf(0)]
    am = iv.mpf(1)
    for m in range(1, K + 1):
        am = am*a_iv
        if m % 2 == 0:
            C.append(2*am*sa/omega - (m/omega)*S[m - 1]); S.append(iv.mpf(0))
        else:
            S.append(-2*am*ca/omega + (m/omega)*C[m - 1]); C.append(iv.mpf(0))
    return C, S


def smooth_term(t, Lf, Ecf, K, rhoK):
    """S(t_j) para todos os nós: devolve (re_lo, re_hi, im_lo, im_hi, largura_max) com ±ρ_K incluído."""
    old = iv.dps; iv.dps = DPS_MOM
    try:
        Lq = Fraction(Lf); Ecq = Fraction(Ecf)
        a_iv = frac_to_iv(Lq/2); Ec_iv = frac_to_iv(Ecq); beta = 2*iv.pi/frac_to_iv(Lq)
        coef0 = iv.log(Ec_iv/(2*iv.pi))
        coefs = [((-1)**(m + 1))/(m*Ec_iv**m) for m in range(1, K + 1)]
        rho_iv = frac_to_iv(rhoK)
        J = len(t); re_lo = np.empty(J); re_hi = np.empty(J); im_lo = np.empty(J); im_hi = np.empty(J); wmax = 0.0
        for j in range(J):
            tj = iv.mpf(float(t[j]))
            Mre = [iv.mpf(0)]*(K + 1); Mim = [iv.mpf(0)]*(K + 1)
            for om, wt in ((tj, iv.mpf(1)/2), (tj - beta, iv.mpf(1)/4), (tj + beta, iv.mpf(1)/4)):
                assert cc.lo_q(om) > 0, "ω ≤ 0"
                C, Sm = moments_CS(om, a_iv, K)
                for m in range(K + 1):
                    Mre[m] = Mre[m] + wt*C[m]; Mim[m] = Mim[m] - wt*Sm[m]      # J_m = C_m − i S_m
            re = coef0*Mre[0]; im = coef0*Mim[0]
            for m in range(1, K + 1):
                re = re + coefs[m - 1]*Mre[m]; im = im + coefs[m - 1]*Mim[m]
            re = re/(2*iv.pi) + iv.mpf([-1, 1])*rho_iv
            im = im/(2*iv.pi) + iv.mpf([-1, 1])*rho_iv
            r = cc.ivf(re); i_ = cc.ivf(im)
            re_lo[j], re_hi[j], im_lo[j], im_hi[j] = r.lo, r.hi, i_.lo, i_.hi
            wmax = max(wmax, float(r.hi - r.lo), float(i_.hi - i_.lo))
        return re_lo, re_hi, im_lo, im_hi, wmax
    finally:
        iv.dps = old


# ---------------------------------------------------------------- parte discreta D(t_j)
def discrete_term(t, geo, raw, indices=None):
    J = len(t)
    tiv = [iv.mpf(float(x)) for x in t]
    Aiv = cc.iv_frac(geo["A_star"]); Ecv = cc.iv_frac(geo["Ecq"]); Liv = iv.mpf(geo["L"])
    D_re = cc.I(np.zeros(J)); D_im = cc.I(np.zeros(J))
    for n in (indices if indices is not None else range(geo["lo"], geo["hi"] + 1)):
        Eq = Fraction(raw[n])
        if not (geo["A_star"] <= Eq <= geo["B_star"]):
            continue
        E = cc.iv_frac(Eq)
        w = iv.sin(cc.PI*(E - Aiv)/Liv)**2
        u = E - Ecv
        re_lo = np.empty(J); re_hi = np.empty(J); im_lo = np.empty(J); im_hi = np.empty(J)
        for j in range(J):
            ph = u*tiv[j]
            re = cc.ivf(w*iv.cos(ph)); im = cc.ivf(-(w*iv.sin(ph)))
            re_lo[j], re_hi[j] = re.lo, re.hi; im_lo[j], im_hi[j] = im.lo, im.hi
        D_re = D_re + cc.I(re_lo, re_hi); D_im = D_im + cc.I(im_lo, im_hi)
    return D_re, D_im


# ---------------------------------------------------------------- registrados e decisão
def registered(ver, name):
    R = glob.glob(cc.runs[ver])[0]
    rows = list(csv.DictReader(open(f"{R}/tables/{name}/arithmetic_matches.csv")))
    return {(int(r["prime"]), int(r["repetition"])): r["fit_ratio_to_theory"] for r in rows}


def c_interval(p, r):
    c = -iv.log(p)/(cc.PI*iv.sqrt(p**r))
    return cc.lo_q(c), cc.hi_q(c)


def decide(X_lo, X_hi, p, r, rhat_str, total_gamma_str):
    """Frações exatas. Devolve q = X/c − 1 (intervalo), ε^sup, inf|q|, T certificado, alarme."""
    c_lo, c_hi = c_interval(p, r); assert c_hi < 0
    Xl, Xh = Fraction(X_lo), Fraction(X_hi)
    cands = [Xl/c_lo, Xl/c_hi, Xh/c_lo, Xh/c_hi]
    q_lo = min(cands) - 1; q_hi = max(cands) - 1
    rh = Fraction(float(rhat_str)) - 1
    eps = max(abs(rh - q_lo), abs(rh - q_hi))
    absinf = Fraction(0) if q_lo <= 0 <= q_hi else min(abs(q_lo), abs(q_hi))
    tg = Fraction(total_gamma_str)
    return {"q_lo": q_lo, "q_hi": q_hi, "eps_sup": eps, "absq_inf": absinf,
            "T_certificado": eps + tg <= TAU, "alarme": absinf > tg}


def block_job(args):
    ver, name, ins = args
    t0 = time.time()
    raw = co.load_raw(); _, zf = co.load_processed_floats()
    geo = co.block_geometry(ins, raw, zf)
    rec = cx.reconstruct(ins)
    t1 = time.time()
    K, rhoK = K_rule(Fraction(ins["B"] - ins["A"])/2, Fraction(ins["E_c"]))
    Sre_lo, Sre_hi, Sim_lo, Sim_hi, wS = smooth_term(rec["t"], rec["L"], rec["Ec"], K, rhoK)
    assert wS <= WIDTH_S_MAX, ("largura de S", wS)
    t2 = time.time()
    D_re, D_im = discrete_term(rec["t"], geo, raw)
    t3 = time.time()
    F_re = D_re - cc.I(Sre_lo, Sre_hi); F_im = D_im - cc.I(Sim_lo, Sim_hi)
    J = rec["J"]; aR = rec["Arows"][:, :J]; aI = rec["Arows"][:, J:]
    X = cc.isum(aR*F_re[None, :] + aI*F_im[None, :], axis=1)
    return {"versao": ver, "bloco": name, "rho": rec["rho"], "a_l1": [float(x) for x in rec["a_l1"]],
            "K": K, "rhoK": str(rhoK), "largura_S_max": wS,
            "largura_D_max": float(max(np.max(D_re.hi - D_re.lo), np.max(D_im.hi - D_im.lo))),
            "X_lo": [float(x) for x in X.lo], "X_hi": [float(x) for x in X.hi],
            "segundos_reconstrucao": t1 - t0, "segundos_suave": t2 - t1, "segundos_discreta": t3 - t2}


def jobs_all():
    out = []
    for ver, pat in cc.runs.items():
        m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
        for name, blk in m["blocks"].items():
            out.append((ver, name, blk["instrument"]))
    return out


if __name__ == "__main__":
    if "--executar" not in sys.argv:
        sys.exit("Execução bloqueada: exige --executar (DECLARACAO_CERT_NUMERICO §3, após testes e revisão).")
    t0 = time.time()
    with Pool(3) as pool:
        res = []
        for r in pool.imap_unordered(block_job, jobs_all()):
            print(r["versao"], r["bloco"], "K=%d %.0fs" % (r["K"], r["segundos_reconstrucao"] + r["segundos_suave"] + r["segundos_discreta"]), flush=True)
            res.append(r)
    blocos4, tab4 = cx.exec4_tables()
    tord = {(t["versao"], t["bloco"], t["p"], t["r"]): t for t in csv.DictReader(open(BASE + "cert_ordenadas_tabela.csv"))}
    stop = []; alarms = []; rows = []; brows = []
    for r in sorted(res, key=lambda x: (x["versao"], x["bloco"])):
        if float(blocos4[(r["versao"], r["bloco"])]["rho"]) != r["rho"]: stop.append((r["versao"], r["bloco"], "rho"))
        reg = registered(r["versao"], r["bloco"])
        brows.append({k: r[k] for k in ["versao", "bloco", "K", "rhoK", "largura_S_max", "largura_D_max",
                                        "segundos_reconstrucao", "segundos_suave", "segundos_discreta"]})
        for k, c in enumerate(cc.catalog):
            key = (r["versao"], r["bloco"], str(c["prime"]), str(c["repetition"]))
            if float(tab4[key]["a_l1_sup"]) != r["a_l1"][k]: stop.append(key + ("a_l1",))
            d = decide(r["X_lo"][k], r["X_hi"][k], c["prime"], c["repetition"], reg[(c["prime"], c["repetition"])],
                       tord[key]["total_ordenadas_sup"])
            if d["alarme"]: alarms.append(key)
            rows.append({"versao": r["versao"], "bloco": r["bloco"], "p": c["prime"], "r": c["repetition"],
                         "eligible": tord[key]["eligible"], "r_hat": reg[(c["prime"], c["repetition"])],
                         "q_inf": inf_chk(cc.iv_frac(d["q_lo"]), 15), "q_sup": cc.sup_chk(cc.iv_frac(d["q_hi"]), 15),
                         "eps_sup": cc.sup_chk(cc.iv_frac(d["eps_sup"]), 18),
                         "absq_inf": inf_chk(cc.iv_frac(d["absq_inf"]), 15) if d["absq_inf"] > 0 else "0",
                         "total_ordenadas_sup": tord[key]["total_ordenadas_sup"],
                         "T_certificado": d["T_certificado"], "alarme": d["alarme"]})
    summ = {"declaracao_sha256": open(BASE + "DECLARACAO_CERT_NUMERICO.sha256").read().split()[0], "bases": SHAS,
            "parada_bit_a_bit": stop, "alarmes_consistencia": alarms, "tempo_s": time.time() - t0}
    if stop or alarms:
        summ["leitura"] = "INTERROMPIDA: " + ("reconstrução diverge da execução 4; " if stop else "") + \
                          ("alarme de consistência disparado; " if alarms else "") + "nenhum par lido como certificado (T)"
    else:
        E = [x for x in rows if x["eligible"] == "True"]
        summ.update({"pares": len(rows), "T_certificados": sum(x["T_certificado"] for x in rows),
                     "elegiveis": len(E), "elegiveis_T_certificados": sum(x["T_certificado"] for x in E),
                     "eps_sup_max_elegiveis": float(max(Fraction(x["eps_sup"]) for x in E)),
                     "eps_sup_max_todos": float(max(Fraction(x["eps_sup"]) for x in rows)),
                     "K_por_bloco": {f'{b["versao"]}/{b["bloco"]}': b["K"] for b in brows}})
    with open(BASE + "cert_numerico_blocos.csv", "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(brows[0].keys())); wr.writeheader(); wr.writerows(brows)
    with open(BASE + "cert_numerico_tabela.csv", "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
    json.dump(summ, open(BASE + "cert_numerico_resumo.json", "w"), indent=1, default=str)
    print(json.dumps(summ, indent=1, default=str))
