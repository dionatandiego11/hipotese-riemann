"""Projeções de custo e lei geométrica: inteiros e frações exatos."""
from fractions import Fraction
from collatz.cost_residues import cost_counts


def projected_generators(level, maximum, resolution):
    """Expande apenas K primeiros ramos; estado final é q_{ℓ−K}."""
    if not 0 <= resolution <= level or maximum < 0:
        raise ValueError('Domínio inválido.')
    previous = [{0: n} if n else {} for n in cost_counts(level-resolution, maximum)]
    for depth in range(1, resolution+1):
        source_level = level-resolution+depth
        modulus = 3**depth
        out = [{} for _ in range(maximum+1)]
        for j in range(min(2*3**(source_level-1),maximum+1)):
            inv=pow(2,-j-1,modulus)
            for k in range(maximum-j+1):
                for b,count in previous[k].items():
                    a=((3*b+1)*inv)%modulus
                    out[k+j][a]=out[k+j].get(a,0)+count
        previous=out
    return previous


def geometric_limit(resolution):
    if resolution < 0:
        raise ValueError('Resolução negativa.')
    values=[Fraction(1)]
    for depth in range(1,resolution+1):
        n=3**depth
        period=2*3**(depth-1)
        out=[Fraction(0)]*n
        for j in range(period):
            weight=Fraction(2**(period-j-1),2**period-1)
            inv=pow(2,-j-1,n)
            for b,mass in enumerate(values):
                out[((3*b+1)*inv)%n]+=weight*mass
        values=out
    return values


def stationary_half(resolution):
    """Eliminação racional independente, limitada a 9 estados."""
    if not 0 <= resolution <= 2:
        raise ValueError('Sistema limitado a K<=2.')
    n=3**resolution
    inv2=pow(2,-1,n) if n>1 else 0
    matrix=[[Fraction(0) for _ in range(n+1)] for _ in range(n)]
    for x in range(n):
        matrix[(x*inv2)%n][x]+=Fraction(1,2)
        matrix[((3*x+1)*inv2)%n][x]+=Fraction(1,2)
        matrix[x][x]-=1
    matrix[-1]=[Fraction(1)]*(n+1)
    for col in range(n):
        row=next(i for i in range(col,n) if matrix[i][col])
        matrix[col],matrix[row]=matrix[row],matrix[col]
        pivot=matrix[col][col]
        matrix[col]=[v/pivot for v in matrix[col]]
        for i in range(n):
            if i!=col:
                multiplier=matrix[i][col]
                matrix[i]=[a-multiplier*b for a,b in zip(matrix[i],matrix[col])]
    return [matrix[i][-1] for i in range(n)]
