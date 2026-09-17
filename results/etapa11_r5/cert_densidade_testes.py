"""
Testes T1–T21 de DECLARACAO_CERT_DENSIDADE.md §5 (antes de --executar).

T1–T15: reaplicação de cert_contaminacao_testes.py (que por sua vez reaplica cert_testes.py, T1–T9, salvando e
restaurando cert_testes_resultado.json). O arquivo vigente cert_contaminacao_testes_resultado.json é salvo, regenerado,
comparado e restaurado.

Desvios de redação da declaração, fixados ANTES de rodar (registrados no resultado):
  (a) cert_contaminacao_testes_resultado.json contém tempos de execução; a comparação byte a byte é registrada, mas o
      critério é a igualdade do conteúdo sem os campos "segundos*".
  (b) T20 "a_l1_sup igual nas duas tabelas vigentes": a tabela da contaminação não tem essa coluna. Substituído por:
      leitura ida-e-volta da string, mesmos 1.410 pares nas duas tabelas e parada bit a bit limpa da contaminação
      (que já comparou ‖a_k‖₁^sup com a execução 4).
"""
import csv, glob, hashlib, json, math, os, shutil, subprocess, sys, time
from fractions import Fraction
import mpmath
from mpmath import iv

sys.path.insert(0, "results/etapa11_r5")
import cert_densidade as cd
cc = cd.cc
BASE = cd.BASE
res = {"desvios_de_redacao_fixados_antes": [
    "(a) comparação de cert_contaminacao_testes_resultado.json pelo conteúdo sem campos de tempo; byte a byte só registrada",
    "(b) T20: a_l1_sup não existe na tabela da contaminação; substituído por ida-e-volta, mesmas chaves e parada bit a bit limpa"]}
t_start = time.time()
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
res["hashes_inicio"] = {f: sha(BASE + f) for f in ["cert_calculo.py", "cert_contaminacao.py", "DECLARACAO_CERT_DENSIDADE.md",
                                                     "cert_testes_resultado.json", "cert_contaminacao_testes_resultado.json"]}

def strip_times(o):
    if isinstance(o, dict):
        return {k: strip_times(v) for k, v in o.items() if not k.startswith("segundos")}
    if isinstance(o, list):
        return [strip_times(v) for v in o]
    return o

# ---------------------------------------------------------------- T1–T15
orig = BASE + "cert_contaminacao_testes_resultado.json"; bak = BASE + ".cert_contaminacao_testes_resultado.json.bak"
sha_orig = sha(orig); content_orig = json.load(open(orig)); shutil.copy2(orig, bak)
t0 = time.time()
proc = subprocess.run([sys.executable, BASE + "cert_contaminacao_testes.py"], capture_output=True, text=True)
regen = json.load(open(orig)); sha_regen = sha(orig)
shutil.copy2(bak, orig); os.remove(bak)
okkeys = ["T10", "T11", "T12", "T13_diagnostico", "reconstrucao_bit_a_bit_3_blocos", "T14", "T15"]
res["T1_T15"] = {"exit": proc.returncode, "todos_passaram": regen.get("todos_passaram"),
                 "T1_T9_todos_passaram": regen["T1_T9"]["todos_passaram"],
                 "T1_T9_resultado_exec4_regenerado_identico": regen["T1_T9"]["resultado_regenerado_identico_ao_da_execucao4"],
                 "oks": {k: regen[k]["ok"] for k in okkeys},
                 "conteudo_sem_tempos_identico_ao_vigente": strip_times(regen) == strip_times(content_orig),
                 "byte_a_byte_identico (esperado falso por tempos)": sha_regen == sha_orig,
                 "arquivo_vigente_restaurado": sha(orig) == sha_orig, "segundos": time.time() - t0}

# ---------------------------------------------------------------- T16 constante C
elem = (Fraction(1, 8) + Fraction(1, 2) + 2*Fraction(99, 70)/3)/(2*3)
res["T16"] = {"C_inf": float(cd.C_INF), "C_sup": float(cd.C_SUP), "C_sup_fracao": str(cd.C_SUP),
              "C_sup_lt_0.24953": cd.C_SUP < Fraction("0.24953"), "sqrt2_le_99_70": Fraction(99, 70)**2 >= 2,
              "cota_elementar": float(elem), "C_sup_le_cota_elementar": cd.C_SUP <= elem,
              "C_inf_gt_0.2495": cd.C_INF > Fraction("0.2495")}
res["T16"]["ok"] = res["T16"]["C_sup_lt_0.24953"] and res["T16"]["sqrt2_le_99_70"] and res["T16"]["C_sup_le_cota_elementar"] and res["T16"]["C_inf_gt_0.2495"]

# ---------------------------------------------------------------- T17 diagnóstico B da cota pontual
mpmath.mp.dps = 50
Csup_mp = mpmath.mpf(cd.C_SUP.numerator)/cd.C_SUP.denominator
Es = [mpmath.mpf(9800) + (mpmath.mpf(74000) - 9800)*i/1999 for i in range(2000)] + [mpmath.mpf(10) + 90*mpmath.mpf(i)/19 for i in range(20)]
worst = mpmath.mpf(0); viol = 0
for E in Es:
    D = (mpmath.re(mpmath.digamma(mpmath.mpf("0.25") + 0.5j*E)) - mpmath.log(E/2))/(2*mpmath.pi)
    ratio = abs(D)*E**2/Csup_mp
    worst = max(worst, ratio)
    if abs(D) > Csup_mp/E**2: viol += 1
res["T17_diagnostico"] = {"pontos": len(Es), "violacoes": viol, "max_|Delta|E2_sobre_Csup": float(worst), "ok": viol == 0}

# ---------------------------------------------------------------- T18 janela
W = cd.windows()
res["T18"] = {"blocos": len(W), "A_star_positivo": all(w["A_star"] > 0 for w in W),
              "B_star_menos_A_star_igual_L": all(w["B_star"] - w["A_star"] == Fraction(w["L"]) for w in W),
              "blocos_janela_igual_AB (diagnóstico)": sum(w["janela_igual_AB"] for w in W),
              "blocos_janela_diferente": [f'{w["versao"]}/{w["bloco"]}' for w in W if not w["janela_igual_AB"]],
              "max_|A*−A|": float(max(abs(w["A_star"] - Fraction(w["A"])) for w in W)),
              "max_|B*−B|": float(max(abs(w["B_star"] - Fraction(w["B"])) for w in W))}
res["T18"]["ok"] = res["T18"]["A_star_positivo"] and res["T18"]["B_star_menos_A_star_igual_L"] and len(W) == 30

# ---------------------------------------------------------------- T19 decisão
Wd = {(w["versao"], w["bloco"]): w for w in W}
w0 = Wd[("m4-v1", "b01")]; a_str = "0.002"; p, r = 53, 1
ex = cd.extra_rel(a_str, w0["D"], p, r)
cases = {}
for label, delta, exp in [("igual", Fraction(0), True), ("acima_1e-25", Fraction(1, 10**25), False), ("abaixo_1e-25", -Fraction(1, 10**25), True)]:
    base = Fraction(1, 10**6) - ex + delta
    tot, ok = cd.decide(f"{base.numerator}/{base.denominator}", a_str, w0["D"], p, r)
    cases[label] = {"esperado": exp, "obtido": ok, "total_menos_tau": str(tot - Fraction(1, 10**6))}
res["T19"] = {"casos": cases, "ok": all(c["esperado"] == c["obtido"] for c in cases.values())}

# ---------------------------------------------------------------- T20 leituras
t4, tx = cd.load_tables()
bad_total = 0; bad_rt = 0
for key, row in tx.items():
    p_, r_ = int(key[2]), int(key[3])
    exact = Fraction(row["B_rel_sup"]) + Fraction(row["Sabs_rel_sup"]) + (Fraction(float(row["P_abs_sup"])) + Fraction(float(row["C_abs_sup"])))/cd.ck_inf_q(p_, r_)
    if Fraction(row["total_sup"]) < exact: bad_total += 1
    if repr(float(t4[key]["a_l1_sup"])) != t4[key]["a_l1_sup"]: bad_rt += 1
    if row["B_rel_sup"] != t4[key]["B_rel_sup"] or row["Sabs_rel_sup"] != t4[key]["Sabs_rel_sup"]: bad_total += 1
resumo_cx = json.load(open(BASE + "cert_contaminacao_resumo.json"))
res["T20"] = {"pares": len(tx), "mesmas_chaves": set(t4) == set(tx), "total_sup_menor_que_soma_exata": bad_total,
              "a_l1_sup_ida_e_volta_falhas": bad_rt, "parada_bit_a_bit_contaminacao": resumo_cx["parada_bit_a_bit"]}
res["T20"]["ok"] = (len(tx) == 1410 and res["T20"]["mesmas_chaves"] and bad_total == 0 and bad_rt == 0 and resumo_cx["parada_bit_a_bit"] == [])

# ---------------------------------------------------------------- T21 diagnóstico da herança
old = {(o["versao"], o["bloco"]): Fraction(o["cota_sup_arredondada_para_cima"]) for o in json.load(open(cd.OLD_JSON))}
ratios = [float(w["D"]/old[(w["versao"], w["bloco"])]) for w in W]
res["T21_diagnostico"] = {"D_novo_sobre_antigo_min": min(ratios), "D_novo_sobre_antigo_max": max(ratios),
                          "D_max_novo": float(max(w["D"] for w in W)), "D_min_novo": float(min(w["D"] for w in W)),
                          "nota": "antigo usava [A−1e−6, B+1e−6] de metrics.json; não entra na decisão"}

# ---------------------------------------------------------------- hashes
res["hashes_fim"] = {f: sha(BASE + f) for f in res["hashes_inicio"]}
res["hashes_intocados"] = res["hashes_fim"] == res["hashes_inicio"]
res["nenhuma_saida_de_execucao_criada"] = not any(os.path.exists(BASE + f) for f in ["cert_densidade_tabela.csv", "cert_densidade_blocos.csv", "cert_densidade_resumo.json"])
res["todos_passaram"] = bool(res["T1_T15"]["todos_passaram"] and res["T1_T15"]["conteudo_sem_tempos_identico_ao_vigente"]
                             and res["T1_T15"]["arquivo_vigente_restaurado"] and res["T16"]["ok"] and res["T17_diagnostico"]["ok"]
                             and res["T18"]["ok"] and res["T19"]["ok"] and res["T20"]["ok"] and res["hashes_intocados"]
                             and res["nenhuma_saida_de_execucao_criada"])
res["script_sha256"] = sha(BASE + "cert_densidade.py"); res["testes_sha256"] = sha(BASE + "cert_densidade_testes.py")
res["segundos_total"] = time.time() - t_start
json.dump(res, open(BASE + "cert_densidade_testes_resultado.json", "w"), indent=1, default=str)
print(json.dumps(res, indent=1, default=str))
sys.exit(0 if res["todos_passaram"] else 1)
