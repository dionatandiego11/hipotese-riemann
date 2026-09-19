# Adendo 1 ao `ctrl-estadio-v1` — detecção no bloco único e calibração sintética compatível com a FWHM (19/09/2026)

Gravado **antes** de qualquer nível do bilhar ser calculado para o instrumento (o único existente é o teste de k = 100).
SHA-256 em `ADENDO_ESTADIO_1.sha256`. Documentos base:
- declaração `c7ce5d5b…`;
- D1-E `c0c28ed9…`;
- O1 `0f7cb16e…`;
- análise de poder `ANALISE_PODER_11_6.md`.

## 1. Motivos

1. **Poder:** a análise de poder, com níveis GOE sintéticos e validada em ζ e em Maass, prevê para a linha "bouncing
   ball" (L = 2) z entre 1,55 e 2,17 nos blocos g01–g04, contra limiar ≈ 2,65. E-C1 exige detecção cega nos 4 blocos e
   ficaria praticamente inalcançável. Num bloco único com os 12.000 níveis, z ≈ 3,84 contra limiar ≈ 2,97.
2. **Calibração sintética:** o mesmo problema do ADENDO_MAASS_2. Com FWHM de 0,15 a 0,34, 12 linhas isoladas a 10 FWHM
   não cabem na janela, e o laço herdado de m4-v3 não termina.

## 2. Mudanças

1. **Novo bloco primário G:** todos os níveis aceitos com k ∈ [85,4699; 304,0528), ≈ 12.000 níveis, FWHM ≈ 0,0575. Os
   blocos g01–g04 continuam, para **E-C2bb** (como declarado) e como replicação descritiva dos demais critérios.
2. **E-C1 (substitui):** detecção clara sem catálogo, pela regra de m4-v3, **no bloco G**, correspondida a L = 2. A
   detecção em g01–g04 é só descritiva. **Previsão registrada:** z ≈ 3,8 contra limiar ≈ 3,0; passa se o sinal real
   estiver perto do previsto, sem folga grande.
3. **E-C1o e E-C4:** avaliados no bloco G, com as mesmas regras. Em g01–g04 são só descritivos.
4. **E-C2bb:** sem mudança; é avaliado em g01–g04, como declarado. A previsão pelo modelo de ruído do nulo, 46–64% de erro
   relativo, fica registrada. O critério só passa se o resíduo real for muito menor que esse modelo.
5. **Calibração sintética:** mesma regra dos ADENDOS_MAASS_2 e 4: n_iso = min(12, ⌊S/(2·10·FWHM)⌋), com n_iso ≥ 1 e
   ⌈480/n_iso⌉ realizações.
6. **Resultado do controle:** "passa" se E-C1, E-C1o e E-C4 (bloco G) e E-C2bb (g01–g04) passam.

## 3. O que não muda

Sistema, setor, código e chamada do `vergini`, janelas, aceitação por tension, verificações E1–E4, catálogo O1, D1-E e
definição de C̄_bb, nulos (shuffle e GOE), semente e demais parâmetros de m4-v3.
