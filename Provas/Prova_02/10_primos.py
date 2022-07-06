lista_primos = []
n = 100
cont = 0

while cont < 10:
    n += 1
    divisor = 0

    for j in range(1, n+1):
        if n % j == 0:
            divisor += 1
    if divisor == 2:
        lista_primos.append(n)
        cont += 1
            
print(lista_primos)