'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. '''

print("Programa para calcular o reajuste salarial. \n")
salario = float(input("Digite o valor do seu salário em reais: \n"))

if salario <= 280 and salario > 0 :
    percent = 20/100
    aumento = salario * percent
    salarioReajustado = aumento + salario

elif salario > 280 and salario <= 700 :
    percent = 15/100
    aumento = salario * percent
    salarioReajustado = aumento + salario

elif salario > 700 and salario <= 1500 :
    percent = 10/100
    aumento = salario * percent
    salarioReajustado = aumento + salario

elif salario > 1500 :
    percent = 5/100
    aumento = salario * percent
    salarioReajustado = aumento + salario

else :
    print("Erro! O valor do salário está incorreto.\n")
    percent = 0
    aumento = 0
    salarioReajustado = 0
    

print("O salário antes do reajuste era {} reais.\n".format(salario))
print("O percentual do reajuste é de {}.\n".format(percent))
print("O valor do aumento foi de {} reais. \n".format(aumento))
print("O salário agora, reajustado, é de {} reais.\n".format(salarioReajustado))
