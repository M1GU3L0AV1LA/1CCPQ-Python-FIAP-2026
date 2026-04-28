#--------------------------------------------------
# ESTRUTURA CONDICIONAL SIMPLES
#--------------------------------------------------

# nota_final = 4.0
#
# if nota_final < 6:
#     print("Reprovado")
#
# print("FIM")

# --------------------------------------------------
# ESTRUTURA CONDICIONAL COMPOSTA
# --------------------------------------------------

# nota_final = 8.0
#
# if nota_final < 6:
#     print("Reprovado")
#
# else:
#     print("Aprovado")
#
# print("FIM")

# --------------------------------------------------
# ESTRUTURA CONDICIONAL ENCADEADA
# --------------------------------------------------

# nota_final = 9.0
#
# if nota_final <4:
#     print("Reprovado")
# else:
#     if nota_final < 6:
#         print("Recuperação")
#     else:
#         print("Aprovado")
#
# print("FIM")

# --------------------------------------------------
# ESTRUTURA CONDICIONAL ENCADEADA (ELIF)
# --------------------------------------------------

nota_final = 9.0

if nota_final <4:
    print("Reprovado")
elif  nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("FIM")