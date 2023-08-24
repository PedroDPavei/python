"""7) Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
de aumento."""
a = float(input("Digite o preço de um produto: "))
b = a*0.95
c = a*1.15
print(f"O valor do produto com desconto de 5% é {b} e com acréscimo de 15% é {c}")
#por algum motivo indescoberto no meu computador 100*1.15 é 114.9999999 