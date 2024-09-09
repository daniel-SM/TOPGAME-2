# Usado para randomizar o fortalecimento dos inimigos
import random

# Usado para dar intervalos ao imprimir mensagens
import time

# Importando funcao para mostrar a historia inicial
from history import initial_history

# Importando funcao para consultar os jogos salvos
from games import search_saved_games

# Importando funcao para gerenciar a batalha completa
from battle import battle_manager

# Importando funcao para validar a entrada do usuario
from option import validate_option

# Imprimindo o nome do jogo
print(
    """
||------------------------------------------||
||                                          ||
||  ######   #####    #####                 ||
||    ##    ##   ##   ##  ##                ||
||    ##    ##   ##   #####                 ||
||    ##     #####    ##                    ||
||                                          ||
||          ####    ####   ##    ##  #####  ||
||         ##      ##  ##  ########  ###    ||
||         ## ###  ######  ## ## ##  ##     ||
||          ####   ##  ##  ##    ##  #####  ||
||                                          ||
||------------------------------------------||
"""
)
time.sleep(2)

# Abrindo arquivo com dados dos jogos salvos
file = open("./storage/game_info.txt", "r")

# Carregando informacao sobre quantidade de jogos salvos
saved_games_count = int(file.readline().rstrip())

# Fechando arquivo
file.close()

# Inicializando variavel para indicar se iniciou um novo jogo
start_from_save = False

# Verificando se tem jogo salvo
if saved_games_count > 0:
    # Perguntando se o jogador quer continuar algum progresso
    option = input("\nS - sim\nN - não\nContinuar algum progresso salvo? ")
    option = validate_option(option)

    # Caso queira continuar progresso, faz busca dos jogos salvos
    if option == "s":
        # Funcao para buscar e imprimir informacao dos jogos salvos
        game_info = search_saved_games(saved_games_count)

        print("\nResgatando o progresso...\n")
        time.sleep(1)

        # Salvando as informacoes
        player_name = game_info["name"]
        phase = game_info["phase"]
        player_life = game_info["life"]
        player_life_regen = game_info["regen"]
        player_attack = game_info["attack"]
        player_defense = game_info["defense"]
        player_magic = game_info["magic"]
        coins = game_info["coins"]
        player_items = game_info["items"]
        enemy_life = game_info["enemy_life"]
        enemy_attack = game_info["enemy_attack"]
        enemy_attack = game_info["enemy_defense"]
        increase_enemy_power = False

        # Indicando que nao iniciou um novo jogo
        start_from_save = True
# Fim do if

# Verificando se iniciou um novo jogo
if not start_from_save:
    # Obtendo o nome do jogador
    player_name = input("\nNome: ")

    # Verificando o nome informado
    while player_name == "" or player_name.isspace():
        print("\nInválido!")
        player_name = input("Nome: ")

    # Definindo as stats iniciais do jogador
    phase = 0
    player_life = 100
    player_life_regen = 30
    player_attack = 80
    player_defense = 40
    player_magic = 0
    coins = 300
    player_items = []
    enemy_life = 70
    enemy_attack = 50
    enemy_attack = 20
    increase_enemy_power = True

    # História Inicial do Jogo
    initial_history(player_name)
# Fim do if

# Variavel de controle do loop
battle_ended = False

while phase < 15 or not battle_ended:
    # Verificando se o jogador ainda tem vida
    if player_life > 0:
        # Verificando se nao esta na primeira fase
        # e se pode fortalecer os inimigos
        if (phase > 0) and increase_enemy_power:
            # Fortalecendo as stats dos inimigos
            player_life += player_life_regen
            enemy_life += random.choice([5, 10])
            enemy_attack += random.choice([10, 10, 20])
            enemy_attack += random.choice([10, 10, 20])

            # Aumentando as coins do jogador
            coins += 150 + (50 * (phase - 1))

        # Executando todas as funcionalidades relacionadas com batalha
        player_items,
        coins,
        player_attack,
        player_defense,
        player_magic,
        player_life,
        player_life_regen,
        phase,
        battle_ended,
        increase_enemy_power = battle_manager(
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
            enemy_attack,
            coins,
            phase
        )
    else:
        # Caso o jogador nao tenha vida, encerra o jogo
        print("||----------------------------||")
        print("||        VOCÊ MORREU!        ||")
        print("||       O JOGO ACABOU!       ||")
        print("||----------------------------||")
        break
    # Fim do if else

    # Incrementando a fase
    phase += 1
# Fim do while
