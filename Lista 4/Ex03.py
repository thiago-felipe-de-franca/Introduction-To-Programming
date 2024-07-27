from math import sqrt

quantidade_de_cidades = int(input())
cidades = []
x_atual = 0
y_atual = 0


def distancia_euclidiana(x1, y1, x2, y2):
    distancia = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distancia


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

    for i in range(len(cidades)):
        cidade = cidades[i]
        distancia = distancia_euclidiana(x_atual, y_atual, cidade[1], cidade[2])
        if distancia < distancia_minima:
            distancia_minima = distancia
            index_cidade_mais_proxima = i

    cidade_mais_proxima = cidades.pop(index_cidade_mais_proxima)
    return cidade_mais_proxima


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

for b in range(quantidade_de_cidades):
    cidade_mais_proxima = encontrar_cidade_mais_proxima(x_atual, y_atual, cidades)
    nome, x_atual, y_atual = cidade_mais_proxima[:3]  # Ajuste para pegar apenas as coordenadas
    senha_descriptografada = cidade_mais_proxima[3]
    print(f"A senha da cidade {nome} é: {senha_descriptografada}")
