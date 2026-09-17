"""
Certificação da contaminação em (5, 13] e do resíduo contra o catálogo 𝒦, conforme
results/etapa11_r5/DECLARACAO_CERT_CONTAMINACAO.md (hash verificado). Reaproveita DECLARACAO_CERT.md e adendos 1–3.

Importa cert_calculo.py (execução 4, congelada; hash verificado) como módulo e chama suas primitivas; não o modifica.
Lê B_rel_sup e Sabs_rel_sup de cert_tabela.csv da execução 4.

Regime I  (5, 6]:  Q_k(log n) ponto a ponto, 51 termos, pela definição de ℓ_u com W_iv.
Regime II (6, 13]: 1.792 células δ = 1/256, envoltórias P + derivada do Lema 1 (mesmo Passo 4 da execução 4).

Execução completa só com a flag --executar (a declaração exige parada após os testes).
"""
import bisect, csv, glob, hashlib, importlib.util, json, math, sys, time
from fractions import Fraction
from multiprocessing import Pool
import numpy as np
from mpmath import iv

BASE = "results/etapa11_r5/"
DOCS = [("DECLARACAO_CERT.md", "DECLARACAO_CERT.sha256"),
        ("DECLARACAO_CERT_CORRECAO1.md", "DECLARACAO_CERT_CORRECAO1.sha256"),
        ("DECLARACAO_CERT_CORRECAO2.md", "DECLARACAO_CERT_CORRECAO2.sha256"),
        ("DECLARACAO_CERT_RECONF_C1C2.md", "DECLARACAO_CERT_RECONF_C1C2.sha256"),
        ("DECLARACAO_CERT_CONTAMINACAO.md", "DECLARACAO_CERT_CONTAMINACAO.sha256")]
for f, h in DOCS:
    assert hashlib.sha256(open(BASE + f, "rb").read()).hexdigest() == open(BASE + h).read().split()[0], f
CC_SHA = "95bec52820df9a8fa9830a6283576e6a3afacb6962f2cf38b546a93d4222aeb2"
assert hashlib.sha256(open(BASE + "cert_calculo.py", "rb").read()).hexdigest() == CC_SHA, "cert_calculo.py alterado"

_spec = importlib.util.spec_from_file_location("cc", BASE + "cert_calculo.py")
cc = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(cc)

K = cc.K
TAU = Fraction(1, 10**6)
U_I, U_II, U_END = 5, 6, 13
NCELL2 = (U_END - U_II) * 256                    # 1792
CELL = 1.0/256                                   # exato em binário


def floors():
    """floor(e⁵), floor(e⁶), floor(e¹³) por extremos exatos; asserção de não ambiguidade."""
    out = {}
    for x in (5, 6, 13):
        E = iv.exp(iv.mpf(x))
        lo, hi = math.floor(cc.lo_q(E)), math.floor(cc.hi_q(E))
        assert lo == hi, ("floor ambíguo", x)
        out[x] = lo
    return out


FL = floors()
N5, N6, N13 = FL[5], FL[6], FL[13]


def trial_prime(m):
    if m < 2: return False
    d = 2
    while d*d <= m:
        if m % d == 0: return False
        d += 1
    return True


def prime_powers(lo_excl, hi_incl, primes):
    """Potências de primo n com lo_excl < n ≤ hi_incl, a partir de uma lista de primos; devolve {n: p}."""
    out = {}
    for p in primes:
        p = int(p)
        if p > hi_incl: break
        q = p
        while q <= hi_incl:
            if q > lo_excl: out[q] = p
            q *= p
    return out


def regime1_terms():
    """Os 51 termos de (e⁵, e⁶]: duas enumerações independentes (crivo × divisão por tentativa)."""
    a = prime_powers(N5, N6, cc.sieve_a(N6))
    b = prime_powers(N5, N6, [m for m in range(2, N6 + 1) if trial_prime(m)])
    assert a == b, "enumeração do regime I diverge"
    return sorted(a.items())


def regime2_cells():
    """Somas Σ Λ(n)/√n (sem peso) por célula de (6, 13], n ∈ [N6+1, N13]; cobertura verificada."""
    edges = [iv.exp(iv.mpf(U_II) + iv.mpf(i)/256) for i in range(NCELL2 + 1)]
    lo_int = [math.floor(cc.lo_q(x)) for x in edges]; hi_int = [math.floor(cc.hi_q(x)) for x in edges]
    assert lo_int[0] == N6 and hi_int[0] == N6 and lo_int[-1] == N13 and hi_int[-1] == N13
    pa = cc.sieve_a(N13); pb = cc.sieve_b(N13)
    sieve_ok = bool(len(pa) == len(pb) and np.array_equal(pa, pb)); assert sieve_ok
    terms = prime_powers(N6, N13, pa)
    ns = sorted(terms)
    assigned = {n: 0 for n in ns}
    logp = {}; S = []
    for i in range(NCELL2):
        a = bisect.bisect_right(ns, lo_int[i]); b = bisect.bisect_right(ns, hi_int[i + 1])
        acc = iv.mpf(0)
        for n in ns[a:b]:
            assigned[n] += 1
            p = terms[n]
            if p not in logp: logp[p] = iv.log(p)
            acc += logp[p]/iv.sqrt(n)
        S.append(acc)
    n_primes = sum(1 for n in ns if terms[n] == n)
    info = {"N6": N6, "N13": N13, "crivo_conferido": sieve_ok, "n_termos": len(ns), "n_primos": n_primes,
            "n_potencias_r2": len(ns) - n_primes, "nao_atribuidos": sum(1 for v in assigned.values() if v == 0),
            "atribuidos_duas_celulas": sum(1 for v in assigned.values() if v >= 2),
            "bordas_ambiguas": sum(1 for i in range(NCELL2 + 1) if lo_int[i] != hi_int[i]),
            "expoente_primeira_borda": "6", "expoente_ultima_borda": str(Fraction(U_II) + Fraction(NCELL2, 256))}
    assert info["nao_atribuidos"] == 0
    return S, info, ns, terms, lo_int, hi_int


def cell_of(n, lo_int, hi_int):
    """Índices de célula que contêm n (mesma regra de atribuição de regime2_cells)."""
    return [i for i in range(NCELL2) if lo_int[i] < n <= hi_int[i + 1]]


def reconstruct(ins):
    """Passos 1–3, na mesma ordem de operações de cc.block (execução 4)."""
    A = ins["A"]; B = ins["B"]; Ec = ins["E_c"]; L = B - A
    h = 0.5*cc.measure_window_response(L)["fwhm"]
    t = np.unique(np.concatenate([np.linspace(x - h, x + h, 9) for x in cc.Tflt])); J = len(t)
    Liv = iv.mpf(L); Eciv = iv.mpf(Ec)
    Tiv = [iv.log(c["prime"]**c["repetition"]) for c in cc.catalog]
    Wm_lo = np.empty((J, K)); Wm_hi = np.empty((J, K)); Wp_lo = np.empty((J, K)); Wp_hi = np.empty((J, K))
    for i in range(J):
        ti = iv.mpf(float(t[i]))
        for j in range(K):
            a = cc.ivf(cc.W_iv(ti - Tiv[j], Liv)); b = cc.ivf(cc.W_iv(ti + Tiv[j], Liv))
            Wm_lo[i, j], Wm_hi[i, j] = a.lo, a.hi; Wp_lo[i, j], Wp_hi[i, j] = b.lo, b.hi
    cph = [cc.ivf(iv.cos(Eciv*Tiv[j])) for j in range(K)]; sph = [cc.ivf(iv.sin(Eciv*Tiv[j])) for j in range(K)]
    C = cc.I(np.array([c.lo for c in cph]), np.array([c.hi for c in cph])); Sn = cc.I(np.array([c.lo for c in sph]), np.array([c.hi for c in sph]))
    Wm = cc.I(Wm_lo, Wm_hi); Wp = cc.I(Wp_lo, Wp_hi); half = cc.I(0.5)
    SP = (Wm + Wp)*half; DF = (Wm - Wp)*half
    ReGH = SP*C[None, :]; ImGH = DF*Sn[None, :]
    ReiGH = -(SP*Sn[None, :]); ImiGH = DF*C[None, :]
    M = cc.I(np.vstack([np.hstack([ReGH.lo, ReiGH.lo]), np.hstack([ImGH.lo, ImiGH.lo])]),
             np.vstack([np.hstack([ReGH.hi, ReiGH.hi]), np.hstack([ImGH.hi, ImiGH.hi])]))
    Mt = cc.I(M.lo.T.copy(), M.hi.T.copy())
    G = cc.matmul(Mt, M)
    R = np.linalg.inv(0.5*(G.lo + G.hi))
    RG = cc.matmul(cc.I(R), G)
    E = cc.I(np.eye(2*K)) - RG
    rho = float(cc.fin(np.max(cc.up(cc.isum(cc.I(E.mag()), axis=1).hi))))
    assert rho < 1, rho
    e = float(cc.fin(cc.up(cc.up(rho)/cc.dn(1 - rho))))
    Y = cc.matmul(cc.I(R), Mt)
    ynorm = cc.isum(cc.I(Y.mag()), axis=1).hi
    ymax_col = np.max(Y.mag(), axis=0)
    a_l1 = cc.fin(cc.up(ynorm[:K] + cc.up(e*np.max(ynorm))))
    rad = cc.up(e*ymax_col)
    Arows = cc.I(cc.dn(Y.lo[:K] - rad[None, :]), cc.up(Y.hi[:K] + rad[None, :]))
    tmax = float(np.max(t)); assert tmax < 5.0
    return {"L": L, "Ec": Ec, "t": t, "J": J, "Liv": Liv, "Eciv": Eciv, "rho": rho, "e": e, "a_l1": a_l1,
            "Arows": Arows, "tmax": tmax, "lam": cc.ivf(Liv/(2*cc.PI)), "kap8": cc.ivf(Liv/(8*cc.PI))}


def q_pointwise(rec, n):
    """Enclausuramento de Q_k(log n), k = 1..K, pela definição: Q_k = Σ_j aR_j Re ℓ_u(t_j) + aI_j Im ℓ_u(t_j)."""
    u = iv.log(n); J = rec["J"]; Liv = rec["Liv"]
    cE = iv.cos(rec["Eciv"]*u); sE = iv.sin(rec["Eciv"]*u)
    re_lo = np.empty(J); re_hi = np.empty(J); im_lo = np.empty(J); im_hi = np.empty(J)
    for j in range(J):
        tj = iv.mpf(float(rec["t"][j]))
        Wm = cc.W_iv(tj - u, Liv); Wp = cc.W_iv(tj + u, Liv)
        re = cc.ivf(cE*(Wm + Wp)/2); im = cc.ivf(sE*(Wm - Wp)/2)
        re_lo[j], re_hi[j] = re.lo, re.hi; im_lo[j], im_hi[j] = im.lo, im.hi
    ReL = cc.I(re_lo, re_hi); ImL = cc.I(im_lo, im_hi)
    aR = rec["Arows"][:, :J]; aI = rec["Arows"][:, J:]
    return cc.isum(aR*ReL[None, :] + aI*ImL[None, :], axis=1)


def c_sup(n, p):
    return cc.float_up(cc.hi_q(iv.log(p)/(cc.PI*iv.sqrt(n))))


def regime1_P(rec, terms1):
    P = np.zeros(K)
    for n, p in terms1:
        P = cc.fin(cc.up(P + cc.up(c_sup(n, p)*q_pointwise(rec, n).mag())))
    return P


def regime2_supQ(rec):
    """sup|Q_k| por célula em (6, 13] (Passo 4 da execução 4, com início em 6) e v_min exato por célula."""
    t = rec["t"]; J = rec["J"]; Liv = rec["Liv"]; lam = rec["lam"]; kap8 = rec["kap8"]; tmax = rec["tmax"]
    Arows = rec["Arows"]; a_l1 = rec["a_l1"]
    th = [cc.ivf(iv.cos(iv.mpf(float(t[j]))*Liv/2)) for j in range(J)]; thS = [cc.ivf(iv.sin(iv.mpf(float(t[j]))*Liv/2)) for j in range(J)]
    cosT = cc.I(np.array([x.lo for x in th]), np.array([x.hi for x in th])); sinT = cc.I(np.array([x.lo for x in thS]), np.array([x.hi for x in thS]))
    aR = Arows[:, :J]; aI = Arows[:, J:]
    cA_re = aR*cosT[None, :] + aI*sinT[None, :]; cA_im = aR*sinT[None, :] - aI*cosT[None, :]
    cB_re = aR*cosT[None, :] - aI*sinT[None, :]; cB_im = -(aR*sinT[None, :]) - aI*cosT[None, :]
    supQ = np.zeros((K, NCELL2)); vmins = np.zeros(NCELL2); margin_ok = True
    for ci in range(NCELL2):
        ulo = U_II + ci*CELL; uc = ulo + CELL/2
        vmn = cc.dn(lam.lo*cc.dn(ulo - tmax))
        ok = bool(vmn > 0 and Fraction(float(vmn))**2 >= 2)
        margin_ok = margin_ok and ok
        assert ok, ("margem", ci)
        vmins[ci] = vmn
        q2 = cc.fin(cc.dn(vmn*vmn)); v4 = cc.fin(cc.dn(q2*q2)); assert v4 > 0
        dR = cc.fin(cc.up(12.0/v4))
        acc = np.zeros(K)
        for sgn in (-1.0, 1.0):
            tu = cc.I(cc.dn(t + sgn*uc), cc.up(t + sgn*uc))
            v = tu*lam
            Rv = (v*(v*v - cc.I(1.0))).inv()
            for cre, cim in ((cA_re, cA_im), (cB_re, cB_im)):
                pr = cc.isum(cre*Rv[None, :], axis=1); pi_ = cc.isum(cim*Rv[None, :], axis=1)
                acc = cc.up(acc + cc.up(pr.mag() + pi_.mag()))
        acc = cc.up(kap8.hi*acc)
        deriv = cc.up(kap8.hi*cc.up(4*cc.up(cc.up(lam.hi*a_l1)*dR)))
        supQ[:, ci] = cc.fin(cc.up(acc + cc.up(deriv*(CELL/2))))
    return supQ, vmins, margin_ok


def regime2_C(supQ, cellS_hi):
    C = np.zeros(K)
    for ci in range(NCELL2):
        C = cc.up(C + cc.up(supQ[:, ci]*cellS_hi[ci]))
    return cc.fin(cc.up(C/cc.PI_INF))


def ck_inf_q(p, r):
    return cc.lo_q(iv.log(p)/(cc.PI*iv.sqrt(p**r)))


def decide(B_rel_str, Sabs_rel_str, P_abs, C_abs, p, r):
    """total_k = B_rel_sup + Sabs_rel_sup + (P + C)/|c_k|_inf, em frações exatas."""
    total = Fraction(B_rel_str) + Fraction(Sabs_rel_str) + (Fraction(P_abs) + Fraction(C_abs))/ck_inf_q(p, r)
    return total, total <= TAU


def exec4_tables():
    blocos = {(b["versao"], b["bloco"]): b for b in csv.DictReader(open(BASE + "cert_blocos.csv"))}
    tab = {(t["versao"], t["bloco"], t["p"], t["r"]): t for t in csv.DictReader(open(BASE + "cert_tabela.csv"))}
    return blocos, tab


def bit_exact_vs_exec4(ver, name, rec, blocos, tab):
    diffs = []
    if float(blocos[(ver, name)]["rho"]) != rec["rho"]:
        diffs.append(("rho", blocos[(ver, name)]["rho"], rec["rho"]))
    for k, c in enumerate(cc.catalog):
        v4 = float(tab[(ver, name, str(c["prime"]), str(c["repetition"]))]["a_l1_sup"])
        if v4 != float(rec["a_l1"][k]):
            diffs.append(("a_l1", c["prime"], c["repetition"], v4, float(rec["a_l1"][k])))
    return diffs


def block_job(args):
    ver, name, ins, cellS_hi, terms1 = args
    t0 = time.time()
    rec = reconstruct(ins)
    P = regime1_P(rec, terms1)
    supQ, vmins, margin_ok = regime2_supQ(rec)
    C = regime2_C(supQ, cellS_hi)
    return {"versao": ver, "bloco": name, "rho": rec["rho"], "a_l1": [float(x) for x in rec["a_l1"]],
            "P": [float(x) for x in P], "C": [float(x) for x in C], "vmin_celulas": float(vmins.min()),
            "margem_ok": margin_ok, "segundos": time.time() - t0}


def jobs_all(cellS_hi, terms1):
    out = []
    for ver, pat in cc.runs.items():
        m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
        for name, blk in m["blocks"].items():
            out.append((ver, name, blk["instrument"], cellS_hi, terms1))
    return out


if __name__ == "__main__":
    if "--executar" not in sys.argv:
        sys.exit("Execução completa bloqueada: exige --executar (DECLARACAO_CERT_CONTAMINACAO §3, parada após os testes).")
    t0 = time.time()
    terms1 = regime1_terms()
    S, info, *_ = regime2_cells()
    cellS_hi = np.array([cc.float_up(cc.hi_q(x)) for x in S])
    blocos, tab = exec4_tables()
    with Pool(3) as pool:
        res = list(pool.imap_unordered(block_job, jobs_all(cellS_hi, terms1)))
    stop = []
    rows = []
    for r in sorted(res, key=lambda x: (x["versao"], x["bloco"])):
        if float(blocos[(r["versao"], r["bloco"])]["rho"]) != r["rho"]:
            stop.append((r["versao"], r["bloco"], "rho"))
        for k, c in enumerate(cc.catalog):
            key = (r["versao"], r["bloco"], str(c["prime"]), str(c["repetition"]))
            t4 = tab[key]
            if float(t4["a_l1_sup"]) != r["a_l1"][k]:
                stop.append(key + ("a_l1",))
            total, ok = decide(t4["B_rel_sup"], t4["Sabs_rel_sup"], r["P"][k], r["C"][k], c["prime"], c["repetition"])
            rows.append({"versao": r["versao"], "bloco": r["bloco"], "p": c["prime"], "r": c["repetition"],
                         "eligible": t4["eligible"], "B_rel_sup": t4["B_rel_sup"], "Sabs_rel_sup": t4["Sabs_rel_sup"],
                         "P_abs_sup": r["P"][k], "C_abs_sup": r["C"][k],
                         "total_sup": cc.sup_chk(cc.iv_frac(total), 15), "certificado": ok and r["margem_ok"]})
    summ = {"declaracao_sha256": open(BASE + "DECLARACAO_CERT_CONTAMINACAO.sha256").read().split()[0],
            "cert_calculo_sha256": CC_SHA, "regime1_termos": len(terms1), "regime2": info,
            "parada_bit_a_bit": stop, "tempo_s": time.time() - t0}
    if stop:
        summ["leitura"] = "INTERROMPIDA: reconstrução diverge da execução 4; nenhum par lido como certificado"
    else:
        E = [x for x in rows if x["eligible"] == "True"]
        summ.update({"pares": len(rows), "certificados": sum(x["certificado"] for x in rows),
                     "elegiveis": len(E), "elegiveis_certificados": sum(x["certificado"] for x in E),
                     "max_total_elegiveis": max(Fraction(x["total_sup"]) for x in E).__float__()})
    with open(BASE + "cert_contaminacao_blocos.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["versao", "bloco", "rho", "vmin_celulas", "margem_ok", "segundos"]); w.writeheader()
        for r in res: w.writerow({k: r[k] for k in ["versao", "bloco", "rho", "vmin_celulas", "margem_ok", "segundos"]})
    with open(BASE + "cert_contaminacao_tabela.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    json.dump(summ, open(BASE + "cert_contaminacao_resumo.json", "w"), indent=1, default=str)
    print(json.dumps(summ, indent=1, default=str))
