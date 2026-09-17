"""
Certificação computacional (condicional a RH) da condição suficiente em (d1, Δ) = (8, 2),
conforme results/etapa11_r5/DECLARACAO_CERT.md (hash verificado).

Base de confiança: (i) IEEE-754 binary64 (+, −, ×, ÷, nextafter) no numpy; (ii) arredondamento dirigido de mpmath.iv;
(iii) inteiros exatos do Python; (iv) crivo conferido por implementação independente.
"""
import csv, glob, hashlib, json, math, sys, time
from multiprocessing import Pool
import numpy as np
from mpmath import iv, mpf

sys.path.insert(0, "src"); sys.path.insert(0, "results/etapa11_3b")
from riemann_spectra.periods import measure_window_response
from riemann_spectra.arithmetic import prime_power_catalog
from interval_export import sup_str

DECL = "results/etapa11_r5/DECLARACAO_CERT.md"
assert hashlib.sha256(open(DECL, "rb").read()).hexdigest() == open("results/etapa11_r5/DECLARACAO_CERT.sha256").read().split()[0]
iv.dps = 30
TAU = 1e-6; D1 = 8; DELTA = 2; U1 = 13; U2 = 15
CELL = 1.0/256                                     # δ exato em binário; bordas 13 + i/256 exatas
NCELL = int(round((U2 - U1)/CELL))                 # 512
EPS = np.finfo(float).eps
INF = np.inf
runs = {"m4-v1": "results/run_20260913_144429_m3_b01*", "m4-v2": "results/run_20260913_173045_m3_c01*", "m4-v3": "results/run_20260913_220906_m3_d01*"}

# ---------------------------------------------------------------- intervalos numpy (lo, hi), arredondamento para fora
def dn(x): return np.nextafter(x, -INF)
def up(x): return np.nextafter(x, INF)

class I:
    __slots__ = ("lo", "hi")
    def __init__(self, lo, hi=None):
        self.lo = np.asarray(lo, float); self.hi = np.asarray(lo if hi is None else hi, float)
    def __add__(s, o):
        o = o if isinstance(o, I) else I(o); return I(dn(s.lo + o.lo), up(s.hi + o.hi))
    def __sub__(s, o):
        o = o if isinstance(o, I) else I(o); return I(dn(s.lo - o.hi), up(s.hi - o.lo))
    def __neg__(s): return I(-s.hi, -s.lo)
    def __mul__(s, o):
        o = o if isinstance(o, I) else I(o)
        p = (s.lo*o.lo, s.lo*o.hi, s.hi*o.lo, s.hi*o.hi)
        return I(dn(np.minimum.reduce(p)), up(np.maximum.reduce(p)))
    def inv(s):
        assert np.all((s.lo > 0) | (s.hi < 0)), "divisão por intervalo com zero"
        return I(dn(1.0/s.hi), up(1.0/s.lo))
    def __truediv__(s, o):
        o = o if isinstance(o, I) else I(o); return s*o.inv()
    def mag(s): return np.maximum(np.abs(s.lo), np.abs(s.hi))
    def __getitem__(s, k): return I(s.lo[k], s.hi[k])

def isum(x, axis):
    """Soma intervalar rigorosa de m termos em qualquer ordem: erro ≤ 2mε·Σ|x| calculada (mε ≤ 0,1)."""
    m = x.lo.shape[axis]; assert m*EPS <= 0.1
    f = 2*m*EPS
    elo = up(f*np.sum(np.abs(x.lo), axis=axis)); ehi = up(f*np.sum(np.abs(x.hi), axis=axis))
    return I(dn(np.sum(x.lo, axis=axis) - elo), up(np.sum(x.hi, axis=axis) + ehi))

def ivf(z):
    """mpmath iv → I escalar, para fora."""
    return I(dn(float(mpf(z.a))), up(float(mpf(z.b))))

def matmul(A, B, chunk=8):
    """Produto intervalar A (p×q) · B (q×r), linha a linha."""
    p = A.lo.shape[0]; r = B.lo.shape[1]
    out_lo = np.empty((p, r)); out_hi = np.empty((p, r))
    for s0 in range(0, p, chunk):
        a = I(A.lo[s0:s0+chunk, :, None], A.hi[s0:s0+chunk, :, None])
        b = I(B.lo[None, :, :], B.hi[None, :, :])
        c = isum(a*b, axis=1)
        out_lo[s0:s0+chunk] = c.lo; out_hi[s0:s0+chunk] = c.hi
    return I(out_lo, out_hi)

# ---------------------------------------------------------------- W exato (mpmath.iv)
PI = iv.pi
def W_iv(om, L):
    v = om*L/(2*PI); L2 = L/2
    vm = max(abs(mpf(v.a)), abs(mpf(v.b)))
    def sinc_small(x):                            # x intervalo com |x| < 1e-3
        xm = max(abs(mpf(x.a)), abs(mpf(x.b)))
        return iv.mpf([1 - (iv.pi*xm)**2/6, 1]) if xm > 0 else iv.mpf(1)
    if vm < mpf("1e-3"):
        return L2*sinc_small(v)/(1 - v**2)
    av = iv.mpf([min(abs(mpf(v.a)), abs(mpf(v.b))), vm])
    if mpf(v.a) > 0 and mpf(v.b) < 0: raise AssertionError
    if abs(vm - 1) < mpf("1e-3") and (mpf(v.a) > 0 or mpf(v.b) < 0):
        return L2*sinc_small(av - 1)/(av*(av + 1))
    return L2*iv.sin(PI*v)/(PI*v*(1 - v**2))

# ---------------------------------------------------------------- crivo (duas implementações)
def sieve_a(N):
    s = np.ones(N + 1, bool); s[:2] = False
    for i in range(2, int(N**0.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0].astype(np.int64)

def sieve_b(N, seg=1 << 16):
    r = math.isqrt(N); small = [p for p in range(2, r + 1) if all(p % q for q in range(2, math.isqrt(p) + 1))]
    out = []
    for lo in range(0, N + 1, seg):
        hi = min(N + 1, lo + seg); mark = bytearray([1])*(hi - lo)
        for p in small:
            st = max(p*p, ((lo + p - 1)//p)*p)
            for m in range(st, hi, p): mark[m - lo] = 0
        for i, f in enumerate(mark):
            n = lo + i
            if f and n >= 2: out.append(n)
    return np.array(out, dtype=np.int64)

# ---------------------------------------------------------------- somas por célula Σ Λ(n) n^{-1/2} (iv)
def cell_sums():
    Xb = [iv.exp(iv.mpf(U1) + iv.mpf(i)/256) for i in range(NCELL + 1)]
    lo_int = [int(math.floor(mpf(x.a))) for x in Xb]; hi_int = [int(math.floor(mpf(x.b))) for x in Xb]
    N = hi_int[-1]
    pa = sieve_a(N); pb = sieve_b(N)
    sieve_ok = bool(len(pa) == len(pb) and np.array_equal(pa, pb))
    assert sieve_ok
    logp = {}
    terms = {}
    for p in pa.tolist():
        q = p
        while q <= N:
            if q > lo_int[0]: terms[q] = p
            q *= p
    S = []
    ns = sorted(terms)
    import bisect
    for i in range(NCELL):
        a = bisect.bisect_right(ns, lo_int[i]); b = bisect.bisect_right(ns, hi_int[i + 1])
        acc = iv.mpf(0)
        for n in ns[a:b]:
            p = terms[n]
            if p not in logp: logp[p] = iv.log(p)
            acc += logp[p]/iv.sqrt(n)
        S.append(acc)
    amb = sum(1 for i in range(NCELL + 1) if lo_int[i] != hi_int[i])
    return S, {"N": N, "n_primos": int(len(pa)), "crivo_conferido": sieve_ok, "n_potencias": len(ns), "bordas_ambiguas": amb}

# ---------------------------------------------------------------- bloco
_prev = json.load(open("results/etapa11_r5/prh_forca_resumo.json"))
catalog = prime_power_catalog(0.5, 5.0); K = len(catalog)
Tflt = np.array([c["period_theoretical"] for c in catalog])

def block(args):
    ver, name, ins, cellS_hi = args
    t0 = time.time()
    A = ins["A"]; B = ins["B"]; Ec = ins["E_c"]; L = B - A
    h = 0.5*measure_window_response(L)["fwhm"]
    t = np.unique(np.concatenate([np.linspace(x - h, x + h, 9) for x in Tflt])); J = len(t)
    Liv = iv.mpf(L); Eciv = iv.mpf(Ec)
    Tiv = [iv.log(c["prime"]**c["repetition"]) for c in catalog]
    # ---- Passo 1: entradas de M^math
    Wm_lo = np.empty((J, K)); Wm_hi = np.empty((J, K)); Wp_lo = np.empty((J, K)); Wp_hi = np.empty((J, K))
    for i in range(J):
        ti = iv.mpf(float(t[i]))
        for j in range(K):
            a = ivf(W_iv(ti - Tiv[j], Liv)); b = ivf(W_iv(ti + Tiv[j], Liv))
            Wm_lo[i, j], Wm_hi[i, j] = a.lo, a.hi; Wp_lo[i, j], Wp_hi[i, j] = b.lo, b.hi
    cph = [ivf(iv.cos(Eciv*Tiv[j])) for j in range(K)]; sph = [ivf(iv.sin(Eciv*Tiv[j])) for j in range(K)]
    C = I(np.array([c.lo for c in cph]), np.array([c.hi for c in cph])); Sn = I(np.array([c.lo for c in sph]), np.array([c.hi for c in sph]))
    Wm = I(Wm_lo, Wm_hi); Wp = I(Wp_lo, Wp_hi); half = I(0.5)
    SP = (Wm + Wp)*half; DF = (Wm - Wp)*half
    ReGH = SP*C[None, :]; ImGH = DF*Sn[None, :]          # G+H
    ReiGH = -(SP*Sn[None, :]); ImiGH = DF*C[None, :]      # i(G−H)
    M = I(np.vstack([np.hstack([ReGH.lo, ReiGH.lo]), np.hstack([ImGH.lo, ImiGH.lo])]),
          np.vstack([np.hstack([ReGH.hi, ReiGH.hi]), np.hstack([ImGH.hi, ImiGH.hi])]))
    Mt = I(M.lo.T.copy(), M.hi.T.copy())
    # ---- Passo 2: posto e inversa
    G = matmul(Mt, M)
    R = np.linalg.inv(0.5*(G.lo + G.hi))
    RG = matmul(I(R), G)
    E = I(np.eye(2*K)) - RG
    rho = float(np.max(up(isum(I(E.mag()), axis=1).hi)))
    assert rho < 1, rho
    e = float(up(up(rho)/dn(1 - rho)))
    # ---- Passo 3: linhas
    Y = matmul(I(R), Mt)                                   # 94 × 846
    ynorm = isum(I(Y.mag()), axis=1).hi                    # sup ‖y_i‖₁
    ymax_col = np.max(Y.mag(), axis=0)                      # max_i |y_ij|
    a_l1 = up(ynorm[:K] + up(e*np.max(ynorm)))
    rad = up(e*ymax_col)
    Arows = I(dn(Y.lo[:K] - rad[None, :]), up(Y.hi[:K] + rad[None, :]))
    # diagnóstico: ‖â_k‖₁ em ponto flutuante do código
    # ---- Passo 4: S^abs
    th = [ivf(iv.cos(iv.mpf(float(t[j]))*Liv/2)) for j in range(J)]; thS = [ivf(iv.sin(iv.mpf(float(t[j]))*Liv/2)) for j in range(J)]
    cosT = I(np.array([x.lo for x in th]), np.array([x.hi for x in th])); sinT = I(np.array([x.lo for x in thS]), np.array([x.hi for x in thS]))
    lam = ivf(Liv/(2*PI)); kap8 = ivf(Liv/(8*PI))
    tmax = float(np.max(t)); assert tmax < 5.0
    vmin_global = dn(lam.lo*dn(U1 - tmax)); assert vmin_global >= math.sqrt(2)
    aR = Arows[:, :J]; aI = Arows[:, J:]
    cA_re = aR*cosT[None, :] + aI*sinT[None, :]; cA_im = aR*sinT[None, :] - aI*cosT[None, :]   # ᾱ e^{+iθ}
    cB_re = aR*cosT[None, :] - aI*sinT[None, :]; cB_im = -(aR*sinT[None, :]) - aI*cosT[None, :]  # ᾱ e^{−iθ}
    supQ = np.zeros((K, NCELL))
    for ci in range(NCELL):
        ulo = U1 + ci*CELL; uc = ulo + CELL/2                  # exatos em binário
        vmn = dn(lam.lo*dn(ulo - tmax))
        dR = up(12.0/dn(vmn**4))                               # |R′| ≤ 12|v|⁻⁴
        acc = np.zeros(K)
        for sgn in (-1.0, 1.0):
            tu = I(dn(t + sgn*uc), up(t + sgn*uc))
            v = tu*lam
            Rv = (v*(v*v - I(1.0))).inv()
            for cre, cim in ((cA_re, cA_im), (cB_re, cB_im)):
                pr = isum(cre*Rv[None, :], axis=1); pi_ = isum(cim*Rv[None, :], axis=1)
                acc = up(acc + up(pr.mag() + pi_.mag()))
        acc = up(kap8.hi*acc)                                   # |Q| ≤ (L/8π)Σ|P| no centro
        deriv = up(kap8.hi*up(4*up(up(lam.hi*a_l1)*dR)))       # 4 funções P, cada |P′| ≤ λ‖a‖₁·12|v|⁻⁴
        supQ[:, ci] = up(acc + up(deriv*(CELL/2)))
    Sabs = np.zeros(K)
    for ci in range(NCELL):
        Sabs = up(Sabs + up(supQ[:, ci]*cellS_hi[ci]))
    Sabs = up(Sabs/dn(math.pi))                                 # 1/π com π inferior em float
    return {"versao": ver, "bloco": name, "L": L, "A": A, "B": B, "Ec": Ec, "h_hex": float(h).hex(),
            "nos_sha256": hashlib.sha256(t.tobytes()).hexdigest(), "J": J, "rho": rho, "e": e,
            "max_y_l1": float(np.max(ynorm)), "vmin": float(vmin_global), "a_l1_sup": a_l1.tolist(),
            "Sabs_sup": Sabs.tolist(), "segundos": time.time() - t0}

# ---------------------------------------------------------------- orçamento B^{RH″} (iv; Lema 4′ + Lema 5′ + Arq)
c1 = iv.mpf(_prev["c1_sup"]); c2 = iv.mpf(_prev["c2_sup"])
EPS0 = iv.mpf("0.1"); TMAX = iv.mpf(5); N6 = 31 + iv.mpf("10.5")*iv.log(13); LOG3 = iv.log(3)
def S1(J): return 1/iv.mpf(2*J - 1)**2 + 1/iv.mpf(2*(2*J - 1))
def sig(J):
    if J == 1: return LOG3/9 + (LOG3 + 1)/6
    y = iv.mpf(2*J - 1); return iv.log(y)/y**2 + (iv.log(y) + 1)/(2*y)
def S2(J): return LOG3*S1(J) + sig(J)

def BRH2(a, L, nus, d1=D1, Dl=DELTA):
    d1 = iv.mpf(d1); Dl = iv.mpf(Dl)
    lam = L/(2*PI); kap = L/(8*PI); CP = 4*PI**2*a/L**2
    U1_ = TMAX + d1; U2_ = U1_ + Dl; rho1 = 1 + TMAX/d1; L0 = CP/(2*d1**2)
    def mn(x, y): return iv.mpf(min(mpf(x.b), mpf(y.b)))
    L2 = CP*( c2/Dl**2*mn(Dl/d1**3, 1/(2*d1**2)) + 24/d1**4 + 12*c1/Dl*mn(Dl/d1**4, 1/(3*d1**3))
             + EPS0**2*(1/(2*d1**2) + 2*c1*rho1/Dl*mn(Dl/d1**2, 1/d1) + 6*rho1/d1**2)
             + rho1**2*(1/(4*iv.e*d1**4) + EPS0**4*iv.sqrt(PI/2)) )
    ratio = mpf((L2/L0).b); Jw = 1
    while (2*Jw - 1)**2 < ratio: Jw += 1
    Arq = iv.exp(-U1_/2)*(1 + 1/(1 - iv.exp(-U1_)))*L0
    Zp = iv.mpf(0); Pol = iv.mpf(0)
    for nu in nus:
        lg = iv.log(nu + 8)
        far = L2*(3*N6/(nu - 6)**2 + 2*N6/nu**2 + iv.mpf("5.25")*(iv.log(nu + 2) + 1)/(nu + 2))
        inner = sum((lg + iv.log(1 + 2*j) for j in range(1, Jw)), iv.mpf(0))
        Zp += 2*(iv.mpf("10.5")*lg*L0 + 21*(L0*inner + L2*(lg*S1(Jw) + S2(Jw))) + far)
        s2 = U2_ - TMAX
        Pol += (iv.exp(-U1_/2)*L0
                + iv.exp(U2_/2)*(CP/s2**3/nu + (EPS0**2*U2_*CP/s2**3 + 6*CP/s2**4 + L2)/nu**2)
                + 2*kap*a*(4*iv.exp(U2_/2)/(nu*(lam*s2)**3) + 2*iv.sqrt(2*PI)*(lam*nu)**(-3)*EPS0**5*iv.exp(-(nu**2 - iv.mpf(1)/4)/(2*EPS0**2))))
    return (Zp/2 + Pol + Arq)/PI, Jw

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    t0 = time.time()
    S, sinfo = cell_sums()
    cellS_hi = np.array([up(float(mpf(x.b))) for x in S])
    print("somas por célula:", sinfo, "%.0fs" % (time.time() - t0), flush=True)
    jobs = []
    for ver, pat in runs.items():
        m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
        for name, blk in m["blocks"].items():
            if only and name != only: continue
            jobs.append((ver, name, blk["instrument"], cellS_hi))
    with Pool(3) as pool:
        res = []
        for r in pool.imap_unordered(block, jobs):
            print(r["versao"], r["bloco"], "rho %.3e vmin %.1f %.0fs" % (r["rho"], r["vmin"], r["segundos"]), flush=True); res.append(r)
    elig = {(r["versao"], r["bloco"], int(r["p"]), int(r["r"])): r["eligible"] == "True" for r in csv.DictReader(open("results/etapa11_r5/cruzamento_tabela.csv"))}
    key = lambda r: (r["versao"], r["bloco"], int(r["p"]), int(r["r"]))
    prh2 = {key(r): r for r in csv.DictReader(open("results/etapa11_r5/prh2_forca_tabela.csv")) if r["d1"] == "8" and r["Delta"] == "2"}
    theta = {key(r): r for r in csv.DictReader(open("results/etapa11_r5/theta_tabela.csv")) if r["d1"] == "8" and r["Delta"] == "2"}
    prh3 = {key(r): r for r in csv.DictReader(open("results/etapa11_r5/prh3_tabela.csv")) if r["d1"] == "8" and r["Delta"] == "2"}
    rows = []; brows = []
    for b in sorted(res, key=lambda r: (r["versao"], r["bloco"])):
        Liv = iv.mpf(b["L"]); Eciv = iv.mpf(b["Ec"]); nus = [Eciv - Liv/2, Eciv + Liv/2]
        brows.append({k: b[k] for k in ["versao", "bloco", "L", "h_hex", "nos_sha256", "J", "rho", "e", "max_y_l1", "vmin", "segundos"]})
        for k, c in enumerate(catalog):
            a = iv.mpf(b["a_l1_sup"][k])
            Bv, Jw = BRH2(a, Liv, nus)
            n = c["prime"]**c["repetition"]; ck = iv.log(c["prime"])/(PI*iv.sqrt(n))
            ck_inf = iv.mpf(mpf(ck.a))
            tot = (Bv + iv.mpf(b["Sabs_sup"][k]))/ck_inf
            kk = (b["versao"], b["bloco"], c["prime"], c["repetition"])
            tot_s = sup_str(tot, 15)
            rows.append({"versao": b["versao"], "bloco": b["bloco"], "p": c["prime"], "r": c["repetition"], "eligible": elig[kk],
                         "a_l1_sup": b["a_l1_sup"][k], "a_l1_float": float(prh2[kk]["a_l1"]),
                         "a_l1_dif_rel": b["a_l1_sup"][k]/float(prh2[kk]["a_l1"]) - 1,
                         "B_rel_sup": sup_str(Bv/ck_inf, 15), "Sabs_rel_sup": sup_str(iv.mpf(b["Sabs_sup"][k])/ck_inf, 15),
                         "Sabs_rel_float": float(theta[kk]["S_abs"])/float(theta[kk]["abs_c"]),
                         "total_sup": tot_s, "orcamento2_hibrido": float(prh3[kk]["orcamento2"]),
                         "certificado": mpf(tot.b) <= mpf(TAU) and b["rho"] < 1 and b["vmin"] >= math.sqrt(2) and sinfo["crivo_conferido"]})
    out = "_teste" if only else ""
    with open(f"results/etapa11_r5/cert_blocos{out}.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(brows[0].keys())); w.writeheader(); w.writerows(brows)
    with open(f"results/etapa11_r5/cert_tabela{out}.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    E = [r for r in rows if r["eligible"]]
    summ = {"declaracao_sha256": open("results/etapa11_r5/DECLARACAO_CERT.sha256").read().split()[0],
            "celulas": {"delta": CELL, "n": NCELL, **sinfo},
            "rho_max": max(b["rho"] for b in brows), "vmin_min": min(b["vmin"] for b in brows),
            "pares": len(rows), "certificados": sum(r["certificado"] for r in rows),
            "elegiveis": len(E), "elegiveis_certificados": sum(r["certificado"] for r in E),
            "max_total_elegiveis": max(float(r["total_sup"]) for r in E) if E else None,
            "max_total_todos": max(float(r["total_sup"]) for r in rows),
            "max_a_l1_dif_rel": max(abs(r["a_l1_dif_rel"]) for r in rows),
            "max_razao_Sabs_cert_float": max(float(r["Sabs_rel_sup"])/r["Sabs_rel_float"] for r in rows),
            "max_razao_total_cert_hibrido": max(float(r["total_sup"])/r["orcamento2_hibrido"] for r in rows),
            "nao_certificados_elegiveis": [(r["versao"], r["bloco"], r["p"], r["r"], r["total_sup"]) for r in E if not r["certificado"]],
            "tempo_total_s": time.time() - t0}
    json.dump(summ, open(f"results/etapa11_r5/cert_resumo{out}.json", "w"), indent=1, default=str)
    print(json.dumps({k: v for k, v in summ.items() if k != "nao_certificados_elegiveis"}, indent=1, default=str))
    print("não certificados elegíveis:", len(summ["nao_certificados_elegiveis"]))
