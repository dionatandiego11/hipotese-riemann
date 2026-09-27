# Verificação numérica de Siegel (arXiv:2111.07883v2), eqs. (2.25) e (2.26), com q=3 e q=5.
import numpy as np, mpmath as mp
N=1<<21
def seqs(q):
    chi=np.zeros(N); M=np.zeros(N); M[0]=1.0
    for n in range(1,N):
        h=n>>1
        if n&1: chi[n]=(q*chi[h]+1)/2; M[n]=q*M[h]/2
        else:   chi[n]=chi[h]/2;       M[n]=M[h]/2
    return chi,M
n=np.arange(N,dtype=float)
for q in (3,5):
    chi,M=seqs(q); sig=np.log2((q+1)/2)
    # checagem de (2.25) em z real
    for x in (1,-2):
        c=(1-M[1:])*x-chi[1:]
        f=lambda z: np.sum(c*z**n[1:])
        z=0.6
        lhs=f(z); rhs=-(q-1)*x/2*z/(1-z**2)-0.5*z/(1-z**2)+(q*z+1)/2*f(z*z)
        print(f"q={q} x={x} (2.25): lhs={lhs:.12g} rhs={rhs:.12g}")
    # checagem de (2.26) em s real grande (convergência absoluta)
    x=1; c=(1-M[1:])*x-chi[1:]
    F=lambda s: float(np.sum(c*n[1:]**(-s)))
    s=4.0
    zeta=float(mp.zeta(s))
    tail=sum((-0.5)**k*float(mp.binomial(s+k-1,k))*F(s+k) for k in range(1,60))
    rhs=-0.5*(2**s*((q-1)*x+1)-1)/(2**s-2**sig)*zeta+(q/2)/(2**s-2**sig)*tail
    print(f"q={q} (2.26) s={s}: F={F(s):.12g}  rhs={rhs:.12g}")
