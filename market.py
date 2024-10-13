import time

from clear import clear_screen
from option import validate_option
from show_items import show_items
from show_player_items import show_player_items
from buy import buy_items
from sell import sell_items
from items import ATTACK_ITEMS, DEFENSE_ITEMS, POTION_ITEMS, REGEN_ITEMS, MAGIC_ITEMS


def market(
    player_items: list[tuple[str, str, int, int, str, int]],
    coins: int,
    player_life: int,
    player_attack: int,
    player_defense: int,
    player_life_regen: int,
    player_magic: int,
) -> tuple[
    list[tuple[str, str, int, int, str, int]],  # player_items
    int,  # coins
    int,  # player_life
    int,  # player_attack
    int,  # player_defense
    int,  # player_life_regen
    int,  # player_magic
]:
    clear_screen()

    # Definindo o tamanho da largura do quadro
    WIDTH: int = 40

    print()
    print(f"||{'-'*(WIDTH-4)}||")
    print(f"||{' '*(WIDTH-4)}||")
    print(f"||{'BEM-VINDO AO MERCADO':^{WIDTH-4}}||")
    print(f"||{' '*(WIDTH-4)}||")
    print(f"||{'-'*(WIDTH-4)}||")
    time.sleep(1)

    print(f"||{f'Você tem {coins} moedas':^{WIDTH-4}}||")
    print(f"||{'-'*(WIDTH-4)}||")
    time.sleep(1)

    print()
    print(f"||{'-'*(WIDTH-4)}||")
    print(f"||{'LOJAS':^{WIDTH-4}}||")
    print(f"||{' ' * 10}{'1. Loja de Armas':<{WIDTH-14}}||")
    print(f"||{' ' * 10}{'2. Loja de Escudos':<{WIDTH-14}}||")
    print(f"||{' ' * 10}{'3. Loja de Poções':<{WIDTH-14}}||")
    print(f"||{' ' * 10}{'4. Loja de Armaduras':<{WIDTH-14}}||")
    print(f"||{' ' * 10}{'5. Loja de Magias':<{WIDTH-14}}||")
    print(f"||{' ' * 10}{'6. Vender Itens':<{WIDTH-14}}||")
    print(f"||{' ' * 10}{'7. Sair':<{WIDTH-14}}||")
    print(f"||{'-'*(WIDTH-4)}||")

    store_code: str = input("\nLoja: ")

    while store_code not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Inválido!")
        store_code = input("Loja: ")

    clear_screen()

    if store_code == "1":
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"||{'LOJA DE ARMAS':^{WIDTH-4}}||")
        print(f"||{'-'*(WIDTH-4)}||")
        print()

        show_items(ATTACK_ITEMS, "ataque")
        option: str = input("\nS - sim\nN - não\nDeseja comprar algum item? ")
        option = validate_option(option)

        if option == "s":
            player_items, coins, player_attack = buy_items(
                player_items, ATTACK_ITEMS, coins, player_attack, "ataque", 0, True
            )

    elif store_code == "2":
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"||{'LOJA DE ESCUDOS':^{WIDTH-4}}||")
        print(f"||{'-'*(WIDTH-4)}||")

        show_items(DEFENSE_ITEMS, "defesa")
        option: str = input("\nS - sim\nN - não\nDeseja comprar algum item? ")
        option = validate_option(option)

        if option == "s":
            player_items, coins, player_defense = buy_items(
                player_items, DEFENSE_ITEMS, coins, player_defense, "defesa", 1, True
            )

    elif store_code == "3":
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"||{'LOJA DE POCÕES':^{WIDTH-4}}||")
        print(f"||{'-'*(WIDTH-4)}||")

        show_items(POTION_ITEMS, "vida a mais")

        option: str = input("\nS - sim\nN - não\nDeseja comprar algum item? ")
        option = validate_option(option)

        if option == "s":
            potion_value: int = 0
            player_items, coins, potion_value = buy_items(
                player_items, POTION_ITEMS, coins, potion_value, "vida a mais"
            )
            player_life += potion_value

    elif store_code == "4":
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"||{'LOJA DE ARMADURAS':^{WIDTH-4}}||")
        print(f"||{'-'*(WIDTH-4)}||")

        show_items(REGEN_ITEMS, "vida p/ fase")

        option: str = input("\nS - sim\nN - não\nDeseja comprar algum item? ")
        option = validate_option(option)

        if option == "s":
            player_items, coins, player_life_regen = buy_items(
                player_items,
                REGEN_ITEMS,
                coins,
                player_life_regen,
                "vida p/ fase",
                2,
                True,
            )

    elif store_code == "5":
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"||{'LOJA DE MAGIAS':^{WIDTH-4}}||")
        print(f"||{'-'*(WIDTH-4)}||\n ")

        show_items(MAGIC_ITEMS, "ataque extra")

        option: str = input("\nS - sim\nN - não\nDeseja comprar algum item? ")
        option = validate_option(option)

        if option == "s":
            magic_value: int = 0
            player_items, coins, magic_value = buy_items(
                player_items, MAGIC_ITEMS, coins, magic_value, "ataque extra"
            )
            player_magic += magic_value

    elif store_code == "6":
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"||{'VENDER ITENS':^{WIDTH-4}}||")
        print(f"||{'-'*(WIDTH-4)}||\n")

        if len(player_items) > 0:
            show_player_items(player_items)

            option: str = input("\nS - sim\nN - não\nVender algum item seu? ")
            option = validate_option(option)

            if option == "s":
                player_items, coins, new_stat_value, sold_item_type = sell_items(
                    player_items, coins
                )
                if sold_item_type == 0:
                    player_attack = new_stat_value
                if sold_item_type == 1:
                    player_defense = new_stat_value
                if sold_item_type == 2:
                    player_life_regen = new_stat_value
        else:
            print("\nVOCÊ NÃO TEM ITENS!\n")
            option: str = input("\nS - sim\nN - não\nSair do mercado? ")
            option = validate_option(option)

            if option == "s":
                return (
                    player_items,
                    coins,
                    player_life,
                    player_attack,
                    player_defense,
                    player_life_regen,
                    player_magic,
                )

    elif store_code == "7":
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"||{'SAIR':^{WIDTH-4}}||")
        print(f"||{'-'*(WIDTH-4)}||\n")

        print("Sair do mercado!")

        option: str = input("\nS - sim\nN - não\nQuer mesmo sair? ")
        option = validate_option(option)

        if option == "s":
            print("\nSaindo do mercado...")
            return (
                player_items,
                coins,
                player_life,
                player_attack,
                player_defense,
                player_life_regen,
                player_magic,
            )

    else:
        print("Inválido!")
        clear_screen()

        (
            player_items,
            coins,
            player_life,
            player_attack,
            player_defense,
            player_life_regen,
            player_magic,
        ) = market(
            player_items,
            coins,
            player_life,
            player_attack,
            player_defense,
            player_life_regen,
            player_magic,
        )

    if option == "n":
        clear_screen()

        (
            player_items,
            coins,
            player_life,
            player_attack,
            player_defense,
            player_life_regen,
            player_magic,
        ) = market(
            player_items,
            coins,
            player_life,
            player_attack,
            player_defense,
            player_life_regen,
            player_magic,
        )

    return (
        player_items,
        coins,
        player_life,
        player_attack,
        player_defense,
        player_life_regen,
        player_magic,
    )
