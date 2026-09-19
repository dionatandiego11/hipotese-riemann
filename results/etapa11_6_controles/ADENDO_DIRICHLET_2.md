# Adendo 2 ao `ctrl-dirichlet-v1` — adendo operacional: retomada, aceitação do refinamento e benchmark (19/09/2026)

Gravado **antes** de qualquer mudança no código correspondente e antes do cálculo completo. SHA-256 em
`ADENDO_DIRICHLET_2.sha256`.
- Declaração: [DECLARACAO_DIRICHLET.md](DECLARACAO_DIRICHLET.md) (`e6cb8ab8…`).
- Adendo 1: [ADENDO_DIRICHLET_1.md](ADENDO_DIRICHLET_1.md) (`6ee78368…`).

**Nada científico muda:** o método dos zeros (Hurwitz, 30 dígitos, passo ≤ 1/8 do espaçamento, tolerância 10⁻¹⁰), as
verificações V1–V4 (V4 segundo o Adendo 1), os blocos, as sementes, o instrumento e os critérios D-C1, D-C1z, D-C2,
D-C2s e D-C2z continuam os da declaração. Os pilotos de 19/09/2026 e seus arquivos ficam preservados como estão.

## 1. Motivo

- **Custo:** o piloto e a medição por altura indicam dezenas de horas por caractere para 12.000 zeros
  (`dados_piloto/REGISTRO_PILOTO.md`). O script dos pilotos não grava progresso: uma interrupção perderia tudo.
- **Aceitação do refinamento:** em `ZeroFinder.refine` (script `0f16b4c5…` e `7b2de8e2…`), se as 200 iterações se
  esgotassem com o intervalo ainda maior que 10⁻¹⁰, o ponto médio era devolvido **sem aviso**. A exigência da
  declaração (§4, item 3: "refinamento de cada troca de sinal até |Δt| ≤ 10⁻¹⁰") não era verificada no código.

## 2. Mudanças (código, sem efeito sobre o método)

**M1. Aceitação do refinamento.**
1. Até 100 iterações de Illinois, exatamente como antes. Com isso, todo zero que o código antigo refinava em menos de
   100 iterações sai idêntico.
2. Se o intervalo ainda for maior que 10⁻¹⁰, passa-se à bisseção pura, que reduz o intervalo à metade a cada passo, por
   até 100 iterações.
3. Um zero só é aceito se o intervalo final [a, b] tiver b − a ≤ 10⁻¹⁰ e Z_χ tiver sinais opostos em a e b; o valor
   aceito é o ponto médio. Z_χ exatamente nulo num ponto avaliado também é aceito, como antes.
4. Se não houver convergência, a execução **para com erro**, gravando o progresso. Nenhum zero não convergido é gravado.
5. Contam-se as iterações máximas e quantas vezes a bisseção foi usada; os dois números vão para o manifesto.

**M2. Salvamento e retomada.**
1. O estado é gravado em `progresso_<carater>_<n>.json`, na pasta de saída, por escrita atômica (arquivo temporário e
   `os.replace`), a cada 25 zeros novos ou 120 s, o que vier primeiro, e também ao receber SIGINT ou SIGTERM.
2. O estado contém: fase (varredura, lacunas, V1, V2, V3, V4), zeros aceitos em precisão total, ponto corrente da
   varredura, contadores, verificações já concluídas e o estado da varredura de V2.
3. **Retomada** com o mesmo comando. Ela só é permitida se o protocolo, o caractere, n, os parâmetros numéricos e o
   **SHA-256 do script** forem iguais aos gravados; caso contrário, recusa com erro.
4. A varredura é determinística: o próximo ponto depende só do ponto atual. Retomar do ponto gravado produz a mesma
   sequência de avaliações que a execução sem interrupção. Na retomada, Z_χ é recalculado no ponto gravado e comparado
   com o valor salvo, que deve ser igual.
5. Um arquivo de trava (`.lock`, com o PID) impede duas execuções simultâneas na mesma pasta e com o mesmo alvo.
6. Os arquivos finais (zeros, com 9 casas, e manifesto) mantêm o formato atual. O manifesto passa a registrar o número
   de retomadas e o SHA-256 deste adendo.

## 3. Testes obrigatórios antes do cálculo completo

- **T1.** A execução com uma interrupção simulada seguida de retomada produz a mesma lista de zeros, bit a bit, que a
  execução sem interrupção, com n pequeno. O teste é feito com interrupção interna e também com um processo real
  terminado por SIGTERM e depois reiniciado.
- **T2.** A retomada recusa estado com SHA-256 de script, caractere, n ou parâmetro diferentes.
- **T3.** A aceitação do refinamento rejeita um intervalo não convergido. Um caso forçado, com limite de iterações
  artificialmente baixo, deve parar com erro e não gravar zero.
- **T4.** Os 21 testes existentes continuam passando.

## 4. Verificação dos pilotos (sem recalculá-los)

Os arquivos dos pilotos guardam γ̂ com 9 casas decimais, com erro de arredondamento ≤ 5·10⁻¹⁰, e o refinamento
acrescenta ≤ 5·10⁻¹¹. Para cada zero γ̂ dos dois pilotos, conferir com 30 dígitos que Z_χ troca de sinal em
[γ̂ − 6·10⁻¹⁰, γ̂ + 6·10⁻¹⁰]. Nota de redação: a primeira versão deste parágrafo dizia ±10⁻¹⁰, o que ignorava o
arredondamento. Foi corrigida antes de qualquer código ou cálculo.
- **Se todos passarem:** fica documentado que a falha de aceitação descrita em §1 não afetou os pilotos.
- **Se algum falhar:** o fato é registrado, e o piloto correspondente não é usado como referência.

Além disso, os 500 primeiros zeros do cálculo completo devem coincidir, linha a linha, com o arquivo do piloto. É uma
conferência operacional de regressão, não um critério científico. Qualquer diferença é investigada e registrada antes
de usar os dados.

## 5. Benchmark limitado (antes do cálculo completo)

Para cada caractere, perto de t = 1.000, 3.000, 6.000 e T₁₂₀₀₀ (≈ 9.750 para χ₋₄ e ≈ 9.507 para χ₅):
- tempo médio de 10 avaliações de Z_χ depois de uma avaliação de aquecimento;
- varredura real de 5 zeros consecutivos, com o custo em avaliações por zero.

A estimativa do tempo total (varredura mais V2) é registrada em `dados_piloto/BENCHMARK.md` antes de entregar os comandos.
O benchmark não produz dados usados pelo instrumento.
