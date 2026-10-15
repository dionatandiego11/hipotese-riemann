"""Invariantes e contraexemplos; não enumera ciclos de Collatz."""

from fractions import Fraction

import pytest

from collatz.congruence_filters import (
    Congruence, affine_word, common_modulus_bound, evaluate_filters,
    iterate_filters, pullback, solve_congruence, word_filter,
)


def test_empty_and_even_modulus():
    assert solve_congruence(4, 2, 8) is None
    assert pullback(Congruence(2, 1), 0) is None
    assert pullback(Congruence(2, 0), 1) is None
    assert pullback(Congruence(2, 1), 1) == Congruence(3, 2)


def test_positive_domain_branch_at_one():
    assert not pullback(Congruence(1, 0), 1).contains(1)
    assert evaluate_filters(iterate_filters(Congruence(1, 0), 1), 1) == 1


def test_word_order_and_no_intermediate_integrality():
    assert affine_word((0, 1)) == (2, 1, 1)
    assert affine_word((1, 0)) == (2, 1, 2)
    root = 2
    literal = Fraction(root)
    for branch in (0, 1):
        literal = 2 * literal if branch == 0 else (2 * literal - 1) / 3
    assert literal == Fraction(7, 3)
    assert not word_filter(Congruence(1, 0), (0, 1)).contains(root)


def test_empty_word():
    f = Congruence(9, 4)
    assert word_filter(f, ()) == f
    assert iterate_filters(f, 0) == {f: 1}


def test_minimum_period_witness():
    for depth in range(1, 8):
        state = iterate_filters(Congruence(1, 0), depth)
        modulus = 3 ** depth
        root = modulus - 1
        assert evaluate_filters(state, root) - evaluate_filters(
            state, root + modulus // 3) == 1


def test_modulus_and_coefficient_bounds():
    for modulus in (1, 2, 3, 5, 6, 12, 18):
        for depth in range(7):
            state = iterate_filters(Congruence(modulus, 0), depth)
            bound = common_modulus_bound(modulus, depth)
            assert all(bound % item.modulus == 0 for item in state)
            assert sum(state.values()) <= 2 ** depth


def test_bad_parameters():
    with pytest.raises(ValueError):
        Congruence(0, 0)
    with pytest.raises(ValueError):
        pullback(Congruence(1, 0), 2)
