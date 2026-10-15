import mpmath as mp
import pytest
from riemann_spectra.negative_moments_ratios import (arithmetic_diagonal,
                                                   diagonal_laurent,
                                                   prime_divisors,two_zero_model)


def test_laurent_coefficients_against_independent_extrapolation():
    with mp.workdps(75):
        h=mp.mpf('1e-12')
        for q in (1,4,5,8,12):
            for kind in (7,8):
                residue,finite=diagonal_laurent(q,kind)
                d1=arithmetic_diagonal(h,q,kind)
                d2=arithmetic_diagonal(2*h,q,kind)
                residue_extrap=2*h*d1-2*h*d2
                finite_extrap=2*(d1-residue/h)-(d2-residue/(2*h))
                assert abs(residue_extrap-residue)<mp.mpf('1e-20')
                assert abs(finite_extrap-finite)<mp.mpf('1e-20')


def test_prime_power_invariance_and_distinct_principal_character_factors():
    with mp.workdps(40):
        assert diagonal_laurent(4,7)==diagonal_laurent(8,7)
        assert diagonal_laurent(4,8)==diagonal_laurent(8,8)
        assert mp.almosteq(diagonal_laurent(12,7)[0],3/mp.pi**2)
        assert diagonal_laurent(12,8)[0]==mp.mpf(1)/3
        assert prime_divisors(12)==(2,3)


def test_two_zero_model_against_integral_and_gap_scaling():
    with mp.workdps(35):
        e=mp.mpf('0.1')
        f=lambda t:1/((e*e+t*t)*(e*e+(t-1)**2))
        h=lambda t:(e*e+(t-mp.mpf('0.5'))**2)*f(t)
        points=[-mp.inf,0,e,mp.mpf('0.5'),1-e,1,1+e,mp.inf]
        model=two_zero_model(1,e)
        assert abs(e/mp.pi*mp.quad(f,points)-model['reciprocal'])<mp.mpf('1e-25')
        assert abs(e/mp.pi*mp.quad(h,points)-model['weighted'])<mp.mpf('1e-25')
        close=two_zero_model('0.01','0.001')
        assert mp.almosteq(close['reciprocal']/close['reciprocal_target'],
                           model['reciprocal']/model['reciprocal_target'])
        assert mp.almosteq(close['weighted'],model['weighted'])


def test_invalid_parameters():
    for q in (0,-1,1.5,True):
        with pytest.raises(ValueError):prime_divisors(q)
    with pytest.raises(ValueError):arithmetic_diagonal(0,1,7)
    with pytest.raises(ValueError):diagonal_laurent(1,9)
    with pytest.raises(ValueError):two_zero_model(0,1)
