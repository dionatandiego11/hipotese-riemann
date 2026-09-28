"""Etapa A: confere numericamente as médias locais (fase uniforme θ) e os produtos de Euler do modelo HKO/CFKRS."""
import math, numpy as np
th = np.linspace(0, 2*math.pi, 200001)[:-1]
def media(f): return float(np.mean(f(th)))
print("== médias locais, p ∤ q (χ(p) = ±1), x = χ(p) p^{-1/2} e^{-iθ}")
for p in (2, 3, 5, 7):
    for c in (1, -1):
        x = lambda t: c * p**-0.5 * np.exp(-1j*t)
        m7 = media(lambda t: np.abs(1 - x(t))**2)                      # |L_p(ρ)|^{-2}
        m8 = media(lambda t: np.abs(1 - x(t))**2 / np.abs(1 - x(t)**2)**2)  # |L_p(2ρ,χ²)|²|L_p(ρ)|^{-2}
        assert abs(m7 - (1 + 1/p)) < 1e-12 and abs(m8 - 1/(1 - 1/p)) < 1e-9, (p, c, m7, m8)
    print(f"p={p}: C7 local (1+1/p) ok; C8 local 1/(1-1/p) ok; com (1-1/p): C7 -> {1-p**-2:.6f}, C8 -> 1")
def primes(n):
    s = np.ones(n+1, bool); s[:2] = False
    for i in range(2, int(n**.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]
P = primes(2_000_000)
for q, divs in ((1, []), (4, [2]), (5, [5]), (8, [2]), (12, [2, 3])):
    c7 = np.prod([(1 - 1/p) * (1 if p in divs else 1 + 1/p) for p in P[:2000]]) * np.prod(1 - 1.0/P[2000:]**2)
    c8 = np.prod([(1 - 1/p) * (1 if p in divs else 1/(1 - 1/p)) for p in P[:2000]])
    Aq = 6/math.pi**2 * math.prod(p/(p+1) for p in divs); phi = math.prod(1 - 1/p for p in divs)
    print(f"q={q:2d}: modelo C7 = {c7:.6f}  A_q = {Aq:.6f} | modelo C8 = {c8:.6f}  φ(q)/q = {phi:.6f}")
    assert abs(c7 - Aq) < 1e-6 and abs(c8 - phi) < 1e-12
# alternativa HE: descartar (1-1/p) também em p|q
for q, divs in ((4, [2]), (5, [5]), (8, [2]), (12, [2, 3])):
    he = 6/math.pi**2 * math.prod(p*p/(p*p - 1) for p in divs)
    print(f"q={q}: HE (sem o fator (1-1/p) em p|q) = {he:.6f} = A_q × {he/(6/math.pi**2*math.prod(p/(p+1) for p in divs)):.4f}")
print("tudo confere")
