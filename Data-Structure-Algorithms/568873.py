'''n = 24
def reduzir(n):
    print(n)
    if n <= 1:
        return
    reduzir(n // 2)

reduzir(n)
'''

'''
n = 24
def reduzir2(n):
    print(n)
    if n <= 1:
        return
    reduzir2(n // 2)
    reduzir2(n // 2)

reduzir2(n)
'''
'''
V = [9, 2, 7, 1, 8, 3, 6, 4]

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    return merge_sort(esquerda,direita)

print(merge_sort(V))'''

V = [9, 2, 7, 1]
def merge(esquerda, direita):
    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

merge(V)
