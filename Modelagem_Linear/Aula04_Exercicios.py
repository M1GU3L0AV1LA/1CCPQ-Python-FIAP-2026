'''
# Exemplo 3
tem_cafe = False

if not tem_cafe:
    print("Precisamos fazer mais café")

else:
    print("Print já temos cáfe o suficiente")
'''
import math

'''
# Exemplo 4
for i in range(5):
    print("Número:", i)
'''
'''
# Exemplo 5
n = 0
while n <= 10:
    print("Número:", n)
    n += 1
'''
'''
#Exemplo 6
def area_triangulo(b,h):
    return (b * h)/2

print(area_triangulo(2,14))
'''
'''
#Exemplo 7
def area_circunferencia(r):
    return math.pi * r**2
print(area_circunferencia(10))
'''
'''
#Localizando o Workspace do Python (directory)
import os
print(os.getcwd())
'''

#Leitura de arquivos
'''
#TXT
import pandas

dados1 = pandas.read_csv("DadosAula(2).txt", sep=" ", header=0)
print(dados1)
'''
'''
#CSV
import pandas

dados2 = pandas.read_csv("DadosAula(2).csv", sep=" ", header=0)
print(dados2)
'''