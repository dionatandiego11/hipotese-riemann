"""Contagem de grupos da família H, preservando custo e resíduo grosso.

Cada grupo tem três palavras, uma em cada filho; as contagens abaixo são
de grupos, não de palavras. Precisão inicial3 dígitos, depois um por ramo.
"""
from collections import Counter


def family_group_counts(depth, maximum_total):
    """Retorna Z_n(S,a), com a módulo3^(n-1), para n=depth>=4."""
    if depth < 4 or maximum_total < 0:
        raise ValueError("Profundidade>=4 e custo não negativo necessários")
    previous = [Counter() for _ in range(maximum_total+1)]
    for first in (1, 2):
        for extra in range(46):
            total = first+11+extra
            if total <= maximum_total:
                residue = 19 * pow(2, -(11+extra), 27) % 27
                previous[total][residue] += 1
    for n in range(5, depth+1):
        modulus, cap = 3**(n-1), 2*3**(n-1)
        out = [Counter() for _ in range(maximum_total+1)]
        inverses = {a:pow(2,-a,modulus) for a in range(1,min(cap,maximum_total)+1)}
        for total, counts in enumerate(previous):
            if not counts:
                continue
            for exponent in range(1,min(cap,maximum_total-total)+1):
                inv = inverses[exponent]
                for residue, multiplicity in counts.items():
                    out[total+exponent][(3*residue+1)*inv % modulus] += multiplicity
        previous = out
    return previous
