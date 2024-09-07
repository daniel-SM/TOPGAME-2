# Funcao para obter os jogos salvos da pasta saved_games
def search_saved_games(games_amount):
    # Os arquivos estao nomeados numericamente na ordem que foram criados
    # Iniciamos com valor 1
    count = 1
    # Criando lista parar guardar as informacoes dos jogos salvos
    games = []
    # Percorrendo os jogos salvos
    # Verificando se ainda tem jogos salvos para mostrar
    while count <= games_amount:
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
            "enemyLife": int(lines[10]),
            "enemyAttack": int(lines[10]),
            "enemyDefense": int(lines[10]),
        }

        # Adicionar as informacoes na lista de jogos salvos
        games.append(info)

        # Imprimindo as informacoes do jogo atual
        # Definindo a largura do quadro
        largura = 40
        print()
        print(f"||{'-'*(largura-4)}||")
        print(f"|| Código:       {info['code']   :>{largura-20}} ||")
        print(f"|| Status:       {info['status'] :>{largura-20}} ||")
        print(f"|| Nome:         {info['name']   :>{largura-20}} ||")
        print(f"|| Fase:         {info['phase']  :>{largura-20}} ||")
        print(f"|| Vida:         {info['life']   :>{largura-20}} ||")
        print(f"|| Ataque:       {info['attack'] :>{largura-20}} ||")
        print(f"|| Defesa:       {info['defense']:>{largura-20}} ||")
        print(f"|| Regeneração:  {info['regen']  :>{largura-20}} ||")
        print(f"|| Magia:        {info['magic']  :>{largura-20}} ||")
        print(f"|| Moedas:       {info['coins']  :>{largura-20}} ||")
        print(f"||{'-'*(largura-4)}||")

        # Fechando arquivo
        file.close()

        # Incrementando para ler proximo jogo salvo
        count += 1

        input("\nEnter para continuar...")
    # Fim do while

    # Salvando a quantidade de jogos salvos
    games_amount = len(games)

    # Recebendo o codigo do jogo salvo para ser carregado
    code = input("\nCódigo do jogo salvo: ")

    # Verificando se o valor informado
    while (not code.isnumeric()) and int(code) in range(games_amount):
        print("\nInválido!")
        code = input("Código do jogo salvo: ")

    # Retornando as informacoes do jogo escolhido
    return games[int(code) - 1]
