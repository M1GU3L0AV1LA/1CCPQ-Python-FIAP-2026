'''Escreva um algoritmo que recebe uma lista de nomes e imprime os nomes na ordem inversa a da
leitura.
▪ A lista termina quando o usuário aperta o Enter sem que nenhum nome tenha sido digitado. '''

nomes = []

while True:

    nome = input("Digite um nome: ")

    if nome == "":
        break

    nomes.append(nome)

print("\nNomes em ordem inversa:")

for i in range(len(nomes) - 1, -1, -1):
    print(nomes[i])