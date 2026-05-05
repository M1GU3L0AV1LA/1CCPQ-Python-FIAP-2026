tabuleiro = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

tabuleiro[0][0] = 'X'
tabuleiro[1][1] = 'O'
tabuleiro[2][2] = 'X'

for i in range(len(tabuleiro)):
    for j in range(len(tabuleiro)):
        print(f"|{tabuleiro[i][j]}",end="|")

    print()