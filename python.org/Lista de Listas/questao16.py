'''Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base 
em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de 
$3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine 
quantos vendedores receberam salários nos seguintes intervalos de valores:

    $200 - $299
    $300 - $399
    $400 - $499
    $500 - $599
    $600 - $699
    $700 - $799
    $800 - $899
    $900 - $999
    $1000 em diante 
'''

vendasBrutas = 0
salarioSemana = 200
porcentagemComissao = 9/100
comissao = 0
salarioBruto = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0
cont7 = 0
cont8 = 0
cont9 = 0

salarios = []

while True :

    vendasBrutas = float(input("Digite o valor bruto que o vendedor vendeu esta semana: \n"))

    if vendasBrutas == 0:
        break
    else :
        comissao = vendasBrutas * porcentagemComissao
        salarioBruto = salarioSemana + comissao

        salarios.append(salarioBruto)

for i in range(len(salarios)):

    if salarios[i] >= 200 and salarios[i] <= 299:
        cont1 += 1
    elif salarios[i] >= 300 and salarios[i] <= 399:
        cont2 += 1
    elif salarios[i] >= 400 and salarios[i] <= 499:
        cont3 += 1
    elif salarios[i] >= 500 and salarios[i] <= 599:
        cont4 += 1    
    elif salarios[i] >= 600 and salarios[i] <= 699:
        cont5 += 1
    elif salarios[i] >= 700 and salarios[i] <= 799:
        cont6 += 1
    elif salarios[i]>= 800 and salarios[i] <= 899:
        cont7 += 1
    elif salarios[i] >= 900 and salarios[i] <= 999:
        cont8 += 1    
    else :
        cont9 += 1

print("{} funcionários ganharam entre 200 e 299 reais.\n".format(cont1))
print("{} funcionários ganharam entre 300 e 399 reais.\n".format(cont2))
print("{} funcionários ganharam entre 400 e 499 reais.\n".format(cont3))
print("{} funcionários ganharam entre 500 e 599 reais.\n".format(cont4))
print("{} funcionários ganharam entre 600 e 699 reais.\n".format(cont5))
print("{} funcionários ganharam entre 700 e 799 reais.\n".format(cont6))
print("{} funcionários ganharam entre 800 e 899 reais.\n".format(cont7))
print("{} funcionários ganharam entre 900 e 999 reais.\n".format(cont8))
print("{} funcionários ganharam mais de 1000 reais.\n".format(cont9))