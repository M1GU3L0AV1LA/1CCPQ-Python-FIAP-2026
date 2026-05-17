'''Crie um programa com uma matriz 3x4
▪ 3 linhas
▪ 4 colunas
▪ Atribua valores aleatórios à todas posições da matriz.
▪ Exiba essa matriz.'''

import random

matriz = []

for i in range(3):

    linha = []

    for j in range(4):

        numero = random.randint(1, 100)
        linha.append(numero)

    matriz.append(linha)

print("Matriz 3x4:")

for linha in matriz:
    print(linha)