from TOPGAME import FRAME_WIDTH  # Importando contante com tamanho dos quadros


# funcao que exibe os itens do inventario da loja
def show_items(
    store_inventory: list[
        tuple[
            str,  # code - codigo do item
            str,  # type - tipo de item
            int,  # stat - valor do atributo
            int,  # price - preco do item
        ]
    ],
    item_description: str,  # descricao do tipo de atributo, como "dano", "defesa"
) -> None:

    # loop para exibir cada item no inventario da loja
    for item in store_inventory:
        # exibindo as informacoes no formato de tabela
        print()
        print(f"||{'-'*(FRAME_WIDTH-4)}||")
        print(f"|| Código: {item[0] :>{FRAME_WIDTH-14}} ||")
        print(f"|| Tipo:   {item[1] :>{FRAME_WIDTH-14}} ||")
        print(f"|| Poder:  {f'{item[2]} de {item_description}' :>{FRAME_WIDTH-14}} ||")
        print(f"|| Valor:  {item[3] :>{FRAME_WIDTH-14}} ||")
        print(f"||{'-'*(FRAME_WIDTH-4)}||")
        input("\nEnter para continuar... ")
