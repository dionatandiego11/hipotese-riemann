# Análise dos resultados e auditoria da implementação

**Data:** 13/09/2026. **Escopo:** revisão de M1–M3, testes existentes e verificações independentes limitadas aos primeiros 10.000 zeros. As execuções históricas, o código científico e o protocolo congelado foram preservados.

O trabalho produziu uma recuperação numérica consistente de frequências e coeficientes aritméticos. A concordância das amplitudes foi reproduzida com outra implementação de soma e quadratura. Entretanto, existe uma assimetria na calibração estatística que altera uma das detecções do bloco `holdout`. Minha avaliação é: **resultado numérico substantivo, mas M3 ainda precisa de correção inferencial e de robustez antes de ser considerado plenamente validado**.

Os resultados atuais não identificam um Hamiltoniano nem reconstruíram trajetórias de um sistema clássico. Eles recuperam informação de uma representação espectral, dentro de uma faixa e com uma janela específicas.

## 1. O que foi verificado nesta auditoria

- Executei `.venv/bin/python -m pytest -q`: **25 testes aprovados em 20,17 s**.
- Conferi que os primeiros 10.000 valores do arquivo bruto coincidem com o CSV processado; confirmei ordenação, hashes dos dados e correspondência entre o código atual e o lock do protocolo M3.
- Conferi os hashes de `blind_peaks.csv` e `nulls.npz` dos blocos `holdout` e `full`.
- Recalculei média e variância dos espaçamentos diretamente das ordenadas brutas.
- Recalculei amplitudes usando soma explícita e quadratura oscilatória QUADPACK, sem usar o módulo `periods.py` para essa medição. O ajuste recebeu frequências conhecidas, mas não recebeu os coeficientes teóricos como restrição: é uma verificação direcionada, não uma nova detecção cega.
- Reproduzi exatamente cinco máximos do controle de permutação de espaçamentos salvos no `holdout`, usando as sementes correspondentes.
- Comparei as rotas de avaliação dos picos dos dados e dos controles, incluindo um sinal sintético e os artefatos reais.
- Inspecionei os gráficos e consultei fontes primárias para avaliar a interpretação das correções de altura finita.

**Não executei:** reprodução integral das simulações de M2/M3, nova validação mpmath dos 20 índices, instalação em ambiente limpo, expansão dos dados, janela alternativa ou busca de operadores. Os testes aprovados não substituem essas verificações.

Código da auditoria e resultados estão em [results/audit_20260913_resultados](../results/audit_20260913_resultados/). A primeira tentativa do script auxiliar falhou por uma chamada removida do NumPy; o log foi preservado e o auxiliar corrigido antes da execução concluída. Isso não envolveu alteração do programa científico original.

## 2. Resultados que permanecem sustentados

### Dados e frequências

O conjunto analisado contém 10.000 ordenadas, de `14,134725142` a `9877,782654004`. A validação histórica de 20 índices registra erro máximo de aproximadamente `2,50 × 10⁻⁹`; nesta auditoria conferi o registro e os hashes, sem recalcular essa amostra.

| Medida | `holdout`: índices 7.001–10.000 | `full`: índices 1–10.000 |
|---|---:|---:|
| Linhas no catálogo `r log(p)` | 47 | 47 |
| Detecções registradas pela rota refinada | 36 | 41 |
| Detecções pela rota de amplitude usada nos controles, com limiar salvo | 35 | 41 |
| Maior erro de período entre as correspondências registradas | `1,39 × 10⁻⁶` | `1,31 × 10⁻⁷` |
| Variância dos espaçamentos recalculada | `0,1568691` | `0,1541545` |
| Média dos espaçamentos recalculada | `0,9999798` | `1,0000230` |

O detector não depende do catálogo de primos para encontrar os candidatos. A comparação aritmética posterior e a gravação dos candidatos antes dela estão presentes no código. As 41 correspondências do conjunto completo persistem na verificação adicional sem refinamento da amplitude.

Isso sustenta a recuperação de frequências aritméticas no experimento. A interpretação de primos como órbitas de um sistema físico é um passo adicional: a analogia espectral já aparece em [Berry e Keating](https://michaelberryphysics.wordpress.com/wp-content/uploads/2013/06/berry307.pdf).

### Amplitudes: a precisão registrada é numericamente reproduzível

Mantendo a amostragem e o estimador do relatório, mas mudando a implementação da transformada:

| Verificação independente | `holdout` | `full` |
|---|---:|---:|
| Mediana de `abs(C_estimado/C_teórico − 1)`, parte real, linhas selecionadas | `5,17 × 10⁻¹⁰` | `1,90 × 10⁻¹⁰` |
| Maior diferença absoluta entre o coeficiente complexo recalculado e o salvo | `9,28 × 10⁻¹⁴` | `6,63 × 10⁻¹⁴` |

Portanto, os pequenos resíduos não são apenas uma afirmação do relatório: foram reproduzidos por outra implementação. As amplitudes teóricas são usadas na comparação, não impostas ao ajuste.

É necessário, porém, distinguir **resíduo do ajuste** de **incerteza total**. Um ajuste alternativo usando apenas os centros das linhas e incluindo os dois lóbulos conjugados deu mediana de desvio `4,37 × 10⁻⁹` no `holdout`, contra `5,17 × 10⁻¹⁰` no estimador original. No `full`, a mediana foi `2,52 × 10⁻¹⁰`. As linhas fracas apresentaram diferenças maiores.

Esse contraste não demonstra que o estimador alternativo seja melhor; ele mostra que o desenho do ajuste também importa. A sensibilidade a perturbações uniformes de ±`3 × 10⁻⁹` nas ordenadas não fornece, sozinha, um intervalo de confiança nem um limite rigoroso para erros de janela, modelo e truncamento. A alegação de que a precisão é limitada exclusivamente pela tabela ainda precisa dessa análise.

### Estatísticas locais

Os registros de M2 mostram incompatibilidade com Poisson e desvios em relação ao GUE finito usado. A menor variância dos espaçamentos dos zeros foi confirmada nesta auditoria. Essa medida estabelece menor dispersão local; não basta, isoladamente, para concluir sobre toda a rigidez espectral de longo alcance.

Não se deve resumir M2 como “os zeros seguem GUE perfeitamente”: CDF e form factor têm valores-p registrados no piso `0,01`; a correlação de pares no bloco completo tem `0,04`. Tampouco isso refuta uma conjectura assintótica. O nulo implementado é um ensemble finito específico, e os zeros estão em baixa altura comparada aos testes clássicos de grande altura.

## 3. Achados que exigem ação

### Prioridade 1 — A calibração de M3 compara estatísticas diferentes

**Local:** `src/riemann_spectra/inverse_spectroscopy.py`, linhas 75–82 e 237–250; `src/riemann_spectra/periods.py`, linha 355.

Nos controles, `detect_blind_peaks` recebe a transformada na malha e conserva a amplitude do ponto amostrado. Nos zeros, recebe um `evaluator` que recalcula a amplitude na posição refinada. O máximo usado na distribuição nula também é calculado na malha. Logo, o valor observado e sua referência nula não seguem exatamente o mesmo procedimento.

**Evidência reproduzida:** para o mesmo sinal Hann, a rota dos controles produz `z = 3,9614378` e a rota dos zeros produz `z ≈ 4,0000000`: diferença de **0,973%**. Em cinco realizações nulas salvas e reproduzidas, o refinamento também alterou alguns máximos.

**Efeito em um resultado real:** no `holdout`, a linha `log(131)` tem:

- `z` na malha: `3,2892471`;
- `z` refinado: `3,2946557`;
- limiar salvo: `3,2914601`;
- valor-p ajustado originalmente reportado: `0,049`.

A linha atravessa o limiar apenas após a avaliação refinada. Usando a rota de amplitude dos controles, a contagem passa de 36 para 35. Isso não é uma recalibração completa nem estabelece um novo valor-p: é uma demonstração de que a assimetria afeta uma conclusão do relatório.

**Correção recomendada:** escolher uma única estatística para dados, controles e sintéticos. Pode-se manter a significância na malha e usar refinamento apenas para localização/apresentação; alternativamente, refinar também os máximos nulos. Recalcular limiares, valores-p e contagens, preservando a versão anterior.

**Questão adicional do escore global:** os mesmos máximos nulos que definem o limiar são usados para produzir a distribuição de contagens `S` (`inverse_spectroscopy.py`, linhas 375–387). O valor observado não participa da construção desse limiar. Não há justificativa de permutabilidade exata desses escores no projeto. Para uma calibração clara, usar conjuntos distintos para estimar ruído, escolher limiar e calibrar o escore global, ou justificar um procedimento simétrico de reamostragem.

O piso reportado `p = 0,001` é a resolução da simulação original. Ele não é uma probabilidade de a interpretação física estar errada, nem fica automaticamente validado pelo fato de o efeito ser grande.

### Prioridade 1 para M4 — A configuração ainda não controla toda a análise anunciada

**Local:** `inverse_spectroscopy.py`, linhas 51–55; `spectral_pipeline.py`, linha 36; `cli.py`, linhas 62–88.

Há três obstáculos concretos ao próximo marco:

1. **`window` e `density` do TOML M3 não são propagados ao instrumento.** A fábrica cria `OscillatoryTransform` com os padrões Hann/RVM. Mudar a configuração para uma janela alternativa ou para `theta` não executa a comparação pretendida. O diagnóstico interno calcula uma diferença entre densidades, mas isso não equivale a executar toda a cadeia com outra densidade.
2. **Os blocos de M2 estão fixos nos primeiros 10.000 índices.** Carregar 100.000 zeros por `extended.toml` não faz M2 analisar automaticamente a faixa nova.
3. **Aquisição e validação reutilizam nomes únicos de manifesto.** Executar `data fetch` com o perfil estendido sobrescreve `data/raw/data_manifest.json`; executar a nova validação sobrescreve `data/processed/data_validation.json`. Isso remove os registros correntes associados à base anterior e pode fazer M1 consultar a validação de outro conjunto.

**Correção recomendada:** propagar e validar todas as opções, recusar opções não implementadas, selecionar blocos pela configuração e separar manifestos/validações por identidade do conjunto. A compatibilidade entre dados carregados e sua validação deve ser verificada explicitamente.

Esses pontos não mudam a janela usada nas execuções atuais, que de fato é Hann/RVM. Eles impedem tratar a expansão como apenas uma troca de arquivo TOML.

### Prioridade 2 — A correção de dimensão efetiva citada é de CUE

**Local:** próximo passo em `docs/ANDAMENTO.md`, item “GUE de dimensão efetiva de Bogomolny et al.”.

O artigo de [Bogomolny, Bohigas, Leboeuf e Monastra](https://arxiv.org/pdf/math/0602270), §2, constrói a comparação de tamanho finito com **CUE** e distingue explicitamente sua expansão da expansão do **GUE**. Não é correto aplicar a referência apenas substituindo a dimensão das matrizes GUE por `N_eff`.

Usando a fórmula citada nos centros das janelas atuais, obtém-se aproximadamente `N_eff = 1,66` no `holdout` e `1,53` no `full`. Esses números, calculados nesta auditoria, também mostram que uma expansão de grande dimensão exige cautela nessa faixa.

**Correção recomendada:** implementar a previsão e suas hipóteses conforme o artigo, usando CUE quando necessário, e avaliar seu domínio de validade. Manter separadas a discrepância numérica observada e uma explicação teórica ainda não testada quantitativamente. A referência apresenta argumentos assintóticos, não uma prova de que qualquer desvio medido nestes blocos tenha essa causa.

### Prioridade 2 — Algumas interpretações ultrapassam a evidência registrada

**Local:** `docs/ANDAMENTO.md`, linhas 65–68 e classificação da fórmula explícita; `docs/REFERENCIAS.md`, itens Selberg e Guinand–Weil.

- **Pico em `tau = 1`:** medir a variância de `Nbar(gamma_n) − (n − 1/2)` e uma coerência de fase não transforma a explicação em consequência demonstrada do teorema de Selberg. A variância não determina a função característica em uma frequência fixa. Além disso, a formulação usual para alturas amostradas em um intervalo não se transfere automaticamente para amostragem nos zeros. O enquadramento do teorema pode ser conferido em [Lugar, Milinovich e Quesada-Herrera](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/mtk.12184), §1.1. A interpretação deve permanecer heurística até haver derivação e teste adequados.
- **Identidade de Guinand–Weil na janela Hann:** o projeto ainda não estabelece a classe de funções-teste, os termos necessários e os erros que justificariam a identificação exata da observável finita com a expressão formal. Saber que os zeros tabelados dessa faixa estão na linha crítica não substitui essa justificativa. Classificar a concordância medida como **B**, reservando **A** para um enunciado preciso com hipóteses e fonte.
- **Coerência versus fase correta:** a estatística `abs(mean(exp(i erro_de_fase)))` é invariante a uma rotação comum de todas as fases. Ela mede alinhamento, não testa sozinha o sinal absoluto dos coeficientes. O ajuste direcionado fornece informação adicional sobre esse sinal e deve continuar sendo apresentado separadamente.

### Prioridade 2 — Contratos de validação e relato precisam ser ajustados

- Em `data.py`, linhas 169 e 173, o código aceita até **duas vezes** o erro declarado, mas usa nomes e mensagem que sugerem teste do limite declarado. A amostra atual passa mesmo no limite de `3 × 10⁻⁹`; o defeito está no critério para futuras validações. Remover o fator ou documentar outra tolerância com justificativa.
- Em `spectral_pipeline.py`, `_envelope_test`, a observação é comparada à média de `B` nulos, enquanto cada nulo é comparado à média dos outros `B−1`. Isso não é um teste de posto exatamente simétrico. Tratar os valores-p como aproximações até validar a calibração ou usar referência independente/simetrização. O resultado limítrofe `0,04` merece atenção especial; 99 simulações dão resolução limitada.
- Em `utils.py`, linha 138, a memória é medida com `RUSAGE_SELF`. Com quatro processos, “pico ≤330 MB” descreve o processo principal, não o pico agregado de toda a execução.
- Há hashes de código, mas não há repositório Git nem cópias históricas completas dos fontes por execução. Hash permite conferir identidade; não permite recuperar uma versão antiga depois de alterá-la. Preservar snapshots do código ou versioná-lo antes da próxima revisão.

## 4. Interpretação científica do avanço

A resposta parcial à pergunta “quanto se recupera a partir dos zeros?” é: **neste instrumento, recuperam-se várias frequências associadas a primos e potências, e os coeficientes direcionados apresentam concordância numérica muito alta com a referência aritmética**. O conjunto completo oferece evidência numérica consistente dessa recuperação.

Não foram recuperados espaço de fases, trajetórias, condições de contorno, matriz de estabilidade orbital ou um operador definido independentemente dos zeros. Frequências e coeficientes não selecionam automaticamente uma classe única de Hamiltonianos. As correspondências de traço e seus obstáculos são discutidos por [Berry e Keating](https://michaelberryphysics.wordpress.com/wp-content/uploads/2013/06/berry307.pdf).

Não identifiquei nesta auditoria um novo resultado matemático ou um achado experimental cuja originalidade esteja estabelecida. O principal ganho é uma implementação que reproduz uma estrutura conhecida e pode servir de instrumento para investigações posteriores, depois das correções.

## 5. Próxima sequência recomendada

1. Criar uma nova versão de protocolo para corrigir a simetria entre dados/nulos e a calibração global. Manter `m3-v2` e suas execuções preservados.
2. Acrescentar testes que exponham o caso de pico fora da malha, a propagação de configurações e a vinculação da validação ao conjunto de dados.
3. Reexecutar os blocos já explorados para medir o impacto da correção. Eles continuam exploratórios/validação: o `holdout` histórico já foi consultado e isso está corretamente reconhecido no projeto.
4. Implementar janela alternativa, seleção de blocos e manifestos por conjunto. Congelar as regras antes de analisar uma nova faixa.
5. Usar segmentos novos entre 10.001–100.000 para confirmação e robustez, separando efeitos da altura, do comprimento da janela e do estimador de amplitudes.
6. Só então avaliar classes de operadores. Tratar a correção de altura finita com o modelo adequado e manter a busca de Hamiltonianos subordinada a previsões independentes.

## 6. Artefatos e reprodução da auditoria

- [Script principal](../results/audit_20260913_resultados/run_audit.py), [métricas](../results/audit_20260913_resultados/metrics.json), [manifesto](../results/audit_20260913_resultados/manifest.json) e [coeficientes independentes](../results/audit_20260913_resultados/coefficients_independent.csv).
- [Verificação das rotas do detector](../results/audit_20260913_resultados/check_detection_routes.py) e [resultado, incluindo log(131)](../results/audit_20260913_resultados/detection_routes.json).
- [Relatório M3 original](../results/run_20260913_024706_m3_holdout-full/report.md) e [registro de andamento consultado nesta auditoria](ANDAMENTO.md).

```bash
.venv/bin/python -m pytest -q
.venv/bin/python results/audit_20260913_resultados/run_audit.py
.venv/bin/python results/audit_20260913_resultados/check_detection_routes.py
```

Os scripts auxiliares gravam apenas seus próprios artefatos na pasta da auditoria. Os estados do andamento original não foram alterados; este parecer recomenda reabrir a validação inferencial de M3 e registrar separadamente o que já foi confirmado numericamente.
