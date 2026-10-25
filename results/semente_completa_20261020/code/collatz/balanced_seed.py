"""Parcela equilibrada máxima da semente cronológica de quatro expoentes.

O catálogo mantém custo do prefixo e sufixo fixos em cada grupo. Não
afirma maximalidade entre reescritas globais com troca de custo.
"""
from collections import Counter, defaultdict
from itertools import product

from .affine_rewrites import word_residue


def complete_four_seed():
    """Contagens finas, grupos por pai e catálogo de triplas disjuntas."""
    fine = [Counter() for _ in range(81)]
    fibers = defaultdict(lambda: defaultdict(list))
    for word in product(range(1,3),range(1,7),range(1,19),range(1,55)):
        total = sum(word)
        residue = word_residue(word)
        fine[total][residue] += 1
        parent = residue % 27
        child = residue // 27
        fibers[total,parent][child].append(word)
    balanced = [Counter() for _ in range(81)]
    catalogue = []
    for (total,parent),children in sorted(fibers.items()):
        capacity = min(len(children[j]) for j in range(3))
        if capacity:
            balanced[total][parent] = capacity
            ordered = [sorted(children[j]) for j in range(3)]
            for k in range(capacity):
                catalogue.append(dict(total=total,parent=parent,words=[ordered[j][k] for j in range(3)]))
    return fine,balanced,catalogue


def transport_group_seed(seed,depth,maximum_total):
    """Transporta uma semente de grupos de nível4 na resolução n-1."""
    if depth < 4 or maximum_total < 0:
        raise ValueError("Profundidade>=4 e custo não negativo necessários")
    previous = [Counter(seed[s]) if s < len(seed) else Counter()
                for s in range(maximum_total+1)]
    for n in range(5,depth+1):
        modulus,cap = 3**(n-1),2*3**(n-1)
        inverses = {a:pow(2,-a,modulus) for a in range(1,min(cap,maximum_total)+1)}
        out = [Counter() for _ in range(maximum_total+1)]
        for total,counts in enumerate(previous):
            if not counts:
                continue
            for exponent in range(1,min(cap,maximum_total-total)+1):
                inv = inverses[exponent]
                for residue,multiplicity in counts.items():
                    out[total+exponent][(3*residue+1)*inv % modulus] += multiplicity
        previous = out
    return previous
