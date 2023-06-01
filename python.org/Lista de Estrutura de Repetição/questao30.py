'''O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia
da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa
que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário,
conforme o exemplo abaixo: '''

print("Tabela de preços da Panificadora!\n")

produtos = 50
preçoFixo = float(input("Digite o preço do pão que você está comprando.\n"))

for i in range (1, 50 + 1) :
    preço = i * preçoFixo
    print("{} - R$ {}".format(i, preço))