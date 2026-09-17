"""
riemann_spectra.periods
Transformada da densidade oscilatória e detector de períodos sem catálogo.

ATENÇÃO METODOLÓGICA:
Este módulo NÃO importa nem referencia teoria dos números. As entradas são
apenas níveis de energia, a janela [A, B], a malha de períodos e parâmetros de
ruído. A saída do detector é congelada antes de qualquer comparação aritmética.

Convenção de Fourier (preservada em todo o módulo):
    F_w(t) = sum_{A<=g<=B} w(g) e^{-i (g - E_c) t}  -  int_A^B w(E) dbar(E) e^{-i (E - E_c) t} dE
Uma componente de densidade  c cos(E T)  produz, para t perto de T,
    F_w(t) ~ (c / 2) e^{i E_c T} W(t - T),
onde W(w) = int w(E) e^{-i (E - E_c) w} dE é a resposta (real) da janela.
"""

import math
from typing import Any, Callable, Dict, List, Tuple

import numpy as np
from scipy.optimize import brentq
from scipy.signal import find_peaks
from scipy.special import digamma

from riemann_spectra.unfolding import d_bar_rvm

TWO_PI = 2.0 * math.pi


# ---------------------------------------------------------------------------
# Janela e resposta instrumental
# ---------------------------------------------------------------------------

# Janelas de soma de cossenos em [A, B]:  w(u) = sum_k (-1)^k a_k cos(2 pi k u / L),  u in [0, L].
# Centrada (u' = u - L/2):  w(u') = sum_k a_k cos(2 pi k u' / L).
WINDOW_COEFFICIENTS: Dict[str, Tuple[float, ...]] = {
    "hann": (0.5, 0.5),
    # Blackman-Harris de 4 termos (Harris, 1978)
    "blackman_harris": (0.35875, 0.48829, 0.14128, 0.01168),
}


def window_coefficients(window: str) -> Tuple[float, ...]:
    if window not in WINDOW_COEFFICIENTS:
        raise ValueError(f"Janela não implementada: {window!r}. Opções: {sorted(WINDOW_COEFFICIENTS)}")
    return WINDOW_COEFFICIENTS[window]


def window_values(E: np.ndarray, A: float, B: float, window: str = "hann") -> np.ndarray:
    """Janela de soma de cossenos suportada em [A, B] (zero fora do intervalo)."""
    coeffs = window_coefficients(window)
    E = np.asarray(E, dtype=np.float64)
    u = (E - A) / (B - A)
    w = np.zeros_like(u)
    for k, a in enumerate(coeffs):
        w += ((-1) ** k) * a * np.cos(TWO_PI * k * u)
    return np.where((u >= 0.0) & (u <= 1.0), w, 0.0)


def window_hann(E: np.ndarray, A: float, B: float) -> np.ndarray:
    return window_values(E, A, B, "hann")


def window_response(omega: np.ndarray | float, L: float, window: str = "hann") -> np.ndarray | float:
    """
    Resposta analítica W(omega) = int_{-L/2}^{L/2} w(u) e^{-i u omega} du (real e par):
        W = a_0 L sinc(v) + sum_{k>=1} (a_k L / 2) [sinc(v - k) + sinc(v + k)],  v = omega L / (2 pi).
    """
    coeffs = window_coefficients(window)
    v = np.asarray(omega, dtype=np.float64) * L / TWO_PI
    W = coeffs[0] * L * np.sinc(v)
    for k, a in enumerate(coeffs[1:], start=1):
        W = W + 0.5 * a * L * (np.sinc(v - k) + np.sinc(v + k))
    return W


def hann_response(omega: np.ndarray | float, L: float) -> np.ndarray | float:
    return window_response(omega, L, "hann")


def measure_window_response(L: float, window: str = "hann") -> Dict[str, Any]:
    """
    Mede numericamente a resposta: ganho W(0), FWHM do módulo, primeiro zero (varredura em v)
    e maior lóbulo lateral entre o primeiro zero e v = primeiro zero + 6.
    """
    unit = TWO_PI / L
    W0 = float(window_response(0.0, L, window))
    v = np.linspace(0.0, 12.0, 240001)
    Wv = np.asarray(window_response(v * unit, L, window))
    sign_change = np.where(np.sign(Wv[1:]) != np.sign(Wv[:-1]))[0]
    if len(sign_change) == 0:
        raise ValueError("Primeiro zero da resposta não encontrado em v <= 12.")
    v_null = float(brentq(lambda x: float(window_response(x * unit, L, window)), v[sign_change[0]], v[sign_change[0] + 1]))
    half = brentq(lambda om: abs(window_response(om, L, window)) - 0.5 * W0, 1e-9 * unit, v_null * unit)
    side_v = np.linspace(v_null, v_null + 6.0, 60001)
    side = float(np.max(np.abs(window_response(side_v * unit, L, window))))
    return {
        "window": window,
        "gain_W0": W0,
        "fwhm": float(2.0 * half),
        "fwhm_in_units_2pi_over_L": float(2.0 * half / unit),
        "first_null_offset": v_null * unit,
        "first_null_in_units_2pi_over_L": v_null,
        "sidelobe_level_db": float(20.0 * math.log10(side / W0)),
        "reference_resolution_2pi_over_L": unit,
    }


def measure_hann_response(L: float) -> Dict[str, Any]:
    return measure_window_response(L, "hann")


# ---------------------------------------------------------------------------
# Densidade média
# ---------------------------------------------------------------------------

def d_bar_theta(E: np.ndarray) -> np.ndarray:
    """
    Densidade média exata derivada da fase de Riemann-Siegel (DLMF 25.10):
    d/dE [1 + theta(E)/pi] = (1/2pi) [Re psi(1/4 + iE/2) - log pi].
    """
    E = np.asarray(E, dtype=np.float64)
    return (np.real(digamma(0.25 + 0.5j * E)) - math.log(math.pi)) / TWO_PI


# ---------------------------------------------------------------------------
# Transformadas: soma direta (referência) e NUFFT tipo 1 (produção)
# ---------------------------------------------------------------------------

def direct_exponential_sum(
    points: np.ndarray, coeffs: np.ndarray, t_values: np.ndarray, chunk: int = 256
) -> np.ndarray:
    """Referência O(N K): S(t) = sum_j c_j e^{-i u_j t}, em blocos de t."""
    points = np.asarray(points, dtype=np.float64)
    coeffs = np.asarray(coeffs, dtype=np.complex128)
    t_values = np.atleast_1d(np.asarray(t_values, dtype=np.float64))
    out = np.empty(len(t_values), dtype=np.complex128)
    for i in range(0, len(t_values), chunk):
        tc = t_values[i:i + chunk]
        out[i:i + chunk] = np.exp(-1j * np.outer(tc, points)) @ coeffs
    return out


def nufft_uniform_t(
    points: np.ndarray,
    coeffs: np.ndarray,
    t_start: float,
    dt: float,
    n_t: int,
    oversampling: float = 2.0,
    spread_half_width: int = 12,
) -> np.ndarray:
    """
    NUFFT tipo 1 com kernel gaussiano (Greengard & Lee, SIAM Review 46, 2004) para uma malha uniforme em t:
        S(t_k) = sum_j c_j exp(-i u_j t_k),  t_k = t_start + k dt,  k = 0..n_t-1.
    Não exige malha uniforme em u. Precisão ~1e-12 relativa com R = 2 e meia-largura 12;
    a precisão efetiva é verificada contra `direct_exponential_sum` nos testes e em cada execução.
    """
    u = np.asarray(points, dtype=np.float64)
    c = np.asarray(coeffs, dtype=np.complex128)
    M = int(n_t) + (int(n_t) % 2)  # número par de modos
    k_shift = M // 2
    t_mid = t_start + k_shift * dt
    # e^{-i u t_k} = e^{-i u t_mid} e^{-i (k - M/2) (u dt)}
    c_eff = c * np.exp(-1j * u * t_mid)
    x = np.mod(u * dt, TWO_PI)

    Mr = int(math.ceil(oversampling * M))
    Mr += Mr % 2
    R = Mr / M
    msp = int(spread_half_width)
    tau = math.pi * msp / (M * M * R * (R - 0.5))
    h = TWO_PI / Mr

    grid = np.zeros(Mr, dtype=np.complex128)
    base = np.floor(x / h).astype(np.int64)
    offsets = np.arange(-msp + 1, msp + 1, dtype=np.int64)
    for start in range(0, len(x), 4096):
        sl = slice(start, start + 4096)
        idx = base[sl, None] + offsets[None, :]
        dist = x[sl, None] - idx * h
        vals = c_eff[sl, None] * np.exp(-dist * dist / (4.0 * tau))
        np.add.at(grid, np.mod(idx, Mr).ravel(), vals.ravel())

    fft_vals = np.fft.fft(grid) / Mr  # F_tau(k) = (1/Mr) sum_m g_m e^{-i k 2 pi m / Mr}
    k_modes = np.arange(M) - k_shift
    Fk = fft_vals[np.mod(k_modes, Mr)]
    result = math.sqrt(math.pi / tau) * np.exp(k_modes.astype(np.float64) ** 2 * tau) * Fk
    return result[:n_t]


def gauss_legendre_panels(A: float, B: float, panel_length: float, order: int = 8) -> Tuple[np.ndarray, np.ndarray]:
    """Quadratura composta de Gauss-Legendre com painéis alinhados às bordas [A, B]."""
    n_panels = max(1, int(math.ceil((B - A) / panel_length)))
    edges = np.linspace(A, B, n_panels + 1)
    xg, wg = np.polynomial.legendre.leggauss(order)
    half = 0.5 * np.diff(edges)
    mid = 0.5 * (edges[:-1] + edges[1:])
    nodes = (mid[:, None] + half[:, None] * xg[None, :]).ravel()
    weights = (half[:, None] * wg[None, :]).ravel()
    return nodes, weights


def smooth_density(E: np.ndarray, density: str) -> np.ndarray:
    if density == "rvm":
        return d_bar_rvm(E)
    if density == "theta":
        return d_bar_theta(E)
    raise ValueError(f"Densidade média desconhecida: {density}")


class OscillatoryTransform:
    """
    Instrumento F_w(t) numa janela de energia [A, B] e numa malha uniforme de t.
    Guarda a malha, o centro E_c, as quadraturas e os diagnósticos de convergência.
    """

    def __init__(
        self,
        A: float,
        B: float,
        t_min: float,
        t_max: float,
        points_per_fwhm: float = 8.0,
        panel_length: float = 0.5,
        quad_order: int = 8,
        density: str = "rvm",
        window: str = "hann",
    ):
        if not (B > A > TWO_PI):
            raise ValueError("A janela deve satisfazer B > A > 2 pi.")
        window_coefficients(window)
        if density not in ("rvm", "theta"):
            raise ValueError(f"Densidade média não implementada: {density!r}")
        self.window = window
        self.A, self.B = float(A), float(B)
        self.L = self.B - self.A
        self.E_c = 0.5 * (self.A + self.B)
        self.response = measure_window_response(self.L, window)
        self.dt = self.response["fwhm"] / points_per_fwhm
        self.n_t = int(math.floor((t_max - t_min) / self.dt)) + 1
        self.t_grid = t_min + self.dt * np.arange(self.n_t)
        self.density = density
        self.panel_length = panel_length
        self.quad_order = quad_order
        self._quad_nodes, self._quad_weights = gauss_legendre_panels(self.A, self.B, panel_length, quad_order)
        self._quad_coeffs = (
            window_values(self._quad_nodes, self.A, self.B, window)
            * smooth_density(self._quad_nodes, density)
            * self._quad_weights
        )
        self.smooth = nufft_uniform_t(self._quad_nodes - self.E_c, self._quad_coeffs, self.t_grid[0], self.dt, self.n_t)

    # Termo discreto --------------------------------------------------------
    def _select(self, levels: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        levels = np.asarray(levels, dtype=np.float64)
        sel = levels[(levels >= self.A) & (levels <= self.B)]
        if len(sel) == 0:
            raise ValueError("Nenhum nível na janela de energia.")
        return sel - self.E_c, window_values(sel, self.A, self.B, self.window)

    def transform(self, levels: np.ndarray) -> np.ndarray:
        """F_w na malha completa via NUFFT."""
        u, w = self._select(levels)
        return nufft_uniform_t(u, w.astype(np.complex128), self.t_grid[0], self.dt, self.n_t) - self.smooth

    def evaluate(self, levels: np.ndarray, t_values: np.ndarray) -> np.ndarray:
        """F_w em pontos arbitrários de t por soma direta (referência e refinamento local)."""
        u, w = self._select(levels)
        disc = direct_exponential_sum(u, w, t_values)
        smooth = direct_exponential_sum(self._quad_nodes - self.E_c, self._quad_coeffs, t_values, chunk=16)
        return disc - smooth

    # Diagnósticos ---------------------------------------------------------
    def diagnostics(self, levels: np.ndarray, n_check: int = 64, seed: int = 0) -> Dict[str, Any]:
        """
        Verificações exigidas pela Etapa 7:
        - NUFFT vs soma direta em amostra de t;
        - convergência da quadratura (painel pela metade);
        - sensibilidade à densidade média alternativa (theta).
        """
        rng = np.random.default_rng(seed)
        idx = np.sort(rng.choice(self.n_t, size=min(n_check, self.n_t), replace=False))
        F_grid = self.transform(levels)
        F_direct = self.evaluate(levels, self.t_grid[idx])
        nufft_err = float(np.max(np.abs(F_grid[idx] - F_direct)))

        nodes2, weights2 = gauss_legendre_panels(self.A, self.B, 0.5 * self.panel_length, self.quad_order)
        coeffs2 = window_values(nodes2, self.A, self.B, self.window) * smooth_density(nodes2, self.density) * weights2
        smooth2 = nufft_uniform_t(nodes2 - self.E_c, coeffs2, self.t_grid[0], self.dt, self.n_t)
        quad_err = float(np.max(np.abs(smooth2 - self.smooth)))

        alt = "theta" if self.density == "rvm" else "rvm"
        coeffs_alt = window_values(self._quad_nodes, self.A, self.B, self.window) * smooth_density(self._quad_nodes, alt) * self._quad_weights
        smooth_alt = nufft_uniform_t(self._quad_nodes - self.E_c, coeffs_alt, self.t_grid[0], self.dt, self.n_t)
        density_diff = float(np.max(np.abs(smooth_alt - self.smooth)))

        return {
            "n_t": self.n_t,
            "dt": self.dt,
            "points_per_fwhm": self.response["fwhm"] / self.dt,
            "max_abs_F": float(np.max(np.abs(F_grid))),
            "nufft_vs_direct_max_abs_error": nufft_err,
            "quadrature_halving_max_abs_change": quad_err,
            "density_rvm_vs_theta_max_abs_change": density_diff,
            "quadrature_nodes": int(len(self._quad_nodes)),
        }

    def to_metadata(self) -> Dict[str, Any]:
        return {
            "A": self.A,
            "B": self.B,
            "E_c": self.E_c,
            "L": self.L,
            "t_min": float(self.t_grid[0]),
            "t_max": float(self.t_grid[-1]),
            "dt": self.dt,
            "n_t": self.n_t,
            "density": self.density,
            "quadrature": {"panel_length": self.panel_length, "order": self.quad_order},
            "window": self.window,
            "response": self.response,
        }


# ---------------------------------------------------------------------------
# Detector sem catálogo
# ---------------------------------------------------------------------------
#
# Observação registrada no piloto de desenvolvimento: para os zeros, |F_w| entre linhas
# é ordens de grandeza menor que as flutuações dos controles, porque a fórmula explícita
# é uma identidade (o "fundo" é vazamento determinístico pelos lóbulos laterais). Uma
# escala de ruído estimada nos próprios dados torna lóbulos laterais "significativos".
# Por isso a escala de ruído vem do ensemble nulo, calculado sem catálogo aritmético.

def null_noise_profile(null_transforms: List[np.ndarray] | np.ndarray, t_grid: np.ndarray, smooth_window: float = 0.05) -> np.ndarray:
    """
    Escala RMS nula sigma(t) = sqrt(media_b |F_b(t)|^2), suavizada por média móvel de largura
    `smooth_window` em t. Deve ser estimada num conjunto de realizações independente daquele
    usado para a distribuição do máximo.
    """
    arr = np.asarray(null_transforms)
    power = np.mean(np.abs(arr) ** 2, axis=0)
    dt = float(t_grid[1] - t_grid[0])
    win = max(1, int(round(smooth_window / dt))) | 1
    kernel = np.ones(win) / win
    padded = np.pad(power, win // 2, mode="reflect")
    smooth = np.convolve(padded, kernel, mode="valid")
    return np.sqrt(smooth)


def normalized_modulus(F: np.ndarray, noise_rms: np.ndarray) -> np.ndarray:
    return np.abs(F) / np.maximum(noise_rms, 1e-300)


def max_statistic(F: np.ndarray, noise_rms: np.ndarray) -> float:
    """Máximo de |F|/sigma ao longo da faixa: estatística para correção pela seleção (FWER)."""
    return float(np.max(normalized_modulus(F, noise_rms)))


def detect_blind_peaks(
    t_grid: np.ndarray,
    F: np.ndarray,
    fwhm: float,
    noise_rms: np.ndarray,
    candidate_z: float = 3.0,
    evaluator: Callable[[np.ndarray], np.ndarray] | None = None,
) -> List[Dict[str, Any]]:
    """
    Candidatos a linhas espectrais sem qualquer catálogo.

    ESTATÍSTICA DE DECISÃO (m3-v3): `z` = |F(t_k)| / sigma_nulo(t_k) no ponto da MALHA do máximo local.
    É exatamente a mesma grandeza usada em `max_statistic` para os controles e para os sinais
    sintéticos, com ou sem `evaluator`. O refinamento (posição parabólica e amplitude por soma direta,
    se `evaluator` for dado) serve apenas para localização e apresentação (`z_refined`) e nunca entra
    em limiares, valores-p ou contagens.
    """
    t_grid = np.asarray(t_grid, dtype=np.float64)
    dt = float(t_grid[1] - t_grid[0])
    mod = np.abs(F)
    z = normalized_modulus(F, noise_rms)

    distance = max(1, int(round(fwhm / dt)))
    idx, _ = find_peaks(z, height=candidate_z, distance=distance)
    if len(idx) == 0:
        return []

    logm = np.log(np.maximum(mod, 1e-300))
    delta = np.zeros(len(idx))
    inner = (idx > 0) & (idx < len(mod) - 1)
    i_in = idx[inner]
    y0, y1, y2 = logm[i_in - 1], logm[i_in], logm[i_in + 1]
    denom = y0 - 2.0 * y1 + y2
    d = np.zeros(len(i_in))
    ok = denom < 0
    d[ok] = 0.5 * (y0[ok] - y2[ok]) / denom[ok]
    delta[inner] = np.clip(d, -0.5, 0.5)
    t_ref = t_grid[idx] + delta * dt

    amp = evaluator(t_ref) if evaluator is not None else F[idx]
    sigma_ref = np.interp(t_ref, t_grid, noise_rms)

    peaks = []
    for k in range(len(idx)):
        peaks.append({
            "grid_index": int(idx[k]),
            "grid_period": float(t_grid[idx[k]]),
            "period": float(t_ref[k]),
            "amplitude_real": float(np.real(amp[k])),
            "amplitude_imag": float(np.imag(amp[k])),
            "modulus": float(np.abs(amp[k])),
            "phase_rad": float(np.angle(amp[k])),
            "null_noise_rms": float(noise_rms[idx[k]]),
            "z": float(z[idx[k]]),
            "z_refined": float(np.abs(amp[k]) / sigma_ref[k]),
        })
    return peaks


def calibrate_threshold(null_max: np.ndarray, alpha: float) -> float:
    """
    Limiar FWER: menor s com (1 + #{max_nulo >= s}) / (B + 1) <= alpha.
    Retorna +inf se B for pequeno demais para atingir alpha.
    """
    arr = np.sort(np.asarray(null_max, dtype=np.float64))
    B = len(arr)
    k = int(math.floor(alpha * (B + 1) + 1e-9)) - 1  # número máximo de nulos permitidos >= s
    if k < 0:
        return float("inf")
    if k >= B:
        return 0.0
    return float(np.nextafter(arr[B - 1 - k], np.inf))


def adjusted_p_values(values: np.ndarray, null_max: np.ndarray) -> np.ndarray:
    """p ajustado pela seleção: (1 + #{max_nulo >= z}) / (B + 1)."""
    null_sorted = np.sort(np.asarray(null_max, dtype=np.float64))
    B = len(null_sorted)
    values = np.asarray(values, dtype=np.float64)
    n_geq = B - np.searchsorted(null_sorted, values, side="left")
    return (1.0 + n_geq) / (B + 1.0)


def threshold_interval(null_max: np.ndarray, alpha: float, confidence: float = 0.95) -> Dict[str, Any]:
    """
    Intervalo de confiança livre de distribuição para o quantil (1 - alpha) do máximo nulo,
    por estatísticas de ordem: com K ~ Binomial(B, 1 - alpha) o número de máximos abaixo do
    quantil verdadeiro, X_(l) <= q <= X_(u) tem probabilidade P(l <= K <= u - 1) >= confidence.

    Regra de decisão m4-v1 (três categorias, sem aumentar simulações a posteriori):
        z >  X_(u)          -> "detected"
        X_(l) <= z <= X_(u) -> "inconclusive" (inconclusivo quanto à detecção significativa)
        z <  X_(l)          -> "not_detected"
    """
    from scipy.stats import binom

    arr = np.sort(np.asarray(null_max, dtype=np.float64))
    B = len(arr)
    p = 1.0 - alpha
    tail = 0.5 * (1.0 - confidence)
    l = int(binom.ppf(tail, B, p))            # P(K <= l - 1) <= tail  (aprox. por ppf)
    while l > 0 and binom.cdf(l - 1, B, p) > tail:
        l -= 1
    u = int(binom.ppf(1.0 - tail, B, p)) + 1  # P(K >= u) <= tail
    while u <= B and binom.sf(u - 1, B, p) > tail:
        u += 1
    l = max(l, 1)
    u = min(u, B)
    coverage = float(binom.cdf(u - 1, B, p) - binom.cdf(l - 1, B, p))
    return {
        "B": B,
        "alpha": alpha,
        "confidence_requested": confidence,
        "coverage_exact": coverage,
        "order_low": l,
        "order_high": u,
        "z_low": float(arr[l - 1]),
        "z_high": float(arr[u - 1]),
        "point_threshold": calibrate_threshold(arr, alpha),
    }


def classify_detection(z: float, interval: Dict[str, Any]) -> str:
    if z > interval["z_high"]:
        return "detected"
    if z < interval["z_low"]:
        return "not_detected"
    return "inconclusive"
