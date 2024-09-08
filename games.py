# Funcao para obter os jogos salvos da pasta saved_games
def search_saved_games(saved_games_count):
    # Os arquivos estao nomeados numericamente na ordem que foram criados
    # Iniciamos com valor 1
    count = 1
    # Criando lista parar guardar as informacoes dos jogos salvos
    saved_games = []
    # Percorrendo os jogos salvos
    # Verificando se ainda tem jogos salvos para mostrar
    while count <= saved_games_count:
        # Lendo as informacoes do arquivo atual
        file = open(f"./storage/saved_games/{count}", "r")

        # Carregando as linhas do arquivo
        lines = file.readlines()

        # Percorrendo as linhas e removendo os caracteres '\n'
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()

        # Criando dicionario com as informacoes do jogo salvo
        info = {
            "code": count,
            "status": lines[0],
            "name": lines[1],
            "phase": int(lines[2]),
            "life": int(lines[3]),
            "attack": int(lines[4]),
            "defense": int(lines[5]),
            "regen": int(lines[6]),
            "magic": int(lines[7]),
            "coins": int(lines[8]),
            "items": eval(lines[9]),  # Transformando em lista
            "enemy_life": int(lines[10]),
            "enemy_attack": int(lines[10]),
            "enemy_defense": int(lines[10]),
        }

        # Adicionar as informacoes na lista de jogos salvos
        saved_games.append(info)

        # Imprimindo as informacoes do jogo atual
        # Definindo a largura do quadro
        width = 40
        print()
        print(f"||{'-'*(width-4)}||")
        print(f"|| Código:       {info['code']   :>{width-20}} ||")
        print(f"|| Status:       {info['status'] :>{width-20}} ||")
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

    # Salvando a quantidade de jogos salvos
    saved_games_count = len(saved_games)

    # Recebendo o codigo do jogo salvo para ser carregado
    code = input("\nCódigo do jogo salvo: ")

    # Verificando se o valor informado
    while (not code.isnumeric()) and int(code) in range(saved_games_count):
        print("\nInválido!")
        code = input("Código do jogo salvo: ")

    # Retornando as informacoes do jogo escolhido
    return saved_games[int(code) - 1]
