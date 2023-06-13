'''Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, 
o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado 
pela empresa, e é o seguinte:
Sistema Operacional     Votos   %'''

print("Enquente: Qual o melhor Sistema Operacional para uso em servidores?\n")
print('==============================')
print("As possíveis respostas são:\n")
print('1 - Windows Server')
print('2 - Unix')
print('3 - Linux')
print('4 - Netware')
print('5 - Mac OS')
print('6 - Outro')
print('==============================')

voto = 1
votos = []
votosTotais = 0
ws = unix = linux = netware = mac = outro = 0

while voto != 0:

    voto = int(input("Digite a opção de 1 a 6 ou digite 0 para sair do programa.\n"))

    if voto < 0 or voto > 6:
        voto = int(input("Digite uma opção válida de 1 a 6 ou digite 0 para sair do programa.\n"))
    else :
        votos.append(voto)
        votosTotais += 1

for i in range(len(votos)):
    if votos[i] == 1:
        ws += 1
    elif votos[i] == 2:
        unix += 1
    elif votos[i] == 3:
        linux += 1
    elif votos[i] == 4:
        netware += 1
    elif votos[i] == 5:
        mac += 1
    elif votos[i] == 6:
        outro += 1


print("Foram arrecadados {} votos totais.".format(votosTotais))
print(f"O Sistema Operacional Windows Server obteve {ws} votos válidos com {(ws/votosTotais)*100:.2f}% dos votos totais.")
print(f"O Sistema Operacional Unix Serverobteve {unix} votos válidos com {(unix/votosTotais)*100:.2f}% dos votos totais.")
print(f"O Sistema Operacional Linux Server obteve {linux} votos válidos com {(linux/votosTotais)*100:.2f}% dos votos totais.")
print(f"O Sistema Operacional Netware Server obteve {netware} votos válidos com {(netware/votosTotais)*100:.2f}% dos votos totais.")
print(f"O Sistema Operacional Mac OS Server obteve {mac} votos válidos com {(mac/votosTotais)*100:.2f}% dos votos totais.")
print(f"Outros Sistemas Operacionais obtiveram {outro} votos válidos com {(outro/votosTotais)*100:.2f}% dos votos totais.")