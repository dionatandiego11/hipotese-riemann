import mpmath as mp
import pytest
from riemann_spectra.negative_moments_ratio_generators import (
    prime_generator,prime_correction7,arithmetic_generator8,
)
from riemann_spectra.negative_moments_ratios import arithmetic_diagonal
from riemann_spectra.negative_moments_discrete_ratios import log_weight_factor


def test_local_generators_by_independent_phase_integration():
    with mp.workdps(50):
        u,v,a,b=map(mp.mpf,['0.03','0.04','0.06','0.07'])
        for p in (2,5):
            for phase in map(mp.mpf,['0','0.7']):
                for kind in (7,8):
                    def integrand(theta):
                        z=mp.exp(1j*(theta+phase))
                        ratio=(1-mp.power(p,-mp.mpf('0.5')-v)*z)/(1-mp.power(p,-mp.mpf('0.5')-u)*z)
                        A=mp.power(p,-mp.mpf('0.5')-a)*z
                        B=mp.power(p,-mp.mpf('0.5')-b)/z
                        return ratio*((1-A)*(1-B) if kind==7 else 1/((1+A)*(1+B)))
                    actual=mp.quad(integrand,[-mp.pi,0,mp.pi])/(2*mp.pi)
                    assert abs(actual/prime_generator(p,u,v,a,b,kind)-1) < mp.mpf('1e-35')


def test_matched_generator_and_arithmetic_correction():
    with mp.workdps(50):
        v,a,b=map(mp.mpf,['0.04','0.06','0.07'])
        for q in (1,4,5,12):
            assert abs(arithmetic_generator8(v,v,a,b,q)/arithmetic_diagonal(a+b,q,8)-1) < mp.mpf('1e-40')
        for p in (2,5):
            assert abs(prime_correction7(p,v,v,a,b)-(1-mp.power(p,-2-2*a-2*b))) < mp.mpf('1e-40')


def test_generator_derivative_by_cauchy_contour():
    with mp.workdps(50):
        a=b=mp.mpf('0.1');v=mp.mpf('0.02');radius=mp.mpf('0.05')
        integrand=lambda t:arithmetic_generator8(v+radius*mp.exp(1j*t),v,a,b,5)*mp.exp(-1j*t)/radius
        derivative=mp.quad(integrand,[0,mp.pi,2*mp.pi])/(2*mp.pi)
        factor,_=log_weight_factor(a,v,5,8)
        expected=arithmetic_diagonal(2*a,5,8)*factor
        assert abs(derivative/expected-1) < mp.mpf('1e-35')


def test_generator_rejects_domain_outside_positive_denominator_shifts():
    with pytest.raises(ValueError):
        arithmetic_generator8(-1,mp.mpf('0.02'),mp.mpf('0.1'),mp.mpf('0.1'),5)
    with pytest.raises(ValueError):
        prime_generator(2,mp.mpf('0.1'),mp.mpf('0.1'),mp.mpf('0.1'),mp.mpf('0.1'),99)
