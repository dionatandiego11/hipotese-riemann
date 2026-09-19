"""
Zeros de L(s, χ) para os caracteres reais primitivos do controle `ctrl-dirichlet-v1`.

Implementa o §4 de DECLARACAO_DIRICHLET.md (SHA-256 e6cb8ab8…) com a justificativa de
D1_DERIVACAO_DIRICHLET.md §2 (SHA-256 f07972a4…):

  Z_χ(t) = e^{iθ_χ(t)} L(½ + it, χ),   θ_χ(t) = arg Γ(¼ + κ/2 + it/2) + (t/2) log(q/π),
  L(s, χ) = q^{−s} Σ_{a=1}^{q} χ(a) ζ(s, a/q)   (zeta de Hurwitz, mpmath, ≥ 30 dígitos).

Z_χ é real porque ε(χ) = 1 (D1 §§1–2). Zeros = trocas de sinal numa varredura com passo
≤ 1/8 do espaçamento médio 2π/log(qt/2π), refinadas (Illinois) até |Δt| ≤ 1e-10.
Verificações V1–V4 da declaração em `verificacoes`; pontos de V4 pelo Adendo 1 (ADENDO_DIRICHLET_1.md).

Não edita nem importa o código congelado de m3/m4. Uso (a partir da raiz do repositório):

  .venv/bin/python3 results/etapa11_6_controles/dirichlet/dirichlet_zeros.py \
      --carater chi_m4 --n 500 --saida <pasta>
  .venv/bin/python3 results/etapa11_6_controles/dirichlet/dirichlet_zeros.py \
      --reavaliar-v4 <pasta>/manifest_chi_m4_500.json

Salvamento e retomada (ADENDO_DIRICHLET_2.md): o progresso vai para <pasta>/progresso_<carater>_<n>.json a cada 25
zeros ou 120 s e ao receber Ctrl+C/SIGTERM; rodar o mesmo comando de novo retoma do ponto gravado.

A versão usada nos pilotos de 19/09/2026 (SHA-256 0f16b4c5…) está preservada em versoes/.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import signal
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple

import mpmath as mp
import numpy as np

# ---------------------------------------------------------------------------
# Caracteres (declaração §2)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Character:
    name: str
    q: int
    kappa: int
    residues: Dict[int, int] = field(hash=False)

    def __call__(self, n: int) -> int:
        return self.residues.get(n % self.q, 0)

    @property
    def a(self) -> float:
        """a = ¼ + κ/2 (D1)."""
        return 0.25 + 0.5 * self.kappa

    def values_list(self) -> List[int]:
        """χ(0), χ(1), …, χ(q−1), formato de `mpmath.dirichlet`."""
        return [self(n) for n in range(self.q)]


CHARACTERS: Dict[str, Character] = {
    # χ_{−4}: Kronecker (−4/·); ímpar (κ = 1)
    "chi_m4": Character("chi_m4", q=4, kappa=1, residues={1: 1, 3: -1}),
    # χ_5: Legendre (·/5); par (κ = 0)
    "chi_5": Character("chi_5", q=5, kappa=0, residues={1: 1, 4: 1, 2: -1, 3: -1}),
}

REFINE_TOL = 1e-10          # |Δt| final do refinamento (declaração §4, item 3)
STEP_FRACTION = 1.0 / 8.0   # passo ≤ 1/8 do espaçamento médio (declaração §4, item 3)
DEFAULT_DPS = 30            # precisão de trabalho ≥ 30 dígitos (declaração §4, item 2)
ILLINOIS_MAX = 100          # Adendo 2, M1.1
BISECT_MAX = 100            # Adendo 2, M1.2


# ---------------------------------------------------------------------------
# Funções analíticas
# ---------------------------------------------------------------------------


def theta_chi(t, ch: Character):
    """θ_χ(t) = arg Γ(a + it/2) + (t/2) log(q/π), com arg contínuo (Im loggamma), θ_χ(0) = 0."""
    t = mp.mpf(t)
    return mp.im(mp.loggamma(mp.mpf(ch.a) + 0.5j * t)) + 0.5 * t * mp.log(mp.mpf(ch.q) / mp.pi)


def L_hurwitz(s, ch: Character):
    """L(s, χ) = q^{−s} Σ_{a=1}^{q} χ(a) ζ(s, a/q)."""
    q = mp.mpf(ch.q)
    return mp.power(q, -s) * mp.fsum(ch(a) * mp.zeta(s, mp.mpf(a) / q) for a in range(1, ch.q) if ch(a) != 0)


def L_dirichlet(s, ch: Character):
    """Segunda avaliação (V3): `mpmath.dirichlet` com a lista de valores de χ."""
    return mp.dirichlet(s, ch.values_list())


def Z_complex(t, ch: Character, L=L_hurwitz):
    t = mp.mpf(t)
    return mp.exp(1j * theta_chi(t, ch)) * L(mp.mpf("0.5") + 1j * t, ch)


def Z_real(t, ch: Character, L=L_hurwitz) -> mp.mpf:
    return mp.re(Z_complex(t, ch, L))


def mean_spacing(t: float, q: int) -> float:
    """
    Espaçamento médio 2π/log(qt/2π). Onde log(qt/2π) < 1 (abaixo do primeiro zero para q = 4, 5)
    usa-se 2π, que dá passo menor ou igual ao da fórmula da declaração.
    """
    lg = math.log(q * t / (2 * math.pi)) if t > 0 else -1.0
    return 2 * math.pi / max(lg, 1.0)


def smooth_count(T: float, ch: Character) -> float:
    """θ_χ(T)/π = N(T, χ) − S(T, χ) + S(0, χ) (D1 §5; Teorema 14.5 de Montgomery–Vaughan)."""
    with mp.workdps(DEFAULT_DPS):
        return float(theta_chi(T, ch) / mp.pi)


# ---------------------------------------------------------------------------
# Busca de zeros
# ---------------------------------------------------------------------------


@dataclass
class ScanStats:
    evaluations: int = 0
    refinements: int = 0
    gap_rescans: int = 0
    seconds: float = 0.0
    max_refine_iterations: int = 0     # Adendo 2, M1.5
    bisection_fallbacks: int = 0       # Adendo 2, M1.5


class RefinementError(RuntimeError):
    """Adendo 2, M1.4: intervalo não convergido até REFINE_TOL; a execução para sem gravar o zero."""


class ScanState:
    """
    Estado mínimo e consistente de uma varredura (Adendo 2, M2): início da próxima iteração (a, Z(a)) e o número de zeros
    aceitos até ali. Atualizado só entre iterações, de modo que um instantâneo nunca inclui um zero pela metade.
    """

    def __init__(self, a: float, fa: float, n_zeros: int):
        self.a, self.fa, self.n_zeros = a, fa, n_zeros


class ZeroFinder:
    def __init__(self, ch: Character, dps: int = DEFAULT_DPS, step_fraction: float = STEP_FRACTION,
                 illinois_max: int = ILLINOIS_MAX, bisect_max: int = BISECT_MAX):
        self.ch = ch
        self.dps = dps
        self.step_fraction = step_fraction
        self.illinois_max = illinois_max
        self.bisect_max = bisect_max
        self.stats = ScanStats()

    def Z(self, t: float) -> float:
        self.stats.evaluations += 1
        with mp.workdps(self.dps):
            return float(Z_real(t, self.ch))

    def step(self, t: float) -> float:
        return self.step_fraction * mean_spacing(t, self.ch.q)

    def refine(self, a: float, fa: float, b: float, fb: float) -> float:
        """
        Illinois (regula falsi modificada) até b − a ≤ REFINE_TOL, com no máximo `illinois_max` iterações (idêntico ao
        código dos pilotos nesse trecho); depois, bisseção pura por até `bisect_max` iterações. Aceita só intervalo com
        b − a ≤ REFINE_TOL e troca de sinal (ou Z exatamente nulo); caso contrário, RefinementError (Adendo 2, M1).
        """
        self.stats.refinements += 1
        side = 0
        it = 0
        while it < self.illinois_max and b - a > REFINE_TOL:
            it += 1
            c = (a * fb - b * fa) / (fb - fa)
            if not (a < c < b):
                c = 0.5 * (a + b)
            # garante contração mesmo quando regula falsi estagna numa ponta
            if min(c - a, b - c) < 0.25 * REFINE_TOL:
                c = 0.5 * (a + b)
            fc = self.Z(c)
            if fc == 0.0:
                self.stats.max_refine_iterations = max(self.stats.max_refine_iterations, it)
                return c
            if (fc > 0) == (fb > 0):
                b, fb = c, fc
                if side == -1:
                    fa *= 0.5
                side = -1
            else:
                a, fa = c, fc
                if side == 1:
                    fb *= 0.5
                side = 1
        if b - a > REFINE_TOL:
            self.stats.bisection_fallbacks += 1
            k = 0
            while k < self.bisect_max and b - a > REFINE_TOL:
                k += 1
                it += 1
                c = 0.5 * (a + b)
                fc = self.Z(c)
                if fc == 0.0:
                    self.stats.max_refine_iterations = max(self.stats.max_refine_iterations, it)
                    return c
                if (fc > 0) == (fb > 0):
                    b, fb = c, fc
                else:
                    a, fa = c, fc
        self.stats.max_refine_iterations = max(self.stats.max_refine_iterations, it)
        if not (b - a <= REFINE_TOL and (fa > 0) != (fb > 0)):
            raise RefinementError(f"{self.ch.name}: refinamento não convergiu em [{a!r}, {b!r}] (largura {b - a:.3e}, "
                                  f"{it} iterações)")
        return 0.5 * (a + b)

    def scan(self, t_start: float, t_stop: Optional[float] = None, n_max: Optional[int] = None,
             step_scale: float = 1.0, zeros: Optional[List[float]] = None, fa_start: Optional[float] = None,
             on_step: Optional[Callable[[ScanState, List[float]], None]] = None) -> List[float]:
        """
        Zeros em (t_start, t_stop] ou até n_max zeros no total. Com `zeros` e `fa_start`, continua uma varredura gravada
        (Adendo 2, M2.4): a sequência de pontos depende só de t_start, então o resultado é o mesmo da execução contínua.
        `on_step(estado, zeros)` é chamado no início de cada iteração.
        """
        if t_stop is None and n_max is None:
            raise ValueError("informe t_stop ou n_max")
        zeros = [] if zeros is None else list(zeros)
        t0 = time.perf_counter()
        a = t_start
        fa = self.Z(a)
        if fa_start is not None and fa != fa_start:
            raise RuntimeError(f"retomada: Z({a!r}) = {fa!r} difere do valor gravado {fa_start!r}")
        try:
            while True:
                if on_step is not None:
                    on_step(ScanState(a, fa, len(zeros)), zeros)
                if n_max is not None and len(zeros) >= n_max:
                    break
                b = a + step_scale * self.step(a)
                if t_stop is not None and b > t_stop:
                    b = t_stop
                fb = self.Z(b)
                if fa == 0.0:
                    zeros.append(a)
                elif (fa > 0) != (fb > 0) and fb != 0.0:
                    zeros.append(self.refine(a, fa, b, fb))
                if n_max is not None and len(zeros) >= n_max:
                    break
                if t_stop is not None and b >= t_stop:
                    break
                a, fa = b, fb
        finally:
            self.stats.seconds += time.perf_counter() - t0
        return zeros[:n_max] if n_max is not None else zeros

    def rescan_large_gaps(self, zeros: List[float], factor: float = 4.0) -> Tuple[List[float], List[Dict]]:
        """V1 (parte 2): intervalos > factor × espaçamento médio são reamostrados com passo pela metade."""
        out = list(zeros)
        log = []
        for k in range(len(zeros) - 1):
            lo, hi = zeros[k], zeros[k + 1]
            if hi - lo > factor * mean_spacing(0.5 * (lo + hi), self.ch.q):
                self.stats.gap_rescans += 1
                inner = self.scan(lo + 10 * REFINE_TOL, t_stop=hi - 10 * REFINE_TOL, step_scale=0.5)
                log.append({"interval": [lo, hi], "new_zeros": inner})
                out.extend(inner)
        return sorted(out), log


# ---------------------------------------------------------------------------
# Verificações V1–V4 (declaração §4)
# ---------------------------------------------------------------------------


def v1_completeness(zeros: List[float], ch: Character, block_size: int = 3000, tol: float = 3.0) -> Dict:
    edges = list(range(block_size, len(zeros) + 1, block_size))
    if not edges or edges[-1] != len(zeros):
        edges.append(len(zeros))
    rows = []
    for k in edges:
        T = 0.5 * (zeros[k - 1] + zeros[k]) if k < len(zeros) else zeros[k - 1] + 1e-6
        nbar = smooth_count(T, ch)
        rows.append({"n_found": k, "T": T, "theta_over_pi": nbar, "difference": k - nbar, "ok": abs(k - nbar) <= tol})
    return {"tolerance": tol, "edges": rows, "passed": all(r["ok"] for r in rows),
            "note": "N(T,χ) = θ_χ(T)/π + S(T,χ) − S(0,χ); S não é estimado (convenção B da declaração)."}


def v2_bounds(zeros: List[float], first: int, last: int) -> Tuple[float, float]:
    lo = zeros[first - 2] + 10 * REFINE_TOL if first > 1 else 0.0
    hi = zeros[last - 1] + 0.5 * (zeros[last] - zeros[last - 1]) if last < len(zeros) else zeros[last - 1] + 1e-6
    return lo, hi


def v2_compare(zeros: List[float], again: List[float], first: int, last: int, stats: ScanStats) -> Dict:
    ref = zeros[first - 1:last]
    same_count = len(again) == len(ref)
    max_diff = float(np.max(np.abs(np.array(again) - np.array(ref)))) if same_count and ref else None
    return {"indices": [first, last], "n_reference": len(ref), "n_recomputed": len(again), "same_count": same_count,
            "max_abs_difference": max_diff, "passed": bool(same_count and max_diff is not None and max_diff <= 1e-9),
            "evaluations": stats.evaluations, "seconds": stats.seconds}


def v2_stability(zeros: List[float], ch: Character, first: int, last: int, dps: int = DEFAULT_DPS) -> Dict:
    """Recalcula os zeros de índices first..last (1-based) com passo pela metade e compara (sem retomada)."""
    finder = ZeroFinder(ch, dps=dps, step_fraction=STEP_FRACTION / 2.0)
    lo, hi = v2_bounds(zeros, first, last)
    again = finder.scan(lo, t_stop=hi)
    return v2_compare(zeros, again, first, last, finder.stats)


def _sign_change(fun, t: float, delta: float = 1e-8) -> bool:
    return (fun(t - delta) > 0) != (fun(t + delta) > 0)


def v3_second_evaluation(zeros: List[float], ch: Character, n_sample: int = 50, seed: int = 20260917) -> Dict:
    rng = np.random.default_rng(seed)
    idx = np.sort(rng.choice(len(zeros), size=min(n_sample, len(zeros)), replace=False))
    rows = []
    for i in idx:
        g = zeros[int(i)]
        with mp.workdps(40):
            ok_dir = _sign_change(lambda t: Z_real(t, ch, L_dirichlet), g)
        with mp.workdps(60):
            ok_60 = _sign_change(lambda t: Z_real(t, ch, L_hurwitz), g)
        rows.append({"index": int(i) + 1, "gamma": g, "dirichlet_40": ok_dir, "hurwitz_60": ok_60})
    return {"seed": seed, "sample": rows, "passed": all(r["dirichlet_40"] and r["hurwitz_60"] for r in rows),
            "note": "mpmath.dirichlet também usa somas de Hurwitz: confere implementação e precisão, não método independente."}


def v4_points(zeros: List[float], n_points: int = 10) -> List[float]:
    """
    Adendo 1 (ADENDO_DIRICHLET_1.md, SHA-256 6ee78368…), §3: para cada s_j = linspace(10, t_max, n_points), o ponto
    médio entre os dois zeros consecutivos que cercam s_j; abaixo do primeiro zero, o ponto médio entre 10 e ele; no
    último zero ou acima dele, o ponto médio entre os dois últimos. Evita avaliar Z_χ num zero, onde |Z_χ| ≈ 0 torna a
    razão |Im Z|/|Z| sem sentido (falha do piloto de 19/09/2026).
    """
    z = np.asarray(zeros, dtype=float)
    out = []
    for s in np.linspace(10.0, max(float(z[-1]), 11.0), n_points):
        j = int(np.searchsorted(z, s, side="right"))  # z[j-1] <= s < z[j]
        if j == 0:
            out.append(0.5 * (10.0 + z[0]) if z[0] > 10.0 else 0.5 * z[0])
        elif j >= len(z):
            out.append(0.5 * (z[-2] + z[-1]))
        else:
            out.append(0.5 * (z[j - 1] + z[j]))
    return out


def v4_reality(ch: Character, zeros: List[float], n_points: int = 10, rel_tol: float = 1e-20) -> Dict:
    rows = []
    for t in v4_points(zeros, n_points):
        with mp.workdps(DEFAULT_DPS):
            z = Z_complex(float(t), ch)
            rel = float(abs(mp.im(z)) / abs(z)) if z != 0 else 0.0
        rows.append({"t": float(t), "abs_Z": float(abs(z)), "imag_over_abs": rel, "ok": rel <= rel_tol})
    return {"rule": "adendo-1 (pontos médios entre zeros consecutivos)", "rel_tol": rel_tol, "points": rows,
            "passed": all(r["ok"] for r in rows)}


def reevaluate_v4(manifest_path: Path) -> Dict:
    """Adendo 1, §4.3: refaz só V4 a partir de um piloto já gravado, sem recalcular zeros; grava arquivo à parte."""
    manifest_path = Path(manifest_path)
    with open(manifest_path, encoding="utf-8") as f:
        m = json.load(f)
    zpath = manifest_path.parent / m["output_file"]
    if sha256_of(zpath) != m["output_sha256"]:
        raise ValueError(f"{zpath.name}: SHA-256 difere do registrado no manifesto")
    zeros = [float(x) for x in zpath.read_text(encoding="utf-8").split()]
    ch = CHARACTERS[m["character"]["name"]]
    v4 = v4_reality(ch, zeros)
    others = {k: m["checks"][k]["passed"] for k in ("V1", "V2", "V3")}
    out = {
        "protocol": "ctrl-dirichlet-v1",
        "addendum": "ADENDO_DIRICHLET_1.md",
        "addendum_sha256": "6ee78368f371165aa117ffc2e4b6502e2975696d79b5d4509275a14bec7f6586",
        "source_manifest": manifest_path.name, "source_manifest_sha256": sha256_of(manifest_path),
        "zeros_file": zpath.name, "zeros_sha256": m["output_sha256"],
        "V4_original_rule_passed": m["checks"]["V4"]["passed"],
        "V4": v4,
        "V1_V3_from_source": others,
        "all_checks_passed_with_addendum": all(others.values()) and v4["passed"],
        "versions": {"python": platform.python_version(), "mpmath": mp.__version__, "numpy": np.__version__},
        "script_sha256": sha256_of(Path(__file__)),
    }
    name = f"v4_adendo1_{m['character']['name']}_{m['n_zeros']}.json"
    with open(manifest_path.parent / name, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    return out


# ---------------------------------------------------------------------------
# Saída
# ---------------------------------------------------------------------------


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_zeros(path: Path, zeros: List[float]) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        for g in zeros:
            f.write(f"{g:.9f}\n")


ADDENDUM2_SHA256 = "619950467fb0a7e3b47998b93b203dcea23e8db69f19db4b288283199aef8811"
STATE_VERSION = 1


class Interrupted(Exception):
    """SIGINT/SIGTERM recebido; o progresso é gravado antes de sair (Adendo 2, M2.1)."""


def _atomic_write_json(path: Path, obj: Dict) -> None:
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


class RunLock:
    """Adendo 2, M2.5: impede duas execuções com o mesmo alvo na mesma pasta; trava de processo morto é retomada."""

    def __init__(self, path: Path):
        self.path = path

    def __enter__(self):
        if self.path.exists():
            try:
                pid = int(self.path.read_text().strip() or "0")
            except ValueError:
                pid = 0
            if pid and pid != os.getpid() and _pid_alive(pid):
                raise RuntimeError(f"outra execução (PID {pid}) está usando {self.path.name}")
        self.path.write_text(str(os.getpid()))
        return self

    def __exit__(self, *exc):
        try:
            if self.path.read_text().strip() == str(os.getpid()):
                self.path.unlink()
        except FileNotFoundError:
            pass
        return False


def run_params(ch: Character, n: int) -> Dict:
    """Tudo o que precisa ser igual para retomar (Adendo 2, M2.3)."""
    return {"protocol": "ctrl-dirichlet-v1", "character": ch.name, "q": ch.q, "kappa": ch.kappa, "n": n,
            "dps": DEFAULT_DPS, "step_fraction": STEP_FRACTION, "refine_tol": REFINE_TOL,
            "illinois_max": ILLINOIS_MAX, "bisect_max": BISECT_MAX, "state_version": STATE_VERSION,
            "script_sha256": sha256_of(Path(__file__))}


class Checkpointer:
    def __init__(self, path: Path, state: Dict, every_zeros: int, every_seconds: float):
        self.path, self.state = path, state
        self.every_zeros, self.every_seconds = every_zeros, every_seconds
        self.last_n, self.last_t = None, time.monotonic()
        self.pending = None   # (chave, ScanState, lista de zeros viva, finder, extra): copiado só ao gravar
        self.writes = 0

    def _materialize(self) -> None:
        if self.pending is not None:
            key, st, zeros, finder, extra = self.pending
            sec = dict(extra or {})
            sec.update({"a": st.a, "fa": st.fa, "zeros": list(zeros[:st.n_zeros]), "stats": dict(finder.stats.__dict__)})
            self.state[key] = sec

    def save(self) -> None:
        self._materialize()
        self.state["updated"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        _atomic_write_json(self.path, self.state)
        self.writes += 1
        self.last_t = time.monotonic()

    def scan_hook(self, key: str, finder: "ZeroFinder", extra: Optional[Dict] = None,
                  stop_after: Optional[int] = None):
        """Devolve on_step para ZeroFinder.scan: guarda (a, Z(a), n.º de zeros) e grava por contagem ou tempo."""
        def on_step(st: ScanState, zeros: List[float]) -> None:
            self.pending = (key, st, zeros, finder, extra)
            if self.last_n is None:
                self.last_n = st.n_zeros
            if (st.n_zeros - self.last_n >= self.every_zeros) or (time.monotonic() - self.last_t >= self.every_seconds):
                self.save()
                self.last_n = st.n_zeros
            if stop_after is not None and st.n_zeros >= stop_after:   # só para testes (interrupção simulada)
                raise Interrupted("interrupção simulada")
        return on_step

    def end_scan(self) -> None:
        self.pending = None
        self.last_n = None


def _restore_stats(finder: "ZeroFinder", d: Optional[Dict]) -> None:
    if d:
        for k, v in d.items():
            if hasattr(finder.stats, k):
                setattr(finder.stats, k, v)


def run(ch: Character, n: int, out_dir: Path, v2_block: Optional[Tuple[int, int]] = None, every_zeros: int = 25,
        every_seconds: float = 120.0, _stop_after: Optional[Dict[str, int]] = None, _finder_kw: Optional[Dict] = None) -> Dict:
    """
    Cálculo completo com salvamento e retomada (Adendo 2). Fases: scan → gaps → V1 → V2 → V3 → V4 → done.
    Reexecutar o mesmo comando retoma de `progresso_<carater>_<n>.json`.
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    params = run_params(ch, n)
    spath = out_dir / f"progresso_{ch.name}_{n}.json"
    fkw = dict(_finder_kw or {})
    stop = dict(_stop_after or {})
    with RunLock(out_dir / f".lock_{ch.name}_{n}"):
        if spath.exists():
            with open(spath, encoding="utf-8") as f:
                state = json.load(f)
            if state.get("params") != params:
                diff = {k: (state.get("params", {}).get(k), v) for k, v in params.items()
                        if state.get("params", {}).get(k) != v}
                raise RuntimeError(f"retomada recusada: parâmetros diferentes do estado gravado {diff}")
            state["resumes"] = state.get("resumes", 0) + 1
        else:
            state = {"params": params, "phase": "scan", "resumes": 0, "checks": {},
                     "started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
        if state["phase"] == "done":
            with open(out_dir / f"manifest_{ch.name}_{n}.json", encoding="utf-8") as f:
                return json.load(f)
        ck = Checkpointer(spath, state, every_zeros, every_seconds)

        def handler(signum, frame):
            raise Interrupted(f"sinal {signum}")
        old = {sig: signal.signal(sig, handler) for sig in (signal.SIGINT, signal.SIGTERM)}
        try:
            ck.save()
            # --- varredura principal -------------------------------------------------------------------------
            if state["phase"] == "scan":
                finder = ZeroFinder(ch, **fkw)
                sc = state.get("scan")
                if sc:
                    _restore_stats(finder, sc.get("stats"))
                    zeros = finder.scan(sc["a"], n_max=n, zeros=sc["zeros"], fa_start=sc["fa"],
                                        on_step=ck.scan_hook("scan", finder, stop_after=stop.get("scan")))
                else:
                    zeros = finder.scan(0.0, n_max=n, on_step=ck.scan_hook("scan", finder, stop_after=stop.get("scan")))
                ck.end_scan()
                state["scan_result"] = {"zeros": zeros, "stats": dict(finder.stats.__dict__)}
                state.pop("scan", None)
                state["phase"] = "gaps"
                ck.save()
            # --- lacunas (curta; refeita inteira se interrompida) ---------------------------------------------
            if state["phase"] == "gaps":
                finder = ZeroFinder(ch, **fkw)
                _restore_stats(finder, state["scan_result"]["stats"])
                zeros, gap_log = finder.rescan_large_gaps(state["scan_result"]["zeros"])
                zeros = zeros[:n]
                state["final"] = {"zeros": zeros, "gap_log": gap_log, "stats": dict(finder.stats.__dict__)}
                state.pop("scan_result", None)
                write_zeros(out_dir / f"zeros_{ch.name}_{n}.txt", zeros)
                state["phase"] = "V1"
                ck.save()
            zeros = state["final"]["zeros"]
            if v2_block is None:
                v2_block = (max(1, n - 2999), n) if n >= 3000 else (1, n)
            if state["phase"] == "V1":
                state["checks"]["V1"] = v1_completeness(zeros, ch)
                state["phase"] = "V2"
                ck.save()
            if state["phase"] == "V2":
                first, last = v2_block
                lo, hi = v2_bounds(zeros, first, last)
                finder = ZeroFinder(ch, step_fraction=STEP_FRACTION / 2.0, **fkw)
                sc = state.get("v2scan")
                if sc:
                    _restore_stats(finder, sc.get("stats"))
                    again = finder.scan(sc["a"], t_stop=hi, zeros=sc["zeros"], fa_start=sc["fa"],
                                        on_step=ck.scan_hook("v2scan", finder, stop_after=stop.get("v2")))
                else:
                    again = finder.scan(lo, t_stop=hi, on_step=ck.scan_hook("v2scan", finder, stop_after=stop.get("v2")))
                ck.end_scan()
                state["checks"]["V2"] = v2_compare(zeros, again, first, last, finder.stats)
                state.pop("v2scan", None)
                state["phase"] = "V3"
                ck.save()
            if state["phase"] == "V3":
                state["checks"]["V3"] = v3_second_evaluation(zeros, ch)
                state["phase"] = "V4"
                ck.save()
            if state["phase"] == "V4":
                state["checks"]["V4"] = v4_reality(ch, zeros)
                state["phase"] = "manifest"
                ck.save()
            # --- manifesto ------------------------------------------------------------------------------------
            zpath = out_dir / f"zeros_{ch.name}_{n}.txt"
            checks = {k: state["checks"][k] for k in ("V1", "V2", "V3", "V4")}
            manifest = {
                "protocol": "ctrl-dirichlet-v1",
                "declaration_sha256": "e6cb8ab84e1d9665f8c8fcb3c8a450b840dbaec8167b7267b180fe410232edff",
                "d1_sha256": "f07972a49422716256401da58c3756e4807e1f2ed26daef3ee50be98bc8ea11d",
                "addenda": {"ADENDO_DIRICHLET_1.md": "6ee78368f371165aa117ffc2e4b6502e2975696d79b5d4509275a14bec7f6586",
                            "ADENDO_DIRICHLET_2.md": ADDENDUM2_SHA256},
                "character": {"name": ch.name, "q": ch.q, "kappa": ch.kappa, "values": ch.values_list()},
                "n_zeros": len(zeros),
                "gamma_first": zeros[0], "gamma_last": zeros[-1],
                "method": {"L": "Hurwitz (mpmath.zeta(s, a/q))", "dps": DEFAULT_DPS, "step_fraction": STEP_FRACTION,
                           "refine": "Illinois (≤ %d) + bisseção (≤ %d), aceitação estrita" % (ILLINOIS_MAX, BISECT_MAX),
                           "refine_tol": REFINE_TOL},
                "gap_rescans": state["final"]["gap_log"],
                "stats": state["final"]["stats"],
                "checks": checks,
                "all_checks_passed": all(c["passed"] for c in checks.values()),
                "output_file": zpath.name, "output_sha256": sha256_of(zpath),
                "resumes": state["resumes"], "checkpoint_file": spath.name,
                "started": state.get("started"), "finished": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                "versions": {"python": platform.python_version(), "mpmath": mp.__version__, "numpy": np.__version__},
                "script_sha256": params["script_sha256"],
            }
            with open(out_dir / f"manifest_{ch.name}_{n}.json", "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2, ensure_ascii=False)
            state["phase"] = "done"
            ck.save()
            return manifest
        except BaseException:
            ck.save()   # interrupção, falha de refinamento ou outro erro: o último estado consistente fica gravado
            raise
        finally:
            for sig, h in old.items():
                signal.signal(sig, h)


def compute(ch: Character, n: int, out_dir: Path, v2_block: Optional[Tuple[int, int]] = None) -> Dict:
    """Compatibilidade: mesmo que run() com os padrões de salvamento."""
    return run(ch, n, out_dir, v2_block=v2_block)


def verify_refinement(manifest_path: Path, half_width: float = 6e-10) -> Dict:
    """Adendo 2, §4: troca de sinal de Z_χ em [γ̂ − 6·10⁻¹⁰, γ̂ + 6·10⁻¹⁰] para cada zero gravado (9 casas)."""
    manifest_path = Path(manifest_path)
    with open(manifest_path, encoding="utf-8") as f:
        m = json.load(f)
    zpath = manifest_path.parent / m["output_file"]
    if sha256_of(zpath) != m["output_sha256"]:
        raise ValueError(f"{zpath.name}: SHA-256 difere do registrado no manifesto")
    ch = CHARACTERS[m["character"]["name"]]
    zeros = [float(x) for x in zpath.read_text(encoding="utf-8").split()]
    bad = []
    t0 = time.perf_counter()
    for i, g in enumerate(zeros, 1):
        with mp.workdps(DEFAULT_DPS):
            lo, hi = Z_real(g - half_width, ch), Z_real(g + half_width, ch)
        if not ((lo > 0) != (hi > 0) or lo == 0 or hi == 0):
            bad.append({"index": i, "gamma": g, "Z_lo": float(lo), "Z_hi": float(hi)})
    out = {"protocol": "ctrl-dirichlet-v1", "addendum": "ADENDO_DIRICHLET_2.md", "addendum_sha256": ADDENDUM2_SHA256,
           "source_manifest": manifest_path.name, "zeros_file": zpath.name, "zeros_sha256": m["output_sha256"],
           "half_width": half_width, "n_checked": len(zeros), "n_failed": len(bad), "failed": bad,
           "passed": not bad, "seconds": time.perf_counter() - t0, "script_sha256": sha256_of(Path(__file__))}
    with open(manifest_path.parent / f"verificacao_refinamento_{ch.name}_{m['n_zeros']}.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    return out


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--carater", choices=sorted(CHARACTERS))
    p.add_argument("--n", type=int, help="número de zeros (piloto: 500; completo: 12000)")
    p.add_argument("--saida", type=Path)
    p.add_argument("--salvar-a-cada", type=int, default=25, metavar="ZEROS",
                   help="grava o progresso a cada N zeros novos (padrão 25; Adendo 2)")
    p.add_argument("--salvar-segundos", type=float, default=120.0, metavar="S",
                   help="grava o progresso a cada S segundos (padrão 120; Adendo 2)")
    p.add_argument("--reavaliar-v4", type=Path, metavar="MANIFESTO",
                   help="Adendo 1: refaz só V4 de um cálculo já gravado (sem recalcular zeros)")
    p.add_argument("--verificar-refinamento", type=Path, metavar="MANIFESTO",
                   help="Adendo 2, §4: confere troca de sinal em ±6e-10 de cada zero gravado")
    args = p.parse_args(argv)
    if args.reavaliar_v4 is not None:
        r = reevaluate_v4(args.reavaliar_v4)
        print(json.dumps({"V4": r["V4"]["passed"], "V1_V3": r["V1_V3_from_source"],
                          "all_checks_passed_with_addendum": r["all_checks_passed_with_addendum"]}, indent=2))
        return 0 if r["all_checks_passed_with_addendum"] else 1
    if args.verificar_refinamento is not None:
        r = verify_refinement(args.verificar_refinamento)
        print(json.dumps({k: r[k] for k in ("n_checked", "n_failed", "passed", "seconds")}, indent=2))
        return 0 if r["passed"] else 1
    if args.carater is None or args.n is None or args.saida is None:
        p.error("--carater, --n e --saida são obrigatórios (exceto com --reavaliar-v4 ou --verificar-refinamento)")
    t0 = time.perf_counter()
    try:
        m = run(CHARACTERS[args.carater], args.n, args.saida, every_zeros=args.salvar_a_cada,
                every_seconds=args.salvar_segundos)
    except Interrupted as e:
        print(f"Interrompido ({e}). Progresso gravado em {args.saida}/progresso_{args.carater}_{args.n}.json; "
              f"rode o mesmo comando para retomar.", file=sys.stderr)
        return 130
    print(json.dumps({"n_zeros": m["n_zeros"], "gamma_last": m["gamma_last"], "all_checks_passed": m["all_checks_passed"],
                      "checks": {k: v["passed"] for k, v in m["checks"].items()}, "resumes": m.get("resumes", 0),
                      "evaluations": m["stats"]["evaluations"], "seconds_this_session": round(time.perf_counter() - t0, 1)},
                     indent=2))
    return 0 if m["all_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
