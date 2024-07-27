var_controle_1 = True
var_controle_2 = True
dic_escolas = {}
dic_quesitos = {}
dic_notas = {}
lista_de_quesitos = []
lista_aux = []
escola_vencedora = ''
nota_escola_vencedora = 0


def nota_final(media, tempo_desfile):
    if tempo_desfile < 65:
        nota_de_retorno = media - (65 - tempo_desfile) * 0.1
        return nota_de_retorno
    elif tempo_desfile > 75:
        nota_de_retorno = media - (tempo_desfile - 75) * 0.1
        return nota_de_retorno
    else:
        return media


while var_controle_1:
    entrada_1 = input()

    if entrada_1 == "Não há mais escolas":
        var_controle_1 = False

    if var_controle_1 is True:
        entrada_2 = input()
        entrada_3 = int(input())
        dic_escolas.update({f'{entrada_1}': entrada_3})
        dic_notas.update({f'{entrada_1}': lista_aux})

while var_controle_2:
    entrada_quesitos = input()
    lista_de_notas = []
    lista_aux = []
    if entrada_quesitos == "Não há mais quesitos":
        var_controle_2 = False

    if var_controle_2 is True:
        for i in range(len(dic_escolas)):
            entrada_notas = input()
            var_aux = entrada_notas.replace(' -', ':')
            lista_aux.append(var_aux)
        dic_quesitos.update({f'{entrada_quesitos}': lista_aux})

print('Desfile de samba do Rio de janeiro 2024')

for quesito, notas in dic_quesitos.items():
    print(f'Vamos às notas para o quesito {quesito}:')
    for nota in notas:
        print(nota)

for escola in dic_escolas:
    lista_aux = []
    for quesito, notas in dic_quesitos.items():
        for nota in notas:
            var_aux = nota.split(': ')
            if var_aux[0] == escola:
                lista_aux.append(var_aux[1])
    dic_notas.update({f'{escola}': lista_aux})

for escola, notas in dic_notas.items():
    notas_teste = 0
    media_teste = 0
    for nota in notas:
        notas_teste += float(nota)

    media_teste = notas_teste / len(dic_quesitos)
    media_teste = nota_final(media_teste, dic_escolas[escola])

    if media_teste > nota_escola_vencedora:
        nota_escola_vencedora = media_teste
        escola_vencedora = escola

print('E o vencedor do desfile de escola de samba do Rio de Janeiro de 2024 é:')
print(f'{escola_vencedora} com uma nota final de {nota_escola_vencedora:.2f}!')
