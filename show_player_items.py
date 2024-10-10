def show_player_items(player_items: list[tuple[str, str, int, int, str, int]]) -> None:
    for item in player_items:
        print()
        print(item[0], "-", item[1])
        print("Poder:", item[2], "de", item[4])
        print("Valor:", item[3], "moedas")
        input("\nEnter para continuar... ")
