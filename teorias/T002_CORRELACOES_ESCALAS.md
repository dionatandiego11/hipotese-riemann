# T002 — Cancelamento aritmético, análise de Fourier e escalas

14/10/2026. Natureza da conexão: **D — proposta exploratória**, sem novidade estabelecida. Primeiro alvo: `pendente`. Prioridade: alta.

**Em linguagem simples:** o erro é uma soma de muitas contribuições com sinais e fases. Queremos descobrir em quais escalas elas se cancelam e em quais se reforçam.

**Base disponível.** O resto tem uma representação exata fora da diagonal na região de convergência absoluta. Seu núcleo é

    K(ω)=∫_A^T exp(itω)dt,  |K(ω)|≤min(T−A,2/|ω|),
    ω=log(n/m).

Os coeficientes envolvem Möbius ou Liouville, convoluções e caracteres. A representação ainda não foi levada à região crítica com erro controlado.

**Ideia D.** Separar os inteiros em blocos de tamanho comparável e escrever n=m+h. Isso aproxima a frequência multiplicativa log(n/m) por uma frequência aditiva h/m. A conexão é entre a nossa transformada em logaritmos e correlações aditivas de sequências aritméticas.

**Primeiro alvo matemático.** Numa banda m de tamanho X e |h|≤m/2, demonstrar e propagar a estimativa

    |log(1+h/m)−h/m|≤h²/m²

através de K, mantendo as somas de coeficientes no orçamento. Derivar depois que tipo de controle de correlações torcidas seria suficiente em cada banda. Não declarar que esse controle de correlações já existe.

**Previsão estrutural a examinar.** A faixa |h| da ordem X/(T−A) tende a manter o núcleo coerente; fora dela há oscilação, que só ajuda se for usada com os coeficientes. A estimativa depende de A,T e não constitui sozinha um teorema de cancelamento.

**Por que pode ajudar.** Converte o erro global numa lista de regimes: quase diagonal, intermediário e afastado. Uma obstrução localizada também é informação útil.

**O que enfraquece a rota.** A linearização introduzir erro tão grande quanto o termo principal, ou apenas trocar a conjectura por uma hipótese de correlações igualmente forte sem redução concreta.

**Ligação à ponte:** é o caminho mais direto para a cota do resto. A continuação/truncamento das séries permanece uma dependência, não uma operação implícita.

**Leitura local:** [erro e representação fora da diagonal, §§5–6](../hipoteses/RAZOES_ERRO_PERFIL_POLAR_20261014.md). Bibliografia especializada para as estimativas de correlações ainda a conferir.
