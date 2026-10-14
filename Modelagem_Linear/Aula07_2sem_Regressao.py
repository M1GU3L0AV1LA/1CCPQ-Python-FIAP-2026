# Preparando o ambiente
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import sklearn
import confusion_matrix

# Montando Base de dados
dados = pd.DataFrame({'idade': [22, 25, 47, 52, 46],
'renda': [2000, 2500, 5000, 6000, 5200],
'experiencia': [1, 2, 10, 12, 9],
'comprou': [0, 0, 1, 1, 1]
})

# A)
modelo = sm.Logit(dados['comprou'],
                  sm.add_constant(dados[['idade',
                                         'renda',
                                         'experiencia']])
                  ).fit()

# B)
idade_novo = np.linspace(dados['idade'].min(), dados['idade'].max(), 100)

X_idade = pd.DataFrame({'const': 1, 'idade': idade_novo, 'renda': dados['renda'].mean(), 'experiencia': dados['experiencia'].mean()})

pred_idade = modelo.predict(X_idade)

plt.plot(idade_novo, pred_idade)
plt.scatter(dados['idade'], dados['comprou'])
plt.title("Sigmoide - Idade")
plt.xlabel("Idade")
plt.ylabel("Probabilidade")
plt.show()

renda_novo = np.linspace(dados['renda'].min(), dados['renda'].max(), 100)

X_renda = pd.DataFrame({'const': 1, 'idade': dados['idade'].mean(), 'renda': renda_novo, 'experiencia': dados['experiencia'].mean()})

pred_renda = modelo.predict(X_renda)
plt.plot(renda_novo, pred_renda)
plt.scatter(dados['renda'], dados['comprou'])
plt.title("Sigmoide - Renda")
plt.xlabel("Renda")
plt.ylabel("Probabilidade")
plt.show()

exp_novo = np.linspace(dados['experiencia'].min(), dados['experiencia'].max(), 100)
X_exp = pd.DataFrame({'const': 1, 'idade': dados['idade'].mean(), 'renda': dados['renda'].mean(), 'experiencia': exp_novo})

pred_exp = modelo.predict(X_exp)
plt.plot(exp_novo, pred_exp)
plt.scatter(dados['experiencia'], dados['comprou'])
plt.title("Sigmoide - Experiência")
plt.xlabel("Experiência")
plt.ylabel("Probabilidade")
plt.show()

# C)
print(modelo.summary()) # Montar a equação com base nos resultados.

# D)
previsoes = modelo.predict(X)
classe = (previsoes > 0.5).astype(int)

# E)
matriz_confusao = confusion_matrix(x, classe)
acuracia = accuracy_score(y, classe)

# F)
dados['classificacao'] = classe

# G)
novo = pd.DataFrame({'const': [1], 'idade': [27], 'renda': [3850], 'experiencia': [5]})

prob = modelo.predict(novo)
print("Probabilidade:", prob.values[0])

classe_novo = (prob > 0.5).astype(int)
print("Classe prevista:", classe_novo.values[0])