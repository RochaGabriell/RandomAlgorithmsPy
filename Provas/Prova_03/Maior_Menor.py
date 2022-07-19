def maior_menor():
    lista = []
    for i in range(0, 5):
        lista.append(int(input(f"{i+1}º Valor: ")))
    maior = lista[0]
    menor = lista[0]
    for i in lista:
        if maior < i:
            maior = i
        elif menor > i:
            menor = i
    return print(f"Maior valor da lista é {maior}, e o menor valor é: {menor}.")

maior_menor()