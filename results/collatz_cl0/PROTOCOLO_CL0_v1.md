# Protocolo inicial do laboratório Collatz — CL0, versão 1 (25/09/2026)

Regras de execução das etapas CL1–CL5 de [docs/PLANO_COLLATZ.md](../../docs/PLANO_COLLATZ.md). Gravadas **antes** de
qualquer execução, comparação ou piloto. SHA-256 deste documento em `PROTOCOLO_CL0_v1.sha256`.

Documentos que este protocolo congela junto consigo:

| Arquivo | SHA-256 |
|---|---|
| `ESPECIFICACAO_CL0_v1.md` | `5556a0701f83153d031394be461c22a3f14eb470b5b10177dd1f6716eb93299a` |
| `collatz_cl1_v1.toml` | `7d00d0ef87f29fb3e3c11c6409c62aafce655966e35d86218b75b11c37a5b1bd` |

Regras herdadas, não reescritas aqui: [AGENTS.md](../../AGENTS.md); protocolo do registro de hipóteses
[v2](../registro_hipoteses/PROTOCOLO_REGISTRO_v2.md) (`55514a35…`), adendo 1 (`2afb657b…`), **adendo 2 de custo**
(`0b505348…`) com errata 1 (`b56b0470…`) e errata 2 (`9deef4f6…`). Onde houver conflito, vale a regra mais restritiva.

Uma mudança destas regras exige **versão nova** (v2, …) com hash próprio; correção pontual vira **errata ou adendo** em
arquivo próprio. Este texto não é editado depois de hasheado.

## 1. Posição de CL0 no projeto

Collatz está **fora do domínio do instrumento espectral** (protocolo do registro v2, §4, que cita Collatz nominalmente
como exemplo do que não entra). Nenhuma etapa CL lê ordenadas da ζ, autovalores dos controles da 11.6 ou o catálogo de
primos; nenhuma alimenta critério de m3/m4; nenhuma altera os protocolos existentes.

**Estado das frentes vizinhas, para não se repetir trabalho:** F-001 (Tao) e F-002 (Ruelle) estão `encerradas (fora do
domínio)` em [docs/REGISTRO_HIPOTESES.md](../../docs/REGISTRO_HIPOTESES.md); F-003 (Bernstein–Lagarias) é `proposta`, e
a partir desta entrega sua fonte está **obtida e hasheada** (§8). Isso não altera a triagem de F-003.

## 2. Pré-registro: o que já tem resposta conhecida

Os valores abaixo são **consequências matemáticas conhecidas**, fixadas antes de qualquer execução do projeto e
derivadas no Anexo A da especificação. Reproduzi-los é rótulo **B**, e apenas B. Nenhum deles pode ser relatado como
achado, contado como evidência de novidade ou usado para justificar ampliação de escopo.

| ID | Verificação | Resposta conhecida (T-tempo) | Onde |
|---|---|---|---|
| V-CL1-1 | \(F_n=\#\operatorname{Fix}(T^n)\) em \(\Sigma_2\) e \(\mathbb Z_2\), \(n=1..12\) | \(2^n\): 2, 4, 8, …, 4096 | Espec. A5, Anexo A.1 |
| V-CL1-2 | órbitas primitivas \(c_n\), \(n=1..12\) | 2, 1, 2, 3, 6, 9, 18, 30, 56, 99, 186, 335 | Anexo A.1 |
| V-CL1-3 | \(F_n=\sum_{d\mid n}d\,c_d\), nos dois sentidos | identidade exata | Anexo A.1 |
| V-CL1-4 | coeficientes de \(\exp\sum F_nz^n/n\) | \(2^n\), isto é \(\zeta_T(z)=(1-2z)^{-1}\) | Anexo A.1 |
| V-CL1-5 | soma periódica com pesos constantes por ramo \(a,b\) | \(Z_n=(a+b)^n\), \(\zeta=[1-(a+b)z]^{-1}\) | Plano, CL1 |
| V-CL2-1 | \(\operatorname{Fix}(T)\) em \(\mathbb Q_{\mathrm{odd}}\) | \(\{0,-1\}\) | Anexo A.2 |
| V-CL2-2 | \(\operatorname{Fix}(T^2)\) em \(\mathbb Q_{\mathrm{odd}}\) | \(\{0,-1,1,2\}\) | Anexo A.2 |
| V-CL2-3 | único ciclo **positivo** conhecido | \(\{1,2\}\), período 2 em T-tempo | Espec. §1 |

**Divulgação obrigatória (transparência do pré-registro).** Antes de congelar `collatz_cl1_v1.toml`, os valores de
V-CL1-1, V-CL1-2, V-CL1-3, V-CL2-1 e V-CL2-2 foram **conferidos por cálculo de rascunho** no diretório temporário da
sessão (contagem exata por enumeração de palavras até \(n=10\) e inversão de Möbius até \(n=12\); segundos de CPU,
nenhum artefato em `results/`). Isso foi feito para não congelar número errado; não é a execução de CL1, não produziu
manifesto e **não** conta como CL1 executado. CL1 permanece `não executado` e exige o pacote de código, os dois
caminhos independentes de contagem, os pesos, os testes e o manifesto.

## 3. Regras de execução (CL1–CL2)

1. **Aritmética exata, tolerância zero.** `int` e `Fraction`; ponto flutuante proibido em CL1 e CL2. O critério é
   igualdade exata, nunca "dentro da tolerância". Paridade de racional é definida por denominador ímpar.
2. **Dois caminhos independentes.** Cada contagem é obtida por enumeração explícita **e** por expansão formal/Möbius, e
   os resultados são comparados. Coincidência entre um caminho e ele mesmo não é verificação.
3. **Candidato ≠ ciclo.** O valor \(x_\varepsilon=b/(2^n-3^k)\) é candidato; só vira ciclo depois de conferir, por
   iteração exata, que o itinerário realizado é \(\varepsilon\) e que \(T^n(x)=x\). Ciclos são canonicalizados por
   rotação, com período mínimo verificado.
4. **Enumeração em fluxo.** Palavras processadas em fluxo, sem materializar o conjunto todo; custo e memória medidos e
   registrados antes de qualquer ampliação.
5. **Testes que não repetem a implementação.** Os testes verificam invariantes matemáticas (A5–A8 da especificação) e
   recuperação de casos conhecidos, não a saída do próprio código. Testes rápidos rodam **sem rede**.
6. **Sem importação cruzada.** O código de Collatz não importa `riemann_spectra`, o catálogo de primos ou as ordenadas
   dos zeros; não recebe esses valores como entrada, em nenhuma forma.
7. **Desvio de caminho registrado.** O plano propunha `src/riemann_spectra/collatz/`; como o código científico de
   m3/m4 está congelado e sob lock, o código novo vai para o pacote `collatz/` na raiz, fora de `src/`. Os locks e
   artefatos de m3/m4 não são tocados.

## 4. Custo

Vale o adendo 2 do registro v2 (`0b505348…`): **nenhuma produção longa — acima de 4 horas-CPU acumuladas — sem ganho
discriminante, viabilidade demonstrada, custo limitado e regra de decisão**, todos na declaração hasheada antes de
começar.

- **CL0** é texto e configuração: custo em horas-CPU desprezível; não é produção.
- **CL1** (períodos 1–12, \(2^{12}\) palavras) fica ordens de grandeza abaixo do limiar. Teto de segurança de
  **0,5 hora-CPU** na configuração, `OMP_NUM_THREADS=1`, um processo. Atingido o teto, interrompe-se e relata-se
  **inconclusivo por orçamento**, com as horas-CPU medidas — nunca um veredito parcial apresentado como veredito.
- **CL2 em diante o custo é exponencial no período.** Qualquer período acima de 12, qualquer mapa adicional e qualquer
  varredura de transientes exigem **configuração nova, com versão e hash próprios**, benchmark medido antes, e — se
  passarem de 4 horas-CPU — os quatro requisitos do §3 do adendo de custo.
- Medição sempre em horas-CPU acumuladas (usuário + sistema, somando processos); tempo de parede só para planejamento.

## 5. Artefatos de cada execução

Cada execução CL cria pasta própria em `results/`, com: configuração resolvida; manifesto com SHA-256 das entradas,
do código e das saídas; versões de Python e dependências; tabelas; logs; duração, horas-CPU e memória de pico.

- Dados de origem, quando houver, são imutáveis e registrados com fonte, precisão declarada, data e SHA-256.
- **Placeholder em tabela de resultado é proibido.** Análise pendente usa estado explícito
  (`pendente`, `não executado`, `inconclusivo`, `bloqueado`), nunca um número de exemplo.
- Falha de execução, execução parcial, perda de precisão e dado faltante são registrados, não escondidos.

## 6. Proibições específicas deste laboratório

1. Não apresentar aproximação finita como o sistema infinito (especificação §6).
2. "Nenhum outro ciclo até período \(n_{\max}\)" é resultado finito; nunca é escrito como ausência global nem como
   evidência sobre a Conjectura 3x+1.
3. Esgotar o orçamento de passos **não** é divergência; censura é registrada como censura.
4. A zeta de pontos periódicos não registra transientes; não se conclui nada sobre convergência a partir dela.
5. Não identificar órbitas de Collatz com primos, nem tempo inteiro de Collatz com \(\log p\). Não escolher tempos,
   pesos ou janelas olhando os primos ou os zeros para fabricar concordância.
6. Não transferir identidade demonstrada de um operador para outro; não aplicar normalização de Haar a
   \(\mathcal L_+\); não exigir auto-adjunticidade nem estatística GUE de operador de transferência.
7. Coincidência das zetas simbólicas de \(T_3\) e \(T_5\) é controle de **perda de informação**, não identificação das
   dinâmicas nos positivos.
8. Simetria 2-ádica não é automaticamente simetria dos positivos (especificação §2 e A3: \(\Omega(3)=-4/9\)).
9. Reprodução de caso conhecido é B. Novidade (C) exige busca bibliográfica registrada, com comparação ao trabalho mais
   próximo; ausência de referência numa busca breve não é novidade.

## 7. Vereditos e estados

Estados de andamento: `pendente`, `em execução`, `validado`, `inconclusivo`, `bloqueado`, `não executado`.

- **validado:** todas as verificações da etapa passaram exatamente, com artefatos e manifesto.
- **inconclusivo:** por orçamento (§4) ou por verificação que não decide; o motivo é nomeado.
- **bloqueado:** dependência não satisfeita.
- Resultado científico negativo — por exemplo, uma assinatura aritmética proposta que **não** distingue os mapas
  declarados — é resultado **validado**, e é registrado com o mesmo destaque de um positivo.
- Nada é apagado. Uma execução reprovada continua reprovada, com seu manifesto intacto; um passe posterior produz dado
  novo, com histórico próprio.

## 8. Fontes

Só conta fonte lida, com página. Resumo de busca e texto gerado por IA não são fonte.

Adquirido nesta entrega e registrado em `archive/fontes_etapa11/collatz_cl0_20260925/aquisicao.json` e no manifesto
geral `archive/fontes_etapa11/MANIFESTO.csv`:

| Fonte | Arquivo | SHA-256 | Leitura desta entrega |
|---|---|---|---|
| Bernstein & Lagarias, *The 3x+1 Conjugacy Map* (1996) | `bernstein_lagarias.pdf`, 16 pp. | `476b0149…` | pp. 1–3 (eqs. (1.1)–(1.6), Conjectura de Periodicidade) e p. 15 (Teorema B.1); provas do corpo do artigo não auditadas |

A tentativa de 19/09 falhou com 403/429 e esse registro de falha é **preservado** em
`archive/fontes_etapa11/hipoteses_20260919/aquisicao.json`; o download de 25/09 é registro novo, não correção do
anterior. A versão obtida é a cópia do autor (carimbo `19960215`), não a versão editorial; não presumir identidade
byte a byte com a publicação.

Monks–Yazinski (`3fcf49c2…`, obtido em 19/09) foi relido nesta entrega: p. 2 (definição de \(\mathbb Q_{\mathrm{odd}}\),
\(\Phi(\mathbb Q_{\mathrm{odd}})\subseteq\mathbb Q_{\mathrm{odd}}\)), p. 3 (Teorema 2.1 e Exemplo 2, \(\Omega(3)=-4/9\)).

## 9. O que CL0 não autoriza

CL0 entrega especificação, protocolo e configuração. **Não** autoriza: executar o piloto de CL1; criar o pacote de
código; enumerar palavras ou ciclos em `results/`; simular transientes; construir modelos finitos; declarar hipótese no
registro espectral; ampliar período, mapa ou espaço além do que a configuração congelada declara.

*Dionatan Resende & Claude Opus — 25/09/2026.*
