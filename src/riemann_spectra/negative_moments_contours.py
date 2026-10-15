"""Controles analíticos finitos; não lê zeros nem estima momentos de L."""
from __future__ import annotations
import mpmath as mp


def reflected(function, s):
    """Reflexão holomorfa f#(s)=conj(f(1-conj(s)))."""
    return mp.conj(function(1-mp.conj(s)))


def polynomial_control(roots, delta, numerator=None):
    """Resíduos dos polos originais e deslocados, multiplicados por δ.

    Zeros artificiais simples na linha crítica; polinômio mônico.
    Não é um avaliador de L nem uma implementação de sua fórmula de razões.
    """
    rr=tuple(mp.convert(r) for r in roots)
    d=mp.mpf(delta)
    if not rr or len(set(rr)) != len(rr) or d <= 0:
        raise ValueError('Zeros distintos e deslocamento positivo são necessários.')
    if any(mp.re(r) != mp.mpf('0.5') for r in rr):
        raise ValueError('Este controle exige zeros na linha crítica.')
    h=numerator if numerator is not None else lambda s: mp.mpf(1)
    f=lambda s: mp.fprod(s-r for r in rr)
    df=lambda r: mp.fprod(r-other for other in rr if other != r)
    ratio=lambda s: h(s)*reflected(h,s-d)/(f(s)*reflected(f,s-d))
    rows=[]
    for r in rr:
        first=d*h(r)*reflected(h,r-d)/(df(r)*reflected(f,r-d))
        second=d*h(r+d)*reflected(h,r)/(f(r+d)*(-mp.conj(df(r))))
        rows.append(dict(root=r,original=first,shifted=second,
                         target=abs(h(r)/df(r))**2))
    return ratio,rows


def cue_regularized_mean(epsilon):
    """(ε/π) E integral angular |det(I-e^{-ε+iθ}U)|^{-2} dθ.

    Forma exata para CUE de qualquer N≥1; não há parâmetro N a ajustar.
    """
    e=mp.mpf(epsilon)
    if e <= 0:
        raise ValueError('ε deve ser positivo.')
    return 2*e/(-mp.expm1(-2*e))
