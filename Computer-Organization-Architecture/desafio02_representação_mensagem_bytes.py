'''
2 - Desenvolva um programa que receba uma mensagem e
apresente sua representação em bytes e bits.
Agora é com você
Resultado:
1. Solicite uma mensagem;
2. Converta cada caractere em seu código;
3. Converta cada código para binário;
4. Mostre os resultados no terminal;
5. Informe a quantidade de caracteres;
6. Informe a quantidade de bytes;
7. Informe a quantidade total de bits.
'''

mensagem = input("Digite uma mensagem: ")

print("\nRepresentação da mensagem:")
for caractere in mensagem:
    codigo = ord(caractere)
    binario = format(codigo, "08b")

    print(f"Caractere: '{caractere}' | Código: {codigo} | Binário: {binario}")

quantidade_caracteres = len(mensagem)
quantidade_bytes = len(mensagem.encode("utf-8"))
quantidade_bits = quantidade_bytes * 8

print("\n--- Resultado ---")
print(f"Quantidade de caracteres: {quantidade_caracteres}")
print(f"Quantidade de bytes: {quantidade_bytes}")
print(f"Quantidade de bits: {quantidade_bits}")


