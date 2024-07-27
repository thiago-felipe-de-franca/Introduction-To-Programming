frase_x = input()
# palavra_y = input()
# palavra_z = input()
# frase_z = input()
# x_jack = input()
# y_jack = input()
# z_jack = input()


def desafio_1(frase):
    lista_do_alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    frase = frase.lower()

    for letra in lista_do_alfabeto:
        if letra not in frase:
            # Se a letra não está presente, não é um pangrama
            # Retorna a contagem da letra que menos se repete
            letra_menos_repetida = min(lista_do_alfabeto, key=frase.count)
            return frase.count(letra_menos_repetida)

    # Se todas as letras estão presentes, é um pangrama
    # Retorna a contagem da letra que mais se repete
    letra_mais_repetida = max(lista_do_alfabeto, key=frase.count)
    return frase.count(letra_mais_repetida)


# def desafio_2()
