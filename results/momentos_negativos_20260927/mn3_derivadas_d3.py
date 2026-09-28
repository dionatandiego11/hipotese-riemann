"""MN-3 (ADENDO_MN3_2): idêntico a mn3_derivadas.py, exceto a pasta de entrada (mn3_zeros_d3/, lista corrigida pelo
passe de completude) e a mensagem de aborto. Aborta se o manifesto da correção não estiver aprovado."""
import argparse, json, resource
from pathlib import Path
import numpy as np, mpmath as mp
from mn3_caracteres import CHARS, dz
OUT = Path(__file__).parent
PRIMES = {"chi_8": [2], "chi_12": [2, 3]}
ap = argparse.ArgumentParser(); ap.add_argument("--carater", choices=list(CHARS), required=True)
ap.add_argument("--n", type=int, required=True); ap.add_argument("--teto-cpu", type=int, required=True); a = ap.parse_args()
resource.setrlimit(resource.RLIMIT_CPU, (a.teto_cpu, a.teto_cpu + 60))
Z = OUT / "mn3_zeros_d3"
man = json.loads((Z / f"manifest_{a.carater}_{a.n}.json").read_text())
if not man.get("all_checks_passed"):
    raise SystemExit(f"{a.carater}: correção não aceita (ADENDO_MN3_2 §1); derivadas não calculadas")
g = np.loadtxt(Z / f"zeros_{a.carater}_{a.n}.txt")
ch, h = CHARS[a.carater], mp.mpf("1e-6")
d, L2 = [], []
for t in g:
    mp.mp.dps = 20
    d.append(abs(float((dz.Z_real(mp.mpf(t) + h, ch) - dz.Z_real(mp.mpf(t) - h, ch)) / (2 * h))))
    mp.mp.dps = 15
    s = mp.mpc(1, 2 * t); v = mp.zeta(s)
    for p in PRIMES[a.carater]:
        v *= 1 - mp.power(p, -s)
    L2.append(abs(complex(v)))
np.savetxt(OUT / f"derivadas_{a.carater}_{a.n}.txt", np.column_stack([g, d]), fmt="%.9f %.12e", header="gamma |L'(rho)|")
np.savetxt(OUT / f"L2rho_{a.carater}_{a.n}.txt", np.column_stack([g, L2]), fmt="%.9f %.12e", header="gamma |L(2rho,chi^2)|")
print("terminado")
