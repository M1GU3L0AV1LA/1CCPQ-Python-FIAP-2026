# Sprint 01: 6 entradas, 4 saídas
#   S1 = A AND B AND C AND D AND E AND F
#   S2 = (A') OR (F')
#   S3 = (B') OR (E')
#   S4 = S2 OR S3
# ============================================================

def ler_entrada(nome, descricao):
    """Lê uma entrada do usuário e valida como 0 ou 1."""
    while True:
        valor = input(f"  {nome} – {descricao} (0 ou 1): ").strip()
        if valor in ("0", "1"):
            return int(valor)
        print("  ⚠ Entrada inválida. Digite 0 ou 1.")

def calcular_saidas(A, B, C, D, E, F):
    """Calcula as 4 saídas com base nas 6 entradas booleanas."""

    # S1: Recarga ligada
    S1 = A and B and C and D and E and F

    # S2: Alerta de erro
    S2 = (not A) or (not F)

    # S3: Modo espera
    S3 = (not B) or (not E)

    # S4: Notificação no app
    S4 = S2 or S3

    return int(S1), int(S2), int(S3), int(S4)

def exibir_resultado(S1, S2, S3, S4):
    """Exibe o estado de cada saída com descrição do sistema."""
    print("\n" + "=" * 50)
    print("  RESULTADO DO SISTEMA WECHARGE")
    print("=" * 50)

    # S1 – Recarga Ligada
    if S1:
        print("  S1 – Recarga LIGADA: carregamento iniciado com sucesso.")
    else:
        print("  S1 – Recarga DESLIGADA: condições não atendidas.")

    # S2 – Alerta de Erro
    if S2:
        print("  S2 – ALERTA DE ERRO: verifique autenticação ou pagamento.")
    else:
        print("  S2 – SEM alerta de erro: acesso e pagamento OK.")

    # S3 – Modo Espera
    if S3:
        print("  S3 – MODO ESPERA: conector desconectado ou temperatura alta.")
    else:
        print("  S3 – Hardware pronto: conector encaixado e temperatura segura.")

    # S4 – Notificação no App
    if S4:
        print("  S4 – NOTIFICAÇÃO ENVIADA: atenção necessária no app.")
    else:
        print("  S4 – Sem notificações: sistema operando normalmente.")

    print("=" * 50)
    print(f"  Valores binários → S1={S1}  S2={S2}  S3={S3}  S4={S4}")
    print("=" * 50 + "\n")

# ============================================================

print("\n" + "=" * 50)
print("  WECHARGE – SIMULAÇÃO DO CIRCUITO LÓGICO")
print("  Sprint 02 | FIAP | Turma 1CCPQ | Equipe 04")
print("=" * 50)

while True:
    print("\nInsira os valores das entradas (0 = FALSO, 1 = VERDADEIRO):\n")

    # Leitura das 6 entradas
    A = ler_entrada("A", "Usuário autenticado")
    B = ler_entrada("B", "Conector encaixado")
    C = ler_entrada("C", "Estação disponível")
    D = ler_entrada("D", "Bateria baixa (necessita recarga)")
    E = ler_entrada("E", "Temperatura segura")
    F = ler_entrada("F", "Pagamento aprovado")

    # Cálculo das saídas
    S1, S2, S3, S4 = calcular_saidas(A, B, C, D, E, F)

    # Exibição dos resultados
    exibir_resultado(S1, S2, S3, S4)

    # Pergunta se deseja simular novamente
    continuar = input("Simular novamente? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nEncerrando simulação WeCharge. Até logo!\n")
        break