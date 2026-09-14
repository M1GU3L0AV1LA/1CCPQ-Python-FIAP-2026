from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    stage = input("Etapa no funil: ")

    # valida os dados aqui!!
    # depois de validado, precisamos modelar o lead como um dict
    # para isso, usamos o model

    print(model_lead(name,email,stage))

    # agora... com meu lead modelado  com um dict
    # precisamos enivar esse lead para o leads.json
    # para isso, vamos usar o control1
    control.create_lead(model_lead(name,email,stage))

    print("Lead adicionado (func)")

def list_leads():
    leads = control.read_leads()        #DESAFIO: Formatar como tabela
    print(leads)


def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar Lead")
        print("[2] Listar Leads")
        print("[3] Sair do programa")

        opt = input("Escolha uma opção:")

        if opt == "1":
            add_lead()
        elif opt == "2":
            print("\nLead listado")
        elif opt == "0":
            print("\nSaindo do programa")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()