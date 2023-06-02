'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno 
e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas. '''

maiorAltura = 0
menorAltura = 1000
codigoAlto = 0
codigoBaixo = 0

for i in range (10):
    codigo = int(input("Digite o código do aluno: \n"))
    altura = int(input("Digite sua altura em centimetros.\n"))

    if altura > maiorAltura :
        maiorAltura = altura
        codigoAlto = codigo

    
    if altura < menorAltura :
        menorAltura = altura
        codigoBaixo = codigo

print("O aluno mais alto tem {} centimetros de altura e seu código é: {}.\n".format(maiorAltura, codigoAlto))
print("O aluno mais baixo tem {} centimetros de altura e seu código é {}.\n".format(menorAltura, codigoBaixo))

