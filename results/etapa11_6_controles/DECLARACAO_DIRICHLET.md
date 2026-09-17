# Etapa 11.6 — controle com resposta conhecida: zeros de funções L de Dirichlet — declaração prévia (17/09/2026)

Gravada **antes** de qualquer código, cálculo de zeros ou execução. SHA-256 em `DECLARACAO_DIRICHLET.sha256`.
Nenhum artefato de m3/m4, lock ou certificado é alterado. Nenhuma afirmação sobre RH ou sobre a hipótese de Riemann
generalizada.

**Identificador do protocolo:** `ctrl-dirichlet-v1`.

## 1. Pergunta e papel no projeto

O instrumento congelado (cadeia m4-v3) recupera, nos zeros de ζ, linhas em t = log n com coeficientes
c(n) = −Λ(n)/(π√n). Este controle pergunta se o **mesmo instrumento**, aplicado a zeros de uma função L de Dirichlet,
recupera a **resposta conhecida e diferente**: linhas com coeficientes c_χ(n) = −Λ(n)χ(n)/(π√n), isto é, com **sinal
trocado** onde χ(n) = −1 e **ausentes** onde χ(n) = 0. É um teste de que o instrumento mede os pesos aritméticos e não
apenas reconhece posições log p.

## 2. Caracteres (fixados)

Dois caracteres **reais primitivos**, um ímpar e um par:

| Rótulo | Caractere | q | κ (χ(−1) = (−1)^κ) | Valores |
|---|---|---|---|---|
| **χ₋₄** | χ_{−4}(n) (símbolo de Kronecker) | 4 | 1 | 0 se n par; +1 se n ≡ 1 (mod 4); −1 se n ≡ 3 (mod 4) |
| **χ₅** | (n/5) (símbolo de Legendre) | 5 | 0 | 0 se 5 ∣ n; +1 se n ≡ ±1 (mod 5); −1 se n ≡ ±2 (mod 5) |

Para potências de primo, χ(p^r) = χ(p)^r.

**Fatos usados (Montgomery–Vaughan, *Multiplicative Number Theory I*, lido; arquivo no manifesto):**
- Corolário 10.8 (p. 333): ξ(s, χ) = L(s, χ)Γ((s + κ)/2)(q/π)^{(s+κ)/2} é inteira e ξ(s, χ) = ε(χ)ξ(1 − s, χ̄);
- (10.17) (p. 332): ε(χ) = τ(χ)/(i^κ q^{1/2}); Teorema 9.17 (p. 300): τ(χ_d) = √d se d > 0 e i√|d| se d < 0.
  Logo **ε(χ) = 1** para χ₋₄ e χ₅, e os zeros não triviais são simétricos em γ ↦ −γ;
- Teorema 14.5 (p. 454): N(T, χ) = (1/π) arg Γ(¼ + κ/2 + iT/2) + (T/2π) log(q/π) + S(T, χ) − S(0, χ);
- Teorema 12.13 (p. 410): fórmula explícita de Weil para χ primitivo, com E₀(χ) = 0 (sem termos de polo), termo
  arquimediano com κ e log(q/π), e soma sobre n com Λ(n)n^{−1/2}(χ(n)F(·) + χ̄(n)F(·)).

## 3. Predição congelada

**P1 (coeficientes).** Para cada n do catálogo 𝒦 do instrumento (potências de primo com log n ∈ [0,5; 5], n ≤ 148):

c_χ(n) = −Λ(n)χ(n)/(π√n).

Consequências explícitas, fixadas agora:
- **χ₋₄:** todas as potências de 2 (2, 4, 8, 16, 32, 64, 128) têm c = 0 (linhas **ausentes**); primos p ≡ 3 (mod 4)
  têm c com **sinal positivo** (oposto ao de ζ); potências pares de p ≡ 3 (mod 4) voltam ao sinal de ζ.
- **χ₅:** 5, 25 e 125 têm c = 0; primos p ≡ ±2 (mod 5) têm **sinal positivo**; potências pares deles voltam ao sinal de ζ.

**P2 (densidade suave).** d̄_χ(E) = (1/2π) log(qE/2π), análogo de `d_bar_rvm` com q (termo dominante da derivada do lado
suave do Teorema 14.5), usado como densidade primária, na mesma posição que `density = "rvm"` ocupa em m4-v3.

**D1 (derivação a escrever antes do código).** A adaptação do modelo de linhas da §2.2(b) de
[ETAPA11_3B_FORMULA_EXPLICITA.md](../../docs/ETAPA11_3B_FORMULA_EXPLICITA.md) (fator ½ da simetrização, convenção de
Fourier) com Λ(n) → Λ(n)χ(n), a ausência de termos de polo e o termo suave com q e κ serão escritos em documento próprio,
com hash, **antes** de qualquer código. Se essa derivação contradisser P1 ou P2, prevalece a derivação, e a divergência
é registrada como adendo antes de qualquer cálculo.

## 4. Dados: cálculo próprio dos zeros (sem fonte externa)

**Alvo:** os primeiros **12.000** zeros com γ > 0 de cada L(s, χ), em 4 blocos contíguos de 3.000 (χ₋₄: e01–e04;
χ₅: f01–f04), com índices 1–3.000, 3.001–6.000, 6.001–9.000 e 9.001–12.000.

**Método declarado:**
1. Função real Z_χ(t) = e^{iθ_χ(t)}L(½ + it, χ), com θ_χ(t) = arg Γ(¼ + κ/2 + it/2) + (t/2)log(q/π) (real porque ε(χ) = 1;
   a verificação de que Z_χ é real entra na derivação D1).
2. L(s, χ) = q^{−s} Σ_{a=1}^{q} χ(a) ζ(s, a/q) (zeta de Hurwitz, `mpmath`, precisão de trabalho ≥ 30 dígitos).
3. Varredura de sinais com passo ≤ 1/8 do espaçamento médio local 2π/log(qt/2π); refinamento de cada troca de sinal até
   |Δt| ≤ 10⁻¹⁰. **Meta de precisão:** |γ̂ − γ| ≤ 10⁻⁹.
4. Formato de saída: um arquivo por caractere, uma ordenada por linha com 9 casas decimais (mesmo formato de `zeros1`),
   com manifesto (SHA-256, versões, parâmetros, tempo).

**Verificações de dados (classe B, obrigatórias antes de usar os blocos):**
- **V1 completude:** em cada borda de bloco T, |N_encontrado(T) − N̄_χ(T)| ≤ 3, com N̄_χ(T) = (1/π) arg Γ(¼ + κ/2 + iT/2)
  + (T/2π) log(q/π) (arg Γ contínuo, nulo em T = 0), isto é, o Teorema 14.5 sem os termos S(T, χ) − S(0, χ), que não
  são estimados; **e** nenhum intervalo entre zeros consecutivos maior que 4 espaçamentos médios sem reamostragem local
  com passo reduzido à metade. A tolerância 3 é convenção de conferência B, não cota demonstrada para S.
- **V2 estabilidade:** recálculo completo de um bloco por caractere com passo reduzido à metade; a lista deve coincidir
  em número de zeros e com |diferença| ≤ 10⁻⁹.
- **V3 segunda avaliação:** 50 zeros por caractere, sorteados com semente fixa 20260917, reavaliados com
  `mpmath.dirichlet` **e** com o método do item 2 em precisão dobrada (60 dígitos): troca de sinal de Z_χ confirmada em
  [γ̂ − 10⁻⁸, γ̂ + 10⁻⁸] nas duas. Ressalva: `mpmath.dirichlet` também usa somas de Hurwitz, então V3 confere
  implementação e precisão, não um método matematicamente independente.
- **V4 simetria:** ε(χ) = 1 verificado numericamente em 10 pontos por caractere (Z_χ real até 10⁻²⁰ relativo).
- **Piloto:** antes dos 12.000 zeros, calcular os primeiros 500 de cada caractere, medir o custo e aplicar V1–V4. O custo
  medido é registrado antes da execução completa.

Falha em V1–V4 ⇒ os dados não são usados; nenhuma conclusão sobre o instrumento é tirada.

## 5. Instrumento e critérios

**Instrumento:** o de m4-v3 (janela de Hann, t ∈ [0,5; 5], estimador primário `band_conjugate`, detector sem catálogo,
nulos shuffle e GUE), com os **mesmos parâmetros numéricos** de `configs/m4_v3.toml`, exceto: dados, blocos, sementes
(χ₋₄: 20260919; χ₅: 20260920), densidade (P2), coeficientes do catálogo (P1) e `declared_table_error` = 10⁻⁹ (meta do §4).
As mudanças de código ficam num caminho novo, sem editar o código congelado nem os locks de m3/m4.

**Critérios (por caractere; mesmos limiares de `[criteria]` de m4-v3 onde houver análogo):**

| Código | Critério | Passa se |
|---|---|---|
| **D-C1** | recuperação sem catálogo das linhas com χ(n) ≠ 0 claramente detectáveis (margem 1,5) | recuperação ≥ 0,95 e no máximo 2 blocos com detecção sem correspondência |
| **D-C1z** | linhas com χ(n) = 0 resolvidas das vizinhas | **nenhuma** detecção clara correspondida a elas em nenhum bloco |
| **D-C2** | estimador primário: r̂_χ = Re Ĉ / c_χ(n) nas linhas elegíveis (regra de elegibilidade de m4-v3, com c_χ) | fração com \|r̂_χ − 1\| ≤ 10⁻⁶ ≥ 0,95 e teste de fase Q ≥ 0,9 |
| **D-C2s** | sinal, nas linhas elegíveis com χ(n) = −1 | Re Ĉ/c(n) < 0 (c(n) de ζ) em **todas**; a hipótese "coeficientes de ζ" é rejeitada: fração com \|Re Ĉ/c(n) − 1\| ≤ 10⁻⁶ < 0,95 sempre que houver tais linhas |
| **D-C2z** | linhas com χ(n) = 0 resolvidas | \|Re Ĉ\| ≤ limite de detecção do bloco (`detection_limit_coefficient`) em todos os blocos |
| D-C3 | estatística local (GUE) | **só descritivo** (a universalidade para L(s, χ) é conjectura, rótulo D); não é critério |

**Resultado do controle:** "passa" se D-C1, D-C1z, D-C2, D-C2s e D-C2z passam para os dois caracteres.

## 6. Regras de leitura fixadas agora

1. **Passa:** o instrumento distingue pesos aritméticos com sinal e ausências (resposta conhecida). Não diz nada sobre RH
   ou GRH, nem valida o certificado da 11.3b.
2. **Falha com dados aprovados em V1–V4:** resultado negativo registrado. Nenhum parâmetro é reajustado. Qualquer nova
   execução exige adendo com a causa identificada, escrito antes de rodar.
3. **Falha só em D-C2 com D-C2s e D-C2z aprovados:** registrar como limitação de precisão (a tolerância 10⁻⁶ foi fixada
   para os zeros de ζ com precisão de tabela 3·10⁻⁹), sem trocar a tolerância a posteriori.
4. O relatório mostra, lado a lado, o resultado de K12 ([DECLARACAO_K12.md](DECLARACAO_K12.md)) e a comparação com a
   hipótese errada "coeficientes de ζ".

## 7. Ordem de execução e responsabilidades

1. D1 (derivação escrita, com hash).
2. Código novo + testes (sem rede; incluindo um teste sintético com linhas de sinais conhecidos).
3. Piloto de 500 zeros por caractere; V1–V4; registro do custo.
4. Cálculo dos 12.000 zeros; V1–V4.
5. Execução do instrumento nos 8 blocos; relatório.

Os comandos de cálculo e execução são entregues ao usuário, que decide quando rodar. Nenhuma etapa começa sem a anterior
registrada.
