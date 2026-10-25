"""Blocos cronológicos de três expoentes: exploração finita exata."""
from collections import defaultdict


def triple_numerator(word):
    if len(word) != 3 or any(a < 1 for a in word):
        raise ValueError("São necessários três expoentes positivos")
    a, b, _ = word
    return 9 + 3 * 2**a + 2**(a+b)


def triple_fibers(position, total):
    """Agrupa blocos pelo numerador mod3^(position+1), depois por filho.

    position começa em1. O mesmo total torna o denominador comum;
    multiplicá-lo por sua inversa permuta os filhos e preserva cobertura.
    """
    if position < 1 or total < 3:
        raise ValueError("Posição e custo fora do domínio")
    caps = [2 * 3**(position+i-1) for i in range(3)]
    modulus = 3**(position+1)
    fibers = defaultdict(lambda: defaultdict(list))
    for a in range(1, min(caps[0], total-2)+1):
        for b in range(1, min(caps[1], total-a-1)+1):
            c = total-a-b
            if not 1 <= c <= caps[2]:
                continue
            word = (a, b, c)
            numerator = triple_numerator(word)
            coarse = numerator % modulus
            child = (numerator // modulus) % 3
            fibers[coarse][child].append(word)
    return {a: dict(children) for a, children in fibers.items()}
