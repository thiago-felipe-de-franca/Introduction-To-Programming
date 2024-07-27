entrada = input()
equipamentos = ['Foice de Hades', 'Talismã de Ícaro', 'Elmo da Invisibilidade', 'Cinto de Hermes', 'Espada Anaklusmos', 'Escudo Aegis', 'Adaga Katoptris']

lista_de_itens_nao_desejados = []
lista_de_herois = []
lista_printada = []

while entrada != 'Parar':
    lista_auxiliar = ['Foice de Hades', 'Talismã de Ícaro', 'Elmo da Invisibilidade', 'Cinto de Hermes', 'Espada Anaklusmos', 'Escudo Aegis', 'Adaga Katoptris']
    lista_de_itens_nao_desejados = entrada
    lista_de_itens_nao_desejados = lista_de_itens_nao_desejados.split('-')
    lista_de_herois.append(lista_de_itens_nao_desejados.pop(0))
    for item in lista_de_itens_nao_desejados:
        lista_auxiliar.pop(lista_auxiliar.index(item))
    lista_printada.append(lista_auxiliar)

    entrada = input()
cont = 0  # contador para acessar cada heroi
cont_2 = 0  # contador para acessar cada item da lista quando houver mais de um para ser printado

for heroi in lista_de_herois:
    cont_2 = 0
    if len(lista_printada[cont]) == 0:
        print(f'{heroi} irá batalhar na base do murro!')
    elif len(lista_printada[cont]) == 1:
        print(f'{heroi} irá rumo a batalha com o equipamento: ', end='')
        print(f'{lista_printada[cont][0]}!')
    else:
        print(f'{heroi} irá rumo a batalha com os seguintes equipamentos: ', end='')
        for item in lista_printada[cont]:
            if cont_2 < len(lista_printada[cont]) - 2:
                print(f'{lista_printada[cont][cont_2]}, ', end="")
            elif cont_2 < len(lista_printada[cont]) - 1:
                print(f'{lista_printada[cont][cont_2]} e ', end="")
            else:
                print(f'{lista_printada[cont][cont_2]}!')
            cont_2 += 1
    cont += 1
