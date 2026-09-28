"""
Reproduces Table 1 of the note (all R values and 95% intervals) from the data in this package.

Requirements: Python 3, numpy. Needs Odlyzko's table `zeros1` (https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1)
for the ordinates of the zeta zeros, which are not redistributed here; pass its path with --zeros1.
The random seeds and the order of the bootstrap calls are those of the pre-registered analyses (MN-1: 20260927,
MN-2: 20260928, MN-3: 20260929), so the intervals are reproduced exactly.
"""
import argparse, hashlib, math, sys
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "code"))
from discrete_moments import block_bootstrap_ratio   # noqa: E402

ZEROS1_SHA256 = "3436c916a7878261ac183fd7b9448c9a4736b8bbccf1356874a6ce1788541632"

def zeta_data(zeros1, n):
    if hashlib.sha256(Path(zeros1).read_bytes()).hexdigest() != ZEROS1_SHA256:
        sys.exit("zeros1: SHA-256 differs from the file used in the computations")
    g = np.loadtxt(zeros1)[:n]
    idx, dz, L2 = np.loadtxt(HERE / "data" / "zeta_values_1-27000.txt", unpack=True)
    assert np.array_equal(idx[:n], np.arange(1, n + 1))
    return g, dz[:n], L2[:n]

def chi_data(name):
    g, d = np.loadtxt(HERE / "data" / f"derivatives_{name}.txt", unpack=True)
    g2, L2 = np.loadtxt(HERE / "data" / f"L2rho_{name}.txt", unpack=True)
    assert np.allclose(g, g2)
    return g, d, L2

def vw(g, d, L2, q):
    dens = np.log(q * g / (2 * math.pi))
    return dens / d**2, dens * L2**2 / d**2, dens

def edges_of(dens):
    e = np.quantile(dens, np.linspace(0, 1, 11)); e[0] -= 1e-9; e[-1] += 1e-9
    return e

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--zeros1", required=True); a = ap.parse_args()
    rows = []
    Q = {"chi_m4": 4, "chi_5": 5, "chi_8": 8, "chi_12": 12}
    for seed, which, nz, keys in ((20260927, "C7", 20000, ["chi_m4", "chi_5"]),
                                  (20260928, "C8", 20000, ["chi_m4", "chi_5"]),
                                  (20260929, "both", 27000, ["chi_8", "chi_12"])):
        rng = np.random.default_rng(seed)
        vz, wz, dzz = vw(*zeta_data(a.zeros1, nz), 1)
        for k in keys:
            v, w, dens = vw(*chi_data(k), Q[k])
            e = edges_of(dens)
            for conj, x, xr in (("C7", v, vz), ("C8", w, wz)):
                if which in (conj, "both"):
                    r = block_bootstrap_ratio(x, dens, xr, dzz, e, 100, 2000, rng)
                    rows.append((Q[k], conj, r["R"], r["q025"], r["q975"]))
    print(f"{'q':>3} {'conj':>5} {'R':>7} {'2.5%':>7} {'97.5%':>7}")
    for q, c, R, lo, hi in sorted(rows, key=lambda t: (t[1], t[0])):
        print(f"{q:>3} {c:>5} {R:7.3f} {lo:7.3f} {hi:7.3f}")

if __name__ == "__main__":
    main()
