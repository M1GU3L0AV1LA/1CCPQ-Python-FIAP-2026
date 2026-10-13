# Preparando o ambiente
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import sklearn.metrics import confusion_matrix, accuracy_score

# Montando Base de dados
dados = pd.DataFrame({'idade': [22, 25, 47, 52, 46],
'renda': [2000, 2500, 5000, 6000, 5200],
'experiencia': [1, 2, 10, 12, 9],
'comprou': [0, 0, 1, 1, 1]
})

# B)
idade_novo = np.linspace(dados['idade'].min(), dados['idade'].max(), 100)

X_idade = pd.DataFrame({})