"""15) Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
tela dizendo se está “quente”, “frio” ou “agradável”."""
clima = float(input("Informe a temperatura atual: "))
if(clima<15):
    print("Ta friozinho, mas quem que nao curte um friozinho né")
elif(20<clima<25):
    print("Clima ta tranquilinho de mais")
else:
    print("CALOOOOOR!!!!")
