'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. '''

print("Programa de média.")
nota1 = float(input("Digite a primeira nota: \n"))
nota2 = float(input("Digite a segunda nota: \n"))

media = (nota1 + nota2)/2

if media >= 7 and media < 10 :
    print("O aluno foi aprovado com média: {}.\n".format(media))
elif  media == 10 :
    print("O aluno foi aprovado com distinção com média: {}. \n".format(media))
else :
    print("O aluno foi reprovado com média {}. \n".format(media))