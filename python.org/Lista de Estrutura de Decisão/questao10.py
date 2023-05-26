'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem 
"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. '''

turno = input("Digite 'M' para turno da manhã, 'T' para turno da tarde e 'V' para turno vespertino.\n")

if turno == 'M' :
    print("Bom dia!\n")
elif turno == 'T' :
    print("Boa tarde!\n")
elif turno == 'V' :
    print("Boa noite!\n")
else :
    print("Turno inválido! \n")