# Adendo 1 ao `ctrl-dirichlet-v1` — falha de V4 no piloto por escolha de ponto de teste (19/09/2026)

Gravado **antes** de qualquer mudança no código e antes de qualquer nova execução. SHA-256 em `ADENDO_DIRICHLET_1.sha256`.
Declaração original: [DECLARACAO_DIRICHLET.md](DECLARACAO_DIRICHLET.md) (SHA-256 `e6cb8ab8…`), que continua valendo em
tudo o que este adendo não muda.

## 1. O que aconteceu (registro; nada é apagado)

O piloto de χ₋₄ (500 zeros, executado pelo usuário em 19/09/2026, arquivo `dados_piloto/manifest_chi_m4_500.json`,
script SHA-256 `0f16b4c5…`) terminou com `all_checks_passed: false`:
- **aprovados:** V1 (diferença 0,246 contra a tolerância 3), V2 (mesma contagem; máx. |Δγ| = 9,3·10⁻¹¹) e V3 (50/50);
- **V4 falhou num único ponto**, t = 628,8248332600831, com |Im Z|/|Z| = 8,8·10⁻²⁰, acima de 10⁻²⁰. Nos outros 9 pontos
  a razão ficou entre 3·10⁻³¹ e 1,6·10⁻²⁸.

Pela regra do §4 da declaração, **os dados desse piloto não são usados** enquanto V4 não for aprovado.

## 2. Causa (diagnóstico feito sem alterar arquivos do projeto)

O código escolhe os pontos de V4 com `np.linspace(10, t_max, 10)`, e t_max é o **último zero calculado**. Então o décimo
ponto cai exatamente num zero de Z_χ, e a medida relativa perde o sentido:

| t | \|Z_χ(t)\| | \|Im Z_χ(t)\| | razão |
|---|---|---|---|
| 628,8248332600831 (zero) | 4,6·10⁻¹³ | 4,1·10⁻³² | 8,8·10⁻²⁰ |
| 628,8248332600831 − 0,3 | 1,56 | 5,5·10⁻²⁹ | 3,5·10⁻²⁹ |
| 628,8248332600831 + 0,3 | 0,78 | 3,0·10⁻²⁹ | 3,9·10⁻²⁹ |
| 628,9 | 0,30 | 5,2·10⁻²⁹ | 1,7·10⁻²⁸ |

A parte imaginária está no nível do ruído de 30 dígitos em todos os pontos, inclusive no zero. O que infla a razão é o
denominador |Z_χ| ≈ 0 no zero. É um **defeito de desenho da verificação**, não um indício de que Z_χ deixa de ser real
nem de erro nos zeros. A declaração fixou "10 pontos por caractere", mas não quais.

## 3. Mudança (única)

**V4, pontos de teste:** para cada um dos 10 pontos s_j = linspace(10, t_max, 10), usar como ponto de teste o **ponto
médio entre os dois zeros consecutivos calculados** que cercam s_j. Se s_j estiver abaixo do primeiro zero, usar o
ponto médio entre 10 e o primeiro zero; se estiver no último zero ou acima dele, usar o ponto médio entre os dois
últimos. A tolerância (10⁻²⁰ relativo), a precisão (30 dígitos) e o número de pontos não mudam.

Nada mais muda: método dos zeros, V1–V3, critérios, sementes e instrumento continuam os da declaração.

## 4. Como aplicar

1. Esperar o fim do piloto de χ₅, que já estava rodando com o código original quando este adendo foi escrito. Esse
   piloto é registrado como está, e o V4 dele é avaliado sob a regra original **e** sob a regra deste adendo.
2. Alterar só a função `v4_reality` de `dirichlet/dirichlet_zeros.py` (e o teste correspondente), com o novo hash do
   script registrado.
3. Reavaliar V4 dos dois pilotos com o código novo, **sem recalcular os zeros**: V4 testa a função Z_χ, não a lista de
   zeros; a lista só fornece os pontos médios. Os arquivos de zeros e os manifestos originais ficam preservados, e o
   resultado novo vai num arquivo à parte.
4. Se V4 passar com a regra nova, os pilotos ficam aprovados em V1–V4, e o custo medido é registrado antes do cálculo
   completo.
