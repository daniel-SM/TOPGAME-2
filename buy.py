import time


def buy_items(itens_person, itens, moedas, poder, texto, num=None, teste=False):
    item = input("\nNº do item: ")

    aux = True
    for i in range(len(itens)):
        if item == itens[i][0]:
            aux = False

            if moedas - itens[i][3] >= 0:
                moedas -= itens[i][3]
                poder = itens[i][2]
                if teste:
                    itens_person.append(
                        [
                            itens[i][0],
                            itens[i][1],
                            itens[i][2],
                            int(itens[i][3] * 0.75),
                            texto,
                            num,
                        ]
                    )
                print("\nCompra efetuada!")
                print(
                    "Você possui o item",
                    itens[i][1],
                    "\nE seu poder é",
                    itens[i][2],
                    "de",
                    texto,
                )
                print("O item custou", itens[i][3], "moedas")
                if moedas > 0:
                    print("\nVocê possui", moedas, "moedas!")
                else:
                    print("\nSeu dinheiro acabou!")
                    break

            elif moedas > 200:
                print("\nMoedas insuficientes!")
                itens_person, moedas, poder = buy_items(
                    itens_person, itens, moedas, poder, texto, num, teste
                )
            else:
                print("\nMoedas insuficientes!")
                print("Impossível comprar outro item!")
                print("Você está saindo do mercado...")
                time.sleep(1)
                break

    if aux:
        print("\nItem não encontrado!")
        itens_person, moedas, poder = buy_items(
            itens_person, itens, moedas, poder, texto, num, teste
        )

    return itens_person, moedas, poder
