from fractions import Fraction as F

import pytest

from collatz.coarse_memory import (
    averaged_density_step, coupling_bound, maps, project_probabilities,
    pull_observable, push_probabilities, stationary_probabilities,
)


def test_orientation_and_mod_three():
    assert maps(1) == ([0, 2, 1], [2, 2, 2])
    assert push_probabilities([F(1), F(0), F(0)], 1) == [F(3, 4), F(0), F(1, 4)]


def test_finite_haar_adjoint_and_density_formula():
    for level in range(4):
        size = 3 ** level
        density = [F(a + 1) for a in range(size)]
        observable = [F((7 * a + 3) % 11) for a in range(size)]
        evolved = averaged_density_step(density, level)
        assert evolved == push_probabilities(density, level)
        assert sum(a * b for a, b in zip(evolved, observable)) == sum(
            a * b for a, b in zip(density, pull_observable(observable, level)))


def test_stationary_level_one():
    assert stationary_probabilities(1) == [F(0), F(3, 7), F(4, 7)]


def test_trivial_level():
    assert push_probabilities([F(1)], 0) == [F(1)]
    assert stationary_probabilities(0) == [F(1)]
    assert coupling_bound(0, 0) == 0
    assert coupling_bound(0, 2) == 1


def test_projection_consistency_of_kernel():
    values = [F(a + 1, 378) for a in range(27)]
    assert sum(values) == 1
    assert project_probabilities(push_probabilities(values, 3), 3, 2) == push_probabilities(
        project_probabilities(values, 3, 2), 2)


def test_invalid_input():
    with pytest.raises(ValueError):
        push_probabilities([], 0)
    with pytest.raises(ValueError):
        project_probabilities([F(1)], 0, 1)
    with pytest.raises(ValueError):
        stationary_probabilities(4)
