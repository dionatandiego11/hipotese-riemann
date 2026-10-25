"""Composição cronológica e reescritas afins de custo fixado.

Os limites cronológicos de Wirsching crescem: 2,6,18,... . A ordem da
raiz para a folha no mapa inverso é a reversa. Não são órbitas positivas.
"""
from fractions import Fraction


def chronological_caps(depth):
    if depth < 1:
        raise ValueError("Profundidade deve ser positiva")
    return tuple(2 * 3**i for i in range(depth))


def affine_block(word):
    """Phi_ultimo o ... o Phi_primeiro = slope*x + offset."""
    if not word or any(a < 1 or not isinstance(a, int) for a in word):
        raise ValueError("Expoentes inteiros positivos necessários")
    slope, offset = Fraction(1), Fraction(0)
    for a in word:
        slope *= Fraction(3, 2**a)
        offset = (3 * offset + 1) / 2**a
    return slope, offset


def word_residue(word, resolution=None):
    if resolution is None:
        resolution = len(word)
    if resolution < 0:
        raise ValueError("Resolução negativa")
    _, offset = affine_block(word)
    modulus = 3**resolution
    return offset.numerator * pow(offset.denominator, -1, modulus) % modulus


def pair_triple(word, index):
    """Três palavras válidas com mesmo custo, sob os limites cronológicos.

    index começa em0. Exige folga bilateral2 em AMBAS as coordenadas.
    As saídas mudam o dígito r=len(word)-index-1, sem mudar os anteriores.
    """
    word = tuple(word)
    caps = chronological_caps(len(word))
    if not 0 <= index < len(word) - 1:
        raise ValueError("Par adjacente inválido")
    if any(not 1 <= a <= cap for a, cap in zip(word, caps)):
        raise ValueError("Palavra fora dos limites")
    if any(not 3 <= word[i] <= caps[i] - 2 for i in (index, index + 1)):
        raise ValueError("Sem folga bilateral para as três versões")
    answer = {}
    for h in (-2, 0, 2):
        rewritten = list(word)
        rewritten[index] += h
        rewritten[index + 1] -= h
        answer[h] = tuple(rewritten)
    return answer


def choose_child(word, index, child):
    """Escolhe uma das três versões; cada imagem tem no máximo3 origens."""
    r = len(word) - index - 1
    if not 0 <= child <= 2:
        raise ValueError("Filho deve ser0,1ou2")
    a = word_residue(word, r)
    target = a + child * 3**r
    for rewritten in pair_triple(word, index).values():
        if word_residue(rewritten, r + 1) == target:
            return rewritten
    raise ArithmeticError("Identidade dos três filhos não satisfeita")
