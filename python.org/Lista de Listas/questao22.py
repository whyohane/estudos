'''Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um 
levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram 
lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número 
indeterminado de entradas, cada uma contendo: 
* um número de identificação do mouse o tipo de defeito:
* 1- necessita da esfera;
* 2- necessita de limpeza; 
* 3- necessita troca do cabo ou conector; 
* 4- quebrado ou inutilizado.

Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:'''

print("Programa contabilizador de mouses.\n")
mouse = 1
ident = []
defeitos = []
cont1 = cont2 = cont3 = cont4 = defeito = quantMouse = 0
while mouse != 0:

    mouse = int(input("Digite o número de identificação do mouse: "))
    if mouse == 0:
        break

    ident.append(mouse)
    print("Digite o número do defeito do mouse: \n")
    quantMouse += 1
    print("========================================")
    print('1- necessita da esfera.')
    print('2- necessita de limpeza.')
    print('3- necessita da troca do cabo ou conector.')
    print('4- quebrado ou inutilizado.')
    defeito = int(input("========================================\n"))
    defeitos.append(defeito)

for i in range(len(defeitos)):
    if defeitos[i] == 1:
        cont1 += 1
    elif defeitos[i] == 2:
        cont2 += 1
    elif defeitos[i] == 2:
        cont3 += 1
    elif defeitos[i] == 2:
        cont4 += 1

print("Foram contabilizados {} mouses. ".format(quantMouse))
print("{} com o defeito: Necessita de esfera.".format(cont1))
print("{} com o defeito: Necessita de limpeza.".format(cont2))
print("{} com o defeito: Necessita da troca do cabo ou conector.".format(cont3))
print("{} com o defeito: Quebrado ou inutilizado.".format(cont4))