from math import sqrt
from scipy.stats import norm

# Encontrar Zc
print("Zc = ", ((55 - 53) - (0)) / sqrt( (7.5/5) + (5/5) ))

# Encontrar Za
print("Za/2 = ", norm.ppf(0.025))