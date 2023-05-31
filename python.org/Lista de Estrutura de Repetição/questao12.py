'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro
entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
A saída deve ser conforme o exemplo abaixo: '''

print("Programa de tabuada.\n")

num = int(input("Digite um número inteiro entre 1 e 10: \n"))
cont = 1

while cont <= 10 :
    operacao = num * cont
    print(" {} * {} = {}".format(num, cont, operacao))
    cont += 1
    