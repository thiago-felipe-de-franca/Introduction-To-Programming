from math import sqrt


def calcular_distancia(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def cifra_de_cesar(palavra, numero_de_posicoes, direcao):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    deslocamento = numero_de_posicoes if direcao == 'R' else -numero_de_posicoes
    palavra_descriptografada = ''
    for letra in palavra:
        if letra in alfabeto:
            indice = (alfabeto.index(letra) + deslocamento) % 26
            palavra_descriptografada += alfabeto[indice]
        else:
            palavra_descriptografada += letra
    return palavra_descriptografada


def encontrar_cidade_mais_proxima(x_atual, y_atual, cidades):
    distancia_minima = float('inf')
    index_cidade_mais_proxima = None

    for i, (nome, x, y, _, _, _) in enumerate(cidades):
        distancia = calcular_distancia(x_atual, y_atual, x, y)
        if distancia < distancia_minima:
            distancia_minima = distancia
            index_cidade_mais_proxima = i

    cidade_mais_proxima = cidades.pop(index_cidade_mais_proxima)
    return cidade_mais_proxima

quantidade_de_cidades = int(input())
cidades = []

for index in range(quantidade_de_cidades):
    cidade_info = input().split(', ')
    nome = cidade_info[0]
    x = float(cidade_info[1])
    y = float(cidade_info[2])
    palavra_criptografada = cidade_info[3]
    numero_de_posicoes = int(cidade_info[4])
    direcao = cidade_info[5]

    senha_descriptografada = cifra_de_cesar(palavra_criptografada, numero_de_posicoes, direcao)
    cidades.append((nome, x, y, senha_descriptografada))

x_atual, y_atual = 0, 0

for _ in range(quantidade_de_cidades):
    cidade_mais_proxima = encontrar_cidade_mais_proxima(x_atual, y_atual, cidades)
    nome, x_atual, y_atual = cidade_mais_proxima[:3]  # Ajuste para pegar apenas as coordenadas
    senha_descriptografada = cidade_mais_proxima[3]
    print(f"A senha da cidade {nome} é: {senha_descriptografada}")
