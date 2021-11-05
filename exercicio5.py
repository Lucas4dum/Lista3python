# Escreva um programa que preencha uma matriz 4 x 3 com números inteiros, 
# calcule e mostre na tela:
# a) A soma dos elementos que estão na 2ª e 4ª linha da matriz
# b) A soma dos números primos
import random 
matriz=[]
linha2=[]
linha4=[]
vetor=[]
somapri=0
for i in range(4):
  linha=[]
  for j in range(3):
    linha.append(random.randint(1,20))
    if i == 1:
      linha2.append(linha[j])
    if i == 3:
      linha4.append(linha[j]+linha2[j])
    contador=0
    for h in range(1,linha[j]+1):
      if linha[j] % h == 0:
        contador +=1
    if contador == 2:
      somapri+=linha[j]
      vetor.append(linha[j])
  matriz.append(linha)
for i in range(4):   
  for j in range(3):    
    print("|",matriz[i][j],end="|")
  print("")
print("A soma dos elementos que estão na 2ª e 4ª linha da matriz:",linha4)
print("A soma dos números primos:",somapri,vetor)