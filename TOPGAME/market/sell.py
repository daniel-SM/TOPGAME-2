from update_player_stats import update_stat_value


def sell_items(
    player_items: list[tuple[str, str, int, int, str, int]], coins: int
) -> tuple[
    list[tuple[str, str, int, int, str, int]],  # player_items
    int,  # coins
    int,  # new_stat_value
    int,  # item_type
]:

    # recebendo o codigo do item a ser vendido
    item_code: str = input("\nCódigo do item: ")

    # iniciando variaveis no escopo geral
    item_description: str = None
    item_type: int = None
    new_stat_value: int = None

    # iniciando variavel de controle da busca do item
    item_found: bool = False
    i: int = 0
    while i < len(player_items):
        if item_code == player_items[i][0]:
            # definindo que encontrou item procurado
            item_found = True

            coins += player_items[i][3]
            item_description = player_items[i][4]
            item_type = player_items[i][5]

            print("Venda efetuada!")
            print("Você ganhou", player_items[i][3], "moedas")
            print("Você tem", coins, "moedas")

            player_items.pop(i)

            new_stat_value = update_stat_value(
                player_items, item_description, item_type
            )
        i += 1

    if not item_found:
        print("Item não encontrado!")
        player_items, coins, new_stat_value, item_type = sell_items(player_items, coins)

    return player_items, coins, new_stat_value, item_type
