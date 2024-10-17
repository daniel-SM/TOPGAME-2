from time import sleep

from constants import FRAME_WIDTH  # Importando constante com tamanho dos quadros
from .fight import fight
from market.market import market
from storage.storage import save_to_storage
from utils.clear import clear_screen
from utils.option import validate_option


def battle_manager(
    saved_games_count: int,
    player_name: str,
    player_items: list[tuple[str, str, int, int, str, int]],
    player_life_regen: int,
    player_life: int,
    enemy_life: int,
    player_magic: int,
    player_attack: int,
    enemy_attack: int,
    player_defense: int,
    enemy_defense: int,
    coins: int,
    phase: int,
) -> list[
    tuple[
        list[tuple[str, str, int, int, str, int]],  # player_items
        int,  # coins
        int,  # player_attack
        int,  # player_defense
        int,  # player_magic
        int,  # player_life
        int,  # player_life_regen
        int,  # phase
        bool,  # game_ended
        bool,  # increase_enemy_power
    ]
]:

    clear_screen()

    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    print(f"||{f'FASE {phase + 1}':^{FRAME_WIDTH-4}}||")
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    sleep(1)

    print(f"||{'VOCÊ':^{FRAME_WIDTH-4}}||")
    print(f"|| Vida     {player_life    :>{FRAME_WIDTH-15}} ||")
    print(f"|| Ataque   {player_attack  :>{FRAME_WIDTH-15}} ||")
    print(f"|| Defesa   {player_defense :>{FRAME_WIDTH-15}} ||")
    print(f"|| Magia    {player_magic   :>{FRAME_WIDTH-15}} ||")
    print(f"|| Moedas   {coins          :>{FRAME_WIDTH-15}} ||")
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    print(f"||{'INIMIGO':^{FRAME_WIDTH-4}}||")
    print(f"|| Vida     {enemy_life     :>{FRAME_WIDTH-15}} ||")
    print(f"|| Ataque   {enemy_attack   :>{FRAME_WIDTH-15}} ||")
    print(f"|| Defesa   {enemy_defense  :>{FRAME_WIDTH-15}} ||")
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    sleep(1)

    increase_enemy_power: bool = True
    game_ended: bool = False
    action: str = ""
    while action != "1":
        print()
        print(f"||{'-'*(FRAME_WIDTH-4)}||")
        print(f"||{'AÇÕES':^{FRAME_WIDTH-4}}||")
        print(f"||{' ' * 10}{'1. Começar Batalha':<{FRAME_WIDTH-14}}||")
        print(f"||{' ' * 10}{'2. Ir pro Mercado':<{FRAME_WIDTH-14}}||")
        print(f"||{' ' * 10}{'3. Seu Status':<{FRAME_WIDTH-14}}||")
        print(f"||{' ' * 10}{'4. Salvar Progresso':<{FRAME_WIDTH-14}}||")
        print(f"||{' ' * 10}{'5. Sair do Jogo':<{FRAME_WIDTH-14}}||")
        print(f"||{'-'*(FRAME_WIDTH-4)}||")

        action = input("\nAção: ")

        if action == "1":
            print("\nComeçar batalha!")
            option: str = input("\nS - sim\nN - não\nQuer mesmo começar a luta? ")
            option = validate_option(option)
            if option == "s":
                print()
                print(f"||{'-'*(FRAME_WIDTH-4)}||")
                print(f"||{' '*(FRAME_WIDTH-4)}||")
                print(f"||{'BATALHA':^{FRAME_WIDTH-4}}||")
                print(f"||{' '*(FRAME_WIDTH-4)}||")
                print(f"||{'-'*(FRAME_WIDTH-4)}||")

                (
                    player_life,
                    player_magic,
                    coins,
                    phase,
                    increase_enemy_power,
                ) = fight(
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
                sleep(2)
            else:
                action = ""
                clear_screen()

        elif action == "2":
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
            sleep(1)
            clear_screen()

        elif action == "3":
            clear_screen()

            print(f"||{'-'*(FRAME_WIDTH-4)}||")
            print(f"||{'VOCÊ':^{FRAME_WIDTH-4}}||")
            print(f"|| Vida     {player_life    :>{FRAME_WIDTH-15}} ||")
            print(f"|| Ataque   {player_attack  :>{FRAME_WIDTH-15}} ||")
            print(f"|| Defesa   {player_defense :>{FRAME_WIDTH-15}} ||")
            print(f"|| Magia    {player_magic   :>{FRAME_WIDTH-15}} ||")
            print(f"|| Moedas   {coins          :>{FRAME_WIDTH-15}} ||")
            print(f"||{'-'*(FRAME_WIDTH-4)}||")
            print(f"||{'INIMIGO':^{FRAME_WIDTH-4}}||")
            print(f"|| Vida     {enemy_life     :>{FRAME_WIDTH-15}} ||")
            print(f"|| Ataque   {enemy_attack   :>{FRAME_WIDTH-15}} ||")
            print(f"|| Defesa   {enemy_defense  :>{FRAME_WIDTH-15}} ||")
            print(f"||{'-'*(FRAME_WIDTH-4)}||")
            sleep(1)

            input("\nEnter para continuar... ")
            clear_screen()

        elif action == "4":
            option: str = input("\nS - sim\nN - não\nSalvar o progresso? ")
            option = validate_option(option)

            if option == "s":
                print("\nSalvando seu progresso...")
                sleep(1)

                saved_games_count = save_to_storage(
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

            print("\nProgresso salvo com sucesso!\n")
            sleep(1)

            clear_screen()

        elif action == "5":
            option: str = input("\nS - sim\nN - não\nQuer mesmo sair do jogo? ")
            option = validate_option(option)

            if option == "s":
                print("\nSaindo do jogo...")

                print()
                print(f"||{'-'*(FRAME_WIDTH-4)}||")
                print(f"||{' '*(FRAME_WIDTH-4)}||")
                print(f"||{'VOCÊ SAIU DO JOGO!':^{FRAME_WIDTH-4}}||")
                print(f"||{' '*(FRAME_WIDTH-4)}||")
                print(f"||{'-'*(FRAME_WIDTH-4)}||")
                sleep(1)

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
            sleep(1)
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
