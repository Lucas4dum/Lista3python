# Escreva um programa que leia uma matriz de ordem 5 x 4, onde na 1ª coluna da 
# matriz é armazenado o nome do vendedor, da 2ª coluna a 4ª coluna são 
# armazenados o total de vendas por mês de cada vendedor, portanto na 2ª coluna 
# é armazenado a venda do mês 1, 3ª coluna do mês 2 e na 4ª coluna do mês 3. 
# Calcule e mostre na tela:
# a) O valor total vendido por vendedor
# b) A maior venda do mês 1
# c) A menor venda do mês 3
# d) O total vendido por mês de todos os vendedores
import random
matriz=[]
vetor=[]
total=0
nome=["Lucas","José","Otávio","Daniel","Turri"]
for i in range(5):
  linha=[]
  h=1
  linha.append(nome[i])  
  total1=0
  for j in range(3):
    linha.append(random.randint(100,200))
    total+=linha[h+j]
    total1+=linha[h+j]
  vetor.append(total1)
  matriz.append(linha)
maior=matriz[0][1]
menor=matriz[0][3]
for i in range(5):   
  for j in range(4):    
    print("|",matriz[i][j],end="|")
  print("")
for i in range(5):
  print("O valor totalvendido pelo vendedor:",matriz[i][0],"foi:",vetor[i])
  if maior < matriz[i][1]:
    maior=matriz[i][1]
  if menor > matriz[i][3]:
    menor=matriz[i][3]
print("A maior venda do mês 1:",maior)
print("A menor venda do mês 3:",menor)
print("O total vendido por mês de todos os vendedores:",total)
