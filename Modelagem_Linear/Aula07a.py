# Preparando o ambiente

from collections import Counter
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Criando base de dados
dados = [14]*6 + [15]*12 + [16]*9 + [17]*3
print(dados)
#print(type(dados))

# Frequência absoluta (fi):
fi = pd.Series(Counter(dados)).sort_index()
print(fi)

# Frequência absoluta acumulada (fia):
fia = fi.cumsum()
print(fia)

# Frequência Relativa (fr):
fr = 100 * fi / fi.sum()
print(fr)

# Frequência Relativa acumulada (fra):
fra = fr.cumsum()
print(fra)

# Montando a tabela:
tabela = pd.DataFrame({
    'Frequencia_Absoluta': fi,
    'Frequncia_Absoluta_Acumulad': fia,
    'Frequencia_Relativa': fr,
    'Frequencia_Relativa_Acumulada': fra
})
print(tabela)

# Nome "Total" na última linha:
tabela.loc['Total'] = [
    fi.sum(),
    '-',
    fr.sum(),
    '-'
]

# Tabela de Distribuição de Frequências:
print(tabela)
