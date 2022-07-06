def maior(*lista): # tuple
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

ele = maior(10, -22, -3, 4, 5, 0) # Sem valores determinados
print(ele)