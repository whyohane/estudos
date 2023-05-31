'''Faça um programa que leia 5 números e informe a soma e a média dos números. '''

print("Programa para ler 5 números e informar a média\n")
soma = int(input("Digite um valor qualquer: \n"))

cont = 0

while cont < 4 :
    num = int(input("Digite um valor qualquer: \n"))
    cont += 1
    soma = soma + num

media = soma/5
print("A média dos 5 valores lidos é : {}.\n".format(media))

