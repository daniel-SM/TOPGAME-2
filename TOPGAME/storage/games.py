from utils.clear import clear_screen  # Importando para limpar a tela
from utils.option import validate_option  # Importando para validar opcao digitada


# Funcao para obter os jogos salvos
def search_saved_games(
    saved_games_count: int,
) -> dict[str, (str | int)] | None:
    # Limpando a tela
    clear_screen()

    # Definindo a largura do quadro
    WIDTH: int = 40

    # Iniciando contagem com valor 1
    count: int = 1

    # OBS: Os arquivos estao nomeados numericamente na ordem que foram criados
    # Criando lista parar guardar as informacoes de cada jogo salvo
    saved_games: list[dict[str, str | int]] = []

    # Imprimindo a quantidade de jogos salvos
    print(f"||{'-'*(WIDTH-4)}||")
    print(f"||{f'Você tem {saved_games_count} jogo(s) salvo(s)!':^{WIDTH-4}}||")
    print(f"||{'-'*(WIDTH-4)}||")
    input("\nEnter para continuar... ")

    # Loop para ler informacoes dos jogos salvos
    while count <= saved_games_count:
        # Carregando as informacoes do jogo atual
        file = open(f"./.storage/{count}", "r")
        lines: list[str] = file.read().splitlines()
        file.close()

        # Criando dicionario com as informacoes do jogo salvo
        info: dict[str, str | int] = {
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
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"||{f'JOGO {count}':^{WIDTH-4}}||")
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"|| Código:       {info['code']    :>{WIDTH-20}} ||")
        print(f"|| Nome:         {info['name']    :>{WIDTH-20}} ||")
        print(f"|| Fase:         {info['phase']   :>{WIDTH-20}} ||")
        print(f"|| Vida:         {info['life']    :>{WIDTH-20}} ||")
        print(f"|| Ataque:       {info['attack']  :>{WIDTH-20}} ||")
        print(f"|| Defesa:       {info['defense'] :>{WIDTH-20}} ||")
        print(f"|| Regeneração:  {info['regen']   :>{WIDTH-20}} ||")
        print(f"|| Magia:        {info['magic']   :>{WIDTH-20}} ||")
        print(f"|| Moedas:       {info['coins']   :>{WIDTH-20}} ||")
        print(f"||{'-'*(WIDTH-4)}||")

        # Adicionar as informacoes na lista de jogos salvos
        saved_games.append(info)

        # Incrementando para ler proximo jogo salvo
        count += 1

        # Nao imprime mensagem se for o ultimo
        if count <= saved_games_count:
            input("\nEnter para continuar... ")
    # Fim do while

    # Confirmando se deseja continuar
    option: str = input("\nS- sim\nN - não\nContinuar algum progresso? ")
    option = validate_option(option)

    # Caso nao deseje continuar
    if option == "n":
        return None

    # Recebendo o codigo do jogo a ser carregado
    game_code: str = input("\nCódigo do jogo salvo: ")

    # Verificando se o valor informado
    while not game_code.isnumeric() and int(game_code) in range(1, saved_games_count):
        print("\nInválido!")
        game_code = input("Código do jogo salvo: ")

    # Retornando as informacoes do jogo escolhido
    return saved_games[int(game_code) - 1]
