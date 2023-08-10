#tipos de dados
""" a = 5
print(type(a))
b ="cock"
print(type(b))
c = 8.5
print(type(c))
d = ()
print(type(d))
e = []
print(type(e))
f = {}
print(type(f))
g = 5+1j
print(type(g))
h = True
print(type(h)) """

#tipos de Print
""" 
nome = "davi que nao veio:("
idade = str(16)
print("Olá",nome,"voce é um bb e tem",idade,"anos") #1° jeito

print("Olá" + nome + "voce é um bb e tem" + idade + "anos") #2° jeito

print("Olá {} voce tem {} anos".format(nome,idade)) #3° jeito

print(f"Olá {nome} voce tem {idade}") #4° jeito """

#caixas de entrada
"""  n1 = input("Digite seu nome: ")
n2 = input("Digite seu nome: ")
n3 = input("Digite seu nome: ")

print(n1,n2,n3) 

print(f"{n1} \n {n2} \n {n3}") #\n quebra as linhas """

""" dia = 10
mes = 8
ano = 2023

print("João estava andando na padaria" , end=",")

print("porque estava com fome")

print(dia,mes,ano, sep="/") """

#criação de listas
""" 
nomes = ["Matheus","Marcelo","Maria","Mariane","Marcos"]
print(nomes)
nomes[2]=1
print(nomes) """

#criação de tuplas
""" 
carros = ("gol","uno","celta","fusca","brailia")
print(carros[0]) """
#carros[0] = "Meredes" #error

#criação de dicionáio
""" peso = {"amanda":55.6,"yuri":1000,"arthur":55.6,"joao":70.6}
print(peso)

valor = input("Digite algo: ") #.upper ou .lower pra tranformar Aids em AIDS ou aids
#a = int(input("Digite um número: "))
print(valor.isnumeric())
print(valor.isalpha())
print(valor.isdecimal())
print(valor.isalnum())
print(valor.islower())
print(valor.isupper())
print(valor.istitle())
print(valor.isspace()) """
""" 
valor = int(input("Digite algo: ")) #pra ler numero e nao caracter 
print(valor.isnumeric())
print(valor.isalpha())
print(valor.isdecimal())
print(valor.isalnum())
print(valor.islower())
print(valor.isupper())
print(valor.istitle())
print(valor.isspace())
 """
"""
valor = (2*10)/5**2+(125/5)
print(valor)

a = 2371//5
b = 2372561/3
c = 2371%5
print(a,b,c)
print(round(b,2)) #casas de decimais com função
print(f"{b:.2f}") #casas de decimais com print formatado

d = 4**2 #potencia com operador
print(d)
e = pow(4,2) #potencia com funcao
print(e)
"""
"""
a = input("Digite seu nome: ")
b = "Joaquim"
print(f"Seja bem vindo{a:20}") 
print(f"Seja bem vindo{a:>20}") #esquerda
print(f"Seja bem vindo{a:<20} e {b}") #direita#meio(divide)
print(f"Seja bem vindo{a:^20}") #meio(divide)
print(f"Seja bem vindo{a:-^20}") #meio(divide) e coloca tudo bonitinho femboy
"""
ads