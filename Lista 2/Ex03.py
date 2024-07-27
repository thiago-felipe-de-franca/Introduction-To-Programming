n = int(input())
cont = 0
c = 0
pontuacao = 1
while cont < n:
    song = input()
    cont += 1
    c = 0
    for caractere in song:
        if caractere == 'A' or caractere == 'a':
            c += 1
        elif caractere == 'E' or caractere == 'e':
            c += 1
        elif caractere == 'I' or caractere == 'i':
            c += 1
        elif caractere == 'O' or caractere == 'o':
            c += 1
        elif caractere == 'U' or caractere == 'u':
            c += 1
        else:
            c += 2
    pontuacao *= c

print(f'Parabéns por adquirir o ingresso! Seu assento é o {pontuacao}, estamos ansiosos para vê-lo, vai ser incrível!')
