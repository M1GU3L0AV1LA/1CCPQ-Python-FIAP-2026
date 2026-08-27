# Microchallenge: Metodos basicos de ordenacao

import random
 
def bubble_sort(lista):
    trocas = 0
 
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
 
    return lista, trocas
 
 
def selection_sort(lista):
    trocas = 0
 
    for i in range(len(lista) - 1):
        menor = i
 
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
 
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1
 
    return lista, trocas
 
 
def insertion_sort(lista):
    trocas = 0
 
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
 
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1
            trocas += 1
 
        lista[j + 1] = atual
 
    return lista, trocas
 
 
# Sorteia um vetor aleatório com 200 elementos
numeros = [random.randint(1, 1000) for _ in range(200)]
 
# Faz uma cópia do mesmo vetor para cada método
numeros_bubble = numeros.copy()
numeros_selection = numeros.copy()
numeros_insertion = numeros.copy()
 
 
print("Vetor original:")
print(numeros)
 
print("\nbubble_sort:")
resultado, trocas = bubble_sort(numeros_bubble)
print(resultado)
print("Trocas:", trocas)
 
print("\nselection_sort:")
resultado, trocas = selection_sort(numeros_selection)
print(resultado)
print("Trocas:", trocas)
 
print("\ninsertion_sort:")
resultado, trocas = insertion_sort(numeros_insertion)
print(resultado)
print("Trocas:", trocas)