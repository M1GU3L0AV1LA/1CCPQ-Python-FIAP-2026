import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Construir base de dados:
dados = pd.DataFrame({
    'horas_estudo': [4, 6, 3, 5, 7],
    'horas_sono': [7, 6, 8, 7, 6],
    'pontuacao': [85, 90, 75, 80, 95]
})

# A) Gráfico de dispersão

sns.pairplot(dados, kind='reg', diag_kind=None)
plt.suptitle("Dispersão entre as variáveis", y=1.02)
plt.show()

# Matriz de Covariância:
print(dados.cov())

# Matriz de Correlação:
print(dados.corr())

# Gráfico de Correlação:
sns.heatmap(dados.corr(), annot=True, cmap='coolwarm')
plt.title("Mapa de Correlação entre Variáveis")
plt.show()

# B)
X = dados[['horas_estudo', 'horas_sono']]
X = sm.add_constant(X)


modelo = sm.OLS(y, X).fit()

# C)
# Y = b0 + b1.X1 + b2.X2 + E
# Pontuação = b0 + b1.Tempo de Estudo + b2.Tempo de Sono

# D)
# R² =
# R²aj =
# p-valor do Teste F =