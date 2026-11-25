"""Mellin transform and Riemann zeta bridge for the Collatz invariant density.

Computes the log-Laplace generating product P(s) = sum_{i=0}^infty log(1 - exp(-2 * 3^i * s)),
its smooth background P0(s), and its exact Fourier coefficients c_n expressed via
the Riemann zeta function zeta(1 - 2 pi i n / log 3) and the Gamma function.
"""
from mpmath import mp

LOG3 = mp.log(3)
LOG2 = mp.log(2)


def collatz_scale_product(s, max_terms=80):
    """Compute P(s) = sum_{i=0}^infty log(1 - exp(-2 * 3^i * s))."""
    s = mp.mpf(s)
    if s <= 0:
        raise ValueError("s must be strictly positive")
    total = mp.mpf(0)
    for i in range(max_terms):
        val = 1 - mp.exp(-2 * (3**i) * s)
        if val <= 0:
            break
        total += mp.log(val)
    return total


def smooth_background_P0(s):
    """Leading-order smooth background P0(s) satisfying P0(s) - P0(3s) = log(s) + log(2)."""
    s = mp.mpf(s)
    log_s = mp.log(s)
    log3 = mp.log(3)
    log2 = mp.log(2)
    return - (log_s**2) / (2 * log3) + (mp.mpf('0.5') - log2 / log3) * log_s


def fourier_coefficient_zeta(n):
    """Exact Fourier coefficient c_n of the log-periodic oscillation from Riemann zeta.

    Derived via Mellin inversion of the scale-invariant sum with poles at w = -2 pi i n / log 3:
    c_n = - (2^(i tau_n) / log 3) * Gamma(-i tau_n) * zeta(1 - i tau_n)
        = (2^(i tau_n) / (2 pi i n)) * Gamma(1 - i tau_n) * zeta(1 - i tau_n)
    where tau_n = 2 pi n / log 3.
    """
    if not isinstance(n, int) or n == 0:
        raise ValueError("n must be a non-zero integer")
    log3 = mp.log(3)
    tau_n = 2 * mp.pi * n / log3
    s_n = mp.mpc(1, -tau_n)
    gamma_factor = mp.gamma(mp.mpc(0, -tau_n))
    zeta_factor = mp.zeta(s_n)
    phase_2 = mp.power(2, mp.mpc(0, tau_n))
    return - (phase_2 / log3) * gamma_factor * zeta_factor
