"""
11.3b / H2: checagens numéricas (classe B) dos PASSOS da derivação analítica do termo arquimediano
(docs/ETAPA11_3B_TERMO_ARQUIMEDIANO.md). Não substituem a derivação; conferem cada identidade intermediária.

  (P1) Connes App. II (31): Pfw ∫_{ℝ*} f0³(|u|) |u|^{1/2}/|1−u| d*u = log π + γ.
       Pela derivação: D_∞(F) = g(0) log π − T[g], com g(x) = F(e^x) = e^{−3|x|/2}, logo deve valer T[g] = −γ.
  (P2) Definição (10)–(11) de Connes avaliada diretamente, com t finito e extrapolação em 1/t, contra g(0) log π − T[g],
       para g gaussiana.
  (P3) T[g] = ∫_0^∞ [g(0)e^{−2x}/x − (g(x)/2)K(x)] dx  contra  (1/2π)∫ h(r) Re ψ(1/4 + ir/2) dr, com h = ∫ g e^{irx} dx.
  K(x) = 1/sinh(x/2) + 1/cosh(x/2).
"""
import json
import mpmath as mp
mp.mp.dps = 30
K = lambda x: 1/mp.sinh(x/2) + 1/mp.cosh(x/2)

def T_of(g):
    return mp.quad(lambda x: g(0)*mp.e**(-2*x)/x - g(x)/2*K(x), [0, 1, 10, mp.inf])

def D_inf_connes(g, t):
    # (10)-(11) em x = log ν: ψ(e^x) = (g(x)/4)[1/|sinh(x/2)| + 1/cosh(x/2)], f0^{2t} = e^{−t|x|}, c = g(0)/2, d*ν = dx
    I = 2*mp.quad(lambda x: (1 - mp.e**(-t*x))*g(x)/4*K(x), [0, 1/t, 1, 10, mp.inf])  # g par
    c = g(0)/2
    return 2*mp.log(2*mp.pi)*c + I - 2*c*mp.log(t)

out = {}
g1 = lambda x: mp.e**(-mp.mpf(3)/2*abs(x))
T1 = T_of(g1)
out["P1"] = {"T[e^{-3|x|/2}]": float(T1), "-euler_gamma": float(-mp.euler), "diff": float(T1 + mp.euler),
             "D_inf_derivado": float(mp.log(mp.pi) - T1), "log(pi)+gamma (Connes (31))": float(mp.log(mp.pi) + mp.euler)}
T0 = mp.mpf(5)
g2 = lambda x: T0/(2*mp.sqrt(mp.pi))*mp.e**(-(T0*x)**2/4)
h2 = lambda r: mp.e**(-(r/T0)**2)
T2 = T_of(g2)
ts = [mp.mpf(10)**k for k in (3, 4, 5)]
vals = [D_inf_connes(g2, t) for t in ts]
extrap = vals[-1] + (vals[-1]-vals[-2])*(ts[-2]/(ts[-1]-ts[-2]))  # Richardson em 1/t
out["P2"] = {"D_inf_(11)_t=1e3,1e4,1e5": [float(v) for v in vals], "extrapolado": float(extrap),
             "g(0)logpi - T": float(g2(0)*mp.log(mp.pi) - T2), "diff_extrap": float(extrap - (g2(0)*mp.log(mp.pi) - T2))}
rhs = mp.quad(lambda r: h2(r)*mp.re(mp.digamma(mp.mpf(1)/4 + 1j*r/2)), [-mp.inf, -50, 0, 50, mp.inf])/(2*mp.pi)
out["P3"] = {"T[g]": float(T2), "(1/2pi)∫h Re psi": float(rhs), "diff": float(T2 - rhs)}
print(json.dumps(out, indent=1))
json.dump(out, open("results/etapa11_3b/check_archimedean_derivation.json", "w"), indent=1)
