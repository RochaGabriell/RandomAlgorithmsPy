def mes_extenso(data):
    mes_nome = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
    print(len(mes_nome))
    return print(f"{data[0]}/{mes_nome[data[1]-1]}/{data[2]}")

data = []
data = list(map(int, input(f"DD/MM/AA: ").split("/")))
mes_extenso(data)