t = ('a', 'b', 'c', 'd', 'e')
print(t)

t = ('a',)
print(t)

t = tuple("fiap")
print(t)
print(t[1:3])

t = ('F',) +t[1:]
print(t)

# Atribuição com Tuples
a = 5
b = 10
print(f"a: {a}, b: {b}")

temp = a
a = b
b = temp
print(f"a: {a}, b: {b}")

a, b = b, a
print(f"a: {a}, b: {b}")

email = "fulano@gmail.com"
usuario, dominio = email.split("@")
print(usuario)
print(dominio)
