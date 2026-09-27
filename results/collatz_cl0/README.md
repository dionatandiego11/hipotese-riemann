# CL0 — Especificação e protocolo do laboratório Collatz

Entrega documental de **25/09/2026**. Etapa CL0 de [docs/PLANO_COLLATZ.md](../../docs/PLANO_COLLATZ.md).
**Nenhum experimento foi executado.** Não há dado, tabela de resultado ou manifesto de execução nesta pasta.

| Arquivo | O que é | SHA-256 |
|---|---|---|
| `ESPECIFICACAO_CL0_v1.md` | espaços, mapa, medidas, operadores, observáveis, rótulos A/B/C/D, derivações | `5556a070…` |
| `PROTOCOLO_CL0_v1.md` | pré-registro, regras de execução, custo, artefatos, proibições, vereditos | `29ca9d5b…` |
| `collatz_cl1_v1.toml` | configuração congelada do piloto CL1 (ainda **não executado**) | `7d00d0ef…` |

Os três estão **congelados**: correção vira errata ou adendo em arquivo novo, nunca edição.

## Estado das etapas

| Etapa | Estado | Observação |
|---|---|---|
| CL0 | **validado** (entrega documental) | especificação, protocolo e configuração entregues |
| CL1 | `não executado` | configuração congelada; falta o pacote `collatz/`, os testes e o piloto |
| CL2–CL5 | `pendente` | dependem de CL1; cada ampliação exige configuração própria |

## Leitura mínima antes de executar CL1

1. `PROTOCOLO_CL0_v1.md` §§2–4: o que já tem resposta conhecida, aritmética exata e teto de custo.
2. `ESPECIFICACAO_CL0_v1.md` §§1–2 e Anexo A: convenção temporal e as derivações que os testes devem verificar.
3. Adendo de custo do registro v2 (`0b505348…`) e suas duas erratas.

Fonte adquirida nesta entrega: Bernstein & Lagarias, *The 3x+1 Conjugacy Map* — `476b0149…`, em
`archive/fontes_etapa11/collatz_cl0_20260925/`.
