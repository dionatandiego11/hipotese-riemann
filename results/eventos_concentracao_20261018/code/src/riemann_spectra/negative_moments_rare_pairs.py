"""Controle CUE(2) de pares raros; nenhuma inferência para zeros de L."""
from __future__ import annotations

import mpmath as mp


def gap_density(phi):
    """Densidade da diferença angular com sinal, em [-pi,pi]."""
    return mp.sin(mp.mpf(phi) / 2) ** 2 / mp.pi


def shifted_pair_weight(phi, epsilon):
    """Peso discreto normalizado Aε para dois autovalores."""
    e = mp.mpf(epsilon)
    if e <= 0:
        raise ValueError("epsilon deve ser positivo")
    return mp.exp(e) / (2 * mp.sin(mp.mpf(phi) / 2) ** 2 + 2 * mp.sinh(e / 2) ** 2)


def scaled_defect_integral(epsilon, cutoff):
    """Integral em |phi|<=cutoff de (Aε-exp(ε)S)p/ε, em forma fechada."""
    e, d = mp.mpf(epsilon), mp.mpf(cutoff)
    if e <= 0 or not 0 <= d <= mp.pi:
        raise ValueError("epsilon>0 e 0<=cutoff<=pi")
    angle = mp.pi / 2 if d == mp.pi else mp.atan(mp.coth(e / 2) * mp.tan(d / 2))
    return -2 * mp.exp(e) * mp.tanh(e / 2) * angle / (mp.pi * e)


def inverse_pair_tail(x):
    """Pr(S>x), S=1/(1-cos(phi)); média finita e segundo momento infinito."""
    x = mp.mpf(x)
    if x < mp.mpf("0.5"):
        return mp.mpf(1)
    angle = 2 * mp.asin(1 / mp.sqrt(2 * x))
    return (angle - mp.sin(angle)) / mp.pi
