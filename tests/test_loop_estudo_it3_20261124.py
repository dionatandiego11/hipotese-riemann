from mpmath import mp
from collatz.wirsching_mellin import (
    collatz_scale_product, smooth_background_P0, fourier_coefficient_zeta, LOG3, LOG2
)


def test_scale_product_functional_equation():
    """Verify that P(s) - P(3s) = log(1 - exp(-2s)) to extreme precision."""
    with mp.workdps(40):
        for s_val in ('0.05', '0.01', '0.001', '0.0001'):
            s = mp.mpf(s_val)
            actual_diff = collatz_scale_product(s) - collatz_scale_product(3 * s)
            expected_diff = mp.log(1 - mp.exp(-2 * s))
            assert abs(actual_diff - expected_diff) < mp.mpf('1e-35')


def test_smooth_background_difference_identity():
    """Verify P0(s) - P0(3s) = log(s) + log(2)."""
    with mp.workdps(40):
        for s_val in ('1e-5', '1e-8', '1e-12'):
            s = mp.mpf(s_val)
            actual_diff = smooth_background_P0(s) - smooth_background_P0(3 * s)
            expected_diff = mp.log(s) + mp.log(2)
            assert abs(actual_diff - expected_diff) < mp.mpf('1e-35')


def test_riemann_zeta_fourier_coefficients():
    """Verify closed-form Fourier coefficients c_n and their super-exponential decay."""
    with mp.workdps(40):
        c1 = fourier_coefficient_zeta(1)
        c2 = fourier_coefficient_zeta(2)
        c3 = fourier_coefficient_zeta(3)

        # Expected magnitude of c1 ~ 1.0468623e-4
        assert abs(abs(c1) - mp.mpf('0.000104686232582')) < mp.mpf('1e-14')

        # Super-exponential decay factor exp(-pi^2 / log 3) ~ 1.25e-4
        decay_12 = abs(c2) / abs(c1)
        assert abs(decay_12 - mp.mpf('0.0001268535')) < mp.mpf('1e-8')

        decay_23 = abs(c3) / abs(c2)
        assert abs(decay_23 - mp.mpf('0.00014449')) < mp.mpf('1e-7')


def test_collatz_oscillation_matches_riemann_zeta():
    """Verify that numerical oscillation in Collatz product matches Riemann zeta c1 to 8+ digits."""
    with mp.workdps(40):
        s_base = mp.mpf('1e-10')
        K_steps = 100
        u_vals = [mp.mpf(k) / K_steps for k in range(K_steps)]
        s_vals = [s_base * (3 ** u) for u in u_vals]
        rem_vals = [collatz_scale_product(s) - smooth_background_P0(s) for s in s_vals]

        c1_num = sum(rem * mp.exp(-2 * mp.pi * mp.mpc(0, 1) * u)
                     for rem, u in zip(rem_vals, u_vals)) / K_steps

        tau_1 = 2 * mp.pi / mp.log(3)
        c1_theo = fourier_coefficient_zeta(1) * (s_base ** mp.mpc(0, tau_1))

        rel_error = abs(c1_num - c1_theo) / abs(c1_theo)
        assert rel_error < mp.mpf('1e-6')
