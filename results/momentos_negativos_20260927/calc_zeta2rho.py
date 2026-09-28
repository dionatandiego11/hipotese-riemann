"""MN-2: |L(2ρ,χ²)| nos zeros. χ real ⇒ χ² principal mod q ⇒ L(2ρ,χ²) = ζ(2ρ)∏_{p|q}(1 − p^{−2ρ}), 2ρ = 1 + 2iγ.
mpmath dps 15; teto de CPU por RLIMIT_CPU; lê os mesmos γ das derivadas da MN-1."""
import argparse, resource
from pathlib import Path
import numpy as np, mpmath as mp
OUT = Path(__file__).parent
PRIMES = {"zeta": [], "chi_m4": [2], "chi_5": [5]}
ap = argparse.ArgumentParser(); ap.add_argument("--fonte", required=True, choices=list(PRIMES)); ap.add_argument("--n", type=int, required=True)
ap.add_argument("--teto-cpu", type=int, required=True); a = ap.parse_args()
resource.setrlimit(resource.RLIMIT_CPU, (a.teto_cpu, a.teto_cpu + 60))
g = np.loadtxt(OUT / f"derivadas_{a.fonte}_{a.n}.txt")[:, 0]
mp.mp.dps = 15
out = []
for i, t in enumerate(g):
    s = mp.mpc(1, 2 * t)
    v = mp.zeta(s)
    for p in PRIMES[a.fonte]:
        v *= 1 - mp.power(p, -s)
    out.append(abs(complex(v)))
    if (i + 1) % 2000 == 0:
        print(f"{a.fonte}: {i+1}/{len(g)}", flush=True)
np.savetxt(OUT / f"L2rho_{a.fonte}_{a.n}.txt", np.column_stack([g, out]), fmt="%.9f %.12e", header="gamma |L(2rho,chi^2)|")
print("terminado", flush=True)
