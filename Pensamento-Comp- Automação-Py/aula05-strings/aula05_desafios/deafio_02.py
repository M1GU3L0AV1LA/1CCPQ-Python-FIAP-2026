'''Considere uma turma de n alunos onde desejamos calcular a média das notas da prova semestral e
saber quantas notas estão iguais, acima e abaixo dessa média.
▪ Escreva um algoritmo que lê um inteiro n representando a quantidade de alunos e cada uma das n
notas e mostra a média da turma, quantas notas são iguais, acima e abaixo da média da turma'''
from numpy.lib import scimath

alunos = int(input("Quantos alunos deseja calcular? "))

vetor_alunos = []

for i in range(alunos):
    notas = int(input("Qual a nota do aluno? "))
    vetor_alunos.append(notas)

media = sum(vetor_alunos)/alunos

acima = 0
abaixo = 0
iguais = 0

for nota in vetor_alunos:
    if nota > media:
        acima += 1
    elif nota < media:
        abaixo += 1
    else:
        iguais += 1


print("A média da turma:", media)
print("Notas acima da média:", acima)
print("Notas na média:", iguais)
print("Notas abaixo da média:", abaixo)
