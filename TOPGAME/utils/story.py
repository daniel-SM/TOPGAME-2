import time  # Usado para gerar intervalos entre as mensagens

from TOPGAME import FRAME_WIDTH  # Importando contante com tamanho dos quadros
from .clear import clear_screen  # Importando funcao para limpar o terminal


# Imprime a historia inicial do jogo
def initial_story() -> None:

    print()
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    print(f"||{'SEJA BEM-VINDO(A)!':^{FRAME_WIDTH-4}}||")
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    time.sleep(2)

    print(f"||{' '*(FRAME_WIDTH-4)}||")
    print(f"||{'Você é um guerreiro que serve':^{FRAME_WIDTH-4}}||")
    print(f"||{'ao rei e nesse momento está':^{FRAME_WIDTH-4}}||")
    print(f"||{'defendendo seu reino de um':^{FRAME_WIDTH-4}}||")
    print(f"||{'ataque de criaturas e monstros!':^{FRAME_WIDTH-4}}||")
    print(f"||{' '*(FRAME_WIDTH-4)}||")
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    print(f"||{' '*(FRAME_WIDTH-4)}||")
    print(f"||{'Derrote todas os inimigos':^{FRAME_WIDTH-4}}||")
    print(f"||{'e salve o rei e seu castelo!':^{FRAME_WIDTH-4}}||")
    print(f"||{' '*(FRAME_WIDTH-4)}||")
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    time.sleep(2)

    print(f"||{'BOA SORTE!':^{FRAME_WIDTH-4}}||")
    print(f"||{'-'*(FRAME_WIDTH-4)}||")

    input("\nEnter para continuar... ")

    print()
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    print(f"||{' '*(FRAME_WIDTH-4)}||")
    print(f"||{'####    ####   ##    ##':^{FRAME_WIDTH-4}}||")
    print(f"||{'## ##  ##  ##  ## ## ##':^{FRAME_WIDTH-4}}||")
    print(f"||{'####   ##  ##  ###  ###':^{FRAME_WIDTH-4}}||")
    print(f"||{'##      ####   ##    ##':^{FRAME_WIDTH-4}}||")
    print(f"||{' '*(FRAME_WIDTH-4)}||")
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    time.sleep(2)

    print(f"||{' '*(FRAME_WIDTH-4)}||")
    print(f"||{'Os monstros destruiram o portão':^{FRAME_WIDTH-4}}||")
    print(f"||{'sul do reino. Eles se aproximam':^{FRAME_WIDTH-4}}||")
    print(f"||{'do castelo do rei. Impeça que os':^{FRAME_WIDTH-4}}||")
    print(f"||{'monstros ataquem o rei!':^{FRAME_WIDTH-4}}||")
    print(f"||{' '*(FRAME_WIDTH-4)}||")
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    time.sleep(2)

    print(f"||{'DEPRESSA!':^{FRAME_WIDTH-4}}||")
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    input("\nEnter para continuar... ")

    # Limpando o terminal apos a historia
    clear_screen()
