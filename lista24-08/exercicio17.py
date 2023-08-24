"""17) Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde h corresponde à altura):
• Homens: (72.7 * h) - 58
• Mulheres: (62, 1 * h) - 44, 7
"""
h = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo(M/F): ")
if(sexo=="M"):
    ms=(72.7*h) - 58
    print(f"Seu peso ideal seria {ms}Kg")
elif(sexo=="F"):
    fs=(62.1*h) - 44.7
    print(f"Seu peso ideal seria {fs}Kg")