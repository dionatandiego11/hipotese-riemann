from collections import Counter

from collatz.affine_rewrites import chronological_caps, word_residue
from collatz.cost_residues import generator_counts, project_counts
from collatz.family_availability import family_group_counts
from collatz.last_digit_rewrites import last_digit_family


def suffixes(total, caps):
    if not caps:
        if total == 0:
            yield ()
        return
    for first in range(1,min(caps[0],total-len(caps)+1)+1):
        for rest in suffixes(total-first,caps[1:]):
            yield (first,)+rest


def direct_family(depth,total):
    groups, fine = Counter(), Counter()
    for first in (1,2):
        for extra in range(46):
            remaining = total-first-11-extra
            if remaining < depth-4:
                continue
            for suffix in suffixes(remaining,chronological_caps(depth)[4:]):
                family = last_digit_family(first,suffix,extra)
                groups[word_residue(family[0],depth-1)] += 1
                for word in family:
                    fine[word_residue(word)] += 1
    return groups,fine


def test_recurrence_against_direct_family_and_full_generator():
    profiles = 0
    for depth in range(4,9):
        maximum = 2*depth+2
        recurrent = family_group_counts(depth,maximum)
        full = generator_counts(depth,maximum-depth)
        for total in range(2*depth-2,maximum+1):
            direct,fine = direct_family(depth,total)
            assert recurrent[total] == direct
            counts = full[total-depth]
            parents = project_counts(counts,depth-1)
            for parent,n in direct.items():
                assert parents[parent] >= 3*n
                for j in range(3):
                    child = parent+j*3**(depth-1)
                    assert fine[child] == n
                    assert counts[child] >= n
            assert sum(fine.values()) == 3*sum(direct.values())
            profiles += 1
    for total in (57,58):
        direct,_ = direct_family(4,total)
        assert family_group_counts(4,total)[total] == direct
    print(f"perfis custo/resíduo conferidos={profiles}; bordas da semente=2")


def test_predeclared_central_counterexample():
    depth,total = 8,16
    family = family_group_counts(depth,total)[total]
    assert family == Counter({971:1})
    missing_word = (1,1,1,1,1,1,1,9)
    assert sum(missing_word) == total
    assert word_residue(missing_word,7) == 299
    assert family[299] == 0
    parents = project_counts(generator_counts(8,8)[8],7)
    assert parents[299] > 0
    assert parents[971] >= 3
    print(f"contraexemplo: pai299 tem{parents[299]} palavras; grupos H=0; pai971 tem{parents[971]} palavras")
