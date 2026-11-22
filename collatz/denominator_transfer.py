"""Weighted transfer on rational 2-adic integers with counting measure.

Finite-support actions of a bounded, noncompact operator; not a Fredholm
determinant approximation or a quotient of the 2-adic dynamics.
"""
from fractions import Fraction
from .periodic_denominator import step


def weight(x, s=1):
    x = Fraction(x)
    if x.denominator % 2 == 0 or not isinstance(s, int) or s < 0:
        raise ValueError("rational 2-adic state and nonnegative integer s required")
    return Fraction(1,x.denominator**s)


def preimages(y):
    y = Fraction(y)
    if y.denominator % 2 == 0:
        raise ValueError("state must be a rational 2-adic integer")
    return (2*y,(2*y-1)/3)


def transfer(vector, s=1):
    out = {}
    for x, coefficient in vector.items():
        x = Fraction(x)
        y = step(x)
        out[y] = out.get(y,Fraction(0))+weight(x,s)*coefficient
    return {x:c for x,c in out.items() if c}


def adjoint_basis(y, s=1):
    return {x:weight(x,s) for x in preimages(y)}


def inner_product(left, right):
    """Real rational vectors only, sufficient for exact witnesses."""
    return sum((c*right.get(x,0) for x,c in left.items()),Fraction(0))
