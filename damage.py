import random

from suspense import makeSuspense

def calculateAttack(jog, life, ataque, defesa, magia = 0):
    fim= False
    
    divisor= random.choice([1,2,2,2,2,5,5,5,5,5,5,10])
    multiplo= random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
    
    if(ataque-defesa > 0):
        dano= (((ataque-defesa)//divisor)*multiplo)+magia
        life-= dano
        
        if(dano > 0): 
            if(jog == 0): 
                print("\nO dano do seu ataque foi",dano)
                if(life > 0): 
                    print("A vida atual do seu inimigo é",life)
                    makeSuspense(0.5)
                else: 
                    print("\nSEU INIMIGO MORREU!!!\nVOCÊ VENCEU!!!\n")
                    fim= True
            else: 
                print("\nO dano sofrido foi",dano)
                if(life > 0): 
                    print("Sua vida atual é",life)
                    makeSuspense(0.5)
                else: 
                    print("\nVOCÊ MORREU!!!\n")
                    fim= True
                   
        else:
            if(jog == 0):
                print("O seu ataque falhou!")
                print("Seu inimigo não teve dano!")
                print("A vida atual do seu inimigo é",life)
                makeSuspense(0.6)
            else:
                print("O ataque do seu inimigo falhou!")
                print("Você não teve dano!")
                print("Sua vida atual é",life)
                makeSuspense(0.6)
    elif(magia > 0):
        dano= magia
        life-= dano
        
        if(dano > 0): 
            if(jog == 0): 
                print("\nO dano do seu ataque foi",dano)
                if(life > 0): 
                    print("A vida atual do seu inimigo é",life)
                    makeSuspense(0.5)
                else: 
                    print("\nSEU INIMIGO MORREU!!!\nVOCÊ VENCEU!!!\n")
                    fim= True
            else: 
                print("\nO dano sofrido foi",dano)
                if(life > 0): 
                    print("Sua vida atual é",life)
                    makeSuspense(0.5)
                else: 
                    print("\nVOCÊ MORREU!!!\n")
                    fim= True
    else:
        dano= 0
        life-= dano
        if(jog == 0):
            print("O seu ataque falhou!")
            print("Seu inimigo não teve dano!")
            print("A vida atual do seu inimigo é",life)
            makeSuspense(0.6)
        else:
            print("O ataque do seu inimigo falhou!")
            print("Você não teve dano!")
            print("Sua vida atual é",life)
            makeSuspense(0.6)
    
    return life,fim

    

