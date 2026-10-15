# B33 — Hateley, cálculo espectral de dinâmica aritmética (v1)

Leitura dirigida: 12/10/2026. James C. Hateley, *The Collatz Conjecture and the Spectral Calculus for Arithmetic Dynamics*, Preprints.org v1, 19/11/2025, DOI 10.20944/preprints202511.1440.v1. A cópia diz “NOT PEER-REVIEWED”.

Arquivo fornecido: `preprints202511.1440.v1.pdf`, movido sem alteração para `archive/fontes_etapa11/collatz_regularidade_20261012/hateley_2025_preprints202511.1440v1.pdf`; 73 páginas, sendo uma capa e 72 páginas de artigo. SHA-256 `c15790c3f8557c1ad38c2d8b77ab9d85f7fd72c1f102ad8e7a6db113daf9ad37`. URL bibliográfica https://www.preprints.org/manuscript/202511.1440/v1; download original não registrado.

**Escopo:** introdução e definições §§2–3 (pp. impressas 1–8), resultados centrais de densidade e espectro (consultas pp. 24–30), e consulta ao argumento de assimptótica de blocos pp. 42–43. Não foram lidas integralmente as 73 páginas nem auditadas todas as desigualdades multiescala. P. impressa 4 (PDF 5) e 24 (PDF 25) conferidas visualmente. Todas as referências nesta nota são à v1, sem juízo sobre versões posteriores.

## 1. O operador é distinto do nosso

O mapa é o clássico C(n)=n/2 para n par e 3n+1 para n ímpar. Seu ciclo é {1,4,2}; a referência introdutória a {1,2} mistura convenções. Mais importante, o operador das eqs. (2), (11) e (15) tem peso 1/m:

\[
(Pf)(n)=\sum_{C(m)=n}\frac{f(m)}m
=\frac{f(2n)}{2n}+\mathbf1_{n\equiv4\ (6)}\frac{f((n-1)/3)}{(n-1)/3}.
\]

Não é L+ nem sua normalização constante, nem Q, nem W3 de Wirsching. Não transportar seus resultados para nosso mapa acelerado e seus operadores.

## 2. Contraexemplo ao Lema 4, p. impressa 4 / PDF 5

O Lema 4 afirma preservação de massa em ℓ1. Tome f=δ2. Temos Pf=(1/2)δ1. Logo

\[
\sum_n(Pf)(n)=1/2\ne1=\sum_n f(n).
\]

A identidade efetivamente decorrente da definição é ΣPf=Σ f(m)/m, para f≥0. O próprio texto imprime essa identidade diferente na eq. (16), p. 6. A prova do Lema 4 omite exatamente o fator 1/m. É um contraexemplo exato, não um diagnóstico numérico.

## 3. Incompatibilidade da densidade c/n com Ph=h

O Lema 14, p. impressa 24 / PDF 25, supõe um autovetor positivo Ph=h e afirma h(n)=c/n·(1+O(n^{−δ})), c>0.

Com o operador acima, essa conclusão não pode ocorrer. Se h(m)=O(1/m), cada parcela de Ph(n) é O(1/n²), pois seus índices são 2n e (n−1)/3. Portanto Ph(n)=O(n^{−2}), ao passo que h(n)~c/n. A igualdade Ph=h é incompatível com tal perfil.

Há ainda uma obstrução independente: H(s)=Σh(n)n^{−s}, definido na prova do Lema 14, é holomorfo em Re s>0 quando h(n)=O(1/n). Sua eq. (56), p. 25 / PDF 26, atribui-lhe um polo em s=1, o que contradiz essa convergência absoluta local. Uma soma parcial c log x corresponde ao peso 1/n e ao polo em s=0 da série deslocada; não justifica o polo em 1 que o texto usa.

Esses argumentos demonstram que os enunciados/identidades da v1, tomados conjuntamente com suas definições, são inconsistentes. Não se afirma que toda ideia de espaço multiescala seja impossível ou que uma versão corrigida tenha sido auditada.

## 4. Decisão para o projeto

A v1 não sustenta as conclusões de conservação de massa e densidade estacionária que precisaríamos. Não usar seu suposto gap espectral, sua continuação ou o argumento de convergência de Collatz como fatos disponíveis. Referências de métodos multiescala podem ser pistas, sujeitas à leitura das fontes originais.

Classificação da auditoria localizada: A para os contraexemplos e incompatibilidades elementares explicitados; sem afirmação de novidade. Não executamos seus scripts, não alteramos o PDF e não avaliamos versões posteriores.
