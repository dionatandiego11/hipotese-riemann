"""Controle exato pequeno; parâmetros fixados em DECLARACAO.md."""

import hashlib
import itertools
import json
import platform
import resource
import sys
import time
import traceback
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))

from collatz.congruence_filters import (  # noqa: E402
    Congruence, affine_word, collatz_step, common_modulus_bound,
    evaluate_filters, iterate_filters, word_filter,
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    expected = "f6311b8538678202a22eb887615b7561d07ecf4c990175def1ba2bf7ca00ad8e"
    assert sha(HERE / "DECLARACAO.md") == expected
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    wall = time.perf_counter()
    cpu = time.process_time()
    results = {"estado": "em execução", "classe": "B (controles exatos)",
               "data_execucao": "2026-10-12", "declaracao_sha256": expected,
               "python": platform.python_version(), "checks": {}, "periodos": []}
    checks = results["checks"]
    try:
        word_checks = 0
        for depth in range(6):
            for word in itertools.product((0, 1), repeat=depth):
                for modulus in range(1, 13):
                    for residue in range(modulus):
                        target = Congruence(modulus, residue)
                        output = word_filter(target, word)
                        for root in range(1, 49):
                            literal = Fraction(root)
                            valid = True
                            for branch in word:
                                literal = 2 * literal if branch == 0 else (2 * literal - 1) / 3
                                if literal.denominator != 1 or literal < 1:
                                    valid = False
                                    break
                            oracle = valid and target.contains(literal.numerator)
                            formula = output is not None and output.contains(root)
                            assert oracle == formula, (word, modulus, residue, root)
                            word_checks += 1
        checks["composicao_literal_vs_congruencia"] = word_checks

        forward_checks = 0
        for depth in range(7):
            # Independente dos ramos inversos: T^m aplicado a cada ancestral possível.
            by_root = {root: [] for root in range(1, 49)}
            for ancestor in range(1, 2 ** depth * 48 + 1):
                target_root = ancestor
                for _ in range(depth):
                    target_root = collatz_step(target_root)
                if target_root in by_root:
                    by_root[target_root].append(ancestor)
            for modulus in range(1, 13):
                for residue in range(modulus):
                    initial = Congruence(modulus, residue)
                    state = iterate_filters(initial, depth)
                    bound = common_modulus_bound(modulus, depth)
                    assert all(bound % item.modulus == 0 for item in state)
                    assert sum(state.values()) <= 2 ** depth
                    for root in range(1, 49):
                        oracle = sum(initial.contains(x) for x in by_root[root])
                        assert evaluate_filters(state, root) == oracle, (depth, modulus, residue, root)
                        forward_checks += 1
        checks["iteracao_direta_vs_expansao"] = forward_checks

        for depth in range(1, 8):
            state = iterate_filters(Congruence(1, 0), depth)
            modulus = 3 ** depth
            values = [evaluate_filters(state, root) for root in range(1, modulus + 1)]
            # Os únicos divisores próprios necessários: se o período é uma potência
            # de 3, todo período divisor próprio divide 3^(m-1).
            assert any(values[i] != values[(i + modulus // 3) % modulus]
                       for i in range(modulus))
            assert Fraction(sum(values), modulus) == Fraction(4, 3) ** depth
            results["periodos"].append({"m": depth, "periodo_minimo": modulus,
                                       "media_exata": str(Fraction(sum(values), modulus)),
                                       "filtros_distintos": len(state)})
        checks["periodo_minimo_e_media"] = 7

        dyadic_checks = 0
        for d in range(7):
            modulus = 2 ** d
            for depth in range(9):
                words = list(itertools.product((0, 1), repeat=depth))
                for root in range(32):
                    # Usa TODOS os ramos em Z2, sem filtro de integridade em Z.
                    count = 0
                    for word in words:
                        length, odd, constant = affine_word(word)
                        value = 0 if modulus == 1 else (
                            (2 ** length * root - constant) * pow(3 ** odd, -1, modulus)
                        ) % modulus
                        count += value == 0
                    if depth >= d:
                        assert Fraction(count, 2 ** depth) == Fraction(1, modulus)
                        dyadic_checks += 1
        checks["media_haar_diadica_apos_d_passos"] = dyadic_checks
        results["estado"] = "validado"
    except Exception:
        results["estado"] = "falha"
        results["erro"] = traceback.format_exc()
        raise
    finally:
        results["cpu_segundos"] = time.process_time() - cpu
        results["parede_segundos"] = time.perf_counter() - wall
        results["memoria_max_kib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        results["limite_cpu_segundos"] = 60
        files = [HERE / "DECLARACAO.md", Path(__file__),
                 ROOT / "collatz/congruence_filters.py", ROOT / "collatz/test_congruence_filters.py"]
        results["hashes"] = {str(p.relative_to(ROOT)): sha(p) for p in files}
        (HERE / "resultados.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
