'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as 
temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''

temperaturas = []

meses = 12
somaTemperaturas = 0

for i in range (1, meses + 1):

    temp = float(input("Digite a temperatura do mês {}:\n".format(i)))

    temperaturas.append(temp)

    somaTemperaturas += temp

mediaTemperaturas = somaTemperaturas/meses

for i in range(len(temperaturas)):

    if temperaturas[i] > mediaTemperaturas:

        if i == 0:
            mes = 'Janeiro'
        
        if i == 1:
            mes = 'Fevereiro'

        if i == 2:
            mes = 'Março'

        if i == 3:
            mes = 'Abril'

        if i == 4:
            mes = 'Maio'

        if i == 5:
            mes = 'Junho'

        if i == 6:
            mes = 'Julho'
        
        if i == 7:
            mes = 'Agosto'

        if i == 8:
            mes = 'Setembro'

        if i == 9:
            mes = 'Outubro'

        if i == 10:
            mes = 'Novembro'

        if i == 11:
            mes = 'Dezembro'

        print("A temperatura média mensal do mês de {} foi {}, sendo mais alta que a média de {} graus ao ano.\n".format(mes, temperaturas[i], mediaTemperaturas))