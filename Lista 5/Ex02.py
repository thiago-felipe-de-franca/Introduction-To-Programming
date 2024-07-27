num_pedidos = int(input())
lista_aux = []
resultado = None
valores_teste = []


def separar(a, b):
    if a == b:
        return True
    elif a < b:
        return False
    if b in valores_teste:
        return True
    if a % 3 == 0:
        x1 = a * 2 / 3
        x2 = a / 3
        valores_teste.append(x1)
        valores_teste.append(x2)
        return separar(x1, b)


for i in range(num_pedidos):
    resultado = ''
    valores_teste = []
    pedido = input()
    lista_aux = pedido.split(' ')
    resultado = separar(int(lista_aux[0]), int(lista_aux[1]))
    if resultado is True:
        print('SIM')
    else:
        print('NAO')
