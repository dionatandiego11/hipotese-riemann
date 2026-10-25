from fractions import Fraction

from collatz.affine_rewrites import affine_block,chronological_caps,word_residue
from collatz.balanced_seed import complete_four_seed,transport_group_seed
from collatz.cost_residues import generator_counts
from collatz.five_block_rewrites import five_block_family


def test_five_block_affine_identity_and_bounds():
    applications = 0
    for extra in (0,1,159):
        for suffix in ((),(1,),(1,1)):
            family = five_block_family(extra,suffix)
            depth = len(family[0])
            cap = chronological_caps(depth)
            assert {sum(w) for w in family} == {9+extra+sum(suffix)}
            assert all(all(1 <= a <= c for a,c in zip(word,cap)) for word in family)
            maps = [affine_block(word) for word in family]
            assert len({slope for slope,_ in maps}) == 1
            step = Fraction(2*3**(depth-1),2**(9+extra+sum(suffix)))
            assert maps[1][1]-maps[0][1] == maps[2][1]-maps[1][1] == step
            assert len({word_residue(w,depth-1) for w in family}) == 1
            assert len({word_residue(w) for w in family}) == 3
            applications += 1
    print(f"famílias verificadas exatamente={applications}")


def test_witness_outside_every_prefix_four_catalogue():
    family = five_block_family()
    assert [affine_block(word)[1] for word in family] == [Fraction(n,512) for n in (331,493,655)]
    assert [word_residue(word) for word in family] == [209,47,128]
    assert {word_residue(word,4) for word in family} == {47}
    fine = generator_counts(5,4)[4]
    assert [fine[47+j*81] for j in range(3)] == [1,1,1]
    _,seed,_ = complete_four_seed()
    assert transport_group_seed(seed,5,9)[9][47] == 0
    assert {word[-1] for word in family} == {1,3}
