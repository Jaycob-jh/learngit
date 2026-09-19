prevalence=0.01
sensitivity=0.99
specificity=0.95
false_positive=1-specificity
p_positive=sensitivity*prevalence+false_positive*(1-prevalence)
posterior=sensitivity*prevalence/p_positive
print(f"P(disease | positive) = {posterior:.3%}")
