from clear import clear_screen  # Importando para limpar a tela
from option import validate_option  # Importando para validar opcao digitada


# Funcao para obter os jogos salvos
def search_saved_games(saved_games_count):
    # Limpando a tela
    clear_screen()

    # Definindo a largura do quadro
    width = 40

    # Iniciando contagem com valor 1
    count = 1

    # OBS: Os arquivos estao nomeados numericamente na ordem que foram criados
    # Criando lista parar guardar as informacoes de cada jogo salvo
    saved_games = []

    # Imprimindo a quantidade de jogos salvos
    print(f"||{'-'*(width-4)}||")
    print(f"||{f'Você tem {saved_games_count} jogo(s) salvo(s)!':^{width-4}}||")
    print(f"||{'-'*(width-4)}||")
    input("\nEnter para continuar... ")

    # Loop para ler informacoes dos jogos salvos
    while count <= saved_games_count:
        # Carregando as informacoes do jogo atual
        file = open(f"./storage/saved_games/{count}", "r")
        lines = file.read().splitlines()
        file.close()

        # Criando dicionario com as informacoes do jogo salvo
        info = {
            "code": count,
            "name": lines[0],
            "phase": int(lines[1]),
            "life": int(lines[2]),
            "attack": int(lines[3]),
            "defense": int(lines[4]),
            "regen": int(lines[5]),
            "magic": int(lines[6]),
            "coins": int(lines[7]),
            "items": eval(lines[8]),  # Transformando em lista
            "enemy_life": int(lines[9]),
            "enemy_attack": int(lines[10]),
            "enemy_defense": int(lines[11]),
        }

        # Imprimindo as informacoes do jogo atual
        print()
        print(f"||{'-'*(width-4)}||")
        print(f"||{f'JOGO {count}':^{width-4}}||")
        print(f"||{'-'*(width-4)}||")
        print(f"|| Código:       {info['code']    :>{width-20}} ||")
        print(f"|| Nome:         {info['name']    :>{width-20}} ||")
        print(f"|| Fase:         {info['phase']   :>{width-20}} ||")
        print(f"|| Vida:         {info['life']    :>{width-20}} ||")
        print(f"|| Ataque:       {info['attack']  :>{width-20}} ||")
        print(f"|| Defesa:       {info['defense'] :>{width-20}} ||")
        print(f"|| Regeneração:  {info['regen']   :>{width-20}} ||")
        print(f"|| Magia:        {info['magic']   :>{width-20}} ||")
        print(f"|| Moedas:       {info['coins']   :>{width-20}} ||")
        print(f"||{'-'*(width-4)}||")

        # Adicionar as informacoes na lista de jogos salvos
        saved_games.append(info)

        # Incrementando para ler proximo jogo salvo
        count += 1

        # Nao imprime mensagem se for o ultimo
        if count <= saved_games_count:
            input("\nEnter para continuar... ")
    # Fim do while

    # Confirmando se deseja continuar
    option = input("\nS- sim\nN - não\nContinuar algum progresso? ")
    option = validate_option(option)

    # Caso nao deseje continuar
    if option == "n":
        return None

    # Recebendo o codigo do jogo a ser carregado
    game_code = input("\nCódigo do jogo salvo: ")

    # Verificando se o valor informado
    while not game_code.isnumeric() and int(game_code) in range(1, saved_games_count):
        print("\nInválido!")
        game_code = input("Código do jogo salvo: ")

    # Retornando as informacoes do jogo escolhido
    return saved_games[int(game_code) - 1]
