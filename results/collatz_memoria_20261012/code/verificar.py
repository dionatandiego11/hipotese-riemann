import csv
import hashlib
import json
import platform
import resource
import sys
import time
import traceback
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))

from collatz.coarse_memory import (
    coupling_bound, holder_one_seminorm, project_probabilities, pull_observable,
    push_probabilities, stationary_probabilities, total_variation,
)
from collatz.congruence_filters import Congruence, evaluate_filters, iterate_filters


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def oracle_projection(depth, level):
    """Média da fórmula de ramos em um período completo, sem usar Q."""
    state = iterate_filters(Congruence(1, 0), depth)
    period = 3 ** max(depth, level)
    out = [F(0) for _ in range(3 ** level)]
    for root in range(1, period + 1):
        out[root % len(out)] += F(3, 4) ** depth * evaluate_filters(state, root) / period
    return out


def main():
    expected = "58f14674d211cd216b3aa3876be697e2b31dda882128e080da73d52ad4adce2d"
    assert sha(HERE / "DECLARACAO.md") == expected
    assert sha(ROOT / "collatz/congruence_filters.py") == "0ac98c2a38960a9e766b3176161d58ef324b19760131ff9a5016aa3d55a53f80"
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    wall = time.perf_counter()
    cpu = time.process_time()
    output = {"estado": "em execução", "classe": "B; controles em aritmética racional exata",
              "data": "2026-10-12", "python": platform.python_version(),
              "declaracao_sha256": expected, "checks": {}, "estacionarias": {}, "mistura": []}
    try:
        stationary = {level: stationary_probabilities(level) for level in range(4)}
        for level, vector in stationary.items():
            assert sum(vector) == 1 and min(vector) >= 0
            assert push_probabilities(vector, level) == vector
            if level:
                assert project_probabilities(vector, level, level - 1) == stationary[level - 1]
            output["estacionarias"][str(level)] = [str(value) for value in vector]
        output["checks"]["estacionarias_massa_equacao_compatibilidade"] = 4

        comparisons = variation = 0
        for level in range(4):
            vector = [F(1, 3 ** level)] * (3 ** level)
            for depth in range(13):
                if depth <= 6:
                    oracle = oracle_projection(depth, level)
                    assert vector == oracle, (level, depth)
                    comparisons += len(vector)
                distance = total_variation(vector, stationary[level])
                bound = coupling_bound(depth, level)
                assert distance <= bound, (level, depth, distance, bound)
                output["mistura"].append({"K": level, "m": depth,
                                          "tv_exata": str(distance), "cota_binomial": str(bound)})
                variation += 1
                assert sum(vector) == 1 and min(vector) >= 0
                vector = push_probabilities(vector, level)
        output["checks"]["componentes_coarse_vs_expansao_completa"] = comparisons
        output["checks"]["cota_acoplamento_variacao_total"] = variation

        holder = 0
        for level in range(1, 4):
            size = 3 ** level
            observables = [[F(a) for a in range(size)]]
            observables += [[F(int(a == residue)) for a in range(size)] for residue in range(size)]
            for observable in observables:
                seminorm = holder_one_seminorm(observable, level)
                transformed = holder_one_seminorm(pull_observable(observable, level), level)
                assert transformed <= F(5, 6) * seminorm
                holder += 1
        output["checks"]["contracao_holder_observaveis"] = holder
        output["estado"] = "validado"
    except Exception:
        output["estado"] = "falha"
        output["erro"] = traceback.format_exc()
        raise
    finally:
        output["cpu_segundos"] = time.process_time() - cpu
        output["parede_segundos"] = time.perf_counter() - wall
        output["memoria_max_kib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        output["teto_cpu_segundos"] = 60
        files = [HERE / "DECLARACAO.md", Path(__file__), ROOT / "collatz/coarse_memory.py",
                 ROOT / "collatz/test_coarse_memory.py", ROOT / "collatz/congruence_filters.py"]
        output["hashes"] = {str(p.relative_to(ROOT)): sha(p) for p in files}
        (HERE / "resultados.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
        if output["mistura"]:
            with (HERE / "mistura.csv").open("w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=list(output["mistura"][0]))
                writer.writeheader()
                writer.writerows(output["mistura"])
    print(json.dumps({key: value for key, value in output.items() if key != "mistura"},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
