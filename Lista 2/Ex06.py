nome_pretendente = input()
perdeu = "perdeu"
resultado = ""
while nome_pretendente != "vou dormir":
    palavra_pretendente = input()
    palavra_taylor = input()
    palavra_taylor_copia = palavra_taylor
    palavra_pretendente_copia = palavra_pretendente
    resultado = ""

    for letra in palavra_taylor:
        if letra in palavra_pretendente_copia:
            palavra_pretendente_copia = palavra_pretendente_copia.replace(letra, '', 1)
            palavra_taylor_copia = palavra_taylor_copia.replace(letra, '', 1)
    if len(palavra_taylor_copia) > 0:
        resultado = perdeu
    if resultado == perdeu:
        print("perdeu covarde!")
    else:
        print(f"você acertou, estreou na lista! {nome_pretendente}")

    nome_pretendente = input()
