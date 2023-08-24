"""16) Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
conversão.
"""
temp = float(input("Digite uma temperatura: "))
medida = input("Você gostaria de tranformar a temperatura em Celsius(C) ou Fahreinheit(F): ")
if(medida=="F"):
    ntemp = (temp*9/5)+32
    print(f"Sua temperatura convertida é de {ntemp}")
elif(medida=="C"):
    Ntemp = (temp-32)*5/9
    print(f"Sua temperatura convertida é de {Ntemp}")
else:
   print("Medida inválida")
