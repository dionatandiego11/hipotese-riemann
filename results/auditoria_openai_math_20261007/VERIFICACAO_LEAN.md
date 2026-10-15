# Verificação formal isolada — estado em 08/10/2026

**Bloqueado na pré-verificação de ambiente. Nenhum kernel Lean ou Comparator foi executado.**
`conferencia_local.json` registra `lean`, `lake`, `elan`, `comparator`, `landrun` e `lean4export` ausentes do PATH. A cópia arquivada também é parcial: não é um checkout compilável. Não houve instalação global nem download de toolchain.

O alvo integral publicado é:

```sh
# Em checkout COMPLETO do commit adc7f1241b42e322a6451854ab7e4b4c146bf78a, diretório lean/:
lake env comparator ComparatorChallenges/QuasiRiemannHypothesis.json
```

O JSON fixa solução `OAI.NumberTheory.DirichletL.Nonvanishing` e enunciado `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`; permite somente `propext`, `Quot.sound`, `Classical.choice`. `enable_nanoda=false`: não solicita esse verificador adicional. A lista de axiomas permitidos é uma configuração, não um resultado local de inspeção dos axiomas efetivamente usados.

O `sorry` do arquivo ComparatorChallenges é o enunciado-alvo, não a prova-solução. A solução delega a FinalAssemblyUnconditional e possui uma cadeia grande. Não executar `lake update` indiscriminadamente: o lakefile contém hooks que clonam/aplicam patches em diversas bibliotecas, inclusive fora da cadeia examinada. Os hashes das dependências estão no lake-manifest arquivado.

## Menor teste preparado

A primeira unidade formal recomendada é `OAI.NumberTheory.DirichletL.Endpoint`, que importa apenas cinco módulos Mathlib, com alvo `OAI.SevenEighths.Endpoint.balanced_endpoint_margin` (Lema 20.2 do PDF). Em um ambiente completo e já provisionado, o arquivo `VerificarEndpoint.lean` desta pasta solicita também os axiomas dos dois lemas. Ele não foi compilado.

Lean exigido: v4.34.1; Mathlib: d13f23b723b8a846827a245b89c10fc7d3f11612. A consulta preliminar da release informou arquivo Linux tar.zst de 580.432.872 bytes; não foi baixado, nem foi medido seu custo de instalação/compilação. O orçamento de 600 s-CPU não é uma estimativa de viabilidade da cadeia inteira.

Preparação futura: ambiente isolado; dependências transitivas fixadas; limitação agregada de CPU e memória; execução em série. O limite por processo sozinho não implementa o teto agregado. Atingir limite deve produzir inconclusão, não continuação automática. Validar Endpoint não valida Nonvanishing. Instalar outra versão de Lean/Mathlib não equivale a reproduzir a release fixada.
