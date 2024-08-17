import time
from clear import clearScreen

from market import market
from fight import fight
from option import validateOption
from storage import saveToStorage

def battleManager(
    qtdJogos, 
    nome, 
    itensPerson, 
    lifeRegen, 
    life, 
    lifeInim, 
    magia, 
    ataque, 
    ataqueInim, 
    defesa, 
    defesaInim, 
    moedas, 
    jogoSalvo, 
    n
):
    clearScreen(100)
    
    print("||--------##--------##--------##----||")
    print("||             FASE ",n+1,"               ||",sep="")
    print("||--------##--------##--------##----||")
    time.sleep(1)
    
    print("\n||--------------------||")
    print("||    VOCÊ")
    print("||    Vida-->",life)
    print("||    Ataque-->",ataque)
    print("||    Defesa-->",defesa)
    print("||    Magia-->",magia)
    print("||    Moedas-->",moedas)
    print("||--------------------||")
    print("||    MONSTRO",n+1)
    print("||    Vida-->",lifeInim)
    print("||    Ataque-->",ataqueInim)
    print("||    Defesa-->",defesaInim)
    print("||--------------------||")
    time.sleep(4)
    
    aumentar = True
    fim = False
    acao= ""
    while(acao != "1"):
        print("\n||------------------------||")
        print("||   AÇÕES:               ||")
        print("||   1. Começar Batalha   ||")
        print("||   2. Ir pro Mercado    ||")
        print("||   3. Seu Status        ||")
        print("||   4. Salvar Progresso  ||")
        print("||   5. Sair do Jogo      ||")
        print("||------------------------||")

        acao= input("\nAção: ")

        if(acao == "1"):
            print("\nComeçar fight!")
            desejo= input("\nQuer mesmo começar a fight?\n(S: sim) ou (N: não): ")
            desejo= validateOption(desejo)
            if(desejo == "s"):
                print("\n||--------------------||")
                print("||       BATALHA      ||")
                print("||--------------------||\n")
        
                life,magia,moedas,n,aumentar = fight(life,lifeInim,ataque,ataqueInim,defesa,defesaInim,magia,moedas,n)
                time.sleep(2)
            else:
                acao= ""
                clearScreen(10)
        
        elif(acao == "2"):
            itensPerson,moedas,life,ataque,defesa,lifeRegen,magia= market(itensPerson,moedas,life,ataque,defesa,lifeRegen,magia)
            time.sleep(2)
            clearScreen(10)
        
        elif(acao == "3"):
            clearScreen(10)
            print("\n||--------------------||")
            print("||    VOCÊ            ||")
            print("||    Vida-->",life)
            print("||    Ataque-->",ataque)
            print("||    Defesa-->",defesa)
            print("||    Magia-->",magia)
            print("||    Moedas-->",moedas)
            print("||--------------------||")
            print("||    MONSTRO",n+1)
            print("||    Vida-->",lifeInim)
            print("||    Ataque-->",ataqueInim)
            print("||    Defesa-->",defesaInim)
            print("||--------------------||")
            time.sleep(4)
    
        elif(acao == "4"):
            desejo = input("\nSalvar o progresso?\n(S: sim) ou (N: não): ")
            desejo = validateOption(desejo)
            
            if(desejo == 's'):
                print("\nSalvando seu progresso...")
                time.sleep(1)
                
                if(jogoSalvo):
                    saveToStorage(True,qtdJogos,jogoSalvo,"PAUSADO",nome,n,life,lifeRegen,ataque,defesa,magia,moedas,itensPerson,lifeInim,ataqueInim,defesaInim)
                else:
                    jogoSalvo = qtdJogos+1
                    qtdJogos += 1
                    saveToStorage(True,qtdJogos,jogoSalvo,"PAUSADO",nome,n,life,lifeRegen,ataque,defesa,magia,moedas,itensPerson,lifeInim,ataqueInim,defesaInim)

            clearScreen(10)
        
        elif(acao == "5"):
            desejo = input("\nQuer mesmo sair do jogo?\n(S: sim) ou (N: não): ")
            desejo = validateOption(desejo)
            
            if(desejo == 's'):
                print("\nSaindo do jogo...")
                
                print("\n||----------------------||")
                print("||                      ||")
                print("||  VOCÊ SAIU DO JOGO!  ||")
                print("||                      ||")
                print("||----------------------||")
                time.sleep(1)
                
                file = open("storage/emulated/0/qpython/projects3/TOPGAME/Database/dados_Jogos.txt",'w')
                
                fim = True
                return itensPerson,moedas,ataque,defesa,magia,life,lifeRegen,n,fim,aumentar
        else:
            print("\nInválido!")
            time.sleep(1)
            clearScreen(10)
        
        
    return itensPerson,moedas,ataque,defesa,magia,life,lifeRegen,n,fim,aumentar
