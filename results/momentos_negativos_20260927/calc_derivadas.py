"""
Calcula |L′(ρ)| = |Z′(γ)| nos zeros (MN-1). ζ: mpmath.siegelz(t, derivative=1), dps 15. χ: diferença central de
Z_real (dirichlet_zeros congelado) com h = 1e-6, dps 20. Checkpoint a cada 100 zeros; teto de CPU por RLIMIT_CPU.
Uso: calc_derivadas.py --fonte {zeta,chi_m4,chi_5} --n N --teto-cpu SEGUNDOS
"""
import argparse, json, resource, sys, time
from pathlib import Path
import numpy as np
import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "results/etapa11_6_controles/dirichlet"))

def load(fonte, n):
    if fonte == "zeta":
        return np.loadtxt(ROOT / "data/processed/zeros_100k.csv", delimiter=",", skiprows=1)[:n, 1]
    f = ROOT / f"results/etapa11_6_controles/dirichlet/completude/zeros_{fonte}_12000_completo.txt"
    return np.loadtxt(f)[:n]          # corte imediato; zeros além de n não entram em cálculo algum

def deriv(fonte, t):
    if fonte == "zeta":
        mp.mp.dps = 15
        return abs(float(mp.siegelz(t, derivative=1)))
    import dirichlet_zeros as dz
    mp.mp.dps = 20
    ch, h = dz.CHARACTERS[fonte], mp.mpf("1e-6")
    return abs(float((dz.Z_real(mp.mpf(t) + h, ch) - dz.Z_real(mp.mpf(t) - h, ch)) / (2 * h)))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonte", required=True, choices=["zeta", "chi_m4", "chi_5"])
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--teto-cpu", type=int, required=True)
    a = ap.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU, (a.teto_cpu, a.teto_cpu + 60))
    g = load(a.fonte, a.n)
    ck = OUT / f"progresso_{a.fonte}.json"
    st = json.loads(ck.read_text()) if ck.exists() else {"d": []}
    d = st["d"]
    t0 = time.process_time()
    for i in range(len(d), len(g)):
        d.append(deriv(a.fonte, g[i]))
        if (i + 1) % 100 == 0 or i + 1 == len(g):
            st.update(d=d, feitos=len(d), cpu_sessao=time.process_time() - t0)
            tmp = ck.with_suffix(".tmp"); tmp.write_text(json.dumps(st)); tmp.replace(ck)
            print(f"{a.fonte}: {len(d)}/{len(g)} ({time.process_time() - t0:.0f} s CPU nesta sessão)", flush=True)
    np.savetxt(OUT / f"derivadas_{a.fonte}_{a.n}.txt", np.column_stack([g, d]), fmt="%.9f %.12e",
               header="gamma |Z'(gamma)| = |L'(rho)|")
    print("terminado", flush=True)

if __name__ == "__main__":
    main()
