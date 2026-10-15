"""Caracteres aditivos exatos em Z[ζ_{3^K}], apenas para grades pequenas."""
from functools import lru_cache


def reduce_polynomial(coefficients, resolution):
    """Redução por Φ_{3^K}=x^{2m}+x^m+1; K=0 é avaliação em 1."""
    if resolution < 0:
        raise ValueError('Resolução negativa.')
    if resolution == 0:
        return (sum(coefficients),)
    n, m = 3 ** resolution, 3 ** (resolution - 1)
    values = [0] * n
    for i, value in enumerate(coefficients):
        values[i % n] += value
    for i in range(m):
        top = values[2*m+i]
        values[i] -= top
        values[m+i] -= top
    return tuple(values[:2*m])


def character_from_counts(counts, resolution, frequency):
    n = 3 ** resolution
    values = [0] * n
    for root, count in counts.items():
        values[(frequency * root) % n] += count
    return reduce_polynomial(values, resolution)


@lru_cache(maxsize=None)
def character_sum(level, cost, resolution, frequency):
    """H=Σ_a g(level,cost,a)exp(2πih a/3^K), não normalizado."""
    if level < 0 or not 0 <= resolution <= level:
        raise ValueError('É necessário 0 <= K <= level.')
    if cost < 0:
        return (0,) * (1 if resolution == 0 else 2*3**(resolution-1))
    if resolution == 0:
        from collatz.cost_residues import cost_counts
        return (cost_counts(level, cost)[cost],)
    n = 3 ** resolution
    h = frequency % n
    out = [0] * n
    for j in range(min(2 * 3 ** (level-1), cost+1)):
        inv = pow(2, -(j+1), n)
        source = character_sum(level-1, cost-j, resolution-1,
                               (h*inv) % (n//3))
        # ζ_{3^(K−1)} = ζ_{3^K}^3; fase do termo constante do levantamento.
        for exponent, value in enumerate(source):
            out[(h*inv + 3*exponent) % n] += value
    return reduce_polynomial(out, resolution)


def haar_character(resolution, frequency):
    """Transformada da probabilidade uniforme nas unidades, como Fraction."""
    from fractions import Fraction
    if resolution < 1:
        raise ValueError('Haar nas unidades exige K>=1.')
    n = 3 ** resolution
    h = frequency % n
    if h == 0:
        return Fraction(1)
    if h % (n//3) == 0:
        return Fraction(-1, 2)
    return Fraction(0)
