'''O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja
de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então 
mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular 
e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo: '''

print("Mercadinho Moranguinho\n")

preço = 1
soma = 0

while preço != 0 :
    preço = float(input("Digite o preço do produto: \n"))
    soma = soma + preço

    if preço == 0 :
        break

dinheiro = float(input("Digite quanto dinheiro o cliente deu: \n"))
troco = dinheiro - soma
print("O total foi {}, o cliente pagou {} e o troco foi: {}".format(soma, dinheiro, troco))
