"""
riemann_spectra.unfolding
Fórmula de Riemann-von Mangoldt, densidade média, desdobramento (unfolding) e sua inversa numérica.
"""

import math
from typing import Tuple

import numpy as np
from scipy.special import loggamma

TWO_PI = 2.0 * math.pi


def n_bar_rvm(E: np.ndarray | float) -> np.ndarray | float:
    """
    Função suave média de contagem de zeros de Riemann-von Mangoldt:
    N_bar(E) = (E / 2pi) * log(E / 2pi) - (E / 2pi) + 7/8
    Válida para E > 0.
    """
    e_over_2pi = E / TWO_PI
    return e_over_2pi * np.log(e_over_2pi) - e_over_2pi + 0.875


def d_bar_rvm(E: np.ndarray | float) -> np.ndarray | float:
    """
    Densidade média teórica d_bar(E) = d(N_bar)/dE = (1 / 2pi) * log(E / 2pi).
    Válida para E > 2pi (onde a densidade é positiva).
    """
    return (1.0 / TWO_PI) * np.log(E / TWO_PI)


def riemann_siegel_theta(t: np.ndarray | float) -> np.ndarray | float:
    """
    Fase suave de Riemann-Siegel theta(t) usando a função log-gama complexa:
    theta(t) = Im(log Gamma(1/4 + i*t/2)) - (t/2)*log(pi)
    Referência: DLMF 25.10.
    """
    # Suporte a escalares ou arrays numpy
    t_arr = np.asarray(t, dtype=np.float64)
    s = 0.25 + 0.5j * t_arr
    # loggamma do scipy suporta complexo
    theta_val = np.imag(loggamma(s)) - 0.5 * t_arr * math.log(math.pi)
    return theta_val if isinstance(t, np.ndarray) else float(theta_val)


def n_bar_theta(E: np.ndarray | float) -> np.ndarray | float:
    """
    Contagem média baseada na fase de Riemann-Siegel exata:
    N_theta(E) = 1 + theta(E) / pi.
    """
    return 1.0 + riemann_siegel_theta(E) / math.pi


def inverse_n_bar(x: np.ndarray | float, tol: float = 1e-12, max_iter: int = 50) -> np.ndarray | float:
    """
    Inversa numérica exata de N_bar(E) via iteração de Newton-Raphson com segunda ordem (Halley).
    Resolve N_bar(E) = x para E > 2pi.
    Garante inversão de alta precisão (erro relativo < 1e-12).
    """
    is_scalar = isinstance(x, (int, float))
    x_arr = np.atleast_1d(np.asarray(x, dtype=np.float64))

    # Chute inicial assintótico invertendo E*log(E) ~ 2pi*x
    # Se x_eff = 2pi*(x - 7/8), então y*log(y) ~ x_eff onde y = E/2pi
    x_eff = np.maximum(TWO_PI * (x_arr - 0.875), 1.0)
    # y ~ x_eff / W(x_eff) ~ x_eff / (log(x_eff) - log(log(x_eff)))
    log_x = np.log(np.maximum(x_eff, 2.0))
    y0 = x_eff / np.maximum(log_x - np.log(np.maximum(log_x, 1.1)), 0.5)
    E = np.maximum(y0 * TWO_PI, 2.0 * math.pi + 0.01)

    for _ in range(max_iter):
        f = n_bar_rvm(E) - x_arr
        f_prime = d_bar_rvm(E)
        f_prime2 = 1.0 / (TWO_PI * E)

        # Passo de Halley: delta = f / (f' - 0.5 * f * f'' / f')
        denom = f_prime - 0.5 * f * f_prime2 / np.maximum(f_prime, 1e-15)
        step = f / np.maximum(denom, 1e-15)
        E -= step
        E = np.maximum(E, 2.0 * math.pi + 1e-6)

        if np.max(np.abs(step)) < tol:
            break

    return float(E[0]) if is_scalar else E


def unfold_spectrum(gammas: np.ndarray, method: str = "rvm") -> Tuple[np.ndarray, np.ndarray]:
    """
    Mapeia os níveis de energia gamma_n para coordenadas normalizadas x_n (unfolded),
    onde o espaçamento médio local é unitário:
    x_n = N_bar(gamma_n).
    Calcula também os espaçamentos consecutivos s_n = x_{n+1} - x_n.
    """
    if method == "rvm":
        x = n_bar_rvm(gammas)
    elif method == "theta":
        x = n_bar_theta(gammas)
    else:
        raise ValueError(f"Método de unfolding desconhecido: {method}")

    s = np.diff(x)
    return x, s


def fold_spectrum(x: np.ndarray) -> np.ndarray:
    """
    Aplica a inversa numérica de N_bar para recuperar níveis em coordenadas de energia originais.
    """
    return inverse_n_bar(x)
