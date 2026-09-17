"""
11.3b / Z1 (F8) e cota de contagem usada em R_longe/E_z2 (F3): constantes explícitas de uma cota N(T) = O(T log T),
derivada em docs/ETAPA11_3B_Z1_CONTAGEM.md. Aritmética intervalar (mpmath.iv); nenhum dado de zeros é usado.
Ingredientes: DLMF 25.2.1 (série de Dirichlet, ℜs>1), DLMF 25.2.10 (Euler–Maclaurin, ℜs > −2n), fórmula de Jensen.
"""
import json, sys
from mpmath import iv
sys.path.insert(0, "results/etapa11_3b")
from interval_export import sup_str, inf_str
iv.dps = 30
out = {}
# |B~3| <= sqrt(3)/36 (máximo exato de B3 em [0,1]); |B~5| <= 1 + 5/2 + 5/3 + 1/6 (cota grosseira pelos coeficientes)
B3 = iv.sqrt(3) / 36
B5 = iv.mpf(1) + iv.mpf(5)/2 + iv.mpf(5)/3 + iv.mpf(1)/6
zeta2_lower = iv.mpf(1) / 4           # |ζ(2+it)| ≥ 1 − Σ_{n≥2} n^{-2} ≥ 1 − 3/4
# (A) T ≥ 5: disco centrado em 2+iT, R = 3, r = 9/4 (cobre [0,1]×[T−1,T+1], pois √5 < 9/4)
def M_A(T):
    T = iv.mpf(T)
    s_abs = T + 5                      # |s| ≤ √(4+T²) + 3 ≤ T + 5 para T ≥ 5
    return (1/(iv.sqrt(1+T**2) - 3) + iv.mpf(1)/2 + s_abs/12
            + (s_abs+2)*(s_abs+1)*s_abs/6 * B3 / 1)   # σ+2 ≥ 1 no disco
cA = 3 / iv.log(iv.mpf(4)/3)
ok = True
for T in [5, 6, 10, 100, 1e3, 1e4, 1e5, 1e8, 1e12]:
    lhs = 4*M_A(T); rhs = (iv.mpf(T)+8)**3
    ok = ok and bool(lhs.b <= rhs.a)
out["A"] = {"afirmacao": "para T>=5: N(T+1)-N(T-1) <= log(4 M_R)/log(4/3) <= 3 log(T+8)/log(4/3) <= 10.5 log(T+8)",
            "3/log(4/3)_sup": float(cA.b), "4M_R <= (T+8)^3 conferido nos T amostrados": ok,
            "nota": "4M_R ≤ (T+8)^3 para todo T≥5 segue de os termos serem ≤ polinômio de grau 3 com coeficiente líder 4√3/216 < 1 (ver doc); amostras só ilustram"}
# (B) N(5): f(s) = (s−1)ζ(s), centro 2+2.5i, R = 9/2, r = 13/4 (cobre [0,1]×[0,5]: distância máx √(4+6.25) ≈ 3.20 < 3.25)
s0_abs = iv.sqrt(iv.mpf(4) + iv.mpf(25)/4)
s_abs = s0_abs + iv.mpf(9)/2; sm1 = s_abs + 1       # |s| e |s−1| no disco
sigma_plus4 = iv.mpf(3)/2                           # σ ≥ 2 − 4.5 = −2.5
term1 = sm1*(iv.mpf(1)/2 + s_abs/12 + (s_abs+2)*(s_abs+1)*s_abs/6 * (iv.mpf(1)/120))
term2 = sm1*(s_abs+4)*(s_abs+3)*(s_abs+2)*(s_abs+1)*s_abs/120 * B5/sigma_plus4
MB = 1 + term1 + term2
f0 = iv.sqrt(iv.mpf(1) + iv.mpf(25)/4) * zeta2_lower
NB = (iv.log(MB) - iv.log(f0)) / iv.log(iv.mpf(18)/13)
out["B"] = {"M_R_sup": float(MB.b), "|f(s0)|_inf": float(f0.a), "N(5)_cota_sup": float(NB.b)}
N5 = int(NB.b)   # floor da cota superior
out["C"] = {"afirmacao": f"para T>=5: N(T) <= {N5} + 5.25 T log(T+9)",
            "T>=7e4 => N(T) <= T^2": bool((N5 + iv.mpf('5.25')*iv.mpf(7e4)*iv.log(iv.mpf(7e4)+9)).b <= iv.mpf(7e4)**2)}
# (D) Z1 explícito: Σ_ρ 1/(1+t²) = 2 Σ_{t>0}; zeros com t ≤ 4 contam ≤ N(5); blocos diádicos (2^k, 2^{k+1}], k ≥ 2.
# Soma explícita para 2 ≤ k ≤ 259 e cota ANALÍTICA para k ≥ 260 incluída no intervalo (revisão 11.3b-6):
#   termo_k ≤ (31 + 5,25·2^{k+1}·log(2^{k+1}+9))/4^k ≤ 31·4^{−k} + 10,5·log2·(k+2)·2^{−k}   [log(2^{k+1}+9) ≤ (k+2)log 2, k ≥ 3]
#   Σ_{k≥K} 4^{−k} = (4/3)·4^{−K};   Σ_{k≥K} (k+2)·2^{−k} = 2^{−K}·(2K+6)
K = 260
S = iv.mpf(N5)
for k in range(2, K):
    Nk = N5 + iv.mpf('5.25')*iv.mpf(2)**(k+1)*iv.log(iv.mpf(2)**(k+1)+9)
    S += Nk / (1 + iv.mpf(2)**(2*k))
tail = 31*(iv.mpf(4)/3)*iv.mpf(4)**(-K) + iv.mpf('10.5')*iv.log(2)*iv.mpf(2)**(-K)*(2*K+6)
half = S + tail
total = 2*half
out["D"] = {"Sigma_{t>0} 1/(1+t^2): intervalo": str(half), "Sigma_{t>0}: sup arredondado para cima": sup_str(half),
            "cauda_analitica_k>=260: sup arredondado para cima": sup_str(tail, 90),
            "Z1_total: intervalo": str(total), "Z1_total: sup arredondado para cima": sup_str(total),
            "Z1_total <= 101": bool(total.b <= 101)}
# exportação dos demais extremos como strings arredondadas para fora
out["A"]["3/log(4/3): sup arredondado para cima"] = sup_str(cA); out["A"].pop("3/log(4/3)_sup", None)
out["B"] = {"M_R: sup arredondado para cima": sup_str(MB), "|f(s0)|: inf arredondado para baixo": inf_str(f0),
            "N(5): sup arredondado para cima": sup_str(NB), "N(5) <= 31": bool(NB.b < 32)}
print(json.dumps(out, indent=1))
json.dump(out, open("results/etapa11_3b/zero_count_bound.json", "w"), indent=1)
