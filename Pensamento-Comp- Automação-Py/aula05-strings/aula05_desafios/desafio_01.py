'''Escreva um algoritmo que recebe um número inteiro n > 0, cria um vetor de números reais com n
posições e preenche o vetor com n números aleatórios reais.
▪ Depois de preenchido o vetor, imprima na tela todos os números gerados'''

import random

n = int(input("Digite quantos números seu vetor irá receber: "))
vetor = []

for i in range(n):
    vetor.append(random.randint(0,99))

print(f"Seu vetor ficou assim = {vetor}.")
