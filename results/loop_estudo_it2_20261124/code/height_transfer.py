"""Transfer operator with Weil height decay on rational 2-adic integers.

Unlike denominator-only weights, the Weil height H(x) = max(|p|, |q|) decays on both
large denominators and large numerators (integers), satisfying Northcott's finiteness
property on bounded height subsets.
"""
from fractions import Fraction
from .periodic_denominator import step


def weil_height(x):
    """Return max(|numerator|, denominator) for irreducible Fraction x."""
    x = Fraction(x)
    return max(abs(x.numerator), x.denominator)


def height_weight(x, alpha=1):
    """Aritmetic weight decaying as H(x)^(-alpha), alpha >= 0 integer."""
    x = Fraction(x)
    if x.denominator % 2 == 0 or not isinstance(alpha, (int, float)) or alpha < 0:
        raise ValueError("rational 2-adic state and nonnegative alpha required")
    h = weil_height(x)
    return Fraction(1, h**alpha) if isinstance(alpha, int) else (1.0 / (float(h)**alpha))


def preimages(y):
    """The two preimage branches under T(x)."""
    y = Fraction(y)
    if y.denominator % 2 == 0:
        raise ValueError("state must be a rational 2-adic integer (odd denominator)")
    return (2 * y, (2 * y - 1) / 3)


def height_transfer(vector, alpha=1):
    """Apply transfer operator L_alpha to finite-support vector."""
    out = {}
    for x, coefficient in vector.items():
        x = Fraction(x)
        y = step(x)
        w = height_weight(x, alpha)
        out[y] = out.get(y, Fraction(0)) + w * coefficient
    return {x: c for x, c in out.items() if c}


def rational_states_by_height(bound):
    """Return sorted tuple of rational 2-adic states with Weil height <= bound."""
    states = set()
    for q in range(1, bound + 1, 2):  # odd denominator
        for p in range(-bound, bound + 1):
            if max(abs(p), q) <= bound:
                states.add(Fraction(p, q))
    return tuple(sorted(states))
