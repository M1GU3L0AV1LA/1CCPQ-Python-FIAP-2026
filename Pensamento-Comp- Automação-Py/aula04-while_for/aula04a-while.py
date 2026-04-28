cp = 0
while cp < 10:
    cp += 1
    if cp == 3:
        continue  # ignora oque ta embaixo na estrutura de repeticao e continua

    if cp == 7:
        break

    print(f"Produto {cp}")

# While decrecente de 4 até 1

i = 4
while i > 0:
    print(i)
    i -= 1