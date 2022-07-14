def regras():
    print(f"|-------------------------------------------------|")
    print(f"Torre de Hanói\n")
    print(f"Esse jogo tem como objetivo deslocar todos os discos de um pilar para outro qualquer, obedecendo a duas regras:\n")
    print(f"(1) Mover apenas um disco por vez.")
    print(f"(2) Um disco com diâmetro maior nunca pode ficar sobre um disco com diâmetro menor.\n")
    print(f"Instruções para jogar:\n")
    print(f"- Para mover um disco, informe o valor dele, em seguida, informe a torre para a qual ele será movido.")
    print(f"|-------------------------------------------------|\n")
    start = True
    return jogo(start)
def ganhou(movimentos):
    if movimentos == 31:
        print(f"\nFim de jogo!!!\nParabéns! Você conseguiu em 31 movimentos.")                
        return jogo(start = False)
    else:
        print(f"\nFim de jogo!!!\nVocê pode fazer melhor que isso!")
        return jogo(start = False)
def jogo(start):
    movimentos = 0
    torre_01 = [1, 2, 3, 4, 5]
    torre_02 = ["|", "|", "|", "|", "|"]
    torre_03 = ["|", "|", "|", "|", "|"]
    while start:
        for i in range(len(torre_01)):
            print(f"{torre_01[i]}".center(10), f"{torre_02[i]}".center(10), f"{torre_03[i]}".center(10))
        print(f"{'-TORRE 01-'.center(10)}{'-TORRE 02-'.center(10)}{'-TORRE 03-'.center(10)}")
        print("")
        disco = int(input("Nº do DISCO: "))
        posicao_jogada = int(input(f"Nº da TORRE: "))
        print("")
        if disco > len(torre_01):
            print("Esse disco não existe!\n")
        elif disco != torre_01[0] and disco != torre_02[0] and disco != torre_03[0]:
            print(f"Você só pode mover um disco que estiver acima!\n")
        elif posicao_jogada == 1 and disco == torre_01[0]:
            print(f"O disco {disco} já está na torre 01!\n")  
        elif posicao_jogada == 2 and disco == torre_02[0]:
            print(f"O disco {disco} já está na torre 02!\n")  
        elif posicao_jogada == 3 and disco == torre_03[0]:
            print(f"O disco {disco} já está na torre 03!\n")
        elif posicao_jogada > 3:
            print(f"Essa torre não existe!\n")
        elif posicao_jogada == 1 and disco != torre_01[0]:
            if torre_01[0] != "|" and disco > torre_01[0]:
                print(f"O disco {disco} não pode ser colocado na torre 01!\n")
            else:
                if disco in torre_02:
                    torre_02.append("|")
                    torre_02.remove(disco)
                elif disco in torre_03:
                    torre_03.append("|")
                    torre_03.remove(disco) 
                torre_01.remove(torre_01[4])
                torre_01.insert(0, disco)
                movimentos += 1       
        elif posicao_jogada == 2 and disco != torre_02[0]:
            if torre_02[0] != "|" and disco > torre_02[0]:
                print(f"O disco {disco} não pode ser colocado na torre 02!\n")
            else:
                if disco in torre_01:
                    torre_01.append("|")
                    torre_01.remove(disco)
                elif disco in torre_03:
                    torre_03.append("|")
                    torre_03.remove(disco)   
                torre_02.remove(torre_02[4])
                torre_02.insert(0, disco)
                movimentos += 1      
        elif posicao_jogada == 3 and disco != torre_03[0]:
            if torre_03[0] != "|" and disco > torre_03[0]:
                print(f"O disco {disco} não pode ser colocado na torre 03!\n")
            else:
                if disco in torre_01:
                    torre_01.append("|")
                    torre_01.remove(disco)
                elif disco in torre_02:
                    torre_02.append("|")
                    torre_02.remove(disco) 
                torre_03.remove(torre_03[4])
                torre_03.insert(0, disco)
                movimentos += 1
        print(f"Minimo de Movimentos: 31\nSeu nº de Movimentos: {movimentos}.\n")
        if  torre_02 == [1, 2, 3, 4, 5] or torre_03 == [1, 2, 3, 4, 5]:
            return ganhou(movimentos)
iniciar = regras()