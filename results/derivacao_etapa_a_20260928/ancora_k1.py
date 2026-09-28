"""Âncora k = 1 da Etapa A: d/dT ∫|L(1/2+it,χ)|² dt ≈ (φ(q)/q)(log(qT/2π) + C). Estima a inclinação em log(qt/2π) das médias
de |Z_χ(t)|² em janelas; o modelo (manter (1−1/p) em p|q) prevê φ(q)/q; descartá-lo preveria 1."""
import sys, math, time, numpy as np, mpmath as mp
sys.path.insert(0, 'results/momentos_negativos_20260927'); sys.path.insert(0, 'results/etapa11_6_controles/dirichlet')
import dirichlet_zeros as dz
from mn3_caracteres import CHARS
chars = {"chi_m4": dz.CHARACTERS["chi_m4"], "chi_12": CHARS["chi_12"]}
mp.mp.dps = 15
rng = np.random.default_rng(20260928)
for name, ch in chars.items():
    t0 = time.process_time()
    t = np.sort(rng.uniform(50, 650, 3000))
    v = np.array([float(abs(dz.Z_complex(x, ch))**2) for x in t])
    edges = np.linspace(50, 650, 13); X, Y = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        s = (t >= a) & (t < b); X.append(math.log(ch.q * (a + b) / 2 / (2 * math.pi))); Y.append(v[s].mean())
    slope, icpt = np.polyfit(X, Y, 1)
    # incerteza da inclinação por bootstrap das amostras dentro das janelas
    bs = []
    for _ in range(500):
        idx = rng.integers(0, len(t), len(t)); tt, vv = t[idx], v[idx]; Yb = []
        for a, b in zip(edges[:-1], edges[1:]):
            s = (tt >= a) & (tt < b); Yb.append(vv[s].mean())
        bs.append(np.polyfit(X, Yb, 1)[0])
    phi = {"chi_m4": 1/2, "chi_12": 1/3}[name]
    print(f"{name}: inclinação {slope:.3f} [{np.quantile(bs,.025):.3f}, {np.quantile(bs,.975):.3f}]  previsto φ(q)/q = {phi:.3f}  (alternativa 1)  CPU {time.process_time()-t0:.0f} s", flush=True)
