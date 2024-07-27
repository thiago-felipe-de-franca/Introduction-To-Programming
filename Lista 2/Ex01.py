entrada = ""
pontuacao = 0
quantidade_de_musicas_tocadas = 0
ciranda = "os fãs estão formando uma ciranda"  # -3 pontos
flashes = "os fãs estão ligando os flashes e atrapalhando a visão"  # -2 pontos
tela = "os fãs estão dançando na frente da tela"  # -2 pontos
gritando = "os fãs estão gritando o nome da Taylor e atrapalhando a música"  # -2 pontos
cantando = "os fãs estão cantando as músicas em coro"  # +2 pontos
casamento = "houve um pedido de casamento na sessão"
continuar = True

while entrada != "long live" and continuar:
    entrada = input()
    if entrada == ciranda:
        pontuacao += -3
    elif entrada == flashes:
        pontuacao += -2
    elif entrada == tela:
        pontuacao += -2
    elif entrada == gritando:
        pontuacao += -2
    elif entrada == cantando:
        pontuacao += 2
    elif entrada == casamento:
        pontuacao += 2
    else:
        pontuacao += 1
        quantidade_de_musicas_tocadas += 1
    if pontuacao < 0:
        print(f'A Taylor só conseguiu cantar {quantidade_de_musicas_tocadas} músicas e a sessão foi interrompida.')
        continuar = False
if pontuacao > 0:
    print(f'A Taylor conseguiu concluir o show sem muitas interrupções e cantou {quantidade_de_musicas_tocadas} músicas.')
