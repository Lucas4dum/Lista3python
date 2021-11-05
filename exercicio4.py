# Escreva um programa que armazene em uma matriz, o nome e duas notas de 5 
# alunos. Calcule e armazene em uma lista a média de cada aluno e em outra lista o 
# status (media >= 6, “aprovado”, caso contrário, “reprovado”)
# • faça uma opção para que o usuário possa fazer uma pesquisar por nome. Se 
# encontrar seja exibido na tela:
# o posição em que foi encontrado (índice);
# o nome do aluno;
# o as duas notas e a média;
# o status
import random
matriz=[]
media=[]
status=[]
nome=["Lucas","José","Otávio","Daniel","Turri"]
for i in range(5):
  linha=[]
  linha.append(nome[i])
  h=1
  total=media1=0
  for j in range(2):
    linha.append(random.randint(1,10))
    total+=linha[h+j]
  media1=total/2
  media.append(media1)
  if media1 >= 6:
    status.append("aprovado")
  else:
    status.append("reprovado")
  matriz.append(linha)
for i in range(5):   
  for j in range(3):    
    print("|",matriz[i][j],end="|")
  print("")
pesquisa=input("Busque por um dos nomes:")
while(pesquisa != "Fim"):
  for i in range(5):
    if matriz[i][0] == pesquisa:
      print("Nome do aluno",matriz[i][0],"está no índice:",i)
      print("Nota 1:",matriz[i][1],"Nota 2:",matriz[i][2],"média:",media[i])
      print("Status do aluno:",status[i])
      break
    elif i == 4:
      print("Não foi encontrado")
      break   
  print("")
  pesquisa=input("Busque por um dos nomes:")
