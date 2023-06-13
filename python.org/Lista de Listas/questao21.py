'''Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de 
combustível. Calcule e mostre:

* O modelo do carro mais econômico;
* Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e 
quanto isto custará, considerando um que a gasolina custe R$ 5,25 o litro. Abaixo segue uma tela de exemplo. O disposição 
das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.'''

gasolina = 5.25
litros = 0
carros = ["Fusca", "Gol", "Vectra", "TCross"]
consumo = [7, 10, 9, 12]
quilometros = 1000
valor = 0
economico = 0
maisEconomico = ""

for i in range(len(carros)):
    litros = quilometros/consumo[i]
    valor = litros * gasolina
    print(f"O carro {carros[i]} consome {[consumo[i]]} litros. Para fazer {quilometros} quilometros, gastariamos {litros:.2f} litros pagando no total {valor:.2f}")

for i in range(len(consumo)):
    if consumo[i] > economico:
        economico = consumo[i]
        maisEconomico = carros[i]

print("O carro mais economico é o {}.\n".format(maisEconomico))