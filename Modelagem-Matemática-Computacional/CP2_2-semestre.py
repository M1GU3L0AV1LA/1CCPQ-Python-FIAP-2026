A = [
    [1, -2, -2],        # Matriz dos coeficientes
    [-2, 3, 1],
    [3, 2, -1]
]

B = [3, -4, 2]         # Vetor dos resultados

n = len(A)        # Eliminação de Gauss

for i in range(n):
    pivo = A[i][i]

    for j in range(i, n):
        A[i][j] = A[i][j] / pivo
    B[i] = B[i] / pivo

    for k in range(i + 1, n):
        fator = A[k][i]

        for j in range(i, n):
            A[k][j] = A[k][j] - fator * A[i][j]

        B[k] = B[k] - fator * B[i]

x = [0] * n

for i in range(n - 1, -1, -1):
    soma = 0

    for j in range(i + 1, n):
        soma += A[i][j] * x[j]

    x[i] = B[i] - soma

print("x =", x[0])
print("y =", x[1])
print("z =", x[2])