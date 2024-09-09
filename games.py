# Funcao para obter os jogos salvos da pasta saved_games
def search_saved_games(saved_games_count):
    # Os arquivos estao nomeados numericamente na ordem que foram criados
    # Iniciando com valor 1
    count = 1
    # Criando lista parar guardar as informacoes de cada jogo salvo
    saved_games = []

    # Loop para ler informacoes dos jogos salvos
    while count <= saved_games_count:
        # Lendo as informacoes do jogo atual
        file = open(f"./storage/saved_games/{count}", "r")

        # Carregando as linhas do arquivo
        lines = file.read().splitlines()

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
        # Adicionar as informacoes na lista de jogos salvos
        saved_games.append(info)

        # Imprimindo as informacoes do jogo atual
        # Definindo a largura do quadro
        width = 40
        print()
        print(f"||{'-'*(width-4)}||")
        print(f"|| Código:       {info['code']   :>{width-20}} ||")
        print(f"|| Nome:         {info['name']   :>{width-20}} ||")
        print(f"|| Fase:         {info['phase']  :>{width-20}} ||")
        print(f"|| Vida:         {info['life']   :>{width-20}} ||")
        print(f"|| Ataque:       {info['attack'] :>{width-20}} ||")
        print(f"|| Defesa:       {info['defense']:>{width-20}} ||")
        print(f"|| Regeneração:  {info['regen']  :>{width-20}} ||")
        print(f"|| Magia:        {info['magic']  :>{width-20}} ||")
        print(f"|| Moedas:       {info['coins']  :>{width-20}} ||")
        print(f"||{'-'*(width-4)}||")

        # Fechando arquivo
        file.close()

        # Incrementando para ler proximo jogo salvo
        count += 1

        input("\nEnter para continuar...")
    # Fim do while

    # Recebendo o codigo do jogo salvo para ser carregado
    game_code = input("\nCódigo do jogo salvo: ")

    # Verificando se o valor informado
    while (not game_code.isnumeric()) and (int(game_code) in range(1, saved_games_count)):
        print("\nInválido!")
        game_code = input("Código do jogo salvo: ")

    # Retornando as informacoes do jogo escolhido
    return saved_games[int(game_code) - 1]
