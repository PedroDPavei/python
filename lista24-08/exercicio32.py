"""32) Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
obtidos os seguintes dados:
a. Código da cidade; (digitado pelo usuário)
b. Número de veículos de passeio (em 1999); (digitado pelo usuário)
c. Número de acidentes de trânsito com vítimas (em 1999). (digitado pelo usuário)
Deseja-se saber:
b. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
c. Qual a média de veículos nas cinco cidades juntas;
d. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio."""
maiorind = menorind = mediaveiculo = mediaac = 0
maiorindcod = menorindcod = auxind = qntd = 0 
while True:
    opcao = int(input("Selecione uma opção:" 
          "\n1- Cadastrar cidade"
          "\n2- Finalizar"
          "\n"))
    
    if(opcao==1):
        codcid = int(input("Digite o código da cidade: "))
        carrospasseio = int(input("Digite o número de carros de passeio da cidade: "))
        acidentes = int(input("Digite o número de acidentes de trânsito com vítimas da cidade: "))

        if(auxind==0):
            maiorind = acidentes
            menorind = acidentes
            maiorindcod = codcid
            menorindcod = codcid
            mediaveiculo = mediaveiculo + carrospasseio
            aux = 1
            qntd = qntd + 1
            if(acidentes<2000):
                mediaac = mediaac + acidentes
        elif(auxind==1):
            qntd = qntd + 1
            mediaveiculo = mediaveiculo + carrospasseio
            if(maiorind<acidentes):
                maiorind = acidentes
                maiorindcod = codcid
            if(acidentes>menorind):
                menorind = acidentes
                menorindcod = codcid
            if(acidentes<2000):
                mediaac = mediaac + acidentes
    elif(opcao==2):
        break
mediaveiculo = mediaveiculo/qntd
mediaac = mediaac/qntd
print(f"O maior índicie de acidentes pertence a cidade {maiorindcod} e o menor pertence a cidade {menorindcod} "
      f"\nA média de veículos nas cidade é de {mediaveiculo} "
      f"\nA média de acidentes nas cidades com menos de 2000 veículos de passeio é {mediaac}")