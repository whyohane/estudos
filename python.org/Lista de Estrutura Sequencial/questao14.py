'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de
pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa 
que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. '''

print("Programa para calcular o excesso de peixe e multa aplicada: \n")
print("O peso máximo é 50KG. Cada kg excedente custa R$4,00. \n")

pesca = float(input("Digite o peso pescado hoje: "))
excesso = pesca - 50

if excesso > 0 :
    multa = excesso * 4
    print("\nExcesso de peso! Multa no valor de ", multa)
else :
    print("\nO peso está dentro do estabelecido pelo regulamento. \n")
