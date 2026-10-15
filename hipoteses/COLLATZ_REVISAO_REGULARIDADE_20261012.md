# Revisão dirigida — Wirsching, Tavares e cálculo espectral de Collatz

Data: 12/10/2026. Solicitação: ler a fonte indicada e os dois PDFs fornecidos, organizando o acervo. Notas individuais: [B31 — Wirsching](leituras/B31_WIRSCHING_PREDECESSORES_2003.md), [B32 — Tavares](leituras/B32_TAVARES_WIRSCHING_2026.md), [B33 — Hateley v1](leituras/B33_HATELEY_SPECTRAL_COLLATZ_V1.md).

**Resultado:** a fonte de Wirsching confirma a lacuna entre convergência de médias regulares e controle relativo por resíduo em resolução crescente. Tavares afirma resolver dois elos do programa, mas mantém essa lacuna. Sua presença de ζ em Mellin tem uma identidade concreta e generalizável. A v1 espectral de Hateley contém incompatibilidades elementares e não oferece um fechamento confiável para o nosso alvo.

Não se realizou uma auditoria completa das provas dos dois preprints. Não houve experimentos, execução de código de terceiros, simulações, leitura de zeros ou alteração das entregas congeladas.

## 1. Organização e versões

Três PDFs em `archive/fontes_etapa11/collatz_regularidade_20261012/`:

| Arquivo | Versão efetiva | Páginas |
|---|---|---|
| `wirsching_positive_predecessor_prelim_bielefeld.pdf` | Preliminar explicitamente identificada; fonte universitária. Não é o PDF editorial de 2003. | 18 |
| `tavares_2026_arxiv_2608.27617v1.pdf` | Fornecida pelo usuário; cabeçalho arXiv v1 de 27/08/2026, data impressa 31/08/2026. | 36 |
| `hateley_2025_preprints202511.1440v1.pdf` | Fornecida pelo usuário; Preprints.org v1 de 19/11/2025. | 73, incluindo capa |

Os dois arquivos da raiz foram copiados para os destinos, conferidos por SHA-256 e só então removidos da raiz, realizando o movimento autorizado. Nenhum conteúdo foi alterado. URLs bibliográficas dos arquivos fornecidos não foram registradas como downloads desta sessão.

Wirsching: a página editorial respondeu, o endpoint de PDF retornou conteúdo vazio, e uma URL antiga deu 404. Obteve-se a versão preliminar de Bielefeld; a versão publicada não foi obtida. As páginas das notas B31 referem-se apenas a essa cópia, não às páginas da revista citadas por Tavares. A divergência de 18 pp. frente às 19 pp. descritas na concordância externa não foi resolvida e não autoriza presumir identidade.

DLMF §§5.2 e 25.5 arquivadas como HTML de suporte, versão 1.2.8, release 15/09/2026 lida no rodapé. As cópias antigas do projeto permanecem intactas.

Registro: `results/leitura_collatz_regularidade_20261012/fontes.json`, `acesso.json` e manifesto geral. Notas com páginas e escopo em B31–B33. Leitura integral das sete seções da cópia preliminar de Wirsching; leitura **dirigida**, explicitada nas notas, dos preprints de 36 e 73 pp. Não se afirma leitura integral/auditoria global destes dois.

## 2. Três densidades diferentes

| Objeto | Espaço / variável | Informação retida | Limite desta revisão |
|---|---|---|---|
| Nossa ν, estacionária do dual Q de (3/4)L+ | Z3, resíduos da raiz | Contagem normalizada por profundidade total | Convergência fraca e médias fixas controladas; densidade forte ainda sem prova |
| Limite W de Applegate–Lagarias | Z3^×, raiz das árvores podadas | Variação das médias entre classes | Antecedente direto de regularidade da informação aritmética; não confundir com φ |
| φ de Wirsching/Tavares | [0,1], coordenada real de custo normalizado | Marginal do limite de operadores sobre I3×Z3^× | Sua estabilidade/assimptótica não controla automaticamente cada resíduo a |

S∞ de Wirsching integra a coordenada aritmética a e produz um resultado independente dela. Teorema 3 fornece convergência uniforme sobre famílias **limitadas e equicontínuas**. A família de geradores em resolução crescente não recebe esse controle automaticamente. Não é lícito inserir g̃_ℓ como se houvesse uma constante uniforme já demonstrada para eles.

Se adotarmos as resoluções alegadas por Tavares após auditá-las, a condição que ainda precisa de prova é (⋆3), uma cota relativa dos geradores no custo central e na variável a. A Conjectura 2 é uma via para essa condição, não a única via concebível. Não relatar “falta apenas uma conjectura” como se as outras condições fossem verdadeiras sem a prova que resta.

## 3. Uma ligação analítica concreta com ζ — derivação local

Seja φ a densidade real de

\[
X=\sum_{j\ge1}2\,3^{-j}U_j,\qquad U_j\text{ uniformes independentes em }[0,1].
\]

Ela é a estacionária real de W3. Como X∈[0,1], seu logaritmo de Laplace K(s)=log E[e^{−sX}], s>0, tem representação

\[
K(s)=\sum_{j\ge1}g(2s/3^j),\qquad
 g(b)=\log\frac{1-e^{-b}}b.
\]

Temos g(b)=O(b) perto de zero e O(log b) no infinito. Logo sua transformada de Mellin converge absolutamente em −1<Re z<0. Integração por partes, com termos de borda nulos, dá

\[
g^*(z)=-\frac1z\int_0^\infty\left(\frac1{e^b-1}-\frac1b\right)b^zdb
=-\Gamma(z)\zeta(1+z).
\]

### Justificação da regularização usada

Para v=1+z, 0<Re v<1, partimos da representação clássica Γ(v)ζ(v)=∫ b^{v−1}/(e^b−1) db em Re v>1 (DLMF 25.5.1). Ao separar a integral em 1 e subtrair 1/b apenas perto de zero, sua continuação a Re v>0 fica

\[
\int_0^1\left(\frac1{e^b-1}-\frac1b\right)b^{v-1}db
+\frac1{v-1}+\int_1^\infty\frac{b^{v-1}}{e^b-1}db.
\]

Em Re v<1, o termo 1/(v−1) é exatamente −∫_1^∞b^{v−2}db. Isso produz a integral subtraída usada acima, com convergência nas duas bordas; Γ(z+1)=zΓ(z) completa a conta.

Para K, a troca de soma e integral é permitida pela soma dos módulos das dilatações: Σ(3^j/2)^{Re z}<∞. Portanto

\[
\boxed{K^*(z)=\frac{(3/2)^z\Gamma(z)\zeta(1+z)}{3^z-1},
\qquad -1<\Re z<0.}
\]

Essa é a identidade (8) de Tavares, p. 12, visualmente conferida. Aqui ela foi reconstruída localmente sem depender de seu ponto de sela ou certificado numérico. Rótulo A para essa derivação, não para todo o preprint.

### O que a identidade diz sobre zeros

Na faixa aberta, Γ é holomorfa e não tem zeros (DLMF §5.2), (3/2)^z não se anula e 3^z−1≠0, pois |3^z|<1. Logo os zeros de K* nessa faixa são **exatamente** os zeros de ζ(1+z), com multiplicidades preservadas. Consequentemente a afirmação de que todos eles têm Re z=−1/2 reformula RH para os zeros na faixa crítica.

Não se obteve uma estimativa que estabeleça essa afirmação. O produto é uma representação alternativa dos mesmos zeros; a reformulação por si só não reduz a dificuldade do problema.

## 4. Controle de especificidade: a base 3 não é suficiente

Troque 3 por uma base real a>1 e tome

\[
X_a=(a-1)\sum_{j\ge1}a^{-j}U_j,\qquad K_a(s)=\log E[e^{-sX_a}].
\]

A mesma prova, na mesma faixa de Mellin, fornece

\[
K_a^*(z)=\frac{(a/(a-1))^z\Gamma(z)\zeta(1+z)}{a^z-1}.
\]

Os mesmos zeros de ζ aparecem para todas essas bases. A lei uniforme de U e a soma de escalas explicam o fator; a aritmética específica dos positivos de Collatz não entra nessa derivação. As frequências do termo periódico dependem de log a, mas os zeros na faixa de Mellin não mudam com essa substituição.

Esse controle é analítico, sem simulação. Não demonstra ausência de qualquer ponte específica; mostra que esta identidade isolada não identifica uma. Se prosseguirmos nessa rota, precisamos de uma propriedade da densidade/operador que venha dos geradores aritméticos e não seja satisfeita automaticamente por toda a família X_a.

## 5. Por que Hateley v1 não fecha a lacuna

Auditoria localizada B33:

1. Lema 4, eq. (12), afirma ΣPf=Σf para P com peso 1/m. O contraexemplo f=δ2 dá ΣPf=1/2, enquanto Σf=1.
2. O Lema 14 afirma um autovetor positivo Ph=h com perfil c/n. Pela própria definição de P, h=O(1/n) implica Ph=O(1/n²), incompatível com esse perfil não nulo.
3. A mesma prova atribui um polo em s=1 à série Σh(n)n^{−s}; o perfil c/n a torna holomorfa em Re s>0, incluindo 1.

São incompatibilidades com as definições efetivamente impressas, não críticas baseadas em um resumo. Assim não usamos suas conclusões espectrais como premissas. A versão v1 foi preservada; versões posteriores não foram auditadas. Não se generaliza o parecer a toda abordagem de espaços multiescala.

## 6. Direção recomendada após as leituras

**Frente aritmética prioritária:** estudar o objeto conjunto g_ℓ(k,a), na janela |k−ℓ|≤δ√ℓ, e o erro ao projetar a variável a módulo 3^K com K crescendo em relação a ℓ. Explicitar se o alvo é uma cota relativa média, uma cota em quase todas as classes ou uma cota inferior uniforme. Essas versões não são equivalentes; apenas a mais forte poderia alimentar diretamente a condição (⋆3), com os quantificadores corretos.

**Frente Mellin, complementar:** auditar a identidade da densidade real e os controles por base já derivados; se houver uma candidata específica, mostrar qual termo aritmético adicional altera o mecanismo genérico. Não procurar zeros numericamente antes dessa distinção.

Próximas fontes necessárias: o livro de Wirsching 1998 para a base completa dos geradores e Berg–Krüppel 1998 para a análise de φ0 e sua correção periódica. Não obtidos nesta entrega. A auditoria de todas as provas e certificados de Tavares é um escopo adicional, ainda não executado.

Antes de um novo piloto, definir **um** alvo quantitativo dos geradores e verificar qual resultado publicado é mais próximo. As leituras já encerram a tentativa de usar a estabilidade de médias fixas, sozinha, como prova da informação aritmética na resolução crescente.

## 7. Registro final

- Dois PDFs fornecidos organizados com hashes preservados; uma fonte original preliminar e dois HTMLs DLMF obtidos.
- Notas B31–B33 e esta síntese produzidas; manifesto e bibliografia atualizados.
- Falhas de obtenção do PDF editorial e avisos de fontes na extração registrados, sem apresentar arquivos vazios como fontes.
- Derivações locais e contraexemplo elementar; nenhum experimento, certificação numérica nova, código externo, enumeração, publicação ou commit.
- Os hashes das entregas `collatz_filtros_20261011` e `collatz_memoria_20261012` serão reconferidos no manifesto desta leitura; seus resultados não foram reexecutados ou alterados.
