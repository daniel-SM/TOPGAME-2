from random import choice  # Usado para sortear o fortalecimento dos inimigos
from time import sleep  # Usado para dar intervalos ao imprimir mensagens

from TOPGAME import FRAME_WIDTH  # Importando contante com tamanho dos quadros
from utils.clear import clear_screen  # Importando para limpar tela
from utils.story import initial_story  # Importando para mostrar a historia inicial
from storage.games import search_saved_games  # Importando para buscar os jogos salvos
from battle.battle import battle_manager  # Importando para gerenciar a batalha


def main():

    # Imprimindo o nome do jogo
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    print(f"||{' '*(FRAME_WIDTH-4)}||")
    print(f"|| {'######   #####    ##### ':<{FRAME_WIDTH-5}}||")
    print(f"|| {'  ##    ##   ##   ##  ##':<{FRAME_WIDTH-5}}||")
    print(f"|| {'  ##    ##   ##   ##### ':<{FRAME_WIDTH-5}}||")
    print(f"|| {'  ##     #####    ##    ':<{FRAME_WIDTH-5}}||")
    print(f"||{' '*(FRAME_WIDTH-4)}||")
    print(f"||{' ####    ####   ##    ##  #####':>{FRAME_WIDTH-5}} ||")
    print(f"||{'##      ##  ##  ########  ###  ':>{FRAME_WIDTH-5}} ||")
    print(f"||{'## ###  ######  ## ## ##  ##   ':>{FRAME_WIDTH-5}} ||")
    print(f"||{' ####   ##  ##  ##    ##  #####':>{FRAME_WIDTH-5}} ||")
    print(f"||{' '*(FRAME_WIDTH-4)}||")
    print(f"||{'-'*(FRAME_WIDTH-4)}||")
    sleep(2)

    # Definindo os dados iniciais do jogo
    player_name: str = ""
    phase: int = 0
    player_life: int = 100
    player_life_regen: int = 30
    player_attack: int = 80
    player_defense: int = 40
    player_magic: int = 0
    coins: int = 300
    player_items: list[tuple[str, str, int, int, str, int]] = []
    enemy_life: int = 70
    enemy_attack: int = 50
    enemy_defense: int = 20
    increase_enemy_power: bool = True

    # Variavel para indicar se deve iniciar um novo jogo
    start_new_game: bool = False

    # Variavel de controle do loop principal
    game_ended: bool = False

    # Carregando informacao sobre quantidade de jogos salvos

    file = open("./.storage/games_count", "r")
    saved_games_count: int = int(file.readline().strip())
    file.close()

    # Verificando se tem jogo salvo
    if saved_games_count > 0:
        # Imprimindo menu inicial
        print()
        print(f"||{'-'*(FRAME_WIDTH-4)}||")
        print(f"||{'MENU INICIAL':^{FRAME_WIDTH-4}}||")
        print(f"||{'-'*(FRAME_WIDTH-4)}||")
        print(f"||{'1. Novo Jogo':^{FRAME_WIDTH-4}}||")
        print(f"||{'2. Continuar Progresso':^{FRAME_WIDTH-4}}||")
        print(f"||{'3. Sair':^{FRAME_WIDTH-4}}||")
        print(f"||{'-'*(FRAME_WIDTH-4)}||")

        # Recebendo escolha do jogador
        option: str = input("\nOpção: ")

        # Validando escolha do jogador
        while option not in ["1", "2", "3"]:
            print("\nInválido!")
            option = input("Opção: ")

        # Caso deseja iniciar novo jogo
        if option == "1":
            # Indicando para iniciar novo jogo
            start_new_game = True
        # Caso queira continuar progresso
        elif option == "2":
            # Funcao para buscar e imprimir informacao dos jogos salvos
            saved_game_info: dict[str, str | int] | None = search_saved_games(
                saved_games_count
            )

            # Caso nao tenha continuado nenhum progresso
            if saved_game_info == None:
                # Indicando para iniciar novo jogo
                start_new_game = True
            # Caso tenha continuado algum progresso
            else:
                # Indicando para nao iniciar novo jogo
                start_new_game = False

                # Imprimindo mensagem de carregamento
                print("\nResgatando o progresso...\n")
                sleep(1)

                # Salvando as informacoes
                player_name = saved_game_info["name"]
                phase = saved_game_info["phase"]
                player_life = saved_game_info["life"]
                player_life_regen = saved_game_info["regen"]
                player_attack = saved_game_info["attack"]
                player_defense = saved_game_info["defense"]
                player_magic = saved_game_info["magic"]
                coins = saved_game_info["coins"]
                player_items = saved_game_info["items"]
                enemy_life = saved_game_info["enemy_life"]
                enemy_attack = saved_game_info["enemy_attack"]
                enemy_defense = saved_game_info["enemy_defense"]
                increase_enemy_power = False
            # Fim do if else
        # Caso queira sair do jogo
        else:
            # Indicando que deve finalizar o jogo
            game_ended = True
            # Indicando que nao deve iniciar novo jogo
            start_new_game = False

            # Imprimindo mensagem ao sair do jogo
            print()
            print(f"||{'-'*(FRAME_WIDTH-4)}||")
            print(f"||{' '*(FRAME_WIDTH-4)}||")
            print(f"||{'VOCÊ SAIU DO JOGO!':^{FRAME_WIDTH-4}}||")
            print(f"||{' '*(FRAME_WIDTH-4)}||")
            print(f"||{'-'*(FRAME_WIDTH-4)}||")
            sleep(1)

        # Limpando a tela
        clear_screen()
    # Fim do if

    # Verificando se vai iniciar um novo jogo
    if start_new_game:
        # Obtendo o nome do jogador
        player_name = input("\nNome: ")

        # Verificando o nome informado
        while player_name == "" or player_name.isspace():
            print("\nInválido!")
            player_name = input("Nome: ")

        # História Inicial do Jogo
        initial_story()
    # Fim do if

    # Loop principal do jogo
    while not game_ended:
        # Verificando se o jogador tem vida
        if player_life > 0:
            # Verificando se pode aumentar poder do inimigo
            if (phase > 0) and increase_enemy_power:
                # Fortalecendo as stats dos inimigos
                player_life += player_life_regen
                enemy_life += choice([5, 10])
                enemy_attack += choice([10, 10, 20])
                enemy_defense += choice([10, 10, 20])

                # Aumentando as coins do jogador
                coins += 150 + (50 * (phase - 1))

            # Executando todas as funcionalidades relacionadas com batalha
            (
                player_items,
                coins,
                player_attack,
                player_defense,
                player_magic,
                player_life,
                player_life_regen,
                phase,
                game_ended,
                increase_enemy_power,
            ) = battle_manager(
                saved_games_count,
                player_name,
                player_items,
                player_life_regen,
                player_life,
                enemy_life,
                player_magic,
                player_attack,
                enemy_attack,
                player_defense,
                enemy_defense,
                coins,
                phase,
            )
        else:
            # Definindo para encerrar o jogo
            game_ended = True

            # Imprimindo mensagem de fim de jogo
            print()
            print(f"||{'-'*(FRAME_WIDTH-4)}||")
            print(f"||{'VOCÊ MORREU!':^{FRAME_WIDTH-4}}||")
            print(f"||{'O JOGO ACABOU!':^{FRAME_WIDTH-4}}||")
            print(f"||{'-'*(FRAME_WIDTH-4)}||")
        # Fim do if else

        # Incrementando a fase
        phase += 1

        # Verificando se as fases acabaram
        if phase > 15:
            # Definindo que o jogo deve encerrar
            game_ended = True
    # Fim do while


if __name__ == "__main__":
    main()
