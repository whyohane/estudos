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
soma = 0
media = 0

while True:
    print("Digite um nome válido para entrar no programa ou um número para sair.\n")
    nome = input("Digite o nome do atleta: \n")
    
    if nome.isdigit():

        print("Erro! Você digitou um número.\n")
        print("Você saiu do programa.\n")
        break
    else:
        
        for i in range(1, 6):

            salto = float(input("Digite a distancia em metros do salto {}:\n ".format(i)))
            soma += salto
            saltos.append(salto)

        media = soma/5
        print("\nResultado final:")
        print("Nome do atleta: {}.".format(nome))
        print("O atleta teve os saltos: {} em metros.".format(saltos))
        print("A média dos saltos é: {}m.\n".format(media))
    
