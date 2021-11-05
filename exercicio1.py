# Escreva um programa que leia uma matriz de ordem 3 x 5 de elementos inteiros, 
# calcule e mostre na tela:
# a) menor número da matriz;
# b) soma dos números múltiplos de 3 da matriz;
# c) maior número da 3ª coluna da matriz (índice 2);
# d) média dos números da matriz;
import random 
matriz=[]
total3=media=total=0
for i in range(3):
  linha=[]
  for j in range(5):
    linha.append(random.randint(1,12))
    total+=linha[j]
  matriz.append(linha)
menor=matriz[0][0]
maior=matriz[0][0]
media=total/15
for i in range(3):
  for j in range(5):
    if menor > matriz[i][j]:
      menor=matriz[i][j]
    if matriz[i][j] % 3 ==0:
      total3+=matriz[i][j]
    if maior < matriz[2][j]:
      maior=matriz[i][j]
    print("|",matriz[i][j],end="|")
  print("")
print("menor número da matriz",menor)
print("soma dos números múltiplos de 3 da matriz",total3)
print("maior número da 3ª coluna da matriz",maior)
print("média dos números da matriz",round(media,1))