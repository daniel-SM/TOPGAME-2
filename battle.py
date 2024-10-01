import time

from market import market
from fight import fight
from clear import clear_screen
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
    phase,
):
    clear_screen()

    # Definindo a largura dos quadros
    width = 40

    print(f"||{'-'*(width-4)}||")
    print(f"||{f'FASE {phase + 1}':^{width-4}}||")
    print(f"||{'-'*(width-4)}||")
    time.sleep(1)

    print(f"||{'VOCÊ':^{width-4}}||")
    print(f"|| Vida     {player_life    :>{width-15}} ||")
    print(f"|| Ataque   {player_attack  :>{width-15}} ||")
    print(f"|| Defesa   {player_defense :>{width-15}} ||")
    print(f"|| Magia    {player_magic   :>{width-15}} ||")
    print(f"|| Moedas   {coins          :>{width-15}} ||")
    print(f"||{'-'*(width-4)}||")
    print(f"||{'INIMIGO':^{width-4}}||")
    print(f"|| Vida     {enemy_life     :>{width-15}} ||")
    print(f"|| Ataque   {enemy_attack   :>{width-15}} ||")
    print(f"|| Defesa   {enemy_defense  :>{width-15}} ||")
    print(f"||{'-'*(width-4)}||")
    time.sleep(1)

    increase_enemy_power = True
    game_ended = False
    action = ""
    while action != "1":
        print()
        print(f"||{'-'*(width-4)}||")
        print(f"||{'AÇÕES':^{width-4}}||")
        print(f"||{' ' * 10}{'1. Começar Batalha':<{width-14}}||")
        print(f"||{' ' * 10}{'2. Ir pro Mercado':<{width-14}}||")
        print(f"||{' ' * 10}{'3. Seu Status':<{width-14}}||")
        print(f"||{' ' * 10}{'4. Salvar Progresso':<{width-14}}||")
        print(f"||{' ' * 10}{'5. Sair do Jogo':<{width-14}}||")
        print(f"||{'-'*(width-4)}||")

        action = input("\nAção: ")

        if action == "1":
            print("\nComeçar batalha!")
            option = input("\nS - sim\nN - não\nQuer mesmo começar a luta? ")
            option = validate_option(option)
            if option == "s":
                print()
                print(f"||{'-'*(width-4)}||")
                print(f"||{' '*(width-4)}||")
                print(f"||{'BATALHA':^{width-4}}||")
                print(f"||{' '*(width-4)}||")
                print(f"||{'-'*(width-4)}||")

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
                clear_screen()

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
            time.sleep(1)
            clear_screen()

        elif action == "3":
            clear_screen()

            print(f"||{'-'*(width-4)}||")
            print(f"||{'VOCÊ':^{width-4}}||")
            print(f"|| Vida     {player_life    :>{width-15}} ||")
            print(f"|| Ataque   {player_attack  :>{width-15}} ||")
            print(f"|| Defesa   {player_defense :>{width-15}} ||")
            print(f"|| Magia    {player_magic   :>{width-15}} ||")
            print(f"|| Moedas   {coins          :>{width-15}} ||")
            print(f"||{'-'*(width-4)}||")
            print(f"||{'INIMIGO':^{width-4}}||")
            print(f"|| Vida     {enemy_life     :>{width-15}} ||")
            print(f"|| Ataque   {enemy_attack   :>{width-15}} ||")
            print(f"|| Defesa   {enemy_defense  :>{width-15}} ||")
            print(f"||{'-'*(width-4)}||")
            time.sleep(1)

            input("\nEnter para continuar... ")
            clear_screen()

        elif action == "4":
            option = input("\nS - sim\nN - não\nSalvar o progresso? ")
            option = validate_option(option)

            if option == "s":
                print("\nSalvando seu progresso...")
                time.sleep(1)

                save_to_storage(
                    saved_games_count,
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

            clear_screen()

        elif action == "5":
            option = input("\nS - sim\nN - não\nQuer mesmo sair do jogo? ")
            option = validate_option(option)

            if option == "s":
                print("\nSaindo do jogo...")

                print()
                print(f"||{'-'*(width-4)}||")
                print(f"||{' '*(width-4)}||")
                print(f"||{'VOCÊ SAIU DO JOGO!':^{width-4}}||")
                print(f"||{' '*(width-4)}||")
                print(f"||{'-'*(width-4)}||")
                time.sleep(1)

                game_ended = True
                return (
                    player_items,
                    coins,
                    player_attack,
                    player_defense,
                    player_magic,
                    player_life,
                    player_life_regen,
                    phase,
                    game_ended,
                    increase_enemy_power,
                )

        else:
            print("\nInválido!")
            time.sleep(1)
            clear_screen()

    return (
        player_items,
        coins,
        player_attack,
        player_defense,
        player_magic,
        player_life,
        player_life_regen,
        phase,
        game_ended,
        increase_enemy_power,
    )
