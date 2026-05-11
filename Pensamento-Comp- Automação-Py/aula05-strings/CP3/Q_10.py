matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] % 2 == 0:
            print(matriz[i][j])