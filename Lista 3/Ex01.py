nome_missao = input()
heroi = ''
grupo = []
while heroi != 'Grupo formado':
    heroi = input()
    if heroi != 'Grupo formado':
        grupo.append(heroi)
quantidade_herois = len(grupo)
print(f'O grupo formado por {quantidade_herois} heróis para a missão {nome_missao} foi:')
for escolhido in range(quantidade_herois):
    print(f'- {grupo[escolhido]}')
