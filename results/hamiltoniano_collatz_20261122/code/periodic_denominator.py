"""Exact rational periodic points and denominator-weighted orbit sums.

T uses (a,b)=(3,1); the binary shift uses (1,-1). State space Z_2,
with real ordering used only for the reported positive-integer filter.
"""
from fractions import Fraction
from itertools import product


def step(x, a=3, b=1):
    x = Fraction(x)
    if x.denominator % 2 == 0:
        raise ValueError("state must be a rational 2-adic integer")
    return (a*x+b)/2 if x.numerator % 2 else x/2


def periodic_points(n, a=3, b=1):
    if n < 1 or a not in (1,3) or (a,b) not in ((3,1),(1,-1)):
        raise ValueError("declared scope: n>=1, T or binary shift")
    for bits in product((0,1), repeat=n):
        A, B = 1, 0
        for j, bit in enumerate(bits):
            if bit:
                A, B = a*A, a*B+b*2**j
        x = Fraction(B, 2**n-A)
        yield bits, x


def weighted_sum(n, a=3, b=1):
    """Product of denom(x)^(-1) along each n-periodic orbit."""
    return sum((Fraction(1,x.denominator**n)
                for _,x in periodic_points(n,a,b)), Fraction(0))
