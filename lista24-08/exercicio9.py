"""9) Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
Euros"""
nome = input("Digite seu nome: ")
a = float(input("Digite seu dinheiro em R$: "))
b = a/5.41
c = a/5.28
print(f"{nome},você tem R${a} quem podem ser convertidos em US${b} dólares e €{c} euros.")