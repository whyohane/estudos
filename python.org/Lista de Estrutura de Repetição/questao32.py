'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo: '''

fat = 1
num = int(input("Digite um número inteiro para calcular o seu fatorial: \n"))

for i in range(num, 1, -1) :    
    fat = fat * i

print("O fatorial do número {} é {}.\n".format(num, fat))
