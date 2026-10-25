from collections import Counter

import pytest

from collatz.affine_rewrites import word_residue
from collatz.balanced_seed import complete_four_seed,transport_group_seed
from collatz.cost_residues import generator_counts,project_counts
from collatz.family_availability import family_group_counts


@pytest.fixture(scope="module")
def seed():
    return complete_four_seed()


def test_complete_seed_against_generator_and_disjoint_catalogue(seed):
    fine,balanced,catalogue = seed
    source = generator_counts(4,76)
    assert sum(map(lambda c:sum(c.values()),fine)) == 11664
    used = set()
    for total in range(4,81):
        assert fine[total] == source[total-4]
    for group in catalogue:
        total,parent,words = group["total"],group["parent"],group["words"]
        assert {sum(w) for w in words} == {total}
        assert {word_residue(w,3) for w in words} == {parent}
        assert {word_residue(w) for w in words} == {parent+j*27 for j in range(3)}
        for word in words:
            assert word not in used
            used.add(word)
    assert len(used) == 3*len(catalogue)
    assert len(catalogue) == sum(sum(c.values()) for c in balanced)
    h = family_group_counts(4,80)
    for total in range(81):
        parents = project_counts(fine[total],3)
        for a in parents:
            assert balanced[total][a] == min(fine[total][a+j*27] for j in range(3))
        assert all(balanced[total][a] >= n for a,n in h[total].items())
    print(f"palavras=11664; grupos disjuntos={len(catalogue)}; palavras equilibradas={len(used)}")


def test_transported_maximum_against_full_and_old_family(seed):
    _,balanced,_ = seed
    profiles = 0
    for depth in range(4,9):
        maximum = 2*depth+2
        propagated = transport_group_seed(balanced,depth,maximum)
        old = family_group_counts(depth,maximum)
        full = generator_counts(depth,maximum-depth)
        for total in range(2*depth-2,maximum+1):
            fine = full[total-depth]
            parents = project_counts(fine,depth-1)
            for a in parents:
                capacity = propagated[total][a]
                assert old[total][a] <= capacity
                assert capacity <= min(fine[a+j*3**(depth-1)] for j in range(3))
            assert set(propagated[total]) <= set(parents)
            profiles += 1
    print(f"perfis transportados conferidos={profiles}")
