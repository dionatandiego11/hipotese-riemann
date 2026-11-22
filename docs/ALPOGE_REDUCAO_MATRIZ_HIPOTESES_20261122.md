# Redução analítica e hipóteses do projeto após o anúncio de RH

22/11/2026. Leitura dirigida de [Alpöge, nota](https://alpo.ge/remark.pdf), [Lean/Mathlib](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), [Sutherland](https://math.mit.edu/~drew/grh/) e [exposição para ζ](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf). Esta nota examina a camada analítica em linguagem matemática: não auditamos o Lean nem reproduzimos a prova da desigualdade aritmética (M). A exposição consultada é rascunho de 21/11, SHA-256 `667d88b3c375adf0466678094f452ca966aef0f4d368f6340d2bd5328b7fb706`, páginas impressas 4–5 e 26–27 (§I.1 e Parte II §1). Resultados de nosso projeto continuam sujeitos às suas bases de confiança e auditorias próprias.

## 1. Enunciado auditado e quantificadores

Escreva Λ para von Mangoldt, γ para a constante de Euler e, para x>=1,

    G(x) = Σ_{n<=x} Λ(n)(x/n−1) − x log x + (1+γ)x.

Para θ em (0,1), a exposição enuncia:

    [para todo Y₀>0 existe Y>=Y₀ tal que, para todo
     x em [Y,Y^(3/2)], G(x)<=x^θ]
       => ζ(s) não tem zeros com Re(s)>θ.                    (J)

O limite deve valer **em todo o intervalo**, e o Y escolhido pode depender de θ e de Y₀. Para concluir a RH, é suficiente que a hipótese de (J) valha para cada θ>1/2, θ<1; a simetria da equação funcional elimina também o lado esquerdo da linha crítica.

Se a cota vier com constante C_ε>0 e expoente 1/2+ε, ela precisa valer em janelas arbitrariamente tardias com C_ε independente de Y e x. Para cada θ>1/2, escolha ε<θ−1/2 e Y suficientemente grande: C_ε x^(1/2+ε)<=x^θ em toda a janela. Isso justifica absorver a constante. Uma constante que cresça livremente com Y ou uma desigualdade apenas em pontos isolados não é a hipótese acima. Exibir uma janela ou qualquer conjunto finito de valores também não estabelece o quantificador de janelas arbitrariamente tardias.

## 2. Conferência das primeiras identidades

Para Re(s)>1 e n>=1, a integral direta dá

    ∫_1^∞ (x/n−1)_+ x^(−s−1) dx = n^(−s)/[s(s−1)].

A soma de Λ(n)n^(−s) converge absolutamente e equivale a −ζ'(s)/ζ(s). Usando ∫_1^∞ x·x^(−s−1)dx=1/(s−1) e derivando em s para o termo x log x,

    F(s) := ∫_1^∞ G(x)x^(−s−1)dx
       = −[ζ'(s)/ζ(s)]/[s(s−1)] − 1/(s−1)^2 + (1+γ)/(s−1). (1)

O desenvolvimento de Laurent em s=1 dá ζ'/ζ=−1/(s−1)+γ+O(s−1). Como 1/[s(s−1)]=1/(s−1)−1+O(s−1), os polos duplo e simples de (1) cancelam. Em um zero não trivial ρ de multiplicidade m, a continuação de F tem polo simples de resíduo −m/[ρ(ρ−1)]. A multiplicidade é incorporada; simplicidade não é usada nesse passo. Para σ real em (0,1), a série alternada e ζ(σ)=η(σ)/(1−2^(1−σ)) dão ζ(σ)<0. Em σ>1 não há zeros pela série/produto de Euler; logo F não tem polo real positivo após o cancelamento em1.

Essas são conferências das identidades iniciais, não verificação da cadeia Lean. As trocas de integral e soma acima foram justificadas na região Re(s)>1; a extensão meromorfa usa as propriedades clássicas de ζ. O polo em0 e zeros triviais ficam fora do semiplano Re(s)>θ da redução.

## 3. Como a janela pode excluir um zero

Na Parte II §1, a exposição põe g(u)=G(e^u) e, para σ>2,

    A_j(σ+it) = (−1)^j F^(j)(σ+it)/j!
              = ∫_0^∞ g(u)e^(−itu) u^j e^(−σu)du/j!.

No intervalo u em [log Y, (3/2)log Y], g(u)<=e^(θu). Fora dele, usa-se uma cota grosseira |g(u)|≲e^(2u), obtida da estimativa clássica de Chebyshev. Fixada σ suficientemente grande, j é escolhido proporcional a log Y de modo que o núcleo u^j e^(−(σ−2)u) concentre sua massa nessa janela. O cálculo no rascunho dá, para uma sequência j→∞ e uniformemente em t,

    |A_j(σ+it)| + A_j(σ) <= C(σ,θ)(σ−θ)^(−j).          (2)

A desigualdade começa por |∫g e^(−itu)K|+∫gK<=2∫max(g,0)K. A contribuição interna usa a cota unilateral; a externa usa a cauda do núcleo concentrado. A expressão acima é uma cota uniforme em t, e não exige que G seja não negativo.

Se houver um zero com parte real maior que θ, o rascunho escolhe um ponto σ+it com um único polo de F mais próximo a distância d inferior a σ−θ e também inferior à distância de σ ao polo mais próximo. Pela expansão local em torno desse polo, |A_j(σ+it)| cresce como uma constante positiva vezes d^(−j), a um fator fixo de d; uma cota de Cauchy controla o resto. No centro real σ, |A_j(σ)| cresce estritamente mais devagar que d^(−j). Isso contradiz (2) na sequência j→∞. É crucial o polo não ser cancelado e o centro com polo mais próximo único; a prova da exposição trata essas escolhas.

**Parecer de leitura:** a cadeia e a ordem dos quantificadores são coerentes com os passos descritos na fonte. Conferimos algebraicamente a transformada, a expansão em1 e o sinal/resíduo do polo; não rederivamos com estimativas explícitas independentes todas as constantes da concentração, nem examinamos `lemmaL` no código Lean. Assim, (J) fica como **lema da exposição conferido em nível de arquitetura**, não uma auditoria formal nossa. Para L de Dirichlet são necessárias combinações positivas e os enunciados próprios de caracteres; não transportamos automaticamente a prova de ζ.

## 4. Matriz localizada de impactos nas nossas frentes

O anúncio externo e o comunicado Lean/Mathlib de 21/11 sustentam usar RH para ζ como teorema reportado por essas fontes; o registro de Sutherland, versão 22/11 04:35 UTC, inclui Dirichlet. Não alteramos os documentos congelados nem declaramos auditoria independente. Uma eventual republicação de resultados deve explicitar essa dependência externa e revisar a cadeia inteira.

| Alvo do projeto | Onde está | Efeito potencial do resultado externo | O que ainda falta |
|---|---|---|---|
| P-RH-trunc e S2-ratio′ | Cauda Projetada §§II.13 e II.20 | A premissa RH para ζ encontra um teorema formal relatado | Verificar as demais hipóteses, F5/J1 bibliográficas, correção matemática da derivação e base de confiança do certificado; revisão independente. O corte é U₂=15 na versão final, selecionado após exploração. |
| S2-ratio no ideal e densidade RVM | §§II.21–II.22 | Mesmo efeito sobre a premissa RH | A cadeia intervalar, a especificação de M^math e as outras entradas permanecem; não é o C2 completo. |
| Ordenadas tabuladas | §II.23 | RH fornece localização dos zeros de ζ, não a identificação da tabela | H-tab exige correspondência por índice, listagem com multiplicidade e erro <=3e-9 em todos os 100.000; é hipótese não certificada. A listagem com multiplicidade dispensa simplicidade neste passo. |
| Valor registrado do estimador, parcela (T) | §II.24 | RH deixa de ser apenas suposição na leitura que aceita o resultado externo | H-tab, F5/J1, confiança nas contas intervalares e auditoria da cadeia continuam; a fidelidade (N) é separada. C2 inclui também elegibilidade, agregação e fase Q. |
| S3b suavizado | Fórmula Explícita §2.3; Cauda Projetada | RH de ζ é mais forte do que a criticidade até a altura usada, para o papel específico F1 | Conferir todas as premissas da identidade admissível e do controle de restos. O limite não prova truncamento abrupto S1/S3a/S3c. |
| R3, momentos negativos e razões | `hipoteses/RAZOES_ERRO_PERFIL_POLAR_20261014.md` | GRH reportada para L de Dirichlet sustenta a localização nesse escopo | Simplicidade local onde exigida, domínio de deslocamentos e estimativa uniforme sublinear M(T) permanecem. RH não controla automaticamente derivados ou pares raros. |
| Família L de Hecke / ponte física | `docs/ARQUITETURA_ALPOGE_20261122.md` | Nenhuma transferência automática do enunciado listado | Conferir escopo da família e demonstrações próprias; zeros não identificam Hamiltoniano. |

**Correção de escopo em relação ao resumo anterior:** a versão mais recente do registro da Cauda Projetada já documenta a camada do valor registrado em §II.24, com hipótese H-tab, e não apenas o estimador ideal. Isso não equivale a certificar o protocolo C2 inteiro.

## 5. Próximo passo delimitado

Conferir de forma independente a concentração do núcleo de (2) e a seleção do polo, identificando as estimativas e hipóteses mínimas; depois rastrear o enunciado Lean em versão e arquivo verificáveis. Separadamente, escolher uma consequência concreta de RH no certificado §II.24, auditando a cadeia e as premissas não resolvidas antes de mudar seu rótulo. Nenhuma simulação ou alteração retroativa de protocolo foi feita nesta leitura.
