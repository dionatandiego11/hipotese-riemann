from collections import Counter

import pytest

from collatz.affine_rewrites import chronological_caps,word_residue
from collatz.cost_residues import generator_counts
from collatz.inverse_cost_policy import base_certificate,construct_four_n,inverse_policies
from collatz.uniform_coverage import construct_coverage,coverage_bound


def compositions(total,length):
    if length == 1:
        yield (total,)
        return
    for first in range(1,total-length+2):
        for rest in compositions(total-first,length-1):
            yield (first,)+rest


@pytest.fixture(scope="module")
def certificates():
    witnesses,counts = base_certificate()
    return witnesses,counts,inverse_policies()


def test_base_and_policy_against_independent_affine_congruences(certificates):
    base,counts,tables = certificates
    assert counts == generator_counts(4,12)[12]
    assert set(base) == {x for x in range(81) if x % 3}
    for x,word in base.items():
        assert sum(word) == 16
        assert word_residue(word) == x
    paths_checked = 0
    for r in range(1,5):
        oracle = {}
        modulus = 3**(r+1)
        for total in range(r,4*r+1):
            for path in compositions(total,r):
                # Afim final: (2^total*x-D)/3^r; integridade final
                # implica integridade de todos os passos (2 é unidade).
                d = 0
                for i,e in enumerate(path):
                    d = 2**e*d+3**i
                inv = pow(2,-total,modulus)
                for unit in (1,2):
                    x = (d+unit*3**r)*inv % modulus
                    candidate = (total,path)
                    if x not in oracle or candidate < oracle[x]:
                        oracle[x] = candidate
                paths_checked += 1
        assert oracle == tables[r]
        for x,(total,path) in tables[r].items():
            y = x
            for e in path:
                assert (2**e*y-1) % 3 == 0
                y = (2**e*y-1)//3
                assert y % 3
            assert total == sum(path) <= 4*r
    print(f"caminhos da busca independente={paths_checked}; classes de políticas=240")


def test_uniform_constructors_all_declared_classes(certificates):
    base,_,tables = certificates
    old_checked = new_checked = 0
    for depth in range(4,9):
        caps = chronological_caps(depth)
        for x in range(1,3**depth):
            if x % 3 == 0:
                continue
            for total,constructor in ((4*depth,construct_four_n),(coverage_bound(depth),None)):
                if constructor:
                    word = constructor(depth,total,x,base)
                    old_checked += 1
                else:
                    word = construct_coverage(depth,total,x,base,tables[4])
                    new_checked += 1
                assert len(word) == depth and sum(word) == total
                assert all(1 <= a <= cap for a,cap in zip(word,caps))
                assert word_residue(word) == x
    print(f"construções4n={old_checked}; construçõesL(n)={new_checked}")


def test_padding_in_previous_cost_grid():
    comparisons = 0
    for depth in range(4,9):
        maximum = 2*depth+2
        values = generator_counts(depth,maximum-depth)
        inverse = pow(2,-1,3**depth)
        for total in range(2*depth-2,maximum):
            source = values[total-depth]
            target = values[total+1-depth]
            for x,count in source.items():
                assert target[x*inverse % (3**depth)] >= count
                comparisons += 1
    print(f"cotas de preenchimento comparadas={comparisons}")
