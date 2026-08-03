'''Crie um programa que:
1. calcule a porcentagem de requisições bem-sucedidas de
cada endpoint;
2. identifique o endpoint com mais erros;
3. verifique se algum endpoint teve dois erros seguidos;
4. classifique cada endpoint como:
▪ ESTÁVEL: pelo menos 80% de sucesso;
▪ INSTÁVEL: menos de 80%;
▪ CRÍTICO: dois erros consecutivos.'''

endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

# print(endpoins[0])
# print(status[0][2])

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# criar funcao para detectar 2 erros seguidos

def erro_seguido(codigo):
