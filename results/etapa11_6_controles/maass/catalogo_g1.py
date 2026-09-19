"""
Catálogo G1 do `ctrl-maass-v1` (DECLARACAO_MAASS.md §4, P3; ADENDO_MAASS_1.md; D1M_DERIVACAO_MAASS.md §§3 e 5).
Aritmética inteira exata; não lê nenhum autovalor de Maass. Classe B (cálculo exato; correção por dois algoritmos).

Para cada (n, δ) — δ = +1: n = 3..13 (hiperbólicas de PSL(2,Z)); δ = −1: n = 1..13 (reflexões com deslizamento,
det = −1) — as classes de conjugação por Γ̂ = PSL(2,Z) correspondem às classes de equivalência PRÓPRIA de todas as
formas binárias (A, B, C) de discriminante D = n² − 4δ (bijeção M ↦ (c, d − a, −b); D1-M §5).

  Algoritmo (a): ciclos de formas reduzidas de Gauss (0 < B < √D, √D − B < 2|A| < √D + B) sob o operador de redução
                 ρ(A, B, C) = (C, B′, (B′² − D)/(4C)), B′ ≡ −B (mod 2C), √D − 2|C| < B′ < √D.
  Algoritmo (b): componentes conexas do grafo de todas as formas de discriminante D numa caixa |A|, |B|, |C| ≤ K,
                 com arestas dos geradores S: (A,B,C) → (C,−B,A) e T: (A,B,C) → (A, B+2A, A+B+C); K dobra até as
                 contagens estabilizarem (e no mínimo 4D).
  As duas contagens precisam coincidir para cada D; senão o programa para.

Raiz primitiva: para a classe com forma Q e (n, δ), procura (n₀, δ₀, k) com k ≥ 2 (δ₀ = +1 para δ = +1; δ₀ = −1 e k
ímpar para δ = −1), Q = U_{k−1}(n₀, δ₀)·Q₀ e disc(Q₀) = n₀² − 4δ₀, e CONFERE multiplicando matrizes que
M(Q₀, n₀)^k = ±M(Q, n). Coeficientes (ADENDO_MAASS_1 §2):
  δ = +1: c = + l_p / (4π sinh(l/2)),   l = 2 arccosh(n/2), l_p = l/k;
  δ = −1: c = − l_ρ / (2π cosh(l/2)),   l = 2 arcsinh(n/2), l_ρ = l/k (k ímpar).

Uso (da raiz):  .venv/bin/python3 results/etapa11_6_controles/maass/catalogo_g1.py
"""
import csv
import hashlib
import json
import math
from math import isqrt
from pathlib import Path

N_MAX = 13


def disc(Q):
    A, B, C = Q
    return B * B - 4 * A * C


def content(Q):
    return math.gcd(math.gcd(abs(Q[0]), abs(Q[1])), abs(Q[2]))


# ------------------------------------------------------------------ (a) formas reduzidas e ciclos

def reduced_forms(D):
    r = math.sqrt(D)
    out = []
    for B in range(1, isqrt(D) + 1):
        if (B - D) % 2 or B >= r:
            continue
        num = B * B - D                         # = 4AC < 0
        for A in range(-isqrt(D) - 1, isqrt(D) + 2):
            if A == 0 or num % (4 * A):
                continue
            if r - B < 2 * abs(A) < r + B:
                out.append((A, B, num // (4 * A)))
    return out


def rho(Q, D):
    A, B, C = Q
    r = math.sqrt(D)
    m = 2 * abs(C)
    # B′ ≡ −B (mod 2C), no intervalo (√D − 2|C|, √D)
    Bp = (-B) % m
    lo = r - m
    k = math.floor((r - Bp) / m)
    Bp = Bp + k * m
    if Bp >= r:
        Bp -= m
    while Bp <= lo:
        Bp += m
    assert lo < Bp < r
    return (C, Bp, (Bp * Bp - D) // (4 * C))


def cycles(D):
    red = reduced_forms(D)
    seen, cyc = set(), []
    for Q in red:
        if Q in seen:
            continue
        c, x = [], Q
        while x not in c:
            c.append(x)
            x = rho(x, D)
        assert x == Q, "ρ não é permutação nas reduzidas"
        seen.update(c)
        cyc.append(c)
    assert seen == set(red)
    return cyc


# ------------------------------------------------------------------ (b) componentes por S e T numa caixa

def components(D, K):
    forms = []
    for B in range(-K, K + 1):
        if (B - D) % 2:
            continue
        num = B * B - D
        for A in range(-K, K + 1):
            if A == 0 or num % (4 * A):
                continue
            C = num // (4 * A)
            if abs(C) <= K:
                forms.append((A, B, C))
    idx = {q: i for i, q in enumerate(forms)}
    parent = list(range(len(forms)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i, j):
        a, b = find(i), find(j)
        if a != b:
            parent[a] = b

    for q, i in idx.items():
        A, B, C = q
        for nb in ((C, -B, A), (A, B + 2 * A, A + B + C), (A, B - 2 * A, A - B + C)):
            j = idx.get(nb)
            if j is not None:
                union(i, j)
    return idx, find


def count_by_components(D):
    red = reduced_forms(D)
    K = max(4 * D, 16)
    prev = None
    while True:
        idx, find = components(D, K)
        comp_of_red = {q: find(idx[q]) for q in red}
        n_comp = len(set(comp_of_red.values()))
        if prev is not None and n_comp == prev:
            return n_comp, comp_of_red, K
        prev, K = n_comp, 2 * K


# ------------------------------------------------------------------ matrizes, potências e coeficientes

def matrix_of(Q, n):
    A, B, C = Q
    assert (n - B) % 2 == 0
    return ((n - B) // 2, -C, A, (n + B) // 2)        # (a, b, c, d)


def mat_mul(X, Y):
    a, b, c, d = X
    e, f, g, h = Y
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def mat_pow(X, k):
    R = (1, 0, 0, 1)
    for _ in range(k):
        R = mat_mul(R, X)
    return R


def cheb_U(k, n0, d0):
    """U_k com U_0 = 1, U_1 = n0, U_{j+1} = n0 U_j − d0 U_{j−1} (M^{k+1} = U_k M − d0 U_{k−1} I)."""
    u_prev, u = 1, n0
    if k == 0:
        return 1
    for _ in range(k - 1):
        u_prev, u = u, n0 * u - d0 * u_prev
    return u


def primitive_root(Q, n, delta, class_of):
    """Maior k com M(Q, n) = ±M₀^k; devolve (k, n₀, forma reduzida da raiz) — k = 1 se primitiva."""
    M = matrix_of(Q, n)
    f = content(Q)
    best = (1, n, None)
    for k in range(2, 12):
        if delta == -1 and k % 2 == 0:
            continue
        d0 = delta if delta == -1 else 1
        for n0 in range(1, n + 1):
            U = cheb_U(k - 1, n0, d0)
            if U == 0 or f % abs(U):
                continue
            Q0 = tuple(x // U for x in Q)
            if disc(Q0) != n0 * n0 - 4 * d0:
                continue
            M0 = matrix_of(Q0, n0) if (n0 - Q0[1]) % 2 == 0 else None
            if M0 is None:
                continue
            P = mat_pow(M0, k)
            if P == M or P == tuple(-x for x in M):
                if k > best[0]:
                    best = (k, n0, Q0)
    return best


def coefficient(n, delta, k):
    if delta == 1:
        l = 2 * math.acosh(n / 2)
        return l, (l / k) / (4 * math.pi * math.sinh(l / 2))
    l = 2 * math.asinh(n / 2)
    return l, -(l / k) / (2 * math.pi * math.cosh(l / 2))


def main():
    here = Path(__file__).resolve().parent
    rows, lines, checks = [], [], []
    for delta, n_range in ((-1, range(1, N_MAX + 1)), (1, range(3, N_MAX + 1))):
        for n in n_range:
            D = n * n - 4 * delta
            cyc = cycles(D)
            n_comp, comp_of_red, K = count_by_components(D)
            # (a) e (b) devem coincidir, e cada ciclo deve estar numa única componente
            same = n_comp == len(cyc) and all(len({comp_of_red[q] for q in c}) == 1 for c in cyc) \
                and len({comp_of_red[c[0]] for c in cyc}) == len(cyc)
            checks.append({"n": n, "delta": delta, "D": D, "cycles": len(cyc), "components": n_comp, "K_final": K,
                           "agree": same})
            if not same:
                raise SystemExit(f"algoritmos discordam em D = {D}")
            c_line = 0.0
            for c in cyc:
                Q = min(c)
                k, n0, Q0 = primitive_root(Q, n, delta, None)
                l, cc = coefficient(n, delta, k)
                rows.append({"delta": delta, "n": n, "D": D, "length": l, "form_rep": Q, "content": content(Q),
                             "cycle_len": len(c), "power_k": k, "root_trace": n0, "root_form": Q0,
                             "coefficient": cc})
                c_line += cc
            lines.append({"delta": delta, "n": n, "length": 2 * (math.acosh(n / 2) if delta == 1 else math.asinh(n / 2)),
                          "n_classes": len(cyc), "coefficient_line": c_line})
    lines.sort(key=lambda r: r["length"])
    with open(here / "catalogo_g1_classes.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["delta", "traco", "discriminante", "comprimento", "forma_representante", "conteudo", "potencia_k",
                    "traco_raiz", "forma_raiz", "coeficiente"])
        for r in rows:
            w.writerow([r["delta"], r["n"], r["D"], f"{r['length']:.12f}", "(%d,%d,%d)" % r["form_rep"], r["content"],
                        r["power_k"], r["root_trace"], "" if r["root_form"] is None else "(%d,%d,%d)" % r["root_form"],
                        f"{r['coefficient']:.12f}"])
    with open(here / "catalogo_g1_linhas.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["comprimento", "delta", "traco", "n_classes", "coeficiente_da_linha"])
        for r in lines:
            w.writerow([f"{r['length']:.12f}", r["delta"], r["n"], r["n_classes"], f"{r['coefficient_line']:.12f}"])
    meta = {"script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "N_MAX": N_MAX,
            "algorithm_checks": checks,
            "classes_csv_sha256": hashlib.sha256((here / "catalogo_g1_classes.csv").read_bytes()).hexdigest(),
            "lines_csv_sha256": hashlib.sha256((here / "catalogo_g1_linhas.csv").read_bytes()).hexdigest()}
    (here / "catalogo_g1.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    for r in lines:
        print(f"l={r['length']:.6f}  δ={r['delta']:+d} n={r['n']:2d}  classes={r['n_classes']:2d}  c={r['coefficient_line']:+.6f}")
    print("algoritmos concordam em todos os D:", all(c["agree"] for c in checks))


if __name__ == "__main__":
    main()
