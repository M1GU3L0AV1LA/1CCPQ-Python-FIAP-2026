'''byte = 42

print("Decimal:", byte)
print("Binário:", "{:08b}".format(byte,))'''

# Tabela ASCII

letra = "A"

codigo = ord(letra)
print("Letra:", letra)
print("Codigo ASCII:", codigo)
print("Binário:", "{:08b}".format(codigo))
print("Hexadecimal:", hex(codigo))

print( )

# Analisar uma palavra

texto = "CASA"
for letra in texto:
    codigo = ord(letra)

    print(
        letra,
        "->",
        codigo,
        "->",
        "{:08b}".format(codigo,)
    )

#
