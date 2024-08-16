import time

def showItems(itens, texto):
    for i in range(len(itens)):
        print("")
        print(itens[i][0],"-",itens[i][1])
        print("Poder:",itens[i][2],"de",texto)
        print("Valor:",itens[i][3],"moedas")
        time.sleep(0.5)
        
        input("\nEnter para continuar...")
        print()
