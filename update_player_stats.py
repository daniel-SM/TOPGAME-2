def update_stat_value(player_items, item_description, item_type):
    item_found = False
    stat_value = 0

    # Buscando algum item que tenha mesmo tipo do item vendido
    for item in player_items:
        # Verificando se encontrou item do mesmo tipo
        if item[4] == item_description:
            item_found = True
            stat_value = item[2]

    # Definindo como o valor padrão caso não encontre algum item
    if not item_found:
        # Se tipo do item vendido for de arma
        if item_type == 0:
            stat_value = 80
        # Se tipo do item vendido for de escudo
        if item_type == 1:
            stat_value = 40
        # Se tipo do item vendido for de armadura
        if item_type == 2:
            stat_value = 30

    return stat_value
