import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Conjunto de dados:
dados = pd.DataFrame({
    'Qtd_Poluente': [1, 2, 3, 4, 5, 6,],
    'Dano_Eco': [3, 6, 7, 10, 10, 12]
})

# A)
sns.scatterplot(x='Qtd_Poluente', y='Dano_Eco', data=dados)
plt.title('Dispersão: Quantidade de Poluentes X Dano Ecológico')
plt.xlabel('Quantidade de Poluentes (Ug/L')
plt.ylabel('Dano Ecológico')
plt.show()

# Covariância:
print(np.cov(dados['Qtd_Poluente'], dados['Dano_Eco'])[0, 1])

# Coeficiente de Correlação de Pearson:
print(np.corrcoef(dados['Qtd_Poluente'], dados['Dano_Eco'])[0, 1])

# Gráfico de Correlação:
sns.heatmap(dados.corr(), annot=True, cmap='coolwarm')
plt.title("Mapa de Correlação")
plt.show()

# B)
modelo = sm.OLS(dados['Dano_Eco'],
                sm.add_constant(dados['Qtd_Poluente'])
                ).fit()

sns.regplot(x='Qtd_Poluente',
            y='Dano_Eco',
            data=dados,
            ci=None,
            line_kws={'color': 'red'},)

plt.title('Gráfico de Dispersão com Reta de Regressão')
plt.xlabel('Quantidade de Poluentes (ug/L)')
plt.ylabel('Dano Ecológico')
plt.show()

# C)
print(modelo.summary())

# Y = a + b.X + E
# Dano Ecológico = a + b.Quantidade de Poluente + E

#p-value do Teste F = Prob (F-statistics):

# E)
nova_obs = 9
intercepto, coeficiente = modelo.params
print(intercepto + coeficiente * nova_obs)