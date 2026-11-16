import pandas as pd 
import numpy as np

df = pd.read_csv("dados/sp156.csv", sep=";", enconding="utf-8", low_memory=False)

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head())
print(df.isna().mean().sort_values(ascending=False))

# “Quais fatores aumentam o tempo de atendimento e a chance de atraso, e o que o assistente digital deve priorizar?”
# Y contínuo: tempo de atendimento em dias.
# Y binário: 1 se atendeu dentro do prazo, 0 se não. Defina o prazo com um critério justificável, por exemplo a mediana do tempo ou o prazo oficial do serviço, se a base trouxer.
# X quantitativas: por exemplo volume de chamados no distrito no mês, hora ou dia da abertura, e nº de solicitações do mesmo tipo.

df[]