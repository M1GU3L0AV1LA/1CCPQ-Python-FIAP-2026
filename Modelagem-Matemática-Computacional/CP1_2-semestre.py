def dimensoes(M):
    n_linhas = len(M)
    n_colunas = len(M[0]) if n_linhas > 0 else 0
    return n_linhas, n_colunas

def criar_matriz_zeros(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def soma_matrizes(A, B):
    lA, cA = dimensoes(A)
    lB, cB = dimensoes(B)

    if lA != lB or cA != cB:
        raise ValueError("Para somar, as matrizes precisam ter a mesma dimensao.")

    resultado = criar_matriz_zeros(lA, cA)

    for i in range(lA):          # percorre cada linha
        for j in range(cA):      # percorre cada coluna
            resultado[i][j] = A[i][j] + B[i][j]

    return resultado

def multiplica_matrizes(A, B, verbose=False):
    lA, cA = dimensoes(A)
    lB, cB = dimensoes(B)

    if cA != lB:
        raise ValueError(
            f"Nao e possivel multiplicar: A e {lA}x{cA} e B e {lB}x{cB} "
            f"(colunas de A devem ser iguais as linhas de B)."
        )

    # matriz resultado tem dimensao (linhas de A) x (colunas de B)
    resultado = criar_matriz_zeros(lA, cB)

    for i in range(lA):              # para cada linha de A
        for j in range(cB):          # para cada coluna de B
            soma = 0
            passo_a_passo = []
            for k in range(cA):      # percorre a "linha de A" e a "coluna de B" juntas
                termo = A[i][k] * B[k][j]
                soma = soma + termo
                passo_a_passo.append(f"A[{i}][{k}]*B[{k}][{j}] = {A[i][k]}*{B[k][j]} = {termo}")
            resultado[i][j] = soma

            if verbose:
                print(f"C[{i}][{j}] = " + " + ".join(
                    [p.split(' = ')[-1] for p in passo_a_passo]
                ) + f" = {soma}")
                for p in passo_a_passo:
                    print("    " + p)

    return resultado

def imprime_matriz(M, nome="Resultado"):
    print(f"\n{nome} =")
    for linha in M:
        print("  [" + "  ".join(f"{v:>4}" for v in linha) + "]")

# ============================================================
# f)
print("=" * 60)
print("Exercicio f)")
print("=" * 60)

f_coluna = [[1], [-6], [2]]        # matriz 3x1
f_linha = [[3, 2, 1]]              # matriz 1x3

resultado_f = multiplica_matrizes(f_coluna, f_linha, verbose=True)
imprime_matriz(resultado_f, "Resultado f")

# ============================================================
# g)
print("\n" + "=" * 60)
print("Exercicio g)")
print("=" * 60)

g_A = [
    [2, -1, 0],
    [1,  0, 3],
]

g_B = [
    [1, -4,  0,  1],
    [2, -1,  3, -1],
    [4,  0, -2,  0],
]

resultado_g = multiplica_matrizes(g_A, g_B, verbose=True)
imprime_matriz(resultado_g, "Resultado g")

# ============================================================
# h)
print("\n" + "=" * 60)
print("Exercicio h)")
print("=" * 60)

h_A = [
    [2, -1, 0, 0],
    [1,  0, 0, 0],
    [0,  0, 1, 1],
    [0,  0, 1, 1],
]

h_B = [
    [2, -1, 0, 0],
    [1,  0, 0, 0],
    [0,  0, 1, 1],
    [0,  0, 1, 1],
]

resultado_h = multiplica_matrizes(h_A, h_B, verbose=True)
imprime_matriz(resultado_h, "Resultado h")