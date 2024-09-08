import time

from clear import clear_screen
from market import market
from fight import fight
from option import validate_option
from storage import save_to_storage


def battle_manager(
    saved_games_count,
    player_name,
    player_items,
    player_life_regen,
    player_life,
    enemy_life,
    player_magic,
    player_attack,
    enemy_attack,
    player_defense,
    enemy_defense,
    coins,
    has_saved_game,
    phase,
):
    clear_screen(100)

    print("||--------##--------##--------##----||")
    print("||             FASE ", phase + 1, "               ||", sep="")
    print("||--------##--------##--------##----||")
    time.sleep(1)

    print()
    print("||--------------------||")
    print("||    VOCÊ")
    print("||    Vida -->", player_life)
    print("||    Ataque -->", player_attack)
    print("||    Defesa -->", player_defense)
    print("||    Magia -->", player_magic)
    print("||    Moedas -->", coins)
    print("||--------------------||")
    print("||    MONSTRO", phase + 1)
    print("||    Vida -->", enemy_life)
    print("||    Ataque -->", enemy_attack)
    print("||    Defesa -->", enemy_defense)
    print("||--------------------||")
    time.sleep(4)

    increase_enemy_power = True
    battle_ended = False
    action = ""
    while action != "1":
        print()
        print("||------------------------||")
        print("||   AÇÕES:               ||")
        print("||   1. Começar Batalha   ||")
        print("||   2. Ir pro Mercado    ||")
        print("||   3. Seu Status        ||")
        print("||   4. Salvar Progresso  ||")
        print("||   5. Sair do Jogo      ||")
        print("||------------------------||")

        action = input("\nAção: ")

        if action == "1":
            print("\nComeçar batalha!")
            option = input("\nQuer mesmo começar a luta?\n(S: sim) ou (N: não): ")
            option = validate_option(option)
            if option == "s":
                print()
                print("||--------------------||")
                print("||       BATALHA      ||")
                print("||--------------------||")
                print()

                player_life,
                player_magic,
                coins,
                phase,
                increase_enemy_power = fight(
                    player_life,
                    enemy_life,
                    player_attack,
                    enemy_attack,
                    player_defense,
                    enemy_defense,
                    player_magic,
                    coins,
                    phase,
                )
                time.sleep(2)
            else:
                action = ""
                clear_screen(10)

        elif action == "2":
            player_items,
            coins,
            player_life,
            player_attack,
            player_defense,
            player_life_regen,
            player_magic = market(
                player_items,
                coins,
                player_life,
                player_attack,
                player_defense,
                player_life_regen,
                player_magic,
            )
            time.sleep(2)
            clear_screen(10)

        elif action == "3":
            clear_screen(10)
            print()
            print("||--------------------||")
            print("||    VOCÊ            ||")
            print("||    Vida -->", player_life)
            print("||    Ataque -->", player_attack)
            print("||    Defesa -->", player_defense)
            print("||    Magia -->", player_magic)
            print("||    Moedas -->", coins)
            print("||--------------------||")
            print("||    MONSTRO", phase + 1)
            print("||    Vida -->", enemy_life)
            print("||    Ataque -->", enemy_attack)
            print("||    Defesa -->", enemy_defense)
            print("||--------------------||")
            time.sleep(1)

            input("Enter para continuar...")

        elif action == "4":
            option = input("\nSalvar o progresso?\n(S: sim) ou (N: não): ")
            option = validate_option(option)

            if option == "s":
                print("\nSalvando seu progresso...")
                time.sleep(1)

                if has_saved_game:
                    # TODO: aqui gera o bug de salvar jogo com arquivo "True"
                    save_to_storage(
                        True,
                        saved_games_count,
                        has_saved_game,
                        "PAUSADO",
                        player_name,
                        phase,
                        player_life,
                        player_life_regen,
                        player_attack,
                        player_defense,
                        player_magic,
                        coins,
                        player_items,
                        enemy_life,
                        enemy_attack,
                        enemy_defense,
                    )
                else:
                    has_saved_game = saved_games_count + 1
                    saved_games_count += 1
                    save_to_storage(
                        True,
                        saved_games_count,
                        has_saved_game,
                        "PAUSADO",
                        player_name,
                        phase,
                        player_life,
                        player_life_regen,
                        player_attack,
                        player_defense,
                        player_magic,
                        coins,
                        player_items,
                        enemy_life,
                        enemy_attack,
                        enemy_defense,
                    )

            clear_screen(10)

        elif action == "5":
            option = input("\nQuer mesmo sair do jogo?\n(S: sim) ou (N: não): ")
            option = validate_option(option)

            if option == "s":
                print("\nSaindo do jogo...")

                print()
                print("||----------------------||")
                print("||                      ||")
                print("||  VOCÊ SAIU DO JOGO!  ||")
                print("||                      ||")
                print("||----------------------||")
                time.sleep(1)

                battle_ended = True
                return (
                    player_items,
                    coins,
                    player_attack,
                    player_defense,
                    player_magic,
                    player_life,
                    player_life_regen,
                    phase,
                    battle_ended,
                    increase_enemy_power,
                )
        else:
            print("\nInválido!")
            time.sleep(1)
            clear_screen(10)

    return (
        player_items,
        coins,
        player_attack,
        player_defense,
        player_magic,
        player_life,
        player_life_regen,
        phase,
        battle_ended,
        increase_enemy_power,
    )
