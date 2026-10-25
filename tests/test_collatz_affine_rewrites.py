from collections import Counter
from fractions import Fraction

import pytest

from collatz.affine_rewrites import (
    affine_block, chronological_caps, choose_child, pair_triple, word_residue,
)
from collatz.cost_residues import generator_counts, tuple_oracle


def bounded_words(total, caps):
    if len(caps) == 1:
        if 1 <= total <= caps[0]:
            yield (total,)
        return
    for first in range(1, min(caps[0], total - len(caps) + 1) + 1):
        for suffix in bounded_words(total - first, caps[1:]):
            yield (first,) + suffix


def root_offset(root_word):
    # Recorrência inversa da fonte, independente da composição com Fraction.
    d, cost = 0, 0
    for i, a in enumerate(root_word):
        d = 2**a * d + 3**i
        cost += a
    return Fraction(d, 2**cost)


def test_order_against_existing_generator_and_inverse_oracle():
    profiles = empty = 0
    for depth in range(1, 6):
        caps = chronological_caps(depth)
        generated = generator_counts(depth, 2 * depth)
        for total in range(depth, 3 * depth + 1):
            words = list(bounded_words(total, caps))
            direct = Counter(word_residue(w) for w in words)
            assert direct == generated[total-depth] == tuple_oracle(depth, total-depth)
            for word in words:
                assert affine_block(word)[1] == root_offset(word[::-1])
            profiles += bool(words)
            empty += not bool(words)
    # A falha antiga não é detectada só pela contagem total ou pelo custo.
    assert word_residue((3, 1)) == 8
    assert root_offset((3, 1)) == Fraction(5, 16)
    assert word_residue((1, 3)) == 2
    assert len(list(bounded_words(4, (2, 6)))) == len(list(bounded_words(4, (6, 2))))
    assert Counter(word_residue(w) for w in bounded_words(4, (2, 6))) != Counter(
        word_residue(w) for w in bounded_words(4, (6, 2)))
    print(f"perfis não vazios={profiles}; vazios={empty}")


def test_affine_identity_three_children_and_fiber_multiplicity():
    triples = classes_with_slack = classes_without_slack = 0
    for depth in range(2, 6):
        caps = chronological_caps(depth)
        for total in range(depth, 3 * depth + 1):
            words = list(bounded_words(total, caps))
            for index in range(depth - 1):
                r, q = depth - index - 1, depth - index - 2
                counts = Counter(word_residue(w, r+1) for w in words)
                parent_counts = Counter(word_residue(w, r) for w in words)
                good = Counter()
                images = [Counter() for _ in range(3)]
                for word in words:
                    if not all(3 <= word[i] <= caps[i]-2 for i in (index, index+1)):
                        continue
                    good[word_residue(word, r)] += 1
                    old_slope, old_offset = affine_block(word)
                    tail_sum = sum(word[index+2:])
                    for h, rewritten in pair_triple(word, index).items():
                        slope, offset = affine_block(rewritten)
                        power = Fraction(2)**h
                        difference = Fraction(3**q, 2**(tail_sum+word[index+1])) * (power-1)
                        assert slope == old_slope
                        assert offset-old_offset == difference
                        assert sum(rewritten) == total
                    variants = list(pair_triple(word, index).values())
                    assert len({word_residue(w, r) for w in variants}) == 1
                    assert len({word_residue(w, r+1) for w in variants}) == 3
                    for child in range(3):
                        image = choose_child(word, index, child)
                        images[child][image] += 1
                    triples += 1
                assert all(n <= 3 for image_counts in images for n in image_counts.values())
                for a in parent_counts:
                    classes_with_slack += good[a] > 0
                    classes_without_slack += good[a] == 0
                    for child in range(3):
                        assert 3*counts[a+child*3**r] >= good[a]
    witness = (1, 3, 3, 1)
    assert len(pair_triple(witness, 1)) == 3
    with pytest.raises(ValueError, match="Sem folga"):
        pair_triple((1, 1, 1, 1), 1)
    print(f"triplas={triples}; classes/par com folga={classes_with_slack}; sem folga={classes_without_slack}")
