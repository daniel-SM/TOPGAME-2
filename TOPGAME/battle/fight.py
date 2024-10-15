import time
import random

from damage import calc_damage
from ..utils.option import validate_option
from ..utils.suspense import make_suspense


def fight(
    player_life: int,
    enemy_life: int,
    player_attack: int,
    enemy_attack: int,
    player_defense: int,
    enemy_defense: int,
    player_magic: int,
    coins: int,
    phase: int,
) -> tuple[
    int,  # player_life
    int,  # player_magic
    int,  # coins
    int,  # phase
    bool,  # increase_enemy_power
]:
    # Definindo o tamanho da largura do quadro
    WIDTH: int = 40

    if (player_attack - enemy_defense <= 0) and (enemy_attack - player_defense <= 0):
        print()
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"||{'EMPATE':^{WIDTH-4}}||")
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"||{'Seu inimigo e você':^{WIDTH-4}}||")
        print(f"||{'tem poder equivalentes!':^{WIDTH-4}}||")
        print(f"||{'-'*(WIDTH-4)}||")
        time.sleep(1)
        phase -= 1
        return player_life, player_magic, coins, phase, False

    player_turn_counter: int = 0
    enemy_turn_counter: int = 0

    while (player_life > 0) and (enemy_life > 0):
        # iniciando variavel de controle do fim da luta
        fight_completed: bool = False

        who_plays_next: int = random.choice([1, 2])

        if player_turn_counter > 1:
            player_turn_counter = 0
            enemy_turn_counter += 1

            if enemy_turn_counter > 1:
                print("\nSeu inimigo novamente!\n")

            print("\nSeu inimigo está atacando!")
            make_suspense(0.3)

            player_life, fight_completed = calc_damage(
                1, player_life, enemy_attack, player_defense
            )
            if fight_completed == True:
                break

        if enemy_turn_counter > 1:
            enemy_turn_counter = 0
            player_turn_counter += 1

            if player_turn_counter > 1:
                print("\nVocê novamente!")

            print()
            print(f"||{'-'*(WIDTH-4)}||")
            print(f"||{'SUA VEZ':^{WIDTH-4}}||")
            print(f"||{'-'*(WIDTH-4)}||")
            print(f"||{'AÇÕES':^{WIDTH-4}}||")
            print(f"||{' ' * 10}{'1. Atacar':<{WIDTH-14}}||")
            print(f"||{' ' * 10}{'2. Usar Magia':<{WIDTH-14}}||")
            print(f"||{' ' * 10}{'3. Defender':<{WIDTH-14}}||")
            print(f"||{' ' * 10}{'4. Fugir':<{WIDTH-14}}||")
            print(f"||{'-'*(WIDTH-4)}||")

            action: str = input("\nAção: ")

            while action not in ["1", "2", "3", "4"]:
                print("Inválido!")
                action = input("Ação: ")

            if action == "1":
                print("\nVocê está atacando!")
                make_suspense(0.3)

                enemy_life, fight_completed = calc_damage(
                    0, enemy_life, player_attack, enemy_defense
                )
            elif action == "2":
                print("\nVocê está atacando!")
                print("Sua magia é", player_magic)
                make_suspense(0.3)

                enemy_life, fight_completed = calc_damage(
                    0, enemy_life, player_attack, enemy_defense, player_magic
                )
                player_magic = 0
            elif action == "3":
                who_plays_next = 2
            elif action == "4":
                option: str = input("\nS - sim\nN - não\nQuer mesmo fugir? ")
                option = validate_option(option)

                if option == "s":
                    phase -= 1

                    print()
                    print(f"||{'-'*(WIDTH-4)}||")
                    print(f"||{'FUGIU':^{WIDTH-4}}||")
                    print(f"||{'-'*(WIDTH-4)}||")
                    print(f"||{'Você fugiu da batalha!':^{WIDTH-4}}||")
                    print(f"||{'Você perdeu 100 moedas!':^{WIDTH-4}}||")
                    print(f"||{'-'*(WIDTH-4)}||")

                    if coins > 100:
                        coins -= 100
                    else:
                        coins = 0

                    print(f"||{f'Você tem {coins} moedas':^{WIDTH-4}}||")
                    print(f"||{'-'*(WIDTH-4)}||")

                    return player_life, player_magic, coins, phase, True

            if fight_completed == True:
                break

        if who_plays_next == 1:
            enemy_turn_counter = 0
            player_turn_counter += 1

            if player_turn_counter > 1:
                print("\nVocê novamente!")

            print()
            print(f"||{'-'*(WIDTH-4)}||")
            print(f"||{'SUA VEZ':^{WIDTH-4}}||")
            print(f"||{'-'*(WIDTH-4)}||")
            print(f"||{'AÇÕES':^{WIDTH-4}}||")
            print(f"||{' ' * 10}{'1. Atacar':<{WIDTH-14}}||")
            print(f"||{' ' * 10}{'2. Usar Magia':<{WIDTH-14}}||")
            print(f"||{' ' * 10}{'3. Defender':<{WIDTH-14}}||")
            print(f"||{' ' * 10}{'4. Fugir':<{WIDTH-14}}||")
            print(f"||{'-'*(WIDTH-4)}||")

            action: str = input("\nAção: ")

            while action not in ["1", "2", "3", "4"]:
                print("Inválido!")
                action = input("\nAção: ")

            if action == "1":
                print("\nVocê está atacando!")
                make_suspense(0.3)

                enemy_life, fight_completed = calc_damage(
                    0, enemy_life, player_attack, enemy_defense
                )
            elif action == "2":
                print("\nVocê está atacando!")
                print("Sua magia é", player_magic)
                make_suspense(0.3)

                enemy_life, fight_completed = calc_damage(
                    0, enemy_life, player_attack, enemy_defense, player_magic
                )
                player_magic = 0
            elif action == "3":
                who_plays_next = 2
                fight_completed = False
            elif action == "4":
                option: str = input("\nS - sim\nN - não\nQuer mesmo fugir? ")
                option = validate_option(option)

                if option == "s":
                    phase -= 1

                    print()
                    print(f"||{'-'*(WIDTH-4)}||")
                    print(f"||{'FUGIU':^{WIDTH-4}}||")
                    print(f"||{'-'*(WIDTH-4)}||")
                    print(f"||{'Você fugiu da batalha!':^{WIDTH-4}}||")
                    print(f"||{'Você perdeu 100 moedas!':^{WIDTH-4}}||")
                    print(f"||{'-'*(WIDTH-4)}||")

                    if coins > 100:
                        coins -= 100
                    else:
                        coins = 0

                    print(f"||{f'Você tem {coins} moedas':^{WIDTH-4}}||")
                    print(f"||{'-'*(WIDTH-4)}||")

                    return player_life, player_magic, coins, phase, True
            if fight_completed == True:
                break

        if who_plays_next == 2:
            player_turn_counter = 0
            enemy_turn_counter += 1

            if enemy_turn_counter > 1:
                print("\nSeu inimigo novamente!")

            print("\nSeu inimigo está atacando!")
            make_suspense(0.3)

            player_life, fight_completed = calc_damage(
                1, player_life, enemy_attack, player_defense
            )

            if fight_completed:
                break

    return player_life, player_magic, coins, phase, True
