import mpmath as mp

from riemann_spectra.negative_moments_rare_pairs import (
    gap_density, inverse_pair_tail, scaled_defect_integral, shifted_pair_weight,
)
from riemann_spectra.negative_moments_discrete_ratios import cue_shifted_discrete


def test_mean_against_gap_quadrature_and_existing_cue_formula():
    with mp.workdps(50):
        assert abs(mp.quad(gap_density, [-mp.pi, 0, mp.pi]) - 1) < mp.mpf("1e-35")
        for e in map(mp.mpf, ("0.04", "0.01", "0.0025")):
            mean = 2 * mp.quad(lambda p: shifted_pair_weight(p, e) * gap_density(p),
                               [0, e, mp.sqrt(e), mp.pi])
            assert abs(mean - cue_shifted_discrete(2, e)) < mp.mpf("1e-35")


def test_inner_and_outer_against_weighted_integrals():
    with mp.workdps(50):
        for e in map(mp.mpf, ("0.04", "0.01", "0.0025")):
            d = mp.sqrt(e)
            # Construção pelos pesos originais, sem usar a fórmula de integral.
            integrand = lambda p: (shifted_pair_weight(p, e) * gap_density(p)
                                   - mp.exp(e) / (2 * mp.pi)) / e
            inner = 2 * mp.quad(integrand, [0, e, d])
            outer = 2 * mp.quad(integrand, [d, mp.pi])
            assert abs(inner - scaled_defect_integral(e, d)) < mp.mpf("1e-35")
            assert abs(inner + outer - scaled_defect_integral(e, mp.pi)) < mp.mpf("1e-35")
            assert abs(inner + mp.mpf("0.5")) <= 2 * e + mp.sqrt(e) / mp.pi
            assert abs(outer) <= mp.sqrt(e)


def test_tail_constant_and_gap_mass():
    with mp.workdps(50):
        constant = mp.sqrt(2) / (3 * mp.pi)
        for x in map(mp.mpf, ("1e4", "1e6")):
            angle = 2 * mp.asin(1 / mp.sqrt(2 * x))
            integral = 2 * mp.quad(gap_density, [0, angle])
            assert abs(integral - inverse_pair_tail(x)) < mp.mpf("1e-35")
            assert abs(integral * x ** mp.mpf("1.5") / constant - 1) < mp.mpf("1e-3")
