def save_to_storage(
    saving,
    qtd_jogos,
    num_jogo,
    titulo,
    nome,
    fase,
    life,
    life_regen,
    ataque,
    defesa,
    magia,
    moedas,
    itens,
    life_inim,
    ataque_inim,
    defesa_inim,
):

    file = open("./storage/saved_games/" + str(num_jogo), "w")

    file.write(str(titulo) + "\n")
    file.write(str(nome) + "\n")
    file.write(str(fase) + "\n")
    file.write(str(life) + "\n")
    file.write(str(life_regen) + "\n")
    file.write(str(ataque) + "\n")
    file.write(str(defesa) + "\n")
    file.write(str(magia) + "\n")
    file.write(str(moedas) + "\n")
    file.write(str(itens) + "\n")
    file.write(str(life_inim) + "\n")
    file.write(str(ataque_inim) + "\n")
    file.write(str(defesa_inim) + "\n")

    file.close()

    # Deixando progresso visível
    file = open("./storage/game_info.txt", "w")
    file.write(str(saving) + "\n")
    file.write(str(qtd_jogos))
    file.close()
