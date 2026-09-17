"""
riemann_spectra.replication
Critérios pré-registrados (m4-v1) para três conclusões separadas e correção por múltiplas
comparações entre blocos. Funções puras sobre as métricas gravadas de cada bloco.

Conclusões e critérios (valores numéricos vêm da seção [criteria] da configuração):

C1 — Recuperação de frequências (detecção sem catálogo; nulo primário):
  por bloco: (a) p global de S com Holm entre blocos <= alpha_family;
             (b) recuperação >= recovery_min entre linhas claramente detectáveis
                 (z previsto >= clear_margin x limite superior do limiar);
  família:   número de blocos com >= 1 detecção sem correspondência no catálogo <= max_blocks_with_unmatched.
C2 — Concordância de coeficientes (medição direcionada; estimador primário):
  por bloco: fração de linhas elegíveis (resolvidas e claramente detectáveis) com |razão - 1| <= ratio_tolerance
             >= coefficient_fraction_min, e Q >= q_min com p_Q (Holm entre blocos) <= alpha_family.
C3 — Compatibilidade estatística local (M2, envelopes simétricos):
  por estatística (CDF, R2, K_c) e por referência (GUE finito, Poisson), Holm entre blocos; reporta
  "rejeitado" ou "não rejeitado". Não existe veredito "compatível confirmado".

Replicação: um critério por bloco "replica" se vale em todos os blocos da faixa. Blocos contíguos
não são independentes; a correção de Holm controla a taxa de erro familiar sem supor independência.
"""

from typing import Any, Dict, List

import numpy as np


def holm_adjust(p_values: List[float]) -> List[float]:
    """Holm–Bonferroni: p ajustados monótonos, válidos sob dependência arbitrária."""
    p = np.asarray(p_values, dtype=np.float64)
    m = len(p)
    if m == 0:
        return []
    order = np.argsort(p)
    adj = np.empty(m)
    running = 0.0
    for rank, idx in enumerate(order):
        running = max(running, min(1.0, (m - rank) * p[idx]))
        adj[idx] = running
    return adj.tolist()


def evaluate_m3_family(blocks: Dict[str, Dict[str, Any]], criteria: Dict[str, Any]) -> Dict[str, Any]:
    names = list(blocks)
    alpha_f = criteria["alpha_family"]
    pS = [blocks[b]["arithmetic"]["p_value_global_mc"] for b in names]
    pQ = [blocks[b]["arithmetic"]["phase_coherence"]["p_value_Q"] for b in names]
    adjS = holm_adjust(pS)
    adjQ = holm_adjust(pQ)
    per_block = {}
    n_blocks_unmatched = 0
    for i, b in enumerate(names):
        ar = blocks[b]["arithmetic"]
        c1a = adjS[i] <= alpha_f
        rec = ar["recovery_among_clearly_detectable"]
        c1b = rec is not None and rec >= criteria["recovery_min"]
        has_unmatched = ar["unmatched_detections"] > 0
        n_blocks_unmatched += int(has_unmatched)
        cf = ar["coefficient_agreement"]
        frac = cf["fraction_within_tolerance"]
        q = ar["phase_coherence"].get("Q_observed")
        c2a = frac is not None and frac >= criteria["coefficient_fraction_min"]
        c2b = q is not None and q >= criteria["q_min"] and adjQ[i] <= alpha_f
        per_block[b] = {
            "C1_p_S": pS[i], "C1_p_S_holm": adjS[i], "C1a_significant": bool(c1a),
            "C1_recovery_clear": rec, "C1b_recovery_ok": bool(c1b),
            "C1_unmatched_detections": ar["unmatched_detections"],
            "C1_inconclusive_candidates": ar["inconclusive_candidates"],
            "C1_block_pass": bool(c1a and c1b),
            "C2_eligible_lines": cf["n_eligible"], "C2_fraction_within_tolerance": frac,
            "C2_Q": q, "C2_p_Q": pQ[i], "C2_p_Q_holm": adjQ[i],
            "C2_block_pass": bool(c2a and c2b),
        }
    c1_family = n_blocks_unmatched <= criteria["max_blocks_with_unmatched"]
    return {
        "blocks": per_block,
        "C1_blocks_with_unmatched_detection": n_blocks_unmatched,
        "C1_family_unmatched_ok": bool(c1_family),
        "C1_replicated_all_blocks": bool(c1_family and all(v["C1_block_pass"] for v in per_block.values())),
        "C1_blocks_passing": int(sum(v["C1_block_pass"] for v in per_block.values())),
        "C2_replicated_all_blocks": bool(all(v["C2_block_pass"] for v in per_block.values())),
        "C2_blocks_passing": int(sum(v["C2_block_pass"] for v in per_block.values())),
        "n_blocks": len(names),
        "criteria": criteria,
        "note": "Holm entre blocos; blocos contíguos não são independentes.",
    }


def evaluate_m2_family(blocks: Dict[str, Dict[str, Any]], alpha_family: float) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    names = list(blocks)
    for ref in ("gue", "poisson"):
        for stat in ("cdf", "r2", "k_connected"):
            ps = [blocks[b]["envelope_tests"][ref][stat]["p_value_mc"] for b in names]
            adj = holm_adjust(ps)
            out[f"{ref}_{stat}"] = {
                b: {"p": ps[i], "p_holm": adj[i], "verdict": "rejeitado" if adj[i] <= alpha_family else "não rejeitado"}
                for i, b in enumerate(names)
            }
            out[f"{ref}_{stat}"]["n_rejected"] = int(sum(a <= alpha_family for a in adj))
            out[f"{ref}_{stat}"]["min_attainable_p_holm"] = float(len(names) * min(ps)) if ps else None
    return out
