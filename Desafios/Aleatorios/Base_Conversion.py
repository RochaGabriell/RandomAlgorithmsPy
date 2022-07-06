def Menu():
    op = ""
    
    while op != "0":
        print(f"\n {'-'*40:^40}")
        print(f"|{'OPÇÕES':^40}|")
        print(f"|{'[1] - CONVERTER BINÁRIO PARA DECIMAL':^40}|")
        print(f"|{'2 - CONVERTER DECIMAL PARA BINÁRIO':^40}|")
        
        print(f"|{'3 - CONVERTER OCTAL PARA DECIMAL':^40}|")
        print(f"|{'4 - CONVERTER DECIMAL PARA OCTAL':^40}|")

        print(f"|{'5 - CONVERTER HEXADECIMAL PARA DECIMAL':^40}|")
        print(f"|{'6 - CONVERTER DECIMAL PARA HEXADECIMAL':^40}|")

        print(f"|{'7 - CONVERTER BINÁRIO PARA HEXADECIMAL':^40}|")
        print(f"|{'8 - CONVERTER HEXADECIMAL PARA BINÁRIO':^40}|")

        print(f"|{'9 - CONVERTER BINÁRIO PARA OCTAL':^40}|")
        print(f"|{'10 - CONVERTER OCTAL PARA BINÁRIO':^40}|")
        print(f"|{'0 - SAIR DO SISTEMA':^40}|")
        print(f" {'-'*40:^40}\n")
        
        op = str(input("INSIRA OPÇÃO: "))
        
        if op == "1":
            n = str(input("INSIRA BINÁRIO: "))
            return Binario_Decimal(n)
        elif op == "2":
            n = str(input("INSIRA DECIMAL: "))
            return Decimal_Binario(n)

        elif op == "3":
            n = str(input("INSIRA OCTAL: "))
            return Octal_Decimal(n)
        elif op == "4":
            n = str(input("INSIRA DECIMAL: "))
            return Decimal_Octal(n)

        elif op == "5":
            n = str(input("INSIRA HEXADECIMAL: "))
            return Hexadecimal_Decimal(n)
        elif op == "6":
            n = str(input("INSIRA DECIMAL: "))
            return Decimal_Hexadecimal(n)
        
        elif op == "7":
            n = str(input("INSIRA BINÁRIO: "))
            return Binario_Hexadecimal(n)
        elif op == "8":
            n = str(input("INSIRA HEXADECIMAL: "))
            return Hexadecimal_Binario(n)

        elif op == "9":
            n = str(input("INSIRA BINÁRIO: "))
            return Binario_Octal(n)
        elif op == "10":
            n = str(input("INSIRA OCTAL: "))
            return Octal_Binario(n)

        elif op not in "012345678910":
            print(f"\n{'OP ERRADA! TENTE NOVAMENTE...':^40}")
    
    print(f"\n{'FECHANDO... SISTEMA...':^40}")

def Binario_Decimal(n):
    binario = list(map(int, n))
    cont = len(binario)-1
    soma = 0

    for i in range(len(binario)):
        soma += binario[i] * (2 ** (cont-i))

    print(f"RESULTADO DA CONVERSÃO PARA DECIMAL:\n{f'{n} (bin) = {soma} (dec)'}")
    
    return Menu()

def Decimal_Binario(n):
    div = int(n)
    resto = []

    while True:
        cal = div%2
        div = int(div/2)
        resto.append(int(cal))
        if div < 2:
            resto.append(div)
            break

    print(f"RESULTADO DA CONVERSÃO PARA BINÁRIO: ")
    print(f"{n} (dec) = {''.join(map(str, resto[::-1]))} (bin)")
    
    return Menu()

def Octal_Decimal(n):
    octal = list(map(int, n))
    cont = len(octal)-1
    soma = 0

    for i in range(len(octal)):
        soma += octal[i] * (8 ** (cont-i))

    print(f"RESULTADO DA CONVERSÃO PARA DECIMAL:\n{f'{n} (octal) = {soma} (dec)'}")

    return Menu()

def Decimal_Octal(n):
    div = int(n)
    resto = []

    while True:
        cal = div%8
        div = int(div/8)
        resto.append(int(cal))
        if div < 8:
            resto.append(div)
            break

    print(f"RESULTADO DA CONVERSÃO PARA BINÁRIO: ")
    print(f"{n} (dec) = {''.join(map(str, resto[::-1]))} (octal)")

    return Menu()

def Hexadecimal_Decimal(n):
    list_hex = ["A", "B", "C", "D", "E", "F"]
    espelho_list_hex = [10, 11, 12, 13, 14, 15]
    hexadecimal = list(n)
    
    for i in range(len(hexadecimal)):
        for j in range(0, len(list_hex)):
            if hexadecimal[i] == list_hex[j]:
                hexadecimal[i] = espelho_list_hex[j]
    
    cont = len(hexadecimal)-1
    soma = 0

    for i in range(len(hexadecimal)):
        soma += int(hexadecimal[i]) * (16 ** (cont-i))

    print(f"RESULTADO DA CONVERSÃO PARA DECIMAL:\n{f'{n} (hex) = {soma} (dec)'}")
    
    return Menu()
    
def Decimal_Hexadecimal(n):
    div = int(n)
    resto = []

    while True:
        cal = div%16
        div = int(div/16)
        resto.append(int(cal))
        if div < 16:
            resto.append(div)
            break
    
    list_hex = [10, 11, 12, 13, 14, 15]
    espelho_list_hex = ["A", "B", "C", "D", "E", "F"]
    for i in range(len(resto)):
        for j in range(len(list_hex)):
            if resto[i] == list_hex[j]:
                resto[i] = espelho_list_hex[j]

    print(f"RESULTADO DA CONVERSÃO PARA BINÁRIO: ")
    print(f"{n} (dec) = {''.join(map(str, resto[::-1]))} (hex)")

    return Menu()

def Binario_Hexadecimal(n):
    return Menu()

def Binario_Octal(n):
    binario =[]
    tabela_binaria = ["000", "001", "010", "011", "100", "101", "110", "111"]

    for i in range(0, len(n), 3):
        binario.append(n[i:i+3])
    
    for i in range(len(binario)):
        for j in range(len(tabela_binaria)):
            if binario[i] == tabela_binaria[j]:
                binario[i] = j
    
    print(f"{''.join(map(str, binario))}")

    return Menu()
    
def Hexadecimal_Binario(n):
    hexadecimal = list(n)
    tabela_binaria = ["000", "001", "010", "011", "100", "101", "110", "111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
    binario = []

    list_hex = ["A", "B", "C", "D", "E", "F"]
    espelho_list_hex = [10, 11, 12, 13, 14, 15]
    
    for i in range(len(hexadecimal)):
        for j in range(0, len(list_hex)):
            if hexadecimal[i] == list_hex[j]:
                hexadecimal[i] = espelho_list_hex[j]
    
    aux = list(map(int, hexadecimal))

    for i in aux:
        binario.append(tabela_binaria[i])
    
    print(f"{''.join(map(str, binario))}")

    return Menu()

def Octal_Binario(n):
    octal = list(map(int, n))
    tabela_binaria = ["000", "001", "010", "011", "100", "101", "110", "111"]
    binario = []

    for i in octal:
        binario.append(tabela_binaria[i])

    print(f"{''.join(map(str, binario))}")
    
    return Menu()

Menu()