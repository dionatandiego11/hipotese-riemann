# Adendo 3 ao `ctrl-dirichlet-v1` — passe de completude depois da falha de V1 e V2 em χ₋₄ (22/09/2026)

Gravado **antes** de escrever o código do passe de completude, **antes** de executá-lo e **antes** de a execução de χ₅
chegar à sua V2. SHA-256 em `ADENDO_DIRICHLET_3.sha256`.

- Declaração: [DECLARACAO_DIRICHLET.md](DECLARACAO_DIRICHLET.md) (`e6cb8ab8…`).
- Adendo 1: [ADENDO_DIRICHLET_1.md](ADENDO_DIRICHLET_1.md) (`6ee78368…`) — pontos médios na V4.
- Adendo 2: [ADENDO_DIRICHLET_2.md](ADENDO_DIRICHLET_2.md) (`61995046…`) — retomada, aceitação do refinamento, benchmark.
- Script congelado do cálculo: `dirichlet/dirichlet_zeros.py` (`65056bc2…`). **Não é alterado por este adendo.**

## 0. O que já havia sido executado quando este adendo foi escrito (transparência)

1. A execução de χ₋₄ terminou em 22/09/2026 08:41 e gravou `dados/manifest_chi_m4_12000.json`
   (`all_checks_passed: false`; V1 e V2 reprovadas, V3 e V4 aprovadas) e `dados/zeros_chi_m4_12000.txt`
   (SHA-256 `698e7dba…`).
2. Em 22/09 21:41 a execução de χ₅, interrompida pelo reinício da máquina às ~21:00, foi retomada do checkpoint
   (11.194/12.000 zeros; `retomadas` passa a 2). Nenhum parâmetro mudou.
3. Entre 21:45 e 22:10 de 22/09 rodou um **diagnóstico** (script fora do repositório, em pasta temporária) que
   reexaminou os 20 maiores intervalos entre zeros consecutivos de χ₋₄ com passo d̄/32, e um teste de `Im loggamma`
   contra Stirling nos pontos dos degraus. **Este adendo foi escrito depois de ver esse diagnóstico**, e é dele que
   saem os números do §3. O diagnóstico não altera nenhum critério da declaração; a íntegra da saída vai para o anexo
   `dirichlet/completude/DIAGNOSTICO_V1V2.md`.

## 1. Fatos medidos (χ₋₄, 12.000 zeros)

- **V1:** N(T) − θ_χ(T)/π vale +0,50 no início da lista e −12,96 no fim. A curva **não deriva**: tem platôs planos
  (variação interna < 0,05) com **degraus de exatamente −2**, em sete pontos, perto dos índices 4.220, 5.350, 7.430,
  7.950, 8.930, 9.000 e 10.260. Déficit total ≈ 14 zeros.
- **V2:** o bloco 9001–12000 recalculado com passo pela metade achou 3.002 zeros onde a lista tem 3.000.
- **Mecanismo, confirmado por reexame direto:** em [3893,1962; 3895,0981] existem dois zeros, 3893,887460453 e
  3893,977078497, separados por 0,0896, enquanto o passo da varredura ali é d̄/8 = 0,0967. O par cabe **dentro de um
  passo**: Z_χ troca de sinal duas vezes entre dois pontos amostrados e nenhuma das trocas é vista. O mesmo foi
  confirmado em [4791,2944; 4793,3374] (par a 0,0836), [6391,8883; 6393,8248] (0,0603) e
  [6785,6489; 6787,6734] (0,0527).
- **Não é convenção nem ramo:** `Im loggamma(1 + it/2)` coincide com a série de Stirling com erro ≤ 3·10⁻²⁰ em todos os
  pontos dos degraus; não há salto de 2π em θ_χ.
- **Por que o rescan automático não pegou:** `ZeroFinder.rescan_large_gaps` só dispara em intervalos maiores que
  **4 d̄**; os buracos têm 2,3–3,4 d̄.
- **O tamanho do intervalo, sozinho, não separa:** há intervalos de 2,374 d̄ e 2,320 d̄ **sem** par escondido e um de
  2,366 d̄ **com** par. Por isso o limiar do §3 é só a primeira passada, e a garantia fica com o certificado.

Rótulo: **B** (comportamento numérico reproduzido e diagnosticado). A perda de pares por passo grosseiro é fenômeno
conhecido em varredura por troca de sinal; não há novidade aqui.

## 2. O que não muda

Método dos zeros (Hurwitz, 30 dígitos, passo d̄/8, refinamento até 10⁻¹⁰ com aceitação estrita), definição das
verificações V1–V4 e suas tolerâncias (V1: |N − θ/π| ≤ 3 por bloco; V2: mesma contagem e max|Δ| ≤ 10⁻⁹; V3; V4 pelo
Adendo 1), blocos, sementes, instrumento e critérios D-C1, D-C1z, D-C2, D-C2s e D-C2z. **Os arquivos originais são
imutáveis**: `zeros_chi_m4_12000.txt`, o manifesto com `all_checks_passed: false` e os checkpoints ficam como estão e
continuam sendo o registro do resultado reprovado.

## 3. Passe de completude D3 (fixado agora)

Aplicado a cada caractere, sobre a lista original, sem tocá-la.

**Etapa A — varredura dirigida.** Todo par consecutivo (γ_i, γ_{i+1}) com γ_{i+1} − γ_i > **1,6 · d̄** (d̄ calculado no
ponto médio, pela mesma `mean_spacing` do script congelado) é reexaminado em [γ_i + 10⁻⁹, γ_{i+1} − 10⁻⁹] com passo
**d̄/32** (`ZeroFinder` do script congelado, `step_fraction = 1/8`, `step_scale = 0,25`), com o mesmo refinamento e a
mesma aceitação estrita. Zeros encontrados são inseridos em ordem. Em χ₋₄ isso são 800 intervalos, largura total
≈ 1.434 d̄.

**Etapa B — certificado D3-C1.** Sobre a lista corrigida, S(n) = n − θ_χ(γ_n)/π. Divide-se a lista em janelas
consecutivas de 200 zeros e toma-se a mediana m_j de S em cada janela. Exige-se:
1. |m_j − m_0| ≤ **0,75** para todo j; e
2. |m_{j+1} − m_j| < **1,5** para todo j.
Um par perdido desloca todos os S seguintes em −2 e viola as duas condições; a flutuação interna dos platôs medida em
χ₋₄ é < 0,05, ou seja, quinze vezes menor que a margem. O certificado detecta qualquer perda **par** (2, 4, …); perda
ímpar é impossível numa varredura por troca de sinal com extremos fixos.

**Etapa C — resíduo.** Para cada degrau que sobrar, a região suspeita é a união das janelas j e j+1 (400 zeros). Todos
os intervalos dessa região com s > **1,1 d̄** são reexaminados com passo **d̄/128**. Se o degrau persistir, repete-se uma
única vez com passo **d̄/512** e limiar **0,8 d̄**. Se ainda persistir, o resultado do caractere é registrado como
**inconclusivo**, com a região identificada. **Nenhum zero é inserido, movido ou apagado à mão em nenhuma hipótese.**

**Terminação:** Etapa A uma vez, Etapa C no máximo duas rodadas. Não há outra iteração possível.

## 4. Artefatos

Pasta nova `dirichlet/completude/` (o script congelado não é editado; o novo código o **importa**):

- `completude_d3.py` — implementa A, B, C e as re-verificações do §5;
- `test_completude_d3.py` — testes obrigatórios, rodados antes de qualquer execução (§6);
- `zeros_<caractere>_12000_completo.txt` — **os 12.000 primeiros zeros da lista corrigida**, que passam a ser o dado de
  trabalho do instrumento. Como a lista corrigida tem mais de 12.000 elementos, o corte mantém um **segmento inicial
  completo** e o último zero fica mais baixo que o da lista original (em χ₋₄, ≈ 14 zeros mais cedo);
- `recuperados_<caractere>.json` — cada zero recuperado, com intervalo de origem, separação do vizinho e passo usado;
- `manifesto_d3_<caractere>.json` — SHA-256 da entrada e da saída, contagens, tempo, avaliações, resultado de cada
  etapa e das re-verificações;
- `DIAGNOSTICO_V1V2.md` — anexo com a íntegra do diagnóstico do §0.3.

Os blocos do instrumento passam a ser definidos por índice **sobre a lista corrigida**, pela mesma regra da declaração.
A conferência dos 500 primeiros zeros contra o piloto (Adendo 2 §4) continua obrigatória e é refeita sobre a lista
corrigida; se algum zero recuperado tiver índice ≤ 500, isso é registrado de forma explícita (no diagnóstico de χ₋₄ o
primeiro déficit está perto do índice 4.220).

## 5. Re-verificação (critérios idênticos aos da declaração)

- **V1′:** `v1_completeness` do script congelado sobre a lista corrigida, tolerância 3,0, mais o certificado D3-C1.
- **V2′:** mesmo bloco 9001–12000 (índices na lista corrigida), recalculado com passo pela metade (d̄/16) pelo script
  congelado. **O passe de completude (Etapas A–C) é aplicado também à lista recomputada, antes da comparação**, porque
  senão a comparação mede a perda de pares das duas listas e não a estabilidade das posições. Critérios inalterados:
  mesma contagem e max|Δ| ≤ 10⁻⁹. Esta é a única mudança operacional na V2, e é simétrica entre as duas listas.
- **V3′ e V4′:** refeitas sobre a lista corrigida (os índices sorteados e os pontos médios mudam), com as mesmas regras
  — V3 com semente 20260917, V4 pelo Adendo 1.
- O caractere só é declarado **validado** se V1′, D3-C1, V2′, V3′ e V4′ passarem. Qualquer falha remanescente é
  registrada como **inconclusivo** e o dado não entra no instrumento.

## 6. Testes obrigatórios antes de executar

1. **Par conhecido:** no intervalo [3893,1962; 3895,0981] o passe encontra exatamente dois zeros, e eles coincidem com
   3893,887460453 e 3893,977078497 dentro de 10⁻⁸.
2. **Invariância:** nenhum zero da lista original é alterado, reordenado ou removido; a saída contém a original como
   subconjunto, na mesma ordem.
3. **Recuperação de par removido (invariante, não repetição do código):** removendo artificialmente um par vizinho
   conhecido da lista corrigida, o certificado D3-C1 acusa degrau de −2 na janela certa e a Etapa C recupera os dois
   zeros nas posições originais dentro de 10⁻⁸.
4. **θ:** o S calculado pelo novo código coincide com `smooth_count` do módulo congelado em 10⁻¹² num conjunto de
   pontos.

## 7. Custo e ordem de execução

Medido no diagnóstico: ~0,35–0,5 s por avaliação de Z_χ nessas alturas; a Etapa A custa 32 avaliações por d̄ de largura
reexaminada.

| Etapa | χ₋₄ | χ₅ |
|---|---|---|
| Etapa A (limiar 1,6 d̄) | ~1.434 d̄ → ~46.000 avaliações → **~6 h** | estimativa semelhante, a medir |
| V2′ (varredura com passo d̄/16 no bloco alto) | **~17 h** (a V2 original levou 16,9 h) | **~30 h** |
| Etapa A sobre a lista da V2′ | **~6 h** | ~6 h |
| Etapas B, C, V1′, V3′, V4′ | minutos | minutos |

Ordem: (i) testes do §6; (ii) passe completo em χ₋₄; (iii) quando a **varredura** de χ₅ terminar, a execução é
interrompida com SIGTERM **antes de a V2 do script congelado avançar**, e o mesmo passe é aplicado a χ₅. Motivo
declarado agora: a V2 do script congelado não grava os zeros recomputados, então as suas ~30 h produziriam apenas uma
contagem que o §5 exige refazer de qualquer modo sobre listas completas. A varredura de χ₅ **não** é interrompida nem
refeita.

## 8. Previsão registrada agora (rótulo D, falsificável)

Antes de ver qualquer verificação de χ₅:

1. χ₅ apresentará o mesmo déficit, com **entre 5 e 30 zeros perdidos** em 12.000, em degraus de −2.
2. Nenhum zero original de χ₋₄ ou de χ₅ será alterado pelo passe.
3. Em χ₋₄, a Etapa A com limiar 1,6 d̄ recuperará **os 14 zeros** do déficit, sem precisar da Etapa C.

Se (3) falhar, a Etapa C entra como previsto e isso fica registrado como tal; se (1) falhar, o número real é o que vai
para o relatório.

## 9. O que este adendo não autoriza

Não muda tolerância, método, critérios nem blocos; não apaga nem corrige arquivo nenhum do resultado reprovado; não
permite ajuste manual de zeros; não transforma a falha de V1/V2 em resultado positivo. Se o passe não fechar o
certificado, o controle `ctrl-dirichlet-v1` fica **inconclusivo** para o caractere afetado, e é isso que o relatório
dirá.

*Dionatan Resende & Claude Opus — 22/09/2026.*
