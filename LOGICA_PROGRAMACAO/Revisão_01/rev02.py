print("Mercadinho BigBom")

produtos = []  # Lista para armazenar os produtos
total_compra = 0  # Valor total das compras
opcao = 0

while opcao != 5:
    print("\nOpções:")
    print("1 - Cadastrar produto")
    print("2 - Comprar produto")
    print("3 - Verificar estoque")
    print("4 - Verificar valor total da compra")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Digite a quantidade em estoque: "))
        produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
        print(f"Produto '{nome}' cadastrado com sucesso.")

    elif opcao == 2:
        nome = input("Digite o nome do produto a comprar: ")
        quantidade = int(input("Digite a quantidade a ser comprada: "))
        encontrado = False
        for p in produtos:
            if p["nome"] == nome:
                encontrado = True
                if p["estoque"] >= quantidade:
                    p["estoque"] -= quantidade
                    valor = p["preco"] * quantidade
                    total_compra += valor
                    print(f"Compra realizada com sucesso! Total: R$ {valor:.2f}")
                else:
                    print("Estoque insuficiente.")
                break
        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == 3:
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("\nEstoque:")
            for p in produtos:
                print(f"{p['nome']} - Preço: R$ {p['preco']:.2f} - Estoque: {p['estoque']}")

    elif opcao == 4:
        print(f"Valor total da compra: R$ {total_compra:.2f}")

    elif opcao == 5:
        print("Saindo do programa. Obrigado por usar o Mercadinho BigBom!")

    else:
        print("Opção inválida. Por favor, tente novamente.")
