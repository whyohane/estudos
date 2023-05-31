'''Altere o programa anterior para que ele aceite apenas números entre 0 e 1000. '''

i = int(input("Digite quantos números deseja digitar: \n"))

cont = 1
maiorNum = int(input("Digite um número entre 0 e 1000: \n"))
while maiorNum < 0 or maiorNum > 1000 :
    maiorNum = int(input("Número inválido! Digite novamente.\n"))
else:
    menorNum = maiorNum
    soma = maiorNum
    while cont < i :
        num = int(input("Digite um número entre 0 e 1000: \n"))
        if maiorNum < num :
            maiorNum = num
    
        if menorNum > num :
            menorNum = num

        soma = soma + num

        cont += 1

print("O menor número lido é: {}\n".format(menorNum))
print("O maior número lido é: {}\n".format(maiorNum))
print("A soma de todos os números lidos é: {}\n".format(soma))