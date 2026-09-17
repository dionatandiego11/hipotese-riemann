"""Testes obrigatórios T1–T6 do adendo DECLARACAO_CERT_CORRECAO1.md (devem passar antes da reexecução)."""
import hashlib, importlib.util, json, re, sys
from fractions import Fraction
import numpy as np
from mpmath import iv

spec = importlib.util.spec_from_file_location("cc", "results/etapa11_r5/cert_calculo.py")
cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
res = {}

def intersect(x, y):
    return not (cc.hi_q(x) < cc.lo_q(y) or cc.hi_q(y) < cc.lo_q(x))

def ref_W(vstr, Lstr):
    old = iv.dps; iv.dps = 80
    try:
        v = iv.mpf(vstr); L = iv.mpf(Lstr)
        r = (L/2)*iv.sin(iv.pi*v)/(iv.pi*v*(1 - v**2))
        return iv.make_mpf(r._mpi_)
    finally:
        iv.dps = old

# T1
Ls = ["2", repr(2519.123430304), "10000"]
vs = []
for d in ["1e-15", "1e-12", "1e-8", "5e-4", "9.99e-4", "1e-3", "1.001e-3"]:
    vs += [d, "-" + d]
for d in ["1e-15", "-1e-15", "1e-12", "-1e-12", "1e-8", "-1e-8", "9.99e-4", "-9.99e-4", "1e-3", "-1e-3", "1.001e-3", "-1.001e-3"]:
    for sg in ["", "-"]:
        vs.append(f"{sg}(1+{d})")
def val(s):  # string → decimal exato
    from decimal import Decimal, getcontext
    getcontext().prec = 60
    neg = s.startswith("-"); s = s.lstrip("-")
    if s.startswith("(1+"):
        x = Decimal(1) + Decimal(s[3:-1])
    else:
        x = Decimal(s)
    return str(-x if neg else x)
rng = np.random.default_rng(12345)
vs_rand = [repr(float(x)) for x in rng.uniform(-3, 3, 2000)]
fails = []; n = 0
for Ls_ in Ls:
    L30 = iv.mpf(Ls_)
    for s in vs + vs_rand:
        vv = val(s) if not s[0].isdigit() or "(" in s else s
        if s in vs: vv = val(s)
        ref = ref_W(vv, Ls_)
        v30 = iv.mpf(vv)
        w_v = cc.W_iv(v30*2*cc.PI/L30, L30)          # via ω intervalar
        n += 1
        if not intersect(w_v, ref): fails.append((Ls_, vv))
res["T1"] = {"casos": n, "falhas": fails[:10], "n_falhas": len(fails)}

# T2
f2 = []
for Ls_ in Ls:
    L30 = iv.mpf(Ls_); Lq = cc.lo_q(L30)
    for v, exact in [(0, Fraction(1, 2)), (1, Fraction(1, 4)), (-1, Fraction(1, 4))]:
        w = cc.W_iv(iv.mpf(v)*2*cc.PI/L30, L30)
        # contém L·exact? L30 é intervalo de largura ≥ 0; testa contra os extremos de L
        lo = cc.lo_q(w); hi = cc.hi_q(w)
        if not (lo <= cc.hi_q(L30)*exact and cc.lo_q(L30)*exact <= hi): f2.append((Ls_, v))
res["T2"] = {"falhas": f2}

# T3
f3 = []; cnt = 0
zs = [iv.log(c["prime"])/(cc.PI*iv.sqrt(c["prime"]**c["repetition"])) for c in cc.catalog]
for x in rng.uniform(-1e6, 1e6, 5000):
    zs.append(iv.mpf(repr(float(x)))/7 + iv.exp(iv.mpf(repr(float(x/1e6)))))
for x in rng.uniform(1e-300, 1e-290, 1000):
    zs.append(iv.mpf(repr(float(x)))/3)
for p in [2, 3, 5, 11, 139]:
    zs.append(iv.log(p)/(cc.PI*iv.sqrt(p)))
for z in zs:
    cnt += 1
    fz = cc.ivf(z)
    if not (Fraction(float(fz.lo)) <= cc.lo_q(z) and Fraction(float(fz.hi)) >= cc.hi_q(z)): f3.append("ivf")
    if not (Fraction(cc.float_dn(cc.lo_q(z))) <= cc.lo_q(z) and Fraction(cc.float_up(cc.hi_q(z))) >= cc.hi_q(z)): f3.append("float_dn/up")
    pl = cc.pt_lo(z)
    if not (cc.lo_q(pl) == cc.lo_q(z) and cc.hi_q(pl) == cc.lo_q(z) and cc.hi_q(pl) <= cc.hi_q(z)): f3.append("pt_lo")
res["T3"] = {"casos": cnt, "falhas": f3[:10], "n_falhas": len(f3)}

# T4
f4 = []
for a, b in [("1", "1e-20"), ("1", "-1e-20"), ("0.156012929039103601824", "1e-25"), ("7", "3e-29")]:
    x = iv.mpf(a) + iv.mpf(b); y = iv.mpf(a)
    for u, w in [(x, y), (y, x)]:
        m = None
        # reproduz mn de BRH2
        m = cc.pt_hi(u) if cc.hi_q(u) <= cc.hi_q(w) else cc.pt_hi(w)
        if cc.hi_q(m) < min(cc.hi_q(u), cc.hi_q(w)) or cc.lo_q(m) < 0 and False: f4.append((a, b))
        if cc.hi_q(m) != min(cc.hi_q(u), cc.hi_q(w)): f4.append(("exato", a, b))
res["T4"] = {"falhas": f4}

# T5
tot_up = iv.mpf("1e-6") + iv.mpf("1e-25"); tot_dn = iv.mpf("1e-6") - iv.mpf("1e-25")
res["T5"] = {"acima_decide_nao": not (cc.hi_q(tot_up) <= Fraction(1, 10**6)), "abaixo_decide_sim": cc.hi_q(tot_dn) <= Fraction(1, 10**6)}

# T6
src = open("results/etapa11_r5/cert_calculo.py").read()
bad = [ln for ln in src.splitlines() if re.search(r"(?<![\w.])mpf\(", ln) and not ln.strip().startswith(("Execução", "#"))]
bad += [ln for ln in src.splitlines() if re.search(r"\.(a|b)\)", ln)]
res["T6"] = {"linhas_suspeitas": bad}

ok = (res["T1"]["n_falhas"] == 0 and not res["T2"]["falhas"] and res["T3"]["n_falhas"] == 0 and not res["T4"]["falhas"]
      and res["T5"]["acima_decide_nao"] and res["T5"]["abaixo_decide_sim"] and not res["T6"]["linhas_suspeitas"])
res["todos_passaram"] = ok
res["script_sha256"] = hashlib.sha256(src.encode()).hexdigest()
json.dump(res, open("results/etapa11_r5/cert_testes_resultado.json", "w"), indent=1, default=str)
print(json.dumps(res, indent=1, default=str))
sys.exit(0 if ok else 1)
