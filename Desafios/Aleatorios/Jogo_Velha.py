velha = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
velha_espelho = [1, 2, 3, 4, 5, 6, 7, 8, 9]

jogadas = 0
jogador = "X"

while True:
    for i in range(0, 8, 3):
      print(f"{' | '.join(map(str, velha[i:i+3])):^20} - {' | '.join(map(str, velha_espelho[i:i+3])):^20}")
    
    if jogadas == 9:
        print("Deu velha!")
        break

    jogada = int(input(f"\nJogador {jogador}: "))
    
    if jogada < 1 or jogada > 9:
        print("Posição Inválida!")
        continue
    if velha[jogada-1] == "X" or velha[jogada-1] == "O":
        print("Posição Ocupada!")
        continue

    velha[jogada-1] = jogador
    
    # Possibilidade de Ganho na Horizontal
    if velha[0] == "X" and velha[1] == "X" and velha[2] == "X" or velha[0] == "O" and velha[1] == "O" and velha[2] == "O":
        print(f"Jogador {jogador} GANHOU!")
        break
    if velha[3] == "X" and velha[4] == "X" and velha[5] == "X" or velha[3] == "O" and velha[4] == "O" and velha[5] == "O":
        print(f"Jogador {jogador} GANHOU!")
        break
    if velha[6] == "X" and velha[7] == "X" and velha[8] == "X" or velha[6] == "O" and velha[7] == "O" and velha[8] == "O":
        print(f"Jogador {jogador} GANHOU!")
        break

    # Possibilidade de Ganho na Vertical
    if velha[0] == "X" and velha[3] == "X" and velha[6] == "X" or velha[0] == "O" and velha[3] == "O" and velha[6] == "O":
        print(f"Jogador {jogador} GANHOU!")
        break
    if velha[1] == "X" and velha[4] == "X" and velha[7] == "X" or velha[1] == "O" and velha[4] == "O" and velha[7] == "O":
        print(f"Jogador {jogador} GANHOU!")
        break
    if velha[2] == "X" and velha[5] == "X" and velha[8] == "X" or velha[2] == "O" and velha[5] == "O" and velha[8] == "O":
        print(f"Jogador {jogador} GANHOU!")
        break

    # Possibilidade de Ganho na Diagonal
    if velha[0] == "X" and velha[4] == "X" and velha[8] == "X" or velha[0] == "O" and velha[4] == "O" and velha[8] == "O":
        print(f"Jogador {jogador} GANHOU!")
        break
    if velha[2] == "X" and velha[4] == "X" and velha[6] == "X" or velha[2] == "O" and velha[4] == "O" and velha[6] == "O":
        print(f"Jogador {jogador} GANHOU!")
        break
    
    jogador = "X" if jogador == "O" else "O"
    jogadas += 1