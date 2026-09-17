"""
riemann_spectra.controls
Modelos de controle nulo, ensembles de matrizes aleatórias (GUE) e sinais sintéticos.
"""

import math
from typing import Dict, List, Tuple

import numpy as np
from scipy.linalg import eigvalsh, eigvalsh_tridiagonal

from riemann_spectra.unfolding import fold_spectrum


def generate_poisson_spectrum(
    n_levels: int,
    length: float | None = None,
    fixed_count: bool = True,
    rng: np.random.Generator | None = None,
) -> np.ndarray:
    """
    Gera um espectro de Poisson com espaçamento médio unitário (intensidade lambda = 1).

    Parâmetros:
    - n_levels: número de níveis a gerar.
    - length: comprimento do intervalo [0, length]. Se None, usa length = n_levels.
    - fixed_count: se True, condicionado a exatamente n_levels uniformes ordenados em [0, length];
                   se False, gerado por soma de variáveis exponenciais i.i.d. de média 1.
    - rng: gerador pseudoaleatório (NumPy Generator).
    """
    if rng is None:
        rng = np.random.default_rng()

    L = float(length) if length is not None else float(n_levels)

    if fixed_count:
        # Estatísticas de ordem de variáveis uniformes em [0, L]
        unifs = rng.uniform(0.0, L, size=n_levels)
        return np.sort(unifs)
    else:
        # Processo de Poisson homogêneo livre
        # Gerar espaçamentos exponenciais com margem de segurança
        est_n = int(L + 5.0 * math.sqrt(L) + 50)
        spacings = rng.exponential(scale=1.0, size=est_n)
        cumsum = np.cumsum(spacings)
        inside = cumsum[cumsum <= L]
        return inside


def semicircle_cdf(y: np.ndarray) -> np.ndarray:
    """
    CDF da lei do semicírculo de Wigner suportada no intervalo [-1, 1]:
    rho(y) = (2 / pi) * sqrt(1 - y^2)
    CDF(y) = 1/2 + (y * sqrt(1 - y^2) + arcsin(y)) / pi
    """
    y_clipped = np.clip(y, -1.0, 1.0)
    term1 = y_clipped * np.sqrt(np.maximum(0.0, 1.0 - y_clipped**2))
    term2 = np.arcsin(y_clipped)
    return 0.5 + (term1 + term2) / math.pi


def generate_gue_dense(
    n: int,
    bulk_fraction: float = 0.5,
    rng: np.random.Generator | None = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera autovalores do GUE (Gaussian Unitary Ensemble) via matriz densa completa N x N.
    H = (A + A^H) / (2 * sqrt(2 * N)) de forma que o suporte assintótico seja [-1, 1].

    Retorna:
    - unfolded_bulk: níveis unfolded da região central com espaçamento médio ~ 1.
    - raw_eigenvalues: todos os autovalores originais ordenados em [-1, 1].
    """
    if rng is None:
        rng = np.random.default_rng()

    # Partes real e imaginária gaussianas independentes
    real_part = rng.normal(0.0, 1.0, size=(n, n))
    imag_part = rng.normal(0.0, 1.0, size=(n, n))
    A = (real_part + 1j * imag_part) / math.sqrt(2.0)

    # Matriz hermitiana: E|H_ij|^2 = 1/2 (i != j), Var(H_ii) = 1/2  => raio do semicírculo sqrt(2N)
    H = (A + A.conj().T) / 2.0
    # Normalização para suporte semicircular [-1, 1]
    # (correção 13/09/2026: a versão anterior dividia por sqrt(4N), dando raio 1/sqrt(2))
    H /= math.sqrt(2.0 * n)

    evals = eigvalsh(H)

    # Unfolding com a lei do semicírculo exata
    unfolded = n * semicircle_cdf(evals)

    # Selecionar região central do bulk (ex: [-bulk_fraction/2, +bulk_fraction/2])
    half_f = bulk_fraction / 2.0
    mask = (evals >= -half_f) & (evals <= half_f)
    bulk_unfolded = unfolded[mask]

    return bulk_unfolded, evals


def generate_gue_tridiagonal(
    n: int,
    bulk_fraction: float = 0.5,
    rng: np.random.Generator | None = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera autovalores do GUE (beta = 2) usando a representação tridiagonal de Dumitriu-Edelman (2002).
    Complexidade O(N^2) em vez de O(N^3), permitindo simulações de alta dimensão.

    Matriz tridiagonal simétrica T:
    - Diagonal a_i ~ Normal(0, 2) / sqrt(2) para i = 1..N
    - Subdiagonal b_i ~ Chi(2*(N-i)) / sqrt(2) para i = 1..N-1
    Normalizada por 1 / sqrt(4 * N) para suporte assintótico em [-1, 1].
    """
    if rng is None:
        rng = np.random.default_rng()

    # Modelo beta-Hermite (Dumitriu-Edelman): H = (1/sqrt 2) tridiag(N(0,2); chi_{beta(n-i)}), beta = 2.
    # Diagonal N(0, 2)/sqrt(2) = N(0, 1).
    # (correção 13/09/2026: a versão anterior usava N(0,1)/sqrt(2), ensemble mais rígido que o GUE)
    diag = rng.normal(0.0, math.sqrt(2.0), size=n) / math.sqrt(2.0)

    # Subdiagonal: qui-quadrado com 2*(N-i) graus de liberdade dividido por sqrt(2)
    # chi(k) = sqrt(gamma(shape=k/2, scale=2))
    k_vec = 2.0 * np.arange(n - 1, 0, -1, dtype=np.float64)
    subdiag = np.sqrt(rng.gamma(shape=k_vec / 2.0, scale=2.0)) / math.sqrt(2.0)

    # Fator de escala para semicírculo [-1, 1]
    scale = 1.0 / math.sqrt(4.0 * n)
    diag *= scale
    subdiag *= scale

    # Diagonalização rápida tridiagonal O(N^2)
    evals = eigvalsh_tridiagonal(diag, subdiag)

    # Unfolding com a lei do semicírculo
    unfolded = n * semicircle_cdf(evals)

    half_f = bulk_fraction / 2.0
    mask = (evals >= -half_f) & (evals <= half_f)
    bulk_unfolded = unfolded[mask]

    return bulk_unfolded, evals


def shuffle_spacings(
    unfolded_spacings: np.ndarray,
    origin_x: float = 0.0,
    rng: np.random.Generator | None = None,
) -> np.ndarray:
    """
    Controle de permutação dos espaçamentos unfolded:
    Preserva a distribuição marginal de s_n, mas destrói correlações entre níveis e coerência.
    Reconstrói os níveis pela soma cumulativa:
    x'_0 = origin_x, x'_k = origin_x + sum_{j=1}^k s_{pi(j)}.
    """
    if rng is None:
        rng = np.random.default_rng()

    shuffled_s = rng.permutation(unfolded_spacings)
    reconstructed_x = np.empty(len(shuffled_s) + 1, dtype=np.float64)
    reconstructed_x[0] = origin_x
    reconstructed_x[1:] = origin_x + np.cumsum(shuffled_s)
    return reconstructed_x


def generate_energy_control_from_unfolded(
    unfolded_levels: np.ndarray,
) -> np.ndarray:
    """
    Mapeia níveis de controle em coordenadas unfolded de volta para o domínio de energia
    utilizando a inversa numérica de N_bar(E).
    """
    return fold_spectrum(unfolded_levels)


def randomize_fourier_phases(
    complex_spectrum: np.ndarray,
    preserve_hermitian: bool = True,
    rng: np.random.Generator | None = None,
) -> np.ndarray:
    """
    Randomiza as fases da transformada de Fourier preservando os módulos |F(t)|.
    Serve como controle negativo estrito para coerência de interferência de fase.
    """
    if rng is None:
        rng = np.random.default_rng()

    n = len(complex_spectrum)
    modulus = np.abs(complex_spectrum)
    random_phases = rng.uniform(0.0, 2.0 * math.pi, size=n)

    if preserve_hermitian and n > 2:
        # Se for representação simétrica com metade conjugada
        half = (n - 1) // 2
        random_phases[0] = 0.0
        random_phases[n - half:] = -random_phases[1:half + 1][::-1]

    return modulus * np.exp(1j * random_phases)


def generate_synthetic_signal(
    t_grid: np.ndarray,
    frequencies: List[float],
    amplitudes: List[float],
    phases: List[float] | None = None,
    noise_sigma: float = 0.0,
    rng: np.random.Generator | None = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera sinal sintético com linhas espectrais conhecidas para calibração do detector cego.
    f(t) = sum_k A_k cos(omega_k * t + phi_k) + noise.
    """
    if rng is None:
        rng = np.random.default_rng()

    signal = np.zeros_like(t_grid, dtype=np.float64)
    if phases is None:
        phases = [0.0] * len(frequencies)

    for omega, amp, phi in zip(frequencies, amplitudes, phases):
        signal += amp * np.cos(omega * t_grid + phi)

    clean_signal = signal.copy()
    if noise_sigma > 0.0:
        signal += rng.normal(0.0, noise_sigma, size=len(t_grid))

    return signal, clean_signal


def generate_gue_central_levels(
    n_levels: int,
    retained_fraction: float = 0.6,
    rng: np.random.Generator | None = None,
) -> Tuple[np.ndarray, Dict[str, float]]:
    """
    Níveis GUE unfolded de UMA única matriz tridiagonal (Dumitriu-Edelman, beta = 2):
    retém os `n_levels` níveis centrais por índice, de uma matriz de dimensão
    ceil(n_levels / retained_fraction). Unfolding pela CDF do semicírculo, N * CDF(lambda).
    Não concatena matrizes independentes.
    """
    if rng is None:
        rng = np.random.default_rng()
    dim = int(math.ceil(n_levels / retained_fraction))
    _, evals = generate_gue_tridiagonal(dim, bulk_fraction=2.0, rng=rng)
    unfolded = dim * semicircle_cdf(evals)
    start = (dim - n_levels) // 2
    central = unfolded[start:start + n_levels]
    meta = {
        "matrix_dim": dim,
        "retained_levels": n_levels,
        "retained_fraction": n_levels / dim,
        "edge_eigenvalue_low": float(evals[start]),
        "edge_eigenvalue_high": float(evals[start + n_levels - 1]),
    }
    return central, meta


def gue_energy_levels_like(
    gammas: np.ndarray,
    retained_fraction: float = 0.6,
    rng: np.random.Generator | None = None,
) -> np.ndarray:
    """
    Controle GUE em energia original com a mesma contagem e origem dos zeros:
    x'_k = Nbar(gamma_1) + (y_k - y_1) * (n - 1) / (y_n - y_1), E'_k = Nbar^{-1}(x'_k).
    A reescala linear fixa o comprimento unfolded total (contagem condicionada).
    """
    from riemann_spectra.unfolding import n_bar_rvm

    gammas = np.asarray(gammas, dtype=np.float64)
    n = len(gammas)
    y, _ = generate_gue_central_levels(n, retained_fraction, rng)
    x0 = float(n_bar_rvm(gammas[0]))
    x1 = float(n_bar_rvm(gammas[-1]))
    x = x0 + (y - y[0]) * (x1 - x0) / (y[-1] - y[0])
    return fold_spectrum(x)


def shuffled_energy_levels_like(
    gammas: np.ndarray,
    rng: np.random.Generator | None = None,
) -> np.ndarray:
    """Controle de permutação dos espaçamentos unfolded, reconstruído em energia original."""
    from riemann_spectra.unfolding import unfold_spectrum

    x, s = unfold_spectrum(np.asarray(gammas, dtype=np.float64))
    return fold_spectrum(shuffle_spacings(s, origin_x=float(x[0]), rng=rng))


def inject_density_lines(
    unfolded_levels: np.ndarray,
    periods: np.ndarray,
    coefficients: np.ndarray,
    tol: float = 1e-11,
    max_iter: int = 60,
) -> np.ndarray:
    """
    Sinal sintético no nível dos autovalores (testa a cadeia inteira, incluindo o termo suave):
    resolve N_mod(E_n) = x_n com
        N_mod(E) = Nbar(E) + sum_k Re[C_k e^{i E T_k}] / T_k  integrado, i.e.
        d_mod(E) = dbar(E) + sum_k Re[C_k e^{i E T_k}].
    Para C_k complexo, a densidade ganha |C_k| cos(E T_k + arg C_k). Exige |C| pequeno o
    bastante para d_mod > 0 (verificado).
    """
    from riemann_spectra.unfolding import d_bar_rvm, n_bar_rvm

    x = np.asarray(unfolded_levels, dtype=np.float64)
    T = np.asarray(periods, dtype=np.float64)
    C = np.asarray(coefficients, dtype=np.complex128)
    E = fold_spectrum(x)

    def osc_N(E_arr):
        ph = np.exp(1j * np.outer(E_arr, T))
        return np.real(ph @ (C / (1j * T)))

    def osc_d(E_arr):
        ph = np.exp(1j * np.outer(E_arr, T))
        return np.real(ph @ C)

    for _ in range(max_iter):
        f = n_bar_rvm(E) + osc_N(E) - x
        fp = d_bar_rvm(E) + osc_d(E)
        if np.any(fp <= 0):
            raise ValueError("Densidade modulada não positiva: reduza os coeficientes injetados.")
        step = f / fp
        E = E - step
        if np.max(np.abs(step)) < tol:
            break
    return E
