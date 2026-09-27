# Formas corrigidas (derivação própria):
# (2.25'): f(z) = (qz+1)/2 f(z^2) + x z (2+z-q)/(2(1-z^2)) - z/(2(1-z^2))
# (2.26'): F(s) = { (x[(2-q)(2^s-1)+1] - (2^s-1)) zeta(s) + q S(s) } / (2(2^s - 2^sigma_q)),
#          S(s) = sum_{k>=1} (-1/2)^k binom(s+k-1,k) F(s+k)
import numpy as np, mpmath as mp
N=1<<20
def seqs(q):
    chi=np.zeros(N); M=np.zeros(N); M[0]=1.0
    for n in range(1,N):
        h=n>>1
        if n&1: chi[n]=(q*chi[h]+1)/2; M[n]=q*M[h]/2
        else:   chi[n]=chi[h]/2;       M[n]=M[h]/2
    return chi,M
n=np.arange(N,dtype=float)
for q in (3,5,7):
    chi,M=seqs(q); sig=np.log2((q+1)/2)
    for x in (1,-2,5):
        c=(1-M[1:])*x-chi[1:]
        f=lambda z: np.sum(c*z**n[1:])
        for z in (0.3,0.6):
            lhs=f(z); rhs=(q*z+1)/2*f(z*z)+x*z*(2+z-q)/(2*(1-z*z))-z/(2*(1-z*z))
            assert abs(lhs-rhs)<1e-9*max(1,abs(lhs)), (q,x,z,lhs,rhs)
        F=lambda s: float(np.sum(c*n[1:]**(-s)))
        for s in (4.0,5.5):
            S=sum((-0.5)**k*float(mp.binomial(s+k-1,k))*F(s+k) for k in range(1,80))
            rhs=((x*((2-q)*(2**s-1)+1)-(2**s-1))*float(mp.zeta(s))+q*S)/(2*(2**s-2**sig))
            print(f"q={q} x={x:>2} s={s}: F={F(s):.12f} (2.26')={rhs:.12f} dif={F(s)-rhs:.1e}")
print("(2.25') ok em todos os casos")
