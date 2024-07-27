n = int(input())
verso1 = "BAD BLOOD"
verso2 = "MAD LOVE"
verso3 = "YOU'VE DONE"
verso4 = "BAD BLOOD, HEY"
contador_versos_errados = 0
entrada = ""
certo = "certo"
errado = "errado"
resposta1 = ""
resposta2 = ""
resposta3 = ""
resposta4 = ""

for i in range(n):
    verso = ""
    if i == 0:
        entrada = input()
        if len(entrada) == len(verso1):
            for x, y in zip(entrada, verso1):
                x = x.upper()
                if x != y:
                    verso = errado
        else:
            verso = errado
        if verso == errado:
            contador_versos_errados += 1
        if entrada.upper() == verso1:
            resposta1 = entrada.upper()
    if i == 1:
        entrada = input()
        if len(entrada) == len(verso2):
            for x, y in zip(entrada, verso2):
                x = x.upper()
                if x != y:
                    verso = errado
        else:
            verso = errado
        if verso == errado:
            contador_versos_errados += 1
        if entrada.upper() == verso2:
            resposta2 = entrada.upper()
    if i == 2:
        entrada = input()
        if len(entrada) == len(verso3):
            for x, y in zip(entrada, verso3):
                x = x.upper()
                if x != y:
                    verso = errado
        else:
            verso = errado
        if verso == errado:
            contador_versos_errados += 1
        if entrada.upper() == verso3:
            resposta3 = entrada.upper()
    if i == 3:
        entrada = input()
        if len(entrada) == len(verso4):
            for x, y in zip(entrada, verso4):
                x = x.upper()
                if x != y:
                    verso = errado
        else:
            verso = errado
        if verso == errado:
            contador_versos_errados += 1
        if entrada.upper() == verso4:
            resposta4 = entrada.upper()

if n > 0:
    print("Cause, baby, now we've got")
    if resposta1 == verso1:
        print(resposta1)

if n > 1:
    print("You know it used to be")
    if resposta2 == verso2:
        print(resposta2)

if n > 2:
    print("So take a look what")
    if resposta3 == verso3:
        print(resposta3)

if n > 3:
    print("Cause, baby, now we've got")
    if resposta4 == verso4:
        print(resposta4)

if contador_versos_errados == 0:
    print("A plateia deu um show! Acertou tudo!")
elif ((n - contador_versos_errados)/n) >= 0.5:
    print("A plateia acertou a maior parte da música")
else:
    print("Foi um dia atípico e a plateia se esqueceu de grande da música")
