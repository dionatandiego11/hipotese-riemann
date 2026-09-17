# Etapa 11.3b — encerramento com itens abertos registrados (17/09/2026)

**Decisão:** a subetapa 11.3b (fórmula explícita e passagem do observável congelado às linhas) é **encerrada** nesta data,
por decisão do usuário, **sem** resolver H1. Os itens em aberto ficam registrados abaixo e não bloqueiam as subetapas
11.5 e 11.6. Nenhum cálculo novo foi feito para este encerramento. Nenhuma afirmação sobre RH.

## 1. O que ficou estabelecido (com rótulo e escopo)

| Resultado | Rótulo | Escopo e hipóteses | Onde |
|---|---|---|---|
| Classe admissível 𝒜 e forma de referência da fórmula explícita | derivação sobre fonte conferida | ponto de partida: Connes, Teorema 6 e Lema 3 (lidos); enunciado independente em Montgomery–Vaughan, Teor. 12.13 (lido) | [ETAPA11_3B_ADMISSIBILIDADE.md](ETAPA11_3B_ADMISSIBILIDADE.md); [ETAPA11_3B_TERMO_ARQUIMEDIANO.md](ETAPA11_3B_TERMO_ARQUIMEDIANO.md) |
| Contagem local Z1: N(T+1) − N(T−1) ≤ 10,5 log(T+8), N(5) ≤ 31 | derivação | sem RH; Jensen conferido em Titchmarsh 1939, §3.61 (J1 resolvida) | [ETAPA11_3B_Z1_CONTAGEM.md](ETAPA11_3B_Z1_CONTAGEM.md) |
| S3b: M_ε(t) → F*(t) quando ε → 0, taxa O(ε²) | derivação condicional | criticidade dos zeros até H₀ (agora com fonte lida: Platt–Trudgian) | [ETAPA11_3B_H1_R5_ESTIMADOR.md](ETAPA11_3B_H1_R5_ESTIMADOR.md) §2.1 |
| Cadeia certificada para o estimador primário, corte (8, 2), 30 blocos | computacional (intervalos) | **(N)** fidelidade do valor registrado, incondicional na base de confiança: ε_k ≤ 6,3·10⁻¹¹ nos 461 elegíveis; **(T)** \|r̂_k − 1\| ≤ 10⁻⁶ nos 461 elegíveis, **sob RH e H-tab**; corte escolhido após exploração; sem auditoria independente | [ETAPA11_3B_H1_CAUDA_PROJETADA.md](ETAPA11_3B_H1_CAUDA_PROJETADA.md) §§II.17–II.24; `results/etapa11_r5/` (manifesto de 59 hashes) |

## 2. Itens em aberto (registrados, não resolvidos)

| Item | O que falta | Por que não bloqueia 11.5/11.6 |
|---|---|---|
| **H1** | passagem geral, com erro controlado, do observável congelado ao modelo de linhas (L-EF2c) | as classes da matriz foram decididas por requisitos M e por derivações próprias; os controles da 11.6 usam o mesmo instrumento em modo empírico |
| **S1** | cota quantitativa de truncamento em U útil para toda a faixa (quantificada, não fechada) | idem |
| **S3a** | convergência do truncamento abrupto M_{≤U} → F* | idem |
| **S3c** | convergência distribucional por cortes abruptos | idem |
| **C2 completo** | a certificação cobre a condição por linha; **não** cobre a elegibilidade calculada pelo pipeline, a agregação por fração ≥ 0,95 nem o teste de fase Q | C2 continua valendo como resultado **B** (medição registrada) |
| **H-tab** | fidelidade da tabela (precisão declarada lida; completude, método e licença de `zeros1` só parciais — F7) | condição explícita de (T) |
| **F5** | leitura do enunciado original de Weil (1952) | pendência bibliográfica, não hipótese matemática |
| **Auditoria independente** | reexecução e revisão por terceiros ([PROTOCOLO_AUDITORIA_CERTIFICADO.md](PROTOCOLO_AUDITORIA_CERTIFICADO.md)) | externa |

## 3. O que não é afirmado

- Nenhuma afirmação de que RH vale ou de que o certificado seja evidência a favor de RH.
- Nenhuma afirmação de novidade sem busca bibliográfica completa ([BUSCA_BIBLIOGRAFICA_MANUSCRITO.md](BUSCA_BIBLIOGRAFICA_MANUSCRITO.md) é preliminar).
- Nenhuma extensão do certificado a outros cortes, estimadores ou blocos.

## 4. Condições para reabrir

A 11.3b só é reaberta por declaração escrita que indique qual item da §2 será atacado, com o alvo e o critério fixados
antes de qualquer cálculo, como nas declarações de `results/etapa11_r5/`.
