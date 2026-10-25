"""Políticas finitas de custo inverso e construção uniforme no custo4n.

Classes finitas de resíduos; não presume a conjectura de Collatz.
"""
from collections import Counter
from itertools import product

from .affine_rewrites import word_residue


def base_certificate():
    """Uma palavra cronológica de custo16 por unidade mod81, mais contagens."""
    witnesses, counts = {}, Counter()
    for a,b,c in product(range(1,3),range(1,7),range(1,19)):
        d = 16-a-b-c
        if not 1 <= d <= 54:
            continue
        word = (a,b,c,d)
        residue = word_residue(word)
        witnesses.setdefault(residue,word)
        counts[residue] += 1
    return witnesses,counts


def inverse_policies(maximum_block=4):
    """Bellman exato: custo mínimo até terminar em unidade após r divisões."""
    if not 1 <= maximum_block <= 4:
        raise ValueError("Escopo declarado: blocos1..4")
    tables = [{1:(0,()),2:(0,())}]
    for r in range(1,maximum_block+1):
        modulus = 3**(r+1)
        previous_modulus = 3**r
        table = {}
        for x in range(1,modulus):
            if x % 3 == 0:
                continue
            choices = []
            for e in range(1,4*r+1):
                numerator = 2**e*x-1
                if numerator % 3:
                    continue
                y = numerator//3 % previous_modulus
                if y not in tables[-1]:
                    continue
                cost,path = tables[-1][y]
                choices.append((e+cost,(e,)+path))
            table[x] = min(choices)
            if table[x][0] > 4*r:
                raise ArithmeticError("Limite elementar4r não satisfeito")
        tables.append(table)
    return tables


def construct_four_n(depth,total,residue,certificate):
    """Constrói palavra em qualquer custo4n<=S<=C_n+n-1, n>=4.

    Usa inversão de um ramo com e<=4, o certificado n4 e preenchimento
    do último expoente. Retorna expoentes cronológicos.
    """
    if depth < 4 or not 4*depth <= total <= 2*3**(depth-1)+depth-1:
        raise ValueError("Fora da faixa provada")
    modulus = 3**depth
    residue %= modulus
    if residue % 3 == 0:
        raise ValueError("Resíduo deve ser uma unidade")
    extra = total-4*depth
    if extra:
        rotated = pow(2,extra,modulus)*residue % modulus
        word = construct_four_n(depth,4*depth,rotated,certificate)
        return word[:-1]+(word[-1]+extra,)
    if depth == 4:
        return tuple(certificate[residue])
    for e in range(1,5):
        numerator = 2**e*residue-1
        if numerator % 3:
            continue
        predecessor = numerator//3 % (modulus//3)
        if predecessor % 3:
            prefix = construct_four_n(depth-1,total-e,predecessor,certificate)
            return prefix+(e,)
    raise ArithmeticError("Não foi encontrado ramo unitário com e<=4")
