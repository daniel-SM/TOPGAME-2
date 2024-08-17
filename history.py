# Usado para gerar intervalos entre as mensagens
import time

# Importando funcao para limpar o terminal
from clear import clearScreen

def printInitialHistory(nome):
    # Imprimindo a historia inicial do RPG
    print()
    print("||---------##---------##---------##---------||")
    print(f"||    SEJA BEM-VINDO(A), {nome}!")
    print("||---------##---------##---------##---------||")  
    time.sleep(1)
    print("||   Você é um guerreiro que serve ao rei   ||")
    print("||   e nesse momento está defendendo seu    ||")
    print("||   reino de um ataque de criaturas e      ||")
    print("||   monstros!                              ||")
    print("||   Derrote todas as criaturas e salve o   ||")
    print("||   rei e o seu castelo!                   ||")
    print("||---------##---------##---------##---------||")
    time.sleep(10)
    print("||                 BOA SORTE!               ||") 
    print("||---------##---------##---------##---------||")
    time.sleep(2)
    print("||                                          ||")
    print("||         #####   ####   ##    ##          ||")
    print("||         ## ##  ##  ##  ## ## ##          ||")
    print("||         #####  ##  ##  ########          ||")
    print("||         ##      ####   ##    ##          ||")
    print("||---------##---------##---------##---------||")
    time.sleep(1)
    print("||   Os monstros destruiram o portão sul    ||")
    print("||   do reino! Monstros perigosos se        ||")
    print("||   aproximam do castelo do rei!           ||")
    print("||   Corra nessa direção e impeça que os    ||")
    print("||   monstros avançem contra o rei!         ||")
    print("||---------##---------##---------##---------||")
    time.sleep(10)
    print("||                 DEPRESSA!                ||")
    print("||---------##---------##---------##---------||")
    time.sleep(1)
    input("\nEnter para continuar...")

    # Limpando o terminal apos a historia
    clearScreen(100)

