'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.'''

print("Programa para calcular o salário e os impostos descontados. \n")

horas = float(input("Digite a quantidade de horas trabalhadas: \n"))
valorHora = float(input("Digite o valor pago por hora: \n"))

salario = horas * valorHora

if salario <= 900 :
    IR = 0 #isento
    INSS = (10/100) * salario
    FGTS = (11/100) * salario
    descontos = INSS + IR
    salarioLiq = salario - descontos

if salario <= 1500 :
    IR = (5/100) * salario
    INSS =  (10/100) * salario
    FGTS = (11/100) * salario
    descontos = INSS + IR
    salarioLiq = salario - descontos

if salario <= 2500 :
    IR = (10/100) * salario
    INSS = (10/100) * salario
    FGTS = (11/100) * salario
    descontos = INSS + IR
    salarioLiq = salario - descontos

if salario > 2500 :
    IR = (20/100) * salario
    INSS = (10/100) * salario
    FGTS = (11/100) * salario
    descontos = INSS + IR
    salarioLiq = salario - descontos

print("O salário bruto é de {} reais.\n".format(salario))
print("O imposto de renda é de {} reais. \n".format(IR))
print("O INSS é de {} reais.\n".format(INSS))
print("O FGTS é de {} reais. \n".format(FGTS))
print("Os descontos do salário é de {} reais. \n".format(descontos))
print("Portanto, o salário líquido é de {} reais.\n".format(salarioLiq))