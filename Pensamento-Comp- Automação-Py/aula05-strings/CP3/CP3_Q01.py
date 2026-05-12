'''Uma escola está testando um sistema simples de monitoramento ambiental para identificar salas com possível risco de calor excessivo.
Você recebeu uma matriz em que cada linha representa uma sala e cada coluna representa a temperatura registrada em um horário diferente do dia.
temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
Crie um programa em Python que:
Percorra toda a matriz de temperaturas.
Calcule a média de temperatura de cada sala.
Identifique quantas vezes cada sala registrou temperatura maior ou igual a 33.
Mostre, para cada sala:
número da sala;
média das temperaturas;
quantidade de registros críticos.
Ao final, informe qual sala teve a maior quantidade de registros críticos.
Considere que a primeira linha da matriz representa a Sala 1, a segunda linha representa a Sala 2, e assim por diante.
Saída esperada:
Sala 1
Média: 31.5
Registros críticos: 2
Sala 2
Média: 27.25
Registros críticos: 0
Sala 3
Média: 34.25
Registros críticos: 3
Sala 4
Média: 25.5
Registros críticos: 0
Sala com maior risco: Sala 3
'''

temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27],
]

total = 0
critico = 0
media = 0
maior_media = 0

for i in range(0, 4):
    for j in range(0,4):
        total += temperaturas[i][j]
        if temperaturas[i][j] >= 33:
            critico +=1
    media = total/4
    if media > maior_media:
        maior = i + 1
        maior_media = media

    print(f"Sala {i+1}")
    print(f"Média: {media}")
    total = 0
    print(f"Registros críticos: {critico}\n")
    critico = 0
print(f"Sala com maior risco: Sala {maior}")