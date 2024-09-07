import time
import random

from damage import calculate_attack
from option import validate_option
from suspense import make_suspense


def fight(life, life_inim, ataque, ataque_inim, defesa, defesa_inim, magia, moedas, i):

    if (ataque - defesa_inim <= 0) and (ataque_inim - defesa <= 0):
        print("""
        ||------------------------||
        ||         EMPATE         ||
        ||------------------------||
        ||   Você e seu inimigo   ||
        ||  tem ataque e defesa   ||
        ||      equivalentes!     ||
        ||------------------------||
        """)
        time.sleep(1)
        i -= 1
        return life, magia, moedas, i, False

    jogs = 0
    jogs_inim = 0

    while (life > 0) and (life_inim > 0):

        sorteio = random.choice([1, 2])

        if jogs > 1:
            jogs = 0
            jogs_inim += 1
            if jogs_inim > 1:
                print("\nSeu inimigo novamente!\n")
            print("\nSeu inimigo está atacando!")
            make_suspense(0.3)
            life, fim = calculate_attack(1, life, ataque_inim, defesa)
            if fim == True:
                break

        if jogs_inim > 1:
            jogs_inim = 0
            jogs += 1

            if jogs > 1:
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

            acao = input("Ação: ")

            while acao not in ["1", "2", "3", "4"]:
                print("Inválido!")
                acao = input("Ação: ")

            if acao == "1":
                print("\nVocê está atacando!")
                make_suspense(0.3)
                life_inim, fim = calculate_attack(0, life_inim, ataque, defesa_inim)
            elif acao == "2":
                print("\nVocê está atacando!")
                print("Sua magia é", magia)
                make_suspense(0.3)
                life_inim, fim = calculate_attack(
                    0, life_inim, ataque, defesa_inim, magia
                )
                magia = 0
            elif acao == "3":
                sorteio = 2
            elif acao == "4":
                desejo = input("\nQuer mesmo fugir?\n(S: sim) ou (N: não): ")
                desejo = validate_option(desejo)
                if desejo == "s":
                    i -= 1
                    print()
                    print("||---------------------------||")
                    print("||           FUGIU           ||")
                    print("||---------------------------||")
                    print("||  Você fugiu da fight!   ||")
                    print("||  Você perdeu 100 moedas!  ||")
                    print("||---------------------------||")
                    if moedas > 100:
                        moedas -= 100
                    else:
                        moedas = 0
                    print("||  Você tem", moedas, "moedas")
                    print("||---------------------------||")

                    return life, magia, moedas, i, True
            if fim == True:
                break

        if sorteio == 1:
            jogs_inim = 0
            jogs += 1
            if jogs > 1:
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

            acao = input("\nAção: ")

            while acao not in ["1", "2", "3", "4"]:
                print("Inválido!")
                acao = input("\nAção: ")
            if acao == "1":
                print("\nVocê está atacando!")
                make_suspense(0.3)
                life_inim, fim = calculate_attack(0, life_inim, ataque, defesa_inim)
            elif acao == "2":
                print("\nVocê está atacando!")
                print("Sua magia é", magia)
                make_suspense(0.3)
                life_inim, fim = calculate_attack(
                    0, life_inim, ataque, defesa_inim, magia
                )
                magia = 0
            elif acao == "3":
                sorteio = 2
                fim = False
            elif acao == "4":
                desejo = input("\nQuer mesmo fugir?\n(S - sim) ou (N - não): ")
                desejo = validate_option(desejo)
                if desejo == "s":
                    i -= 1
                    print()
                    print("||---------------------------||")
                    print("||           FUGIU           ||")
                    print("||---------------------------||")
                    print("||  Você fugiu da fight!   ||")
                    print("||  Você perdeu 100 moedas!  ||")
                    print("||---------------------------||")
                    if moedas > 100:
                        moedas -= 100
                    else:
                        moedas = 0
                    print("||  Você tem", moedas, "moedas")
                    print("||---------------------------||")

                    return life, magia, moedas, i, True
            if fim == True:
                break

        if sorteio == 2:
            jogs = 0
            jogs_inim += 1
            if jogs_inim > 1:
                print("\nSeu inimigo novamente!")
            print("\nSeu inimigo está atacando!")
            make_suspense(0.3)
            life, fim = calculate_attack(1, life, ataque_inim, defesa)
            if fim:
                break

    return life, magia, moedas, i, True
