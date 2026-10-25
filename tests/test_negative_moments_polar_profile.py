import mpmath as mp
from riemann_spectra.negative_moments_polar_profile import polar_shape,single_pole_scaled_mean
from riemann_spectra.negative_moments_ratio_generators import arithmetic_generator8
from riemann_spectra.negative_moments_ratios import diagonal_laurent


def test_single_pole_profile_against_direct_quadrature():
    with mp.workdps(50):
        zs=[mp.mpf(0),mp.mpf('0.5'),mp.mpc(0,'0.5'),mp.mpf('-0.5'),mp.mpc(0,'-0.5')]
        for lam in map(mp.mpf,['0.25','0.4']):
            for e in map(mp.mpf,['0.04','0.02','0.01']):
                v=lam*e
                for z in zs:
                    u=v+e*z
                    integrand=lambda x:(u+1j*x)/(v+1j*x)/(e*e+x*x)
                    direct=e*mp.quad(integrand,[-1,0,1])
                    closed=single_pole_scaled_mean(e,lam,z)
                    assert abs(direct/closed-1) < mp.mpf('1e-35')
                    assert abs(closed-mp.pi*polar_shape(z,lam)) < 20*e


def test_two_pole_profile_depends_on_actual_moment_weight():
    with mp.workdps(50):
        half=mp.mpf('0.5');lam=mp.mpf('0.25')
        roots=[mp.mpc(half,1),mp.mpc(half,3)]
        f=lambda s:(s-roots[0])*(s-roots[1])
        # Each derivative has modulus2, giving S=1/2 independently.
        S=mp.mpf('0.5')
        for z in [mp.mpf(0),mp.mpf('0.5'),mp.mpc(0,'0.5')]:
            previous=mp.inf
            for e in map(mp.mpf,['0.02','0.01']):
                v=lam*e;u=v+e*z
                def integrand(t):
                    s=half+1j*t
                    return f(s+u)/f(s+v)/abs(f(s+e))**2
                actual=e*mp.quad(integrand,[0,1,2,3,4])
                error=abs(actual-mp.pi*S*polar_shape(z,lam))
                assert error < 30*e
                assert error < previous
                previous=error


def test_arithmetic_generator_polar_profile():
    with mp.workdps(50):
        lam=mp.mpf('0.25')
        for q in (4,5):
            k,_=diagonal_laurent(q,8)
            for z in [mp.mpf('0.5'),mp.mpc(0,'0.5')]:
                for e in map(mp.mpf,['0.001','0.0001']):
                    v=lam*e;u=v+e*z
                    actual=e*arithmetic_generator8(u,v,e,e,q)
                    expected=k/2*polar_shape(z,lam)
                    assert abs(actual/expected-1) < mp.mpf('0.02')
