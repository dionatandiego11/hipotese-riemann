"""
Erro das ordenadas tabuladas ρ_ord: projeção por a_k, conforme results/etapa11_r5/DECLARACAO_CERT_ORDENADAS.md
(hash verificado). Condicional a RH (F5, J1) e à hipótese H-tab (não certificada).

total^γ_k = total^Δ_k + [ 3e-9·Σ_{n∈I}|g_k(γ_n^tab)| + ‖a_k‖₁^sup·(|I|·½(3e-9)²·S₂(t_max) + Borda) ] / |c_k|_inf ≤ 10⁻⁶
g_k(E) = Σ_j aR_kj·Re f̃′_{t_j}(E) + aI_kj·Im f̃′_{t_j}(E),  f̃′_t = e_t(w′ − i t w) em [A*, B*], 0 fora.

Ordenadas lidas como Fraction dos decimais brutos de data/raw/zeros1. Execução só com --executar.
"""
import csv, glob, hashlib, importlib.util, json, math, sys, time
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
        ("DECLARACAO_CERT_ORDENADAS.md", "DECLARACAO_CERT_ORDENADAS.sha256")]
for f, h in DOCS:
    assert hashlib.sha256(open(BASE + f, "rb").read()).hexdigest() == open(BASE + h).read().split()[0], f
SHAS = {"cert_calculo.py": "95bec52820df9a8fa9830a6283576e6a3afacb6962f2cf38b546a93d4222aeb2",
        "cert_contaminacao.py": "4baff93389cea085c690567fadc8c20c87ab951d4e88a214988457e953885945",
        "cert_densidade.py": "598871cf3efbf2bd6641b18ac5a8a4590b9cba119427bee13f349aff3fa9afe7"}
for f, h in SHAS.items():
    assert hashlib.sha256(open(BASE + f, "rb").read()).hexdigest() == h, f
RAW = "data/raw/zeros1"; RAW_SHA = "3436c916a7878261ac183fd7b9448c9a4736b8bbccf1356874a6ce1788541632"
assert hashlib.sha256(open(RAW, "rb").read()).hexdigest() == RAW_SHA
PROC = "data/processed/zeros_100k.csv"

sys.path.insert(0, BASE)
import cert_contaminacao as cx          # importa cert_calculo (cc) e a reconstrução testada
cc = cx.cc
K = cc.K
TAU = Fraction(1, 10**6)
DELTA_TAB = Fraction(3, 10**9)
PI_SUP = cc.hi_q(cc.PI)


def load_raw():
    """Decimais brutos: lista de strings (índice n = posição + 1)."""
    vals = [ln.strip() for ln in open(RAW) if ln.strip()]
    assert len(vals) == 100000
    return vals


def load_processed_floats():
    rows = list(csv.reader(open(PROC)))[1:]
    return [int(r[0]) for r in rows], np.array([float(r[1]) for r in rows])


def block_geometry(ins, raw, zf):
    """I pelos decimais, bordas decimais, janela [A*, B*], η, S₂, Borda (sem a_k) — tudo exato."""
    A = ins["A"]; B = ins["B"]; Ec = ins["E_c"]; L = B - A
    lo = int(np.searchsorted(zf, A, side="left")); hi = int(np.searchsorted(zf, B, side="right")) - 1
    assert zf[lo] == A and zf[hi] == B, "bordas do bloco não são entradas da tabela (float)"
    A_dec = Fraction(raw[lo]); B_dec = Fraction(raw[hi])
    idx_dec = [n for n in range(lo, hi + 1) if A_dec <= Fraction(raw[n]) <= B_dec]
    assert idx_dec == list(range(lo, hi + 1))
    Lq = Fraction(L); Ecq = Fraction(Ec); As = Ecq - Lq/2; Bs = Ecq + Lq/2
    eta = DELTA_TAB + max(abs(As - A_dec), abs(Bs - B_dec))
    h = 0.5*cc.measure_window_response(L)["fwhm"]
    t = np.unique(np.concatenate([np.linspace(x - h, x + h, 9) for x in cc.Tflt]))
    tmax = Fraction(float(np.max(t))); assert tmax < 5
    S2 = 2*PI_SUP**2/Lq**2 + 2*tmax*PI_SUP/Lq + tmax**2
    nI = hi - lo + 1
    rest_unit = nI*Fraction(1, 2)*DELTA_TAB**2*S2                          # × ‖a_k‖₁^sup
    cnt = cc.hi_q(iv.mpf("10.5")*iv.log(cc.iv_frac(As + 8)) + iv.mpf("10.5")*iv.log(cc.iv_frac(Bs + 8)))
    edge_unit = cnt*(PI_SUP*eta/Lq)**2                                     # × ‖a_k‖₁^sup
    return {"lo": lo, "hi": hi, "nI": nI, "A_dec": A_dec, "B_dec": B_dec, "A_star": As, "B_star": Bs, "eta": eta,
            "S2": S2, "rest_unit": rest_unit, "edge_unit": edge_unit, "L": L, "Lq": Lq, "Ecq": Ecq}


def g_abs_sum(rec, geo, raw, indices=None, return_each=False):
    """Σ_n |g_k(γ_n^tab)|^sup (vetor K), com g_k em intervalos; opcionalmente devolve os intervalos por zero."""
    J = rec["J"]; t = rec["t"]
    tiv = [iv.mpf(float(x)) for x in t]
    Aiv = cc.iv_frac(geo["A_star"]); Ecv = cc.iv_frac(geo["Ecq"]); Liv = iv.mpf(geo["L"])
    aR = rec["Arows"][:, :J]; aI = rec["Arows"][:, J:]
    acc = np.zeros(K); each = []
    for n in (indices if indices is not None else range(geo["lo"], geo["hi"] + 1)):
        Eq = Fraction(raw[n])
        if not (geo["A_star"] <= Eq <= geo["B_star"]):
            if return_each: each.append((n, None))
            continue                                                   # f̃′ = 0 fora da janela
        E = cc.iv_frac(Eq)
        x = cc.PI*(E - Aiv)/Liv
        w = iv.sin(x)**2; wp = (cc.PI/Liv)*iv.sin(2*x)
        u = E - Ecv
        re_lo = np.empty(J); re_hi = np.empty(J); im_lo = np.empty(J); im_hi = np.empty(J)
        for j in range(J):
            ph = u*tiv[j]; c = iv.cos(ph); s = iv.sin(ph)
            re = cc.ivf(c*wp - s*tiv[j]*w); im = cc.ivf(-(c*tiv[j]*w + s*wp))
            re_lo[j], re_hi[j] = re.lo, re.hi; im_lo[j], im_hi[j] = im.lo, im.hi
        g = cc.isum(aR*cc.I(re_lo, re_hi)[None, :] + aI*cc.I(im_lo, im_hi)[None, :], axis=1)
        acc = cc.fin(cc.up(acc + g.mag()))
        if return_each: each.append((n, g))
    return (acc, each) if return_each else acc


def block_job(args):
    ver, name, ins = args
    t0 = time.time()
    raw = load_raw(); _, zf = load_processed_floats()
    geo = block_geometry(ins, raw, zf)
    rec = cx.reconstruct(ins)
    t1 = time.time()
    G = g_abs_sum(rec, geo, raw)
    return {"versao": ver, "bloco": name, "rho": rec["rho"], "a_l1": [float(x) for x in rec["a_l1"]],
            "Gsum": [float(x) for x in G], "geo": {k: (str(v) if isinstance(v, Fraction) else v) for k, v in geo.items()},
            "segundos_reconstrucao": t1 - t0, "segundos_pares": time.time() - t1}


def ck_inf_q(p, r):
    return cc.lo_q(iv.log(p)/(cc.PI*iv.sqrt(p**r)))


def total_gamma(total_dens_str, a_l1_str, Gsum_float, rest_unit, edge_unit, p, r):
    """Frações exatas. Devolve (total, lin_rel, rest_rel, edge_rel, ok)."""
    ck = ck_inf_q(p, r); a = Fraction(float(a_l1_str))
    lin = DELTA_TAB*Fraction(Gsum_float)/ck
    rest = a*rest_unit/ck; edge = a*edge_unit/ck
    tot = Fraction(total_dens_str) + lin + rest + edge
    return tot, lin, rest, edge, tot <= TAU


def jobs_all():
    out = []
    for ver, pat in cc.runs.items():
        m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
        for name, blk in m["blocks"].items():
            out.append((ver, name, blk["instrument"]))
    return out


if __name__ == "__main__":
    if "--executar" not in sys.argv:
        sys.exit("Execução bloqueada: exige --executar (DECLARACAO_CERT_ORDENADAS §4, após testes e revisão).")
    t0 = time.time()
    with Pool(3) as pool:
        res = []
        for r in pool.imap_unordered(block_job, jobs_all()):
            print(r["versao"], r["bloco"], "%.0fs" % (r["segundos_reconstrucao"] + r["segundos_pares"]), flush=True); res.append(r)
    blocos4, tab4 = cx.exec4_tables()
    tdens = {(t["versao"], t["bloco"], t["p"], t["r"]): t for t in csv.DictReader(open(BASE + "cert_densidade_tabela.csv"))}
    stop = []; rows = []; brows = []
    for r in sorted(res, key=lambda x: (x["versao"], x["bloco"])):
        if float(blocos4[(r["versao"], r["bloco"])]["rho"]) != r["rho"]: stop.append((r["versao"], r["bloco"], "rho"))
        geo = r["geo"]
        brows.append({"versao": r["versao"], "bloco": r["bloco"], "nI": geo["nI"], "A_dec": geo["A_dec"], "B_dec": geo["B_dec"],
                      "eta": geo["eta"], "S2": geo["S2"], "rest_unit": geo["rest_unit"], "edge_unit": geo["edge_unit"],
                      "segundos": r["segundos_reconstrucao"] + r["segundos_pares"]})
        for k, c in enumerate(cc.catalog):
            key = (r["versao"], r["bloco"], str(c["prime"]), str(c["repetition"]))
            if float(tab4[key]["a_l1_sup"]) != r["a_l1"][k]: stop.append(key + ("a_l1",))
            tot, lin, rest, edge, ok = total_gamma(tdens[key]["total_densidade_sup"], tab4[key]["a_l1_sup"], r["Gsum"][k],
                                                   Fraction(geo["rest_unit"]), Fraction(geo["edge_unit"]), c["prime"], c["repetition"])
            rows.append({"versao": r["versao"], "bloco": r["bloco"], "p": c["prime"], "r": c["repetition"],
                         "eligible": tdens[key]["eligible"], "total_densidade_sup": tdens[key]["total_densidade_sup"],
                         "certificado_densidade": tdens[key]["certificado"],
                         "lin_rel_sup": cc.sup_chk(cc.iv_frac(lin), 15), "resto_rel_sup": cc.sup_chk(cc.iv_frac(rest), 15),
                         "borda_rel_sup": cc.sup_chk(cc.iv_frac(edge), 15), "total_ordenadas_sup": cc.sup_chk(cc.iv_frac(tot), 15),
                         "certificado": ok})
    summ = {"declaracao_sha256": open(BASE + "DECLARACAO_CERT_ORDENADAS.sha256").read().split()[0], "bases": SHAS,
            "tabela_bruta_sha256": RAW_SHA, "parada_bit_a_bit": stop, "tempo_s": time.time() - t0}
    if stop:
        summ["leitura"] = "INTERROMPIDA: reconstrução diverge da execução 4; nenhum par lido como certificado"
    else:
        E = [x for x in rows if x["eligible"] == "True"]
        summ.update({"pares": len(rows), "certificados": sum(x["certificado"] for x in rows),
                     "elegiveis": len(E), "elegiveis_certificados": sum(x["certificado"] for x in E),
                     "max_total_elegiveis_sup": float(max(Fraction(x["total_ordenadas_sup"]) for x in E)),
                     "max_lin_elegiveis_sup": float(max(Fraction(x["lin_rel_sup"]) for x in E)),
                     "perdidos_elegiveis_frente_densidade": sum(1 for x in E if x["certificado_densidade"] == "True" and not x["certificado"])})
    with open(BASE + "cert_ordenadas_blocos.csv", "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(brows[0].keys())); wr.writeheader(); wr.writerows(brows)
    with open(BASE + "cert_ordenadas_tabela.csv", "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
    json.dump(summ, open(BASE + "cert_ordenadas_resumo.json", "w"), indent=1, default=str)
    print(json.dumps(summ, indent=1, default=str))
