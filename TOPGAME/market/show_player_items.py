# funcao para exibir os itens possuidos pelo jogador
def show_player_items(
    player_items: list[
        tuple[
            str,  # code - codigo do item
            str,  # type description - descricao do tipo de item
            int,  # stat - valor do atributo
            int,  # selling price - preco de venda do item
            str,  # stat description - descrição do atributo (como "dano", "defesa", etc.)
            int,  # type code - codigo do tipo de item
        ]
    ]
) -> None:
    # loop que percorre a lista de itens do jogador
    for item in player_items:
        # exibindo as informacoes no formato de tabela
        print()
        print(item[0], "-", item[1])
        print("Poder:", item[2], "de", item[4])
        print("Valor:", item[3], "moedas")
        input("\nEnter para continuar... ")
