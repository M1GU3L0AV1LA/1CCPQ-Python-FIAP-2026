'''
▪ Você foi contratado para criar um pequeno sistema que analisa uma lista de endereços de e-mail de
alunos da FIAP e gera um relatório.
▪ O programa deve:
▪ Receber uma lista de e-mails digitada pelo usuário (separados por vírgula).
▪ Exemplo: joao.silva@fiap.com.br, maria.souza@fiap.com.br, ana.paula@fiap.com.br
▪ Separar cada e-mail em:
▪ Nome de usuário (parte antes do @)
▪ Domínio (parte depois do @)
▪ Contar quantos e-mails pertencem a cada domínio usando um dicionário
'''

# input emails + separa por vírgula
entrada = input('Digite os emails separados por vígula: ')
emails = entrada.split(",")

dominios = {}                # cria um dicionário
for email in emails:
    usuario, dominio = email.split('@')      # separa usuario do dominio

    if dominio in dominios:
        dominios[dominio] += 1
    else:
        dominios[dominio] = 1

for dominio, quantidade in dominios.items():    # saída com items() pega chave e valores juntos
    print(f"{dominio}: {quantidade} email(s).")
