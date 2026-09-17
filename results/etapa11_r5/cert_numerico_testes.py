"""
Testes T1–T34 de DECLARACAO_CERT_NUMERICO.md §3 (antes de --executar).

Desvio de redação fixado ANTES de rodar (registrado no resultado):
  T30: a declaração previa comparar os momentos com mpmath.quad a 60 dígitos. Com ωa ~ 10³ oscilações a quadratura
       adaptativa é impraticável (dezenas de minutos por par). Substituído pela primitiva fechada
       ∫ x^m e^{cx} dx = e^{cx} Σ_{k=0}^{m} (−1)^k m!/(m−k)! x^{m−k}/c^{k+1}, c = −iω, avaliada em mpmath.mpc a 60 dígitos —
       forma independente da recorrência.
"""
import csv, glob, hashlib, json, math, os, shutil, subprocess, sys, time
from fractions import Fraction
import numpy as np
import mpmath
from mpmath import iv

sys.path.insert(0, "results/etapa11_r5")
import cert_numerico as cn
cc = cn.cc; co = cn.co; cx = cn.cx; BASE = cn.BASE
sys.path.insert(0, "src")
from riemann_spectra.periods import OscillatoryTransform, direct_exponential_sum, window_values
from riemann_spectra import arithmetic as ar

res = {"desvios_de_redacao_fixados_antes": [
    "T30: primitiva fechada em mpmath.mpc (60 dígitos) no lugar de mpmath.quad (impraticável com ωa ~ 10³)"]}
t_start = time.time()
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
WATCH = ["cert_calculo.py", "cert_contaminacao.py", "cert_densidade.py", "cert_ordenadas.py", "DECLARACAO_CERT_NUMERICO.md",
         "cert_testes_resultado.json", "cert_contaminacao_testes_resultado.json", "cert_densidade_testes_resultado.json",
         "cert_ordenadas_testes_resultado.json", "cert_ordenadas_tabela.csv"]
res["hashes_inicio"] = {f: sha(BASE + f) for f in WATCH}; res["hashes_inicio"]["data/raw/zeros1"] = sha(co.RAW)

def strip_times(o):
    if isinstance(o, dict): return {k: strip_times(v) for k, v in o.items() if not k.startswith("segundos")}
    if isinstance(o, list): return [strip_times(v) for v in o]
    return o

def diff_paths(a, b, path=""):
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in set(a) | set(b):
            if k not in a or k not in b: out.append(path + "/" + k)
            else: out += diff_paths(a[k], b[k], path + "/" + k)
        return out
    return [] if a == b else [path]

# ---------------------------------------------------------------- T1–T27
orig = BASE + "cert_ordenadas_testes_resultado.json"; bak = BASE + ".cert_ordenadas_testes_resultado.json.bak"
content_orig = json.load(open(orig)); sha_orig = sha(orig); shutil.copy2(orig, bak)
t0 = time.time()
proc = subprocess.run([sys.executable, BASE + "cert_ordenadas_testes.py"], capture_output=True, text=True)
regen = json.load(open(orig)); shutil.copy2(bak, orig); os.remove(bak)
dpaths = sorted(diff_paths(strip_times(regen), strip_times(content_orig)))
ord_out_exist = all(os.path.exists(BASE + f) for f in ["cert_ordenadas_tabela.csv", "cert_ordenadas_blocos.csv", "cert_ordenadas_resumo.json"])
oks = {k: regen[k]["ok"] for k in ["T1_T21", "T22", "T24", "T25", "T26", "T27"]}
res["T1_T27"] = {"exit": proc.returncode, "todos_passaram_regenerado": regen.get("todos_passaram"), "oks": oks,
                 "hashes_intocados_regenerado": regen["hashes_intocados"], "chaves_que_diferem_sem_tempos": dpaths,
                 "nenhuma_saida_regenerado": regen["nenhuma_saida_de_execucao_criada"], "saidas_de_ordenadas_existem": ord_out_exist,
                 "arquivo_vigente_restaurado": sha(orig) == sha_orig, "segundos": time.time() - t0}
res["T1_T27"]["ok"] = bool(set(dpaths) <= {"/nenhuma_saida_de_execucao_criada", "/todos_passaram"} and regen["nenhuma_saida_de_execucao_criada"] is False
                           and ord_out_exist and all(oks.values()) and regen["hashes_intocados"] and res["T1_T27"]["arquivo_vigente_restaurado"])

# ---------------------------------------------------------------- T28 leitura dos registrados
cat = {(c["prime"], c["repetition"]) for c in cc.catalog}
T28 = {"blocos": 0, "linhas_ok": True, "ida_e_volta_falhas": 0, "primario_band_conjugate": True}
blocks = []
for ver, pat in cc.runs.items():
    m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
    for name, blk in m["blocks"].items():
        blocks.append((ver, name, blk))
        reg = cn.registered(ver, name); T28["blocos"] += 1
        if set(reg) != cat or len(reg) != 47: T28["linhas_ok"] = False
        T28["ida_e_volta_falhas"] += sum(1 for s in reg.values() if repr(float(s)) != s)
        if blk["arithmetic"]["targeted_fit"]["primary_estimator"] != "band_conjugate": T28["primario_band_conjugate"] = False
T28["ok"] = T28["blocos"] == 30 and T28["linhas_ok"] and T28["ida_e_volta_falhas"] == 0 and T28["primario_band_conjugate"]
res["T28"] = T28

# ---------------------------------------------------------------- blocos de teste: T29, T32, T33 (b01, c01, d01)
raw = co.load_raw(); _, zf = co.load_processed_floats()
cfg_rows = {}
T29 = {}; T32 = {}; T33 = {}
for ver, name in [("m4-v1", "b01"), ("m4-v2", "c01"), ("m4-v3", "d01")]:
    blk = [b for v, n, b in blocks if v == ver and n == name][0]; ins = blk["instrument"]
    geo = co.block_geometry(ins, raw, zf)
    g = zf[geo["lo"]:geo["hi"] + 1]
    tr = OscillatoryTransform(float(g[0]), float(g[-1]), 0.5, 5.0, points_per_fwhm=8.0, panel_length=0.5, quad_order=8, density="rvm", window="hann")
    # T29: reprodução do ajuste primário
    try:
        catalog = ar.prime_power_catalog(float(tr.t_grid[0]), float(tr.t_grid[-1]))
        half = 0.5*tr.response["fwhm"]
        fit = ar.targeted_joint_fit(lambda t: tr.evaluate(g, t), catalog, tr.L, tr.E_c, half_width=half, window=tr.window,
                                    sampling="band", include_conjugate=True)
        reg = cn.registered(ver, name)
        diffs = [abs(f["ratio_to_theory"] - float(reg[(c["prime"], c["repetition"])])) for f, c in zip(fit, catalog)]
        T29[f"{ver}/{name}"] = {"bit_a_bit_iguais": sum(d == 0.0 for d in diffs), "de": len(diffs), "max_diferenca": max(diffs)}
    except Exception as e:
        T29[f"{ver}/{name}"] = {"erro": repr(e)}
    # reconstrução + termo suave enclausurado
    rec = cx.reconstruct(ins)
    K, rhoK = cn.K_rule(Fraction(ins["B"] - ins["A"])/2, Fraction(ins["E_c"]))
    Sre_lo, Sre_hi, Sim_lo, Sim_hi, wS = cn.smooth_term(rec["t"], rec["L"], rec["Ec"], K, rhoK)
    Scode = direct_exponential_sum(tr._quad_u, tr._quad_coeffs, rec["t"], chunk=16)
    Smid = 0.5*(Sre_lo + Sre_hi) + 1j*0.5*(Sim_lo + Sim_hi)
    T32[f"{ver}/{name}"] = {"K": K, "largura_S_max": wS, "max_|S_enclausurado − S_codigo|": float(np.max(np.abs(Smid - Scode))),
                            "max_|S|": float(np.max(np.abs(Smid)))}
    # T33: parte discreta em 50 zeros
    idx = [int(round(geo["lo"] + i*(geo["hi"] - geo["lo"])/49)) for i in range(50)]
    Dre, Dim = cn.discrete_term(rec["t"], geo, raw, indices=idx)
    sel = zf[idx]; u = sel - tr.E_c; w = window_values(sel, tr.A, tr.B, tr.window)
    Dcode = direct_exponential_sum(u, w, rec["t"])
    Dmid = 0.5*(Dre.lo + Dre.hi) + 1j*0.5*(Dim.lo + Dim.hi)
    T33[f"{ver}/{name}"] = {"max_|D_enclausurado − D_codigo|": float(np.max(np.abs(Dmid - Dcode))),
                            "largura_D_max": float(max(np.max(Dre.hi - Dre.lo), np.max(Dim.hi - Dim.lo)))}
res["T29_diagnostico"] = T29
res["T32_diagnostico"] = T32
res["T33_diagnostico"] = T33

# ---------------------------------------------------------------- T30 momentos × primitiva fechada
mpmath.mp.dps = 60
rng = np.random.default_rng(20260917)
T30 = []; worst30 = 0.0; contains = True
for i in range(20):
    ver, name, blk = blocks[int(rng.integers(0, 30))]; ins = blk["instrument"]
    L = ins["B"] - ins["A"]; a = Fraction(L)/2
    h = 0.5*cc.measure_window_response(L)["fwhm"]
    t = np.unique(np.concatenate([np.linspace(x - h, x + h, 9) for x in cc.Tflt]))
    K, _ = cn.K_rule(Fraction(L)/2, Fraction(ins["E_c"]))
    m_ = int(rng.integers(0, K + 1)); tj = float(t[int(rng.integers(0, len(t)))])
    old = iv.dps; iv.dps = 60
    om_iv = iv.mpf(tj); C, S = cn.moments_CS(om_iv, cn.frac_to_iv(a), K)
    Jiv_re, Jiv_im = C[m_], -S[m_]
    iv.dps = old
    c = mpmath.mpc(0, -mpmath.mpf(tj)); A_ = mpmath.mpf(a.numerator)/a.denominator
    def prim(x):
        return mpmath.exp(c*x)*sum(((-1)**k)*mpmath.factorial(m_)/mpmath.factorial(m_ - k)*x**(m_ - k)/c**(k + 1) for k in range(m_ + 1))
    Jcl = prim(A_) - prim(-A_)
    tol = Fraction(str(abs(Jcl)*mpmath.mpf("1e-45"))) + Fraction(1, 10**45)   # precisão da primitiva fechada a 60 dígitos
    Jre = Fraction(str(mpmath.re(Jcl))); Jim = Fraction(str(mpmath.im(Jcl)))
    inside = (cc.lo_q(Jiv_re) <= Jre + tol and Jre - tol <= cc.hi_q(Jiv_re) and cc.lo_q(Jiv_im) <= Jim + tol and Jim - tol <= cc.hi_q(Jiv_im))
    rel = float(abs(mpmath.mpc(float(0.5*(cc.lo_q(Jiv_re) + cc.hi_q(Jiv_re))), float(0.5*(cc.lo_q(Jiv_im) + cc.hi_q(Jiv_im)))) - Jcl)/max(abs(Jcl), mpmath.mpf(1e-300)))
    contains = contains and inside; worst30 = max(worst30, rel)
    T30.append({"bloco": f"{ver}/{name}", "m": m_, "omega": tj, "fechada_dentro_do_intervalo": inside, "dif_rel_ponto_medio": rel})
res["T30"] = {"casos": T30, "todos_dentro": contains, "max_dif_rel": worst30, "ok": contains}

# ---------------------------------------------------------------- T31 resto, K e largura em todos os blocos
T31 = {"blocos": {}}; wmax = 0.0; t31 = time.time()
for ver, name, blk in blocks:
    ins = blk["instrument"]; L = ins["B"] - ins["A"]
    K, rhoK = cn.K_rule(Fraction(L)/2, Fraction(ins["E_c"]))
    h = 0.5*cc.measure_window_response(L)["fwhm"]
    t = np.unique(np.concatenate([np.linspace(x - h, x + h, 9) for x in cc.Tflt]))
    *_, wS = cn.smooth_term(t, L, ins["E_c"], K, rhoK)
    wmax = max(wmax, wS)
    T31["blocos"][f"{ver}/{name}"] = {"K": K, "rho_K": float(rhoK), "rho_K_le_1e-20": rhoK <= Fraction(1, 10**20), "largura_S_max": wS}
ys = rng.uniform(-0.113, 0.113, 1000); serr = 0
for y in ys:
    s = sum(((-1)**(m + 1))*y**m/m for m in range(1, 23)); b = abs(y)**23/(23*(1 - abs(y)))
    if abs(math.log1p(y) - s) > b + 1e-15: serr += 1
T31.update({"largura_S_max_global": wmax, "serie_log_violacoes_diag": serr, "segundos": time.time() - t31})
T31["ok"] = all(v["rho_K_le_1e-20"] and v["largura_S_max"] <= cn.WIDTH_S_MAX for v in T31["blocos"].values()) and serr == 0
res["T31"] = T31

# ---------------------------------------------------------------- T34 decisões e alarme
p, r = 2, 1
c_lo, c_hi = cn.c_interval(p, r)
X = Fraction(-1, 7)
tg = Fraction(1, 10**7)
cases = {}
q = X/c_lo - 1 if X/c_lo < X/c_hi else X/c_hi - 1
for label, delta, exp in [("igual", Fraction(0), True), ("acima_1e-25", Fraction(1, 10**25), False), ("abaixo_1e-25", -Fraction(1, 10**25), True)]:
    d0 = cn.decide(float(X), float(X), p, r, repr(1.0), f"{tg.numerator}/{tg.denominator}")
    eps = d0["eps_sup"]
    tgs = cn.TAU - eps + delta
    d = cn.decide(float(X), float(X), p, r, repr(1.0), f"{tgs.numerator}/{tgs.denominator}")
    cases[label] = {"esperado": exp, "obtido": d["T_certificado"]}
cfl = float(c_hi)
dA = cn.decide(cfl*1.5, cfl*1.5, p, r, repr(1.5), "1/1000000000")
cases["alarme_disparado_q≈0,5_total=1e-9"] = {"esperado": True, "obtido": dA["alarme"]}
dB = cn.decide(cfl, cfl, p, r, repr(1.0), "1/1000000")
cases["alarme_nao_disparado_q≈0"] = {"esperado": False, "obtido": dB["alarme"]}
res["T34"] = {"casos": cases, "ok": all(v["esperado"] == v["obtido"] for v in cases.values())}

# ---------------------------------------------------------------- integridade
res["hashes_fim"] = {f: sha(BASE + f) for f in WATCH}; res["hashes_fim"]["data/raw/zeros1"] = sha(co.RAW)
res["hashes_intocados"] = res["hashes_fim"] == res["hashes_inicio"]
res["nenhuma_saida_de_execucao_criada"] = not any(os.path.exists(BASE + f) for f in ["cert_numerico_tabela.csv", "cert_numerico_blocos.csv", "cert_numerico_resumo.json"])
res["todos_passaram"] = bool(res["T1_T27"]["ok"] and res["T28"]["ok"] and res["T30"]["ok"] and res["T31"]["ok"] and res["T34"]["ok"]
                             and res["hashes_intocados"] and res["nenhuma_saida_de_execucao_criada"])
res["nota"] = "T29, T32, T33 são diagnósticos registrados e não entram em todos_passaram (declaração §3)"
res["script_sha256"] = sha(BASE + "cert_numerico.py"); res["testes_sha256"] = sha(BASE + "cert_numerico_testes.py")
res["segundos_total"] = time.time() - t_start
json.dump(res, open(BASE + "cert_numerico_testes_resultado.json", "w"), indent=1, default=str)
print(json.dumps(res, indent=1, default=str))
sys.exit(0 if res["todos_passaram"] else 1)
