"""Identidades finitas de colisão para a estacionária Syracuse, em Fraction."""
from __future__ import annotations

from fractions import Fraction


def collision_decomposition(current, previous):
    """Retorna DD/DO/OD/OO e H na resolução K>=1.

    current e previous são massas em todos os resíduos módulo 3^K e 3^(K-1).
    A função não presume que a lei de um custo condicionado seja estacionária.
    """
    n = len(current)
    if n != 3 * len(previous) or n < 3 or n % 3:
        raise ValueError("Resoluções consecutivas incompatíveis")
    p = tuple(Fraction(x) for x in current)
    q = tuple(Fraction(x) for x in previous)
    inv2 = pow(2, -1, n)
    d = [Fraction(0)] * n
    o = [Fraction(0)] * n
    for x, mass in enumerate(p):
        d[x * inv2 % n] += mass / 2
        o[(3 * x + 1) * inv2 % n] += mass / 2
    h = sum((p[(3 * b + 1) % n] * mass for b, mass in enumerate(q)), Fraction(0))
    return {
        "D": d,
        "O": o,
        "DD": sum((x * x for x in d), Fraction(0)),
        "DO": sum((x * y for x, y in zip(d, o)), Fraction(0)),
        "OD": sum((x * y for x, y in zip(o, d)), Fraction(0)),
        "OO": sum((x * x for x in o), Fraction(0)),
        "H": h,
        "collision": sum((x * x for x in p), Fraction(0)),
        "energy": n * sum((x * x for x in p), Fraction(0)),
    }
