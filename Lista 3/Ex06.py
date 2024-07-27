entrada = input()
lista_de_objetos = entrada.split(' - ')
n = int(input())
spot = ''
var_aux = ''
lista_aux = []
mochila = []

if len(lista_de_objetos) % 2 == 0:  # se o número de itens for par
    for i in range(n):
        movimento = input()
        comando = input()
        movimento = movimento.replace('>', '|>').replace('<', '|<')
        lista_aux = movimento.split('|')
        for x in range(int(lista_aux[0])):
            if lista_aux[1] == '<':  # rotacao para a direita
                var_aux = lista_de_objetos.pop(-1)
                lista_de_objetos.insert(0, var_aux)
            else:  # rotacao para a esquerda
                var_aux = lista_de_objetos.pop(0)
                lista_de_objetos.append(var_aux)
        spot = lista_de_objetos[int(len(lista_de_objetos) / 2)]
        if spot in mochila:  # se o objeto ja estava na mochila
            print(f'{spot} já está na mochila. Não seja gananciosa, ou acabará como Midas!')
        else:  # se o objeto nao estava na mochila
            if comando == 'Adicionar':
                mochila.append(spot)
                print(f'{spot} adicionado a mochila!')
            else:
                print(f'{spot} não vai ser tão útil assim!')

else:  # se o número de itens for impar
    for i in range(n):
        movimento = input()
        comando = input()
        movimento = movimento.replace('>', '|>').replace('<', '|<')
        lista_aux = movimento.split('|')
        for x in range(int(lista_aux[0])):
            if lista_aux[1] == '<':  # rotacao para a direita
                var_aux = lista_de_objetos.pop(-1)
                lista_de_objetos.insert(0, var_aux)
            else:  # rotacao para a esquerda
                var_aux = lista_de_objetos.pop(0)
                lista_de_objetos.append(var_aux)
        spot = lista_de_objetos[int(len(lista_de_objetos) / 2)]
        if spot in mochila:  # se o objeto ja estava na mochila
            print(f'{spot} já está na mochila. Não seja gananciosa, ou acabará como Midas!')
        else:  # se o objeto nao estava na mochila
            if comando == 'Adicionar':
                mochila.append(spot)
                print(f'{spot} adicionado a mochila!')
            else:
                print(f'{spot} não vai ser tão útil assim!')

if len(mochila) > 0:
    print('Com ', end='')
    for item in mochila:
        print(f'{item}, ', end='')
    print('seremos imbatíveis na caça à bandeira!')

else:
    print('Não achei nada útil no arsenal. Acho que vamos precisar ser menos violentos dessa vez…')
