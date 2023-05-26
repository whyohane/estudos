'''Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. '''

num = int(input("Digite uma nota entre zero e dez.\n"))

while num > 10 or num < 0 :
    num = int(input("Digite uma nota válida entre zero e dez. \n"))

