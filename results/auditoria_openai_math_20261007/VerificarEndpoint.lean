-- Preparado, NÃO compilado. Exige ambiente da release fixada.
import OAI.NumberTheory.DirichletL.Endpoint
#print axioms OAI.SevenEighths.Endpoint.endpoint_identity
#print axioms OAI.SevenEighths.Endpoint.balanced_endpoint_margin
example {δ y : ℝ} (hd0 : 0 ≤ δ) (hd1 : δ ≤ 5 / 6)
    (hy0 : 0 ≤ y) (hy1 : y ≤ 1 / 2) :
    (49 : ℝ) / 440640 ≤ -OAI.SevenEighths.Endpoint.balancedExponent δ y :=
  OAI.SevenEighths.Endpoint.balanced_endpoint_margin hd0 hd1 hy0 hy1
