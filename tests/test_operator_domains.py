from fractions import Fraction
from mpmath import mp
from collatz.denominator_transfer import (
    preimages, weight, transfer, adjoint_basis, inner_product,
)
from collatz.periodic_denominator import step
from riemann_spectra.prime_trace_kernel import trivial_remainder


def test_preimages_and_adjoint_identity():
    for y in (0,2,5,-1,Fraction(1,5),Fraction(2,7)):
        even,odd=preimages(y)
        assert even.numerator%2==0 and odd.numerator%2==1
        assert step(even)==y and step(odd)==y
        f={even:Fraction(3,7),odd:Fraction(-2,9)}
        assert transfer(f).get(Fraction(y),0)==inner_product(f,adjoint_basis(y))


def test_exact_noncompact_witnesses():
    ys=[3*k+2 for k in range(8)]
    vectors=[adjoint_basis(y) for y in ys]
    for i,(y,f) in enumerate(zip(ys,vectors)):
        assert transfer(f)=={Fraction(y):Fraction(2)}
        for j,g in enumerate(vectors):
            assert inner_product(f,g)==(2 if i==j else 0)


def test_denominator_weight_discontinuity_witness():
    assert weight(1)==1
    for k in range(1,9):
        x=1+Fraction(2**k,5**k)
        delta=x-1
        assert x.denominator==5**k
        assert delta.numerator==2**k and delta.denominator%2==1
        assert weight(x)==Fraction(1,5**k)


def test_trivial_remainder_derivative_independently():
    with mp.workdps(80):
        for h in map(mp.mpf,('0.01','0.0001','0.000001','0.00000001')):
            expected=mp.exp(h)*mp.atanh(mp.exp(-h))-1
            assert abs(mp.diff(trivial_remainder,h)-expected)<mp.mpf('1e-60')
