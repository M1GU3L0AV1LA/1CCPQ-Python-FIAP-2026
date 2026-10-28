# Tutorial de Implementação - Arvóres Gerais

# Questões iniciais a ser respondidas:
# 1. Diferença entre nó e raiz?
    # O nó é qualquer elemento da árvore que armazena um valor e pode ter filhos. Já a raiz é o nó principal do qual acessamos todos os outros nós, localizado no início da árvore.
# 2. Significado de no.esquerda e no.direita?
    # São atributos que armazenam os filhos do nó, sendo no.esquerda o filho à esquerda normalmente com os valores menores. Já no.direita é o filho à direita normalmente com os valores maiores. Em árvores gerais, podemos ter mais de dois filhos, então esses atributos podem ser adaptados para armazenar uma lista de filhos.
# 3. Por que uma função recursiva recebe um nó?
    # Uma função recursiva recebe um nó para poder processar a árvore de forma hierárquica, permitindo que a função chame a si mesma para cada filho do nó, percorrendo toda a estrutura da árvore.
# 4. Como um percurso visita todos os nós?
    # Um percurso visita todos os nós da árvore seguindo uma ordem específica, como pré-ordem, em-ordem ou pós-ordem. A função recursiva percorre cada nó e seus filhos, garantindo que todos os elementos sejam visitados.
# 5. O que mudar para permitir cinco filhos?
    # Para permitir cinco filhos, podemos modificar a estrutura do nó para armazenar uma lista de filhos em vez de apenas dois atributos (esquerda e direita). A função recursiva também precisaria ser ajustada para iterar sobre essa lista de filhos, chamando a si mesma para cada filho.

# Questões do Tutorial:
# 1. Por que não definir antes quantos filhos o nó terá?
    # Porque a lista cresce dinamicamente com append; cada nó tem sua própria lista, que começa vazia.
# 2. Por que o algoritmo continua recursivo mesmo usando for?
    # Porque a recursão está na chamada self.pre_ordem(filho). O for só repete essa chamada para cada filho; o caso base (no is None) encerra a descida.
# 3. Por que não usamos valor < no.dado na busca?
    # Porque a árvore geral não tem regra de ordenação; não dá para descartar nenhum ramo, então pode ser preciso visitar todos.
# 4. E se o elemento estiver no último ramo?
    # Todos os ramos anteriores são visitados antes de encontrá-lo.
# 5. Complexidade no pior caso: 
    # O(n) com dados repetidos, a busca retorna o primeiro encontrado na ordem do percurso.
# 6. Por que total começa com 1 em contar_nos?
    # Porque conta o próprio nó atual; depois soma as subárvores dos filhos.
# 7. Diferença na verificação de folhas:
    # Na binária: esquerda is None and direita is None. Na geral: len(no.filhos) == 0, uma única condição para qualquer número de filhos.

class NoGeral:
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)


class ArvoreGeral:
    def __init__(self):
        self.raiz = None

    def criar_raiz(self, dado):
        if self.raiz is not None:
            raise ValueError("A árvore já possui uma raiz.")
        self.raiz = NoGeral(dado)
        return self.raiz

    def inserir(self, pai, dado):
        if pai is None:
            raise ValueError("O nó pai não foi informado.")
        novo = NoGeral(dado)
        pai.adicionar_filho(novo)
        return novo

    def pre_ordem(self, no):
        if no is None:
            return
        print(no.dado)
        for filho in no.filhos:
            self.pre_ordem(filho)

    def mostrar(self, no, nivel=0):
        if no is None:
            return
        print(" " * nivel + str(no.dado))
        for filho in no.filhos:
            self.mostrar(filho, nivel + 1)

    def buscar(self, no, valor):
        if no is None:
            return None
        if no.dado == valor:
            return no
        for filho in no.filhos:
            encontrado = self.buscar(filho, valor)
            if encontrado is not None:
                return encontrado
        return None

    def contar_nos(self,no):
        if no is None:
            return 0
        total = 1
        for filho in no.filhos:
            total += self.contar_nos(filho)
        return total

    def altura(self, no):
        if no is None:
            return 0 
        maior_altura = 0
        for filho in no.filhos:
            altura_filho = self.altura(filho)
            if altura_filho > maior_altura:
                maior_altura = altura_filho
        return 1 + maior_altura

    def listar_folhas(self, no):
        if no is None:
            return
        if len(no.filhos) == 0:
            print(no.dado)
            return
        for filho in no.filhos:
            self.listar_folhas(filho)

    def inserir_por_valor(self, valor_pai, dado):
        pai = self.buscar(self.raiz, valor_pai)
        if pai is None:
            return None
        return self.inserir(pai, dado)

# DESAFIO
    def contar_folhas(self, no):
        if no is None:
            return 0 
        if len(no.filhos) == 0:
            return 1 
        total = 0
        for filho in no.filhos:
            total += self.contar_folhas(filho)
        return total

    def grau_arvore(self, no):
        if no is None:
            return 0
        maior = len(no.filhos)
        for filho in no.filhos:
            grau_filho = self.grau_arvore(filho)
            if grau_filho > maior:
                maior = grau_filho
        return maior

# TESTE DO NÓ
raiz = NoGeral("A")
raiz.adicionar_filho(NoGeral("B"))
raiz.adicionar_filho(NoGeral("C"))
raiz.adicionar_filho(NoGeral("D"))
print(len(raiz.filhos))  # 3

# Árvore de Exemplo
arvore = ArvoreGeral()
instituicao = arvore.criar_raiz("Instituição")
graduacao = arvore.inserir(instituicao, "Graduação")
pos = arvore.inserir(instituicao, "Pós-graduação")
arvore.inserir(graduacao, "Ciência da Computação")
arvore.inserir(graduacao, "Sistemas de Informação")
arvore.inserir(pos, "Mestrado")
 
print("\nPRÉ-ORDEM:")
arvore.pre_ordem(arvore.raiz)
 
print("\nHIERARQUIA:")
arvore.mostrar(arvore.raiz)
 
print("\nTOTAL:", arvore.contar_nos(arvore.raiz))   # 6
print("ALTURA:", arvore.altura(arvore.raiz))         # 3
 
arvore.inserir_por_valor("Graduação", "Engenharia de Software")
 
print("\nHIERARQUIA (após inserir_por_valor):")
arvore.mostrar(arvore.raiz)
 
print("\nFOLHAS:")
arvore.listar_folhas(arvore.raiz)
 
resultado = arvore.buscar(arvore.raiz, "Mestrado")
print("\nBUSCA:", resultado.dado if resultado else "Não encontrado")

# TESTE DE VALIDAÇÃo
assert arvore.contar_nos(arvore.raiz) == 7
assert arvore.altura(arvore.raiz) == 3
assert len(arvore.raiz.filhos) == 2
assert len(arvore.buscar(arvore.raiz, "Graduação").filhos) == 3
assert arvore.buscar(arvore.raiz, "Mestrado") is not None
assert arvore.buscar(arvore.raiz, "Doutorado") is None
assert arvore.contar_folhas(arvore.raiz) == 4
 
vazia = ArvoreGeral() # árvore vazia
assert vazia.contar_nos(vazia.raiz) == 0
assert vazia.altura(vazia.raiz) == 0
assert vazia.contar_folhas(vazia.raiz) == 0
assert vazia.buscar(vazia.raiz, "X") is None
 
so_raiz = ArvoreGeral() # árvore só com a raiz
so_raiz.criar_raiz("X")
assert so_raiz.contar_nos(so_raiz.raiz) == 1
assert so_raiz.altura(so_raiz.raiz) == 1
assert so_raiz.contar_folhas(so_raiz.raiz) == 1
 
assert arvore.inserir_por_valor("Inexistente", "Y") is None # pai inexistente: retorna None e não altera a árvore
assert arvore.contar_nos(arvore.raiz) == 7
 
print("\nTodos os testes de validação passaram.")
 

# DESAFIO: ESTRUTURA ACÂDEMICA COMPLETA 
ampliada = ArvoreGeral()
ampliada.criar_raiz("Instituição")
ampliada.inserir_por_valor("Instituição", "Graduação")
ampliada.inserir_por_valor("Instituição", "Pós-graduação")
ampliada.inserir_por_valor("Instituição", "Administração")
ampliada.inserir_por_valor("Graduação", "Ciência da Computação")
ampliada.inserir_por_valor("Graduação", "Sistemas de Informação")
ampliada.inserir_por_valor("Graduação", "Engenharia de Software")
ampliada.inserir_por_valor("Pós-graduação", "Especialização")
ampliada.inserir_por_valor("Pós-graduação", "Mestrado")
ampliada.inserir_por_valor("Administração", "Secretaria")
ampliada.inserir_por_valor("Administração", "Biblioteca")
 
print("\nESTRUTURA AMPLIADA:")
ampliada.mostrar(ampliada.raiz)
 
print("\nNós:", ampliada.contar_nos(ampliada.raiz))        # 11
print("Altura:", ampliada.altura(ampliada.raiz))            # 3
print("Folhas:", ampliada.contar_folhas(ampliada.raiz))     # 7
print("Grau:", ampliada.grau_arvore(ampliada.raiz))         # 3
 
assert ampliada.contar_nos(ampliada.raiz) == 11
assert ampliada.altura(ampliada.raiz) == 3
assert ampliada.contar_folhas(ampliada.raiz) == 7
assert ampliada.grau_arvore(ampliada.raiz) == 3
 


    






