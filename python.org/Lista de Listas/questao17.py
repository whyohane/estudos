'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus 
saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando 
não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m'''

saltos = []
nomes = []
soma = 0
media = 0
medias = []
saltosTotal = []

while True:
    
    nome = input("Digite o nome do atleta: \n")
    
    if nome.isdigit():

        print("Você digitou um número.\n")
        break
    else:

        nomes.append(nome)
        
        for i in range(1, 6):

            salto = float(input("Digite a distancia em metros do salto {}:\n ".format(i)))
            soma += salto
            saltos.append(salto)

        saltosTotal.append(saltos)
        media = soma/5
        medias.append(media)

for i in range(len(nomes)):

    print("Resultado final: \n")
    print("Nome do atleta: {}.\n".format(nomes[i]))
    print("O atleta teve os saltos: {} em metros.\n".format(saltosTotal[i]))
    print("A média dos saltos é: {}m.\n".format(medias[i]))
