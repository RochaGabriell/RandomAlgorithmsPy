a = []
a_aux = []
cont = 0

for i in range(5):
    a.append(int(input()))

for i in range(len(a)):
    if a[i] not in a_aux:
        a_aux.append(a[i])

for i in range(len(a_aux)):
    cont = 0
    for j in range(len(a)):
        if a[j] == a_aux[i]:
            cont += 1
    print(f"O numero {a_aux[i]} se repete {cont} vezes;")