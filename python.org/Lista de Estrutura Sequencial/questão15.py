'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS
e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo: '''

print("Programa para calcular o seu salário e descontos aplicados: \n")

valorHora = float(input("Digite quanto você ganha por hora: \n"))
horas = float(input("Digite quantas horas você trabalha por mês: \n"))

salarioBruto = valorHora * horas

descontoINSS = (8/100 * salarioBruto)

descontoSind = (5/100 * salarioBruto)

descontoIR = (11/100 * salarioBruto)

salarioLiq = salarioBruto - descontoINSS - descontoIR - descontoSind

#print("Seu salário {}, seu desconto {} e suas horas {}".format(salarioBruto, descontoINSS, horas))
print("O seu salário bruto é: \n", salarioBruto)
print("Você paga para o INSS {} reais. \n".format(descontoINSS))
print("Você paga para {} reais em Imposto de renda. \n".format(descontoIR))
print("Você paga para o Sindicato {} reais. \n".format(descontoSind))
print("Com os descontos, o seu salário liquido é de: ", salarioLiq)
