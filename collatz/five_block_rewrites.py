"""Identidade selecionada após o diagnóstico completo da semente4."""
from .affine_rewrites import chronological_caps


BASE_FIVE = ((1,1,3,1,3),(2,2,1,1,3),(1,2,3,2,1))


def five_block_family(extra=0,suffix=()):
    """Três palavras de mesmo custo que equilibram o último dígito.

    A identidade não é uma afirmação de disponibilidade em toda classe.
    """
    if not isinstance(extra,int) or not 0 <= extra <= 159:
        raise ValueError("Reserva fora do intervalo0..159")
    suffix = tuple(suffix)
    caps = chronological_caps(5+len(suffix))
    if any(not isinstance(a,int) or not 1 <= a <= cap for a,cap in zip(suffix,caps[5:])):
        raise ValueError("Sufixo fora dos limites")
    return tuple(word[:4]+(word[4]+extra,)+suffix for word in BASE_FIVE)
