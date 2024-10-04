def show_items(store_items, item_description):
    # Definindo o tamanho da largura do quadro
    WIDTH = 40

    for item in store_items:
        print()
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"|| Código: {item[0] :>{WIDTH-14}} ||")
        print(f"|| Tipo:   {item[1] :>{WIDTH-14}} ||")
        print(f"|| Poder:  {f'{item[2]} de {item_description}' :>{WIDTH-14}} ||")
        print(f"|| Valor:  {item[3] :>{WIDTH-14}} ||")
        print(f"||{'-'*(WIDTH-4)}||")

        input("\nEnter para continuar... ")
