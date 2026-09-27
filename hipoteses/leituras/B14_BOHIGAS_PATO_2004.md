# B14 — Bohigas & Pato (2004), *Missing levels in correlated spectra*

**Referência.** O. Bohigas e M. P. Pato, arXiv:nucl-th/0403006v2 (03/03/2004), 16 pp. (texto nas pp. 1–11; referências e
figuras nas pp. 12–16). Publicação em periódico não conferida. **Cópia local:**
`archive/fontes_etapa11/hipoteses_20260925/missing_levels.pdf`, SHA-256 `c4ba67df…`; registro de aquisição da própria
pasta (`aquisicao.json`, baixado em 25/09/2026). **Lido por inteiro**; eqs. (6)–(13) conferidas na imagem (pp. 6–7).

## O que o texto afirma

| item | página | conteúdo |
|---|---|---|
| localizar **um** nível faltante | 3 | impossível para Poisson, trivial para espectro rígido ("picket fence"), sem sucesso até então para matrizes aleatórias; **em sistemas caóticos 2D é possível localizar aproximadamente um nível faltante** usando as correlações longas das órbitas periódicas curtas e a lei de Weyl (ref. [8], Schmit–Giannoni–Bohigas 1986) |
| hipótese central | 3–4 | fração f de níveis observada, **retirada ao acaso** de uma sequência infinita e estacionária |
| (1)–(4) | 4–5 | r_n = f^n R_n; após o desdobramento, x_k = f X_k e y_n(x₁,…,x_n) = Y_n(x₁/f,…,x_n/f): as funções de correlação só mudam de escala |
| (6)–(7) | 6 | σ²(L) = (1−f) L + f² Σ²(L/f) e δ(L) = (1−f) L/15 + f² Δ(L/f): aparece um **termo linear** |
| (8), (10), (11) | 6–7 | e(n,s), p(n,s) e a distribuição de vizinho mais próximo p(s) = Σ_k (1−f)^k P(k, s/f) |
| aplicação | 9 | inclinação de p(s) na origem multiplicada por 1/f; dados de ²³⁸U e ⁴⁸Ti indicam ~10% de ressonâncias faltantes |
| (25) e conclusão | 11 | p(s) tende a Poisson quando f → 0; com f conhecido recupera-se a estatística completa, e com a estatística conhecida estima-se f |

Ponto de atenção: a eq. (13) (p. 7) está impressa com (1/n!)(s/f)^n dentro da soma, onde deveria estar (1/k!)(s/f)^k;
o resultado E(n, s), invariância de Poisson, está certo. Erro tipográfico inofensivo.

## Para o projeto

- **O certificado D3 não é ideia nova.** Localizar zeros faltantes por meio da contagem suave (θ/π, o análogo da lei de
  Weyl) pertence a uma família conhecida: para caos, Schmit–Giannoni–Bohigas (1986, ref. [8] daqui); para zeros de
  funções L, o método de Turing. O rótulo do passe D3 continua **B** (procedimento conhecido, reproduzido), como o
  ADENDO_DIRICHLET_3 já dizia.
- **A hipótese de retirada ao acaso não vale para o nosso caso.** A varredura perdeu justamente os **pares mais
  próximos** — perda seletiva nos menores espaçamentos, não aleatória. As fórmulas de Bohigas–Pato não descrevem esse
  viés. A mesma ressalva vale para o Maass, onde o LMFDB tem uma **janela contígua** faltante. Isso importa para
  qualquer estatística de espaçamento calculada sobre listas incompletas.
- **Nenhuma previsão para o instrumento espectral.** O texto trata estatísticas locais, não a transformada. O efeito de
  perdas na transformada — o sinal oscilatório escalado por f mais um ruído adicional, e o termo suave com f·d̄ — seria
  derivação nossa, não deles.

Rótulos: resultados do texto, **A** (derivações simples, conferidas na leitura).

*Leitura de 25/09/2026, Claude Opus.*
