"""
11.3b / L-EF2a(a3): cota CERTIFICADA (módulo a cota de resto da DLMF 5.11(ii)) para o termo determinístico
    |∫_A^B w e_t Δ dE| ≤ ∫_A^B w |Δ| dE,   Δ(E) = (1/2π)[Re ψ(1/4 + iE/2) − ln(E/2)]   (= θ'/π − d̄_rvm).
Derivação (z = 1/4 + iE/2, E > 0):
  DLMF 5.11.2 truncada em n = 1:  ψ(z) = ln z − 1/(2z) + R,  |R| ≤ sec³(½ ph z) · |B₂/(2 z²)| = sec³(½ ph z)/(12|z|²)
  (DLMF 5.11(ii): 'If z is complex, then the remainder terms are bounded in magnitude by sec^{2n+1}(½ ph z) for (5.11.2),
  times the first neglected terms').  Para ℜz > 0: |½ ph z| < π/4, sec³ < 2√2.
  ln|z| − ln(E/2) = ½ ln(1 + 1/(4E²)) ∈ [0, 1/(8E²)];   ℜ(1/(2z)) = (1/4)/(2|z|²) ∈ (0, 1/(2E²)]  (|z|² ≥ E²/4);
  |ℜR| ≤ 2√2/(12|z|²) ≤ (2√2/3)/E².
  ⇒ |Δ(E)| ≤ C/E²,  C = (1/8 + 1/2 + 2√2/3)/(2π)  (cota superior calculada em aritmética intervalar).
  ⇒ ∫_A^B w|Δ| ≤ C ∫_A^B w/E² dE ≤ C (L/2)/A²   (w ≤ 1, ∫w = L/2, 1/E² ≤ 1/A²).
Nenhuma maximização numérica: a cota é uma função explícita de A e L, avaliada com intervalos (mpmath.iv).
Os valores A, B vêm dos metrics.json de m4 (arredondamento decimal de 9 casas; A é tomado 10⁻⁶ menor, B 10⁻⁶ maior).
"""
import glob, json, sys
from mpmath import iv
sys.path.insert(0, "results/etapa11_3b")
from interval_export import sup_str
iv.dps = 30
C = (iv.mpf(1)/8 + iv.mpf(1)/2 + 2*iv.sqrt(2)/3) / (2*iv.pi)
runs = {"m4-v1": "results/run_20260913_144429_m3_b01*", "m4-v2": "results/run_20260913_173045_m3_c01*",
        "m4-v3": "results/run_20260913_220906_m3_d01*"}
out = []
for ver, pat in runs.items():
    m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
    for name, blk in m["blocks"].items():
        A = iv.mpf(blk["instrument"]["A"]) - iv.mpf("1e-6"); B = iv.mpf(blk["instrument"]["B"]) + iv.mpf("1e-6")
        L = B - A
        bound = C * (L / 2) / A**2
        out.append({"versao": ver, "bloco": name, "cota_sup_arredondada_para_cima": sup_str(bound, 15), "C_sup_arredondado_para_cima": sup_str(C, 15)})
json.dump(out, open("results/etapa11_3b/density_error_certified.json", "w"), indent=1)
print("C <=", sup_str(C, 15)); print("max:", max(out, key=lambda o: float(o["cota_sup_arredondada_para_cima"]))["cota_sup_arredondada_para_cima"], "min:", min(out, key=lambda o: float(o["cota_sup_arredondada_para_cima"]))["cota_sup_arredondada_para_cima"])
