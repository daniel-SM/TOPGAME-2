import time
import random

from damage import calc_damage
from option import validate_option
from suspense import make_suspense


def fight(
    player_life,
    enemy_life,
    player_attack,
    enemy_attack,
    player_defense,
    enemy_defense,
    player_magic,
    coins,
    phase,
):

    if (player_attack - enemy_defense <= 0) and (enemy_attack - player_defense <= 0):
        print("||------------------------||")
        print("||         EMPATE         ||")
        print("||------------------------||")
        print("||   Você e seu inimigo   ||")
        print("||       tem poder        ||")
        print("||     equivalentes!      ||")
        print("||------------------------||")
        time.sleep(1)
        phase -= 1
        return player_life, player_magic, coins, phase, False

    player_turn_counter = 0
    enemy_turn_counter = 0

    while (player_life > 0) and (enemy_life > 0):
        who_plays_next = random.choice([1, 2])

        if player_turn_counter > 1:
            player_turn_counter = 0
            enemy_turn_counter += 1

            if enemy_turn_counter > 1:
                print("\nSeu inimigo novamente!\n")

            print("\nSeu inimigo está atacando!")
            make_suspense(0.3)

            player_life, fight_completed = calc_damage(1, player_life, enemy_attack, player_defense)
            if fight_completed == True:
                break

        if enemy_turn_counter > 1:
            enemy_turn_counter = 0
            player_turn_counter += 1

            if player_turn_counter > 1:
                print("\nVocê novamente!")

            print()
            print("||------------------||")
            print("||     Sua vez!     ||")
            print("||------------------||")
            print("||   AÇÕES:         ||")
            print("||   1. Atacar      ||")
            print("||   2. Usar Magia  ||")
            print("||   3. Defender    ||")
            print("||   4. Fugir       ||")
            print("||------------------||")

            action = input("Ação: ")

            while action not in ["1", "2", "3", "4"]:
                print("Inválido!")
                action = input("Ação: ")

            if action == "1":
                print("\nVocê está atacando!")
                make_suspense(0.3)

                enemy_life, fight_completed = calc_damage(0, enemy_life, player_attack, enemy_defense)
            elif action == "2":
                print("\nVocê está atacando!")
                print("Sua magia é", player_magic)
                make_suspense(0.3)

                enemy_life, fight_completed = calc_damage(0, enemy_life, player_attack, enemy_defense, player_magic)
                player_magic = 0
            elif action == "3":
                who_plays_next = 2
            elif action == "4":
                option = input("\nQuer mesmo fugir?\n(S: sim) ou (N: não): ")
                option = validate_option(option)

                if option == "s":
                    phase -= 1

                    print()
                    print("||---------------------------||")
                    print("||           FUGIU           ||")
                    print("||---------------------------||")
                    print("||  Você fugiu da batalha!   ||")
                    print("||  Você perdeu 100 moedas!  ||")
                    print("||---------------------------||")

                    if coins > 100:
                        coins -= 100
                    else:
                        coins = 0
                    print("||  Você tem", coins, "moedas")
                    print("||---------------------------||")

                    return player_life, player_magic, coins, phase, True

            if fight_completed == True:
                break

        if who_plays_next == 1:
            enemy_turn_counter = 0
            player_turn_counter += 1

            if player_turn_counter > 1:
                print("\nVocê novamente!")

            print()
            print("||------------------||")
            print("||     Sua vez!     ||")
            print("||------------------||")
            print("||   AÇÕES:         ||")
            print("||   1. Atacar      ||")
            print("||   2. Usar Magia  ||")
            print("||   3. Defender    ||")
            print("||   4. Fugir       ||")
            print("||------------------||")

            action = input("\nAção: ")

            while action not in ["1", "2", "3", "4"]:
                print("Inválido!")
                action = input("\nAção: ")

            if action == "1":
                print("\nVocê está atacando!")
                make_suspense(0.3)

                enemy_life, fight_completed = calc_damage(0, enemy_life, player_attack, enemy_defense)
            elif action == "2":
                print("\nVocê está atacando!")
                print("Sua player_magic é", player_magic)
                make_suspense(0.3)

                enemy_life, fight_completed = calc_damage(0, enemy_life, player_attack, enemy_defense, player_magic)
                player_magic = 0
            elif action == "3":
                who_plays_next = 2
                fight_completed = False
            elif action == "4":
                option = input("\nQuer mesmo fugir?\n(S - sim) ou (N - não): ")
                option = validate_option(option)

                if option == "s":
                    phase -= 1

                    print()
                    print("||---------------------------||")
                    print("||           FUGIU           ||")
                    print("||---------------------------||")
                    print("||  Você fugiu da batalha!   ||")
                    print("||  Você perdeu 100 moedas!  ||")
                    print("||---------------------------||")

                    if coins > 100:
                        coins -= 100
                    else:
                        coins = 0

                    print("||  Você tem", coins, "moedas")
                    print("||---------------------------||")

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
            
            player_life, fight_completed = calc_damage(1, player_life, enemy_attack, player_defense)

            if fight_completed:
                break

    return player_life, player_magic, coins, phase, True
