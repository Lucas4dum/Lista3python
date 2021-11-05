# Escreva um programa que preencha uma listar com os nomes de 10 alunos, e 
# outra lista com a média dos alunos. Calcule e mostre:
# a) a média da classe;
# b) a quantidade de alunos que tiveram média igual ou superior a 7;
# c) a quantidade de alunos que tiveram média abaixo de 7;
# d) a maior média da classe e nome do aluno que obteve a maior média
import random
nome=["Lucas","Otavio","Jaine","Daniel","Jose","Turri","Felipe","Vinicius","Samuel","Lukemor"]
matriz=[]
totalmed=qtdalunosab=qtdalunossu=0
for i in range(10):
  linha=[]
  linha.append(nome[i])
  for j in range(1):
    linha.append(random.randint(1,10))
    totalmed+=linha[1]
    if i == 0 and j == 0:
      maior=linha[1]
      nomemaior=i 
    if maior < linha[1]:
        maior=linha[1]
        nomemaior=i    
    if linha[1] >= 7:
      qtdalunossu+=1
    else:
      qtdalunosab+=1
  matriz.append(linha)

for i in range(10):      
  for j in range(2): 
    if j == 1:
      if maior < matriz[i][j]:
        maior=matriz[i][j]
        nomemaior=j
    print("|",matriz[i][j],end="|")
  print("")
print("a média da classe",totalmed/10)
print("a quantidade de alunos que tiveram média igual ou superior a 7:",qtdalunossu)
print("a quantidade de alunos que tiveram média abaixo de 7:",qtdalunosab)
print("a maior média da classe",maior,"e nome do aluno que obteve a maior média",matriz[nomemaior][0])