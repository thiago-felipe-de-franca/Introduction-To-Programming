linhas = int(input())
colunas = int(input())

lista_de_linhas = []

chale_mais_cheio = 0
maximo_de_alunos = 0

for y in range(linhas):
    lista_de_colunas = []
    var_auxiliar = 0
    for x in range(colunas):
        var = int(input())
        lista_de_colunas.append(var)
        var_auxiliar += var
    lista_de_linhas.append(lista_de_colunas)
    if var_auxiliar > maximo_de_alunos:
        maximo_de_alunos = var_auxiliar
        chale_mais_cheio = y + 1

for l in range(linhas):
    for c in range(colunas):
        print(lista_de_linhas[l][c], end='')
        if c < (colunas - 1):
            print(' ', end='')
    print()

print()
print(f'O chalé {chale_mais_cheio} foi o que mais recebeu semi-deuses, tendo um acréscimo de {maximo_de_alunos} novos campistas!')
