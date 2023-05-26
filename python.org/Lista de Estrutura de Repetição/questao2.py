'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

user = input('Digite um nome de usuário: \n')
senha = input('Digite uma senha diferente do nome de usuário: \n')

while user == senha :
    senha = input("Erro! Digite uma senha válida! \n")
else :
    print("Cadastro concluído.\n")
