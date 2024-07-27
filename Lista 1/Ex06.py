pontuacao = 0
porta1 = ""
porta2 = ""
porta3 = ""
porta4 = ""
porta5 = ""
certa = "CERTA"
errada = "ERRADA"
contador_portas_certas = 0
contador_portas_erradas = 0

# Primeira porta 150 pontos

direcao_escolhida_p1 = input()
numero_p1 = int(input())

if(numero_p1 % 2 == 1): # Se o numero for impar
    if(direcao_escolhida_p1 == "direita"):
        porta1 = certa
        contador_portas_certas += 1
    else:
        porta1 = errada
        contador_portas_erradas += 1
else:# Se o numero for par
    if(direcao_escolhida_p1 == "esquerda"):
        porta1 = certa
        contador_portas_certas += 1
    else:
        porta1 = errada
        contador_portas_erradas += 1

if(porta1 == "CERTA"):
    pontuacao = pontuacao + 150
else:
    pontuacao = pontuacao - 150

# Porta 2 200 pontos

direcao_escolhida_p2 = input()
cor_p2 = input()
planta_p2 = input()
macaneta_p2 = input()

if((cor_p2 == "dourada" or cor_p2 == "prateada") or ((planta_p2 == "avenca" or planta_p2 == "espadinha") and (macaneta_p2 == "redonda"))):
    if (direcao_escolhida_p2 == "direita"):
        porta2 = certa
        contador_portas_certas += 1
    else:
        porta2 = errada
        contador_portas_erradas += 1
else:
    if (direcao_escolhida_p2 == "esquerda"):
        porta2 = certa
        contador_portas_certas += 1
    else:
        porta2 = errada
        contador_portas_erradas += 1

if(porta2 == "CERTA"):
    pontuacao = pontuacao + 200
else:
    pontuacao = pontuacao - 200

# Porta 3 250 pontos

direcao_escolhida_p3 = input()
cor_p3 = input()
numero_p3 = int(input())
planta_p3 = input()
macaneta_p3 = input()


if(((numero_p3 % 5 == 0) and (planta_p3 == "espadinha") and (macaneta_p3 == "quadrada")) or (cor_p3 == "perolada")):
    if(direcao_escolhida_p3 == "esquerda"):
        porta3 = certa
        contador_portas_certas += 1
    else:
        porta3 = errada
        contador_portas_erradas += 1
else:
    if(direcao_escolhida_p3 == "direita"):
        porta3 = certa
        contador_portas_certas += 1
    else:
        porta3 = errada
        contador_portas_erradas += 1

if (porta3 == certa):
    pontuacao = pontuacao + 250
else:
    pontuacao = pontuacao - 250

# Porta 4 300 pontos

direcao_escolhida_p4 = input()
numero_p4 = int(input())

if((numero_p4 % 3 == 0) and (numero_p4 % 2 != 0) and (numero_p4 % 5 != 0)):
    if (direcao_escolhida_p4 == "direita"):
        porta4 = certa
        contador_portas_certas += 1
    else:
        porta4 = errada
        contador_portas_erradas += 1
else:
    if(direcao_escolhida_p4 == "esquerda"):
        porta4 = certa
        contador_portas_certas += 1
    else:
        porta4 = errada
        contador_portas_erradas += 1

if (porta4 == certa):
    pontuacao += 300
else:
    pontuacao += -300

# Porta 5

cor_p5 = input()
numero_p5 = int(input())
planta_p5 = input()
flor_p5 = input()
macaneta_p5 = input()

if ((cor_p5 == "acobreada") and ((numero_p5 % 2 == 1) or (macaneta_p5 == "triangular") or (macaneta_p5 == "quadrada")) and (planta_p5 == "jiboia")):
    pontuacao += 500
    porta5 = certa
    contador_portas_certas += 1
elif ((cor_p5 == "prateada") and ((flor_p5 != "margarida") and (flor_p5 != "papoula") and (flor_p5 != "cosmos")) and ((macaneta_p5 == "hexagonal") or (macaneta_p5 == "redonda"))):
    pontuacao += 450
    porta5 = certa
    contador_portas_certas += 1
elif ((cor_p5 == "dourada") and ((flor_p5 == "lirio") or (flor_p5 == "ixora")) and (macaneta_p5 == "hexagonal")):
    pontuacao += 400
    porta5 = certa
    contador_portas_certas += 1
else:
    pontuacao += - 500
    porta5 = errada
    contador_portas_erradas += 1

print("ARISU, VOCÊ FEZ SUAS ESCOLHAS E AGORA VEREMOS SE ESCOLHEU AS PORTAS CERTAS:")
print(porta1 + " " + porta2 + " " + porta3 + " " + porta4 + " " + porta5)

if(pontuacao > 0):
    if(contador_portas_erradas > 0):
        print("Você passou com " + str(pontuacao) + " pontos, mas faça melhores escolhas da próxima vez.")
    else:
        print("Parece que a sorte está ao seu favor, Arisu... Você conseguiu passar com " + str(pontuacao) + " pontos!")
else:
    if (contador_portas_certas > 0):
        print("Por mais que você tenha feito escolhas corretas, não foi suficiente para sobreviver. Você finalizou o jogo com " + str(pontuacao) + " pontos")
    else:
        print("Todas suas escolhas foram erradas, Arisu, esperávamos mais de você... Você será executado pois obteve " + str(pontuacao) + " pontos.")
