'''Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo 
usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final 
devem ser informados também pelo usuário, conforme exemplo abaixo: '''

print("Programa de tabuada.\n")

num = int(input("Digite um número inteiro: \n"))
limIni = int(input("Digite o número inicial multiplicador:\n"))
limFinal = int(input("Digite o número final multiplicador:\n"))
cont = 1

for i in range (limIni, limFinal) :
    operacao = num * i
    print(" {} * {} = {}".format(num, i, operacao))
    