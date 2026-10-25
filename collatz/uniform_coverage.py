"""Cobertura uniforme derivada de certificado finito e política de quatro ramos."""
from .inverse_cost_policy import construct_four_n


def coverage_bound(depth):
    if depth < 4:
        raise ValueError("A prova começa em profundidade4")
    base = 4+(depth-4) % 4
    return 3*depth+base


def construct_coverage(depth,total,residue,certificate,policy_four):
    """Constrói expoentes cronológicos para L(n)<=S<=C_n+n-1.

    policy_four precisa ser o certificado exato de custo<=12 em unidades
    mod243; a identidade desse certificado é conferida pelo runner.
    """
    lower = coverage_bound(depth)
    if not lower <= total <= 2*3**(depth-1)+depth-1:
        raise ValueError("Custo fora do intervalo provado")
    modulus = 3**depth
    residue %= modulus
    if residue % 3 == 0:
        raise ValueError("Classe deve ser uma unidade")
    extra = total-lower
    if extra:
        rotated = pow(2,extra,modulus)*residue % modulus
        word = construct_coverage(depth,lower,rotated,certificate,policy_four)
        return word[:-1]+(word[-1]+extra,)
    if depth <= 7:
        return construct_four_n(depth,total,residue,certificate)
    cost,path = policy_four[residue % 243]
    if len(path) != 4 or sum(path) != cost or cost > 12:
        raise ValueError("Política não satisfaz o certificado requerido")
    current = residue
    for i,e in enumerate(path):
        numerator = 2**e*current-1
        if numerator % 3:
            raise ArithmeticError("Ramo não integral")
        current = numerator//3 % (3**(depth-i-1))
        if current % 3 == 0:
            raise ArithmeticError("Ramo saiu das unidades")
    prefix = construct_coverage(depth-4,total-cost,current,certificate,policy_four)
    return prefix+tuple(reversed(path))
