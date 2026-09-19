# Protocolo do registro de hipóteses — versão 1 (19/09/2026)

Regras fixas do registro [docs/REGISTRO_HIPOTESES.md](../../docs/REGISTRO_HIPOTESES.md). Gravadas **antes** de qualquer
hipótese ser testada por este registro. SHA-256 em `PROTOCOLO_REGISTRO_v1.sha256`. Uma mudança nestas regras exige uma
versão nova (v2, …), com hash, e só vale para hipóteses declaradas depois dela.

## 1. Para que serve

Testar, com o instrumento validado (cadeia m4-v3 e seus controles da 11.6), hipóteses de terceiros ou do projeto que
façam **previsões espectrais concretas**:
- posições de linhas;
- coeficientes e sinais;
- contagem;
- estatística local dos níveis.

Cumpre o papel da Etapa 11.5 (testes discriminantes) e o estende a hipóteses fora da matriz de operadores.

**Pré-requisito:** o registro só começa a **testar** depois que os três controles da 11.6 (Dirichlet, estádio, Maass)
tiverem resultado registrado, qualquer que seja. Antes disso, as hipóteses só podem ser propostas e triadas.

## 2. Ciclo de vida de uma hipótese

`proposta` → `triada` → `declarada` → `testada` → `encerrada`

1. **Proposta:** enunciado curto, fonte e rótulo provisório. Nada é calculado.
2. **Triada:** decide se a hipótese está no domínio do instrumento (§4) e se já foi testada na literatura. Hipótese
   fora do domínio fica `encerrada (fora do domínio)`, com o motivo.
3. **Declarada:** documento próprio em `results/registro_hipoteses/H-xxx/DECLARACAO.md`, com hash, contendo:
   - previsão numérica ou qualitativa **fixada**;
   - critério de sucesso e critério de **refutação**;
   - dados de teste (§3);
   - estatística e nível de significância;
   - leitura prevista para cada resultado possível.
4. **Testada:** execução conforme a declaração. Qualquer desvio só por adendo, **antes** de rodar.
5. **Encerrada:** o resultado é registrado — confirmada, refutada, inconclusiva ou fora do domínio. **Nada é apagado.**

## 3. Dados

- **T0 (já vistos):** zeros 1–100.000 de ζ (M1–M4, certificado). Qualquer teste de hipótese em T0 é **exploratório**
  (rótulo C no máximo), porque esses dados já influenciaram decisões do projeto.
- **T1 (reserva confirmatória):** dados que nenhuma decisão do projeto usou até a data da declaração. Candidatos, a
  fixar por adendo a este protocolo **antes** de baixar ou calcular:
  - tabelas de zeros de Odlyzko em outras alturas;
  - zeros de ζ calculados pelo projeto em faixa nova;
  - zeros de outras funções L.

  Os dados dos controles da 11.6 (L(s, χ₋₄), L(s, χ₅), estádio, Maass) passam a T0 depois que os controles forem
  avaliados.
- **Regra de uso:** uma hipótese só pode ser declarada **confirmada** com dados T1 que ela não viu, abertos só depois
  da declaração. Cada lote T1 tem manifesto com hash e data de abertura.

## 4. Domínio do instrumento

Entram hipóteses que prevejam, para uma sequência de níveis ou zeros:
- linhas (posição, coeficiente complexo, sinal);
- contagem ou densidade;
- estatística local (espaçamentos, R₂, variância).

Não entram (ficam `fora do domínio`): afirmações sem previsão espectral e hipóteses de outros sistemas sem controle
próprio. Exemplo: Collatz, que tem as etapas CL0–CL5 do plano complementar.

## 5. Refinamento

Um refinamento é uma **hipótese nova** (H-xxx.2, …), com declaração própria, e só pode ser confirmado em dados T1 que
**nenhuma** versão anterior viu. O resultado da versão anterior fica registrado como está.

## 6. Testes múltiplos

- Todas as hipóteses testadas confirmatoriamente formam uma família.
- O controle é por Benjamini–Hochberg com taxa de falsas descobertas de 10%, aplicado ao conjunto de p-valores
  confirmatórios na data de cada relatório. O relatório também informa o resultado sob Holm (5%).
- Hipóteses exploratórias (T0) não entram na família e não podem ser anunciadas como confirmadas.

## 7. Rótulos e afirmações

- **A:** teorema com hipóteses. **B:** reprodução numérica. **C:** achado experimental. **D:** conjectura.
- Separar sempre o que é condicional (RH, GRH, conjecturas) do que não é.
- **Novidade** só pode ser afirmada depois de busca bibliográfica registrada. "Já testada na literatura" é informação
  obrigatória da triagem.

## 8. Fontes

Só vale o que foi lido na fonte, com página (regra geral do projeto). Texto gerado por IA e resumos de busca não são
fonte. Em 19/09/2026, por exemplo, dois resumos de outro assistente trouxeram atribuições erradas, registradas nas §§17
e 20 das pendências de fontes.
