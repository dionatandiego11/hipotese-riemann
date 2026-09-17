# Etapa 11.6 — controle de ajuste K12: declaração prévia (17/09/2026)

Gravada **antes** de qualquer uso deste controle em comparação com candidatos. SHA-256 em `DECLARACAO_K12.sha256`.
Não introduz código, execução nem cálculo novo.

## 1. Objeto

**K12** (matriz de operadores, [ETAPA11_MATRIZ_OPERADORES.md](../../docs/ETAPA11_MATRIZ_OPERADORES.md), seção K12):
H = diag(γ₁, …, γ_N), com γ_n as ordenadas tabuladas dos zeros. Códigos vigentes: M1 = V, M2–M4 = V (N finito),
M5 = S, N1–N4 = S **apenas** com N ≥ 100.000 níveis inseridos com a precisão do dado (E-K12-N), sem valor explicativo.

**Função (plano da Etapa 11, §5, item 5):** controle negativo. Mostra que um objeto construído a partir dos próprios
níveis passa N1–N4 sem explicar nada.

## 2. Identificação com execuções existentes (sem cálculo novo)

O espectro de K12 é, por definição, a própria sequência de ordenadas. A cadeia congelada é determinística. Logo a
"execução de K12 pela cadeia m4" **é** a execução primária já realizada sobre essas ordenadas. Declara-se a identificação
com os artefatos abaixo, que **não** são recalculados nem alterados:

| Faixa de índices | Execução primária (janela de Hann) | protocol_version | SHA-256 de `manifest.json` (prefixo) |
|---|---|---|---|
| 10.001–40.000 | `results/run_20260913_144429_m3_b01-b02-b03-b04-b05-b06-b07-b08-b09-b10` | m4-v1 | `eeba25bbe8a264ae` |
| 40.001–70.000 | `results/run_20260913_173045_m3_c01-c02-c03-c04-c05-c06-c07-c08-c09-c10` | m4-v2 | `2acc8a379f70738c` |
| 70.001–100.000 | `results/run_20260913_220906_m3_d01-d02-d03-d04-d05-d06-d07-d08-d09-d10` | m4-v3 | `24bf5810192d7839` |

Dado de entrada: `data/raw/zeros1` (SHA-256 `3436c916…`). As execuções de robustez (Blackman–Harris) e as execuções m3
sobre os zeros 1–10.000 ficam fora desta identificação.

**Ressalva de nível.** N = 90.000 níveis nessas três execuções. O código E-K12-N fala em N ≥ 100.000; aqui a leitura é
restrita às faixas efetivamente processadas (10.001–100.000), e o controle não é usado fora delas.

## 3. Regras de uso fixadas agora (para 11.5 e 11.6)

1. **Nenhum crédito por N1–N4 em níveis inseridos.** Se um candidato reproduz N1–N4 apenas porque seu espectro contém
   (ou foi ajustado a) as ordenadas usadas na medição, o resultado é equivalente a K12 e **não conta** como evidência
   discriminante. Exemplo já registrado: K8 (Wu–Sprung), M1 = V por ajuste aos zeros.
2. **Teste fora da amostra obrigatório.** Um candidato que use níveis como dado de construção só pode ser avaliado em
   índices **não usados** na construção, com a predição congelada antes do cálculo.
3. **Comparação com K12.** Todo relatório de teste discriminante da 11.5 deve informar, lado a lado, o resultado do
   candidato e o de K12 nas mesmas faixas e com os mesmos critérios, e dizer em que o candidato supera K12 (por exemplo,
   predição de níveis fora da amostra ou de estrutura não inserida).
4. **Critério de leitura.** K12 "passa" N1–N4 nas faixas da tabela §2, por construção. Qualquer diferença entre K12 e as
   execuções citadas indicaria erro de identificação ou de registro, não propriedade física ou aritmética.

## 4. O que esta declaração não faz

- Não reexecuta a cadeia nem altera locks ou artefatos de m3/m4.
- Não afirma nada sobre RH nem sobre a existência de um operador de Hilbert–Pólya.
- Não pré-registra os outros controles da 11.6 (funções L de Dirichlet, triângulo modular, bilhar), que exigem desenho
  e cálculo próprios.
