from update_player_stats import update_stat_value


def sell_items(player_items, coins):
    item_code = input("\nCódigo do item: ")

    item_found = False
    i = 0
    while i < len(player_items):
        if item_code == player_items[i][0]:
            item_found = True

            coins += player_items[i][3]
            item_description = player_items[i][4]
            item_type = player_items[i][5]

            print("Venda efetuada!")
            print("Você ganhou", player_items[i][3], "moedas")
            print("Você tem", coins, "moedas")

            player_items.pop(i)

            new_stat_value = update_stat_value(player_items, item_description, item_type)
        i += 1

    if not item_found:
        print("Item não encontrado!")
        player_items, coins, new_stat_value = sell_items(player_items, coins)

    return player_items, coins, new_stat_value, item_type
