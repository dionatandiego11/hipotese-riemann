"""
11.3b / L-EF2a, ponto 1: erro integrado do termo determinístico
  |∫_A^B w(E) e_t(E) (θ'(E)/π − d̄_rvm(E)) dE| ≤ ∫_A^B w |Δ| dE ≤ sup_[A,B] |Δ| · L/2,
com Δ(E) = (1/2π)[Re ψ(1/4 + iE/2) − log π] − (1/2π) log(E/2π) (funções explícitas; mpmath, 40 dígitos).
Também a integral exata ∫ w |Δ| por quadratura e a expansão assintótica −1/(48π E²) para conferência.
"""
import glob, json
import mpmath as mp
mp.mp.dps = 40
def delta(E):
    E = mp.mpf(E)
    return (mp.re(mp.digamma(mp.mpf(1)/4 + 1j*E/2)) - mp.log(mp.pi))/(2*mp.pi) - mp.log(E/(2*mp.pi))/(2*mp.pi)
runs = {"m4-v1": "results/run_20260913_144429_m3_b01*", "m4-v2": "results/run_20260913_173045_m3_c01*",
        "m4-v3": "results/run_20260913_220906_m3_d01*"}
out = []
for ver, pat in runs.items():
    m = json.load(open(glob.glob(pat)[0] + "/metrics.json"))
    for name, blk in m["blocks"].items():
        A, B = mp.mpf(blk["instrument"]["A"]), mp.mpf(blk["instrument"]["B"]); L = B - A
        dA, dB = delta(A), delta(B)
        w = lambda E: mp.sin(mp.pi*(E-A)/L)**2
        exact = mp.quad(lambda E: w(E)*abs(delta(E)), [A, (A+B)/2, B])
        rec = {"versao": ver, "bloco": name, "L": float(L), "Delta(A)": float(dA), "Delta(B)": float(dB),
               "assint_-1/(48 pi A^2)": float(-1/(48*mp.pi*A**2)), "cota_sup_L/2": float(max(abs(dA), abs(dB))*L/2),
               "integral_w_abs_Delta": float(exact)}
        out.append(rec)
json.dump(out, open("results/etapa11_3b/density_error_bound.json", "w"), indent=1)
print(json.dumps(out[0])); print(json.dumps(out[-1]))
print("max cota:", max(r["cota_sup_L/2"] for r in out))
