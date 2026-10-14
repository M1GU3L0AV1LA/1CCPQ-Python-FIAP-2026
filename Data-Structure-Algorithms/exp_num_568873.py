# Calculadora de Expressões Matemáticas com Árvore de Expressão
# Aluno: Miguel Avila   RM:568873
# Turma: 1CCPQ   Equipe: 04

OPERADORES = "+-*/"

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def tokenizar(expressao):
    tokens = []
    numero = ''

    for c in expressao:
        if c in "0123456789" or c == '.':
            numero += c
        else:
            if numero:
                tokens.append(numero)
                numero = ''
            if c in OPERADORES or c in "()":
                tokens.append(c)
            elif not c.isspace():
                raise ValueError(f"Caractere não aceito: '{c}'")

    if numero:
        tokens.append(numero)

    if not tokens:
        raise ValueError("Expressão incorreta.")

    for t in tokens:
        if t not in OPERADORES and t not in "()":
            try:
                float(t)
            except ValueError:
                raise ValueError(f"Número inválido: '{t}'")

    return tokens

def precedencia(operador):
    if operador in "*/":
        return 2
    if operador in "+-":
        return 1
    return 0

def para_posfixa(tokens):
    saida = []
    pilha = []

    for t in tokens:
        if t in OPERADORES:
            while pilha and pilha[-1] in OPERADORES and \
                    precedencia(pilha[-1]) >= precedencia(t):
                saida.append(pilha.pop())
            pilha.append(t)
        elif t == '(':
            pilha.append(t)
        elif t == ')':
            while pilha and pilha[-1] != '(':
                saida.append(pilha.pop())
            if not pilha:
                raise ValueError("Parênteses incompatíveis: ')' sem '(' correspondente.")
            pilha.pop()  # descarta o '('
        else:
            saida.append(t)  # número vai direto para a saída

    while pilha:
        topo = pilha.pop()
        if topo == '(':
            raise ValueError("Parênteses incompatíveis: '(' sem ')' correspondente.")
        saida.append(topo)

    return saida


def construir_arvore(posfixa):
    pilha = []

    for t in posfixa:
        if t in OPERADORES:
            if len(pilha) < 2:
                raise ValueError("Expressão inválida: operador sem operandos suficientes.")
            direita = pilha.pop()
            esquerda = pilha.pop()
            no = No(t)
            no.esquerda = esquerda
            no.direita = direita
            pilha.append(no)
        else:
            pilha.append(No(t))

    if len(pilha) != 1:
        raise ValueError("Expressão inválida: operandos sem operador entre eles.")

    return pilha[0]


def pre_ordem(no):
    if no is None:
        return []
    return [no.valor] + pre_ordem(no.esquerda) + pre_ordem(no.direita)


def em_ordem(no):
    if no is None:
        return []
    return em_ordem(no.esquerda) + [no.valor] + em_ordem(no.direita)


def pos_ordem(no):
    if no is None:
        return []
    return pos_ordem(no.esquerda) + pos_ordem(no.direita) + [no.valor]


def gerar_expressao(no):
    if no.esquerda is None and no.direita is None:  # folha
        return str(no.valor)
    return "(" + gerar_expressao(no.esquerda) + " " + no.valor + " " + \
        gerar_expressao(no.direita) + ")"


def calcular(no):
    if no.esquerda is None and no.direita is None:  # folha: devolve o número
        return float(no.valor)

    esq = calcular(no.esquerda)
    dir_ = calcular(no.direita)

    if no.valor == '+':
        return esq + dir_
    if no.valor == '-':
        return esq - dir_
    if no.valor == '*':
        return esq * dir_
    if no.valor == '/':
        if dir_ == 0:
            raise ZeroDivisionError("Divisão por zero.")
        return esq / dir_

    raise ValueError(f"Operador desconhecido: '{no.valor}'")

def mostrar_arvore(no, nivel=0):
    if no is None:
        return
    mostrar_arvore(no.direita, nivel + 1)
    print("      " * nivel + str(no.valor))
    mostrar_arvore(no.esquerda, nivel + 1)


def formatar_numero(x):
    x = round(x, 10)
    if x == int(x):
        return str(int(x))  # 48.0 -> "48"
    return str(x)


def processar(expressao):
    tokens = tokenizar(expressao)               # Output
    posfixa = para_posfixa(tokens)
    raiz = construir_arvore(posfixa)
    resultado = calcular(raiz)

    print("\nTokens reconhecidos:")
    print(tokens)
    print("Pós-fixa:")
    print(" ".join(posfixa))
    print("Pré-ordem:")
    print(" ".join(pre_ordem(raiz)))
    print("Em ordem:")
    print(" ".join(em_ordem(raiz)))
    print("Pós-ordem:")
    print(" ".join(pos_ordem(raiz)))
    print("Expressão reconstruída:")
    print(gerar_expressao(raiz))
    print("Árvore (raiz à esquerda):")
    mostrar_arvore(raiz)
    print("Resultado:")
    print(formatar_numero(resultado))
    return resultado

# Validação
def executar_testes():
    print("TESTES OBRIGATÓRIOS")
    testes = [
        ("8 + 4 * 2", 16),
        ("(8 + 4) * 2", 24),
        ("((15 - 3) / 4) + (2 * 5)", 13),
        ("((20 / 5) + 3) * (9 - (2 + 1))", 42),
        ("12.5 + 2.5 * 4", 22.5),
    ]
    for i, (expr, esperado) in enumerate(testes, start=1):
        raiz = construir_arvore(para_posfixa(tokenizar(expr)))
        obtido = calcular(raiz)
        status = "OK" if abs(obtido - esperado) < 1e-9 else "FALHOU"
        print(f"Teste {i}: {expr:<35} esperado={esperado:<6} "
              f"obtido={formatar_numero(obtido):<6} [{status}]")

    print("\n")
    print("TESTES DE VALIDAÇÃO")
    invalidas = ["", "   ", "8 / (4 - 4)", "(8 + 4", "8 + 4)", "8 $ 2",
                 "8 + * 2", "(8 + 4) 2", "1.2.3 + 1", "()"]
    for expr in invalidas:
        try:
            raiz = construir_arvore(para_posfixa(tokenizar(expr)))
            calcular(raiz)
            print(f"'{expr}' -> [FALHOU] não gerou erro")
        except (ValueError, ZeroDivisionError) as e:
            print(f"'{expr}' -> [OK] {e}")
    print()

def main():
    executar_testes()
    print("Calculadora de expressões com árvore binária")
    while True:
        try:
            expr = input("\nDigite uma expressão (ou 'sair'): ")
        except EOFError:
            break
        if expr.strip().lower() == "sair":
            break
        try:
            processar(expr)
        except (ValueError, ZeroDivisionError) as e:
            print(f"Erro: {e}")
    print("Encerrado.")


if __name__ == "__main__":
    main()


'''
15. QUESTÕES DE ANÁLISE
1) Para o computador, a expressão é só uma sequência de caracteres. Sem a tokenização, "15" seria lido como '1' e '5' separados, 
e não haveria como distinguir números de vários algarismos. A tokenização agrupa os caracteres em unidades com significado (tokens), 
que é o que os algoritmos precisam receber. Também é nela que se detectam caracteres inválidos.

2) Porque a pilha é LIFO (o último a entrar é o primeiro a sair). Parênteses aninhados fecham na ordem inversa da abertura: o último '(' aberto é o
primeiro a ser fechado, que é o topo da pilha. Com operadores acontece algo parecido: o operador mais recente e pendente fica no topo, e é ele
que deve ser comparado em precedência com o operador que acabou de chegar.

3) Na pós-fixa os operandos aparecem antes do operador, na ordem original (esquerdo, depois direito). Como a pilha é LIFO, o último operando
empilhado (o direito) é o primeiro a sair. Em "10 6 -", o 6 foi empilhado por último; logo, o primeiro pop devolve o 6 (direita) e o segundo devolve
o 10 (esquerda). Inverter a ordem trocaria 10 - 6 por 6 - 10.

4) São a mesma sequência. A pós-ordem visita esquerda, depois direita e por último o nó (operador), que é exatamente a regra da notação pós-fixa: os 
operandos vêm antes do operador. Por isso a pós-ordem da árvore construída é idêntica à pós-fixa que serviu de entrada para construí-la.

5) O(n). A função calcular visita cada nó exatamente uma vez e, em cada nó, faz uma quantidade constante de trabalho (uma operação aritmética ou
devolver o valor da folha). Total: n visitas x trabalho constante = O(n).

6) A altura da árvore. As chamadas ficam empilhadas enquanto se desce por um caminho da raiz até uma folha, então o máximo simultâneo é a altura h
(quantidade de níveis). Em árvore balanceada, h ~ log n; no pior caso (árvore degenerada, como uma expressão muito encadeada à direita), h = n.
'''