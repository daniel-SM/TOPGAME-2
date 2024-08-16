def saveToStorage(
    saving, 
    qtdJogos, 
    numJogo, 
    titulo, 
    nome, 
    fase, 
    life, 
    lifeRegen, 
    ataque, 
    defesa, 
    magia, 
    moedas, 
    itens, 
    lifeInim, 
    ataqueInim, 
    defesaInim
):
    file = open("./Database/Dados_Salvos/"+str(numJogo), 'w')
    
    file.write(str(titulo) + "\n")
    file.write(str(nome) + "\n")
    file.write(str(fase) + "\n")
    file.write(str(life) + "\n")
    file.write(str(lifeRegen) + "\n")
    file.write(str(ataque) + "\n")
    file.write(str(defesa) + "\n")
    file.write(str(magia) + "\n")
    file.write(str(moedas) + "\n")
    file.write(str(itens) + "\n")
    file.write(str(lifeInim) + "\n")
    file.write(str(ataqueInim) + "\n")
    file.write(str(defesaInim) + "\n")
    
    file.close()

    # Deixando progresso visível
    file = open("./Database/dadosGame.txt", 'w')
    file.write(str(saving) + "\n")
    file.write(str(qtdJogos))
    file.close()
