import random

from ..utils.suspense import make_suspense


def calc_damage(
    current_attacker: int,
    life_value: int,
    attack_value: int,
    defense_value: int,
    magic_value: int = 0,
) -> tuple[
    int,  # player_life
    bool,  # fight_completed
]:

    # iniciando variavel de controle da luta
    fight_completed: bool = False

    # Sorteando possíveis divisores com pesos
    random_result: list[int] = random.choices(
        population=[1, 2, 5, 10], weights=[1, 4, 6, 1]
    )
    damage_divisor: int = random_result[0]

    # Sorteando possíveis multiplicadores com pesos
    random_result: list[int] = random.choices(population=[0, 1], weights=[1, 19])
    damage_multiplier: int = random_result[0]

    attack_vs_defense: int = attack_value - defense_value

    if attack_vs_defense > 0:
        # calculando o dano causado
        damage: int = (attack_vs_defense // damage_divisor) * damage_multiplier
        # adicionando dano de magica
        damage += magic_value
        # subtraindo o valor do dano
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
        damage: int = magic_value
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
