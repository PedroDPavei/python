"""14) Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista"""
aux = -1
a = ["errado","outroerrado","errado2","certo","muitoerrado"]
b = input("Escreva a palavra para ser procurada na lista: ")
for i in a:
    aux+=1
    if(i==b):
        print(f"A palavra foi encontrada na posição {aux}")