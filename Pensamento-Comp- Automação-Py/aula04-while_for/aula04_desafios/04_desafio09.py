''' Determine e mostre todos os números primos no intervalo de 2 a 2000.
Dicas:
▪ Para resolver esse problema, primeiro faça um algoritmo que verifica se um número inteiro qualquer é
primo ou não.
▪ A seguir, com esse código em mãos, faça os ajustes necessários para mostrar todos os números primos
no intervalo solicitado.
▪ Você precisará colocar uma estrutura de repetição dentro da outra.
▪ Laços aninhados!!!! '''

for n in range(2, 2001):
    primo = True

    for i in range(2, n):
        if n % i == 0:
            primo = False
            break

    if primo:
        print(n)