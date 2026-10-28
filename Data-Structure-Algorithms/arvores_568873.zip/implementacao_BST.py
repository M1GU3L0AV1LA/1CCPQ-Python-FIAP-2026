# Implementação de BST (Árvore Binária de Busca) - gerenciador de valores com menu de terminal
 
# RESPOSTAS DAS QUESTÕES
# 1. Por que o percurso em ordem produz valores ordenados?
    # Porque em toda BST a subárvore esquerda tem valores menores que o nó e a direita, maiores. O percurso em ordem visita esquerda -> nó -> direita,
# então, em cada nó, todos os menores saem antes dele e todos os maiores depois. Aplicado recursivamente em toda a árvore, o resultado é crescente.
# 2. Por que o mínimo não precisa ser uma folha?
    # Porque a condição de parada é apenas não existir filho à esquerda. O nó mínimo pode ter um filho à direita (maior que ele, mas ainda menor que o
# pai), então não é necessariamente folha. O mesmo vale para o máximo.
# 3. Pior formato possível de uma BST?
    # A árvore degenerada: uma cadeia, que ocorre ao inserir valores já ordenados (ex.: 10, 20, 30, 40, 50). A altura vira n e busca, inserção
# e remoção passam a ser O(n), como em uma lista encadeada.
# 4. Por que a remoção com dois filhos usa o mínimo da subárvore direita?
    # Porque esse valor (o sucessor em ordem) é maior que todos os da subárvore esquerda e menor que todos os demais da direita. Ao colocá-lo
# no lugar do nó removido, a propriedade da BST continua valendo. Além disso, ele tem no máximo um filho (direito), então sua remoção cai nos casos simples.
 
class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
 
class BST:
    def __init__(self):
        self.raiz = None
 
    def inserir(self, dado):
        novo = No(dado)
        if self.raiz is None:
            self.raiz = novo
            return
        atual = self.raiz
        while True:
            if dado < atual.dado:
                if atual.esquerda is None:
                    atual.esquerda = novo
                    return
                atual = atual.esquerda
            elif dado > atual.dado:
                if atual.direita is None:
                    atual.direita = novo
                    return
                atual = atual.direita
            else:
                return  # valor duplicado: não inserir
 
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
 
    def minimo(self, no=None):
        atual = self.raiz if no is None else no
        if atual is None:
            return None
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.dado
 
    def maximo(self, no=None):
        atual = self.raiz if no is None else no
        if atual is None:
            return None
        while atual.direita is not None:
            atual = atual.direita
        return atual.dado
 
    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.dado, end=" ")
            self.em_ordem(no.direita)
 
    def pre_ordem(self, no):
        if no is not None:
            print(no.dado, end=" ")
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)
 
    def pos_ordem(self, no):
        if no is not None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.dado, end=" ")
 
    def remover(self, no, dado):
        if no is None:
            return None
        if dado < no.dado:
            no.esquerda = self.remover(no.esquerda, dado)
        elif dado > no.dado:
            no.direita = self.remover(no.direita, dado)
        else:
            # Casos 1 e 2: folha ou um filho
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            # Caso 3: dois filhos (sucessor = mínimo da subárvore direita)
            sucessor = no.direita
            while sucessor.esquerda is not None:
                sucessor = sucessor.esquerda
            no.dado = sucessor.dado
            no.direita = self.remover(no.direita, sucessor.dado)
        return no
 
    def excluir(self, dado):
        self.raiz = self.remover(self.raiz, dado)
 
# TESTES
def teste_obrigatorio():
    arvore = BST()
    valores = [61, 43, 77, 16, 55, 69, 85, 11, 31, 49, 59, 65, 73, 81, 89]
    for valor in valores:
        arvore.inserir(valor)
 
    print("1. Em ordem:")
    arvore.em_ordem(arvore.raiz)
    print("\n2. Buscar 73:", arvore.buscar(73))
    print("3. Buscar 100:", arvore.buscar(100))
    print("4. Mínimo:", arvore.minimo(), "| Máximo:", arvore.maximo())
 
    arvore.excluir(31)  # folha
    print("5. Removido 31 (folha). Em ordem:")
    arvore.em_ordem(arvore.raiz)
 
    arvore.excluir(16)  # um filho (11), após remover 31
    print("\n6. Removido 16 (um filho). Em ordem:")
    arvore.em_ordem(arvore.raiz)
 
    arvore.excluir(77)  # dois filhos
    print("\n7. Removido 77 (dois filhos). Em ordem:")
    arvore.em_ordem(arvore.raiz)
 
    print("\n8. Em ordem final:")
    arvore.em_ordem(arvore.raiz)
    print("\n")
 
# MENU
def ler_inteiro(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
        return None
 
 
def menu():
    arvore = BST()  # começa vazia
    while True:
        print("\n1 - Inserir valor")
        print("2 - Buscar valor")
        print("3 - Mostrar em ordem")
        print("4 - Mostrar menor valor")
        print("5 - Mostrar maior valor")
        print("6 - Remover valor")
        print("7 - Encerrar")
        opcao = input("Escolha: ").strip()
 
        if opcao == "1":
            valor = ler_inteiro("Valor a inserir: ")
            if valor is not None:
                arvore.inserir(valor)
                print("Valor processado.")
        elif opcao == "2":
            valor = ler_inteiro("Valor a buscar: ")
            if valor is not None:
                print("Encontrado." if arvore.buscar(valor) else "Não encontrado.")
        elif opcao == "3":
            if arvore.raiz is None:
                print("Árvore vazia.")
            else:
                arvore.em_ordem(arvore.raiz)
                print()
        elif opcao == "4":
            menor = arvore.minimo()
            print("Árvore vazia." if menor is None else f"Menor valor: {menor}")
        elif opcao == "5":
            maior = arvore.maximo()
            print("Árvore vazia." if maior is None else f"Maior valor: {maior}")
        elif opcao == "6":
            valor = ler_inteiro("Valor a remover: ")
            if valor is not None:
                if arvore.buscar(valor):
                    arvore.excluir(valor)
                    print("Valor removido.")
                else:
                    print("Valor não encontrado.")
        elif opcao == "7":
            print("Encerrando.")
            break
        else:
            print("Opção inválida.")
 
 
if __name__ == "__main__":
    teste_obrigatorio()
    menu()