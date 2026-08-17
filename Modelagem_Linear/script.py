# Preparando o ambiente
import numpy as np
from scipy.stats import norm

# Erro Padrão da Média Amostral:
dp = 10/np.sqrt(25)

# Probabilidade:
print(norm.cdf(95, 100, dp))

n= 110/50

# Encontrando o erro padrão da média amostral:
ep = 0.7/np.sqrt(50)

# Probabilidade:
print(norm.sf(n,2,ep))
