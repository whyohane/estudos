# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 

print("Programa para calcular o peso ideal de homens e mulheres.")
altura = float(input("Digite sua altura: \n"))
gen = input("Digite o seu sexo: homem ou mulher: \n")
if gen == 'homem' :
    pesoH = (72.7*altura) - 58
    print("O seu peso ideal é: ", pesoH)
else :
        pesoM = (62.1*altura) - 44.7 
        print("O seu peso ideal é: ", pesoM)
