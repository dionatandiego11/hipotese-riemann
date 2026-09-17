"""
riemann_indep.core — implementação independente (não importa `riemann_spectra`).

Conteúdo: leitura do arquivo bruto, contagem média e sua inversa (W de Lambert), janela de Hann e sua
resposta por integrais exatas de exponenciais, termo suave em forma fechada (Si/Ci) e soma direta
trigonométrica da transformada.

Convenção (PROTOCOLO §3.1, §7.2):
    F(t) = sum_{A<=g<=B} w(g) exp(-i (g - Ec) t) - (1/2pi) int_A^B w(E) log(E/2pi) exp(-i (E - Ec) t) dE
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from scipy.special import lambertw, sici

TAU = 2.0 * math.pi


# --------------------------------------------------------------------------- dados
def read_raw_zeros(path: str | Path, first_index: int, last_index: int) -> np.ndarray:
    """Lê as ordenadas de índices [first_index, last_index] (1-based) direto do arquivo de Odlyzko."""
    out = []
    with open(path, "r", encoding="ascii") as fh:
        for n, line in enumerate(fh, start=1):
            if n < first_index:
                continue
            if n > last_index:
                break
            out.append(float(line.split()[0]))
    arr = np.array(out)
    if len(arr) != last_index - first_index + 1 or not np.all(np.diff(arr) > 0):
        raise ValueError("leitura incompleta ou não ordenada")
    return arr


# --------------------------------------------------------------------------- contagem média
def nbar(E):
    y = np.asarray(E, dtype=float) / TAU
    return y * np.log(y) - y + 0.875


def nbar_inverse(x):
    """y log y - y = x - 7/8  =>  y = (x - 7/8) / W((x - 7/8)/e); seguido de um passo de Newton."""
    x = np.asarray(x, dtype=float)
    a = x - 0.875
    y = a / np.real(lambertw(a / math.e))
    E = TAU * y
    for _ in range(2):
        E = E - (nbar(E) - x) / (np.log(E / TAU) / TAU)
    return E


# --------------------------------------------------------------------------- janela e resposta
def hann(E, A, B):
    L = B - A
    return 0.5 - 0.5 * np.cos(TAU * (np.asarray(E) - A) / L)


def _sinc_int(x, L):
    """int_{-L/2}^{L/2} exp(-i u x) du = 2 sin(x L/2)/x, com limite L em x = 0."""
    x = np.asarray(x, dtype=float)
    small = np.abs(x) < 1e-12
    xs = np.where(small, 1.0, x)
    return np.where(small, L, 2.0 * np.sin(xs * L / 2.0) / xs)


def hann_response(omega, L):
    """W(ω) = ∫ w(u) e^{-iuω} du, w(u) = 1/2 + (e^{iκu} + e^{-iκu})/4 centrada, κ = 2π/L."""
    k = TAU / L
    return 0.5 * _sinc_int(omega, L) + 0.25 * _sinc_int(np.asarray(omega) - k, L) + 0.25 * _sinc_int(np.asarray(omega) + k, L)


def fwhm_hann(L: float) -> float:
    """Largura total a meia altura de |W| por bissecção (independente de brentq)."""
    W0 = float(hann_response(0.0, L))
    lo, hi = 0.0, 2.0 * TAU / L
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if abs(float(hann_response(mid, L))) > 0.5 * W0:
            lo = mid
        else:
            hi = mid
    return 2.0 * 0.5 * (lo + hi)


# --------------------------------------------------------------------------- termo suave (forma fechada)
def _J(Omega: np.ndarray, A: float, B: float) -> np.ndarray:
    """
    J(Ω) = ∫_A^B log(E/2π) e^{iΩE} dE
         = [log(E/2π) e^{iΩE}/(iΩ)]_A^B − (1/(iΩ)) ∫_A^B e^{iΩE}/E dE,
    ∫_A^B e^{iΩE}/E dE = [Ci(|Ω|E)]_A^B + i sgn(Ω) [Si(|Ω|E)]_A^B.
    """
    Om = np.asarray(Omega, dtype=float)
    a = np.abs(Om)
    siA, ciA = sici(a * A)
    siB, ciB = sici(a * B)
    inner = (ciB - ciA) + 1j * np.sign(Om) * (siB - siA)
    bnd = (math.log(B / TAU) * np.exp(1j * Om * B) - math.log(A / TAU) * np.exp(1j * Om * A)) / (1j * Om)
    return bnd - inner / (1j * Om)


def smooth_term(t: np.ndarray, A: float, B: float) -> np.ndarray:
    """(1/2π) ∫_A^B w(E) log(E/2π) e^{-i(E−Ec)t} dE em forma fechada, para t ≠ 0 e t ≠ ±2π/L."""
    t = np.asarray(t, dtype=float)
    L = B - A
    Ec = 0.5 * (A + B)
    k = TAU / L
    # w(E) = 1/2 − (1/4) e^{iκ(E−A)} − (1/4) e^{−iκ(E−A)}
    val = 0.5 * _J(-t, A, B) - 0.25 * np.exp(-1j * k * A) * _J(k - t, A, B) - 0.25 * np.exp(1j * k * A) * _J(-k - t, A, B)
    return np.exp(1j * Ec * t) * val / TAU


# --------------------------------------------------------------------------- transformada por soma direta
def discrete_sum(levels: np.ndarray, t: np.ndarray, A: float, B: float, chunk: int = 256) -> np.ndarray:
    """Σ w(γ) e^{−i(γ−Ec)t} por soma direta em partes real e imaginária (sem NUFFT)."""
    g = np.asarray(levels, dtype=float)
    g = g[(g >= A) & (g <= B)]
    Ec = 0.5 * (A + B)
    u = g - Ec
    w = hann(g, A, B)
    t = np.asarray(t, dtype=float)
    re = np.empty(len(t))
    im = np.empty(len(t))
    for s in range(0, len(t), chunk):
        ph = np.multiply.outer(t[s:s + chunk], u)
        re[s:s + chunk] = np.cos(ph) @ w
        im[s:s + chunk] = -(np.sin(ph) @ w)
    return re + 1j * im


class Instrument:
    """Parâmetros do instrumento para um bloco (A2, A3)."""

    def __init__(self, gammas: np.ndarray, t_min: float = 0.5, t_max: float = 5.0, ppf: float = 8.0):
        self.A = float(gammas[0])
        self.B = float(gammas[-1])
        self.L = self.B - self.A
        self.Ec = 0.5 * (self.A + self.B)
        self.W0 = float(hann_response(0.0, self.L))
        self.fwhm = fwhm_hann(self.L)
        self.dt = self.fwhm / ppf
        self.n_t = int(math.floor((t_max - t_min) / self.dt)) + 1
        self.t = t_min + self.dt * np.arange(self.n_t)
        self.smooth = smooth_term(self.t, self.A, self.B)

    def F(self, levels: np.ndarray) -> np.ndarray:
        return discrete_sum(levels, self.t, self.A, self.B) - self.smooth

    def F_at(self, levels: np.ndarray, t: np.ndarray) -> np.ndarray:
        t = np.atleast_1d(np.asarray(t, dtype=float))
        return discrete_sum(levels, t, self.A, self.B) - smooth_term(t, self.A, self.B)


def recurrence_sum(levels: np.ndarray, t0: float, dt: float, n_t: int, A: float, B: float) -> np.ndarray:
    """
    Σ w(γ) e^{−i(γ−Ec)t_k}, t_k = t0 + k dt, pela recorrência z_{k+1} = z_k · e^{−iu dt} (malha uniforme).
    Caminho numérico distinto da soma direta; renormaliza |z| = 1 a cada 512 passos para conter a deriva.
    Usado nos controles; validado contra `discrete_sum` nos testes.
    """
    g = np.asarray(levels, dtype=float)
    g = g[(g >= A) & (g <= B)]
    u = g - 0.5 * (A + B)
    w = hann(g, A, B)
    z = np.exp(-1j * u * t0)
    step = np.exp(-1j * u * dt)
    out = np.empty(n_t, dtype=complex)
    for k in range(n_t):
        out[k] = z @ w
        z *= step
        if k % 512 == 511:
            z /= np.abs(z)
    return out


def instrument_F_fast(ins: "Instrument", levels: np.ndarray) -> np.ndarray:
    return recurrence_sum(levels, ins.t[0], ins.dt, ins.n_t, ins.A, ins.B) - ins.smooth
