def string(qtd):
    cadeia_str = []
    for i in range(0, qtd):
        aux = list(map(str, input().split()))
        cadeia_str.append(aux[:])
    return combinador(cadeia_str)

def combinador(cadeia_str):
    for i in range(len(cadeia_str)):
        troca = []
        aux = list(cadeia_str[i][0])
        aux2 = list(cadeia_str[i][1])
        for j in range(len(aux)):
            lala = []
            lala.append(aux[j]+aux2[j])
            troca += lala
        t = ''.join(map(str, troca))
        print(t)

qtd = int(input())
string(qtd)