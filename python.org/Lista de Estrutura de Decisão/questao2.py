'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. '''
print("Verificador de números positivos ou negativos.\n")
a = float(input("Digite um número.\n"))
if a < 0 :
    print("O número {} é negativo. \n".format(a))
else :
    print("O número {} é positivo. \n".format(a))
    