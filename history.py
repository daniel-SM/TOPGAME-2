import time  # Usado para gerar intervalos entre as mensagens

from clear import clear_screen  # Importando funcao para limpar o terminal


# Imprime a historia inicial do jogo
def initial_history() -> None:
    # Definindo largura dos quadro exibido
    WIDTH: int = 40

    print()
    print(f"||{'-'*(WIDTH-4)}||")
    print(f"||{'SEJA BEM-VINDO(A)!':^{WIDTH-4}}||")
    print(f"||{'-'*(WIDTH-4)}||")
    time.sleep(2)

    print(f"||{' '*(WIDTH-4)}||")
    print(f"||{'Você é um guerreiro que serve':^{WIDTH-4}}||")
    print(f"||{'ao rei e nesse momento está':^{WIDTH-4}}||")
    print(f"||{'defendendo seu reino de um':^{WIDTH-4}}||")
    print(f"||{'ataque de criaturas e monstros!':^{WIDTH-4}}||")
    print(f"||{' '*(WIDTH-4)}||")
    print(f"||{'-'*(WIDTH-4)}||")
    print(f"||{' '*(WIDTH-4)}||")
    print(f"||{'Derrote todas as criaturas':^{WIDTH-4}}||")
    print(f"||{'e salve o rei e seu castelo!':^{WIDTH-4}}||")
    print(f"||{' '*(WIDTH-4)}||")
    print(f"||{'-'*(WIDTH-4)}||")
    time.sleep(2)

    print(f"||{'BOA SORTE!':^{WIDTH-4}}||")
    print(f"||{'-'*(WIDTH-4)}||")

    input("\nEnter para continuar... ")

    print()
    print(f"||{'-'*(WIDTH-4)}||")
    print(f"||{' '*(WIDTH-4)}||")
    print(f"||{'####    ####   ##    ##':^{WIDTH-4}}||")
    print(f"||{'## ##  ##  ##  ## ## ##':^{WIDTH-4}}||")
    print(f"||{'####   ##  ##  ###  ###':^{WIDTH-4}}||")
    print(f"||{'##      ####   ##    ##':^{WIDTH-4}}||")
    print(f"||{' '*(WIDTH-4)}||")
    print(f"||{'-'*(WIDTH-4)}||")
    time.sleep(2)

    print(f"||{' '*(WIDTH-4)}||")
    print(f"||{'Os monstros destruiram':^{WIDTH-4}}||")
    print(f"||{' o portão sul do reino!':^{WIDTH-4}}||")
    print(f"||{'Monstros perigosos se aproximam':^{WIDTH-4}}||")
    print(f"||{'do castelo do rei!':^{WIDTH-4}}||")
    print(f"||{'Vá nessa direção e impeça que os':^{WIDTH-4}}||")
    print(f"||{'monstros avançem contra o rei!':^{WIDTH-4}}||")
    print(f"||{' '*(WIDTH-4)}||")
    print(f"||{'-'*(WIDTH-4)}||")
    time.sleep(2)

    print(f"||{'DEPRESSA!':^{WIDTH-4}}||")
    print(f"||{'-'*(WIDTH-4)}||")
    input("\nEnter para continuar... ")

    # Limpando o terminal apos a historia
    clear_screen()
