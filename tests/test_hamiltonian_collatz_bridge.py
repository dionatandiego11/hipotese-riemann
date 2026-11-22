from fractions import Fraction
from mpmath import mp

from collatz.periodic_denominator import periodic_points, step, weighted_sum
from riemann_spectra.prime_trace_kernel import prime_kernel, trivial_remainder


def test_trivial_remainder_against_independent_series():
    with mp.workdps(60):
        for t in map(mp.mpf, ('0.25','0.5','1','2','3')):
            q = mp.exp(-2*t)
            partial = -mp.fsum(q**k/(2*k*(2*k+1)) for k in range(1,301))
            tail = q**301/(602*603*(1-q))
            assert abs(trivial_remainder(t)-partial) <= tail+mp.mpf('1e-55')
        assert trivial_remainder(0) == mp.log(2)-1
        assert abs(prime_kernel(0)-(2+mp.euler-mp.log(4*mp.pi))) < mp.mpf('1e-58')


def test_periodic_orbits_and_denominator_invariance():
    for n in range(1,9):
        for a,b in ((3,1),(1,-1)):
            points = list(periodic_points(n,a,b))
            assert len({x for _,x in points}) == 2**n
            for bits,x in points:
                y = x
                product_weight = Fraction(1)
                for bit in bits:
                    assert y.numerator % 2 == bit
                    assert y.denominator == x.denominator
                    product_weight /= y.denominator
                    y = step(y,a,b)
                assert y == x
                assert product_weight == Fraction(1,x.denominator**n)


def test_period_two_arithmetic_separation():
    assert {x for _,x in periodic_points(2)} == {Fraction(0),Fraction(-1),Fraction(1),Fraction(2)}
    assert {x for _,x in periodic_points(2,1,-1)} == {Fraction(0),Fraction(-1),Fraction(-1,3),Fraction(-2,3)}
    assert weighted_sum(2) == 4
    assert weighted_sum(2,1,-1) == Fraction(20,9)
