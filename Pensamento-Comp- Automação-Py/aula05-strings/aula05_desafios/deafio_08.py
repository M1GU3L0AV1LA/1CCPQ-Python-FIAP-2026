'''Faça um programa que realize a soma de duas matrizes, com mesmas dimensões. Seu programa deve
ter 2 matrizes A e B de números inteiros. A terceira matriz deve ser a soma de A com B'''

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]

soma = []

for i in range(len(A)):

    linha = []

    for j in range(len(A[i])):
        linha.append(A[i][j] + B[i][j])

    soma.append(linha)

print("Matriz Soma:")

for linha in soma:
    print(linha)