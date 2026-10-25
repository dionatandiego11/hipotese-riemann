"""Momentos exatos auxiliares da cota de energia com custo total fixado.

Não modela órbitas positivas. As leis geométricas são as da lei aleatória
de Syracuse; ver teorias/SYRACUSE_ENERGIA_CONDICIONADA_20261019.md.
"""
from fractions import Fraction
from math import comb


def total_mass(depth: int, total: int, *, tilted: bool = False) -> Fraction:
    """Massa de soma=total para depth geometrias positivas.

    Lei usual: P(a)=2**(-a). Inclinada: P(a)=3*4**(-a).
    """
    if depth < 1:
        raise ValueError("depth deve ser positivo")
    if total < depth:
        return Fraction(0)
    if tilted:
        return Fraction(comb(total - 1, depth - 1) * 3**depth, 4**total)
    return Fraction(comb(total - 1, depth - 1), 2**total)


def tilted_translation_moment(depth: int, total: int) -> Fraction:
    """H=E_inclinada[(1+Y) 1_{soma=total}], por identidade geradora."""
    b = total_mass(depth, total, tilted=True)
    f = total_mass(depth, total)
    difference_cdf = sum(
        (total_mass(depth, s, tilted=True) - total_mass(depth, s)
         for s in range(depth, total + 1)), Fraction(0)
    )
    return (3 * b - f + difference_cdf) / 2


def energy_upper_bound(depth: int, total: int, event_probability) -> Fraction:
    """Cota para qualquer subconjunto do evento soma=total, massa beta>0.

    A validade requer que a probabilidade fornecida seja a do evento sob
    a lei usual; a função não verifica a identidade do evento.
    """
    beta = Fraction(event_probability)
    if not 0 < beta <= total_mass(depth, total):
        raise ValueError("massa incompatível com um subconjunto do custo fixado")
    return 2 * tilted_translation_moment(depth, total) / beta**2
