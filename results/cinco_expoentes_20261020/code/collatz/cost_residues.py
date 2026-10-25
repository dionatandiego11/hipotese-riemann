"""Geradores de Wirsching: custo condicionado e resíduos, aritmética exata."""
from collections import Counter
from fractions import Fraction


def cost_counts(level, maximum):
    """Coeficientes de Q_level, limitados ao grau maximum (sem grade residual)."""
    if level < 0 or maximum < 0:
        raise ValueError('Níveis e custos devem ser não negativos.')
    values = [1] + [0] * maximum
    for i in range(1, level + 1):
        cap = 2 * 3 ** (i - 1)
        out, running = [], 0
        for k in range(maximum + 1):
            running += values[k]
            if k >= cap:
                running -= values[k - cap]
            out.append(running)
        values = out
    return values


def generator_counts(level, maximum):
    """Levantamento a=(3b+1)2^{−j−1} mod 3^level; contagens inteiras."""
    if level < 0 or maximum < 0:
        raise ValueError('Níveis e custos devem ser não negativos.')
    previous = [Counter({0: 1})] + [Counter() for _ in range(maximum)]
    for i in range(1, level + 1):
        modulus, cap = 3 ** i, 2 * 3 ** (i - 1)
        out = [Counter() for _ in range(maximum + 1)]
        for j in range(min(cap, maximum + 1)):
            inv = pow(2, -(j + 1), modulus)
            for cost in range(maximum - j + 1):
                for b, count in previous[cost].items():
                    out[cost + j][((3 * b + 1) * inv) % modulus] += count
        previous = out
    return previous


def tuple_oracle(level, cost):
    """Outra construção: compõe blocos afins em ordem da raiz à folha."""
    if level < 0 or cost < 0:
        raise ValueError('Níveis e custos devem ser não negativos.')
    answer = Counter()
    modulus = 3 ** level
    def visit(step, remaining, used, offset):
        if step == level:
            if remaining == 0:
                root = (offset * pow(2, -(used + level), modulus)) % modulus if level else 0
                answer[root] += 1
            return
        cap = 2 * 3 ** (level - step - 1)
        for j in range(min(cap - 1, remaining) + 1):
            visit(step + 1, remaining - j, used + j,
                  2 ** (j + 1) * offset + 3 ** step)
    visit(0, cost, 0, 0)
    return answer


def conditional_weights(level, cost):
    if level < 1 or cost < 0:
        raise ValueError('É necessário level >= 1 e cost >= 0.')
    denominator = cost_counts(level, cost)[cost]
    if not denominator:
        raise ValueError('Custo fora do suporte.')
    previous = cost_counts(level - 1, cost)
    return [Fraction(previous[cost-j], denominator)
            for j in range(min(2 * 3 ** (level-1), cost+1))]


def tail_bound(level, cost, cutoff):
    """Cota provada na nota para level>=16, 0<=cost<=2level."""
    if level < 16 or not 0 <= cost <= 2 * level or cutoff < 0:
        raise ValueError('Fora do domínio da proposição.')
    return min(Fraction(1), 5 * Fraction(4, 5) ** cutoff)


def project_counts(counts, resolution):
    if resolution < 0:
        raise ValueError('Resolução negativa.')
    result = Counter()
    for root, count in counts.items():
        result[root % (3 ** resolution)] += count
    return result
