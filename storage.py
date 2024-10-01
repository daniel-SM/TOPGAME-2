def save_to_storage(
    saved_games_count,
    player_name,
    phase,
    player_life,
    player_life_regen,
    player_attack,
    player_defense,
    player_magic,
    coins,
    player_items,
    enemy_life,
    enemy_attack,
    enemy_defense,
):
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
    file = open("./.storage/games_count.txt", "w")
    file.write(str(saved_games_count))
    file.close()
