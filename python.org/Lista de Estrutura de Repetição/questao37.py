'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a 
cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados 
deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve 
ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, 
além da média das alturas e dos pesos dos clientes '''

codAlto = 0
codBaixo = 0
codGordo = 0
codMagro = 0
clientes = 0
somaPesos = 0
somaAlturas = 0

maiorPeso = 0
menorPeso = 1000
menorAltura = 1000
maiorAltura = 0

while True :
    codigo = int(input("Digite o código do cliente: \n"))
    if codigo == 0 :
        break
    else :
        clientes += 1

    altura = float(input("Digite a altura do cliente em centimetros: \n"))
    peso = float(input("Digite o peso do cliente em quilogramas: \n"))

    somaPesos += peso
    somaAlturas += altura

    if peso > maiorPeso :
        maiorPeso = peso
        codGordo = codigo

    if peso < menorPeso :
        menorPeso = peso
        codMagro = peso

    if altura > maiorAltura :
        maiorAltura = altura
        codAlto = codigo

    if altura < menorAltura :
        menorAltura = altura
        codBaixo = codigo

print("O código da pessoa mais alta é {} e tem altura {}.\n".format(codAlto, maiorAltura))
print("O código da pessoa mais baixa é {} e tem altura {}.\n".format(codBaixo, menorAltura))
print("O código da pessoa mais gorda é {} e tem peso {}.\n".format(codGordo, maiorPeso))
print("O código da pessoa mais baixa é {} e tem peso {}.\n".format(codBaixo, menorPeso))