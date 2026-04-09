from database.setup import create_tables
from repositories.pedido_repository import (
    criar_pedido,
    listar_pedidos,
    cancelar_pedido_db,
    inserir_item_pedido,
    buscar_pedido_por_id,
    buscar_itens_por_pedido
)

from repositories.cliente_repository import (
    inserir_cliente,
    listar_clientes
)
from repositories.produto_repository import (
    inserir_produto,
    listar_produtos,
    buscar_produto_por_id,
    atualizar_estoque
)
def menu():
    print("\n=== SISTEMA DE PEDIDOS ===")
    print("1 - Cadastrar Produto")
    print("2 - Lista Produtos")
    print("3 - Cadastrar Cliente")
    print("4 - Lista Cliente")
    print("5 - Criar Pedido")
    print("6 - Lista Pedidos")
    print("7 - Cancelar pedido")
    print("8 - Sair")

if __name__ == "__main__":
    create_tables()

    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input('Nome do Produto: ')
            preco = float(input('Preço: '))
            estoque = int(input('Estoque: '))

            inserir_produto(nome, preco, estoque)
            print('Produto cadastrado com sucesso!')

        elif opcao == "2":
            produtos = listar_produtos()

            print("\n--- LISTA DE PRODUTOS ---")

            if not produtos:
                print("Nenhum produto cadastrado.")
            else:
                for produto in produtos:
                    status_estoque = "Sem estoque" if produto["estoque"] <= 0 else "Disponível"

                    print(
                        f"ID: {produto['id']} | "
                        f"Nome: {produto['nome']} | "
                        f"Preço: R$ {produto['preco']:.2f} | "
                        f"Estoque: {produto['estoque']} | "
                        f"Status: {status_estoque}"
                    )
        elif opcao == "3":
            nome = input("Nome do cliente: ")
            email = input("Email: ")

            inserir_cliente(nome, email)
            print("Cliente cadastrado com sucesso!")

        elif opcao == "4":
            clientes = listar_clientes()

            print("\n--- LISTA DE CLIENTES ---")

            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                for cliente in clientes:
                    print(f"ID: {cliente['id']} | Nome: {cliente['nome']} | Email: {cliente['email']}")

        elif opcao == "5":
            cliente_id = int(input("ID do cliente: "))
            produto_id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))

            produto = buscar_produto_por_id(produto_id)

            if not produto:
                print("Produto não encontrado.")
            elif produto["estoque"] < quantidade:
                print(f"Estoque insuficiente. Disponível: {produto['estoque']}")
            else:
                preco_unitario = produto["preco"]
                total = preco_unitario * quantidade

                pedido_id = criar_pedido(cliente_id, total)

                sucesso = inserir_item_pedido(pedido_id, produto_id, quantidade, preco_unitario)

                novo_estoque = produto["estoque"] - quantidade
                atualizar_estoque(produto_id, novo_estoque)

                if not sucesso:
                    print("Erro ao criar pedido.")
                else:
                    print(f"Pedido criado com sucesso! Total: R$ {total:.2f}")


        elif opcao == "6":
            pedidos = listar_pedidos()

            print("\n--- LISTA DE PEDIDOS ---")

            if not pedidos:
                print("Nenhum pedido encontrado.")
            else:
                for pedido in pedidos:
                    print(
                        f"Pedido ID: {pedido['pedido_id']} | "
                        f"Cliente: {pedido['cliente_nome']} | "
                        f"Produto: {pedido['produto_nome']} | "
                        f"Qtd: {pedido['quantidade']} | "
                        f"Preço Unit: R$ {pedido['preco_unitario']:.2f} | "
                        f"Total: R$ {pedido['total']:.2f} | "
                        f"Status: {pedido['status']}"
                    )
        elif opcao == "7":
            pedido_id = int(input("ID do pedido para cancelar: "))

            pedido = buscar_pedido_por_id(pedido_id)

            if not pedido:
                print("Pedido não encontrado.")
            elif pedido["status"] == "cancelado":
                print("Pedido já está cancelado.")
            else:
                itens = buscar_itens_por_pedido(pedido_id)

                for item in itens:
                    produto = buscar_produto_por_id(item["produto_id"])
                    novo_estoque = produto["estoque"] + item["quantidade"]
                    atualizar_estoque(item["produto_id"], novo_estoque)

                cancelar_pedido_db(pedido_id)
                print("Pedido cancelado e estoque devolvido com sucesso!")

        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida")
