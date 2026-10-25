import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

from collatz.affine_rewrites import affine_block, word_residue
from collatz.last_digit_rewrites import last_digit_family, choose_last_child


RUN = Path(__file__).resolve().parents[1] / "results/blocos_tres_20261019"


def test_all_selected_fibers_via_independent_affine_composition():
    witnesses = json.loads((RUN/"testemunhas.json").read_text())
    applications = 0
    for witness in witnesses:
        i, total, blocks = witness["i"], witness["S"], witness["palavras"]
        assert len({sum(block) for block in blocks}) == 1
        assert sum(blocks[0]) == total
        for suffix in ((), (1,)):
            words = [(1,)*(i-1) + tuple(block) + suffix for block in blocks]
            offsets = [affine_block(word) for word in words]
            assert len({slope for slope, _ in offsets}) == 1
            coarse = {word_residue(word, len(word)-1) for word in words}
            fine = {word_residue(word) for word in words}
            assert len(coarse) == 1
            assert len(fine) == 3
            applications += 1
    print(f"fibras selecionadas={len(witnesses)}; aplicações afins={applications}")


def test_chosen_identity_and_complete_first_block_obstruction():
    # A identidade é calculada por composição racional, sem a fórmula B3.
    words = last_digit_family(1)
    assert [affine_block(word)[1] for word in words] == [
        Fraction(65,4096),Fraction(605,4096),Fraction(2117,4096)]
    assert {word_residue(word) for word in words} == {2,29,56}
    for suffix in ((), (1,)):
        family = last_digit_family(1, suffix)
        for child in range(3):
            images = Counter(choose_last_child(word, child) for word in family)
            assert len(images) == 1
            assert max(images.values()) == 3
    table = json.loads((RUN/"primeiro_bloco.json").read_text())
    assert set(map(int,table)) == {1,2,4,5,7,8}
    assert all(len(row) == 2 for row in table.values())
    for coarse, rows in table.items():
        for row in rows:
            _, offset = affine_block((row["a"],row["b"],1))
            numerator = offset * 2**(row["a"]+row["b"]+1)
            assert numerator == row["B"]
            assert row["B"] % 9 == int(coarse)
