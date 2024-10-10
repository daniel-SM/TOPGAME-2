# Funcao para validar opcao respostas das perguntas de sim ou nao
def validate_option(option: str) -> str:
    option = option.lower()

    while option != "s" and option != "n":
        print("\nInválido!")
        option = input("S - sim\nN - não\nDigite novamente: ")
        option = option.lower()

    return option
