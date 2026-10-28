# Evoluindo uma BST para uma Árvore AVL (inserção autobalanceada)
from bst import BST

class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
        self.altura = 1  # folha tem altura 1; subárvore vazia, 0

class AVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if no is None:
            return 0
        return no.altura 

    def atualizar_altura(self, no):
        altura_esquerda = self.altura(no.esquerda)
        altura_direita = self.altura(no.direita)
        no.altura = 1 + max(altura_esquerda, altura_direita)

    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, y):
        x = y.esquerda
        temp = x.direita
        x.direita = y
        y.esquerda = temp
        self.atualizar_altura(y)  # primeiro o nó que desceu
        self.atualizar_altura(x)  # depois o novo topo
        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        temp = y.esquerda
        y.esquerda = x
        x.direita = temp
        self.atualizar_altura(x)
        self.atualizar_altura(y)
        return y

    def inserir_recursivo(self, no, dado):
        if no is None:
            return No(dado)
        if dado < no.dado:
            no.esquerda = self.inserir_recursivo(no.esquerda, dado)
        elif dado > no.dado:
            no.direita = self.inserir_recursivo(no.direita, dado)
        else:
            return no  

        self.atualizar_altura(no)
        fb = self.fator_balanceamento(no)


        if fb > 1 and dado < no.esquerda.dado:
            return self.rotacao_direita(no)
  
        if fb < -1 and dado > no.direita.dado:
            return self.rotacao_esquerda(no)
     
        if fb > 1 and dado > no.esquerda.dado:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)
  
        if fb < -1 and dado < no.direita.dado:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def inserir(self, dado):
        self.raiz = self.inserir_recursivo(self.raiz, dado)

    def buscar(self, dado):
        atual = self.raiz
        while atual is not None:
            if dado == atual.dado:
                return True
            if dado < atual.dado:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return False

    def minimo(self):
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.dado

    def maximo(self):
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.dado

    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.dado, end=" ")
            self.em_ordem(no.direita)

    def lista_em_ordem(self, no):
        if no is None:
            return []
        return self.lista_em_ordem(no.esquerda) + [no.dado] + self.lista_em_ordem(no.direita)

    def mostrar(self, no, nivel=0):
        if no is None:
            return
        self.mostrar(no.direita, nivel + 1)
        print(
            "    " * nivel + str(no.dado)
            + f" (h={no.altura}, FB={self.fator_balanceamento(no)})"
        )
        self.mostrar(no.esquerda, nivel + 1)

    def verificar_balanceamento(self, no):
        if no is None:
            return True
        fb = self.fator_balanceamento(no)
        if abs(fb) > 1:
            return False
        return (
            self.verificar_balanceamento(no.esquerda)
            and self.verificar_balanceamento(no.direita)
        )

# AUXILIAR
def verificar(descricao, condicao):
    if condicao:
        print("OK:   " + descricao)
    else:
        print("ERRO: " + descricao)

def altura_bst(no):
    if no is None:
        return 0
    return 1 + max(altura_bst(no.esquerda), altura_bst(no.direita))

def contar_visitas(raiz, dado):
    visitas = 0
    atual = raiz
    while atual is not None:
        visitas += 1
        if dado == atual.dado:
            break
        if dado < atual.dado:
            atual = atual.esquerda
        else:
            atual = atual.direita
    return visitas

# TESTES
casos = [
    ("LL", [30, 20, 10]),
    ("RR", [10, 20, 30]),
    ("LR", [30, 10, 20]),
    ("RL", [10, 30, 20]),
]

for nome, sequencia in casos:
    arvore = AVL()  # árvore vazia para cada teste
    for valor in sequencia:
        arvore.inserir(valor)
    print(f"\nCaso {nome}: inserindo {sequencia}")
    arvore.mostrar(arvore.raiz)
    verificar(f"{nome}: raiz = 20", arvore.raiz.dado == 20)
    verificar(f"{nome}: em ordem = 10 20 30",
              arvore.lista_em_ordem(arvore.raiz) == [10, 20, 30])
    verificar(f"{nome}: árvore balanceada", arvore.verificar_balanceamento(arvore.raiz))

# SEQUÊNCIA MAIOR
arvore = AVL()
for valor in [10, 20, 30, 40, 50, 25]:
    arvore.inserir(valor)

print("\nInserindo 10, 20, 30, 40, 50, 25:")
arvore.mostrar(arvore.raiz)
print("Em ordem:", end=" ")
arvore.em_ordem(arvore.raiz)
print()
verificar("raiz = 30", arvore.raiz.dado == 30)
verificar("altura total = 3", arvore.altura(arvore.raiz) == 3)
verificar("em ordem = 10 20 25 30 40 50",
          arvore.lista_em_ordem(arvore.raiz) == [10, 20, 25, 30, 40, 50])
verificar("árvore balanceada", arvore.verificar_balanceamento(arvore.raiz))

# BST x AVL
valores = list(range(1, 101))
bst = BST()
avl = AVL()
for valor in valores:
    bst.inserir(valor)
    avl.inserir(valor)

print("\nCOMPARAÇÃO com os valores de 1 a 100:")
print("Altura da BST:", altura_bst(bst.raiz))
print("Altura da AVL:", avl.altura(avl.raiz))
print("Nós visitados ao buscar 100 na BST:", contar_visitas(bst.raiz, 100))
print("Nós visitados ao buscar 100 na AVL:", contar_visitas(avl.raiz, 100))
verificar("AVL com 1..100 está balanceada", avl.verificar_balanceamento(avl.raiz))
verificar("AVL com 1..100 mantém a ordem",
          avl.lista_em_ordem(avl.raiz) == valores)

# QUESTÕES A SER RESPONDIDAS:
# 1. A ordenação mudou? 
    # Não: o percurso em ordem continua crescente.
# 2. Os dados mudaram? 
    # Não: os mesmos valores estão na árvore.
# 3. Mudou apenas a organização das referências (quem aponta para quem).
    # A busca custa O(h), pois a cada comparação descemos um nível. Como a AVL mantém FB em {-1, 0, +1} em todos os nós, sua altura fica limitada a
# aproximadamente 1,44 * log2(n), ou seja, h = O(log n). Logo, a busca na AVL é O(log n), enquanto na BST degenerada pode chegar a O(n).