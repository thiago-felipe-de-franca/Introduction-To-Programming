qtd_dias = int(input())
frase_1 = "Os astros estão radiantes hoje! Eles farão o possível para abençoar a todos com boa sorte."
frase_2 = "Os astros estão de bom humor hoje. Acho que você terá um pouco de sorte extra."
frase_3 = "As estrelas estão neutras hoje. O dia está em suas mãos."
frase_4 = "Isso é raro. As estrelas estão absolutamente neutras hoje."
frase_5 = "Hoje, Kiq não pôde consultar as estrelas. Sem a orientação astrológica, a busca por ovos fica à mercê do destino."
lista_de_ovos_encontrados = []
qtd_ovos = 0

for dias in range(qtd_dias):
    def maximo(a, b):
        maior = 0
        if a > b:
            maior = a
        else:
            maior = b
        return maior


    def horoscopo_dia(horoscopo_do_dia):
        if horoscopo_do_dia == frase_1:
            ovos_encontrados_dia = ovos_escondidos_dia
            lista_de_ovos_encontrados.append(ovos_encontrados_dia)
        elif horoscopo_do_dia == frase_2:
            ovos_encontrados_dia = int(ovos_escondidos_dia * 0.7)
            lista_de_ovos_encontrados.append(ovos_encontrados_dia)
        elif horoscopo_do_dia == frase_3:
            ovos_encontrados_dia = int(maximo(ovos_escondidos_dia* 0.7, ovos_escondidos_dia/ ((ovos_escondidos_dia% (dias + 1)) + 1)))
            lista_de_ovos_encontrados.append(ovos_encontrados_dia)
        elif horoscopo_do_dia == frase_4:
            ovos_encontrados_dia = int((ovos_escondidos_dia % (dias + 1)) + 1)
            lista_de_ovos_encontrados.append(ovos_encontrados_dia)
        else:
            ovos_encontrados_dia = 0
            lista_de_ovos_encontrados.append(ovos_encontrados_dia)
        return ovos_encontrados_dia


    ovos_escondidos_dia = int(input())
    qtd_ovos += horoscopo_dia(input())
    print(f'Dia {dias + 1}')
    print(f'Hoje Carlos encontrou {lista_de_ovos_encontrados[dias]} ovos!!')

print(qtd_ovos)
