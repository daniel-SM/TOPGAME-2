from search_player_items import searchItems


def sell_items(itens_person, moedas):
    item = input("\nNº do item: ")

    aux = True
    i = 0
    while i < len(itens_person):
        if item == itens_person[i][0]:
            aux = False

            moedas += itens_person[i][3]
            texto = itens_person[i][4]
            tipo = itens_person[i][5]

            print("Venda efetuada!")
            print("Você ganhou", itens_person[i][3], "moedas")
            print("Você tem", moedas, "moedas")

            itens_person.pop(i)

            poder = searchItems(itens_person, texto, tipo)

        i += 1

    if aux:
        print("Item não encontrado!")
        itens_person, moedas, poder = sell_items(itens_person, moedas)

    return itens_person, moedas, poder, tipo
