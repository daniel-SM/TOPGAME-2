# Funcao para salvar os dados do jogo em arquivo
def save_to_storage(
    saved_games_count: int,
    player_name: str,
    phase: int,
    player_life: int,
    player_life_regen: int,
    player_attack: int,
    player_defense: int,
    player_magic: int,
    coins: int,
    player_items: list[tuple[str, str, int, int, str, int]],
    enemy_life: int,
    enemy_attack: int,
    enemy_defense: int,
) -> int:
    saved_games_count += 1

    file = open("./.storage/" + str(saved_games_count), "w")

    file.write(str(player_name) + "\n")
    file.write(str(phase) + "\n")
    file.write(str(player_life) + "\n")
    file.write(str(player_life_regen) + "\n")
    file.write(str(player_attack) + "\n")
    file.write(str(player_defense) + "\n")
    file.write(str(player_magic) + "\n")
    file.write(str(coins) + "\n")
    file.write(str(player_items) + "\n")
    file.write(str(enemy_life) + "\n")
    file.write(str(enemy_attack) + "\n")
    file.write(str(enemy_defense) + "\n")

    file.close()

    # Deixando progresso visível
    file = open("./.storage/games_count", "w")
    file.write(str(saved_games_count))
    file.close()

    return saved_games_count
