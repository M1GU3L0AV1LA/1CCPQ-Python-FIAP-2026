# Bubble Sort
from encodings.punycode import insertion_sort


def bubble_sort(lista):
    comparacoes = 0
    trocas = 0

    n = len(lista)

    for i in range(n):
        for j in range(n - 1 - i):
            comparacoes += 1

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1

    return lista, comparacoes, trocas
# -------------------------------------------------------------------

# Selection Sort
def selection_sort(lista):
    comparacoes = 0
    trocas = 0

    n = len(lista)

    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            comparacoes += 1

            if lista[j] < lista[menor]:
                menor = j

        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1

    return lista, comparacoes, trocas
# --------------------------------------------------------------------

# Insertion Sort
def insertion_sort(lista):
    comparacoes = 0
    trocas = 0

    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1

            if lista[j] > atual:
                lista[j + 1] = lista[j]
                trocas += 1
                j -= 1
            else:
                break

        lista[j + 1] = atual

    return lista, comparacoes, trocas
# ---------------------------------------------------------------------

numeros = [38, 12, 45, 7, 29, 18, 41, 3, 25, 10]

print("Atividade Prática - Comparando os algoritmos: ")
print()

#Bubble Sort
resultado_bubble = bubble_sort(numeros.copy())
print("Bubble sort: ")
print("Lista: ", resultado_bubble[0])
print("Comparações: ", resultado_bubble[1])
print("Trocas: ", resultado_bubble[2])
print()

# Selection Sort
resultado_selection = selection_sort(numeros.copy())
print("Selection sort: ")
print("Lista: ", resultado_selection[0])
print("Comparações: ", resultado_selection[1])
print("Trocas: ", resultado_selection[2])
print()

# Insertion Sort
resultado_insertion = insertion_sort(numeros.copy())
print("Insertion sort: ")
print("Lista: ", resultado_insertion[0])
print("Comparações: ", resultado_insertion[1])
print("Trocas: ", resultado_insertion[2])
print()