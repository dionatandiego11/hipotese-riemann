# Registro de hipóteses testáveis no instrumento

**Criado em 19/09/2026.** Adendos ao protocolo v2: [ADENDO_REGISTRO_v2_1.md](../results/registro_hipoteses/ADENDO_REGISTRO_v2_1.md) (`2afb657b…`), categoria T1-prospectivo; [ADENDO_REGISTRO_v2_2.md](../results/registro_hipoteses/ADENDO_REGISTRO_v2_2.md) (`0b505348…`, 25/09/2026), produção longa só com ganho discriminante, viabilidade demonstrada e custo limitado — teto em horas-CPU, poder com intervalo de Wilson e exceção declarada para estudos de viabilidade. Documento vivo: índice e situação de cada hipótese. As regras estão fixadas em
[results/registro_hipoteses/PROTOCOLO_REGISTRO_v1.md](../results/registro_hipoteses/PROTOCOLO_REGISTRO_v1.md)
(v1, SHA-256 `2f6404b7…`) e [PROTOCOLO_REGISTRO_v2.md](../results/registro_hipoteses/PROTOCOLO_REGISTRO_v2.md) (v2, que acrescenta a análise de poder prévia obrigatória) e prevalecem sobre este resumo. Dados em [registro_hipoteses.csv](registro_hipoteses.csv), com
uma linha por hipótese.

**Resumo das regras:**
- **Ciclo:** proposta → triada → declarada → testada → encerrada.
- **Declaração prévia com hash** antes de qualquer teste.
- **Confirmação** só com dados T1, que nenhuma decisão do projeto usou. Os zeros 1–100.000 (T0) servem só para testes
  exploratórios.
- **Refinar** é criar uma hipótese nova.
- **Nada se apaga.**
- **Testes múltiplos:** Benjamini–Hochberg (10%) sobre as hipóteses confirmatórias.
- **Rótulos A/B/C/D.** Novidade só depois de busca bibliográfica.
- **Início dos testes:** só depois que os três controles da 11.6 tiverem resultado registrado.

## Situação (19/09/2026)

| ID | Hipótese | Fonte | Rótulo | Estado |
|---|---|---|---|---|
| H-001 | Correções de altura finita na estatística local dos zeros: CUE de tamanho N_eff | Bogomolny, Bohigas, Leboeuf & Monastra 2006 | D (argumento heurístico) | triada |
| H-002 | Número de zeros suficiente para decidir se μ é primo: ordem μ log^{3/2} μ (sob RH) | Balanzario, Cárdenas Romero & Chacón Serna 2023 | A (suficiência, sob RH) e D (necessidade) | triada |
| H-003 | Classes de operadores que sobraram da matriz (K3a, K4, condicionais) | matriz da Etapa 11 | — | proposta |
| **H-004** | **P-R1: o mecanismo de vazamento prevê sinal e tamanho dos erros do estimador em L(s, χ)** | `hipoteses/CANDIDATAS.md` P-R1; desenvolvimento em Maass e ζ (T0) | — (resultado seria B) | **declarada (T1-prospectivo)**, `results/registro_hipoteses/H-004/DECLARACAO.md` (`82382c59…`) + `ADENDO_H004_1.md` |
| F-001 | Órbitas de Collatz quase limitadas | Tao 2019/2022 | A | encerrada (fora do domínio) |
| F-002 | Zetas dinâmicas e operadores de transferência | Ruelle | — | encerrada (fora do domínio) |
| F-003 | Mapa de conjugação 3x+1 | Bernstein & Lagarias | — | proposta (fonte obtida em 25/09, `476b0149…`) |

## Triagem

### H-001 — correções de altura finita (BBLM 2006)

- **Fonte (lida):** arXiv:math/0602270v1 (arquivo `hipoteses_20260919/cue_altura.pdf`, `38baa479…`).
  - Resumo, p. 1: "to leading order these deviations are the same as those of unitary random matrices of finite
    dimension N_eff = log(E/2π)/√(12Λ), where Λ = 1,57314…".
  - Eqs. (18)–(19), p. 5: α = 1 + C/log(E/2π), com C = 1,4720…
  - Eq. (24), p. 7: δp(s) = N_eff⁻² p₁(αs) + O(N_eff⁻⁴).
- **Por que interessa:** o projeto registrou em C3 (M3/M4) que a CDF de espaçamentos e K_c **rejeitam** o GUE finito
  usado como controle em todos os blocos (resultado negativo, RELATORIO_CONSOLIDADO §3.3). H-001 dá uma explicação
  concreta e quantitativa para isso.
- **Ressalvas da triagem:**
  1. Nas alturas de T0 (E ≈ 10⁴ a 7,5·10⁴), N_eff ≈ 1,7 a 2,2. O termo O(N_eff⁻⁴) não é pequeno, e a própria
     aproximação pode falhar.
  2. **Já foi testada na literatura:** os autores compararam com os zeros de Odlyzko perto de E = 2,5·10¹⁵ e 1,3·10²²
     (Figs. 1–3). Não há novidade em confirmar.
  3. **O valor para o projeto** é explicar o resultado negativo C3 e calibrar o controle GUE, não uma descoberta.
- **Teste possível:**
  - exploratório em T0, comparando os 30 blocos com p₀ + N_eff⁻² p₁(αs) contra o GUE finito;
  - confirmatório em T1, em outra altura.

### H-002 — quantos zeros são necessários para ver um primo (Balanzario et al. 2023)

- **Fonte (lida em parte):** arXiv:2311.04347v1 (`hipoteses_20260919/landau_suave.pdf`, `6b5bbd00…`).
  - Resumo, p. 1: sob RH, "to determine whether a natural number μ is a prime number, it is sufficient to know the
    location of a number of non trivial zeros … of order μ log^{3/2} μ", e o argumento de Heisenberg sustenta "the
    conjecture that this number of zeros cannot be essentially diminished".
  - Teorema 2, p. 3; Corolário 1, p. 5; discussão, p. 6.
- **No nosso instrumento:** é uma **lei de resolução**. Para separar a linha em log μ das vizinhas log(μ ± 1), a janela
  precisa de largura L ≳ c·μ na variável E. Com densidade (1/2π)log(E/2π), isso dá da ordem de μ log μ zeros; a forma
  exata depende da janela e da altura. O teste mede o número mínimo de zeros com que o instrumento separa Λ(μ), para
  μ ≤ 148 (t ≤ 5). O expoente da fonte vale para a tarefa e a suavização do artigo e **não** se transporta
  automaticamente para a janela de Hann (ver P-R4 em `hipoteses/CANDIDATAS.md`).
- **Ressalvas:** a suficiência é teorema sob RH, e a necessidade é conjectura. Para o nosso instrumento, a resolução
  (FWHM = 4π/L para Hann) já é conhecida. O resultado seria sobretudo uma **caracterização do instrumento**, útil e
  modesta.

### H-003 — classes de operadores restantes (Etapa 11.5)

Da matriz: K3a e K4 ficaram condicionais (C); quase todas as outras caíram por derivação. A 11.5 decide o que ainda
pode ser testado numericamente. Fica `proposta` até a triagem da 11.5.

### Fora do domínio do instrumento

- **F-001 (Tao, Collatz):** `tao_artigo.pdf` (arXiv:1909.03562v7, `62cf49d4…`) e `tao_collatz.pdf` (slides, `593fd589…`).
  O teorema é sobre densidade logarítmica de órbitas, sem previsão espectral para o instrumento. Material de contexto
  para a frente Collatz (docs/PLANO_COLLATZ.md, CL0–CL5), que precisa dos próprios controles.
- **F-002 (Ruelle):** `ruelle.pdf` (`ebf2be2e…`), *Dynamical zeta functions and transfer operators* (texto de
  divulgação; só a primeira página foi lida). É contexto para as zetas dinâmicas da frente Collatz, sem hipótese
  testável aqui.
- **F-003 (Bernstein & Lagarias):** o download de 19/09 falhou (403 e 429; `hipoteses_20260919/aquisicao.json`,
  registro preservado). Em **25/09/2026** o PDF foi obtido: `collatz_cl0_20260925/bernstein_lagarias.pdf`
  (`476b0149…`, 16 pp., cópia do autor, carimbo 19960215), registrado no `MANIFESTO.csv`. Lidas pp. 1–3 e p. 15.
  A triagem **não** muda: F-003 segue `proposta`, e a conjugação 2-ádica é usada como fato de referência (A2–A4)
  da frente Collatz, em `results/collatz_cl0/ESPECIFICACAO_CL0_v1.md` (`5556a070…`), não como hipótese espectral.

## Onde procurar mais hipóteses

A discutir com o usuário. Critério de entrada: a hipótese precisa prever algo **mensurável pelo instrumento** e ainda
**não** ter sido testada da mesma forma na literatura; se já foi, entra como reprodução (B).

## Revisões

- **19/09/2026 (revisão do usuário, `hipoteses/REVISAO_PODER_E_REGISTRO.md` §4, conferida pelo agente na imagem da p. 1
  da fonte):** H-002 dizia "μ log² μ"; o resumo de Balanzario et al. diz **μ log^{3/2} μ**. O erro veio da extração de
  texto do PDF, que perdeu a fração do expoente. Corrigido na tabela, na triagem e no CSV. H-003 estava com rótulo "C";
  uma classe ainda a triar não é achado, e o rótulo passou a "—". O teste de BH e a dependência entre valores-p (§5 da
  revisão) serão tratados por adendo ao protocolo antes do primeiro teste confirmatório.
