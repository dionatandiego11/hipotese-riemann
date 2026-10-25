from fractions import Fraction

from collatz.central_residues import geometric_limit, stationary_half
from collatz.collision_energy import collision_decomposition


def test_stationarity_projection_and_collision_recursion_exactly():
    previous = geometric_limit(0)
    previous_energy = Fraction(1)
    for k in range(1, 5):
        current = geometric_limit(k)
        n = 3 ** k
        result = collision_decomposition(current, previous)
        assert sum(current) == 1
        assert all(sum(current[b::n // 3]) == previous[b] for b in range(n // 3))
        assert all(d + o == p for d, o, p in zip(result["D"], result["O"], current))
        assert result["DD"] == result["collision"] / 4
        assert result["OO"] == sum(x * x for x in previous) / 4
        assert result["DO"] == result["OD"] == result["H"] / 4
        assert sum(result[x] for x in ("DD", "DO", "OD", "OO")) == result["collision"]
        assert 3 * result["collision"] == sum(x * x for x in previous) + 2 * result["H"]
        assert result["energy"] - previous_energy == 2 * 3 ** (k - 1) * result["H"] > 0
        previous, previous_energy = current, result["energy"]


def test_geometric_construction_against_independent_elimination():
    for k in range(3):
        assert geometric_limit(k) == stationary_half(k)
