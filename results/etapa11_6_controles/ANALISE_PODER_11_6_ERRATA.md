# Errata de ANALISE_PODER_11_6.md (`21d2edae…`) — 19/09/2026

Motivada pela revisão do usuário (`hipoteses/REVISAO_PODER_E_REGISTRO.md`, §§1–3), conferida pelo agente. O documento
original fica como está; esta errata **prevalece** onde diverge. SHA-256 em `ANALISE_PODER_11_6_ERRATA.sha256`.

1. **Natureza do cálculo.** `power_block` gera **um** espectro substituto por bloco, estima σ(t) e o limiar com o nulo
   shuffle e calcula z_prev = |c|·W(0)/(2σ). Isso é uma **triagem de detectabilidade por sinal/ruído num modelo
   substituto (classe B/modelo)**, e **não** uma estimativa de poder: não injeta o sinal previsto em várias réplicas,
   não aplica o detector, o ajuste, a elegibilidade e os critérios completos, e não estima P(critério passar | modelo)
   nem a sua incerteza. As 200 e 999 realizações são calibração interna do nulo, não réplicas do experimento.
2. **Afirmações retiradas.** "Todos os critérios D-C* têm conjuntos elegíveis não vazios e **poder comparável ao de
   m4-v3**" (§3) fica reduzida a: pela triagem, **cada bloco do Dirichlet deve ter linhas com z_prev ≥ 1,5 × limiar**,
   incluindo linhas com χ = −1 e linhas com χ = 0 resolvidas. Conjuntos elegíveis não vazios **não** garantem que os
   critérios passem. A escala 1/z usada como "erro relativo" do ajuste é **só orientativa**: não é a variância do ajuste
   complexo, e não justifica conclusões sobre o poder dos critérios de amplitude, de sinal ou de ausência.
3. **Validação.** As três comparações (ζ d01: 13 previstas contra 15 observadas; Maass S2 e S1) sustentam a **escala**
   das previsões, não contagens exatas nem transferência garantida a outros espectros.
4. **Rastreabilidade.** Os números do bloco único G (12.000 níveis) e de g01+g02 (7.000) **não** saem do `main` de
   `analise_poder.py`: vieram de um comando avulso. Agora são reproduzidos por
   `poder/analise_poder_blocos_combinados.py`, com a mesma semente (5) e |C| de g02, que dá os mesmos valores (z = 3,84
   e 3,14; limiares 2,97 e 2,91).
5. **Estádio.** z ≈ 3,84 contra limiar 2,97 no bloco G **não** significa sucesso certo nem probabilidade medida, e fica
   abaixo de 1,5 × limiar. A regra de E-C1 fica explicitada no `ADENDO_ESTADIO_2.md`.
