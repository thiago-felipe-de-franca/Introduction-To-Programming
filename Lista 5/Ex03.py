entrada = input()
lista_de_caracteres = entrada.split(' ')


def conversor_binario_decimal(binario):
    if len(binario) == 1:
        return int(binario)
    else:
        return int(binario[0]) * 2 ** (len(binario) - 1) + conversor_binario_decimal(binario[1:])


def converter_codigos(codigos):
    if len(codigos) == 1:
        return chr(conversor_binario_decimal(codigos[0]))
    else:
        return chr(conversor_binario_decimal(codigos[0])) + converter_codigos(codigos[1:])


mensagem = converter_codigos(lista_de_caracteres)
print(f"Os códigos da Matrix indicam que {mensagem} está perto.")
