# Registro de preparação do commit — 14/10/2026

Escopo: trabalho acumulado de auditorias bibliográficas, Collatz e razões/momentos negativos; código, testes, declarações, resultados e documentação. Sem novas análises de zeros nem mudança de critérios científicos nesta preparação.

A conferência dos manifestos de razões verificou 70 referências a arquivos: 69 coincidem. Uma referência histórica aponta para o plano vivo, posteriormente ampliado pelas continuações R3:

- Arquivo: `hipoteses/PLANO_RAZOES_MOMENTOS_NEGATIVOS.md`.
- SHA-256 no manifesto inicial de 13/10: `30926d05d6c42caf0b4cce80b466238d2912895072902366f434d7a7b93622a3`.
- SHA-256 após as continuações: `cb5c1cb0a2abcf63a00636658840c6d045111dcf61d05407f73267073f0a5cc7`.

A divergência é documental e fica explícita: o hash antigo não valida a versão atual do plano. O manifesto inicial foi preservado, sem reescrever o registro anterior. As verificações não encontraram divergências nas demais referências examinadas. Isso não é auditoria matemática independente.

O diff dos arquivos anteriormente versionados passa com `core.whitespace=cr-at-eol`, respeitando o formato CRLF do manifesto bibliográfico. No conjunto completo preparado, a checagem aponta quebras Markdown com dois espaços e um espaço em log TeX; os artefatos históricos e seus hashes foram preservados. Nenhuma normalização dos bytes antigos foi aplicada.

Os PDFs/HTMLs/fontes TeX de terceiros em `archive/fontes_etapa11/` continuam locais, conforme `.gitignore`; os registros de URL e hashes entram no commit. Os arquivos soltos `paper2.pdf` e `HUTRKGobAAAMnI5.jpeg` ficam fora. Os testes científicos já executados estão nos registros de cada etapa; não foram repetidos apenas para fazer o commit.
