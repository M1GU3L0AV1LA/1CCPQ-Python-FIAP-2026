# Preparando o ambiente
import pandas as pd
import matplotlib.pyplot as plt

#Conjunto de dados:
vendas_camisetas = pd.Series([2, 4, 3, 4, 5, 2, 4, 11])

# Análise exploratória de dados: etapa da estatística descritiva
# Medidas de Tendência Central:
# Média:
print("Média:", vendas_camisetas.mean())

# Mediana:
print("Mediana:", vendas_camisetas.median())

# Moda:
print("Moda:", vendas_camisetas.mode())

# Mínimo:
print("Mínimo:", vendas_camisetas.min())

# Máximo:
print("Maximo:", vendas_camisetas.max())

# Amplitude:
print("Amplitude:", vendas_camisetas.max()-vendas_camisetas.min())

# Variância:
print("Variância:", vendas_camisetas.var())

# Desvio Padrão:
print("Desvio padrão:", vendas_camisetas.std())

# Coeficiente de Variação:
print("Coeficiente de variação:", vendas_camisetas.std() / vendas_camisetas.mean() * 100)

# Medidas Separatrizes:
# Quartis:
print("Quartis:", vendas_camisetas.quantile([0.25, 0.50, 0.75]))

# Análise Gráfica: Boxplot
plt.boxplot(vendas_camisetas,
            patch_artist=True,
            boxprops=dict(facecolor='red'))
plt.show()

# Medidas Resumo:
print("Medidas Resumo:", vendas_camisetas.describe())