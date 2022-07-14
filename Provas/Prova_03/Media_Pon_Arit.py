def notas():
    notas_dados = []
    for i in range(0, 3):
        notas_dados.append(int(input(f"{i+1}º Nota: ")))
    op = str(input("Opção (A, P): "))
    if op in "Aa":
        return media_aritmetica(notas_dados)
    if op in "Pp":
        return media_ponderada(notas_dados)
    else:
        print("Opção errada!")

def media_aritmetica(notas_dados):
    media = sum(notas_dados) / len(notas_dados)
    print(f"Média Aritmética do Aluno é: {media:.1f}")

def media_ponderada(notas_dados):
    media = ((notas_dados[0] * 5)+(notas_dados[0] * 3)+(notas_dados[0] * 2)) / 10
    print(f"Média Ponderada do Aluno é: {media:.1f}")

notas()