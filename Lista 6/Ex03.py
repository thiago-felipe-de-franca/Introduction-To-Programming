# Dicionário para armazenar o cardápio
cardapio = {
    "bobo de camarao": {"camarao": 1, "macaxeira": 1, "leite de coco": 1, "dende": 1, "tomate": 1, "cebola": 1},
    "tapioca de carne de sol": {"massa de tapioca": 1, "carne de sol": 1, "queijo coalho": 1, "tomate": 1, "cebola": 1},
    "carne de sol com macaxeira": {"carne de sol": 1, "macaxeira": 1, "manteiga": 1},
    "camarao na moranga": {"moranga": 1, "camarao": 1, "cebola": 1, "alho": 1, "tomate": 1, "pimentao": 1, "creme de leite": 1, "azeite": 1, "coentro": 1}
}

# Dicionário para armazenar os preços dos ingredientes
precos = {
    "camarao": 30,
    "macaxeira": 3,
    "leite de coco": 5,
    "dende": 15,
    "tomate": 3,
    "cebola": 2,
    "massa de tapioca": 10,
    "carne de sol": 30,
    "queijo coalho": 15,
    "moranga": 10,
    "alho": 1.5,
    "pimentao": 2,
    "creme de leite": 4,
    "azeite": 15,
    "coentro": 1,
    "manteiga": 5.5
}

# Dicionário para armazenar os preços dos pedidos do cardápio original
precos_cardapio_original = {
    "bobo de camarao": 58,
    "tapioca de carne de sol": 60,
    "carne de sol com macaxeira": 38.50,
    "camarao na moranga": 68.50
}

# Dicionário para armazenar as unidades em estoque
estoque = {ingrediente: 5 for ingrediente in precos}

# Variáveis para o lucro total e o pedido mais vendido
lucro_total = 0
mais_vendido = ""
quantidade_mais_vendido = 0

# Dicionário para armazenar as vendas de cada pedido
vendas = {pedido: 0 for pedido in cardapio}

# Dicionário para rastrear os pedidos que não estão no cardápio
novos_pedidos = {}

# Dicionário para armazenar os valores dos novos pedidos adicionados ao cardápio
novos_pedidos_adicionados = {}

try:
    while True:
        pedido = input().strip().lower()

        if pedido in cardapio:
            # Atualiza as vendas do pedido
            vendas[pedido] += 1

            # Verifica se há ingredientes suficientes em estoque
            ingredientes_suficientes = True
            for ingrediente, quantidade in cardapio[pedido].items():
                if estoque[ingrediente] < quantidade:
                    ingredientes_suficientes = False
                    break

            if ingredientes_suficientes:
                print(f"{pedido} saindo...")
                # Atualiza o estoque
                for ingrediente, quantidade in cardapio[pedido].items():
                    estoque[ingrediente] -= quantidade
                # Calcula o preço do pedido
                if pedido in precos_cardapio_original:
                    preco_pedido = precos_cardapio_original[pedido]
                elif pedido in novos_pedidos_adicionados:
                    preco_pedido = novos_pedidos_adicionados[pedido]
                else:
                    preco_pedido = sum(precos[ingrediente] for ingrediente in cardapio[pedido]) + 5
                lucro_total += preco_pedido
                # Atualiza o pedido mais vendido, se necessário
                quantidade_pedido_atual = sum(cardapio[pedido].values())
                if vendas[pedido] > quantidade_mais_vendido:
                    mais_vendido = pedido
                    quantidade_mais_vendido = vendas[pedido]
            else:
                print("Desculpe, não há ingredientes suficientes para preparar o pedido.")
        else:
            # Adiciona o pedido ao dicionário de novos pedidos
            novos_pedidos[pedido] = novos_pedidos.get(pedido, 0) + 1
            # Verifica se o pedido foi solicitado mais de duas vezes
            if novos_pedidos[pedido] > 2:
                print(f"Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Sabores de Recife.")
                # Recebe os ingredientes do novo pedido
                ingredientes_novo_pedido = []
                for _ in range(9):
                    ingrediente = input().strip().lower()
                    ingredientes_novo_pedido.append(ingrediente)
                # Calcula o preço do novo pedido
                preco_novo_pedido = sum(precos[ingrediente] for ingrediente in ingredientes_novo_pedido) + 5
                # Atualiza o cardápio com o novo pedido
                cardapio[pedido] = {ingrediente: 1 for ingrediente in ingredientes_novo_pedido}
                # Armazena o valor do novo pedido adicionado ao cardápio
                novos_pedidos_adicionados[pedido] = preco_novo_pedido
                vendas[pedido] = 0
                # Remove o pedido do dicionário de novos pedidos
                del novos_pedidos[pedido]
            else:
                print(f"{pedido} ainda não é uma opção disponível.")

        # Verifica quais ingredientes estão com estoque zerado e repõe
        for ingrediente, quantidade in estoque.items():
            if quantidade == 0 and any(quantidade > 0 for quantidade in cardapio[pedido].values()):
                # Reposição de ingredientes em múltiplos de 4
                unidades_repor = 4
                estoque[ingrediente] += unidades_repor  # Reposição de unidades

except EOFError:
    print("##### Fim do expediente #####")
    print(f"O lucro obtido no dia de hoje foi de R${lucro_total:.2f}.")
    if mais_vendido == "bobo de camarao":
        print("O bom e tradicional Bobó de Camarão, líder em vendas, nunca será superado!")
    else:
        print(f"{mais_vendido.capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário Bobó de Camarão.")
