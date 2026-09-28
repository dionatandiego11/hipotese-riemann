# PT-1 — adendo técnico 1 (27/09/2026)

A primeira execução de `medicao/medicao.py` (congelado, `11d23365…`, preservado como `medicao_v1_congelado.py`)
abortou **ao gravar o JSON**, antes de imprimir ou salvar qualquer valor: `TypeError: Object of type bool is not JSON
serializable` (booleanos do numpy). Nenhum valor medido foi exibido.

Correção: apenas conversão explícita com `bool(...)` em três campos (`na_faixa_B`, `acima_alt`, `agregado_compativel`).
Cálculo, dados, critérios e limiares inalterados (diff de 2 linhas). Novo SHA-256 de `medicao.py`:
b16e8dc2dc1dbb59f9a37e9731aade3f90adf73a51039375c50282cd9ec609bb.
