"""12) Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre
os itens repetidos.
"""
aux = 0
a = ["Vermelho","Azul","Roxo","Preto","Vermelho"]
for i in a:
    b = (a.count(i))
    if(aux==0):
        if(b>1):
            print(f"A posição {i} está duplicada")
            aux = 1


