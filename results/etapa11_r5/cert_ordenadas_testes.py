"""
Testes T1–T27 de DECLARACAO_CERT_ORDENADAS.md §4 (antes de --executar).
T1–T21: reaplicação de cert_densidade_testes.py (cadeia completa), com o resultado vigente salvo, regenerado, comparado
sem campos de tempo e restaurado.

Rodada 2 — correções nos testes autorizadas após a rodada 1 (preservada em cert_ordenadas_testes_resultado_rodada1.json,
SHA-256 f9245a4a…); método e decisão de cert_ordenadas.py inalterados:
  (1) T1–T21: a meta-condição "nenhuma saída de execução criada" de cert_densidade_testes.py só vale antes do --executar
      da densidade. Critério: só podem diferir (sem tempos) as chaves nenhuma_saida_de_execucao_criada e todos_passaram,
      a primeira falsa porque as saídas da densidade existem, e todos os ok substantivos verdadeiros.
  (2) T22: igualdade decimal bruto × CSV processado passa a diagnóstico (ruído de float ≤ 7e-12, camada ρ_num).
  (3) T25: tolerância 1e-10·max(|g|) + ‖a_k‖₁^sup·S₂·|fl(E) − E_dec|·1,01 (piso de avaliar em fl(E)).
"""
import csv, glob, hashlib, json, math, os, shutil, subprocess, sys, time
from fractions import Fraction
import numpy as np
import mpmath
from mpmath import iv

sys.path.insert(0, "results/etapa11_r5")
import cert_ordenadas as co
cc = co.cc; cx = co.cx; BASE = co.BASE
res = {"correcoes_de_teste_rodada2": [
    "(1) T1–T21: meta-condição pós-execução da densidade; só podem diferir nenhuma_saida_de_execucao_criada e todos_passaram",
    "(2) T22: decimal bruto × CSV processado vira diagnóstico (ρ_num)",
    "(3) T25: piso ‖a_k‖₁·S₂·|fl(E) − E_dec|·1,01 + 1e-10·max|g|"],
    "rodada1_preservada": "cert_ordenadas_testes_resultado_rodada1.json"}
t_start = time.time()
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
WATCH = ["cert_calculo.py", "cert_contaminacao.py", "cert_densidade.py", "DECLARACAO_CERT_ORDENADAS.md",
         "cert_testes_resultado.json", "cert_contaminacao_testes_resultado.json", "cert_densidade_testes_resultado.json"]
res["hashes_inicio"] = {f: sha(BASE + f) for f in WATCH}
res["hashes_inicio"]["data/raw/zeros1"] = sha(co.RAW)

def strip_times(o):
    if isinstance(o, dict): return {k: strip_times(v) for k, v in o.items() if not k.startswith("segundos")}
    if isinstance(o, list): return [strip_times(v) for v in o]
    return o

# ---------------------------------------------------------------- T1–T21
orig = BASE + "cert_densidade_testes_resultado.json"; bak = BASE + ".cert_densidade_testes_resultado.json.bak"
content_orig = json.load(open(orig)); sha_orig = sha(orig); shutil.copy2(orig, bak)
t0 = time.time()
proc = subprocess.run([sys.executable, BASE + "cert_densidade_testes.py"], capture_output=True, text=True)
regen = json.load(open(orig)); shutil.copy2(bak, orig); os.remove(bak)
def diff_paths(a, b, path=""):
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in set(a) | set(b):
            if k not in a or k not in b: out.append(path + "/" + k)
            else: out += diff_paths(a[k], b[k], path + "/" + k)
        return out
    return [] if a == b else [path]
dpaths = sorted(diff_paths(strip_times(regen), strip_times(content_orig)))
dens_out_exist = all(os.path.exists(BASE + f) for f in ["cert_densidade_tabela.csv", "cert_densidade_blocos.csv", "cert_densidade_resumo.json"])
oks = {k: regen[k]["ok"] for k in ["T16", "T17_diagnostico", "T18", "T19", "T20"]}
res["T1_T21"] = {"exit": proc.returncode, "todos_passaram_regenerado": regen.get("todos_passaram"),
                 "T1_T15_todos_passaram": regen["T1_T15"]["todos_passaram"],
                 "T1_T15_conteudo_sem_tempos_identico": regen["T1_T15"]["conteudo_sem_tempos_identico_ao_vigente"],
                 "oks_T16_T20": oks, "hashes_intocados_regenerado": regen["hashes_intocados"],
                 "chaves_que_diferem_sem_tempos": dpaths,
                 "nenhuma_saida_regenerado": regen["nenhuma_saida_de_execucao_criada"], "saidas_da_densidade_existem": dens_out_exist,
                 "arquivo_vigente_restaurado": sha(orig) == sha_orig, "segundos": time.time() - t0}
res["T1_T21"]["ok"] = bool(set(dpaths) <= {"/nenhuma_saida_de_execucao_criada", "/todos_passaram"}
                           and regen["nenhuma_saida_de_execucao_criada"] is False and dens_out_exist
                           and regen["T1_T15"]["todos_passaram"] and regen["T1_T15"]["conteudo_sem_tempos_identico_ao_vigente"]
                           and regen["T1_T15"]["arquivo_vigente_restaurado"] and all(oks.values())
                           and regen["hashes_intocados"] and res["T1_T21"]["arquivo_vigente_restaurado"])

# ---------------------------------------------------------------- T22 entradas da tabela
raw = co.load_raw()
prows = list(csv.reader(open(co.PROC)))[1:]
idx_bad = sum(1 for i, r in enumerate(prows) if int(r[0]) != i + 1)
dd = [abs(Fraction(r[1]) - Fraction(raw[i])) for i, r in enumerate(prows)]
mism = sum(1 for d in dd if d); mism_max = max(dd)
_, zf = co.load_processed_floats()
geos = {}; per_block = []
for ver, pat in cc.runs.items():
    m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
    for name, blk in m["blocks"].items():
        ins = blk["instrument"]; g = co.block_geometry(ins, raw, zf); geos[(ver, name)] = (ins, g)
        sel = np.nonzero((zf >= ins["A"]) & (zf <= ins["B"]))[0]
        per_block.append({"bloco": f"{ver}/{name}", "nI": g["nI"], "selecao_pipeline_igual_I": list(sel) == list(range(g["lo"], g["hi"] + 1)),
                          "float(A_dec)==A": float(g["A_dec"]) == ins["A"], "float(B_dec)==B": float(g["B_dec"]) == ins["B"],
                          "|A*-A_dec|": float(abs(g["A_star"] - g["A_dec"])), "|B*-B_dec|": float(abs(g["B_star"] - g["B_dec"]))})
res["T22"] = {"sha_tabela_bruta_ok": sha(co.RAW) == co.RAW_SHA, "linhas": len(raw),
              "indices_processado_fora_de_ordem": idx_bad,
              "diagnostico_rho_num_decimais_bruto_vs_processado": {"divergentes": mism, "max_abs": float(mism_max)},
              "blocos_com_3000": sum(b["nI"] == 3000 for b in per_block),
              "selecao_pipeline_igual_I_todos": all(b["selecao_pipeline_igual_I"] for b in per_block),
              "bordas_float_iguais_todos": all(b["float(A_dec)==A"] and b["float(B_dec)==B"] for b in per_block),
              "max_|A*-A_dec|": max(b["|A*-A_dec|"] for b in per_block), "max_|B*-B_dec|": max(b["|B*-B_dec|"] for b in per_block)}
res["T22"]["ok"] = (res["T22"]["sha_tabela_bruta_ok"] and len(raw) == 100000 and idx_bad == 0 and res["T22"]["blocos_com_3000"] == 30
                    and res["T22"]["selecao_pipeline_igual_I_todos"] and res["T22"]["bordas_float_iguais_todos"])

# ---------------------------------------------------------------- T23 diagnóstico B de H-tab
rng = np.random.default_rng(20260916)
mpmath.mp.dps = 30
diffs = []; t23 = time.time()
for (ver, name), (ins, g) in sorted(geos.items()):
    n0 = int(rng.integers(g["lo"], g["hi"] + 1))           # índice 0-based; zero de posto n0+1
    zz = mpmath.zetazero(n0 + 1)
    d = abs(mpmath.mpf(raw[n0]) - mpmath.im(zz))
    diffs.append({"bloco": f"{ver}/{name}", "indice": n0 + 1, "|tab - zetazero|": float(d)})
res["T23_diagnostico"] = {"amostra": diffs, "max_diferenca": max(x["|tab - zetazero|"] for x in diffs),
                          "todos_<=_3e-9": all(x["|tab - zetazero|"] <= 3e-9 for x in diffs),
                          "nota": "diagnóstico B; não valida H-tab", "segundos": time.time() - t23}

# ---------------------------------------------------------------- T24 Lipschitz
ins, g = geos[("m4-v1", "b01")]
As = float(g["A_star"]); Bs = float(g["B_star"]); L = g["L"]; Ec = ins["E_c"]
def fw(E, t):
    inside = (E >= As) & (E <= Bs)
    w = np.where(inside, np.sin(np.pi*(E - As)/L)**2, 0.0)
    wp = np.where(inside, (np.pi/L)*np.sin(2*np.pi*(E - As)/L), 0.0)
    e = np.exp(-1j*(E - Ec)*t)
    return w*e, e*(wp - 1j*t*w)
worst = 0.0; viol = 0; npairs = 0
tt = rng.uniform(0.5, 4.94, 10000)
for mode in range(4):
    if mode == 0: x = rng.uniform(As, Bs, 2500); y = x + rng.uniform(-0.5, 0.5, 2500)
    elif mode == 1: x = As + rng.uniform(-0.2, 0.2, 2500); y = As + rng.uniform(-0.2, 0.2, 2500)
    elif mode == 2: x = Bs + rng.uniform(-0.2, 0.2, 2500); y = Bs + rng.uniform(-0.2, 0.2, 2500)
    else: x = rng.uniform(As - 1, Bs + 1, 2500); y = x + rng.uniform(-2, 2, 2500)
    t = tt[mode*2500:(mode + 1)*2500]
    fx, dfx = fw(x, t); fy, _ = fw(y, t)
    lhs = np.abs(fy - fx - dfx*(y - x))
    S2t = 2*np.pi**2/L**2 + 2*t*np.pi/L + t**2
    rhs = 0.5*S2t*(y - x)**2
    ok = lhs <= rhs*(1 + 1e-9) + 1e-12
    viol += int(np.sum(~ok)); npairs += len(x)
    worst = max(worst, float(np.max(lhs/np.maximum(rhs, 1e-300))))
res["T24"] = {"S2_por_bloco_max": max(float(v[1]["S2"]) for v in geos.values()), "S2_por_bloco_min": min(float(v[1]["S2"]) for v in geos.values()),
              "pares_diagnostico": npairs, "violacoes": viol, "max_lhs_sobre_rhs": worst, "ok": viol == 0}

# ---------------------------------------------------------------- T25 enclausuramento de g_k (3 blocos, 50 zeros)
blocos4, tab4 = cx.exec4_tables()
from riemann_spectra.periods import window_response
T25 = {}; bitexact = {}
for ver, name in [("m4-v1", "b01"), ("m4-v2", "c01"), ("m4-v3", "d01")]:
    ins, g = geos[(ver, name)]
    tb = time.time(); rec = cx.reconstruct(ins)
    bitexact[f"{ver}/{name}"] = cx.bit_exact_vs_exec4(ver, name, rec, blocos4, tab4)
    idx = [int(round(g["lo"] + i*(g["hi"] - g["lo"])/49)) for i in range(50)]
    _, each = co.g_abs_sum(rec, g, raw, indices=idx, return_each=True)
    t = rec["t"]; J = rec["J"]; Lf = rec["L"]; Ecf = rec["Ec"]; T = cc.Tflt
    ph = np.exp(1j*Ecf*T); G = 0.5*window_response(t[:, None] - T[None, :], Lf)*ph; H = 0.5*window_response(t[:, None] + T[None, :], Lf)*np.conj(ph)
    Mc = np.hstack([G + H, 1j*(G - H)]); Mf = np.vstack([Mc.real, Mc.imag]); U_, s_, Vt = np.linalg.svd(Mf, full_matrices=False); Mp = (Vt.T/s_) @ U_.T
    Asf = float(g["A_star"]); Bsf = float(g["B_star"])
    out = 0; worst = 0.0; nz = 0; ncmp = 0; out_tol = 0; worst_ratio = 0.0
    a_l1 = np.array([float(x) for x in rec["a_l1"]]); S2f = float(g["S2"])
    for n, gi in each:
        E = float(Fraction(raw[n])); dE = float(abs(Fraction(E) - Fraction(raw[n])))
        if gi is None:
            nz += 1; continue
        w = np.sin(np.pi*(E - Asf)/Lf)**2; wp = (np.pi/Lf)*np.sin(2*np.pi*(E - Asf)/Lf)
        e = np.exp(-1j*(E - Ecf)*t); fp = e*(wp - 1j*t*w)
        gf = Mp[:cc.K, :J] @ fp.real + Mp[:cc.K, J:] @ fp.imag
        for k in range(cc.K):
            ncmp += 1
            d = max(gi.lo[k] - gf[k], gf[k] - gi.hi[k], 0.0)
            tol = 1e-10*max(abs(gf[k]), float(gi.mag()[k])) + a_l1[k]*S2f*dE*1.01
            if d > 0: out += 1; worst = max(worst, d/max(abs(gf[k]), 1e-300))
            if d > tol: out_tol += 1
            if d > 0: worst_ratio = max(worst_ratio, d/tol if tol > 0 else float("inf"))
    T25[f"{ver}/{name}"] = {"comparacoes": ncmp, "zeros_fora_da_janela": nz, "fora_do_intervalo": out,
                            "pior_distancia_relativa_(rodada1)": worst, "acima_da_tolerancia_corrigida": out_tol,
                            "max_distancia_sobre_tolerancia": worst_ratio, "ok": out_tol == 0, "segundos": time.time() - tb}
res["T25"] = {**T25, "reconstrucao_bit_a_bit": bitexact,
              "ok": all(v["ok"] for v in T25.values()) and all(len(v) == 0 for v in bitexact.values())}

# ---------------------------------------------------------------- T26 borda
T26 = []
for (ver, name), (ins, g) in sorted(geos.items()):
    lo, hi = g["lo"], g["hi"]
    dlo = (g["A_dec"] - Fraction(raw[lo - 1])) if lo > 0 else None
    dhi = (Fraction(raw[hi + 1]) - g["B_dec"]) if hi + 1 < len(raw) else None
    thr = Fraction(3, 10**9) + g["eta"]
    T26.append({"bloco": f"{ver}/{name}", "eta": float(g["eta"]), "edge_unit": float(g["edge_unit"]), "rest_unit": float(g["rest_unit"]),
                "vizinho_inferior_dist": (float(dlo) if dlo is not None else None), "vizinho_superior_dist": (float(dhi) if dhi is not None else None),
                "vizinhos_alem_do_limiar": (dlo is None or dlo > thr) and (dhi is None or dhi > thr)})
res["T26"] = {"blocos": T26, "eta_max": max(b["eta"] for b in T26), "edge_unit_max": max(b["edge_unit"] for b in T26),
              "rest_unit_max": max(b["rest_unit"] for b in T26), "sem_vizinho": [b["bloco"] for b in T26 if b["vizinho_inferior_dist"] is None or b["vizinho_superior_dist"] is None],
              "ok": all(b["vizinhos_alem_do_limiar"] for b in T26)}

# ---------------------------------------------------------------- T27 decisão
ins, g = geos[("m4-v1", "b01")]
p, r = 53, 1; a_str = "0.002"; Gs = 0.5
ck = co.ck_inf_q(p, r)
extra = co.DELTA_TAB*Fraction(Gs)/ck + Fraction(float(a_str))*(g["rest_unit"] + g["edge_unit"])/ck
cases = {}
for label, dl, exp in [("igual", Fraction(0), True), ("acima_1e-25", Fraction(1, 10**25), False), ("abaixo_1e-25", -Fraction(1, 10**25), True)]:
    base = Fraction(1, 10**6) - extra + dl
    tot, *_, ok = co.total_gamma(f"{base.numerator}/{base.denominator}", a_str, Gs, g["rest_unit"], g["edge_unit"], p, r)
    cases[label] = {"esperado": exp, "obtido": ok, "total_menos_tau": str(tot - Fraction(1, 10**6))}
res["T27"] = {"casos": cases, "ok": all(c["esperado"] == c["obtido"] for c in cases.values())}

# ---------------------------------------------------------------- integridade
res["hashes_fim"] = {f: sha(BASE + f) for f in WATCH}; res["hashes_fim"]["data/raw/zeros1"] = sha(co.RAW)
res["hashes_intocados"] = res["hashes_fim"] == res["hashes_inicio"]
res["nenhuma_saida_de_execucao_criada"] = not any(os.path.exists(BASE + f) for f in ["cert_ordenadas_tabela.csv", "cert_ordenadas_blocos.csv", "cert_ordenadas_resumo.json"])
res["todos_passaram"] = bool(res["T1_T21"]["ok"] and res["T22"]["ok"] and res["T24"]["ok"]
                             and res["T25"]["ok"] and res["T26"]["ok"] and res["T27"]["ok"]
                             and res["hashes_intocados"] and res["nenhuma_saida_de_execucao_criada"])
res["nota_T23"] = "T23 é diagnóstico registrado e não entra em todos_passaram (declaração §4)"
res["script_sha256"] = sha(BASE + "cert_ordenadas.py"); res["testes_sha256"] = sha(BASE + "cert_ordenadas_testes.py")
res["segundos_total"] = time.time() - t_start
json.dump(res, open(BASE + "cert_ordenadas_testes_resultado.json", "w"), indent=1, default=str)
print(json.dumps(res, indent=1, default=str))
sys.exit(0 if res["todos_passaram"] else 1)
