import mpmath as mp
from riemann_spectra.negative_moments_discrete_ratios import (
    log_weight_factor,cue_palm_ratio,cue_shifted_discrete,
)
from riemann_spectra.negative_moments_ratios import diagonal_laurent,arithmetic_diagonal,prime_divisors


def test_prime_local_generator_derivative():
    with mp.workdps(50):
        for p in (2,5,11):
            a,b,v=map(mp.mpf,['0.12','0.19','0.03'])
            local=lambda u:1-mp.power(p,-1-u-b)+mp.power(p,-1-v-b)+mp.power(p,-1-a-b)
            actual=mp.diff(local,v)/local(v)
            expected=mp.log(p)*mp.power(p,-1-v-b)/(1+mp.power(p,-1-a-b))
            assert abs(actual-expected) < mp.mpf('1e-40')


def test_weight_factors_reproduce_both_leading_constants():
    with mp.workdps(50):
        # Reuse the all-prime factor within this calculation; remove bad primes exactly.
        for e in map(mp.mpf,['0.001','0.0001','0.00001']):
            bases={kind:log_weight_factor(e,0,1,kind) for kind in (7,8)}
            for q in (1,4,5,12):
                k7,b7=diagonal_laurent(q,7)
                constant=-b7/k7
                for kind in (7,8):
                    value,tail=bases[kind]
                    if kind==7:
                        value-=sum((mp.log(p)*mp.power(p,-1-e)/(1+mp.power(p,-1-2*e)) for p in prime_divisors(q)),mp.mpf(0))
                    else:
                        value-=sum((mp.log(p)/(mp.power(p,1+e)+1) for p in prime_divisors(q)),mp.mpf(0))
                    assert abs(e*value-1) < mp.mpf('0.01')
                    assert abs(value-1/e-constant) < mp.mpf('0.02')+tail
                    k,_=diagonal_laurent(q,kind)
                    leading=e**2*arithmetic_diagonal(2*e,q,kind)*value
                    assert abs(leading/(k/2)-1) < mp.mpf('0.01')


def test_cue_palm_by_independent_toeplitz_determinants():
    with mp.workdps(50):
        for m in (0,1,2,5,10):
            for r in map(mp.mpf,['0.25','0.9','0.99']):
                def coefficient(k):
                    return 2/(1+r) if k==0 else -(1-r)/(1+r)*r**(abs(k)-1)
                determinant=mp.det(mp.matrix([[coefficient(i-j) for j in range(m)] for i in range(m)])) if m else mp.mpf(1)
                assert abs(determinant/cue_palm_ratio(m,r)-1) < mp.mpf('1e-35')
        r=mp.mpf('0.25')
        weight=lambda theta:abs(1-mp.exp(1j*theta))**2/abs(1-r*mp.exp(1j*theta))**2
        for k in (0,1,2):
            actual=mp.quad(lambda t:weight(t)*mp.exp(-1j*k*t),[-mp.pi,0,mp.pi])/(2*mp.pi)
            expected=2/(1+r) if k==0 else -(1-r)/(1+r)*r**(k-1)
            assert abs(actual-expected) < mp.mpf('1e-35')


def test_cue_joint_shift_size_limit_keeps_a_bias():
    with mp.workdps(50):
        for c in map(mp.mpf,['0.5','1']):
            errors=[]
            for n in (10,100,1000):
                actual=cue_shifted_discrete(n,c/n)
                errors.append(abs(actual-(1+c/2)))
                assert actual > 1
            assert errors[2] < errors[1] < errors[0]
