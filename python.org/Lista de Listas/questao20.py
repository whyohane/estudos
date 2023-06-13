'''As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado 
durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será 
gasto com o pagamento deste abono.

Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a 
seguinte forma de cálculo:

* Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; 
* O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
* O salário de cada funcionário, juntamente com o valor do abono;
* O número total de funcionário processados;
* O valor total a ser gasto com o pagamento do abono;
* O número de funcionário que receberá o valor mínimo de 100 reais;
* O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.'''

salarios = []
salario = 1
abonoTotal = maiorAbono = 0
funcionarios = funcionariosAbonoMin = 0
abonoMinimo = 100
porcentagem = 20/100 

while salario != 0:
    salario = float(input("Digite o salário do colaborador ou digite 0 para sair do programa.\n"))
    if salario == 0:
        break

    salarios.append(salario)
    funcionarios += 1

for i in range(len(salarios)):

    abono = salarios[i]*porcentagem
    
    if abono < abonoMinimo:
        abono = abonoMinimo
        funcionariosAbonoMin += 1
        abonoTotal += abono
    else:
        abonoTotal += abono

    if abono > maiorAbono:
        maiorAbono = abono

    print("O colaborador com salário de {} teve abono de {}.\n".format(salarios[i], abono))

print("Foram contabilizados {} colaboradores no total, sendo {} colaboradores que ganharam abono mínimo.\n".format(funcionarios, funcionariosAbonoMin))
print("O total gasto em abonos pela empresa foi de {}.\n".format(abonoTotal))
print("O maior abono pago foi de {}.\n".format(maiorAbono))
    
