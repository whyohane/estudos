'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). '''

arq = float(input("Digite o tamanho de um arquivo para baixar em MEGABYTES: \n"))

bits = arq * 8.388608

internet = float(input("Digite a velocidade da sua internet em MEGABITS POR SEGUNDO: \n"))

tempo = bits / internet

minutos = tempo / 60

print("Para baixar o arquivo de tamanho {} MEGABYTES demorou {} minutos. \n".format(arq, minutos))

