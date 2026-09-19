# Adendo 1 ao protocolo do registro v2 — teste registrado durante a aquisição, antes da análise (19/09/2026)

Protocolo: `PROTOCOLO_REGISTRO_v2.md` (`55514a35…`). SHA-256 deste adendo em `ADENDO_REGISTRO_v2_1.sha256`. Motivado pela
revisão do usuário de 19/09/2026 (P-R1 e dados de Dirichlet).

## 1. O conflito

O v2 exige, para confirmação, dados T1 **fixados antes de calcular os dados** (§3) e só permite testar depois dos três
controles da 11.6 (§1). A aquisição dos zeros de L(s, χ₋₄) e L(s, χ₅) já começou (19/09/2026, 13:42), e o controle do
estádio ainda não tem resultado.

## 2. Exceção, explícita e limitada

Fica criada a categoria **"T1-prospectivo"**: dados cuja aquisição já começou, mas que ninguém analisou, e que são
reservados por declaração com hash **antes** de qualquer análise. **Não equivale** a uma declaração anterior à
aquisição; todo relatório que use essa categoria tem de dizer isso.

Condições:
1. **Registro de acesso**: listar exatamente quais arquivos, resumos e métricas desses dados já foram acessados e por
   quem.
2. Blocos que contenham dados já usados (por exemplo, pilotos) ficam **fora** da reserva.
3. A previsão é um **procedimento determinístico com hash** (script congelado), que só usa informação permitida pela
   declaração e **nunca** o erro observado.
4. A execução do controle e a avaliação do teste ficam na ordem fixada pela declaração, sem ajustar nada entre elas.
5. **Exceção ao §1:** um teste T1-prospectivo pode ser avaliado antes de os três controles terem resultado, desde que
   não dependa de controle pendente. Isso é necessário, porque os dados deixariam de ser T1 depois da análise do
   controle a que pertencem.
6. **Família confirmatória:** fica fechada na data de cada relatório; se tiver um único teste, não há correção.
   Dependência entre blocos contíguos do mesmo espectro é reconhecida: os blocos **não** contam como observações
   independentes, e os critérios usam agregação sobre os blocos, não contagem de "sucessos" independentes.

## 3. Primeiro uso

`H-004/DECLARACAO.md` (P-R1): previsão do erro do estimador nos blocos e02–e04 e f02–f04 do `ctrl-dirichlet-v1`.
