# Adendo técnico 1 — antes de qualquer espectro

A tentativa 1 falhou na importação de threadpoolctl (ausente no ambiente); nenhum pai foi gerado e não existe checkpoint. Log, código e lock dessa tentativa preservados em tentativa1_importacao/.

Correção: ler Threads de /proc/self/status no início, em cada pai e no fim, sem instalar dependência. Variáveis de BLAS permanecem em 1; o número de threads do processo será verificado, não inferido delas. Desenho, sementes, observáveis e decisões inalterados.

A CPU da tentativa de importação não foi medida separadamente. Reserva conservadora de 10 s para essa tentativa curta; novo RLIMIT_CPU de 590 s e parada cooperativa antes de 560 s, mantendo teto nominal agregado de 600 s. Nenhum resultado científico consultado.
