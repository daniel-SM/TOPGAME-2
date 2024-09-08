import time


def show_items(store_items, item_description):
    for item in store_items:
        print()
        print(item[0], "-", item[1])
        print("Poder:", item[2], "de", item_description)
        print("Valor:", item[3], "moedas")
        input("\nEnter para continuar...")
