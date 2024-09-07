import time


def show_purchased_items(itens_person):
    for i in range(len(itens_person)):
        print("")
        print(itens_person[i][0], "-", itens_person[i][1])
        print("Poder:", itens_person[i][2], "de", itens_person[i][4])
        print("Valor:", itens_person[i][3], "moedas")
        time.sleep(0.5)

        input("\nEnter para continuar...")
        print("")
