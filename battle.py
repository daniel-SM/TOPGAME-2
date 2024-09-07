import time

from clear import clear_screen
from market import market
from fight import fight
from option import validate_option
from storage import save_to_storage


def battle_manager(
    qtd_jogos,
    nome,
    itens_person,
    life_regen,
    life,
    life_inim,
    magia,
    ataque,
    ataque_inim,
    defesa,
    defesa_inim,
    moedas,
    jogo_salvo,
    n,
):
    clear_screen(100)

    print("||--------##--------##--------##----||")
    print("||             FASE ", n + 1, "               ||", sep="")
    print("||--------##--------##--------##----||")
    time.sleep(1)

    print()
    print("||--------------------||")
    print("||    VOCÊ")
    print("||    Vida -->", life)
    print("||    Ataque -->", ataque)
    print("||    Defesa -->", defesa)
    print("||    Magia -->", magia)
    print("||    Moedas -->", moedas)
    print("||--------------------||")
    print("||    MONSTRO", n + 1)
    print("||    Vida -->", life_inim)
    print("||    Ataque -->", ataque_inim)
    print("||    Defesa -->", defesa_inim)
    print("||--------------------||")
    time.sleep(4)

    aumentar = True
    fim = False
    acao = ""
    while acao != "1":
        print()
        print("||------------------------||")
        print("||   AÇÕES:               ||")
        print("||   1. Começar Batalha   ||")
        print("||   2. Ir pro Mercado    ||")
        print("||   3. Seu Status        ||")
        print("||   4. Salvar Progresso  ||")
        print("||   5. Sair do Jogo      ||")
        print("||------------------------||")

        acao = input("\nAção: ")

        if acao == "1":
            print("\nComeçar batalha!")
            desejo = input("\nQuer mesmo começar a luta?\n(S: sim) ou (N: não): ")
            desejo = validate_option(desejo)
            if desejo == "s":
                print()
                print("||--------------------||")
                print("||       BATALHA      ||")
                print("||--------------------||")
                print()

                life,
                magia,
                moedas,
                n,
                aumentar = fight(
                    life,
                    life_inim,
                    ataque,
                    ataque_inim,
                    defesa,
                    defesa_inim,
                    magia,
                    moedas,
                    n,
                )
                time.sleep(2)
            else:
                acao = ""
                clear_screen(10)

        elif acao == "2":
            itens_person,
            moedas,
            life,
            ataque,
            defesa,
            life_regen,
            magia = market(
                itens_person, moedas, life, ataque, defesa, life_regen, magia
            )
            time.sleep(2)
            clear_screen(10)

        elif acao == "3":
            clear_screen(10)
            print()
            print("||--------------------||")
            print("||    VOCÊ            ||")
            print("||    Vida -->", life)
            print("||    Ataque -->", ataque)
            print("||    Defesa -->", defesa)
            print("||    Magia -->", magia)
            print("||    Moedas -->", moedas)
            print("||--------------------||")
            print("||    MONSTRO", n + 1)
            print("||    Vida -->", life_inim)
            print("||    Ataque -->", ataque_inim)
            print("||    Defesa -->", defesa_inim)
            print("||--------------------||")
            time.sleep(1)

            input("Enter para continuar...")

        elif acao == "4":
            desejo = input("\nSalvar o progresso?\n(S: sim) ou (N: não): ")
            desejo = validate_option(desejo)

            if desejo == "s":
                print("\nSalvando seu progresso...")
                time.sleep(1)

                if jogo_salvo:
                    save_to_storage(
                        True,
                        qtd_jogos,
                        jogo_salvo,
                        "PAUSADO",
                        nome,
                        n,
                        life,
                        life_regen,
                        ataque,
                        defesa,
                        magia,
                        moedas,
                        itens_person,
                        life_inim,
                        ataque_inim,
                        defesa_inim,
                    )
                else:
                    jogo_salvo = qtd_jogos + 1
                    qtd_jogos += 1
                    save_to_storage(
                        True,
                        qtd_jogos,
                        jogo_salvo,
                        "PAUSADO",
                        nome,
                        n,
                        life,
                        life_regen,
                        ataque,
                        defesa,
                        magia,
                        moedas,
                        itens_person,
                        life_inim,
                        ataque_inim,
                        defesa_inim,
                    )

            clear_screen(10)

        elif acao == "5":
            desejo = input("\nQuer mesmo sair do jogo?\n(S: sim) ou (N: não): ")
            desejo = validate_option(desejo)

            if desejo == "s":
                print("\nSaindo do jogo...")

                print()
                print("||----------------------||")
                print("||                      ||")
                print("||  VOCÊ SAIU DO JOGO!  ||")
                print("||                      ||")
                print("||----------------------||")
                time.sleep(1)

                fim = True
                return (
                    itens_person,
                    moedas,
                    ataque,
                    defesa,
                    magia,
                    life,
                    life_regen,
                    n,
                    fim,
                    aumentar,
                )
        else:
            print("\nInválido!")
            time.sleep(1)
            clear_screen(10)

    return (
        itens_person,
        moedas,
        ataque,
        defesa,
        magia,
        life,
        life_regen,
        n,
        fim,
        aumentar,
    )
