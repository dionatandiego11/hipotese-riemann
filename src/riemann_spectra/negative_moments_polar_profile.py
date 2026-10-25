"""Perfil local do gerador em janela fixa; não estima a soma de momentos de L."""
from __future__ import annotations
import mpmath as mp


def polar_shape(z, shift_ratio):
    """1+z/(1+λ), com λ=ν/ε fixo, 0<λ<1/2."""
    lam=mp.mpf(shift_ratio)
    if not 0 < lam < mp.mpf('0.5'):
        raise ValueError('Este perfil exige 0<λ<1/2 fixo.')
    return 1+mp.convert(z)/(1+lam)


def single_pole_scaled_mean(epsilon, shift_ratio, z, distance=1):
    """εM para F(s)=s−ρ,H=1 e janela simétrica [γ−D,γ+D].

    ν=λε,u=ν+εz. Forma fechada de uma integral de controle artificial.
    """
    e,lam,d=map(mp.mpf,(epsilon,shift_ratio,distance))
    polar_shape(z,lam)  # Validate the fixed-ratio domain.
    if e <= 0 or d <= 0:
        raise ValueError('ε e distância às bordas devem ser positivos.')
    base=2*mp.atan(d/e)
    correction=2*mp.convert(z)*(lam*mp.atan(d/e)-mp.atan(d/(lam*e)))/(lam**2-1)
    return base+correction
