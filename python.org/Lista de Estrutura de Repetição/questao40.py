'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:

    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. '''
maiorAcidente = 0
menorAcidente = 1000000
somaCarros = 0
somaAcidentes = 0

for i in range(5):

    codigo = int(input("Digite o código da cidade: \n"))
    carros = int(input("Digite o número de carros: \n"))
    acidentes = int(input("Digite o número de acidentes de carro: \n"))

    if acidentes > maiorAcidente :
        maiorAcidente = acidentes
        codigoMaior = codigo

    if acidentes < menorAcidente :
        menorAcidente = acidentes
        codigoMenor = codigo

    somaCarros += carros
    somaAcidentes += acidentes

mediaCarros = somaCarros/5
mediaAcidentes = somaAcidentes/5

print("O maior indice de acidentes é {} e pertence a cidade de código {}.\n".format(maiorAcidente, codigoMaior))
print("O menor indice de acidentes é {} e pertence a cidade de código {}.\n".format(menorAcidente, codigoMenor))
print("A média de acidentes das 5 cidades é: {}".format(mediaAcidentes))
print("A média de carros nas 5 cidades é: {}".format(mediaCarros))