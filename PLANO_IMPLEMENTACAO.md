# Plano de implementação — espectroscopia inversa dos zeros da zeta

**Estado:** M1–M3 executados; Etapa 10 de M4 concluída, incluindo m4-v3 com R2 acionada e investigada; Etapa 11 e M5 pendentes. Estado detalhado em [docs/ANDAMENTO.md](docs/ANDAMENTO.md) e [relatório consolidado, §5](docs/RELATORIO_CONSOLIDADO.md). Frente complementar Collatz adicionada em 14/09/2026, ainda pendente.

**Objetivo inicial:** construir um instrumento confiável que meça estatísticas espectrais e recupere períodos, amplitudes e fases a partir de uma lista finita de zeros. A interpretação desses resultados em termos de dinâmica e operadores vem depois.

**Resultado aceitável:** uma medição quantitativa, inclusive negativa ou inconclusiva, acompanhada de resolução, incerteza, controles e comando de reprodução. Encontrar um Hamiltoniano não é condição para o projeto produzir conhecimento útil.

## 1. Marcos e dependências

| Marco | Etapas deste plano | Entrega verificável |
|---|---|---|
| M1 — Fundação | 0–3 | Protocolo, ambiente, dados auditados e controles |
| M2 — Estatística espectral | 4–6 | Unfolding, espaçamentos, correlação de pares e form factor validados |
| M3 — Espectroscopia inversa | 7–9 | Catálogo de picos sem primos na entrada, comparação aritmética e testes de significância |
| M4 — Robustez e interpretação | 10–11 | Replicação, anomalias, controle físico e avaliação dos operadores |
| M5 — Síntese | 12–13 | Busca limitada, se viável, relatório final e limites da interpretação |
| CL — Laboratório de dinâmica aritmética | CL0–CL5 no plano complementar | Zetas e operadores com casos exatos, filtros aritméticos, transientes e limites da reconstrução inversa |

Execute primeiro um piloto com 1.000 zeros para depurar o fluxo; a base mínima da investigação contém 10.000. A expansão para 100.000 é uma etapa de robustez. Não espere concluir a busca por Hamiltonianos para produzir os relatórios intermediários.

Os critérios de avanço verificam o método. Um resultado que contradiga a hipótese investigada deve ser relatado e pode encerrar uma linha de pesquisa sem invalidar a etapa.

## 2. Convenções que precisam ser preservadas

### Duas coordenadas, duas perguntas

Para estatística local, use

\[
x_n=\bar N(\gamma_n),\qquad
\bar N(E)=\frac{E}{2\pi}\log\frac{E}{2\pi}-\frac{E}{2\pi}+\frac78,
\qquad \bar d(E)=\frac{1}{2\pi}\log\frac{E}{2\pi}.
\]

Para períodos aritméticos, use `E = gamma`, com transformada `exp(-i E t)`. Nessa convenção, o período candidato é `t = r log(p)`. Se uma FFT usar `exp(-2π i E f)`, converta com `t = 2π f`. O unfolding é não linear e modifica essas frequências.

### Identidade formal e instrumento numérico

A expressão de referência é

\[
d_{\mathrm{osc}}(E)\sim
-\frac1\pi\sum_{p}\sum_{r\geq1}
\frac{\log p}{p^{r/2}}\cos(E r\log p).
\]

A soma requer uma interpretação regularizada; não é uma série ordinária convergente na linha crítica. Períodos, coeficientes e sinal aparecem na analogia de traço discutida por [Berry e Keating, especialmente §2](https://michaelberryphysics.wordpress.com/wp-content/uploads/2013/06/berry307.pdf). A etapa 7 define uma observável finita que pode ser calculada sem somar essa série.

### Controles que realmente mudam a hipótese testada

- Permutar os zeros conserva o mesmo conjunto e, portanto, o espectro. Isso serve como teste de invariância do código.
- Permutar espaçamentos e reconstruir níveis conserva a distribuição dos espaçamentos, mas altera sua organização.
- Randomizar fases de Fourier preservando módulos conserva o espectro de potência. Esse controle serve para testar fase/coerência, não desaparecimento de picos de potência.
- Uma janela com vários picos testados exige correção pela seleção e pelas comparações múltiplas.

### Evidência e identificabilidade

Uma lista finita de autovalores não determina, sem restrições adicionais, um Hamiltoniano físico único. É possível construir matrizes distintas com os mesmos autovalores. O projeto deve medir quais classes e propriedades continuam compatíveis, em vez de pressupor reconstrução única.

## 3. Etapas para o agente implementar

### Etapa 0 — Fixar o protocolo e a pergunta mensurável

**Tarefas**

1. Criar `docs/PROTOCOLO.md`, `docs/ANDAMENTO.md` e `docs/REFERENCIAS.md`.
2. Registrar três perguntas: a estatística local é compatível com os controles GUE? Um detector sem catálogo recupera frequências aritméticas? Amplitudes e fases resistem à mudança de janela e ao teste reservado?
3. Separar índices contíguos: `1–1.000` para diagnóstico de baixa altura; `1.001–4.000` para desenvolvimento; `4.001–7.000` para validação; `7.001–10.000` para teste reservado. São blocos disjuntos de um espectro determinístico, não amostras independentes garantidas.
4. Fazer análise descritiva dos 10.000 apenas depois de congelar o protocolo do teste reservado. Não usar os primeiros 1.000 como justificativa para excluir resultados desfavoráveis.
5. Fixar métricas primárias, janelas, intervalos, procedimento de seleção, tolerância de matching e famílias de testes antes de abrir o teste reservado.
6. Registrar configurações iniciais: semente `20260912`; janela Hann; períodos entre `0,5` e `5,0`; `alpha = 0,05` para a família primária; 99 realizações nulas no piloto e pelo menos 999 na inferência principal. São escolhas operacionais propostas, não constantes matemáticas.
7. Fixar uma regra de incerteza: controles simulados para calibração; sensibilidade por blocos para os zeros. Se usar bootstrap em blocos, justificar comprimento e limitações para correlações de longo alcance.

**Entregáveis:** protocolo versionado e registro com as etapas pendentes. O congelamento deve salvar o hash da configuração antes da comparação confirmatória.

**Aceite:** outra pessoa consegue identificar o que será testado, em quais dados e quais decisões já foram fixadas. Mudanças futuras criam nova versão e tornam exploratória qualquer análise que reutilize um teste já consultado.

### Etapa 1 — Criar a estrutura reproduzível

**Tarefas**

1. Criar pacote Python, configuração de dependências e ambiente local. O ambiente inspecionado possui Python 3.12.3; verificar compatibilidade das bibliotecas antes de fixar versões.
2. Usar inicialmente NumPy, SciPy, mpmath, Matplotlib e pytest; adicionar dependências apenas quando houver necessidade concreta.
3. Implementar configuração, logging, sementes, hashes, manifesto e CLI. Todo gráfico deve poder ser regenerado sem notebook.
4. Criar perfis `pilot`, `main` e `extended`. Medir tempo e memória no piloto antes de estimar a execução maior.
5. Como padrão conservador, limitar blocos temporários a aproximadamente 128 MiB e almejar menos de 2 GiB por processo. Revisar com base em medição, sem lançar cálculos grandes silenciosamente.

**Estrutura prevista**

```text
pyproject.toml
arquivo de dependências fixadas
configs/                     # pilot, main, extended e protocolos congelados
src/riemann_spectra/
    cli.py
    data.py
    unfolding.py
    controls.py
    statistics.py
    form_factor.py
    periods.py               # detector sem conhecimento de primos
    arithmetic.py            # comparação posterior e fórmula de referência
    inference.py
    candidates.py
    reporting.py
tests/
data/raw/
data/processed/
results/<run_id>/
docs/
```

**Aceite:** instalação em ambiente limpo; CLI com ajuda; execução pequena produz manifesto e resultados repetíveis dentro de tolerâncias declaradas. Guardar versões de Python, bibliotecas e BLAS, configuração completa, hash do código e dos dados.

### Etapa 2 — Obter e auditar os zeros

**Tarefas**

1. Baixar a tabela oficial de [Andrew Odlyzko](https://www-users.cse.umn.edu/~odlyzko/zeta_tables/), que disponibiliza os primeiros 100.000 zeros com erro declarado de até `3 × 10⁻⁹` nas ordenadas. Preservar o arquivo original.
2. Importar as ordenadas como dados numéricos mantendo índices globais. Extrair os primeiros 10.000 para a análise principal e reservar os restantes para expansão.
3. Salvar URL, data, SHA-256, número de registros, intervalo de alturas, precisão publicada, formato e qualquer transformação aplicada.
4. Verificar dados finitos, ordenação estrita e quantidade esperada. Duplicatas ou lacunas devem gerar diagnóstico; não remover entradas silenciosamente.
5. Recalcular uma amostra determinística estratificada de aproximadamente 20 índices com 40 casas de trabalho usando [`mpmath.zetazero`](https://mpmath.org/doc/current/functions/zeta.html#zetazero). Incluir extremos e índices internos. Comparar erros absolutos com a precisão da fonte.
6. Separar validação da amostra, confiança na completude da tabela publicada e eventual certificação rigorosa. Resíduo pequeno de zeta não certifica sozinho a localização nem a completude de todos os zeros.

**Entregáveis:** arquivo bruto, tabela processada, `data_manifest.json` e `data_validation.json`.

**Aceite:** pelo menos 10.000 registros válidos e auditáveis; divergências superiores à tolerância declarada investigadas antes de continuar. Calcular tudo do zero é alternativa de contingência, sujeita a benchmark.

### Etapa 3 — Implementar os controles antes das conclusões

**Tarefas**

1. Gerar processo Poisson de intensidade unitária. Declarar se a contagem é aleatória ou se o processo está condicionado a uma contagem fixa; aplicar a mesma convenção na comparação.
2. Gerar GUE com normalização explícita. Validar uma implementação densa pequena; para maior escala, usar o modelo tridiagonal com `beta = 2` de [Dumitriu e Edelman](https://arxiv.org/abs/math-ph/0206043).
3. Usar a região central do espectro de cada matriz e seu unfolding apropriado. Registrar dimensão da matriz, fração retida e correções de tamanho finito.
4. Gerar o controle de permutação dos espaçamentos unfolded seguido de soma cumulativa. Registrar efeitos do condicionamento ao comprimento total.
5. Para controles em energia original, aplicar a inversa numérica de `Nbar` em `E > 2π`, respeitando a mesma janela de observação e tratamento de contagem.
6. Implementar controle de fase sobre o sinal apropriado, preservando simetria conjugada para sinal real. Identificá-lo como sinal substituto se não produzir uma medida espectral positiva de níveis discretos.
7. Construir sinais sintéticos com frequências, amplitudes e fases conhecidas, incluindo linhas isoladas, vizinhas e abaixo do limiar de detecção.

**Verificações:** permutar níveis deixa observáveis invariantes; inverter e reaplicar `Nbar` recupera níveis; o Poisson recupera densidade esperada; GUE denso e tridiagonal dão estatísticas compatíveis na mesma convenção.

**Aceite:** controles podem ser repetidos por semente e submetidos à mesma cadeia de análise. Não concatenar matrizes GUE independentes e interpretar o resultado como um único espectro com correlações de longo alcance.

**Entrega M1:** base pronta, controles verificados e piloto executável. Atualizar o README com comandos que realmente existem.

### Etapa 4 — Unfolding e espaçamentos

**Tarefas**

1. Implementar `Nbar`, sua derivada e inversa no domínio adotado; transformar `gamma` em `x`.
2. Calcular `s_n = x_(n+1) - x_n`, média, variância, histograma e distribuição acumulada por bloco.
3. Comparar com Poisson, `P(s) = exp(-s)`, e com a aproximação de Wigner para GUE,

\[
P_{\mathrm W}(s)=\frac{32}{\pi^2}s^2 e^{-4s^2/\pi}.
\]

4. Identificar essa fórmula como aproximação, não distribuição exata dos espaçamentos do GUE de grande dimensão. Usar também os controles GUE efetivamente simulados.
5. Reportar distância de Wasserstein e distância entre CDFs. Calibrar qualquer valor-p por controles submetidos ao mesmo estimador; não aplicar automaticamente tabelas de KS para observações independentes.
6. Comparar a densidade assintótica com a alternativa `Nbar = 1 + theta(E)/π`, usando o ramo contínuo da fase de Riemann–Siegel. A definição de `theta` e de `Z(t)` está na [DLMF §25.10](https://dlmf.nist.gov/25.10). Registrar a convenção de ramo.

**Entregáveis:** tabela de espaçamentos, métricas, CDFs, histogramas e resíduos por bloco.

**Aceite:** médias e desvios são reportados antes de qualquer renormalização adicional. Não forçar média exatamente 1 para esconder deriva. Explicar desvios de baixa altura e sensibilidade ao unfolding.

### Etapa 5 — Correlação de pares

**Tarefas**

1. Estimar pares distintos, com convenção explícita para pares ordenados ou não ordenados e separações positivas ou assinadas.
2. Adotar inicialmente separação positiva `0 < s <= 5`, excluindo a diagonal. Para uma janela unfolded de comprimento `L`, corrigir a redução da exposição de pares com `L - s`; registrar também a normalização de intensidade e de contagem fixa, se usada.
3. Comparar com

\[
R_2(s)=1-\left(\frac{\sin\pi s}{\pi s}\right)^2.
\]

4. Usar a média teórica dentro de cada bin, em vez de apenas o valor no centro, quando a curvatura importar.
5. Reportar resíduos e erro integrado em faixas previamente fixadas; produzir envelopes de simulação.
6. Usar busca por intervalo ou dois ponteiros em dados ordenados. Não materializar uma matriz `N × N` de diferenças.

O trabalho original de [Montgomery](https://websites.umich.edu/~hlm/paircor1.pdf) distingue resultados sob RH e restrições do domínio de Fourier da conjectura mais ampla. O relatório deve preservar essas hipóteses ao classificar afirmações como conhecidas.

**Aceite:** Poisson recupera o patamar esperado com a correção adotada; GUE recupera seu comportamento de referência dentro do envelope e da resolução finita. Escolhas de bin não podem ser ajustadas apenas para melhorar a aparência dos zeros.

### Etapa 6 — Spectral form factor com janela finita

**Tarefas**

1. Trabalhar nas coordenadas unfolded e definir, para cada janela `b`,

\[
Z_b(\tau)=\sum_n w_b(x_n)e^{-2\pi i\tau x_n},\quad
\mu_b(\tau)=\int w_b(x)e^{-2\pi i\tau x}\,dx,\quad
Q_b=\int w_b(x)^2\,dx.
\]

2. Implementar como estimador inicial da contribuição conectada

\[
\widehat K_c(\tau)=
\frac{\sum_b|Z_b(\tau)-\mu_b(\tau)|^2}{\sum_b Q_b}.
\]

3. Documentar janela, sobreposição, média entre blocos e suavização em `tau`. Janelas sobrepostas não contam como realizações independentes.
4. Comparar o limite GUE `K(tau) = min(|tau|, 1)` com sua versão convoluída pela janela, ou com controles finitos equivalentes. Para Poisson não condicionado, a referência conectada é 1; se houver contagem fixa, medir a correção perto de zero.
5. Manter a contribuição diagonal no form factor para representar o plateau. Registrar separadamente o termo desconectado e a curva sem sua remoção.
6. Explicar que a existência de dip depende da definição e da contribuição desconectada. Não exigir dip no estimador conectado acima.

**Entregáveis:** curvas brutas e suavizadas, normalização, comparação finita, envelopes e resíduos.

**Aceite:** a implementação passa pelos controles antes de interpretar ramp ou plateau nos zeros; não há ajuste posterior da escala vertical para impor plateau unitário.

**Entrega M2:** relatório de estatística espectral com incertezas e faixas de comparação válidas.

### Etapa 7 — Separar a densidade média e construir a transformada

**Tarefas**

1. Definir janela em energia original `[A,B]` e centro `E_c`. Calcular diretamente

\[
F_w(t)=\sum_{A\leq\gamma_n\leq B}
w(\gamma_n)e^{-i(\gamma_n-E_c)t}
-\int_A^B w(E)\bar d(E)e^{-i(E-E_c)t}\,dE.
\]

2. Usar somas em blocos de frequências e quadratura com convergência verificada. Salvar partes real e imaginária; guardar o centro `E_c` para recuperar a fase na coordenada original.
3. Para visualizar a densidade, usar um kernel explicitamente normalizado e aplicar a mesma suavização ao termo médio. A transformada direta acima é a referência; um histograma não deve definir o resultado principal.
4. Medir a resposta da janela: posição, largura do lóbulo principal, lóbulos laterais e ganho. A escala `2π/(B-A)` é uma referência de resolução, não uma garantia de separação de duas linhas para qualquer janela.
5. Usar malha com vários pontos por largura medida e refinamento local. Zero-padding ou interpolação não aumentam a resolução física.
6. Se usar FFT de sinal em energia regular, controlar aliasing (`t_max < π/ΔE`), erro de discretização e efeito do kernel. Validar contra soma direta em uma amostra.
7. Repetir com janela alternativa e densidade média mais precisa. Qualquer referência construída por soma sobre primos deve declarar amortecimento/truncamento e demonstrar estabilidade, incluindo efeitos das bordas.

**Entregáveis:** transformada complexa, densidade visual, resposta instrumental e benchmark de tempo/memória.

**Aceite:** sinais sintéticos recuperam frequência, amplitude e fase dentro de tolerâncias fixadas antes da aplicação aos zeros. Duas linhas não resolvidas são marcadas como mistura. Refinar malha e quadratura não muda conclusões além da tolerância.

### Etapa 8 — Detectar períodos sem consultar primos

**Tarefas**

1. Implementar um detector que receba apenas espectro, janela, malha e parâmetros de ruído. Ele não recebe `log(p)`, uma peneira de primos ou limites centrados em primos conhecidos.
2. Localizar candidatos, estimar posição, largura, amplitude complexa, proeminência e estabilidade entre janelas.
3. Calibrar o limiar nos sinais sintéticos e controles. Não aumentar a quantidade de picos até atingir a quantidade de primos esperada.
4. Gravar `blind_peaks.csv`, configuração e hash antes de executar o módulo aritmético. Esse procedimento é cegamento do algoritmo ao catálogo, não desconhecimento da teoria por parte do pesquisador.
5. Implementar posteriormente uma alternativa de inversão harmônica, como matrix pencil ou ESPRIT, se a recuperação sintética justificar. Fixar seleção de ordem, regularização e diagnóstico de condicionamento; comparar com a transformada direta.

[Main e colaboradores](https://arxiv.org/abs/chao-dyn/9709009) apresentam inversão harmônica aplicada à quantização por órbitas periódicas. O sentido da inferência estudado aqui é diferente: recuperar frequências a partir dos zeros exige uma validação própria.

**Entregáveis:** catálogo sem rótulos aritméticos e curva de recuperação versus ruído, amplitude e separação nos sinais sintéticos.

**Aceite:** catálogo congelado e ausência de dependência aritmética verificável por inspeção das entradas e do código. A alternativa de inversão harmônica pode ser registrada como inconclusiva; isso não impede relatar o resultado do detector de referência.

### Etapa 9 — Comparar com primos, repetições e modelos nulos

**Tarefas**

1. Só após congelar o catálogo, gerar pares `(p,r)` com `r >= 1` e `r log(p)` na faixa observada. Identificar `r = 1` como frequência primitiva e `r > 1` como repetição candidata.
2. Fazer matching com tolerância baseada na resolução e no erro medidos nos sintéticos. Usar correspondência um a um para linhas resolvidas e marcar misturas; não atribuir um mesmo pico a vários primos por conveniência.
3. Salvar erro absoluto `abs(t_obs - r log(p))`, erro em unidades de resolução, falsos positivos, não detecções e regiões sem sensibilidade suficiente.
4. Estimar coeficientes corrigindo janela, fator de Fourier, sobreposição e fase do centro. O coeficiente do cosseno de referência é `-log(p)/(π p^(r/2))`; para um mesmo primo, a razão de módulos entre a repetição `r` e a fundamental é `p^(-(r-1)/2)` antes dos efeitos instrumentais.
5. Preferir ajuste conjunto da resposta conhecida da janela para linhas sobrepostas. Não comparar altura bruta do pico com coeficiente teórico e não substituir amplitude por potência.
6. Separar dois testes: detecção em toda a faixa sem catálogo e medição direcionada nos períodos conhecidos. Relatar os dois sem confundir suas taxas de seleção.
7. Aplicar a cadeia completa aos controles, incluindo seleção e matching. Para um escore em que valores altos indiquem maior evidência, usar

\[
p_{\mathrm{MC}}=\frac{1+\#\{S_{\mathrm{nulo}}\geq S_{\mathrm{obs}}\}}{B+1}.
\]

8. Fixar um escore global, como número de matches resolvidos acima do limiar, e valores-p ajustados por pico mediante o máximo da estatística ao longo da faixa em cada controle. Se houver várias janelas selecionáveis, incluir essa seleção no nulo. Com 999 realizações, não reportar valores-p menores que `0,001`.
9. Medir intervalos de incerteza Monte Carlo e reportar o nulo usado. Os valores-p avaliam incompatibilidade com esse nulo; não são a probabilidade de a interpretação física estar correta.
10. Comparar coerência de fase com o controle de fase, respeitando o fato de que ele conserva potência.

**Tabela mínima**

```text
run_id, bloco, primo, repeticao, periodo_teorico, periodo_observado,
erro_absoluto, erro_em_resolucoes, largura, amplitude_real,
amplitude_imaginaria, modulo_corrigido, fase_corrigida,
coeficiente_teorico, p_ajustado, detectado, resolvido, limite_deteccao
```

**Aceite:** concluir o teste reservado com protocolo congelado e relatar precisão de localização, taxa de recuperação e limitações. Uma ausência de pico só restringe a hipótese se o instrumento conseguir detectar a amplitude prevista naquela região.

**Entrega M3:** experimento mínimo completo com 10.000 zeros, controles, picos, comparação quantitativa e relatório. Não condicionar sua conclusão à obtenção de significância positiva.

### Etapa 10 — Ampliar, procurar anomalias e medir robustez

**Tarefas**

1. Aplicar o protocolo congelado aos zeros `10.001–100.000`, se o benchmark permitir. Usar blocos comparáveis para separar efeitos de altura e de largura da janela.
2. A análise dos primeiros 100.000 contém a base anterior; identificá-la como expansão aninhada. A faixa adicional é uma validação fora da faixa original, sem assumir independência estatística completa.
3. Repetir com janelas alternativas, precisões coerentes com a fonte e variação controlada dos parâmetros. Perturbações de precisão são análise de sensibilidade, não simulações de erro conhecido sem modelo.
4. Procurar desvios de GUE, linhas sem correspondente, linhas previstas ausentes, fases incompatíveis, deriva por altura e mudanças de escala. Usar diagnóstico de variância do número de níveis para aprofundar anomalias de longo alcance.
5. Reavaliar candidatos a anomalia em regiões não usadas para descobri-los; registrar tentativas que não replicaram.
6. Consultar a literatura de cada anomalia antes de sugerir novidade.

**Entregáveis:** `robustness.csv`, `anomalies.csv`, comparação 10.000 versus faixa adicional e limites de recursos medidos.

**Aceite:** distinguir erro numérico, efeito da janela, tamanho finito, falta de potência e possível sinal persistente. Se 100.000 não couberem no orçamento disponível, registrar extensão não executada e manter as conclusões restritas à base analisada.

### Etapa 11 — Comparar fórmulas de traço e classes de operadores

**Tarefas**

1. Criar uma tabela de correspondências com: primo/orbita primitiva, `r`/repetição, `T = log(p)`, ação candidata `S_p(E) = E log(p)` com `hbar = 1`, coeficientes, fase, estabilidade e multiplicidade. Distinguir identidade aritmética de interpretação física hipotética.
2. Examinar a discrepância de sinais nas repetições e a diferença entre amplitudes exatas da fórmula aritmética e amplitudes semiclassicas. [Berry e Keating, §2](https://michaelberryphysics.wordpress.com/wp-content/uploads/2013/06/berry307.pdf) explicitam esses obstáculos; uma atribuição de fase deve funcionar para todas as repetições.
3. Avaliar cada linha da matriz abaixo com referências primárias, hipóteses, observáveis calculáveis e motivos de exclusão. “Não especificado” é uma resposta válida; uma classe ampla não é um candidato concreto.

| Classe | Verificação inicial exigida |
|---|---|
| Berry–Keating `xp` e quantização simetrizada | Domínio, condições de contorno, regularização e origem de eventual espectro discreto |
| Operadores diferenciais | Ordem, domínio, potencial, condições de contorno e lei de contagem |
| Operadores integrais | Kernel, espaço funcional, auto-adjunticidade, compacidade e comportamento espectral |
| Sistemas hiperbólicos | Dinâmica definida, quantização, órbitas e simetrias |
| Bilhares quânticos | Geometria, condição de contorno, variável espectral e setores de simetria |
| Superfícies de curvatura negativa | Operador, área/volume, geodésicas e multiplicidades |
| Sistemas com fórmula de Selberg | Hipóteses da fórmula, espectro usado e dados geométricos necessários |
| Operadores pseudodiferenciais | Símbolo, ordem, domínio e lei espectral correspondente |

4. Para todas as linhas, preencher colunas: contagem média, GUE, simetrias antiunitárias, períodos, amplitudes, fases, multiplicidades, espectro discreto e definição independente dos zeros ajustados.
5. Para `xp`, não confundir hiperbolicidade local com sistema caótico confinado que já possua o espectro desejado. A proposta original e suas condições devem ser consultadas em [Berry–Keating, H = xp](https://research-information.bris.ac.uk/en/publications/ih-xpi-and-the-riemann-zeros/).
6. Acrescentar um controle dinâmico concreto: escolher um bilhar fechado com dinâmica caótica documentada, calcular ou obter níveis de fonte primária e validar convergência do método. Resolver setores de simetria e determinar a classe estatística apropriada antes da comparação. Se preservar reversão temporal, não impor GUE; para compará-lo diretamente ao GUE, justificar sua quebra.
7. Distinguir níveis reais de sistemas fechados de ressonâncias de sistemas abertos. Não misturá-los nos mesmos estimadores sem reformular o experimento.

**Entregáveis:** `operator_matrix.csv`, relatório de correspondências e análise do controle físico, ou justificativa específica de sua não execução.

**Aceite:** nenhum candidato é favorecido apenas por ajustar níveis ou apresentar repulsão de espaçamentos. Cada incompatibilidade é ligada a uma propriedade verificável, e cada propriedade desconhecida fica explícita.

### Etapa 12 — Busca limitada por candidatos, condicionada à viabilidade

**Pré-requisito:** instrumentos validados e pelo menos uma família com operador, domínio, método espectral e previsões definidos. Sem isso, produzir uma análise de inviabilidade; não inventar uma família apenas para executar um otimizador.

**Tarefas**

1. Escolher no máximo duas famílias e fixar um número pequeno de parâmetros. Registrar a complexidade antes de usar os dados reservados.
2. Verificar convergência da discretização e estabilidade numérica antes de otimizar. Uma matriz discretizada hermitiana não prova auto-adjunticidade do operador contínuo.
3. Usar custo multifatorial

\[
\mathcal L(\theta)=
w_E L_E+w_N L_N+w_s L_s+w_R L_R+w_K L_K+
w_T L_T+w_A L_A+w_\phi L_\phi+\lambda C(\theta).
\]

4. Normalizar os termos por escalas previamente fixadas, idealmente estimadas nos controles. Reportar componentes e sua dependência; não tratar estatísticas correlacionadas como evidências independentes somáveis.
5. Penalizar complexidade, instabilidade e escolhas livres de reparametrização da energia. Um termo não calculado é dado ausente, não custo zero.
6. Separar ajuste, seleção de hiperparâmetros e teste final em blocos contíguos distintos. Dados já explorados nas etapas anteriores não são teste intocado para uma família escolhida com base neles; reservar nova faixa para uma afirmação confirmatória.
7. Comparar com modelos simples e um controle que incorpora níveis explicitamente, para evidenciar ajuste sem poder explicativo. Exigir previsões fora do treino.
8. Interromper famílias sem convergência, dependentes de parâmetros por nível ou incapazes de satisfazer restrições estruturais. Regressão simbólica é uma extensão posterior, sujeita às mesmas regras.

**Entregáveis:** definição completa das famílias, histórico de busca, componentes do custo e desempenho fora do treino; ou relatório de por que a busca ainda não tem base suficiente.

**Aceite:** nenhum resultado é rotulado como reconstrução dinâmica apenas por reduzir o erro de autovalores. A rejeição de todas as famílias é uma conclusão válida.

### Etapa 13 — Consolidar o relatório e os limites de Hilbert–Pólya

**Tarefas**

1. Gerar relatório a partir dos artefatos salvos, com links para código, dados, tabelas e gráficos. Entregar Markdown ou HTML; PDF pode ser acrescentado sem se tornar dependência da análise.
2. Para cada afirmação, registrar categoria, fonte ou execução que a sustenta, intervalo de validade e limitação.
3. Separar A: resultados matemáticos conhecidos com suas hipóteses; B: reprodução numérica realizada; C: achados experimentais cuja novidade foi investigada; D: conjecturas.
4. Responder quanto foi recuperado: faixa de períodos, resolução, taxa de detecção, amplitudes e fases confiáveis, informação não identificável e classes ainda compatíveis.
5. Explicar o que seria exigido para uma estratégia de prova: espaço de Hilbert e domínio definidos; auto-adjunticidade demonstrada, incluindo igualdade dos domínios com o adjunto; construção não circular; relação exata que abarque todos os zeros não triviais e suas multiplicidades.
6. Tornar explícito por que a realidade das ordenadas de zeros selecionados não resolve RH. Uma relação global com `Xi(z) = xi(1/2 + iz)`, por exemplo mediante identidade rigorosa com um determinante espectral adequadamente definido, teria de excluir também zeros fora da linha; não basta listar os que já estão nela.
7. Executar a reprodução a partir de ambiente limpo e dados identificados por hash. Permitir reutilização do cache bruto verificado, sem exigir novo download idêntico.

**Aceite final:** cada figura aponta para seus dados e parâmetros; cada conclusão numérica aponta para uma execução real; as dez entregas do prompt original estão disponíveis ou têm estado explícito de não execução. Não afirmar investigação completa se um requisito necessário ficou pendente.

## 4. Contrato das execuções

Estas são interfaces a implementar, não comandos disponíveis neste momento:

```bash
python -m riemann_spectra data fetch --config configs/main.toml
python -m riemann_spectra data validate --config configs/main.toml
python -m riemann_spectra run --config configs/pilot.toml --milestone M1
python -m riemann_spectra run --config configs/main.toml --milestone M2
python -m riemann_spectra run --config configs/main.toml --milestone M3
python -m riemann_spectra report --run-id ID_DA_EXECUCAO
```

`--milestone` deve verificar dependências e reutilizar somente artefatos compatíveis por hash. Cada execução deve conter:

```text
manifest.json                 # código, ambiente, dados, sementes, tempo e memória
config_resolved.toml          # todos os parâmetros efetivamente usados
metrics.json                  # valores medidos, sem placeholders numéricos
tables/                       # resultados e resíduos
figures/                      # PNG e PDF ou SVG
logs/                         # comandos, avisos e falhas
report.md                     # conclusões e limitações daquela entrega
```

Para retomar o trabalho, `docs/ANDAMENTO.md` deve registrar: etapa, estado, evidências/artefatos, última execução, pendências e próximo comando. O relatório deve distinguir “planejado”, “implementado”, “executado” e “validado”.

## 5. Correspondência com as 15 etapas do prompt original

| Etapa original | Cobertura neste plano |
|---|---|
| 1 — Dados | 2 e 10 |
| 2 — Densidade média e unfolding | 4 |
| 3 — Correlação de pares | 5 |
| 4 — Spectral form factor | 6 |
| 5 — Separação da densidade | 7 |
| 6 — Domínio dos períodos | 7–9 |
| 7 — Potências dos primos | 9 |
| 8 — Fórmula de traço | 11 |
| 9 — Problema espectral inverso | 11–12 |
| 10 — Busca de Hamiltonianos | 12 |
| 11 — Reconstrução de órbitas | 8–9, com limites explicitados em 13 |
| 12 — Controles | 3, 5–9 e 11 |
| 13 — Anomalias | 10 |
| 14 — Hilbert–Pólya | 13 |
| 15 — Resultado final | 13 |

## 6. Fontes iniciais verificadas

Consulta realizada em 12/09/2026. Esta lista fundamenta o início do projeto; não é uma revisão exaustiva nem certifica originalidade de futuros achados.

- [Odlyzko — tabelas oficiais de zeros](https://www-users.cse.umn.edu/~odlyzko/zeta_tables/): aquisição e precisão publicada.
- [mpmath — zetazero e funções relacionadas](https://mpmath.org/doc/current/functions/zeta.html#zetazero): verificação numérica independente da amostra.
- [NIST DLMF §25.10](https://dlmf.nist.gov/25.10): zeros, função Z e fase de Riemann–Siegel.
- [Montgomery — The Pair Correlation of Zeros of the Zeta Function, 1973](https://websites.umich.edu/~hlm/paircor1.pdf): formulação e hipóteses dos resultados de correlação.
- [Berry e Keating — The Riemann Zeros and Eigenvalue Asymptotics, 1999](https://michaelberryphysics.wordpress.com/wp-content/uploads/2013/06/berry307.pdf): analogias espectrais e obstáculos de interpretação.
- [Berry e Keating — H = xp and the Riemann zeros, 1999](https://research-information.bris.ac.uk/en/publications/ih-xpi-and-the-riemann-zeros/): registro bibliográfico da proposta; consultar o texto integral antes de implementar uma variante.
- [Dumitriu e Edelman — Matrix Models for Beta Ensembles, 2002](https://arxiv.org/abs/math-ph/0206043): controles GUE por matrizes tridiagonais.
- [Main e colaboradores — Harmonic inversion as a general method for periodic orbit quantization, 1997](https://arxiv.org/abs/chao-dyn/9709009): método de referência para a extensão por inversão harmônica.

## 7. Frente complementar — Collatz como laboratório de dinâmica aritmética

O [plano Collatz](docs/PLANO_COLLATZ.md) investiga o caminho **regra aritmética → órbitas → estrutura espectral**, para esclarecer quais informações são necessárias no caminho inverso estudado neste projeto. Sua pergunta central é: **que informação aritmética precisamos preservar para distinguir sistemas com a mesma dinâmica simbólica?**

A sequência CL0–CL5 fixa as convenções, reproduz zetas conhecidas, enumera ciclos por aritmética exata, compara regras e transientes, valida operadores finitos e testa reconstrução com resposta conhecida. Cada etapa tem entregáveis e critérios próprios. As classificações A/B/C/D e as regras de reprodutibilidade deste projeto continuam valendo.

Essa frente pode informar a discussão de identificabilidade e operadores nas etapas 11–13. Ela não é dependência para concluir M4 ou M5 e não estabelece uma relação causal entre Collatz e os zeros da zeta. m4-v3 está concluído, com a ressalva de R2 registrada; todos os 100.000 zeros da tabela foram utilizados. A inclusão desta frente não altera protocolos congelados nem implica reexecutar os experimentos. A primeira implementação proposta cobre apenas CL0–CL1.
