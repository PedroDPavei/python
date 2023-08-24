"""33) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
códigos utilizados são:
 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
valor zero.
"""
cand1 = cand2 = cand3 = cand4 = nulo = branco = votos = 0


while True:
    voto = int(input("Selecione um candidato:" 
          "\n1- José"
          "\n2- João"
          "\n3- Jonas"
          "\n4- Jorge"
          "\n5- Nulo"
          "\n6- Em Branco"
          "\n0- Encerrar"
          "\n"))
    if(voto==1):   
        cand1+=1
        votos+=1
    elif(voto==2):   
        cand2+=1
        votos+=1
    elif(voto==3):   
        cand3+=1
        votos+=1
    elif(voto==4):   
        cand4+=1
        votos+=1
    elif(voto==5):   
        nulo+=1
        votos+=1
    elif(voto==6):   
        branco+=1
        votos+=1
    elif(voto==0):
        break
pnulos = (100*nulo)/votos
pbrancos = (100*branco)/votos
print(f"Votação Encerrada"
      f"\nResultados:"
      f"\nJosé: {cand1} votos"
      f"\nJoão: {cand2} votos"
      f"\nJonas: {cand3} votos"
      f"\nJorge: {cand4} votos"
      f"\nVotos Nulos: {nulo} votos"
      f"\nVotos em Branco: {branco} votos"
      f"\nPorcentagem de Votos Nulos:{pnulos}"
      f"\nPorcentagem de Votos em Branco:{pnulos}")
