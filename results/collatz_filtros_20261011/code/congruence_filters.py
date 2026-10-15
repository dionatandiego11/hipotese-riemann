"""Filtros periódicos do operador de contagem de Collatz nos positivos.

Convenção: T(x)=x/2 no ramo par, (3x+1)/2 no ímpar.
Nenhuma função deste módulo pressupõe a conjectura de Collatz.
"""

from collections import Counter
from dataclasses import dataclass
from math import gcd
from typing import Iterable


@dataclass(frozen=True, order=True)
class Congruence:
    modulus: int
    residue: int

    def __post_init__(self):
        if self.modulus < 1:
            raise ValueError("O módulo deve ser positivo.")
        object.__setattr__(self, "residue", self.residue % self.modulus)

    def contains(self, value: int) -> bool:
        return value % self.modulus == self.residue


def solve_congruence(multiplier: int, rhs: int, modulus: int):
    """Resolve multiplier*y ≡ rhs mod modulus; None denota filtro vazio."""
    if modulus < 1 or multiplier < 1:
        raise ValueError("Multiplicador e módulo devem ser positivos.")
    common = gcd(multiplier, modulus)
    if rhs % common:
        return None
    reduced = modulus // common
    if reduced == 1:
        return Congruence(1, 0)
    residue = (rhs // common) * pow(multiplier // common, -1, reduced)
    return Congruence(reduced, residue)


def pullback(filter_: Congruence, branch: int):
    """Um ramo, incluindo a condição de integridade do ramo ímpar."""
    if branch == 0:
        return solve_congruence(2, filter_.residue, filter_.modulus)
    if branch == 1:
        return solve_congruence(2, 3 * filter_.residue + 1,
                                3 * filter_.modulus)
    raise ValueError("Ramo deve ser 0 ou 1.")


def affine_word(word: Iterable[int]):
    """Composição na ordem de visita raiz→ancestral: (2^m*y-c)/3^k."""
    length = odd = constant = 0
    for branch in word:
        if branch not in (0, 1):
            raise ValueError("Palavra deve ser binária.")
        constant *= 2
        if branch:
            constant += 3 ** odd
            odd += 1
        length += 1
    return length, odd, constant


def word_filter(filter_: Congruence, word: Iterable[int]):
    length, odd, constant = affine_word(word)
    return solve_congruence(2 ** length,
                            constant + 3 ** odd * filter_.residue,
                            3 ** odd * filter_.modulus)


def iterate_filters(filter_: Congruence, depth: int):
    """Expande L_+^depth e agrega filtros idênticos, sem criar grafo de órbitas."""
    if depth < 0:
        raise ValueError("Profundidade deve ser não negativa.")
    state = Counter({filter_: 1})
    for _ in range(depth):
        next_state = Counter()
        for item, coefficient in state.items():
            for branch in (0, 1):
                transformed = pullback(item, branch)
                if transformed is not None:
                    next_state[transformed] += coefficient
        state = next_state
    return state


def evaluate_filters(state, root: int):
    return sum(coefficient for item, coefficient in state.items()
               if item.contains(root))


def common_modulus_bound(modulus: int, depth: int):
    """q=2^d*q_odd ⇒ período comum que divide 2^(d-m)_+*3^m*q_odd."""
    if modulus < 1 or depth < 0:
        raise ValueError("Parâmetros inválidos.")
    two_valuation = 0
    odd_part = modulus
    while odd_part % 2 == 0:
        odd_part //= 2
        two_valuation += 1
    return 2 ** max(two_valuation - depth, 0) * 3 ** depth * odd_part


def collatz_step(value: int):
    if value < 1:
        raise ValueError("O domínio desta função são os inteiros positivos.")
    return value // 2 if value % 2 == 0 else (3 * value + 1) // 2
