numero = int(input())

string_1 = input()
string_2 = input()
string_3 = input()

len_string_1 = len(string_1)
len_string_2 = len(string_2)
len_string_3 = len(string_3)

string_mais_letras = ""
string_menos_letras = ""
string_lexicograficamente_maior = ""
contador = 0

if (numero == 1):
    if (len_string_1 >= len_string_2 and len_string_1 >= len_string_3):
        string_mais_letras = string_1
    if (len_string_2 >= len_string_1 and len_string_2 >= len_string_3):
        string_mais_letras = string_2
    if (len_string_3 >= len_string_2 and len_string_3 >= len_string_1):
        string_mais_letras = string_3

    # contador de empate
    if (len_string_1 == len(string_mais_letras)):
        contador = contador + 1
    if (len_string_2 == len(string_mais_letras)):
        contador = contador + 1
    if (len_string_3 == len(string_mais_letras)):
        contador = contador + 1

    if (contador > 1):
        print("(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)")
        if (string_1 > string_2 and string_1 > string_3):
            string_lexicograficamente_maior = string_1
            print(string_lexicograficamente_maior)
            print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
        elif (string_2 > string_1 and string_2 > string_3):
            string_lexicograficamente_maior = string_2
            print(string_lexicograficamente_maior)
            print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
        elif (string_3 > string_1 and string_3 > string_2):
            string_lexicograficamente_maior = string_3
            print(string_lexicograficamente_maior)
            print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
        else:
            print('"AAAAAA! Um fantasma me assustou!"')
            print('(Uma mensagem apareceu no monitor que você estava usando. "Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin")')

    else:
        print(string_mais_letras)
        print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')


elif (numero == 2):
    if (len_string_1 <= len_string_2 and len_string_1 <= len_string_3):
        string_menos_letras = string_1
    if (len_string_2 <= len_string_1 and len_string_2 <= len_string_3):
        string_menos_letras = string_2
    if (len_string_3 <= len_string_2 and len_string_3 <= len_string_1):
        string_menos_letras = string_3
    # contador de empate

    if (len_string_1 == len(string_menos_letras)):
        contador = contador + 1
    if (len_string_2 == len(string_menos_letras)):
        contador = contador + 1
    if (len_string_3 == len(string_menos_letras)):
        contador = contador + 1

    if (contador > 1):
        print("(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)")
        if (string_1 > string_2 and string_1 > string_3):
            string_lexicograficamente_maior = string_1
            print(string_lexicograficamente_maior)
            print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
        elif (string_2 > string_1 and string_2 > string_3):
            string_lexicograficamente_maior = string_2
            print(string_lexicograficamente_maior)
            print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
        elif (string_3 > string_1 and string_3 > string_2):
            string_lexicograficamente_maior = string_3
            print(string_lexicograficamente_maior)
            print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')
        else:
            print('"AAAAAA! Um fantasma me assustou!"')
            print('(Uma mensagem apareceu no monitor que você estava usando. "Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin")')

    else:
        print(string_menos_letras)
        print('(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. "Muito bem agente. A EPF agradece os seus esforços")')

print("(Depois de ler a mensagem, você dormiu. Ao acordar, você não estava mais no CIn de outubro de 2012, mas no CIn de 2023, sem acreditar na situação que vivenciou)")


