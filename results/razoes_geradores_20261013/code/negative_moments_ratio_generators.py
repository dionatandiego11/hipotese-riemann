"""Geradores diagonais formais, distintos de médias demonstradas de L."""
from __future__ import annotations
import mpmath as mp
from .negative_moments_ratios import arithmetic_diagonal


def _domain(u,v,a,b):
    u,v,a,b=map(mp.convert,(u,v,a,b))
    if any(mp.re(x) <= 0 for x in (u+b,v+b,a+b)):
        raise ValueError('É necessário Re(u+b), Re(v+b), Re(a+b)>0.')
    return u,v,a,b


def prime_generator(p,u,v,a,b,kind):
    """Fator local para p∤q, após média na fase do primo."""
    if not isinstance(p,int) or isinstance(p,bool) or p < 2:
        raise ValueError('p inteiro≥2; primalidade é hipótese do chamador.')
    u,v,a,b=_domain(u,v,a,b)
    U,V,A=(mp.power(p,-1-x-b) for x in (u,v,a))
    if kind==7:
        return 1-U+V+A
    if kind==8:
        return (1+V)/((1+U)*(1-A))
    raise ValueError('kind em {7,8}.')


def prime_correction7(p,u,v,a,b):
    """Fator A7, após retirar os polos universais do produto G7."""
    u,v,a,b=_domain(u,v,a,b)
    U,V,A=(mp.power(p,-1-x-b) for x in (u,v,a))
    return (1-V)*(1-A)/(1-U)*prime_generator(p,u,v,a,b,7)


def arithmetic_generator8(u,v,a,b,q):
    """G8=D8(a+b)D7(v+b)/D7(u+b); fórmula da diagonal, não média de L."""
    u,v,a,b=_domain(u,v,a,b)
    return (arithmetic_diagonal(a+b,q,8)*arithmetic_diagonal(v+b,q,7)
            /arithmetic_diagonal(u+b,q,7))
