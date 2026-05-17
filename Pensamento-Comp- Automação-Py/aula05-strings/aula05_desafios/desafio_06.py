'''Escreva um algoritmo que lê um número inteiro n > 0 e preenche um vetor de caracteres de n
posições.
▪ Depois de preencher o vetor, você deverá inverter o seu conteúdo, ou seja, trocar o conteúdo da
primeira posição (0) com a ´ultima (n − 1) a segunda com a penúltima e assim por diante até que o
vetor esteja invertido.'''

n = int(input("Digite o tamanho do vetor: "))

vetor = []

for i in range(n):
    caractere = input(f"Digite o caractere da posição {i}: ")
    vetor.append(caractere)

print("\nVetor original:")
print(vetor)

inicio = 0
fim = n - 1

while inicio < fim:
    temp = vetor[inicio]
    vetor[inicio] = vetor[fim]
    vetor[fim] = temp

    inicio += 1
    fim -= 1

print("\nVetor invertido:")
print(vetor)