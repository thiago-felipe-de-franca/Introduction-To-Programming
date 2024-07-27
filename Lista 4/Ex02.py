n = int(input())
lista_de_presentes = []
lista_de_presentes_excluidos = []
lista_aux_for = []
lista_aux_funcao = []


def somarvalores(lista):
    total = 0
    for elemento in lista:
        total += int(elemento)
    return total


for i in range(n):
    presente_codificado = input()
    lista_aux_for = presente_codificado.split(" ")
    lista_aux_funcao = presente_codificado.split(" ")
    for char in range(len(lista_aux_for)):  # substituir os numeros por caracteres
        lista_aux_for[char] = chr(int(lista_aux_for[char]))

    valores = somarvalores(lista_aux_funcao)  # capturar a soma dos valores do codigo
    presente = ''.join(lista_aux_for)

    if valores % 2 == 0:  # Se a soma dos codigos ASCII for par
        if presente in lista_de_presentes:
            print(f'{presente} já está na lista de presentes da Anya!!')
        else:
            lista_de_presentes.append(presente)
            print(f'{presente} foi adicionado a lista ultrassecreta de presentes da Anya!!')
    else:  # Se a soma dos codigos ASCII for impar
        if presente in lista_de_presentes_excluidos:
            print(f'{presente} já está na lista de presentes da Anya!!')
        else:
            lista_de_presentes_excluidos.append(presente)
            print(f'{presente} foi adicionado a lista ultrassecreta de presentes da Anya!!')
if n == 0:
    print('O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!')

elif len(lista_de_presentes) == 0:
    print(f"Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: ", end='')
    for i in range(len(lista_de_presentes_excluidos)):
        if i == (len(lista_de_presentes_excluidos) - 1):
            print(f'{lista_de_presentes_excluidos[i]}.')
        else:
            print(f'{lista_de_presentes_excluidos[i]}, ', end='')
    print('O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!')
elif len(lista_de_presentes_excluidos) == 0:
    print("Parece que o Dia das Crianças desse ano será especial!!!! Anya ganhará todos os presentes planejados, mesmo que ela não seja tão exemplar como deveria…")
    print('Lista final dos melhores presentes da Anya: ', end='')
    for i in range(len(lista_de_presentes)):
        if i == (len(lista_de_presentes) - 1):
            print(f'{lista_de_presentes[i]}.')
        else:
            print(f'{lista_de_presentes[i]}, ', end='')
else:
    print(f"Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: ", end='')
    for i in range(len(lista_de_presentes_excluidos)):
        if i == (len(lista_de_presentes_excluidos) - 1):
            print(f'{lista_de_presentes_excluidos[i]}.')
        else:
            print(f'{lista_de_presentes_excluidos[i]}, ', end='')
    print('Lista final dos melhores presentes da Anya: ', end='')
    for i in range(len(lista_de_presentes)):
        if i == (len(lista_de_presentes) - 1):
            print(f'{lista_de_presentes[i]}.')
        else:
            print(f'{lista_de_presentes[i]}, ', end='')
