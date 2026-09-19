# Adendo 2 ao `ctrl-maass-v1` — número de linhas sintéticas isoladas por realização (19/09/2026)

Gravado **antes** de qualquer aplicação do instrumento aos autovalores de Maass e antes da correção do código.
SHA-256 em `ADENDO_MAASS_2.sha256`. Declaração `5db97004…`; adendo 1 `4efb9020…`.

## 1. O que aconteceu

A declaração (§5) manda usar "os parâmetros numéricos de `configs/m4_v3.toml`". Entre eles estão
`synthetic_lines_per_realization = 12` e `synthetic_realizations = 40`. No gerador de linhas isoladas da calibração
sintética (cópia de `inverse_spectroscopy._task_synthetic`, código congelado, linhas 111–117), as linhas são sorteadas
em t ∈ [t_min + 0,05, t_max − 0,05] com separação mínima de **10 FWHM**, num laço que só termina quando há 12 linhas.

- Nos zeros de ζ (m4-v3), a FWHM é ≈ 0,005: 12 linhas × 10 FWHM ≈ 0,6 cabem na janela de 4,4.
- No bloco H de Maass, com R ∈ [9,53; 184,92], a FWHM é 4π/175,4 ≈ 0,072: cabem no máximo ⌊4,4/0,72⌋ = 6 linhas. O
  **laço não termina**. Isso foi observado no teste de fumaça do código, sobre dados sintéticos, sem nenhum autovalor real.

É uma incompatibilidade entre um parâmetro herdado e a resolução deste controle, não uma escolha feita depois de ver
dados.

## 2. Mudança (única)

- Linhas isoladas por realização: **n_iso = min(12, ⌊S/(2·10·FWHM)⌋)**, com S = t_max − t_min − 0,1 o comprimento útil,
  exigindo n_iso ≥ 2; senão, o bloco é declarado sem calibração e os critérios que dependem dela não são avaliados.
  **Por que 2·10·FWHM:** o sorteio é sequencial e aleatório, com exclusão d = 10·FWHM. Num estado em que não cabe mais
  nenhuma linha, todo buraco entre linhas vizinhas é < 2d, e as pontas são < d; logo há sempre ≥ S/(2d) linhas. Com
  n_iso = ⌊S/(2d)⌋, o laço **sempre termina**.
- **Nota de redação:** a primeira versão deste item usava ⌊S/(10·FWHM)⌋ (o empacotamento máximo), que **não** garante
  término por causa desse travamento: o teste de fumaça, sobre dados sintéticos, travou de novo. Corrigido antes de
  qualquer uso em dados reais.
- Realizações isoladas: **⌈40 × 12 / n_iso⌉**, de modo que o total de linhas isoladas fique o de m4-v3 (≥ 480).
- A calibração de pares (separações de 0,5 a 3 FWHM) não tem restrição de separação mínima no gerador e **não muda**.
- Nada mais muda: separação de 10 FWHM, intervalo de z, quantil da tolerância, curva de recuperação e alvo de
  resolução continuam os de m4-v3.

## 3. Registro

O `block_metrics.json` de cada bloco registra n_iso e o número de realizações usadas. A mesma incompatibilidade vai
existir no `ctrl-estadio-v1`, onde a FWHM vai de 0,15 a 0,34, e será tratada por adendo próprio antes do código daquele
controle.
