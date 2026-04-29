# Gráficos para Variáveis Qualitativas
# Setores
from collections import Counter
import matplotlib.pyplot as plt

dados1 = ['Sim'] * 20 + ['Não'] * 45
print(dados1)

respostas1 = Counter(dados1)
print(respostas1)

plt.pie(list(respostas1.values()),
        labels=list(respostas1.keys()),
        autopct='%1.2f%%',
        colors=['red', 'blue'])

plt.title('Respostas Entrevista')
plt.legend (list(respostas1.keys()), loc='upper right')
plt.show()


