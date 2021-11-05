# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando 
# dados sobre o salário, idade e o número de filhos. Escreva um programa que leia 
# esses dados, por exemplo para 10 pessoas. Armazene esses dados em uma 
# matriz, depois calcule e mostre:
# a) A média de salário da população
# b) A média do número de filhos
# c) A quantidade de filhos das pessoas que tem idade entre 15 a 25 anos
# d) A média de salário de pessoas que tem idade entre 20 a 30 anos
import random
nome=["Lucas","Otavio","Jaine","Daniel","Jose","Turri","Felipe","Vinicius","Samuel","Lukemor"]
matriz=[]
totalsal=totalfilhos=qtdfil=totalsal2=qtd=0
for i in range(10):
  linha=[]
  linha.append(nome[i])
  for j in range(3):    
    if j == 0:  
      linha.append(random.randint(900,2000))
      totalsal+=linha[1]
    elif j == 1:
      linha.append(random.randint(15,50))  
      if linha[2] > 19 and linha[2] < 31:
        totalsal2+=linha[1]  
        qtd+=1 
    elif j == 2:
      linha.append(random.randint(1,4))
      totalfilhos+=linha[3]
      if linha[2] > 14 and linha[2] < 26:
        qtdfil+=linha[3]
  matriz.append(linha)

print("|Nome||Salário||QTD Filhos|")  
for i in range(10):      
  for j in range(4): 
      print("|",matriz[i][j],end="|")
  print("")
print("A média de salário da população",totalsal/10)
print("A média do número de filhos",totalfilhos/10)
print("A quantidade de filhos das pessoas que tem idade entre 15 a 25 anos",qtdfil)
print("A média de salário de pessoas que tem idade entre 20 a 30 anos",round(totalsal2/qtd,1))