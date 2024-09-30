# Funcao para validar opcao digitada
def validate_option(option):
    option = option.lower()

    while option != "s" and option != "n":
        print("\nInválido!")
        option = input("S - sim\nN - não\nDigite novamente: ")
        option = option.lower()

    return option
