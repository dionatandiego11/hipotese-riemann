"""Transporte exato de médias 3-ádicas das contagens normalizadas de ancestrais.

O kernel com pesos 3/4 e 1/4 é dual da contagem. Não é uma
hipótese probabilística sobre paridades de órbitas inteiras.
"""

from fractions import Fraction
from math import comb


def _check(values, level):
    if level < 0 or len(values) != 3 ** level:
        raise ValueError("Vetor deve ter 3^K entradas, K >= 0.")


def maps(level):
    if level < 0:
        raise ValueError("K deve ser não negativo.")
    modulus = 3 ** level
    inv2 = pow(2, -1, modulus) if modulus > 1 else 0
    return ([(x * inv2) % modulus for x in range(modulus)],
            [((3 * x + 1) * inv2) % modulus for x in range(modulus)])


def push_probabilities(values, level):
    """μ Q: massa movida pelos dois mapas; permite vetores assinados."""
    _check(values, level)
    first, second = maps(level)
    out = [Fraction(0) for _ in values]
    for x, mass in enumerate(values):
        out[first[x]] += Fraction(3, 4) * mass
        out[second[x]] += Fraction(1, 4) * mass
    return out


def pull_observable(values, level):
    """Qf, calculado nas observáveis em vez de nas probabilidades."""
    _check(values, level)
    first, second = maps(level)
    return [Fraction(3, 4) * values[first[x]] + Fraction(1, 4) * values[second[x]]
            for x in range(len(values))]


def averaged_density_step(values, level):
    """E_K A: fórmula em densidades derivada das médias dos ramos inversos."""
    _check(values, level)
    if level == 0:
        return list(values)
    modulus = 3 ** level
    shorter = modulus // 3
    out = []
    for a in range(modulus):
        value = Fraction(3, 4) * values[(2 * a) % modulus]
        if a % 3 == 2:
            base = ((2 * a - 1) // 3) % shorter
            value += Fraction(1, 4) * sum(values[base + j * shorter] for j in range(3))
        out.append(value)
    return out


def project_probabilities(values, from_level, to_level):
    _check(values, from_level)
    if not 0 <= to_level <= from_level:
        raise ValueError("A projeção deve reduzir ou manter o nível.")
    out = [Fraction(0) for _ in range(3 ** to_level)]
    for a, mass in enumerate(values):
        out[a % len(out)] += mass
    return out


def total_variation(first, second):
    if len(first) != len(second):
        raise ValueError("Vetores devem ter mesma dimensão.")
    return sum(abs(a - b) for a, b in zip(first, second)) / 2


def coupling_bound(depth, level):
    """Pr[Binomial(m,1/4)<K] como fração exata."""
    if depth < 0 or level < 0:
        raise ValueError("m e K devem ser não negativos.")
    return sum((Fraction(comb(depth, j) * 3 ** (depth - j), 4 ** depth)
                for j in range(min(level, depth + 1))), Fraction(0))


def stationary_probabilities(level):
    """Eliminação racional da equação πQ=π + massa 1; apenas níveis pequenos."""
    if not 0 <= level <= 3:
        raise ValueError("Esta rotina densa está limitada a K <= 3.")
    size = 3 ** level
    columns = []
    for x in range(size):
        basis = [Fraction(int(a == x)) for a in range(size)]
        columns.append(push_probabilities(basis, level))
    augmented = [[columns[col][row] - int(row == col) for col in range(size)] + [Fraction(0)]
                 for row in range(size)]
    augmented[-1] = [Fraction(1)] * (size + 1)
    for col in range(size):
        pivot = next((row for row in range(col, size) if augmented[row][col]), None)
        if pivot is None:
            raise ArithmeticError("Sistema estacionário singular.")
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        factor = augmented[col][col]
        augmented[col] = [value / factor for value in augmented[col]]
        for row in range(size):
            if row == col:
                continue
            factor = augmented[row][col]
            if factor:
                augmented[row] = [a - factor * b for a, b in zip(augmented[row], augmented[col])]
    result = [row[-1] for row in augmented]
    if sum(result) != 1 or min(result) < 0 or push_probabilities(result, level) != result:
        raise ArithmeticError("Solução não é probabilidade estacionária.")
    return result


def holder_one_seminorm(values, level):
    _check(values, level)
    largest = Fraction(0)
    for a in range(len(values)):
        for b in range(a):
            delta = a - b
            power = 1
            while delta % 3 == 0:
                delta //= 3
                power *= 3
            largest = max(largest, abs(values[a] - values[b]) * power)
    return largest
