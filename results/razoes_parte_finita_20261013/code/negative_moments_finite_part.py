"""Coeficientes locais e controles do viés de regularização; sem dados de L."""
from __future__ import annotations
import mpmath as mp


def local_quotient_coefficients(f, h, rho):
    """a,b em H/F=a/(s−ρ)+b+O(s−ρ), para zero simples fornecido.

    f,h devem ser holomorfas; essa hipótese não é certificada por este helper.
    Usa diferenciação numérica mpmath, não aritmética intervalar.
    """
    r=mp.convert(rho)
    if f(r) != 0:
        raise ValueError('Este controle exige um zero exato fornecido de f.')
    first=mp.diff(f,r)
    if first == 0:
        raise ValueError('O zero deve ser simples.')
    a=h(r)/first
    b=mp.diff(h,r)/first-h(r)*mp.diff(f,r,2)/(2*first**2)
    return a,b


def finite_part_bias(finite_part_integral, coefficients, side=1):
    """B±=FP/π ±2Σ Re(a conj(b)); não calcula a parte finita de L."""
    if side not in (-1,1):
        raise ValueError('side deve ser +1 ou −1.')
    return (mp.mpf(finite_part_integral)/mp.pi+
            side*2*sum((mp.re(a*mp.conj(b)) for a,b in coefficients),mp.mpf(0)))


def richardson_two_scale(value_at_half, value_at_full):
    """Cancela um termo linear existente; não garante erro uniforme nem positividade."""
    return 2*value_at_half-value_at_full


def single_pole_window(epsilon, left_distance, right_distance, slope=0, side=1):
    """Controle q=exp(k(s−ρ))/(s−ρ), k real, janela com polo interno."""
    e,l,r,k=map(mp.mpf,(epsilon,left_distance,right_distance,slope))
    if min(e,l,r) <= 0 or side not in (-1,1):
        raise ValueError('ε e distâncias positivos; side em {−1,+1}.')
    return mp.exp(2*side*k*e)*(mp.atan(l/e)+mp.atan(r/e))/mp.pi
