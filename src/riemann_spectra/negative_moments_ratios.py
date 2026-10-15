"""Diagonais aritméticas e regularização local; não uma previsão completa de razões.

Precisão controlada pelo contexto mpmath do chamador. Nenhuma leitura de zeros.
"""
from __future__ import annotations
import mpmath as mp


def prime_divisors(q: int) -> tuple[int, ...]:
    if isinstance(q, bool) or not isinstance(q, int) or q < 1:
        raise ValueError('q deve ser inteiro positivo.')
    out, n, p = [], q, 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return tuple(out)


def arithmetic_diagonal(alpha, q: int, kind: int):
    """D7(α)=L(1+α,χ0)/L(2+2α,χ0); D8(α)=L(1+α,χ0)."""
    primes=prime_divisors(q)
    a=mp.convert(alpha)
    if mp.re(a) <= 0 or kind not in (7,8):
        raise ValueError('É necessário Re α>0 e kind em {7,8}.')
    numerator=mp.zeta(1+a)
    for p in primes:
        numerator*=1-mp.power(p,-1-a)
    if kind == 8:
        return numerator
    denominator=mp.zeta(2+2*a)
    for p in primes:
        denominator*=1-mp.power(p,-2-2*a)
    return numerator/denominator


def diagonal_laurent(q: int, kind: int):
    """Retorna resíduo e parte finita de D_kind no ponto α=0."""
    primes=prime_divisors(q)
    if kind not in (7,8):
        raise ValueError('kind deve ser 7 ou 8.')
    if kind == 7:
        residue=1/mp.zeta(2)
        for p in primes:
            residue*=mp.mpf(p)/(p+1)
        finite=residue*(mp.euler-2*mp.diff(mp.zeta,2)/mp.zeta(2)
                         +sum((mp.log(p)/(p+1) for p in primes),mp.mpf(0)))
    else:
        residue=mp.mpf(1)
        for p in primes:
            residue*=mp.mpf(p-1)/p
        finite=residue*(mp.euler+sum((mp.log(p)/(p-1) for p in primes),mp.mpf(0)))
    return residue,finite


def two_zero_model(gap, epsilon):
    """Integrais escaladas em toda a reta para F com dois zeros simples artificiais."""
    d,e=mp.mpf(gap),mp.mpf(epsilon)
    if d <= 0 or e <= 0:
        raise ValueError('Separação e deslocamento devem ser positivos.')
    denominator=d*d+4*e*e
    return {'reciprocal':2/denominator,
            'weighted':(d*d+8*e*e)/(2*denominator),
            'reciprocal_target':2/(d*d),
            'weighted_target':mp.mpf(1)/2}


def principal_square_boundary(q: int, central_value):
    """Polo de borda de C8 se χ² é principal e L(1/2,χ)=central_value !=0.

    A hipótese sobre χ² é do chamador, não inferida de q. Não avalia L.
    """
    value=mp.convert(central_value)
    if not mp.isfinite(value) or value == 0:
        raise ValueError('Valor central deve ser finito e não nulo.')
    residue=mp.mpf(1)
    for p in prime_divisors(q):
        residue*=mp.mpf(p-1)/p
    return residue**2/(8*abs(value)**2)
