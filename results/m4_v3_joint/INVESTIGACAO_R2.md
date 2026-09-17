# Investigação da regra R2 acionada em m4-v3 (14/09/2026)

**Gatilho pré-registrado:** S4 fora da tolerância em 3 blocos (d05, d09, d10). Pelo plano, R2 exige o mesmo código S
fora em ≥ 3 blocos. A conclusão conjunta ficou suspensa até esta investigação.
**Dados acessados:** somente artefatos já gerados (`arrays.npz` e `summary.json` da reprodução; `block_metrics.json`
da primária). Nenhuma nova computação sobre os zeros 70.001–100.000. Registrado em `results/m4_v3_data_access_log.md`.

## Resultado

**Causa:** erro de desenho do plano (categoria vi), não discrepância entre implementações.

- S4 compara a fração do conjunto-escore acima do **limite superior** X₍ᵤ₎ do IC do limiar com uma faixa binomial
  centrada em **α = 0,05**.
- Pela regra estrita de três categorias, a probabilidade esperada de exceder X₍ᵤ₎ é (B+1−u)/(B+1):
  - reprodução (B = 1.999, u = 1.919): 0,0405;
  - primária (B = 9.999, u = 9.542): 0,0458.
  A faixa de S4, [0,0345; 0,0665], estava deslocada para cima.
- Médias observadas: reprodução 0,0401 e primária 0,0443, ambas conforme o desenho. Em relação ao limiar pontual,
  as frações da reprodução ficam em torno de 0,05.
- Simulação do procedimento em duas etapas, independente dos dados (20.000 réplicas): P(falha de S4 por bloco) =
  0,159; P(≥ 3 falhas em 10 blocos, se independentes) = 0,20. Os percentis dos 10 valores observados na
  distribuição simulada estão espalhados (0,015–0,959).
- Ressalva: a dispersão observada (0,0085) é maior que a simulada (0,0062). O resultado é compatível com
  flutuação e com a dependência entre blocos contíguos, mas fica registrado.

O mesmo defeito de desenho estava em `independent/COMPARISON_PLAN.md` (S4 da auditoria; b01 caiu exatamente no limite
inferior). Também está no rótulo "(esperado ≈ α)" do relatório M3 da primária; o valor correto é (B+1−u)/(B+1).

## Situação

- R2 **permanece registrada como acionada**; não há reclassificação.
- A causa está identificada e não envolve divergência entre implementações. R1 (determinísticas), R3 (vereditos
  C1/C2) e R4 (C3) não foram acionadas.
- A conclusão conjunta é emitida **depois** desta investigação, com a ressalva explícita de que R2 foi acionada.
- Uma versão futura do plano deve centrar S4 em (B+1−u)/(B+1) e usar uma faixa que inclua a variabilidade do limiar estimado (distribuição Beta(B+1−u, u) da probabilidade de excedência, combinada com a amostragem do conjunto-escore), em vez da binomial simples em torno de α.
- O valor 0,20 para ≥ 3 falhas em 10 supõe blocos independentes; com blocos contíguos, é apenas indicativo.
