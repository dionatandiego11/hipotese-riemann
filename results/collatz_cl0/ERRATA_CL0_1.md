# Errata documental CL0 — 25/09/2026

A especificação v1, protocolo e configuração congelados permanecem intactos. Esta errata corrige a frase após a cadeia de inclusões na §2 da ESPECIFICACAO_CL0_v1.md. Não executa CL1 nem altera números esperados ou critérios.

A frase que identifica Q_odd com a imagem dos pontos eventualmente periódicos “sob a codificação de paridades” mistura a codificação binária e a conjugação de Collatz. Sua leitura como igualdade Φ(Q_odd)=Q_odd não é um resultado demonstrado na fonte.

**Redação substitutiva:** identificando sequências binárias com Z₂, os pontos eventualmente periódicos do shift S são precisamente Q_odd. Se Q=Φ⁻¹ é a codificação de paridades, Q∘T=S∘Q, então

    EPer(T)=Φ(Q_odd) ⊆ Q_odd,
    Q(x)∈Q_odd ⇔ x∈EPer(T).

A inclusão vem da equação afim de uma órbita eventualmente periódica. A igualdade Φ(Q_odd)=Q_odd é a conjectura de periodicidade apresentada pela fonte, não uma hipótese disponível gratuitamente. Não confundir com a conjectura apenas sobre inteiros positivos.

**Evidência:** Monks–Yazinski, PDF já arquivado em `archive/fontes_etapa11/hipoteses_20260919/monks_yazinski.pdf`, pp. 2–3: descrição de Q_odd, conjugação e Teorema 2.1. Esta leitura estabelece a distinção na fonte; não é uma revisão exaustiva do estado atual da conjectura.

**Impacto:** as contagens simbólicas finitas de CL1 não dependem da igualdade conjectural. Qualquer transporte posterior de resultados para todos os racionais precisa respeitar a inclusão. A revisão não afirma que todo o restante da CL0 foi auditado.

Complemento bibliográfico: as normas do transporte e da composição em ℓᵖ têm antecedente explícito nos Teoremas 4.2–4.3 de Leventides–Poulios (2020), registrado em `hipoteses/RODADA_BIBLIOGRAFICA_20260925.md`. Isso não muda as derivações locais, mas impede atribuir-lhes novidade.
