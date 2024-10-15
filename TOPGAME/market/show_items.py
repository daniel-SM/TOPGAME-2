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
    # definindo o tamanho da largura do quadro
    WIDTH = 40

    # loop para exibir cada item no inventario da loja
    for item in store_inventory:
        # exibindo as informacoes no formato de tabela
        print()
        print(f"||{'-'*(WIDTH-4)}||")
        print(f"|| Código: {item[0] :>{WIDTH-14}} ||")
        print(f"|| Tipo:   {item[1] :>{WIDTH-14}} ||")
        print(f"|| Poder:  {f'{item[2]} de {item_description}' :>{WIDTH-14}} ||")
        print(f"|| Valor:  {item[3] :>{WIDTH-14}} ||")
        print(f"||{'-'*(WIDTH-4)}||")
        input("\nEnter para continuar... ")
