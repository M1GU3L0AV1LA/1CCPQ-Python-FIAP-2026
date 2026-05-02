'''Faça um programa que receba um número n
▪ Exiba a tabuada deste número do 0 ao 25.
▪ Utilize laços de repetição.'''

n = int(input("Digite um número: "))

for i in range(0, 26):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")
