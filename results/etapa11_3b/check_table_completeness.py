"""
11.3b / L-EF2a, ponto 1: a tabela usada contém todos os zeros de cada janela [A, B] do instrumento?
Compara, para cada bloco de m4-v1, m4-v2 e m4-v3, o número de ordenadas da tabela em [A, B] com N(B) − N(A),
calculado por mpmath.nzeros (método de Gram/Turing implementado em ponto flutuante: classe B, não certificado),
e confere que N(A) é igual ao índice do último zero da tabela abaixo de A.
Não altera nenhum resultado de m4; lê apenas A, B e a tabela já utilizada.
"""
import csv, glob, json, bisect
import mpmath as mp

mp.mp.dps = 25
Z = [float(r[1]) for r in list(csv.reader(open("data/processed/zeros_100k.csv")))[1:]]
runs = {"m4-v1": "results/run_20260913_144429_m3_b01*", "m4-v2": "results/run_20260913_173045_m3_c01*",
        "m4-v3": "results/run_20260913_220906_m3_d01*"}
out = []
for ver, pat in runs.items():
    m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
    for name, blk in m["blocks"].items():
        A, B = blk["instrument"]["A"], blk["instrument"]["B"]
        lo, hi = bisect.bisect_left(Z, A), bisect.bisect_right(Z, B)
        n_table = hi - lo
        # distância de A e B ao zero mais próximo (nzeros em cima de um zero é ambíguo)
        dA = min(abs(A - Z[lo]), abs(A - Z[lo - 1])); dB = min(abs(B - Z[hi - 1]), abs(B - Z[hi]) if hi < len(Z) else 9)
        eps = 1e-6
        NA = int(mp.nzeros(A - eps)); NB = int(mp.nzeros(B + eps))
        rec = {"versao": ver, "bloco": name, "A": A, "B": B, "n_tabela_em_[A,B]": n_table,
               "N(B+1e-6)-N(A-1e-6)": NB - NA, "N(A-1e-6)": NA, "indice_tabela_abaixo_de_A": lo,
               "dist_A_zero": dA, "dist_B_zero": dB, "concorda": (NB - NA == n_table) and (NA == lo)}
        out.append(rec); print(json.dumps(rec))
json.dump(out, open("results/etapa11_3b/check_table_completeness.json", "w"), indent=1)
print("todos_concordam:", all(r["concorda"] for r in out), "blocos:", len(out))
