def retur():
    nome = "Bob"
    idade = 20

    return nome, idade

lista = list(retur())

print(", ".join(map(str, lista)))