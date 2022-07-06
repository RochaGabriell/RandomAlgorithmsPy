def Validar_cpf(str_cpf):
    # Faz a separação dos "." e "-".
    mod = str_cpf.replace("-" , "")
    cpf = list(map(int, mod.replace("." , "")))

    # Validação do primeiro dígito
    soma_01 = 0
    desc_01 = 10

    for i in range(0, 9):
        soma_01 += cpf[i] * desc_01
        desc_01 -= 1

    verificar_01 = (soma_01 * 10) % 11

    # Se o resto da divisão for igual a 10, nós o consideramos como 0.
    if verificar_01 == 10:
        verificar_01 = 0
    
    # Validação do segundo dígito
    if verificar_01 == cpf[9] or verificar_01 == 10:
        soma_02 = 0
        desc_02 = 11

        for i in range(0, 10):
            soma_02 += cpf[i] * desc_02
            desc_02 -= 1
        
        verificar_02 = (soma_02 * 10) % 11

    verificar_03 = cpf.count(cpf[0])

    print("CPF é válido") if verificar_01 == cpf[9] and verificar_02 == cpf[10] and verificar_03 < len(cpf) else print("CPF não é válido")

Validar_cpf(str(input("CPF: ")))