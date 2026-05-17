'''Faça um programa que tenha 2 vetores.
Um vetor para os meses e outros para a quantidade de dias
para cada mês.
▪ Seu programa deve exibir mensagens da seguinte forma:
▪ O Mês de Jan tem 31 dias ao todo.
▪ O mês de Fev tem 28 dias ao todo.
▪ O mês de Mar tem 31 dias ao todo.
▪ ...
▪ O mês de Dez tem 31 dias ao todo.'''

# Vetor com os meses
meses = [
    "Jan", "Fev", "Mar", "Abr",
    "Mai", "Jun", "Jul", "Ago",
    "Set", "Out", "Nov", "Dez"
]

# Vetor com quantidade de dias
dias = [
    31, 28, 31, 30,
    31, 30, 31, 31,
    30, 31, 30, 31
]

# Percorre os vetores
for i in range(len(meses)):
    print(f"O mês de {meses[i]} tem {dias[i]} dias ao todo.")