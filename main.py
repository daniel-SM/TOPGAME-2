# Usado para randomizar o fortalecimento dos inimigos
import random
# Usado para dar intervalos ao imprimir mensagens
import time

# Importando funcao para mostrar a historia inicial
from history import printInitialHistory
# Importando funcao para consultar os jogos salvos
from games import searchSavedGames
# Importando funcao para gerenciar a batalha completa
from battle import battleManager
# Importando funcao para validar a entrada do usuario 
from option import validateOption

# Imprimindo o nome do jogo
print('''
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
''')
time.sleep(2)

# Abrindo arquivo com dados dos jogos salvos
file = open("./storage/game_info.txt", "r")

# Carregando informacao se existe jogo salvo
jogoSalvo = eval(file.readline().rstrip())
# Carregando quantidade de jogos salvos
qtdJogos  = int(file.readline().rstrip())

# Fechando arquivo
file.close()

# Inicializando variavel para indicar se iniciou um novo jogo
iniciarZero = True

# Verificando se tem jogo salvo
if (jogoSalvo == True):
    # Perguntando se o jogador quer continuar algum progresso
    desejo = input("\nS - sim\nN - não\nContinuar algum progresso salvo? ")
    desejo = validateOption(desejo)
    
    # Caso queira continuar progresso, faz busca dos jogos salvos
    if (desejo == "s"):
        # Funcao para buscar e imprimir informacao dos jogos salvos
        gameInfo = searchSavedGames(qtdJogos)
        
        print("\nResgatando o progresso...\n")
        time.sleep(1)

        # Salvando as informacoes
        nome        = gameInfo["name"]
        fase        = gameInfo["phase"]
        life        = gameInfo["life"]
        lifeRegen   = gameInfo["regen"]
        ataque      = gameInfo["attack"]
        defesa      = gameInfo["defense"]
        magia       = gameInfo["magic"]
        moedas      = gameInfo["coins"]
        itensPerson = gameInfo["items"]
        lifeInim    = gameInfo["enemyLife"]
        ataqueInim  = gameInfo["enemyAttack"]
        defesaInim  = gameInfo["enemyDefense"]
        aumentar    = False

        # Indicando que nao iniciou um novo jogo
        iniciarZero = False
# Fim do if

# Verificando se iniciou um novo jogo
if (iniciarZero == True):
    # Obtendo o nome do jogador
    nome = input("\nNome: ")
    
    # Verificando o nome informado
    while (nome == "" or nome.isspace()):
        print("\nInválido!")
        nome = input("Nome: ")
    
    # Definindo as stats iniciais do jogador
    fase        = 0
    life        = 100
    lifeRegen   = 30
    ataque      = 80
    defesa      = 40
    magia       = 0
    moedas      = 300
    itensPerson = []
    lifeInim    = 70
    ataqueInim  = 50
    defesaInim  = 20
    aumentar    = True

    # História Inicial do Jogo
    printInitialHistory(nome)
# Fim do if

# Variavel de controle do loop
fim = False

while (fase < 15 or not fim):
    # Verificando se o jogador ainda tem vida
    if (life > 0):
        # Verificando se nao esta na primeira fase 
        # e se pode fortalecer os inimigos
        if (fase > 0) and (aumentar == True):
            # Fortalecendo as stats dos inimigos
            life       += lifeRegen
            lifeInim   += random.choice([5, 10])
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
        aumentar = battleManager(
            qtdJogos,
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
            jogoSalvo,
            fase
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
