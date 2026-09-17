"""Exportação de extremos intervalares sem arredondamento para dentro (11.3b-6)."""
import mpmath as mp

def sup_str(x, digits=12):
    """Cota superior decimal arredondada PARA CIMA do extremo superior de um intervalo mpmath.iv."""
    with mp.workdps(60):
        b = mp.mpf(x.b)
        n = int(mp.ceil(b * mp.mpf(10) ** digits)) + 1   # +1: margem contra arredondamento do produto
    s = "-" if n < 0 else ""
    n = abs(n)
    ip, fp = divmod(n, 10 ** digits)
    return f"{s}{ip}.{fp:0{digits}d}"

def inf_str(x, digits=12):
    """Cota inferior decimal arredondada PARA BAIXO do extremo inferior."""
    with mp.workdps(60):
        a = mp.mpf(x.a)
        n = int(mp.floor(a * mp.mpf(10) ** digits)) - 1
    s = "-" if n < 0 else ""
    n = abs(n)
    ip, fp = divmod(n, 10 ** digits)
    return f"{s}{ip}.{fp:0{digits}d}"
