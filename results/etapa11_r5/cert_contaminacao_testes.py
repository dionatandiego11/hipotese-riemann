"""
Testes obrigatórios T1–T15 de DECLARACAO_CERT_CONTAMINACAO.md §3 (antes da execução completa).
T1–T9: cert_testes.py reaplicado (o arquivo de resultado da execução 4 é salvo e restaurado byte a byte).
"""
import csv, glob, hashlib, json, math, shutil, subprocess, sys, time
from fractions import Fraction
import numpy as np
from mpmath import iv

sys.path.insert(0, "results/etapa11_r5")
import cert_contaminacao as cx
cc = cx.cc
BASE = cx.BASE
res = {}
t_start = time.time()

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()

# ---------------------------------------------------------------- hashes
res["hashes_inicio"] = {"cert_calculo.py": sha(BASE + "cert_calculo.py"),
                        "DECLARACAO_CERT_CONTAMINACAO.md": sha(BASE + "DECLARACAO_CERT_CONTAMINACAO.md")}

# ---------------------------------------------------------------- T1–T9 (cert_testes.py, execução 4)
orig = BASE + "cert_testes_resultado.json"; bak = BASE + ".cert_testes_resultado.json.bak"
sha_orig = sha(orig); shutil.copy2(orig, bak)
t0 = time.time()
proc = subprocess.run([sys.executable, BASE + "cert_testes.py"], capture_output=True, text=True)
t19 = json.load(open(orig))
sha_regen = sha(orig)
shutil.copy2(bak, orig); import os; os.remove(bak)
assert sha(orig) == sha_orig
res["T1_T9"] = {"exit": proc.returncode, "todos_passaram": t19.get("todos_passaram"),
                "resumo": {k: ({kk: vv for kk, vv in v.items() if kk not in ("falhas", "a_cobertura", "b_falhas")} if isinstance(v, dict) else v)
                           for k, v in t19.items() if k.startswith("T")},
                "script_sha256_testado": t19.get("script_sha256"),
                "resultado_regenerado_identico_ao_da_execucao4": sha_regen == sha_orig,
                "arquivo_execucao4_restaurado": sha(orig) == sha_orig, "segundos": time.time() - t0}

# ---------------------------------------------------------------- T10 enumeração
terms1 = cx.regime1_terms()
S, info, ns2, terms2, lo_int, hi_int = cx.regime2_cells()
res["T10"] = {"floor_e5_e6_e13": [cx.N5, cx.N6, cx.N13], "floors_nao_ambiguos": True,
              "regime1_n_termos": len(terms1), "regime1_lista": [n for n, _ in terms1],
              "regime1_potencias_r2": [(n, p) for n, p in terms1 if n != p],
              "regime1_duas_enumeracoes_iguais": True, "regime2_crivo_duas_impl_iguais": info["crivo_conferido"],
              "ok": len(terms1) == 51 and info["crivo_conferido"]}

# ---------------------------------------------------------------- T11 cobertura
exp0 = iv.mpf(cx.U_II) + iv.mpf(0)/256; expN = iv.mpf(cx.U_II) + iv.mpf(cx.NCELL2)/256
exps_exatos = all(cc.lo_q(iv.mpf(cx.U_II) + iv.mpf(i)/256) == cc.hi_q(iv.mpf(cx.U_II) + iv.mpf(i)/256) == Fraction(cx.U_II) + Fraction(i, 256)
                  for i in range(cx.NCELL2 + 1))
# Correção de implementação do teste (16/09/2026): a versão anterior exigia min_regime2 == N6 + 1 = 404, mas 404 não é
# potência de primo (a menor acima de 403 é 409). A exigência declarada é: n ≤ N6 no regime I, n ≥ N6 + 1 no regime II,
# nenhum n fora ou em ambos. Verifica-se por completude e disjunção contra enumeração independente de (N5, N13].
_indep = cx.prime_powers(cx.N5, cx.N13, cc.sieve_b(cx.N13))
_r1 = {n for n, _ in terms1}; _r2 = set(ns2)
fronteira = {"max_regime1": max(_r1), "min_regime2": min(_r2), "N6": cx.N6,
             "uniao_igual_enumeracao_independente": (_r1 | _r2) == set(_indep), "disjuntos": not (_r1 & _r2),
             "n_total_5_13": len(_indep)}
res["T11"] = {**{k: info[k] for k in ["n_termos", "n_primos", "n_potencias_r2", "nao_atribuidos", "atribuidos_duas_celulas", "bordas_ambiguas"]},
              "n_celulas": cx.NCELL2, "expoente_primeira_borda": str(cc.lo_q(exp0)), "expoente_ultima_borda": str(cc.lo_q(expN)),
              "expoentes_das_bordas_exatos_e_contiguos": exps_exatos, "fronteira_u6": fronteira,
              "ok": (info["n_termos"] == 37210 and info["n_primos"] == 37049 and info["n_potencias_r2"] == 161 and info["nao_atribuidos"] == 0
                     and exps_exatos and cc.lo_q(exp0) == 6 and cc.lo_q(expN) == 13
                     and fronteira["max_regime1"] <= cx.N6 < fronteira["min_regime2"]
                     and fronteira["uniao_igual_enumeracao_independente"] and fronteira["disjuntos"])}

# ---------------------------------------------------------------- blocos de teste (T12, T13)
blocos4, tab4 = cx.exec4_tables()
def ins_of(ver, name):
    m = json.load(open(glob.glob(cc.runs[ver])[0] + "/metrics.json")); return m["blocks"][name]["instrument"]
TB = [("m4-v1", "b01"), ("m4-v2", "c01"), ("m4-v3", "d01")]
e7 = math.floor(cc.hi_q(iv.exp(7))); e12 = math.floor(cc.lo_q(iv.exp(12)))
low = [n for n in ns2 if n <= e7]; high = [n for n in ns2 if n > e12]
pick = lambda arr, m: [arr[int(round(i*(len(arr) - 1)/(m - 1)))] for i in range(m)]
sample12 = pick(low, 10) + pick(high, 10)
T12 = {"amostra_n": sample12, "blocos": {}}; T13 = {"blocos": {}}; bitexact = {}
recs = {}
for ver, name in TB:
    tb = time.time()
    ins = ins_of(ver, name); rec = cx.reconstruct(ins); recs[(ver, name)] = rec
    bitexact[f"{ver}/{name}"] = cx.bit_exact_vs_exec4(ver, name, rec, blocos4, tab4)
    supQ, vmins, margin_ok = cx.regime2_supQ(rec)
    viol = []; ratios = []
    for n in sample12:
        cells = cx.cell_of(n, lo_int, hi_int)
        qp = cx.q_pointwise(rec, n).mag()
        for ci in cells:
            bad = np.nonzero(qp > supQ[:, ci])[0]
            if len(bad): viol.append((n, ci, [int(b) for b in bad]))
            ratios.append(float(np.max(qp/supQ[:, ci])))
    T12["blocos"][f"{ver}/{name}"] = {"violacoes": viol, "max_razao_pontual_sobre_celula": max(ratios),
                                      "min_razao": min(ratios), "segundos": time.time() - tb}
    # T13: Q_k em ponto flutuante (estimador do código) contra o intervalo, nos 51 n do regime I
    L = rec["L"]; Ec = rec["Ec"]; t = rec["t"]; J = rec["J"]; T = cc.Tflt
    lamf = L/(2*math.pi)
    Wf = lambda om: -(L/(2*math.pi))*np.sin(om*L/2)/((om*lamf)*((om*lamf)**2 - 1))
    from riemann_spectra.periods import window_response
    ph = np.exp(1j*Ec*T); G = 0.5*window_response(t[:, None] - T[None, :], L)*ph; H = 0.5*window_response(t[:, None] + T[None, :], L)*np.conj(ph)
    Mc = np.hstack([G + H, 1j*(G - H)]); Mf = np.vstack([Mc.real, Mc.imag]); U_, s_, Vt = np.linalg.svd(Mf, full_matrices=False)
    Mp = (Vt.T/s_) @ U_.T
    worst = 0.0; outside = 0; tot = 0
    for n, p in terms1:
        u = math.log(n)
        z = 0.5*(np.exp(1j*Ec*u)*Wf(t - u) + np.exp(-1j*Ec*u)*Wf(t + u))
        qf = Mp[:cc.K, :J] @ z.real + Mp[:cc.K, J:] @ z.imag
        qi = cx.q_pointwise(rec, n)
        for k in range(cc.K):
            tot += 1
            d = max(qi.lo[k] - qf[k], qf[k] - qi.hi[k], 0.0)
            if d > 0:
                outside += 1
                worst = max(worst, d/max(abs(qf[k]), 1e-300))
    T13["blocos"][f"{ver}/{name}"] = {"comparacoes": tot, "fora_do_intervalo": outside, "pior_distancia_relativa": worst,
                                      "ok": worst <= 1e-10}
res["T12"] = {**T12, "ok": all(len(v["violacoes"]) == 0 for v in T12["blocos"].values())}
res["T13_diagnostico"] = {**T13, "ok": all(v["ok"] for v in T13["blocos"].values())}
res["reconstrucao_bit_a_bit_3_blocos"] = {"diffs": bitexact, "ok": all(len(v) == 0 for v in bitexact.values())}

# ---------------------------------------------------------------- T14 decisão por frações
p, r = 2, 7
ck = cx.ck_inf_q(p, r)
P = 1.0e-9; C = 2.0e-9
extra = (Fraction(P) + Fraction(C))/ck
cases = {}
for label, delta, expect in [("igual", Fraction(0), True), ("acima_1e-25", Fraction(1, 10**25), False), ("abaixo_1e-25", -Fraction(1, 10**25), True)]:
    B = Fraction(1, 10**6) - extra + delta
    tot, ok = cx.decide(f"{B.numerator}/{B.denominator}", "0", P, C, p, r)
    cases[label] = {"esperado": expect, "obtido": ok, "total_menos_tau": str(tot - Fraction(1, 10**6))}
tot, ok = cx.decide("0.000000999999999999999999999", "0.000000000000000000000000001", 0.0, 0.0, 2, 1)
cases["strings_decimais_soma_exata_1e-6"] = {"esperado": True, "obtido": ok, "total_menos_tau": str(tot - Fraction(1, 10**6))}
res["T14"] = {"casos": cases, "ok": all(v["esperado"] == v["obtido"] for v in cases.values())}

# ---------------------------------------------------------------- T15 margem exata em todas as células, 30 blocos
worst = None; nfail = 0
for ver, pat in cc.runs.items():
    m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
    for name, blk in m["blocks"].items():
        ins = blk["instrument"]; L = ins["B"] - ins["A"]
        h = 0.5*cc.measure_window_response(L)["fwhm"]
        t = np.unique(np.concatenate([np.linspace(x - h, x + h, 9) for x in cc.Tflt])); tmax = float(np.max(t))
        lam = cc.ivf(iv.mpf(L)/(2*cc.PI))
        for ci in range(cx.NCELL2):
            vmn = cc.dn(lam.lo*cc.dn(cx.U_II + ci*cx.CELL - tmax))
            if not (vmn > 0 and Fraction(float(vmn))**2 >= 2): nfail += 1
            if worst is None or vmn < worst[0]: worst = (float(vmn), ver, name, ci)
res["T15"] = {"celulas_verificadas": 30*cx.NCELL2, "falhas": nfail, "menor_vmin": worst, "ok": nfail == 0}

# ---------------------------------------------------------------- hashes no fim
res["hashes_fim"] = {"cert_calculo.py": sha(BASE + "cert_calculo.py"),
                     "DECLARACAO_CERT_CONTAMINACAO.md": sha(BASE + "DECLARACAO_CERT_CONTAMINACAO.md"),
                     "cert_testes_resultado.json (execução 4)": sha(orig)}
res["hashes_intocados"] = (res["hashes_fim"]["cert_calculo.py"] == cx.CC_SHA
                           and res["hashes_fim"]["DECLARACAO_CERT_CONTAMINACAO.md"] == open(BASE + "DECLARACAO_CERT_CONTAMINACAO.sha256").read().split()[0]
                           and res["hashes_fim"]["cert_testes_resultado.json (execução 4)"] == sha_orig)
res["todos_passaram"] = bool(res["T1_T9"]["todos_passaram"] and res["T10"]["ok"] and res["T11"]["ok"] and res["T12"]["ok"]
                             and res["T13_diagnostico"]["ok"] and res["T14"]["ok"] and res["T15"]["ok"]
                             and res["reconstrucao_bit_a_bit_3_blocos"]["ok"] and res["hashes_intocados"])
res["script_sha256"] = sha(BASE + "cert_contaminacao.py"); res["testes_sha256"] = sha(BASE + "cert_contaminacao_testes.py")
res["segundos_total"] = time.time() - t_start
json.dump(res, open(BASE + "cert_contaminacao_testes_resultado.json", "w"), indent=1, default=str)
print(json.dumps(res, indent=1, default=str))
sys.exit(0 if res["todos_passaram"] else 1)
