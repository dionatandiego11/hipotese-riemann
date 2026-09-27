# B19 — Bell & Lagarias (2015), *3x+1 inverse orbit generating functions almost always have natural boundaries*

**Referência.** J. P. Bell e J. C. Lagarias, Acta Arith. 170 (2015), n.º 2, 101–120; arXiv:1408.6884v1.
**Cópia local:** `archive/fontes_etapa11/ponte_collatz_20260925/bell_lagarias_2015_arXiv_1408.6884.pdf`,
SHA-256 `f6578566…`, 15 pp., baixada em 26/09/2026. A paginação da versão publicada não foi conferida.
**Leitura:** texto inteiro (arXiv v1, com camada de texto nativa).

## 1. O que o texto afirma

T_k(n) = (3n+k)/2 (ímpar) ou n/2 (par), com k ≡ ±1 (mod 6); O_k⁻(m) é a órbita inversa (backward orbit) de m, e
f_{k,m}(z) = Σ_{n ∈ O_k⁻(m) ∩ ℕ⁺} zⁿ.

| item | seção | conteúdo |
|---|---|---|
| tricotomia | 1.1 | duas órbitas inversas são disjuntas ou uma contém a outra |
| **Teor. 1.1** | 1.1, 3 | uma união finita S de órbitas inversas tem função geradora racional ⟺ S coincide, a partir de algum ponto, com uma união de classes (mod \|k\|), e essas classes são fechadas sob r ↦ 2r e r ↦ 3r. Prova: teorema de Skolem–Mahler–Lech e redução do módulo mínimo admissível (ímpar, primo com 3, igual a \|k\|) |
| **Teor. 1.2** | 4 | 3x+1: para m ∉ {1, 2, 4, 8}, f_{1,m} tem \|z\| = 1 como **fronteira natural**, incondicionalmente (a prova separa os casos "Collatz vale" e "Collatz falha"). Para m ∈ {1, 2, 4, 8}: Collatz ⟺ f_{1,m} racional; se Collatz falha, as quatro funções também têm fronteira natural |
| Teor. 1.3 | 4 | 3x−1: fronteira natural para todo m ≥ 1 (prova a Conj. 2.4 de Berg–Opfer), porque há três órbitas inversas infinitas e disjuntas conhecidas |
| Teor. 1.4 | 5 | 3x+k: fronteira natural para todo m ≥ 1, com no máximo finitas exceções |
| ferramentas | 2 | Fabry (lacunas: m ≡ 0 (mod 3) ⇒ O⁻(m) = {m·2^j}); **Pólya–Carlson** (coeficientes inteiros e raio 1 ⇒ racional ou fronteira natural); Skolem–Mahler–Lech |
| Teor. 6.3 | 6 | sob as conjecturas de ciclos finitos e de ausência de trajetórias divergentes, há infinitas coleções finitas de órbitas com soma geradora racional |
| §7 | 7 | funções de Berg–Meinardus: g^{(m)} (iterado m-ésimo) é racional, com polos em raízes 2^m-ésimas da unidade; h_{k,n}(w) (órbita direta) e F_k(z, w) bivariada com racionalidade em aberto |

## 2. Pontos de atenção (erros tipográficos no arXiv v1)

1. Prova do Teor. 1.2: "which certifies that the elements … **are** eventually periodic modulo 1" deveria ser
   "**are not**", e "All other m ∈ ℕ⁻" deveria ser ℕ⁺. O argumento está correto; a redação, não.
2. Prova do Teor. 1.4: cita "criterion (2) of Theorem 1.2"; o correto é o **Teorema 1.1**.
3. §2.1: a referência "[?, Conjecture A]" está quebrada; provavelmente é Applegate–Lagarias (B13).
4. Não conferi a versão publicada; os erros podem ter sido corrigidos lá.

## 3. Consequência para a ponte direta — corrige B18 §5

Em B18 §5 escrevi que a fronteira natural "bloqueia a continuação analítica que uma ponte com zeros exigiria" na
rota 2. **Isso estava errado para séries de Dirichlet.** A fronteira natural diz respeito à série de potências em z
no círculo inteiro \|z\| = 1. A série de Dirichlet D_m(s) = Σ_{n ∈ O⁻(m)} n^{−s} se relaciona com ela por

  Γ(s) D_m(s) = ∫_0^∞ f_{1,m}(e^{−t}) t^{s−1} dt  (Re s > 1),

que só depende do comportamento **radial em z = 1** (t → 0⁺), não do círculo inteiro.

**Contraexemplo explícito (A, verificação imediata):** para m ≡ 0 (mod 3), O⁻(m) = {m·2^j}. A série f_{1,m}(z) =
Σ z^{m2^j} tem fronteira natural (Fabry), mas D_m(s) = m^{−s}/(1 − 2^{−s}) é meromorfa em todo ℂ.

Logo, **Bell–Lagarias não obstrui a rota 2.** O que eles mostram é que a informação útil está em t → 0⁺, isto é, na
**distribuição de O⁻(m) nos inteiros grandes**:

- polo de D_m em s = 1 ⟺ O⁻(m) tem densidade natural positiva (sob hipóteses tauberianas); o resíduo é a densidade;
- continuação para Re s > 1 − δ ⟺ controle do termo de erro da contagem #(O⁻(m) ∩ [1, x]).

**Controle de conteúdo (plano, rota 2):** se Collatz vale, O⁻(8) = {8} ⊔ O⁻(16) ⊔ O⁻(5), e daí
D_5(s) + D_16(s) = ζ(s) − 1 − 2^{−s} − 4^{−s} − 8^{−s}. É a recomposição trivial de ζ que o plano já descarta como
evidência. O conteúdo específico de Collatz está nas séries **individuais** D_5 e D_16: nas densidades delas (se
existirem) e nos termos de erro. Isso muda ao trocar a regra.

**Candidata a P2 (pergunta, rótulo D; checagem bibliográfica pendente):** O⁻(5) e O⁻(16) têm densidade natural? D_5
tem continuação além de Re s = 1? Até onde li, só há cotas inferiores de contagem, x^{0,84} em Krasikov–Lagarias via
B13, e não resultados de densidade. Nada aqui sugere relação entre as singularidades de D_5 e os zeros de ζ. Seria
preciso um mecanismo que produza exatamente os zeros de ζ, e não apenas o polo em s = 1.

**Rótulos:** Teors. 1.1–1.4 e 6.3: **A** (provas lidas e coerentes; erros apenas de redação). Contraexemplo e fórmula de
Mellin: **A**. Pergunta de P2: **D**.

*Leitura de 26/09/2026, Claude Opus.*
