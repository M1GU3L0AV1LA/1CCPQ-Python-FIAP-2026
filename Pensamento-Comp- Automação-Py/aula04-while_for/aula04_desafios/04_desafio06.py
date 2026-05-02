''' Faça um programa capaz de exibir todos os valores pares entre 2 e um valor fornecido pelo usuário. '''

n = int(input("Digite um número:"))

for i in range(2, n + 1):
    if i % 2 == 0:
        print(i)



