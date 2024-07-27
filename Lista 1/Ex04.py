# Capturando as entradas
nome_filme1 = input()
nota_letterboxd1 = int(input())
nota_imdb1 = int(input())

nome_filme2 = input()
nota_letterboxd2 = int(input())
nota_imdb2 = int(input())

nome_filme3 = input()
nota_letterboxd3 = int(input())
nota_imdb3 = int(input())

# decidir a maior nota
maior_nota_letterboxd = 0

if (nota_letterboxd1 > maior_nota_letterboxd):
    maior_nota_letterboxd = nota_letterboxd1
if (nota_letterboxd2 > maior_nota_letterboxd):
    maior_nota_letterboxd = nota_letterboxd2
if (nota_letterboxd3 > maior_nota_letterboxd):
    maior_nota_letterboxd = nota_letterboxd3

# decidir se teve empate
contador = 0
nota_produto1 = 0
nota_produto2 = 0
nota_produto3 = 0

if (nota_letterboxd1 == maior_nota_letterboxd):
    contador = contador + 1
    nota_produto1 = nota_letterboxd1 * nota_imdb1

if (nota_letterboxd2 == maior_nota_letterboxd):
    contador = contador + 1
    nota_produto2 = nota_letterboxd2 * nota_imdb2

if (nota_letterboxd3 == maior_nota_letterboxd):
    contador = contador + 1
    nota_produto3 = nota_letterboxd3 * nota_imdb3

if (contador > 1):
    print("Aldo continua sem saber qual filme assistir...")

# Resolver os casos de empate
nota_melhor_filme = 0

if (nota_produto1 > nota_produto2 and nota_produto1 > nota_produto3):
    melhor_filme = nome_filme1
    nota_melhor_filme = nota_letterboxd1

if (nota_produto2 > nota_produto1 and nota_produto2 > nota_produto3):
    melhor_filme = nome_filme2
    nota_melhor_filme = nota_letterboxd2

if (nota_produto3 > nota_produto1 and nota_produto3 > nota_produto2):
    melhor_filme = nome_filme3
    nota_melhor_filme = nota_letterboxd3

print("O filme de terror escolhido foi...")

if(nota_melhor_filme <= 6):
    print(melhor_filme + "?! Aldo provavelmente irá odiar um filme de terror com essa nota...")
else:
    print(melhor_filme+"! Esse filme de terror é maravilhoso... Aldo vai amar!")