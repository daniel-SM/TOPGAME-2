# importando para definir tipo dos parametros
from typing import Literal


# funcao para atualizar o stat de um item vendido
def update_stat_value(
    player_items: list[tuple[str, str, int, int, str, int]],
    item_description: str,
    item_type: Literal[0, 1, 2],
) -> int:
    item_found: bool = False
    stat_value: int = 0

    # buscando algum item que tenha mesmo tipo do item vendido
    for item in player_items:
        # verificando se encontrou item do mesmo tipo
        if item[4] == item_description:
            item_found = True
            stat_value = item[2]

    # definindo como o valor padrão caso não encontre algum item
    if not item_found:
        # se tipo do item vendido for de arma
        if item_type == 0:
            stat_value = 80
        # se tipo do item vendido for de escudo
        if item_type == 1:
            stat_value = 40
        # se tipo do item vendido for de armadura
        if item_type == 2:
            stat_value = 30

    return stat_value
