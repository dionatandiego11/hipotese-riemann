import mpmath as mp
from riemann_spectra.negative_moments_finite_part import (
    local_quotient_coefficients, finite_part_bias, richardson_two_scale,
    single_pole_window,
)
from riemann_spectra.negative_moments_ratios import two_zero_model


def test_laurent_coefficient_by_independent_limit():
    with mp.workdps(60):
        root=mp.mpc('0.5',2)
        f=lambda s:(s-root)*(s-mp.mpc('0.5',4))
        h=lambda s:mp.exp(mp.mpf('0.7')*(s-root))
        a,b=local_quotient_coefficients(f,h,root)
        assert abs(a-1/(-2j)) < mp.mpf('1e-55')
        # Difference quotients recover the regular Laurent coefficient.
        for shift in map(mp.mpf,['1e-10','1e-15']):
            estimate=(h(root+shift)/f(root+shift)-a/shift)
            assert abs(estimate-b) < 10*shift


def test_single_pole_quadrature_bias_and_symmetrization():
    with mp.workdps(60):
        for k in map(mp.mpf,['0','0.7']):
            for e in map(mp.mpf,['0.02','0.01','0.005']):
                for side in (-1,1):
                    integral=e/mp.pi*mp.quad(
                        lambda t:abs(mp.exp(k*(side*e+1j*(t-2)))/
                                     (side*e+1j*(t-2)))**2,[1,2,3])
                    closed=single_pole_window(e,1,1,k,side)
                    assert abs(integral/closed-1) < mp.mpf('1e-40')
                    expected=finite_part_bias(-2,[(mp.mpf(1),k)],side)
                    assert abs((closed-1)/e-expected) < 20*e
                symmetric=sum(single_pole_window(e,1,1,k,side)
                              for side in (-1,1))/2
                assert abs((symmetric-1)/e+2/mp.pi) < 20*e
                extrapolated=richardson_two_scale(single_pole_window(e/2,1,1,k),
                                                 single_pole_window(e,1,1,k))
                assert abs(extrapolated-1) < 20*e**2


def test_two_pole_finite_part_with_separate_subtractions():
    with mp.workdps(60):
        roots=[mp.mpc('0.5',1),mp.mpc('0.5',3)]
        f=lambda s:(s-roots[0])*(s-roots[1])
        coefficients=[local_quotient_coefficients(f,lambda s:mp.mpf(1),r)
                      for r in roots]
        # Partial fractions on [0,4] give this FP integral exactly.
        fp=-mp.mpf(2)/3+mp.log(3)/2
        for cutoff in map(mp.mpf,['0.01','0.005']):
            density=lambda t:1/((t-1)**2*(t-3)**2)
            punctured=mp.quad(density,[0,1-cutoff])+mp.quad(density,[1+cutoff,3-cutoff])+mp.quad(density,[3+cutoff,4])
            subtracted=punctured-1/cutoff
            assert abs(subtracted-fp) < 10*cutoff
        bias=finite_part_bias(fp,coefficients)
        previous=mp.inf
        for e in map(mp.mpf,['0.01','0.005','0.0025']):
            value=e/mp.pi*mp.quad(lambda t:abs(1/f(mp.mpf('0.5')+e+1j*t))**2,
                                 [0,1,2,3,4])
            error=abs((value-mp.mpf('0.5'))/e-bias)
            assert error < 20*e
            assert error < previous
            previous=error


def test_extrapolation_does_not_remove_close_pair_scale():
    with mp.workdps(60):
        for d in map(mp.mpf,['1','0.01']):
            for x in map(mp.mpf,['0.1','0.01']):
                e=x*d
                full=two_zero_model(d,e)['reciprocal']
                half=two_zero_model(d,e/2)['reciprocal']
                target=2/d**2
                relative=richardson_two_scale(half,full)/target
                exact=2/(1+x*x)-1/(1+4*x*x)
                assert abs(relative-exact) < mp.mpf('1e-55')
                assert relative > 1  # The extrapolation is not a universal lower bound.
