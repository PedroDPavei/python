"""11) Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
ao final mostrar seu nome e salário final calculado."""
nome = input("Digite seu nome: ")
nhoras = float(input("Digite suas horas trabalhadas: "))
phoras = float(input("Digite o valor pago por horas de trabalho: "))
sbruto = nhoras*phoras
sfinal = sbruto*0.98
print(f"Seu nome é {nome} e seu salário final com desconto de INSS é de R${sfinal}.")