'''
▪ Você foi contratado para criar um pequeno sistema que analisa uma lista de endereços de e-mail de
alunos da FIAP e gera um relatório.
▪ O programa deve:
▪ Criar uma tupla com todos os nomes de usuário e exibir o primeiro e o último.
▪ Trocar a ordem do primeiro e último nome de usuário usando atribuição de tupla (sem variável temporária).
▪ Exibir o relatório final, por exemplo:
▪ Relatório:
▪ Quantidade de e-mails por domínio:
▪ fiap.com.br: 3
▪ Lista de usuários: ('ana.paula', 'joao.silva', 'maria.souza')
▪ Após troca de posições: ('maria.souza', 'joao.silva', 'ana.paula')
Dicas:
▪ Use split('@') para separar nome de usuário e domínio.
▪ Use um dicionário para contar os domínios.
▪ Use tuple(lista) para converter uma lista em tupla.
▪ Use a, b = b, a para trocar valores.
'''

entrada = input("Digite os e-mails separados por vírgula: ")
emails = entrada.split(",")

users = []
dominios = {}

for email in emails:
    user, dominio = email.split("@")
    users.append(user)               # adiciona o usuario na lista

    if dominio in dominios:
        dominios[dominio] += 1
    else:
        dominios[dominio] = 1

users = tuple(users)

primeiro = users[0]
ultimo = users[-1]

primeiro, ultimo = ultimo, primeiro

users_trocados = (primeiro, *users[1:-1], ultimo)

print("\nRelatório: ")
print("Quantidade de emails por domínio: ")

for dominio, quantidade in dominios.items():
    print(f"{dominio}: {quantidade}")

print("Lista de usuários: ",  users)
print("Após trocar de posições: ", users_trocados)