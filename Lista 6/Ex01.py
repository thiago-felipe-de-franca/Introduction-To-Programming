tupla_de_escolas_do_rio = ("Porto da Pedra", "Beija-flor", "Salgueiro", "Grande Rio", "Unidos da Tijuca", "Imperatriz", "Mocidade", "Portela", "Vila Isabel", "Mangueira", "Paraíso do Tuiuti", "Viradouro")
dic_escolas = {}
var_controle = True
lista_aux = []
entrada = input()

while var_controle:
    lista_aux = entrada.split(": ")

    if lista_aux[0] not in tupla_de_escolas_do_rio:
        print("Epa, o que essa escola está fazendo aqui?!")
    else:
        if lista_aux[0] not in dic_escolas:
            dic_escolas.update({f'{lista_aux[0]}': lista_aux[1]})
            print(f'{lista_aux[0]} teve sua nota apurada!')
        elif lista_aux[0] in dic_escolas:
            dic_escolas.update({f'{lista_aux[0]}': lista_aux[1]})
            print(f'{lista_aux[0]} teve sua nota atualizada!')

    entrada = input()
    if entrada == 'Fim':
        var_controle = False


