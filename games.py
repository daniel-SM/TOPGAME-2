def searchSavedGames(qtdJogos):
    arquivo = 1
    while(arquivo != 0) and (arquivo <= qtdJogos) and (qtdJogos > 0):
        file = open("./Database/Dados_Salvos/"+str(arquivo),'r')
        
        print("\nN° do jogo salvo:",arquivo)
        print("Status:",file.readline().rstrip())
        print("Nome:",file.readline().rstrip())
        print("Fase:", file.readline().rstrip())
        print("Vida:",file.readline().rstrip())
        print("Vida p/ fase:",file.readline().rstrip())
        print("Ataque:",file.readline().rstrip())
        print("Defesa:",file.readline().rstrip())
        print("Magia:",file.readline().rstrip())
        print("Moedas:",file.readline().rstrip())
        itens = eval(file.readline().rstrip())
        print("Itens:",end=' ')
        print(len(itens)>0 and [itens[i][1] for i in range(0,len(itens))] or '---')
        
        file.close()
        
        input("\nEnter para continuar...")
        
        arquivo += 1
    
    jogoSalvo = input("\nN° do jogo salvo: ")
    
    while not jogoSalvo.isnumeric():
        print("Inválido!")
        jogoSalvo = input("N° da jogo salvo: ")
    
    jogoSalvo = int(jogoSalvo)
    
    while(jogoSalvo <= 0) or (jogoSalvo > qtdJogos):
        print("Inválido!")
        jogoSalvo = input("N° do jogo salvo: ")
        while not jogoSalvo.isnumeric():
            print("Inválido!")
            jogoSalvo = input("N° da jogo salvo: ")
        jogoSalvo = int(jogoSalvo)
    
    return jogoSalvo
