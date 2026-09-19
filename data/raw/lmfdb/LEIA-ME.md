# Dados do LMFDB — autovalores de formas de Maass de nível 1

## Arquivo

| Campo | Valor |
|---|---|
| Arquivo | `lmfdb_maass_rigor_0919_1121.txt` |
| SHA-256 | `f4ca1d21465ee2907352c38f79eec4ab8091e2caf9444fc38181a0378df929c6` |
| Tamanho | 283.876 bytes |
| Origem | https://www.lmfdb.org/ModularForm/GL2/Q/Maass/?level=1 (download pelo site, 19/09/2026) |
| Conteúdo | 2.202 formas de Maass de nível 1, peso 0, caractere trivial; R de 9,5337 a 184,9240 |
| Formato | cabeçalho e definições do próprio LMFDB, em comentários `#`; campos: rótulo, nível, peso, caractere, parâmetro espectral R (λ = ¼ + R²), simetria (1 = ímpar, 0 = par, conferido nas páginas do LMFDB), sinal de Fricke |

O arquivo está **como foi baixado**, sem nenhuma alteração. O repositório usa `* -text` (`.gitattributes`) para preservar os
bytes. O caminho antigo `Mass-Forms/lmfdb_maass_rigor_0919_1121.txt` é um link simbólico para este arquivo; ele fica mantido
porque a declaração `ctrl-maass-v1` e o código executado o citam.

## Licença e atribuição

Os dados do LMFDB estão sob a licença **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**:
https://creativecommons.org/licenses/by-sa/4.0/ (página de licenças do LMFDB conferida em 19/09/2026; ver
`docs/ETAPA11_PENDENCIAS_FONTES.md` §13). **Este arquivo e qualquer derivado direto dos dados continuam sob CC BY-SA 4.0.**
O código do projeto continua sob MIT; a licença de dados vale só para os dados.

**Citação pedida pelo LMFDB:**

> The LMFDB Collaboration, *The L-functions and modular forms database*, https://www.lmfdb.org, 2026, [Online; accessed
> 19 September 2026].

**Origem dos dados, segundo o LMFDB** (página "Source of Maass form data"): formas rigorosas calculadas por Kieran Child,
Andrei Seymour-Howell e David Lowry-Duda; formas heurísticas por Fredrik Strömberg, Stefan Lemurell, Holger Then e David
Farmer.

## Observação sobre completude (19/09/2026)

Há um indício forte (rótulo C) de que faltam formas **ímpares** em R ∈ (99,5791; 110,1701) e acima de R = 177,9845,
embora o LMFDB declare completude até 184,9239. Detalhes em `docs/ETAPA11_PENDENCIAS_FONTES.md` §22 e em
`results/etapa11_6_controles/ADENDO_MAASS_3.md`. Se o LMFDB corrigir isso, os dados atuais do site vão diferir desta cópia;
esta é a versão usada no controle `ctrl-maass-v1`.
