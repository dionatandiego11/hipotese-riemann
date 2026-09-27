# Controle em GUE: o modelo (G)+(E) prevê K_c(1) de níveis GUE reais? (sem zeros)
import numpy as np, time
from riemann_spectra.controls import generate_gue_central_levels
from riemann_spectra.number_variance import sigma2_gue
from riemann_spectra.bragg_peak import structure_from_sigma2, predictive_kc_tau1, kc_tau1
t0=time.time(); rng=np.random.default_rng(777)
real=np.array([kc_tau1(generate_gue_central_levels(3000, rng=rng)[0]) for _ in range(200)])
k=np.arange(1,300); s2=sigma2_gue(k.astype(float))
for corr in (True, False):
    p=predictive_kc_tau1(structure_from_sigma2(s2, corr), 300, 10, 400, rng)
    print('modelo correcao_1/6=',corr, {k:round(v,3) for k,v in p.items()})
print('GUE real: media %.3f q025 %.3f q50 %.3f q975 %.3f'%(real.mean(),*np.quantile(real,[.025,.5,.975])), '(%.0f s)'%(time.time()-t0))
