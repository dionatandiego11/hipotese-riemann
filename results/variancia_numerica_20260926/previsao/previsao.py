"""
Previsões ANTES de medir Σ²(L) nos zeros (ficha FICHA_VARIANCIA_NUMERICA). Usa só primos, alturas obtidas por inversão
da contagem suave (sem ler zeros) e substitutos GUE para o ruído do estimador. Semente explícita.
"""
import json, math, sys, time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from scipy.special import loggamma
from riemann_spectra.number_variance import sigma2_gue, sigma2_berry_averaged, number_variance
from riemann_spectra.unfolding import inverse_n_bar
from riemann_spectra.controls import generate_gue_central_levels

OUT = Path(__file__).parent
L = np.array([0.25, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30], dtype=float)
TAU_MAIN, TAU_SENS = 0.5, (0.25, 0.75)
SEED = 20260926
t0 = time.time()

def theta_chi(t, q, kappa):
    a = 0.25 + 0.5 * kappa
    return np.imag(loggamma(a + 0.5j * t)) + 0.5 * t * math.log(q / math.pi)

def E_of_index_chi(k, q, kappa):
    # altura aproximada do k-ésimo zero: θ_χ(t)/π = k − 1/2 (só para escolher a altura local da fórmula)
    return brentq(lambda t: theta_chi(t, q, kappa) / math.pi - (k - 0.5), 1e-3, 1e6)

res = {"L": L.tolist(), "tau_main": TAU_MAIN, "tau_sens": TAU_SENS, "seed": SEED, "gue": sigma2_gue(L).tolist()}

# ζ: 10 blocos de 10.000 zeros; alturas locais em 200 índices por bloco
zeta = {}
for b in range(10):
    i0, i1 = 10000 * b + 1, 10000 * (b + 1)
    E = inverse_n_bar(np.linspace(i0, i1, 200))
    d = {"indices": [i0, i1], "E_min": float(E[0]), "E_max": float(E[-1])}
    for tau in (TAU_MAIN,) + TAU_SENS:
        d[f"berry_tau{tau}"] = sigma2_berry_averaged(L, E, tau_star=tau).tolist()
    zeta[f"b{b+1:02d}"] = d
res["zeta"] = zeta

# χ: zeros 1–3000 (e01/f01, fora da reserva)
chis = {"chi_m4": (4, 1, {2}), "chi_5": (5, 0, {5})}
chi = {}
for name, (q, kappa, excl) in chis.items():
    E = np.array([E_of_index_chi(k, q, kappa) for k in np.linspace(1, 3000, 200)])
    d = {"q": q, "kappa": kappa, "primos_excluidos": sorted(excl), "E_min": float(E[0]), "E_max": float(E[-1])}
    w_chi = lambda p, ex=excl: 0 if p in ex else 1
    for tau in (TAU_MAIN,) + TAU_SENS:
        d[f"berry_chi_tau{tau}"] = sigma2_berry_averaged(L, E, tau_star=tau, q=q, weight=w_chi).tolist()
    # alternativa errada (controle de conteúdo): todos os primos, mesma densidade
    d["berry_todos_primos_tau0.5"] = sigma2_berry_averaged(L, E, tau_star=TAU_MAIN, q=q, weight=lambda p: 1).tolist()
    chi[name] = d
res["chi"] = chi

# ruído do estimador: substitutos GUE (uma matriz por réplica), mesmo estimador e parâmetros
rng = np.random.default_rng(SEED)
noise = {}
for N, R in ((10000, 30), (3000, 60)):
    Vs, sg = [], []
    for _ in range(R):
        r = number_variance(generate_gue_central_levels(N, rng=rng)[0], L)
        Vs.append(r["V"]); sg.append(r["sigma"])
    Vs, sg = np.array(Vs), np.array(sg)
    noise[str(N)] = {"R": R, "media_V": Vs.mean(0).tolist(), "dp_replicas": Vs.std(0, ddof=1).tolist(),
                     "media_sigma_subblocos": sg.mean(0).tolist()}
res["ruido_gue"] = noise
res["segundos"] = round(time.time() - t0, 1)
(OUT / "previsao.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
print("ok", res["segundos"], "s")
