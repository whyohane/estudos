'''Faça um Programa que peça dois números e imprima o maior deles. '''
print("Programa para comparar dois valores.\n")
a = float(input("Digite um número: \n"))
b = float(input("Digite um segundo número: \n"))
if a > b :
    print("O número {} é maior que {}.\n".format(a, b))
else :
    print("O número {} é maior que {}.\n".format(b, a))