import time


def buy_items(
    player_items: list[tuple[str, str, int, int, str, int]],
    store_inventory: list[tuple[str, str, int, int]],
    coins: int,
    current_stat_value: int,
    item_description: str,
    item_type: int | None = None,
    is_inventory_item: bool = False,
) -> tuple[
    list[tuple[str, str, int, int, str, int]],  # player_items  
    int,  # coins
    int,  # current_stat_value
]:

    # recebendo o codigo do item a ser comprado
    item_code: str = input("\nCódigo do item: ")

    # definindo flag de busca do item
    item_found: bool = False

    # percorrendo os itens fazendo a busca
    for item in store_inventory:
        # verficiando se encontrou o item procurado
        if item_code == item[0]:
            # definindo a flag como verdadeiro
            item_found = True

            # verificando se tem moedas suficientes
            if coins >= item[3]:
                # subtraindo o custo do item
                coins -= item[3]
                # atualizando a estatistica do jogador
                current_stat_value = item[2]
                # verificando caso seja um item de permanente do inventario
                if is_inventory_item:
                    # adicionando o item comprado aos itens do jogador
                    player_items.append(
                        [
                            item[0],
                            item[1],
                            item[2],
                            int(item[3] * 0.75),  # reduz o preço do item para a venda
                            item_description,
                            item_type,
                        ]
                    )

                print("\nCompra efetuada!\n")
                print(f"Você possui o item {item[1]}")
                print(f"E seu poder é {item[2]} de {item_description}")
                print(f"O item custou {item[3]} moedas")

                # verificando se zerou as moeodas ou nao
                # nesse ponto nao tem possibilidade das moedas serem negativas
                if coins == 0:
                    # imprimindo mensagem e finalizando loop
                    print("\nSeu dinheiro acabou!\n")
                    break

                # imprimindo a quantidade restante de moedas
                print("\nVocê possui", coins, "moedas!")

            # verificando se tem moedas suficientes para nova compra
            elif coins > 200:
                # imprimindo mensagem de aviso
                print("\nMoedas insuficientes!")
                # continuando em compras pois tem moedas suficientes
                player_items, coins, current_stat_value = buy_items(
                    player_items,
                    store_inventory,
                    coins,
                    current_stat_value,
                    item_description,
                    item_type,
                    is_inventory_item,
                )
            # caso apenas nao tenha moedas suficientes para nada
            else:
                # imprimindo mensagens de aviso
                print("\nMoedas insuficientes!\n")
                print("Não é possível comprar novos itens!")
                print("Saindo do mercado...")
                time.sleep(1)
                break

    if not item_found:
        # impriminido mensagem de aviso
        print("\nItem não encontrado!\n")
        # continuando para compras
        player_items, coins, current_stat_value = buy_items(
            player_items,
            store_inventory,
            coins,
            current_stat_value,
            item_description,
            item_type,
            is_inventory_item,
        )

    # retornando informacoes necessarias
    return player_items, coins, current_stat_value
