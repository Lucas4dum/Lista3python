# Escreva um programa que preencha uma matriz 4 x 6 com números inteiros, 
# calcule e mostre na tela:
# a) A quantidade de números que estão no intervalo entre 10 e 30
# b) A soma dos números maiores que 10 e pares
# c) A soma dos números que estão na quarta coluna da matriz
# d) A média dos números da matriz que estão na terceira linha
import random 
matriz=[]
qtd=soma1=soma2=soma3=0
for i in range(4):
  linha=[]
  for j in range(6):
    linha.append(random.randint(1,35))
  matriz.append(linha)
for i in range(4):
  for j in range(6):
    if matriz[i][j] > 9 and matriz[i][j] < 31:
      qtd+=1
    if matriz[i][j] > 10 and matriz[i][j] % 2 ==0:
      soma1+=matriz[i][j]
    if 3 == j:
      soma2+=matriz[i][j]
    if i == 2:
      soma3+=matriz[i][j]            
    print("|",matriz[i][j],end="|")
  print("")
media=soma3/6
print("A quantidade de números que estão no intervalo entre 10 e 30:",qtd)
print("A soma dos números maiores que 10 e pares:",soma1)
print("A soma dos números que estão na quarta coluna da matriz:",soma2)
print("A média dos números da matriz que estão na terceira linha:",soma3)
