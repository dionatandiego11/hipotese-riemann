"""Fatores diagonais de razões discretas; médias completas permanecem conjecturais."""
from __future__ import annotations
import mpmath as mp
from .arithmetic import sieve_primes
from .negative_moments_ratios import prime_divisors


def log_weight_factor(epsilon, nu, q, kind, cutoff=20000):
    """P7/P8 e majorante analítica da cauda de P7 (aritmética não certificada).

    ν=0 representa o limite formal da derivada logarítmica deslocada.
    Não avalia médias de L nem afirma uniformidade dos erros da receita.
    """
    e,v=mp.mpf(epsilon),mp.mpf(nu)
    bad=prime_divisors(q)
    if e <= 0 or v < 0 or kind not in (7,8):
        raise ValueError('ε>0, ν≥0, kind em {7,8}.')
    s=1+v+e
    if kind == 8:
        value=-mp.diff(mp.zeta,s)/mp.zeta(s)+2*mp.diff(mp.zeta,2*s)/mp.zeta(2*s)
        value-=sum((mp.log(p)/(mp.power(p,s)+1) for p in bad),mp.mpf(0))
        return value,mp.mpf(0)
    if not isinstance(cutoff,int) or isinstance(cutoff,bool) or cutoff < 2:
        raise ValueError('cutoff inteiro≥2.')
    u=1+2*e
    correction=mp.mpf(0)
    for p in sieve_primes(cutoff):
        x=mp.power(p,-s); y=mp.power(p,-u)
        correction+=mp.log(p)*x*(x+y)/((1-x)*(1+y))
    value=-mp.diff(mp.zeta,s)/mp.zeta(s)-correction
    value-=sum((mp.log(p)*mp.power(p,-s)/(1+mp.power(p,-u)) for p in bad),mp.mpf(0))
    tail=4*(mp.log(cutoff)+1)/cutoff
    # The truncated subtraction overestimates the exact P7 by 0≤error≤tail.
    return value,tail


def cue_palm_ratio(size, radius):
    """E_U(size) |Λ(1)/Λ(r)|² = 1+size(1-r)/(1+r)."""
    r=mp.mpf(radius)
    if not isinstance(size,int) or isinstance(size,bool) or size < 0 or not 0 < r < 1:
        raise ValueError('size inteiro≥0 e 0<r<1.')
    return 1+size*(1-r)/(1+r)


def cue_shifted_discrete(size, epsilon):
    """(1-r)² E Σ_j |Λ(r z_j)|^(−2), r=e^(−ε), N=size≥1."""
    if not isinstance(size,int) or isinstance(size,bool) or size < 1:
        raise ValueError('size inteiro≥1.')
    e=mp.mpf(epsilon)
    if e <= 0:
        raise ValueError('ε>0.')
    return cue_palm_ratio(size-1,mp.exp(-e))
