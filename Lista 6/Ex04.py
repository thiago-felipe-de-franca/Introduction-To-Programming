def calcular_pontuacao(fantasia):
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    soma_posicoes = sum(consoantes.index(letra) + 1 for letra in fantasia if letra in consoantes)
    tamanho_fantasia = len(fantasia)
    if soma_posicoes == 0:
        return 0
    return (tamanho_fantasia ** 2) / soma_posicoes

candidatos = {}

while True:
    comando = input()
    entrada_personagem = input()
    entrada = entrada_personagem.split(" - ")
    if comando == 'Fim':
        break
    elif comando == 'Adicionar':
        if len(entrada) > 1:
            nome = entrada[0]
            fantasia = entrada[1]
            if nome in candidatos:
                print(f'Opa, parece que {nome} ja consta aqui, voce quis dizer "Atualizar"?')
            else:
                duplicata = False
                for candidato, f in candidatos.items():
                    if f == fantasia:
                        print(f'Eita, parece que {nome} tentou usar a fantasia {fantasia} que ja está sendo utilizada por {candidato}, ele deverá ser desqualificado por plágio')
                        duplicata = True
                        break
                if not duplicata:
                    candidatos[nome] = fantasia
                    print(f'{nome.upper()} é o novo participante do desfile!')
        else:
            print("Entrada inválida para o comando 'Adicionar'")
    elif comando == 'Remover':
        if len(entrada) > 1:
            nome = entrada[0]
            fantasia = entrada[1]
            if nome in candidatos:
                del candidatos[nome]
                print(f'Parece que {nome} desistiu...')
            else:
                print(f'Hmmm não consegui achar {nome} no banco de dados...')
        else:
            print("Entrada inválida para o comando 'Remover'")
    elif comando == 'Atualizar':
        if len(entrada) > 1:
            nome = entrada[0]
            nova_fantasia = entrada[1]
            if nome in candidatos:
                del candidatos[nome]
                print(f'Fantasia de {nome} atualizada')
                for candidato, f in candidatos.items():
                    if f == nova_fantasia:
                        print(f'Eita, parece que {nome} tentou usar a fantasia {nova_fantasia} que ja está sendo utilizada por {candidato}, ele deverá ser desqualificado por plágio')
                        break
                else:
                    candidatos[nome] = nova_fantasia
            else:
                print(f'Hmmm não consegui achar {nome} no banco de dados...')
        else:
            print("Entrada inválida para o comando 'Atualizar'")
    elif comando == 'Julgar':
        if len(candidatos) < 2:
            print('Parece que não temos candidatos o suficiente para julgar ainda...')
        else:
            pontuacoes = {nome: calcular_pontuacao(fantasia) for nome, fantasia in candidatos.items()}
            sorted_candidatos = sorted(pontuacoes.items(), key=lambda x: (-x[1], x[0]))
            diferenca_pontos = sorted_candidatos[0][1] - sorted_candidatos[1][1]
            print(f'Até o momento, o primeiro colocado é {sorted_candidatos[0][0].upper()} com uma diferença de {diferenca_pontos:.1f} pontos para o segundo colocado')

print("=== RESULTADOS DO DESFILE ===")
if len(candidatos) > 0:
    pontuacoes = {nome: calcular_pontuacao(fantasia) for nome, fantasia in candidatos.items()}
    sorted_candidatos = sorted(pontuacoes.items(), key=lambda x: (-x[1], x[0]))
    for candidato, pontuacao in sorted_candidatos:
        print(f'{candidato} --- {pontuacao:.1f}\n')
    print("PARABÉNS", sorted_candidatos[0][0].upper() + "!!! VOCÊ ACABA DE VENCER O PRIMEIRO DESFILE DO LIMOEIRO!!")
else:
    print("Parece que não sobrou ninguem na disputa, que pena…")
