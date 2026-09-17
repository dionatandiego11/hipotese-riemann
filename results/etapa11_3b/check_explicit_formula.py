"""
11.3b / L-EF1: checagem de consistência (classe B) da forma de referência (ETAPA11_PLANO §3.1)
    Σ_ρ h(γ_ρ) = h(i/2) + h(−i/2) − g(0) log π + (1/2π)∫ h(r) Re ψ(1/4 + ir/2) dr − 2 Σ_n Λ(n) n^{−1/2} g(log n),
    g(u) = (1/2π)∫ h(r) e^{−iru} dr,   h(r) = exp(−(r/T)²) cos(a r).

Revisão 11.3b-2: acrescenta um ORÇAMENTO DE ERRO (estimado, não certificado):
  E_ord   propagação do erro das ordenadas: Σ_{n≤n_used} 2|h'(γ_n)| · 3e-9 (precisão declarada da tabela);
  E_z1    cauda de zeros dentro da tabela: Σ_{n_used<n≤100000} 2|h(γ_n)| (soma explícita, tabela já consultada);
  E_z2    cauda além da tabela (γ > 74920,8): cota via N(T) ≤ T² para T ≥ 7·10⁴ (hipótese de contagem explícita;
          citação de uma cota explícita de S(T) pendente), avaliada em log10;
  E_p     cauda de primos n > n_max: cota elementar Λ(n) ≤ log n e integral ∫_{log n_max}^∞ u e^{u/2} |g(u)| du
          (termos decrescentes nessa faixa, verificado);
  E_quad  diferença entre duas quadraturas (tanh-sinh e Gauss-Legendre) do termo arquimediano;
e verifica a completude dos primeiros zeros por mpmath.nzeros (classe B).
Zeros de data/processed/zeros_100k.csv (SHA-256 1af728cf…; os primeiros 1.000 coincidem com zeros_10k.csv).
Σ_ρ h(γ_ρ) = 2 Σ_{γ>0} h(γ) supõe criticidade e simplicidade desses zeros (verificação externa; citação PC).
Não é experimento do protocolo.
"""
import csv, json, math
import mpmath as mp

mp.mp.dps = 30
ZEROS = "data/processed/zeros_100k.csv"
ORD_ERR = mp.mpf("3e-9")

def load_zeros():
    return [mp.mpf(r[1]) for r in list(csv.reader(open(ZEROS)))[1:]]

def von_mangoldt_terms(xmax):
    sieve = bytearray([1]) * (xmax + 1); sieve[0:2] = b"\x00\x00"
    for i in range(2, int(xmax ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    out = []
    for p in range(2, xmax + 1):
        if sieve[p]:
            pk = p
            while pk <= xmax:
                out.append((pk, math.log(p))); pk *= p
    return out

def case(T, a, n_used, n_max, Z):
    T = mp.mpf(T); a = mp.mpf(a)
    h = lambda r: mp.e ** (-(r / T) ** 2) * mp.cos(a * r)
    dh = lambda r: mp.e ** (-(r / T) ** 2) * (-2 * r / T ** 2 * mp.cos(a * r) - a * mp.sin(a * r))
    g0 = lambda u: T / (2 * mp.sqrt(mp.pi)) * mp.e ** (-(T * u) ** 2 / 4)
    g = lambda u: (g0(u - a) + g0(u + a)) / 2
    zeros = Z[:n_used]
    lhs = 2 * mp.fsum(h(z) for z in zeros)
    poles = mp.re(h(mp.mpc(0, 0.5)) + h(mp.mpc(0, -0.5)))
    f_arch = lambda r: h(r) * mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * r / 2))
    pts = [-mp.inf, -50, 0, 50, mp.inf]
    arch_ts = mp.quad(f_arch, pts, method="tanh-sinh") / (2 * mp.pi)
    arch_gl = mp.quad(f_arch, pts, method="gauss-legendre") / (2 * mp.pi)
    logpi = -g(0) * mp.log(mp.pi)
    primes = -2 * mp.fsum(mp.mpf(L) / mp.sqrt(n) * g(mp.log(n)) for n, L in von_mangoldt_terms(n_max))
    rhs = poles + logpi + arch_ts + primes
    diff = lhs - rhs
    # orçamento
    E_ord = 2 * ORD_ERR * mp.fsum(abs(dh(z)) for z in zeros)
    E_z1 = 2 * mp.fsum(abs(h(z)) for z in Z[n_used:])
    X = Z[-1]
    # Σ_{γ>X} e^{-(γ/T)²} ≤ Σ_{k≥0} N(X+k+1) e^{-((X+k)/T)²} ≤ Σ_k (X+k+1)² e^{-((X+k)/T)²}; em log10 (termo k=0 domina)
    log10_E_z2 = float((2 * mp.log(X + 1) - (X / T) ** 2 + mp.log(2)) / mp.log(10))
    gmax = lambda u: T / (2 * mp.sqrt(mp.pi)) * mp.e ** (-(T * (u - a)) ** 2 / 4)  # |g(u)| ≤ gmax(u) para u ≥ a
    U0 = mp.log(n_max)
    integrand = lambda u: u * mp.e ** (u / 2) * gmax(u)
    # decrescimento de log x · x^{-1/2} gmax(log x) para x ≥ n_max (derivada em u de u e^{-u/2} ... com o fator gaussiano)
    decreasing = bool(mp.diff(lambda u: mp.log(u) - u / 2 - (T * (u - a)) ** 2 / 4, U0) < 0)
    E_p = 2 * mp.quad(integrand, [U0, U0 + 10, mp.inf])
    E_quad = abs(arch_ts - arch_gl)
    budget = E_ord + E_z1 + E_quad + E_p + mp.mpf(10) ** max(log10_E_z2, -300)
    return {"T": float(T), "a": float(a), "n_used": n_used, "gamma_last_used": float(zeros[-1]), "n_max_prime": n_max,
            "lhs": float(lhs), "rhs": float(rhs), "diff": float(diff),
            "terms": {"poles": float(poles), "logpi": float(logpi), "arch": float(arch_ts), "primes": float(primes)},
            "budget": {"E_ord": float(E_ord), "E_z1_tabela": float(E_z1), "log10_E_z2_alem_tabela": log10_E_z2,
                       "E_primos_cauda": float(E_p), "cauda_primos_termos_decrescentes": decreasing, "E_quad": float(E_quad),
                       "total_estimado": float(budget)},
            "diff_dentro_do_orcamento": bool(abs(diff) <= budget),
            "diff_if_prime_coef_1_instead_of_2": float(diff + primes / 2),
            "diff_if_logpi_sign_flipped": float(diff + 2 * logpi)}

if __name__ == "__main__":
    Z = load_zeros()
    compl = {"nzeros(gamma_1000+1e-6)": int(mp.nzeros(Z[999] + mp.mpf("1e-6"))),
             "nzeros(gamma_1000-1e-6)": int(mp.nzeros(Z[999] - mp.mpf("1e-6")))}
    print(json.dumps({"completude_primeiros_1000": compl}))
    cases = [(5, 0.0, 400, 5000), (5, math.log(2), 400, 5000), (5, math.log(3), 400, 5000), (8, 1.0, 400, 5000), (40, 0.0, 1000, 100)]
    res = [case(*c, Z=Z) for c in cases]
    for r in res:
        print(json.dumps(r))
    json.dump({"completude_primeiros_1000": compl, "casos": res}, open("results/etapa11_3b/check_explicit_formula.json", "w"), indent=2)
