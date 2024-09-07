def validate_option(option):
    option = option.lower()
    while option != "s" and option != "n":
        print("Inválido!")
        option = input("(S - sim) ou (N - não): ")
        option = option.lower()
    return option
