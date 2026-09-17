"""
Termo determinístico ρ_Δ: cota de densidade sob a base atual e projeção por a_k,
conforme results/etapa11_r5/DECLARACAO_CERT_DENSIDADE.md (hash verificado).

|Δ(E)| ≤ C/E², C = (1/8 + 1/2 + 2√2/3)/(2π)  (DLMF 5.11.2 e §5.11(ii); DLMF 25.10.2)
sup_t|ρ_Δ(t)| ≤ D_bloco := C^sup·(L/2)/A*²,  A* = E_c − L/2,  L = fl(B − A)
|a_k·ρ_Δ| ≤ ‖a_k‖₁^sup·D_bloco;   total^Δ_k = total_k(contaminação) + ‖a_k‖₁^sup·D_bloco/|c_k|_inf ≤ 10⁻⁶

Decisão inteiramente em frações exatas. Não usa density_error_certified.py (dependência herdada).
Execução só com --executar.
"""
import csv, glob, hashlib, importlib.util, json, sys, time
from fractions import Fraction
from mpmath import iv

BASE = "results/etapa11_r5/"
DOCS = [("DECLARACAO_CERT.md", "DECLARACAO_CERT.sha256"),
        ("DECLARACAO_CERT_CORRECAO1.md", "DECLARACAO_CERT_CORRECAO1.sha256"),
        ("DECLARACAO_CERT_CORRECAO2.md", "DECLARACAO_CERT_CORRECAO2.sha256"),
        ("DECLARACAO_CERT_RECONF_C1C2.md", "DECLARACAO_CERT_RECONF_C1C2.sha256"),
        ("DECLARACAO_CERT_CONTAMINACAO.md", "DECLARACAO_CERT_CONTAMINACAO.sha256"),
        ("DECLARACAO_CERT_DENSIDADE.md", "DECLARACAO_CERT_DENSIDADE.sha256")]
for f, h in DOCS:
    assert hashlib.sha256(open(BASE + f, "rb").read()).hexdigest() == open(BASE + h).read().split()[0], f
CC_SHA = "95bec52820df9a8fa9830a6283576e6a3afacb6962f2cf38b546a93d4222aeb2"
CX_SHA = "4baff93389cea085c690567fadc8c20c87ab951d4e88a214988457e953885945"
assert hashlib.sha256(open(BASE + "cert_calculo.py", "rb").read()).hexdigest() == CC_SHA
assert hashlib.sha256(open(BASE + "cert_contaminacao.py", "rb").read()).hexdigest() == CX_SHA

_spec = importlib.util.spec_from_file_location("cc", BASE + "cert_calculo.py")
cc = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(cc)

TAU = Fraction(1, 10**6)
OLD_JSON = "results/etapa11_3b/density_error_certified.json"   # só diagnóstico (T21)


def C_enclosure():
    """C = (1/8 + 1/2 + 2√2/3)/(2π) em mpmath.iv; devolve (C_inf, C_sup) exatos."""
    C = (iv.mpf(1)/8 + iv.mpf(1)/2 + 2*iv.sqrt(2)/3)/(2*cc.PI)
    return cc.lo_q(C), cc.hi_q(C)


C_INF, C_SUP = C_enclosure()


def windows():
    """Por bloco: A* = E_c − L/2, B* = E_c + L/2 (L = fl(B − A)) e D = C^sup·(L/2)/A*², tudo em Fraction."""
    out = []
    for ver, pat in cc.runs.items():
        m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
        for name, blk in m["blocks"].items():
            ins = blk["instrument"]; A = ins["A"]; B = ins["B"]; Ec = ins["E_c"]; L = B - A
            Lq = Fraction(L); Ecq = Fraction(Ec)
            As = Ecq - Lq/2; Bs = Ecq + Lq/2
            assert As > 0
            D = C_SUP*(Lq/2)/(As*As)
            out.append({"versao": ver, "bloco": name, "A": A, "B": B, "E_c": Ec, "L": L, "A_star": As, "B_star": Bs,
                        "janela_igual_AB": (As == Fraction(A) and Bs == Fraction(B)), "D": D})
    return out


def ck_inf_q(p, r):
    return cc.lo_q(iv.log(p)/(cc.PI*iv.sqrt(p**r)))


def extra_rel(a_l1_str, D, p, r):
    """‖a_k‖₁^sup·D/|c_k|_inf, exato (Fraction do valor binário do float certificado)."""
    return Fraction(float(a_l1_str))*D/ck_inf_q(p, r)


def decide(total_contam_str, a_l1_str, D, p, r):
    tot = Fraction(total_contam_str) + extra_rel(a_l1_str, D, p, r)
    return tot, tot <= TAU


def load_tables():
    t4 = {(t["versao"], t["bloco"], t["p"], t["r"]): t for t in csv.DictReader(open(BASE + "cert_tabela.csv"))}
    tx = {(t["versao"], t["bloco"], t["p"], t["r"]): t for t in csv.DictReader(open(BASE + "cert_contaminacao_tabela.csv"))}
    return t4, tx


if __name__ == "__main__":
    if "--executar" not in sys.argv:
        sys.exit("Execução bloqueada: exige --executar (DECLARACAO_CERT_DENSIDADE §6, após testes e revisão).")
    t0 = time.time()
    W = windows(); Wd = {(w["versao"], w["bloco"]): w for w in W}
    old = {(o["versao"], o["bloco"]): o["cota_sup_arredondada_para_cima"] for o in json.load(open(OLD_JSON))}
    t4, tx = load_tables()
    assert set(t4) == set(tx) and len(tx) == 1410
    rows = []
    for key in sorted(tx):
        ver, name, p, r = key
        w = Wd[(ver, name)]
        ex = extra_rel(t4[key]["a_l1_sup"], w["D"], int(p), int(r))
        tot, ok = decide(tx[key]["total_sup"], t4[key]["a_l1_sup"], w["D"], int(p), int(r))
        rows.append({"versao": ver, "bloco": name, "p": p, "r": r, "eligible": tx[key]["eligible"],
                     "total_contaminacao_sup": tx[key]["total_sup"], "certificado_contaminacao": tx[key]["certificado"],
                     "extra_rhoDelta_rel_sup": cc.sup_chk(cc.iv_frac(ex), 15),
                     "total_densidade_sup": cc.sup_chk(cc.iv_frac(tot), 15), "certificado": ok})
    with open(BASE + "cert_densidade_blocos.csv", "w", newline="") as fh:
        wr = csv.writer(fh); wr.writerow(["versao", "bloco", "A_star", "B_star", "janela_igual_AB", "D_sup", "D_antigo_herdado", "D_novo_sobre_antigo"])
        for w in W:
            wr.writerow([w["versao"], w["bloco"], str(w["A_star"]), str(w["B_star"]), w["janela_igual_AB"],
                         cc.sup_chk(cc.iv_frac(w["D"]), 15), old[(w["versao"], w["bloco"])], float(w["D"]/Fraction(old[(w["versao"], w["bloco"])]))])
    with open(BASE + "cert_densidade_tabela.csv", "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
    E = [x for x in rows if x["eligible"] == "True"]
    summ = {"declaracao_sha256": open(BASE + "DECLARACAO_CERT_DENSIDADE.sha256").read().split()[0],
            "cert_calculo_sha256": CC_SHA, "cert_contaminacao_sha256": CX_SHA,
            "C_inf": str(C_INF), "C_sup": str(C_SUP), "C_sup_decimal15": cc.sup_chk(cc.iv_frac(C_SUP), 15),
            "blocos_janela_igual_AB": sum(w["janela_igual_AB"] for w in W),
            "D_max_sup": cc.sup_chk(cc.iv_frac(max(w["D"] for w in W)), 15),
            "pares": len(rows), "certificados": sum(x["certificado"] for x in rows),
            "elegiveis": len(E), "elegiveis_certificados": sum(x["certificado"] for x in E),
            "max_total_elegiveis_sup": max(Fraction(x["total_densidade_sup"]) for x in E).__float__(),
            "max_extra_elegiveis_sup": max(Fraction(x["extra_rhoDelta_rel_sup"]) for x in E).__float__(),
            "perdidos_frente_contaminacao": sum(1 for x in rows if x["certificado_contaminacao"] == "True" and not x["certificado"]),
            "tempo_s": time.time() - t0}
    json.dump(summ, open(BASE + "cert_densidade_resumo.json", "w"), indent=1, default=str)
    print(json.dumps(summ, indent=1, default=str))
