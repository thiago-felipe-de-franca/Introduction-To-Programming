entrada = input()
coordenadas_coluna = []
coordenadas_linha = []
linha = 0
reliquias = 0


while entrada != 'Fim do labirinto':
    coluna = 0
    for x in entrada:
        if x == "1":
            coordenadas_coluna.append(coluna/2)
            coordenadas_linha.append(linha)
            reliquias += 1
        coluna += 1

    linha += 1
    entrada = input()

if reliquias > 0:
    print('Relíquias encontradas nos seguintes locais:')
    for it in range(reliquias):
        print(f'linha: {int(coordenadas_linha[it])}, coluna: {int(coordenadas_coluna[it])}')
else:
    print('Nenhuma relíquia encontrada no labirinto.')
