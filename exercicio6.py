# Escreva um programa que leia uma matriz 6 x 10, some as colunas 
# individualmente e acumule as somas na 7ª linha da matriz. O programa deverá 
# mostrar o resultado de cada coluna.
import random
matriz=[]
vetor=[]
for i in range(6):
  linha=[]
  for j in range(10):      
    linha.append(random.randint(1,10))          
  matriz.append(linha)
for i in range(10):
  total=0    
  for j in range(6):     
    total+=matriz[j][i]
    if j == 5: 
      vetor.append(total) 
  if i == 9:  
    matriz.append(vetor)  
for i in range(7):   
  for j in range(10):    
    print("|",matriz[i][j],end="|")
  print("")