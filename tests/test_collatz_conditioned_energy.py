from collections import Counter, defaultdict
from fractions import Fraction

from collatz.conditioned_energy import energy_upper_bound, tilted_translation_moment


def compositions(total, depth):
    if depth == 1:
        yield (total,)
        return
    for first in range(1, total - depth + 2):
        for rest in compositions(total - first, depth - 1):
            yield (first,) + rest


def numerator_and_residue(word):
    # Composição afim cronológica independente da fórmula de coeficientes.
    numerator, previous_total = 0, 0
    for a in word:
        numerator = 3 * numerator + 2**previous_total
        previous_total += a
    modulus = 3**len(word)
    return numerator, numerator * pow(2**previous_total, -1, modulus) % modulus


def test_tilted_moment_against_direct_words():
    count = 0
    for depth in range(1, 6):
        for total in range(depth, 3 * depth + 1):
            direct = Fraction(0)
            for word in compositions(total, depth):
                numerator, _ = numerator_and_residue(word)
                direct += Fraction(3**depth + numerator, 4**total)
            formula = tilted_translation_moment(depth, total)
            assert formula == direct
            assert 0 <= formula <= 2
            count += 1
    print(f"momentos conferidos exatamente: {count}")


def test_conditioned_energy_and_projection_against_enumeration():
    cases = empty = 0
    for depth in range(1, 6):
        modulus = 3**depth
        for total in range(depth, 3 * depth + 1):
            for capped in (False, True):
                counts = Counter()
                quotients = defaultdict(set)
                for word in compositions(total, depth):
                    if capped and any(a > 2 * 3**(depth-i-1) for i, a in enumerate(word)):
                        continue
                    numerator, residue = numerator_and_residue(word)
                    quotient = numerator // modulus
                    assert quotient not in quotients[residue]
                    quotients[residue].add(quotient)
                    counts[residue] += 1
                n = sum(counts.values())
                if not n:
                    empty += 1
                    continue
                beta = Fraction(n, 2**total)
                energy = Fraction(modulus * sum(x*x for x in counts.values()), n*n)
                assert energy <= energy_upper_bound(depth, total, beta) <= 4 / beta**2
                last = Fraction(1)
                for resolution in range(1, depth + 1):
                    projected = Counter()
                    for a, mass in counts.items():
                        projected[a % 3**resolution] += mass
                    current = Fraction(3**resolution * sum(x*x for x in projected.values()), n*n)
                    assert last <= current <= energy
                    last = current
                if total == 2 * depth and not capped:
                    assert beta**2 >= Fraction(1, 16 * depth)
                    assert energy <= 64 * depth
                cases += 1
    print(f"eventos não vazios: {cases}; eventos vazios preservados: {empty}")
