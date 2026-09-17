# Plano de reprodução m4-v3 — duas implementações, faixa final (zeros 70.001–100.000)

Congelado por hash em `independent/M4V3_PLAN.lock.json` antes de qualquer análise dos zeros 70.001–100.000. Até lá,
os dados só passaram por aquisição e auditoria (`results/m4_v3_data_access_log.md`).

## 1. Papéis (fixados agora)

- **Implementação primária:** `src/riemann_spectra`, versão m4-v3, configurações `configs/m4_v3.toml`,
  `configs/m4_v3_bh.toml` e `configs/m4_v3_m2.toml`, lock de pacote. As conclusões C1–C3 do m4-v3 são as da primária.
- **Verificação de reprodução:** `independent/riemann_indep` v2 (difere de v1 apenas pelo limite explícito de acesso).
  Orçamentos: σ 200, limiar 1.999, escore 1.999, GUE 100 + 199, M2 299 + 299, fase 999. Sementes 9001–9010.
- **Não se escolhe depois qual resultado é principal.** A independente não substitui a primária, e a primária não é
  corrigida pela independente.
- **Não independência estatística.** As duas implementações analisam os mesmos zeros; a concordância entre elas não é
  uma segunda confirmação estatística. Ela verifica que as conclusões não dependem de detalhes de implementação.
- Blackman–Harris (robustez) e CUE (secundária) só na primária. CUE também é recalculado pela independente, para a
  verificação determinística D8.

## 2. Blocos

`d01` = 70.001–73.000, …, `d10` = 97.001–100.000: dez blocos contíguos de 3.000 zeros, com as mesmas regras científicas
de m4-v1 e m4-v2.

## 3. Comparação por bloco

Tolerâncias numéricas idênticas a `independent/COMPARISON_PLAN.md` (D1–D9, S1–S13), com uma mudança de coordenadas:

- **D2 e D3 nas mesmas coordenadas.** O termo suave e F da independente são avaliados na malha t da primária
  (`nulls.npz`) e comparados ponto a ponto. D1 continua comparando as malhas próprias. Com a FWHM corrigida em m4-v3,
  espera-se diferença ≤ 1e-10.
- **D8 com a CUE exata** da primária (sem interpolação).
- Grandezas Monte Carlo com sementes distintas; tolerâncias S1–S13 justificadas pela incerteza, como antes. Não se
  exige concordância em valores-p nem em linhas não claramente decididas.

## 4. Comparação de família (conclusões)

A independente aplica os mesmos critérios de §9.3 do protocolo aos seus próprios resultados, com Holm entre os 10 blocos:
- p(S): piso 1/2.000, ajustado ≤ 0,005;
- p(Q): piso 1/1.000, ajustado ≤ 0,01;
- C3: 299 realizações, menor p Holm atingível 10/300 ≈ 0,033.

São comparados:
- C1 replicado (sim/não), blocos que passam e blocos com detecção sem correspondência;
- C2 replicado e blocos que passam;
- C3: número de rejeições por par (referência, estatística).

## 5. Regras de interrupção da interpretação conjunta (pré-registradas)

- **R1 — discrepância determinística.** Qualquer verificação D (D1–D9) fora da tolerância em qualquer bloco suspende a
  conclusão conjunta até investigação.
- **R2 — discrepância estatística sistemática.** O mesmo código S fora da tolerância em ≥ 3 blocos suspende a conclusão
  conjunta. Falhas isoladas de S são investigadas e relatadas, sem suspensão automática; com 13 códigos × 10 blocos,
  falhas isoladas são esperadas por acaso.
- **R3 — mudança de conclusão.** Vereditos de família diferentes para C1 ou C2 suspendem a conclusão conjunta, salvo se
  **todos** os blocos com veredito diferente forem explicáveis dentro da incerteza prevista:
  - nenhuma linha claramente decidida com status diferente (S5);
  - componentes de p com o maior p ajustado ≤ 0,10;
  - diferenças de recuperação ou elegibilidade causadas só por linhas não claramente decididas ou com z previsto a
    ≤ 5% da margem 1,5 × limite superior.
- **R4 — mudança em C3.** Para cada par, a diferença no número de blocos rejeitados deve ser ≤ ao número de blocos em
  que o p Holm de alguma das implementações está em [0,01; 0,20]. Caso contrário, suspende a conclusão conjunta.

**Com uma regra acionada:** a conclusão da primária é relatada como tal, marcada como "reprodução com discrepância
aberta". A investigação usa os artefatos já gerados. Qualquer nova computação sobre os zeros 70.001–100.000 durante a
investigação é registrada em `results/m4_v3_data_access_log.md`, com data, comando e finalidade. Nenhuma regra, limiar
ou orçamento é alterado depois de ver os resultados.

## 6. Execução

Primária Hann → BH → M2 + CUE → independente (10 blocos) → `results/m4_v3_joint/compare_m4v3.py`.
Os scripts de execução independente e de comparação entram no lock deste plano.
