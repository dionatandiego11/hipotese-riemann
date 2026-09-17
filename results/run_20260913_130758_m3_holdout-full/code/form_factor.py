"""
riemann_spectra.form_factor
Spectral Form Factor (SFF) em coordenadas unfolded com janelamento finito e separação conectada/desconectada.
"""

import math
from typing import Any, Dict, List

import numpy as np


def compute_spectral_form_factor(
    unfolded_levels: np.ndarray,
    tau_grid: np.ndarray,
    n_blocks: int = 1,
    window_type: str = "hann",
) -> Dict[str, Any]:
    """
    Calcula o Spectral Form Factor (SFF) nas coordenadas unfolded:
    Z_b(tau) = sum_n w_b(x_n) exp(-2pi * i * tau * x_n)
    mu_b(tau) = int w_b(x) exp(-2pi * i * tau * x) dx (termo desconectado suave)
    Q_b = int w_b(x)^2 dx (normalização de energia da janela)

    Estimador conectado:
    K_c(tau) = sum_b |Z_b(tau) - mu_b(tau)|^2 / sum_b Q_b

    Estimador total (incluindo desconectado):
    K_total(tau) = sum_b |Z_b(tau)|^2 / sum_b Q_b

    Compara com a previsão GUE assintótica: K_GUE(tau) = min(|tau|, 1.0).
    """
    x = np.sort(np.asarray(unfolded_levels, dtype=np.float64))
    n = len(x)
    tau = np.asarray(tau_grid, dtype=np.float64)

    # Dividir em blocos disjuntos (se n_blocks > 1) para reduzir variância
    block_size = n // n_blocks
    if block_size < 50:
        n_blocks = 1
        block_size = n

    z_connected_sq = np.zeros_like(tau, dtype=np.float64)
    z_total_sq = np.zeros_like(tau, dtype=np.float64)
    total_q = 0.0

    for b in range(n_blocks):
        idx_start = b * block_size
        idx_end = (b + 1) * block_size if b < n_blocks - 1 else n
        x_b = x[idx_start:idx_end]
        x_min = x_b[0]
        x_max = x_b[-1]
        L = x_max - x_min
        if L <= 0:
            continue

        # Janela de ponderação normalizada sobre o intervalo [x_min, x_max]
        u = (x_b - x_min) / L  # em [0, 1]
        x_c = x_min + 0.5 * L
        phase = np.exp(-2j * math.pi * tau * x_c)
        if window_type == "hann":
            w = 0.5 * (1.0 - np.cos(2.0 * math.pi * u))
            Q_b = 0.375 * L  # int w^2 dx
            # mu_b = e^{-2 pi i tau x_c} W(2 pi tau), W a resposta da Hann centrada (ver periods.hann_response)
            v = tau * L
            mu_b = phase * (0.5 * L * np.sinc(v) + 0.25 * L * (np.sinc(v - 1.0) + np.sinc(v + 1.0)))
        else:
            w = np.ones_like(x_b)
            Q_b = L
            mu_b = phase * L * np.sinc(tau * L)

        total_q += Q_b

        # Z_b(tau) = sum_n w_n exp(-2pi i tau x_n)
        # Vetorizado sobre blocos de tau para controle estrito de memória
        tau_chunks = np.array_split(tau, max(1, len(tau) // 500))
        mu_chunks = np.array_split(mu_b, len(tau_chunks))

        offset = 0
        for tc, muc in zip(tau_chunks, mu_chunks):
            # Matriz temporária pequena: len(tc) x len(x_b) <= 500 x 2500 -> ~10 MB
            phases = np.exp(-2j * math.pi * np.outer(tc, x_b))
            zb_chunk = phases @ w
            z_total_sq[offset:offset + len(tc)] += np.abs(zb_chunk)**2
            z_connected_sq[offset:offset + len(tc)] += np.abs(zb_chunk - muc)**2
            offset += len(tc)

    if total_q <= 0:
        total_q = 1.0

    k_connected = z_connected_sq / total_q
    k_total = z_total_sq / total_q

    # Teórico GUE linear ramp até o plateau em tau = 1
    k_gue_theor = np.minimum(np.abs(tau), 1.0)
    k_poisson_theor = np.ones_like(tau)

    return {
        "n_levels": n,
        "n_blocks": n_blocks,
        "window_type": window_type,
        "tau": tau.tolist(),
        "k_connected": k_connected.tolist(),
        "k_total": k_total.tolist(),
        "k_gue_theoretical": k_gue_theor.tolist(),
        "k_poisson_theoretical": k_poisson_theor.tolist(),
    }
