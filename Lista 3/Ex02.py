itens_desejados = input()
itens_no_acampamento = input()

lista_de_itens_desejados = itens_desejados.split(', ')
lista_de_itens_no_acampamento = itens_no_acampamento.split(', ')
lista_de_itens_utilizados = []
lista_de_itens_nao_utilizados = []

for desejado in lista_de_itens_desejados:
    if desejado in lista_de_itens_no_acampamento:
        lista_de_itens_utilizados.append(desejado)
    else:
        lista_de_itens_nao_utilizados.append(desejado)

if len(lista_de_itens_utilizados) > 0:
    print('Estes são os itens que já tenho no Acampamento Meio-Sangue:')
    for index in range(len(lista_de_itens_utilizados)):
        print(f'{index + 1}º item: {lista_de_itens_utilizados[index]}')
    if len(lista_de_itens_nao_utilizados) > 0:
        print(f'Vou precisar adquirir {len(lista_de_itens_nao_utilizados)} itens antes da batalha!')
    else:
        print(f'Perfeito, encontrei todos os {len(lista_de_itens_desejados)} itens aqui no Acampamento Meio-Sangue!')

else:
    print(f'Hmm, preciso visitar um vendedor ambulante! Não encontrei nenhum dos {len(lista_de_itens_desejados)} itens aqui no Acampamento Meio-Sangue.')

print('Estou pronto para a batalha! Que comece a guerra contra os Titãs!')
