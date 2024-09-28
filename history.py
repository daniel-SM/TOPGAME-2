# usado para gerar intervalos entre as mensagens
import time

# importando funcao para limpar o terminal
from clear import clear_screen


# imprime a historia inicial do jogo
def initial_history(nome):
    # definindo largura dos quadro exibido
    width = 40
    print()
    print(f"||{'-'*(width-4)}||")
    print(f"||{f'SEJA BEM-VINDO (A), {nome}!':^{width-4}}||")
    print(f"||{'-'*(width-4)}||")
    time.sleep(2)
    print(f"||{' '*(width-4)}||")
    print(f"||{'Você é um guerreiro que serve':^{width-4}}||")
    print(f"||{'ao rei e nesse momento está':^{width-4}}||")
    print(f"||{'defendendo seu reino de um':^{width-4}}||")
    print(f"||{'ataque de criaturas e monstros!':^{width-4}}||")
    print(f"||{' '*(width-4)}||")
    print(f"||{'-'*(width-4)}||")
    print(f"||{' '*(width-4)}||")
    print(f"||{'Derrote todas as criaturas':^{width-4}}||")
    print(f"||{'e salve o rei e seu castelo!':^{width-4}}||")
    print(f"||{' '*(width-4)}||")
    print(f"||{'-'*(width-4)}||")
    time.sleep(2)
    print(f"||{' '*(width-4)}||")
    print(f"||{'BOA SORTE!':^{width-4}}||")
    print(f"||{' '*(width-4)}||")
    print(f"||{'-'*(width-4)}||")

    input("\nEnter para continuar... ")
    print()
    print(f"||{'-'*(width-4)}||")
    print(f"||{' '*(width-4)}||")
    print(f"||{'####    ####   ##    ##':^{width-4}}||")
    print(f"||{'## ##  ##  ##  ## ## ##':^{width-4}}||")
    print(f"||{'####   ##  ##  ###  ###':^{width-4}}||")
    print(f"||{'##      ####   ##    ##':^{width-4}}||")
    print(f"||{' '*(width-4)}||")
    print(f"||{'-'*(width-4)}||")
    time.sleep(2)
    print(f"||{' '*(width-4)}||")
    print(f"||{'Os monstros destruiram':^{width-4}}||")
    print(f"||{' o portão sul do reino!':^{width-4}}||")
    print(f"||{'Monstros perigosos se aproximam':^{width-4}}||")
    print(f"||{'do castelo do rei!':^{width-4}}||")
    print(f"||{'Vá nessa direção e impeça que os':^{width-4}}||")
    print(f"||{'monstros avançem contra o rei!':^{width-4}}||")
    print(f"||{' '*(width-4)}||")
    print(f"||{'-'*(width-4)}||")
    time.sleep(2)
    print(f"||{' '*(width-4)}||")
    print(f"||{'DEPRESSA!':^{width-4}}||")
    print(f"||{' '*(width-4)}||")
    print(f"||{'-'*(width-4)}||")
    input("\nEnter para continuar... ")

    # Limpando o terminal apos a historia
    clear_screen()
