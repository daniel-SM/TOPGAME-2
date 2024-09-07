# Usado para gerar intervalos entre as mensagens
import time

# Importando funcao para limpar o terminal
from clear import clear_screen


def initial_history(nome):
    # Imprimindo a historia inicial do RPG
    print()
    print("||---------##---------##---------##---------||")
    print(f"||    SEJA BEM-VINDO(A), {nome}!")
    print("||---------##---------##---------##---------||")
    time.sleep(2)
    print("||   Você é um guerreiro que serve ao rei   ||")
    print("||   e nesse momento está defendendo seu    ||")
    print("||   reino de um ataque de criaturas e      ||")
    print("||   monstros!                              ||")
    print("||   Derrote todas as criaturas e salve o   ||")
    print("||   rei e o seu castelo!                   ||")
    time.sleep(2)
    print("||---------##---------##---------##---------||")
    print("||                 BOA SORTE!               ||")
    print("||---------##---------##---------##---------||")
    input("\nEnter para continuar...")
    print()
    print("||---------##---------##---------##---------||")
    print("||                                          ||")
    print("||         #####   ####   ##    ##          ||")
    print("||         ## ##  ##  ##  ## ## ##          ||")
    print("||         #####  ##  ##  ########          ||")
    print("||         ##      ####   ##    ##          ||")
    print("||                                          ||")
    print("||---------##---------##---------##---------||")
    time.sleep(2)
    print("||   Os monstros destruiram o portão sul    ||")
    print("||   do reino! Monstros perigosos se        ||")
    print("||   aproximam do castelo do rei!           ||")
    print("||   Corra nessa direção e impeça que os    ||")
    print("||   monstros avançem contra o rei!         ||")
    time.sleep(2)
    print("||---------##---------##---------##---------||")
    print("||                 DEPRESSA!                ||")
    print("||---------##---------##---------##---------||")
    input("\nEnter para continuar...")

    # Limpando o terminal apos a historia
    clear_screen(100)
