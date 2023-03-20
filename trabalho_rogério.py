
#TRABALHO DO ROGÉRIO.
# Escreva um algoritmo que exiba um menu para o usuário com as opções: 
# Tamanho do Vetor, Armazenar Valores, Ordenar Valores
# Tipo de Pesquisa, Pesquisar e Sair; e implemente essas funcionalidades.

vet =[]
tamanho=0
#perguntamos para o usuario o tamanho do vetor desejado
def tamanho_vetor():
  global tamanho
  tamanho = int(input("Qual o tamanho do vetor?\n"))

#armazenamos valores dentro do vetor criado.
def armazenar_valores():
  for i in range(tamanho):
    vet[i] = int(input(f"Digite o {i+1} valor:"))

#realizamos a ordenação dos valores atravez do metodo bubble sort
def bubble_sort(tamanho):
  for j in range(tamanho-1):
    for i in range(tamanho-j-1):  
      if vet[i]>vet[i+1]:
        aux=vet[i+1]                    
        vet[i+1]=vet[i]
        vet[i]=aux
#realizamos a ordenação dos valores atravez do metodo insertion sort
def insertion_sort(tamanho):
  for i in range (1,tamanho):
    aux = vet[i]
    j = i
    while (j > 0 and vet[j-1] > aux):
      vet[j] = vet[j-1]
      j -= 1
    vet[j] = aux
#realizamos a ordenação dos valores atravez do metodo selection sort
def selection_sort(tamanho):
  for i in range(tamanho - 1):
    cont = i
    for j in range(i + 1, tamanho):
      if vet[j] < vet[cont]:
        cont = j
    aux = vet[i]
    vet[i] = vet[cont]
    vet[cont] = aux
#realizamos uma pesquisa atravez do metodo pesquisa sequencial.
def pesquisa_sequencial(tamanho):
  entrada = int(input("Qual numero você quer encontrar?"))
  achou = False
  i=0
  while i<=tamanho and achou == False:
    if vet[i] == entrada:
      achou = True
      print(f"O seu numero esta na posição {i} ")
    else:
      i += 1
  if achou == False:
    print("Numero não encontrado")
#realizamos uma pesquisa atravez do metodo pesquisa binária.
def pesquisa_binaria(tamanho):
  entrada = int(input("Qual numero você quer encontrar? "))

  tam = tamanho-1
  i = 0

  while i <= tam:
    cont = int((i+tam)/ 2)

    if(vet[cont] == entrada):
      print(f"O seu numero esta na posição {cont} ")
      break
    if(vet[cont] < entrada):
      i = cont+1
    else:
      tam = cont - 1

#Programa de interação com o usuario.
while True:
  print("\nBem vindo ao seu programa, selecione uma operação\n")
  print("1- Tamanho do Vetor\n")
  print("2- Armazenar Valores\n")
  print("3- Ordenar Valores\n")
  print("4- Tipo de Pesquisa\n")
  print("5- Pesquisar\n")
  print("6- Sair\n")
  opcao=int(input())
  if opcao==1:
    tamanho_vetor()
    vet= [0]*tamanho
    print(f"\no seu vetor tem {tamanho} posicoes\n")
  elif opcao==2:
    armazenar_valores()
    print(vet)
  elif opcao==3:
    print("\nQual tipo de ordenação voce quer realizar?\n")
    operacao=int(input("\n1-Bubble sort\n2-Insertion sort\n3-Selection sort\n"))
    if operacao==1:
      bubble_sort(tamanho)
      print(f"\nvetor ordenado\n {vet}\n")
    if operacao == 2:
      insertion_sort(tamanho)
      print(f"\nVetor ordenado:\n {vet}")
    if operacao == 3:
      selection_sort(tamanho)
      print(vet)
  elif opcao==6:
    print("\nEncerrando o programa...\n")
    break
  elif opcao==4:
    print("\nQual tipo de pesquisa você quer realizar?\n")
    tipo=int(input("\n1-Pesquisa sequencial\n2-Pesquisa binaria\n"))
    if tipo==1:
      print("Pesquisa sequencial")
    else:
      print("Pesquisa binaria")
  elif opcao==5:
    if tipo==1:
      pesquisa_sequencial(tamanho)
    else:
      pesquisa_binaria(tamanho)
  else:
    print("Opcao nao existente")