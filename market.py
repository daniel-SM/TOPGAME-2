import time

from clear import clear_screen
from option import validate_option
from show_items import show_items
from show_player_items import show_purchased_items
from buy import buy_items
from sell import sell_items
from items import attack_items, defense_items, potion_items, regen_items, magic_items


def market(itens_person, moedas, life, ataque, defesa, life_regen, magia):
    clear_screen(100)
    print("\n||-------##-------##------##------||")
    print("||      BEM-VINDO AO MERCADO      ||")
    print("||-------##-------##------##------||")
    time.sleep(1)

    print("||      Você tem", moedas, "moedas.")
    print("||--------------------------------||")
    time.sleep(1)

    print("\n||--------------------------||")
    print("||   LOJAS                  ||")
    print("||   1. Loja de Armas       ||")
    print("||   2. Loja de Escudos     ||")
    print("||   3. Loja de Poções      ||")
    print("||   4. Loja de Armaduras   ||")
    print("||   5. Loja de Magias      ||")
    print("||   6. Vender Itens        ||")
    print("||   7. Sair                ||")
    print("||--------------------------||")

    loja = input("\nNumº da loja: ")

    while loja not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Inválido!")
        loja = input("Numº da loja: ")

    clear_screen(10)

    if loja == "1":
        print("||--------------------||")
        print("||    LOJA DE ARMAS   ||")
        print("||--------------------||\n")

        show_items(attack_items, "ataque")
        desejo = input("\nComprar algum item?\n(S: sim) ou (N: não): ")
        desejo = validate_option(desejo)
        if desejo == "s":
            itens_person, moedas, ataque = buy_items(
                itens_person, attack_items, moedas, ataque, "ataque", 0, True
            )

    elif loja == "2":
        print("||--------------------||")
        print("||  LOJA DE ESCUDOS   ||")
        print("||--------------------||\n")

        show_items(defense_items, "defesa")
        desejo = input("\nComprar algum item?\n(S: sim) ou (N: não): ")
        desejo = validate_option(desejo)
        if desejo == "s":
            itens_person, moedas, defesa = buy_items(
                itens_person, defense_items, moedas, defesa, "defesa", 1, True
            )

    elif loja == "3":
        print("||--------------------||")
        print("||   LOJA DE POÇÕES   ||")
        print("||--------------------||\n")

        show_items(potion_items, "vida a mais")
        desejo = input("\nComprar algum item?\n(S: sim) ou (N: não): ")
        desejo = validate_option(desejo)
        if desejo == "s":
            poder = 0
            itens_person, moedas, poder = buy_items(
                itens_person, potion_items, moedas, poder, "vida a mais"
            )
            life += poder

    elif loja == "4":
        print("||---------------------||")
        print("||  LOJA DE ARMADURAS  ||")
        print("||---------------------||\n")

        show_items(regen_items, "vida p/ fase")
        desejo = input("\nComprar algum item?\n(S: sim) ou (N: não): ")
        desejo = validate_option(desejo)
        if desejo == "s":
            itens_person, moedas, life_regen = buy_items(
                itens_person, regen_items, moedas, life_regen, "vida p/ fase", 2, True
            )

    elif loja == "5":
        print("||--------------------||")
        print("||   LOJA DE MAGIAS   ||")
        print("||--------------------||\n ")

        show_items(magic_items, "ataque extra")
        desejo = input("\nComprar algum item?\n(S: sim) ou (N: não): ")
        desejo = validate_option(desejo)
        if desejo == "s":
            poder = 0
            itens_person, moedas, poder = buy_items(
                itens_person, magic_items, moedas, poder, "ataque extra"
            )
            magia += poder

    elif loja == "6":
        print("||--------------------||")
        print("||    VENDER ITENS    ||")
        print("||--------------------||\n")

        if len(itens_person) > 0:
            show_purchased_items(itens_person)
            desejo = input("\nVender algum item seu?\n(S: sim) ou (N: não): ")
            desejo = validate_option(desejo)
            if desejo == "s":
                itens_person, moedas, poder, tipo = sell_items(itens_person, moedas)
                if tipo == 0:
                    ataque = poder
                elif tipo == 1:
                    defesa = poder
                elif tipo == 2:
                    life_regen = poder
        else:
            print("\nVOCÊ NÃO TEM ITENS!!!\n")
            desejo = input("Sair do mercado?\n(S: sim) ou (N: não): ")
            desejo = validate_option(desejo)
            if desejo == "s":
                return itens_person, moedas, life, ataque, defesa, life_regen, magia

    elif loja == "7":
        print("||--------------------||")
        print("||        SAIR        ||")
        print("||--------------------||\n")

        print("Sair do mercado!\n")
        desejo = input("Quer mesmo sair?\n(S: sim) ou (N: não): ")
        desejo = validate_option(desejo)
        if desejo == "s":
            print("\nSaindo do mercado...")
            return itens_person, moedas, life, ataque, defesa, life_regen, magia
    else:
        print("Inválido!")
        clear_screen(100)
        itens_person, moedas, life, ataque, defesa, life_regen, magia = market(
            itens_person, moedas, life, ataque, defesa, life_regen, magia
        )

    if desejo == "n":
        clear_screen(100)
        itens_person, moedas, life, ataque, defesa, life_regen, magia = market(
            itens_person, moedas, life, ataque, defesa, life_regen, magia
        )

    return itens_person, moedas, life, ataque, defesa, life_regen, magia
