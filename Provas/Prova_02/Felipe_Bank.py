aux = []
bank = [["503", 200.0], ["504", 100.0]]

for i in range(10):
    aux.append(input(f"Cod: "))
    aux.append(float(input(f"Saldo da Conta: ")))
    bank.append(aux[:])
    aux.clear()

while True:
    print("""
Menu: 
A - Depósito
B - Saque
C - Ativo Bancário
D - Sair
    """)

    for i in range(len(bank)):
        print(bank[i])

    print()
    op = str(input("Opção: "))
    print()

    if op in "Aa":
        print("Depósito")
        conta = str(input("Conta: "))
        existe = False
        for i in range(len(bank)):
            if bank[i][0] == conta:
                print(f"Saldo Atual: R$ {bank[i]} ")
                deposito = float(input("Valor do Deposito: R$ "))
                bank[i][1] += deposito
                print(f"Novo deposito na conta {bank[i]}")
                existe = True
        if existe == False:
            print("Conta não existe.")
    
    if op in "Bb":
        print("Saque")
        conta = str(input("Conta: "))
        existe = False
        for i in range(len(bank)):
            if bank[i][0] == conta:
                print(f"Saldo Atual: R$ {bank[i]} ")
                saque = float(input("Valor Sacado: R$ "))
                if saque <= bank[i][1] and saque >= 0: 
                    bank[i][1] -= saque
                    print(f"Novo saque na conta {bank[i]}")
                else:
                    print("Vc n tem dinheiro.")
                existe = True
        if existe == False:
            print("Conta não existe.")

    if op in "Cc":
        print("Ativo Bancário")
        atv_bank = 0
        for i in range(len(bank)):
            atv_bank += bank[i][1]
        print(f"Saldo banco: R$ {atv_bank:.2f}")

    if op in "Dd":
        print("Sair...")
        break

    if op not in "AaBbCcDd":
        print("Op errada!")