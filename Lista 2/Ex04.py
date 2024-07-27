n = int(input())
y = 0

for i in range(n):
    nome_comprador = input()
    cpf_comprador = input()
    nome_identidade = input()
    cpf_identidade = input()
    qtd_ingressos = int(input())
    preco_ingressos = int(input())
    codigo_compra = input()
    contador_impares = 0
    contador_criterios = 0

    if nome_comprador != nome_identidade:
        contador_criterios += 1

    if cpf_comprador != cpf_identidade:
        contador_criterios += 1

    if qtd_ingressos > 12:
        contador_criterios += 1

    if preco_ingressos > 1500:
        contador_criterios += 1

    for caractere in codigo_compra:
        if (int(caractere) % 2) == 1:
            contador_impares += 1

    if contador_impares >= 7:
        contador_criterios += 1

    if contador_criterios >= 3:
        y += 1

print(f"Total de compradores analisados: {n}")
print(f"Total de suspeitas de cambistas: {y}")