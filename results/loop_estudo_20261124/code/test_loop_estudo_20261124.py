from fractions import Fraction
from mpmath import mp
from collatz.height_transfer import (
    weil_height, height_weight, preimages, height_transfer, rational_states_by_height
)
from collatz.periodic_denominator import step


def test_weil_height_and_northcott_finiteness():
    assert weil_height(Fraction(3, 5)) == 5
    assert weil_height(Fraction(-7, 3)) == 7
    assert weil_height(Fraction(10, 1)) == 10
    assert weil_height(Fraction(0, 1)) == 1

    states_b5 = rational_states_by_height(5)
    assert len(states_b5) > 0
    for s in states_b5:
        assert weil_height(s) <= 5
        assert s.denominator % 2 == 1  # 2-adic integer


def test_height_weight_decay_on_integers_vs_denominator():
    """Contrast with denominator weight which is identically 1 on integers."""
    for k in range(1, 10):
        # On integers, Weil height H(k) = k
        assert height_weight(k, alpha=1) == Fraction(1, k)
        assert height_weight(k, alpha=2) == Fraction(1, k**2)


def test_height_transfer_consistency():
    for y in (0, 2, 5, -1, Fraction(1, 5), Fraction(2, 7)):
        even, odd = preimages(y)
        assert step(even) == y and step(odd) == y
        vec = {even: Fraction(1), odd: Fraction(1)}
        res = height_transfer(vec, alpha=1)
        expected = height_weight(even, 1) + height_weight(odd, 1)
        assert res.get(Fraction(y), 0) == expected


def test_bbm_eigenfunction_logarithmic_divergence():
    """Verify that BBM Hurwitz zeta eigenfunction tail grows as (x+1)/|z-1|^2, causing quadratic L^2 divergence."""
    with mp.workdps(50):
        gamma_1 = mp.mpf('14.13472514173469379045725198356247027078425711569924')
        z = mp.mpc('0.5', gamma_1)
        # By Euler-Maclaurin expansion of Hurwitz zeta for Re(z) = 1/2:
        # zeta(z, x+1) ~ (x+1)^(1-z) / (z-1) = (x+1)^(1/2 - i gamma) / (-1/2 + i gamma)
        # Therefore |zeta(z, x+1)|^2 ~ (x+1) / |z-1|^2.
        # This causes int_0^X |psi|^2 dx ~ X^2 / (2|z-1|^2) -> infty (quadratic divergence!).
        inv_denom = 1 / abs(z - 1)**2
        for x_val in (1000, 10000, 100000):
            psi = mp.hurwitz(z, x_val + 1)
            density = abs(psi)**2
            expected_density = (x_val + 1) * inv_denom
            relative_error = abs(density - expected_density) / expected_density
            assert relative_error < mp.mpf('0.01')


def test_sierra_rodriguez_laguna_exact_solution():
    """Verify exact analytic solution of Sierra-Rodriguez-Laguna ODE H psi = E psi."""
    with mp.workdps(60):
        lp = mp.mpf('1.5')
        E = mp.mpf('14.134725')

        def f(p):
            return p + lp**2 / p

        def f_prime(p):
            return 1 - lp**2 / p**2

        def psi(p):
            return (1 / mp.sqrt(f(p))) * (p**2 + lp**2)**(-mp.mpc(0, E / 2))

        # Check ODE: i [ f(p) psi'(p) + 0.5 f'(p) psi(p) ] - E psi(p) == 0
        for p_val in (mp.mpf('0.5'), mp.mpf('1.0'), mp.mpf('2.5'), mp.mpf('10.0')):
            psi_val = psi(p_val)
            dpsi = mp.diff(psi, p_val)
            H_psi = mp.mpc(0, 1) * (f(p_val) * dpsi + mp.mpf('0.5') * f_prime(p_val) * psi_val)
            residual = abs(H_psi - E * psi_val) / abs(psi_val)
            assert residual < mp.mpf('1e-45')
