def primeiro_desafio(frase_x):
    # Remover espaços e transformar em letras minúsculas
    frase_x = frase_x.replace(" ", "").lower()

    # Verificar se é um pangrama
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    pangrama = set(frase_x) >= alfabeto

    # Contar a letra que mais ou menos se repete
    if pangrama:
        letra_contagem = max(set(frase_x), key=frase_x.count)
    else:
        letra_contagem = min(set(frase_x), key=frase_x.count)

    return ord(letra_contagem) - ord('a') + 1


def segundo_desafio(palavra_y):
    # Calcular o número de Fibonacci com base no comprimento da palavra
    n = len(palavra_y)
    fib = fibonacci(n)

    # Multiplicar por 4 se a palavra contiver vogais, caso contrário, multiplicar por 2
    multiplicador = 4 if any(vogal in palavra_y for vogal in "aeiou") else 2

    return fib * multiplicador


def fibonacci(n):
    # Calcular o número de Fibonacci recursivamente
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def terceiro_desafio(palavra_z, frase_z):
    # Calcular a diferença entre minúsculas e maiúsculas para a palavra
    dif_palavra = palavra_z.count('a') - palavra_z.count('A')

    # Calcular a diferença entre minúsculas e maiúsculas para a frase
    dif_frase = frase_z.count('a') - frase_z.count('A')

    # Elevar à potência
    z_noel = dif_frase ** dif_palavra

    return z_noel


def calcular_distancia(x_noel, y_noel, z_noel, x_jack, y_jack, z_jack):
    # Calcular a distância entre dois pontos no espaço tridimensional
    distancia_final = ((x_noel - x_jack) ** 2 + (y_noel - y_jack) ** 2 + (z_noel - z_jack) ** 2) ** 0.5
    return distancia_final


# Entradas
frase_x = input()
palavra_y = input()
palavra_z = input()
frase_z = input()
x_jack = int(input())
y_jack = int(input())
z_jack = int(input())

# Resolver cada desafio
x_noel = primeiro_desafio(frase_x)
y_noel = segundo_desafio(palavra_y)
z_noel = terceiro_desafio(palavra_z, frase_z)

# Imprimir resultados
print(f"A 1ª coordenada do Papai Noel é: {x_noel}")
print(f"A 2ª coordenada do Papai Noel é: {y_noel}")
print(f"A 3ª coordenada do Papai Noel é: {z_noel}")

# Calcular e imprimir a distância final
distancia_final = calcular_distancia(x_noel, y_noel, z_noel, x_jack, y_jack, z_jack)
print(f"A distância entre Jack Esqueleto e Papai Noel é: {distancia_final:.2f}")
