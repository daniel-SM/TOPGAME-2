import time

def showPurchasedItems(itensPerson):
    for i in range(len(itensPerson)):
        print("")
        print(itensPerson[i][0],"-",itensPerson[i][1])
        print("Poder:",itensPerson[i][2],"de",itensPerson[i][4])
        print("Valor:",itensPerson[i][3],"moedas")
        time.sleep(0.5)
        
        input("\nEnter para continuar...")
        print("")
