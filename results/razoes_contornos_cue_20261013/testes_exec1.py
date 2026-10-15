import mpmath as mp
import pytest
from riemann_spectra.negative_moments_contours import (
    polynomial_control, cue_regularized_mean,
)


def test_displaced_residues_have_opposite_limits():
    with mp.workdps(50):
        for heights in [(1,), (1,2), (1,2,4)]:
            roots=[mp.mpc('0.5',t) for t in heights]
            for h in [None,lambda s:s+2]:
                previous=mp.inf
                for d in map(mp.mpf,['0.02','0.002','0.0002']):
                    _,rows=polynomial_control(roots,d,h)
                    error=max(max(abs(x['original']/x['target']-1),
                                  abs(x['shifted']/x['target']+1)) for x in rows)
                    assert error < 20*d
                    assert error < previous
                    previous=error


def test_circle_contour_isolates_original_pole():
    with mp.workdps(50):
        d=mp.mpf('0.02'); root=mp.mpc('0.5',1)
        f,rows=polynomial_control([root,mp.mpc('0.5',2)],d,lambda s:s+2)
        rad=d/3
        integral=mp.quad(lambda angle:f(root+rad*mp.exp(1j*angle))*
                         1j*rad*mp.exp(1j*angle),[0,mp.pi,2*mp.pi])
        assert abs((d*integral/(2j*mp.pi))/rows[0]['original']-1) < mp.mpf('1e-35')


def test_cue_one_eigenangle_by_direct_quadrature():
    with mp.workdps(50):
        for e in map(mp.mpf,['0.1','0.3']):
            r=mp.exp(-e)
            integral=mp.quad(lambda theta:1/abs(1-r*mp.exp(1j*theta))**2,
                             [-mp.pi,0,mp.pi])
            assert abs((e*integral/mp.pi)/cue_regularized_mean(e)-1) < mp.mpf('1e-35')


def test_cue_finite_shift_bias_series():
    with mp.workdps(50):
        for e in map(mp.mpf,['0.01','0.02']):
            series=1+e+e**2/3-e**4/45
            assert abs(cue_regularized_mean(e)-series) < e**6


def test_control_rejects_invalid_hypotheses():
    with pytest.raises(ValueError):
        polynomial_control([mp.mpc('0.5',1)]*2,mp.mpf('0.01'))
    with pytest.raises(ValueError):
        polynomial_control([mp.mpc('0.6',1)],mp.mpf('0.01'))
    with pytest.raises(ValueError):
        cue_regularized_mean(0)
