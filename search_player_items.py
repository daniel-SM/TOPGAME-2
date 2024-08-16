def searchItems(itensPerson, texto, tipo):
    aux= True
    
    for i in range(len(itensPerson)):
        if(itensPerson[i][4] == texto):
            aux= False
            poder= itensPerson[i][2]
    
    if(aux):
        if(tipo == 0):
            poder= 80
        elif(tipo == 1):
            poder= 40
        elif(tipo == 2):
            poder= 30
        
    return poder
