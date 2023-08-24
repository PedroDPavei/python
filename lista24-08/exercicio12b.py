"""12) Faça 4 listas:
A. Filmes
B. Jogos
C. Livros
D. Esporte
a. Adicione no mínimo 2 itens em cada lista.
b. Crie uma lista das 4 listas criadas acima.
c. Acesse (mostrar) algum item da lista livros.
d. Remova um item da lista esporte.
"""

A = ["Velozes e Furiosos I","Velozes e Furiosos II","Velozes e Furiosos III","Velozes e Furiosos IV"]
B = ["Final Fantasy I","Final Fantasy II","Final Fantasy III","Final Fantasy IV",]
C = ["Apostila Ético I","Apostila Ético II","Apostila Ético III","Apostila Ético IV",]
D = ["Fórmula I","Fórmula II","Fórmula III","Fórmula IV"]

#literalmente dentro das regras
#a)
A.append("Velozes e Furiosos V")
A.append("Velozes e Furiosos VI")

B.append("Final Fantasy V")
B.append("Final Fantasy VI")

C.append("Apostila Ético V")
C.append("Apostila Ético VI")

D.append("Fórmula E")
D.append("Fórumula Indy")

#literamente dentro das regras tambem
#b)
E = A+B+C+D
print(E)
#c)
print(C[2])
#d)
D.pop(0)
print(D)
