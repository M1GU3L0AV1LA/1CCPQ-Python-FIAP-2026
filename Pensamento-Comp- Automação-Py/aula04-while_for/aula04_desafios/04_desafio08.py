''' ▪ Escreva um algoritmo que recebe um inteiro positivo n e imprime todos os divisores positivos de n.
▪ Utilize o laço for.
▪ Exemplo:
Suponha que n = 28, nessa situação devemos imprimir os números
1, 2, 4, 7, 14 e 28, que são todos os divisores do 28.
▪ Dica: para o número ser divisor de n, a divisão precisa ter resto nulo. '''

n = int(input("Digite um número inteiro e positivo: "))

while n <= 0:
    print("Não é possível utilizar esse valor!")
    n = int(input("Digite um número inteiro e positivo: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)