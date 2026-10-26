# Tutorial de Implementação - Arvóres Gerais

# Questões a ser respondidas:
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


class No:
 def __init__(self, dado):
 self.dado = dado
 self.esquerda = None
 self.direita = None

 class NoGeral:
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

    def adicionar_filos(self, filho):
        self.filhos.append(filho)

raiz = NoGeral("A")
print(len(raiz.filhos))  # 3

class ArvoreGeral:
    def__init__(self):
        self.raiz = None

    def criar_raiz(self,dado):
        if self.raiz is not None:
            raise ValueError("A árvore já possui uma raiz.")
        self.raiz = NoGeral(dado)
        return self.raiz

def inserir(self, pai, dado):
    if pai is None:
        raise ValueError("O nó pai não pode ser None.")
    novo = NoGeral(dado)
    pai.adicionar_filos(novo)
    return novo

arvore = ArvoreGeral()
instituicao = arvore.criar_raiz("Instituição")
graduacao = arvore.inserir(instiuicao, "Pós-Graduação")

 def pre_ordem(self, no):
    if no is None:
        return
    print(no.dado)
    for filho in no.filhos:
        self.pre_ordem(filho)
