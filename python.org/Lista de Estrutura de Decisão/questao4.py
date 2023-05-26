'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante. '''
print("Programa verificador de vogais e consoantes.\n")
letra = input("Digite uma letra minúscula: \n")


if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' :
    print("A letra {} é uma vogal.\n".format(letra))
else :
    print("A letra {} é uma consoante. \n".format(letra))
