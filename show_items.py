import time


def show_items(store_items, item_description):
    # Definindo o tamanho da largura do quadro
    width = 40

    for item in store_items:
        print()
        print(f"||{'-'*(width-4)}||")
        print(f"|| Código: {item[0] :>{width-14}} ||")
        print(f"|| Tipo:   {item[1] :>{width-14}} ||")
        print(f"|| Poder:  {f'{item[2]} de {item_description}' :>{width-14}} ||")
        print(f"|| Valor:  {item[3] :>{width-14}} ||")
        print(f"||{'-'*(width-4)}||")

        input("\nEnter para continuar... ")
