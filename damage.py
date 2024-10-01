import random

from suspense import make_suspense


def calc_damage(
    current_attacker, life_value, attack_value, defense_value, magic_value=0
):
    fight_completed = False

    # Sorteando possíveis divisores com pesos
    random_result = random.choices(population=[1, 2, 5, 10], weights=[1, 4, 6, 1])
    damage_divisor = random_result[0]

    # Sorteando possíveis multiplicadores com pesos
    random_result = random.choices(population=[0, 1], weights=[1, 19])
    damage_multiplier = random_result[0]

    attack_vs_defense = attack_value - defense_value

    if attack_vs_defense > 0:
        damage = (attack_vs_defense // damage_divisor) * damage_multiplier + magic_value
        life_value -= damage

        if damage > 0:
            if current_attacker == 0:
                print("\nO dano do seu ataque foi", damage)
                if life_value > 0:
                    print("A vida atual do seu inimigo é", life_value)
                    make_suspense(0.5)
                else:
                    print("\nSEU INIMIGO MORREU!\nVOCÊ VENCEU!\n")
                    fight_completed = True
            else:
                print("\nO dano sofrido foi", damage)
                if life_value > 0:
                    print("Sua vida atual é", life_value)
                    make_suspense(0.5)
                else:
                    print("\nVOCÊ MORREU!\n")
                    fight_completed = True

        else:
            if current_attacker == 0:
                print("O seu ataque falhou!")
                print("Seu inimigo não teve dano!")
                print("A vida atual do seu inimigo é", life_value)
                make_suspense(0.6)
            else:
                print("O ataque do seu inimigo falhou!")
                print("Você não teve dano!")
                print("Sua vida atual é", life_value)
                make_suspense(0.6)
    elif magic_value > 0:
        damage = magic_value
        life_value -= damage

        if damage > 0:
            if current_attacker == 0:
                print("\nO dano do seu ataque foi", damage)
                if life_value > 0:
                    print("A vida atual do seu inimigo é", life_value)
                    make_suspense(0.5)
                else:
                    print("\nSEU INIMIGO MORREU!\nVOCÊ VENCEU!\n")
                    fight_completed = True
            else:
                print("\nO dano sofrido foi", damage)
                if life_value > 0:
                    print("Sua vida atual é", life_value)
                    make_suspense(0.5)
                else:
                    print("\nVOCÊ MORREU!\n")
                    fight_completed = True
    else:
        if current_attacker == 0:
            print("O seu ataque falhou!")
            print("Seu inimigo não teve dano!")
            print("A vida atual do seu inimigo é", life_value)
            make_suspense(0.6)
        else:
            print("O ataque do seu inimigo falhou!")
            print("Você não teve dano!")
            print("Sua vida atual é", life_value)
            make_suspense(0.6)

    return life_value, fight_completed
