# QRH — auditoria da aplicação da densidade de zeros

Data: 11/10/2026. Escopo autorizado: conferir a aplicação da estimativa de densidade de zeros, não a demonstração global do QRH. Estado da aplicação: **validado no escopo abaixo**, tomando o Lema 3.3 citado como resultado externo. Auditoria global: **inconclusivo**. Não se assume RH.

## 1. Fontes e alcance da leitura

- Shiva Kintali, *A Short Proof of the Quasi-Riemann Hypothesis*, data impressa 7/10/2026, `archive/fontes_etapa11/QRH.pdf`, 27 páginas. SHA-256 `f7ddc46632e37466e85951ea67acbd3c2abc19c8259fac51be569b1f6bbbe8e5`. Arquivo fornecido localmente; URL de aquisição não informada. Nesta auditoria: convenções da p. 2–3, Lema 2 (p. 6), formação dos rótulos (p. 12–13), equação (16) (p. 13), uso no expoente (p. 16).
- Khale–O'Kuhn–Panidapu–Sun–Zhang, *A Bombieri–Vinogradov Theorem for primes in short intervals and small sectors*, [arXiv:2008.09677v3](https://arxiv.org/pdf/2008.09677v3), versão de 12/01/2022. PDF arquivado, 20 páginas, SHA-256 `1e92b7ce59924f4a839a9168fff5de00a4796f415f76ada9d262a893236e8ee2`. Conferidas as definições de caracteres (§1.1), convenções de somação, definição de N (§2.3, p. 10), Lema 3.3 e sua prova (p. 18). Página 18 também conferida renderizada. Páginas impressas e do PDF coincidem.

O resultado externo usado é: para 1/2 ≤ σ < 1, R > 1, M > 2,

\[
\sum_{N\mathfrak f\le R}\sum_{\mu\bmod\mathfrak f}^{*}
\sum_{\|\mathbf m\|\le M}N(\sigma,M,\mu\lambda^{\mathbf m})
\ll (R^2M^{[K:\mathbb Q]})^{h(\sigma)(1-\sigma)}(\log RM)^B,
\quad h(\sigma)=\min\{3/(2-\sigma),2/\sigma\}.
\]

A estrela restringe aos caracteres primitivos; N conta zeros com parte real ≥ σ e altura absoluta ≤ M. O enunciado é uniforme nos parâmetros exibidos, para corpo fixo. Não exclui zeros excepcionais. A prova publicada remete a adaptações de Duke, Montgomery, Hinz e Coleman; essa cadeia não foi reconstruída aqui. A auditoria aceita esse lema como entrada bibliográfica, sem alegar uma demonstração independente dele.

## 2. Especialização correta da família

No QRH, F = Q(√−3) tem grau 2. Os caracteres de ordem finita têm tipo arquimediano trivial. Portanto, o termo m = 0 da soma externa inclui os caracteres primitivos necessários. Como os somandos são não negativos, descartar os demais tipos angulares preserva a desigualdade superior.

Não se aplica aqui a condição de alcance dos parâmetros do teorema principal de Bombieri–Vinogradov: a entrada é o Lema 3.3, com seu próprio domínio. Também não se substitui esse lema pelo Teorema 2.6 de caráter finito fixado.

A especialização produz (Q²H²)^{h(σ)(1−σ)}. Para a construção do QRH deve-se usar H = 2T, pois o rótulo procura zeros até essa altura, não apenas até T. O fator 2 é absorvido numa constante uniforme, porque o expoente permanece limitado.

## 3. Condutor e multiplicidade das linhas

Uma linha física é um elemento u livre de sextas potências, primo a S, com U ≤ N(u) < 2U. A família da linha contém νψ_u^{±1}, com ν numa família finita Θ, fixa, ramificada apenas em S.

### Condutor

Fora de S, o caráter residual sextico tem ordem exata 6: as normas dos primos bons são 1 módulo 6. A reciprocidade local identifica a restrição à inércia com esse caráter elevado a ±v_p(u), salvo a convenção global de sinal de Artin. Como v_p(u) está entre 0 e 5, o expoente do condutor é 1 quando v_p(u) ≠ 0 e 0 caso contrário. Os twists ν não alteram essa restrição.

Em S, a ramificação de ψ_u é uniformemente limitada: para m > 2v_p(6), Hensel aplicado a X⁶−a em 1 mostra que 1+p^m é formado por sextas potências. Os condutores dos twists são fixos. Logo

\[
\mathfrak f(\nu\psi_u^{\pm1})\mid\mathfrak c_{S,\Theta}\operatorname{rad}(u),
\qquad N\mathfrak f\le C_{S,\Theta}N(u)\le 2C_{S,\Theta}U.
\]

Escolher Q = max(2, 2C_{S,Θ}U) atende Q > 1. A constante pode depender do alvo fixado; isso não é uniformidade simultânea em todos os alvos, nem é necessário para (16).

### No máximo 12 linhas por caráter primitivo

Fixe o caráter induzido e uma orientação ±. Suas restrições à inércia fora de S determinam cada v_p(u) módulo 6, portanto exatamente em {0,…,5}. Como u não tem fatores em S, determinam o ideal (u). Um ideal principal tem seis geradores associados em Z[ω]. As duas orientações dão no máximo 12 elementos u.

O número de apresentações ν não multiplica esse limite: todas têm a mesma inércia fora de S para um caráter fixado e uma orientação fixada. A afirmação é sobre linhas distintas, não sobre apresentações distintas. Uma linha não unitária tem inércia não trivial em algum primo fora de S, de modo que não induz o caráter principal.

Este argumento foi conferido matematicamente no escopo local do Lema 2. Não é auditoria da construção inteira da sonda ou das identidades dos Apêndices A/B.

## 4. Reconstrução da equação (16)

Para a > 51/100, a formação dos rótulos fornece em cada linha de B_a um caráter primitivo com pelo menos um zero em Re ρ ≥ a, |Im ρ| ≤ 2T. Escolha um testemunho por linha. A multiplicidade anterior implica

\[
\#B_a\le12\sum_{N\mathfrak f\le Q}\sum_\psi^*N(a,2T,\psi).
\]

Isso não pressupõe independência, simplicidade de zeros nem uma correspondência bijetiva entre linhas e zeros. Zeros múltiplos só aumentam a majorante.

Para a ≤ 4/5, 3/(2−a) ≤ 5/2; para a ≥ 4/5, 2/a ≤ 5/2. Assim h(a) ≤ 5/2 e

\[
\#B_a\ll U^{5(1-a)}(3+T)^2[\log(CU(3+T))]^B.
\]

Na potência da altura usamos também 2h(a)(1−a) ≤ 2 para a ≥ 1/2. Para qualquer δ > 0, o logaritmo é absorvido em C_δ U^δ(3+T)^δ. A contagem de pontos da rede de Eisenstein dá, independentemente, #B_a ≪ U. Combinando:

\[
\boxed{\#B_a\ll_{S,\Theta,\delta}U^{R(a)+\delta}(3+T)^{2+\delta},
\qquad R(a)=\min\{1,5(1-a)\}.}
\]

Isso justifica o expoente de U da equação (16), com uma escolha explícita possível do expoente de altura desta etapa. Não substitui o A total do QRH, que reúne outras estimativas.

### Bordas e fatores removidos

- **Piso a = 51/100:** pode não haver zero testemunha. Usa-se apenas #B_a ≪ U; R(a)=1, como requerido.
- **Possível a = 1:** para Q,T fixos, os zeros na reta 1 são incluídos nas contagens para todo σ < 1. A uniformidade do lema permite σ ↑ 1, dando uma majorante logarítmica e depois U^δ(3+T)^A. Não é preciso supor previamente ausência desses zeros.
- **Fatores de Euler deletados:** os zeros de 1−ψ*(p)(Np)^{−s}, quando ψ*(p) ≠ 0, têm parte real zero. Não fornecem falsos testemunhos na faixa a ≥ 0,51. Os rótulos usam explicitamente as funções primitivas induzidas.
- **Zero excepcional real:** permanece contado. A aplicação não depende da inexistência de zeros de Siegel, nem de RH.

## 5. Efeito sobre o fechamento do QRH

A substituição de R(a) no expoente de p. 16 é consistente. Em d=1/2,

\[
E(1/2,a)=a-\beta_*+R(a)/2-1/3.
\]

Para a ≤ 4/5, a+R(a)/2−1/3=a+1/6; para a ≥ 4/5, vale 13/6−3a/2. O máximo de ambos os ramos é 29/30, em a=4/5. Portanto β_* > 47/48 dá E(1/2,a)<−1/80.

Além disso, 0 < R(a)+a−21/25 ≤ 1 no intervalo [0,51;1]. Para d ≤ 501/1000, a perda adicional em relação a d=1/2 é no máximo 1/1000. Logo a margem exibida −23/2000 é compatível com essa aplicação. Essa conferência algébrica não valida a estimativa de linha (22) nem os deslocamentos de contorno que a precedem.

## 6. Veredito e próximo passo

**Não foi encontrada falha na aplicação da estimativa de densidade à equação (16).** O QRH cita o lema pertinente; a especialização, a passagem condutor/linha, a absorção dos logaritmos e os extremos dos rótulos são consistentes.

Rótulo: **A, derivação a partir do resultado externo explicitado**, sem RH. Isso não promove a conclusão global de QRH a A: a sonda, a reflexão, a energia e os contornos permanecem fora deste parecer. Não há achado experimental nem reivindicação de novidade.

O próximo ponto da auditoria global é o **Lema 3/Apêndice B**, especialmente a independência dos coeficientes duais em relação ao fator quadrado-livre variável e as estimativas uniformes necessárias ao Lema 4. Uma auditoria dos fundamentos do Lema 3.3 externo seria tarefa diferente, voltando aos artigos que sua prova cita.

## 7. Execução e limites

Executado: obtenção de uma fonte primária versionada, extração de texto, inspeção visual da p. 18 e derivação analítica acima. A tentativa de screenshot pelo navegador falhou; a inspeção foi feita no PDF local com pdftoppm. Registro das fontes em `results/auditoria_qrh_densidade_20261011/fontes.json` e no manifesto geral.

Não executado: experimentos, enumerações de zeros, testes de hipóteses, Lean, reconstrução da prova externa ou novos cálculos sobre dados reservados. CPU agregada não foi instrumentada; são operações documentais curtas, sem execução longa. Nenhum protocolo congelado foi alterado.
