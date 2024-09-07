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

# Carregando informacao se existe jogo salvo
jogo_salvo = eval(file.readline().rstrip())
# Carregando quantidade de jogos salvos
qtd_jogos = int(file.readline().rstrip())

# Fechando arquivo
file.close()

# Inicializando variavel para indicar se iniciou um novo jogo
iniciar_do_zero = True

# Verificando se tem jogo salvo
if jogo_salvo == True:
    # Perguntando se o jogador quer continuar algum progresso
    desejo = input("\nS - sim\nN - não\nContinuar algum progresso salvo? ")
    desejo = validate_option(desejo)

    # Caso queira continuar progresso, faz busca dos jogos salvos
    if desejo == "s":
        # Funcao para buscar e imprimir informacao dos jogos salvos
        game_info = search_saved_games(qtd_jogos)

        print("\nResgatando o progresso...\n")
        time.sleep(1)

        # Salvando as informacoes
        nome = game_info["name"]
        fase = game_info["phase"]
        life = game_info["life"]
        lifeRegen = game_info["regen"]
        ataque = game_info["attack"]
        defesa = game_info["defense"]
        magia = game_info["magic"]
        moedas = game_info["coins"]
        itensPerson = game_info["items"]
        lifeInim = game_info["enemyLife"]
        ataqueInim = game_info["enemyAttack"]
        defesaInim = game_info["enemyDefense"]
        aumentar = False

        # Indicando que nao iniciou um novo jogo
        iniciar_do_zero = False
# Fim do if

# Verificando se iniciou um novo jogo
if iniciar_do_zero == True:
    # Obtendo o nome do jogador
    nome = input("\nNome: ")

    # Verificando o nome informado
    while nome == "" or nome.isspace():
        print("\nInválido!")
        nome = input("Nome: ")

    # Definindo as stats iniciais do jogador
    fase = 0
    life = 100
    lifeRegen = 30
    ataque = 80
    defesa = 40
    magia = 0
    moedas = 300
    itensPerson = []
    lifeInim = 70
    ataqueInim = 50
    defesaInim = 20
    aumentar = True

    # História Inicial do Jogo
    initial_history(nome)
# Fim do if

# Variavel de controle do loop
fim = False

while fase < 15 or not fim:
    # Verificando se o jogador ainda tem vida
    if life > 0:
        # Verificando se nao esta na primeira fase
        # e se pode fortalecer os inimigos
        if (fase > 0) and (aumentar == True):
            # Fortalecendo as stats dos inimigos
            life += lifeRegen
            lifeInim += random.choice([5, 10])
            ataqueInim += random.choice([10, 10, 20])
            defesaInim += random.choice([10, 10, 20])

            # Aumentando as moedas do jogador
            moedas += 150 + (50 * (fase - 1))

        # Executando todas as funcionalidades relacionadas com batalha
        itensPerson,
        moedas,
        ataque,
        defesa,
        magia,
        life,
        lifeRegen,
        fase,
        fim,
        aumentar = battle_manager(
            qtd_jogos,
            nome,
            itensPerson,
            lifeRegen,
            life,
            lifeInim,
            magia,
            ataque,
            ataqueInim,
            defesa,
            defesaInim,
            moedas,
            jogo_salvo,
            fase,
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
    fase += 1
# Fim do while
