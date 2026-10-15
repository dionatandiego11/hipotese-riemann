# Declaração anterior — reinício analítico dos momentos negativos, 13/10/2026

Prioridade do usuário: conjectura das razões, termos principais C7/C8 e
termos inferiores. Primeiro auditar a Etapa B antiga, preservando original.
Não aceitar erro O(T^(1/2+ε)) ou ausência de T/log T sem uniformidade no
limite do deslocamento. Fontes principais: Pearce-Crump v1 e Conrey–Snaith
v2, já arquivadas. Dados reservados e zeros não serão lidos ou calculados.

Alvos finitos: resíduos e partes finitas das diagonais D7,D8 para
q∈{1,4,5,8,12}; conferir por extrapolação em α=10^(−4),10^(−6),10^(−8)
a 70 dígitos. Fórmulas analíticas declaradas antes: R7=A_q,
F7=R7[γ−2ζ'(2)/ζ(2)+Σ_{p|q}log p/(p+1)]; R8=φ(q)/q,
F8=R8[γ+Σ_{p|q}log p/(p−1)]. Partes finitas NÃO são declaradas termos
inferiores dos momentos discretos.
Modelo com dois zeros artificiais: separações d=1,1/100 e ε/d=1,1/10,1/100;
conferir por quadratura direta em toda a reta as formas fechadas de
(ε/π)∫1/|F|² e de (ε/π)∫|H/F|², F=(s−ρ1)(s−ρ2),
H=s−(ρ1+ρ2)/2. Não há zeros reais da zeta ou de L no piloto.

Código novo centralizado em src/riemann_spectra/negative_moments_ratios.py.
Testes rápidos sem rede. Verificação: RLIMIT_CPU60 s, sem filhos, não
certificada por intervalos; relatar precisão e CPU/parede/RSS. Não testar
novidade, ajustar às tabelas ou ampliar dados. Se a Etapa B tiver falha,
registrar errata e corrigir o rascunho local; PDFs/pacotes anteriores
preservados. Sem publicação, envio ao autor ou commit.
