import time


def buy_items(
    player_items,
    store_inventory,
    coins,
    current_stat_value,
    item_description,
    num=None,
    is_inventory_item=False,
):
    item_code = input("\nCódigo do item: ")

    item_found = False
    for item in store_inventory:
        if item_code == item[0]:
            item_found = True

            if coins - item[3] >= 0:
                coins -= item[3]
                current_stat_value = item[2]
                if is_inventory_item:
                    player_items.append(
                        [
                            item[0],
                            item[1],
                            item[2],
                            int(item[3] * 0.75), # reduz o preço do item para a venda
                            item_description,
                            num,
                        ]
                    )
                print("\nCompra efetuada!")
                print(
                    "Você possui o item",
                    item[1],
                    "\nE seu poder é",
                    item[2],
                    "de",
                    item_description,
                )
                print("O item custou", item[3], "moedas")
                if coins > 0:
                    print("\nVocê possui", coins, "moedas!")
                else:
                    print("\nSeu dinheiro acabou!")
                    break
            elif coins > 200:
                print("\nMoedas insuficientes!")
                player_items, coins, current_stat_value = buy_items(
                    player_items,
                    store_inventory,
                    coins,
                    current_stat_value,
                    item_description,
                    num,
                    is_inventory_item,
                )
            else:
                print("\nMoedas insuficientes!")
                print("Não é possível comprar novos itens!")
                print("Saindo do mercado...")
                time.sleep(1)
                break

    if not item_found:
        print("\nItem não encontrado!")
        player_items, coins, current_stat_value = buy_items(
            player_items,
            store_inventory,
            coins,
            current_stat_value,
            item_description,
            num,
            is_inventory_item,
        )

    return player_items, coins, current_stat_value
