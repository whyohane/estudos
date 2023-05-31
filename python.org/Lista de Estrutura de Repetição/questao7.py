'''Faça um programa que leia 5 números e informe o maior número. '''

print("Programa para ler o maior número lido.\n")

cont = 0

maiorNum = int(input("Digite um valor qualquer: \n"))

while cont < 5 :
    num = int(input("Digite um valor qualquer: \n"))
    cont += 1
    if maiorNum < num :
        maiorNum = num
    
print("O maior número lido é : {}".format(maiorNum))