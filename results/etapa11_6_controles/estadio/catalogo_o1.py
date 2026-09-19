"""
Catálogo O1 do `ctrl-estadio-v1` (DECLARACAO_ESTADIO.md §3, P2): comprimentos das órbitas periódicas do quarto de
estádio (raio 1, trecho reto a = 1 no quarto; `qust:2` do vergini) com L ≤ 5,5 e até 8 colisões. Calculado ANTES de
qualquer nível do bilhar ser usado. Classe B (busca numérica; completude não demonstrada).

Procedimento (fixado neste arquivo antes da execução):
  1. Órbitas do quarto = "órbitas relativas" do estádio inteiro: sequência de n reflexões na fronteira do estádio
     inteiro (sem cantos; C¹) que fecha a menos de um elemento g do grupo de simetria G = {id, σx, σy, σxσy}:
     o último segmento vai de q_n a g(q_1). O comprimento é L = Σ|q_{i+1} − q_i| + |g(q_1) − q_n|, e as órbitas são os
     pontos estacionários de L (reflexão especular em cada q_i). Dobrar por (x, y) ↦ (|x|, |y|) dá a órbita do quarto,
     com reflexões nos eixos onde o segmento cruza x = 0 ou y = 0.
  2. Para n = 1..8 e cada g ≠ id (e g = id para n ≥ 2): partidas aleatórias (semente fixa), raiz do gradiente
     (scipy.optimize.root, 'hybr'); aceita se max|∂L/∂s_i| ≤ 1e-10 e nenhum segmento corre ao longo de uma parede reta.
  3. Colisões no quarto = reflexões na fronteira externa (n) + cruzamentos de eixos pelos segmentos; um cruzamento na
     origem conta 2; um ponto de reflexão sobre um eixo ((0, ±1) ou (±2, 0)) conta +1 (canto do quarto).
     Mantêm-se só órbitas com L ≤ 5,5 e ≤ 8 colisões.
  4. Primitividade e unicidade pela órbita dobrada: chave = (L arredondado a 1e-8, conjunto ordenado dos pontos de
     reflexão dobrados arredondados a 1e-7). Sequência dobrada com período menor que n = repetição (descartada; a
     primitiva aparece com n menor).
  5. Famílias: autovalor da hessiana de L com |λ| ≤ 1e-6 ⇒ órbita não isolada (família), marcada.
     Órbitas cuja órbita dobrada corre sobre um eixo do quarto são marcadas "fronteira".
  6. Estabilidade da busca: repetir com uma segunda semente; o catálogo final é a união, e o relatório diz se a segunda
     semente acrescentou algo.

Uso (da raiz):  .venv/bin/python3 results/etapa11_6_controles/estadio/catalogo_o1.py
"""
import csv
import hashlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import root

A = 1.0                 # meio trecho reto do estádio inteiro (= trecho reto do quarto)
R = 1.0                 # raio
P = 4 * A + 2 * math.pi * R
L_MAX, COLL_MAX, N_MAX = 5.5, 8, 8
G = {"id": (1, 1), "sx": (-1, 1), "sy": (1, -1), "sxsy": (-1, -1)}
S0 = 2 * A                          # fim da parede de cima
S1 = S0 + math.pi * R               # fim do arco esquerdo
S2 = S1 + 2 * A                     # fim da parede de baixo


def point(s):
    """Fronteira do estádio inteiro, anti-horária, s ∈ [0, P): cima (1,1)→(−1,1); arco esq.; baixo; arco dir."""
    s = s % P
    if s < S0:
        return np.array([A - s, R]), np.array([-1.0, 0.0]), "wall"
    if s < S1:
        ph = math.pi / 2 + (s - S0) / R
        return np.array([-A + R * math.cos(ph), R * math.sin(ph)]), np.array([-math.sin(ph), math.cos(ph)]), "arc"
    if s < S2:
        return np.array([-A + (s - S1), -R]), np.array([1.0, 0.0]), "wall"
    ph = -math.pi / 2 + (s - S2) / R
    return np.array([A + R * math.cos(ph), R * math.sin(ph)]), np.array([-math.sin(ph), math.cos(ph)]), "arc"


def chords(s, g):
    gx, gy = G[g]
    pts = [point(x) for x in s]
    q = [p[0] for p in pts]
    n = len(s)
    nxt = [q[i + 1] if i < n - 1 else q[0] * np.array([gx, gy]) for i in range(n)]
    prv = [q[i - 1] if i > 0 else q[n - 1] * np.array([gx, gy]) for i in range(n)]   # g = g⁻¹
    return pts, q, nxt, prv


def length(s, g):
    _, q, nxt, _ = chords(s, g)
    return float(sum(np.linalg.norm(nxt[i] - q[i]) for i in range(len(s))))


def grad(s, g):
    pts, q, nxt, prv = chords(s, g)
    out = np.empty(len(s))
    for i in range(len(s)):
        a, b = q[i] - prv[i], nxt[i] - q[i]
        na, nb = np.linalg.norm(a), np.linalg.norm(b)
        if na < 1e-12 or nb < 1e-12:
            return np.full(len(s), 1e3)
        out[i] = pts[i][1] @ (a / na - b / nb)
    return out


def hessian(s, g, h=1e-6):
    n = len(s)
    H = np.empty((n, n))
    for j in range(n):
        e = np.zeros(n); e[j] = h
        H[:, j] = (grad(s + e, g) - grad(s - e, g)) / (2 * h)
    return 0.5 * (H + H.T)


def same_wall(p1, p2):
    return abs(p1[1]) == R and abs(p2[1]) == R and abs(p1[1] - p2[1]) < 1e-12 and abs(p1[0]) <= A + 1e-12 and abs(p2[0]) <= A + 1e-12


def fold(p):
    return (abs(p[0]), abs(p[1]))


def axis_crossings(p, q):
    """Cruzamentos de x = 0 e y = 0 no interior do segmento p→q (extremos excluídos); origem conta 2."""
    c = 0
    for k in (0, 1):
        if (p[k] > 1e-12 and q[k] < -1e-12) or (p[k] < -1e-12 and q[k] > 1e-12):
            c += 1
    return c


def on_axis(p):
    return abs(p[0]) < 1e-9 or abs(p[1]) < 1e-9


def analyse(s, g):
    pts, q, nxt, _ = chords(s, g)
    n = len(s)
    for i in range(n):
        if np.linalg.norm(nxt[i] - q[i]) < 1e-9 or same_wall(q[i], nxt[i]):
            return None
    L = length(s, g)
    coll = n + sum(axis_crossings(q[i], nxt[i]) for i in range(n)) + sum(1 for x in q if on_axis(x))
    folded = [tuple(round(v, 7) for v in fold(x)) for x in q]
    per = n
    for d in range(1, n):
        if n % d == 0 and all(folded[i] == folded[(i + d) % n] for i in range(n)):
            per = d
            break
    eig = np.linalg.eigvalsh(hessian(s, g))
    boundary = all((abs(q[i][0]) < 1e-9 and abs(nxt[i][0]) < 1e-9) or (abs(q[i][1]) < 1e-9 and abs(nxt[i][1]) < 1e-9)
                   or axis_along(q[i], nxt[i]) for i in range(n))
    return {"L": L, "n_outer": n, "g": g, "collisions_quarter": coll, "primitive": per == n,
            "family": bool(np.min(np.abs(eig)) <= 1e-6), "min_abs_hess_eig": float(np.min(np.abs(eig))),
            "boundary_orbit": bool(boundary), "folded_points": sorted(folded),
            "points": [[float(x[0]), float(x[1])] for x in q], "s": [float(v % P) for v in s]}


def axis_along(p, q):
    """Segmento que, dobrado, corre sobre um eixo do quarto (atravessa o estádio sobre y = 0 ou x = 0)."""
    return (abs(p[1]) < 1e-9 and abs(q[1]) < 1e-9) or (abs(p[0]) < 1e-9 and abs(q[0]) < 1e-9)


def search(seed, starts_per_n):
    rng = np.random.default_rng(seed)
    found = {}
    for n in range(1, N_MAX + 1):
        for g in G:
            if g == "id" and n < 2:
                continue
            for _ in range(starts_per_n(n)):
                s0 = np.sort(rng.uniform(0, P, n)) if rng.random() < 0.5 else rng.uniform(0, P, n)
                sol = root(grad, s0, args=(g,), method="hybr", options={"xtol": 1e-14, "maxfev": 400 * (n + 1)})
                s = sol.x
                gr = grad(s, g)
                if not np.all(np.isfinite(gr)) or np.max(np.abs(gr)) > 1e-10:
                    continue
                if length(s, g) > L_MAX + 1e-9:
                    continue
                info = analyse(s, g)
                if info is None or not info["primitive"] or info["collisions_quarter"] > COLL_MAX:
                    continue
                key = (round(info["L"], 8), tuple(info["folded_points"]))
                if info["family"]:
                    key = ("family", round(info["L"], 6))
                found.setdefault(key, info)
    return found


def main():
    t0 = time.time()
    spn = lambda n: 100 * n * n
    run1 = search(20260919, spn)
    run2 = search(20260920, spn)
    keys1, keys2 = set(run1), set(run2)
    allk = {**run1, **run2}
    rows = sorted(allk.values(), key=lambda r: (r["L"], r["n_outer"]))
    here = Path(__file__).resolve().parent
    with open(here / "catalogo_o1.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["indice", "comprimento", "reflexoes_externas", "colisoes_no_quarto", "elemento_g", "familia",
                    "orbita_de_fronteira", "min_autovalor_hessiana", "pontos_dobrados"])
        for i, r in enumerate(rows, 1):
            w.writerow([i, f"{r['L']:.12f}", r["n_outer"], r["collisions_quarter"], r["g"], int(r["family"]),
                        int(r["boundary_orbit"]), f"{r['min_abs_hess_eig']:.3e}",
                        ";".join(f"({x:.7f},{y:.7f})" for x, y in r["folded_points"])])
    meta = {"procedure": "ver docstring", "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "L_max": L_MAX, "collisions_max": COLL_MAX, "n_outer_max": N_MAX, "starts_per_n": "100 n² por g",
            "seeds": [20260919, 20260920], "n_orbits": len(rows),
            "only_seed1": len(keys1 - keys2), "only_seed2": len(keys2 - keys1),
            "csv_sha256": hashlib.sha256((here / "catalogo_o1.csv").read_bytes()).hexdigest(),
            "seconds": round(time.time() - t0, 1), "orbits": rows}
    (here / "catalogo_o1.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    for r in rows:
        print(f"{r['L']:.9f}  n={r['n_outer']} coll={r['collisions_quarter']} g={r['g']:5s} fam={int(r['family'])} "
              f"fronteira={int(r['boundary_orbit'])}")
    print({k: meta[k] for k in ("n_orbits", "only_seed1", "only_seed2", "seconds")})


if __name__ == "__main__":
    main()
