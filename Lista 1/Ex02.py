local_do_teste = input()
hora_do_teste = int(input())
resposta = input()

if (local_do_teste == "Salão"):
    print("Em direção ao salão!")
    print("Pra chegar na hora, vou ter que sair de " + str(hora_do_teste - 2) + " horas.")
elif (local_do_teste == "Praça"):
    print("Para a praça eu vou!")
    print("Pra chegar na hora, vou ter que sair de " + str(hora_do_teste - 2) + " horas.")
else:
    print("Faz tempo que não visito o centro, mal posso esperar!")
    print("Pra chegar na hora, vou ter que sair de " + str(hora_do_teste - 1) + " horas.")

if (resposta == "Sim, Pearl! Siga seus sonhos!"):
    print("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
else:
    print("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")