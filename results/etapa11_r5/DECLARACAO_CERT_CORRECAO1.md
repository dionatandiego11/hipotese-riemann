# Adendo 1 à DECLARACAO_CERT.md — correção de enclausuramento (15/09/2026)

Gravado **antes** de alterar o código e reexecutar. SHA-256 em `DECLARACAO_CERT_CORRECAO1.sha256`. O método da declaração
original (SHA-256 b7a7980c…) não muda. Este adendo corrige a implementação e acrescenta testes obrigatórios.

## 1. Estado da execução 1
Os arquivos `cert_calculo_exec1_pendente.py`, `cert_blocos_exec1_pendente.csv`, `cert_tabela_exec1_pendente.csv` e
`cert_resumo_exec1_pendente.json` ficam preservados como **certificação pendente de correção numérica**. Nenhum par da
execução 1 é considerado certificado.

## 2. Defeitos identificados (auditoria externa, reproduzidos localmente)
- **D1.** `ck_inf = iv.mpf(mpf(ck.a))` converte o extremo inferior para a precisão comum (mp.dps = 15). Para p = 2, 3, 5,
  11 e 139, o valor resultante fica acima do extremo superior do intervalo.
- **D2.** `mn` (mínimo de extremos superiores) converte por `mpf` e pode devolver valor abaixo do intervalo.
- **D3.** `W_iv`, ramo |v| ≈ 1: os extremos de `av` passam por `mpf`. Com L = 2 e v = 1 + 10⁻¹², 1 − 10⁻¹² ou 1 + 10⁻⁸, o
  intervalo devolvido é disjunto da fórmula direta intervalar. O ramo v ≈ 0 também usava extremos convertidos por `mpf`.
- **D4.** A decisão final usa `mpf(tot.b) <= mpf(TAU)`, uma conversão comum.
- **D5 (encontrado na revisão local).** Outras conversões por `mpf` de extremos:
  - `floor(mpf(X.a))` e `floor(mpf(X.b))` nas bordas das células;
  - `float(mpf(·))` em `ivf` e nas somas por célula (estas protegidas por um `nextafter`, mas sem argumento explícito);
  - a razão L₂/L₀ que define J.
  A escolha de J não afeta a validade do Lema 4′, que vale para qualquer J ≥ 1, mas é corrigida mesmo assim.

## 3. Correções (mesmo método)
- **Extremos exatos:** lidos de `x._mpi_` (mpf bruto) e convertidos para `fractions.Fraction` por `libmp.to_rational`, com
  asserção de finitude.
- **Pontos degenerados:** `iv.make_mpf((raw, raw))`, sem arredondamento.
- **Conversão para binary64 dirigida:** f = float(q), correto ao mais próximo. Se Fraction(f) > q, toma-se o `nextafter`
  para baixo (e simetricamente para cima).
- **W_iv reescrita**, só com operações `mpmath.iv` e decisões de ramo por frações exatas:
  - ramo |v| < 10⁻³: sinc(v) ∈ 1 − [0, (π·x_m)²/6], com x_m exato e W = (L/2)·sinc/(1 − v·v);
  - ramo com sinal definido e ||v| − 1| < 10⁻³: av = ±v (intervalar), x = av − 1 e W = (L/2)·sinc(x)/(av(av + 1));
  - caso geral: fórmula direta, com asserção de que o denominador intervalar exclui 0.
- **Demais:** `mn` devolve o ponto degenerado do menor extremo superior (comparação exata); `ck_inf` é o ponto degenerado
  do extremo inferior exato; bordas das células por floor exato; somas por célula por conversão dirigida.
- **Decisão:** extremo superior exato de total_k ≤ Fraction(1, 10⁶).
- **Varredura:** o script não contém mais conversão de extremos por `mpf(…)` (nem ao ler `.a` ou `.b`).

## 4. Testes obrigatórios antes da reexecução (`cert_testes.py`)
Todos devem passar. Falha em qualquer um impede a reexecução.
- **T1.** W_iv contra a fórmula direta em `mpmath.iv` a 80 dígitos:
  - interseção não vazia (comparação exata de extremos) para v ∈ {±10⁻¹⁵, ±10⁻¹², ±10⁻⁸, ±5·10⁻⁴, ±9,99·10⁻⁴,
    ±10⁻³, ±1,001·10⁻³} e v = ±(1 + δ), com δ ∈ {±10⁻¹⁵, ±10⁻¹², ±10⁻⁸, ±9,99·10⁻⁴, ±10⁻³, ±1,001·10⁻³}, para
    L ∈ {2; 2.519,12…; 10⁴};
  - também com v gerado a partir de ω intervalar;
  - mais 2.000 v aleatórios em [−3, 3].
- **T2.** Valores exatos: W_iv contém L/2 em v = 0 e L/4 em v = ±1.
- **T3.** Conversões: para 10⁴ intervalos (aleatórios e das 47 linhas |c_k|), float_dn ≤ extremo inferior exato e
  float_up ≥ extremo superior exato; ck_inf ≤ extremo inferior de ck.
- **T4.** mn(x, y) ≥ min(sup x, sup y), exatamente, em casos com diferença abaixo da precisão comum.
- **T5.** A decisão compara frações exatas: caso sintético com extremo superior 10⁻⁶ + 10⁻²⁵ deve dar "não".
- **T6.** Varredura textual: nenhum `mpf(` aplicado a extremos no script corrigido.

## 5. Reexecução
- **Saídas:** `cert_blocos.csv`, `cert_tabela.csv` e `cert_resumo.json` (execução 2), com o hash do adendo registrado.
- **Diagnóstico:** comparação par a par com a execução 1.
- **Regras de leitura** de DECLARACAO_CERT §5 inalteradas.
