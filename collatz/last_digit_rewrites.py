"""Família selecionada após a exploração declarada de blocos de três.

Identidade afim exata; não demonstra disponibilidade em toda classe.
"""
from .affine_rewrites import chronological_caps, word_residue


BASE_BLOCKS = ((1, 1, 9), (3, 5, 3), (2, 8, 1))


def last_digit_family(first, suffix=(), extra=0):
    """Três palavras cronológicas; bloco nas posições2,3,4."""
    if first not in (1, 2) or not isinstance(extra, int) or not 0 <= extra <= 45:
        raise ValueError("Prefixo ou reserva de custo fora do domínio")
    suffix = tuple(suffix)
    caps = chronological_caps(4 + len(suffix))
    if any(not isinstance(a, int) or not 1 <= a <= cap for a, cap in zip(suffix, caps[4:])):
        raise ValueError("Sufixo fora dos limites")
    return tuple((first, a, b, c+extra) + suffix for a, b, c in BASE_BLOCKS)


def choose_last_child(word, child):
    """Manda palavras da família ao filho desejado; no máximo3 origens."""
    word = tuple(word)
    if len(word) < 4 or child not in (0, 1, 2):
        raise ValueError("Comprimento ou filho inválido")
    for a, b, c in BASE_BLOCKS:
        if word[1:3] == (a, b):
            family = last_digit_family(word[0], word[4:], word[3]-c)
            break
    else:
        raise ValueError("Palavra fora da família declarada")
    r = len(word)-1
    coarse = word_residue(word, r)
    for rewritten in family:
        if word_residue(rewritten) == coarse + child * 3**r:
            return rewritten
    raise ArithmeticError("Identidade do último dígito falhou")
