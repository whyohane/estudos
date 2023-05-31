'''Faça um programa que, dado um conjunto de N números, determine o menor valor, 
o maior valor e a soma dos valores.'''

i = int(input("Digite quantos números deseja digitar: \n"))

cont = 1
maiorNum = int(input("Digite um número qualquer: \n"))
menorNum = maiorNum
soma = maiorNum

while cont < i :
    num = int(input("Digite um número qualquer: \n"))
    if maiorNum < num :
        maiorNum = num
    
    if menorNum > num :
        menorNum = num

    soma = soma + num

    cont += 1

print("O menor número lido é: {}\n".format(menorNum))
print("O maior número lido é: {}\n".format(maiorNum))
print("A soma de todos os números lidos é: {}\n".format(soma))

    
