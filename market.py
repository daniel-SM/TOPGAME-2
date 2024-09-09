import time

from clear import clear_screen
from option import validate_option
from show_items import show_items
from show_player_items import show_player_items
from buy import buy_items
from sell import sell_items
from items import ATTACK_ITEMS, DEFENSE_ITEMS, POTION_ITEMS, REGEN_ITEMS, MAGIC_ITEMS


def market(
    player_items,
    coins,
    player_life,
    player_attack,
    player_defense,
    player_life_regen,
    player_magic,
):
    clear_screen()
    print()
    print("||-------##-------##------##------||")
    print("||                                ||")
    print("||      BEM-VINDO AO MERCADO      ||")
    print("||                                ||")
    print("||-------##-------##------##------||")
    time.sleep(1)

    print("||      Você tem", coins, "moedas.")
    print("||--------------------------------||")
    time.sleep(1)

    print()
    print("||--------------------------||")
    print("||   LOJAS                  ||")
    print("||   1. Loja de Armas       ||")
    print("||   2. Loja de Escudos     ||")
    print("||   3. Loja de Poções      ||")
    print("||   4. Loja de Armaduras   ||")
    print("||   5. Loja de Magias      ||")
    print("||   6. Vender Itens        ||")
    print("||   7. Sair                ||")
    print("||--------------------------||")

    store_code = input("\nNúmero da loja: ")

    while store_code not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Inválido!")
        store_code = input("Número da loja: ")

    clear_screen()

    if store_code == "1":
        print("||--------------------||")
        print("||    LOJA DE ARMAS   ||")
        print("||--------------------||")
        print()

        show_items(ATTACK_ITEMS, "ataque")
        option = input("\nS - sim\nN - não\nDeseja comprar algum item? ")
        option = validate_option(option)

        if option == "s":
            player_items, coins, player_attack = buy_items(
                player_items, ATTACK_ITEMS, coins, player_attack, "ataque", 0, True
            )

    elif store_code == "2":
        print("||--------------------||")
        print("||  LOJA DE ESCUDOS   ||")
        print("||--------------------||\n")

        show_items(DEFENSE_ITEMS, "defesa")
        option = input("\nS - sim\nN - não\nDeseja comprar algum item? ")
        option = validate_option(option)

        if option == "s":
            player_items, coins, player_defense = buy_items(
                player_items, DEFENSE_ITEMS, coins, player_defense, "defesa", 1, True
            )

    elif store_code == "3":
        print("||--------------------||")
        print("||   LOJA DE POÇÕES   ||")
        print("||--------------------||\n")

        show_items(POTION_ITEMS, "vida a mais")

        option = input("\nS - sim\nN - não\nDeseja comprar algum item? ")
        option = validate_option(option)

        if option == "s":
            potion_value = 0
            player_items, coins, potion_value = buy_items(
                player_items, POTION_ITEMS, coins, potion_value, "vida a mais"
            )
            player_life += potion_value

    elif store_code == "4":
        print("||---------------------||")
        print("||  LOJA DE ARMADURAS  ||")
        print("||---------------------||\n")

        show_items(REGEN_ITEMS, "vida p/ fase")
        
        option = input("\nS - sim\nN - não\nDeseja comprar algum item? ")
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
        print("||--------------------||")
        print("||   LOJA DE MAGIAS   ||")
        print("||--------------------||\n ")

        show_items(MAGIC_ITEMS, "ataque extra")
        
        option = input("\nS - sim\nN - não\nDeseja comprar algum item? ")
        option = validate_option(option)
        
        if option == "s":
            magic_value = 0
            player_items, coins, magic_value = buy_items(
                player_items, MAGIC_ITEMS, coins, magic_value, "ataque extra"
            )
            player_magic += magic_value

    elif store_code == "6":
        print("||--------------------||")
        print("||    VENDER ITENS    ||")
        print("||--------------------||\n")

        if len(player_items) > 0:
            show_player_items(player_items)
        
            option = input("\nVender algum item seu?\n(S: sim) ou (N: não): ")
            option = validate_option(option)
        
            if option == "s":
                player_items, coins, new_stat_value, sold_item_type = sell_items(player_items, coins)
                if sold_item_type == 0:
                    player_attack = new_stat_value
                if sold_item_type == 1:
                    player_defense = new_stat_value
                if sold_item_type == 2:
                    player_life_regen = new_stat_value
        else:
            print("\nVOCÊ NÃO TEM ITENS!\n")
            option = input("Sair do mercado?\n(S: sim) ou (N: não): ")
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
        print("||--------------------||")
        print("||        SAIR        ||")
        print("||--------------------||\n")

        print("Sair do mercado!\n")
        
        option = input("Quer mesmo sair?\n(S: sim) ou (N: não): ")
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
