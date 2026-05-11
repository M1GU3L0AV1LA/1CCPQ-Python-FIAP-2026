matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

contador = 0

for linha in matriz:
    for valor in linha:
        if valor > 5:
            contador += 1

print(contador)