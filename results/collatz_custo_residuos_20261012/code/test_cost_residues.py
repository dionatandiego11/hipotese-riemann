from fractions import Fraction
import pytest
from collatz.cost_residues import (cost_counts, generator_counts, tuple_oracle,
                                  conditional_weights, tail_bound, project_counts)


def test_single_odd_block_has_exact_root_and_support():
    assert generator_counts(1, 3) == [{2: 1}, {1: 1}, {}, {}]
    assert cost_counts(1, 3) == [1, 1, 0, 0]


def test_composed_affine_oracle_and_haar_normalization():
    for level in range(1, 5):
        maps = generator_counts(level, 2 * level)
        totals = cost_counts(level, 2 * level)
        for k, counts in enumerate(maps):
            assert counts == tuple_oracle(level, k)
            assert sum(counts.values()) == totals[k]
            assert all(a % 3 for a in counts)
            for resolution in range(level + 1):
                assert sum(project_counts(counts, resolution).values()) == totals[k]


def test_cost_polynomial_total_and_reflection():
    for level in range(1, 5):
        degree = 3 ** level - level - 1
        coefficients = cost_counts(level, degree)
        assert coefficients == coefficients[::-1]
        assert sum(coefficients) == 2 ** level * 3 ** (level * (level-1)//2)


def test_conditional_law_and_uniform_tail():
    for level in (16, 24, 32, 64):
        for cost in (0, level, 2 * level):
            weights = conditional_weights(level, cost)
            assert sum(weights) == 1
            for cutoff in (0, 1, 2, 4, 8, 16):
                assert sum(weights[cutoff:], Fraction(0)) <= tail_bound(level, cost, cutoff)


def test_invalid_support_is_not_a_probability():
    with pytest.raises(ValueError):
        conditional_weights(1, 2)
    with pytest.raises(ValueError):
        tail_bound(15, 1, 1)
