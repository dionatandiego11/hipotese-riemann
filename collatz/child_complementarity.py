"""Decomposição positiva dos três filhos, conservando os estados de custo."""
from itertools import combinations


def exponent_state(depth,parent,exponent):
    """Estado bruto c, pai b e deslocamento k de um expoente final."""
    if depth < 2 or not 0 <= parent < 3**(depth-1) or exponent < 1:
        raise ValueError("Estado fora do domínio")
    numerator = 2**exponent * parent-1
    if numerator % 3:
        raise ValueError("Expoente não admissível para o pai")
    modulus = 3**(depth-2)
    c = numerator//3
    return c,c % modulus,(c//modulus) % 3


def predecessor_parts(depth,total,parent,previous_by_extra):
    """Parcelas do vetor no nível depth; previous usa custo extra do nível anterior.

    previous_by_extra é o formato de generator_counts(depth-1,...).
    Parcelas de contagem zero são preservadas, não renormalizadas.
    """
    if depth < 2 or not 0 < parent < 3**(depth-1) or parent % 3 == 0:
        raise ValueError("Pai deve ser uma unidade no nível indicado")
    modulus = 3**(depth-2)
    maximum = min(2*3**(depth-1),total-(depth-1))
    parts = []
    for exponent in range(1,maximum+1):
        if (2**exponent*parent-1) % 3:
            continue
        _,b,k = exponent_state(depth,parent,exponent)
        previous_total = total-exponent
        index = previous_total-(depth-1)
        if not 0 <= index < len(previous_by_extra):
            raise ValueError("Tabela anterior não cobre todos os custos necessários")
        counts = previous_by_extra[index]
        vector = tuple(counts[b+modulus*((k+2**exponent*j) % 3)] for j in range(3))
        mask = sum(1 << j for j in range(3) if vector[j])
        parts.append(dict(e=exponent,S_pre=previous_total,b=b,k=k,vector=vector,mask=mask))
    return parts


def minimum_cover(parts):
    """Menor conjunto de expoentes cobrindo os3 filhos; None se incompleto.

    Empates: ordem lexicográfica dos expoentes. Nenhuma hipótese de
    independência, aleatoriedade ou suficiência universal de duas parcelas.
    """
    masks = {}
    for part in sorted(parts,key=lambda p:p["e"]):
        if part["mask"]:
            masks.setdefault(part["mask"],part["e"])
    candidates = sorted((e,mask) for mask,e in masks.items())
    for size in (1,2,3):
        for chosen in combinations(candidates,size):
            union = 0
            for _,mask in chosen:
                union |= mask
            if union == 7:
                return tuple(e for e,_ in chosen)
    return None
