''' Escreva um algoritmo que lê um número inteiro n, cria um vetor de inteiros de tamanho n, faz a leitura
de um conjunto de n números inteiros armazenando-os no vetor e depois calcula a somatória dos
números contidos no vetor.
▪ Dica: note que a somatória deverá ser feita após o vetor estar preenchido. Escreva um algoritmo que lê um número inteiro n, cria um vetor de inteiros de tamanho n, faz a leitura
de um conjunto de n números inteiros armazenando-os no vetor e depois calcula a somatória dos
números contidos no vetor.
▪ Dica: note que a somatória deverá ser feita após o vetor estar preenchido.'''

n = int(input("Digite a quantidade de números: "))

vetor = []

for i in range(n):
    numero = int(input(f"Digite o número da posição {i}: "))
    vetor.append(numero)

soma = 0

for numero in vetor:
    soma += numero

print("\nVetor:", vetor)
print("Somatória dos números:", soma)