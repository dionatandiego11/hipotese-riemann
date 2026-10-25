# Política inversa — 25/10/2026

Exploração declarada de blocos1–4 e verificação exata de construtores em comprimentos4–8. Base n4/S16 conhecida antes da declaração; escolha do bloco4 e do alvo melhorado declarada no adendo após a exploração.

- `DECLARACAO.md` e `ADENDO_CONSTRUTOR.md`: escopo e hashes preservados.
- `explorar.py`: base de54 classes e240 políticas, custo máximo12 em quatro passos.
- `verificar.py` e `pytest.log`: três testes, incluindo oráculo independente de2.072 caminhos,13.068 construções e13.703 desigualdades de preenchimento.
- Manifestos: hashes de código/entradas, duração e limites; `code/` contém as cópias utilizadas.

Comandos: `.venv/bin/python results/politica_inversa_20261025/explorar.py` e `.venv/bin/python results/politica_inversa_20261025/verificar.py`. Não reexecutar sobrescrevendo resultados para uma versão alterada.

A afirmação para todo comprimento vem da prova em `teorias/SYRACUSE_COBERTURA_UNIFORME_20261025.md`, não de extrapolação dos testes. Cobertura central, revisão independente e prioridade bibliográfica pendentes. Sem zeros ou trajetórias positivas de Collatz.
