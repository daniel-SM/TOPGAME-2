def validateOption(desejo):
    desejo= desejo.lower()
    while(desejo != "s" and desejo != "n"):
        print("Inválido!")
        desejo= input("(S - sim) ou (N - não): ")
        desejo= desejo.lower()
    return desejo
