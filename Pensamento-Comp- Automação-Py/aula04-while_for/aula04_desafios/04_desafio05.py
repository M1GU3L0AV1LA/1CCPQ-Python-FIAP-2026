''' Faça um programa que receba 5 valores digitados pelo usuário e, ao final, informe qual é o maior deles. '''

maior = int(input("Digite um número: "))

for i in range(4):
    num = int(input("Digite outro número: "))

    if num > maior:
        maior = num

print("O maior número é:", maior)
