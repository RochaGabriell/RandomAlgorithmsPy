array = []

while True:
  print(f"""
  |{'-' * 20}|
  |{'Menu':^20}|
  |{'1 - Inserir':^20}|
  |{'2 - Deletar':^20}|
  |{'3 - Exibir':^20}|
  |{'4 - Maior Valor':^20}|
  |{'5 - Sair':^20}|
  |{'-' * 20}|
  """)

  op = int(input("Opção: "))

  if op == 1:
    array.append(int(input("Valor: ")))

  elif op == 2:
    deletar = int(input("Valor a ser deletado: "))
    if deletar in array:
      array.remove(deletar)
    else:
      print("Valor informado não consta na lista.")

  elif op == 3:
    '''
    array.sort()
    print(f"Lista ordem crescente: {', ' .join(map(str, array))}")
    '''
    array_temp = []
    for i in range(len(array)):
      if i == 0 or array[i] > array_temp[-1]:
        array_temp.append(array[i])
      else:
        for j in range(len(array_temp)):
          if array[i] <= array_temp[j]:
            array_temp.insert(j, array[i])
            break
    print(f"Lista ordem crescente: {', ' .join(map(str, array_temp))}")
    array_temp.clear()
    '''
    Na aula dia 30 de maio
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                aux = array[j]
                array[j] = array[j+1]
                array[j+1] = aux
    print(f"Lista ordem crescente: {', ' .join(map(str, array))}")
    '''

  elif op == 4:
    '''
    array.sort(reverse = True)
    print(f"Maior Valor da Lista {array[0]}")
    '''
    maior = 0
    for i in range(len(array)):
      if array[i] > maior:
        maior = array[i]
    print(f"Maior Valor da Lista {maior}.")

  elif op == 5:
    print("Finalizando Programa...")
    break

  else:
    print("Opção errada...")