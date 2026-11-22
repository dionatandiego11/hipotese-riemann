"""Prime-defined smoothed kernel; no zero table is an input.

Positive definiteness and a spectral interpretation use RH and the explicit
formula. Numerical Gram diagnostics are not positivity certificates.
"""
from mpmath import mp


def prime_powers_up_to(bound):
    """Return (prime power, prime) once for each power at most bound."""
    for p in range(2, bound + 1):
        if any(p % d == 0 for d in range(2, int(p ** 0.5) + 1)):
            continue
        n = p
        while n <= bound:
            yield n, p
            n *= p


def trivial_remainder(t):
    """R(exp(t)), t>=0, with its continuous value at zero."""
    t = mp.mpf(t)
    if t < 0:
        raise ValueError("t must be nonnegative")
    if not t:
        return mp.log(2) - 1
    q = mp.exp(-t)
    return mp.log(-mp.expm1(-2*t))/2 + mp.atanh(q)/q - 1


def smoothed_prime_error(t):
    t = mp.mpf(t)
    if t < 0:
        raise ValueError("t must be nonnegative")
    x = mp.exp(t)
    return (mp.fsum(mp.log(p)*(x/n-1)
                    for n, p in prime_powers_up_to(int(mp.floor(x))))
            - x*t + (1+mp.euler)*x)


def prime_kernel(t):
    t = abs(mp.mpf(t))
    if not t:
        return 2 + mp.euler - mp.log(4*mp.pi)
    return mp.exp(-t/2)*(smoothed_prime_error(t)
                         - mp.log(2*mp.pi) - trivial_remainder(t))
