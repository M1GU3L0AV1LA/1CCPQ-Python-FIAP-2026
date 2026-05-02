''' Escreva um programa que dado um inteiro n positivo calcula e imprime a soma de todos os números
inteiros entre 1 e n.
▪ Valide a entrada do usuário, só aceite números positivos!!
▪ Dica: use while para a validação e for para a soma.
▪ Por exemplo, se n = 10 então deverá ser calculado:
▪ 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
▪ E a impressão final seria:
▪ A soma de 1 até 10 é: 55 '''

n = int(input("Digite um número inteiro e positivo: "))

while n <= 0:
    print("Não é possível utilizar esse valor!")
    n = int(input("Digite um número inteiro e positivo: "))

soma = 0
for i in range(0, n + 1):
    soma += i

print(f"A soma de 1 até {n} é: {soma}")