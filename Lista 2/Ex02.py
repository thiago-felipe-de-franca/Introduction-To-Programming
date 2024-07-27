quant_min = 0
i = 0
while i < 21:
    entrada = input()
    if entrada == "amei":
        quant_min += 4
    elif entrada == "não parei de ouvir":
        x = 0
        entrada2 = ""
        while entrada2 != 'pulei':
            entrada2 = input()
            if entrada2 != 'pulei':
                x += 1
        quant_min += 4 * x
    elif entrada == "escutei só metade":
        quant_min += 2
    if entrada == "parei":
        i = 20
    i += 1
print(f'Você ouviu {quant_min} minutos hoje!!!')
