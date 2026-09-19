# Adendo 3 ao `ctrl-maass-v1` — lacuna de formas ímpares nos dados; blocos por segmento completo (19/09/2026)

Gravado **antes** de qualquer nova execução e **sem** que os resultados de linhas da execução interrompida tenham sido
abertos. SHA-256 em `ADENDO_MAASS_3.sha256`.
- Declaração `5db97004…`;
- adendos 1 (`4efb9020…`) e 2 (`3a40cf7a…`).

## 1. O que aconteceu

**A execução.** A primeira execução (19/09, 14:42–14:48; pasta `maass/execucao_v1_interrompida/`, preservada e marcada
"NÃO USAR") parou no bloco h1 com "Densidade modulada não positiva" na calibração sintética. **Só as linhas de limiar
dos nulos foram vistas**; os arquivos de linhas do bloco H não foram abertos.

**O diagnóstico.** Ele usou só a escada de contagem, sem o catálogo:
- o ajuste suave declarado (R²/24 + βR log R + γR + δ₀) teve resíduo quadrático médio de **18,3 níveis** no bloco H e
  **14,9** no h1, contra **0,72** no h2;
- no bloco H, d̄(R) sai **negativa** no início;
- a causa é uma **lacuna de formas ímpares**: entre R = 99,5791 e R = 110,1701 há uma distância de **87,9 espaçamentos
  médios locais** (12/R);
- nenhum outro espaçamento, ímpar ou par, passa de 8 espaçamentos médios.

**A origem, conferida no LMFDB em 19/09/2026** (busca `level=1&spectral_parameter=99.5-110.3` no espelho beta):
- o site devolve **79 formas** nesse intervalo, as mesmas do arquivo (4 ímpares e 75 pares), e afirma "The results
  below are complete, since the LMFDB contains all Maass forms with level 1 and spectral parameter at most 184.9239";
- a busca `spectral_parameter=178-185&symmetry=1` devolve "No matches", e o arquivo não tem formas ímpares acima de
  R = 177,9845, contra 92 pares em [178; 185];
- pela lei de Weyl, com densidade ímpar ≈ R/12, seriam esperadas ~90 formas ímpares em (99,58; 110,17) e ~100 em
  (177,98; 184,92).

**Leitura (rótulo C, indício forte, não demonstração):** o LMFDB parece **não conter** parte das formas ímpares de
nível 1 nessas duas faixas, apesar da declaração de completude. A lei de Weyl dá só a média, então não prova a falta;
mas uma lacuna de 88 espaçamentos médios não é plausível numa sequência completa. **A premissa de completude da
declaração (§2) falha** para o setor ímpar deste arquivo. A conferência B da declaração não incluía teste de lacunas;
esta falha fica registrada.

## 2. Mudanças

1. **Nova conferência B (obrigatória):** um espaçamento maior que **10 espaçamentos médios locais** (12/R) marca uma
   lacuna de dados. Para Poisson, P(s > 10) = e⁻¹⁰, o que dá ~0,05 alarme falso esperado em 1.091 espaçamentos. Os
   blocos só podem ser **segmentos sem lacuna**.
2. **Blocos (substituem H, h1, h2):**
   - **S2 (primário):** formas ímpares 342 a 1.092 (índice na lista do arquivo), R ∈ [110,1701; 177,9845], 751 níveis;
     FWHM ≈ 4π/67,8 ≈ 0,185;
   - **S1 (replicação, só descritivo):** formas 1 a 341, R ∈ [9,5337; 99,5791], 341 níveis; FWHM ≈ 0,14.
3. **Conferência do ajuste suave (obrigatória, antes da transformada de cada bloco):** resíduo quadrático médio ≤ **2
   níveis** e d̄ > 0 em todo o segmento. Se falhar, o bloco não é avaliado. O índice j da escada é o índice no arquivo;
   o deslocamento constante causado pela lacuna, em S2, é absorvido por δ₀.
4. **Orçamento das linhas sintéticas:** o limite de amplitude injetada passa a ser 0,8 · min d̄ no segmento, e não
   0,8 · d̄ no primeiro nível. Se d̄ for crescente, as duas coisas coincidem; a mudança só evita que a calibração
   quebre quando d̄ tem mínimo interno.
5. **Resultado do controle:** "passa" se M-C1, M-C2s, M-C2a+, M-C2a−, M-C4 e M-C4s passam em **S2**. S1 é reportado
   com os mesmos critérios, sem decidir.

## 3. O que não muda

Setor ímpar; catálogo G1; coeficientes e critérios dos adendos 1 e 2; densidade suave com R²/24 fixo e três
parâmetros ajustados; nulos; semente 20260922; parâmetros numéricos.

## 4. Consequências registradas

- A resolução piora em relação ao plano: FWHM de 0,185 em S2, contra 0,072 previsto para H. Mais linhas de G1 ficam
  não resolvidas acima de t ≈ 3,5, e a regra de elegibilidade trata disso.
- **A possível incompletude do LMFDB é um achado à parte**, registrado na §22 das pendências de fontes. Comunicar aos
  mantenedores é decisão do usuário.
