def searchItems(itens_person, texto, tipo):
    aux = True

    for i in range(len(itens_person)):
        if itens_person[i][4] == texto:
            aux = False
            poder = itens_person[i][2]

    if aux:
        if tipo == 0:
            poder = 80
        elif tipo == 1:
            poder = 40
        elif tipo == 2:
            poder = 30

    return poder
