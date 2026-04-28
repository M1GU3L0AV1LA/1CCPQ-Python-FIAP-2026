num1 = 5
num2 = 2

print(type(num1), type(num2))

resultado_operacao = num1 // num2
print(resultado_operacao, type(resultado_operacao))

# OPERADORES DE ATRIBUIÇÃO
num = 15
print() #PULAR LINHA
print(num)

num = num + 2 #ACUMULAMDO 2 EM NUM
print(num)

num -= 2
print(num)

#OPERADORES RELACIONAIS
print(6 >= 6)

idade = 20
print(idade >= 21)  #BOOLEANO

logado = True
print(logado, type(logado))

maior_idade = idade >= 18
print(maior_idade, type(maior_idade))

#STRING
nome1 = "Marcos"
nome2 = "marcos"

print(nome1.upper() == nome2.upper())
