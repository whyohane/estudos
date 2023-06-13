'''Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para 
saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de 
um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi 
contratada para desenvolver este programa, utilizando a linguagem de programação Python. Para computar 
cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador.
Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado,
o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. 
Após o final da votação, o programa deverá exibir:

O total de votos computados;
Os números e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

'''
jogadores = [0]*23

votos = 0
camisa = 1
melhorJogador = 0

print("Enquente: Quem foi o melhor jogador da partida?\n")

while camisa != 0:
    camisa = int(input("Digite a camisa do jogador entre 1 e 23. Caso queira sair do programa digite 0.\n"))
    
    if camisa < 0 or camisa > 23 :
        camisa = int(input("Digite um número válido para a camisa do jogador entre 1 e 23. Caso queira sair do programa digite 0.\n"))
    else :
        jogadores[camisa-1] += 1
        votos += 1 

print("Foram contabilizados {} votos ao total!\n".format(votos))
print('Mostrando agora a quantidade de votos para os jogadores: \n')
print('========================================')

for i in range(len(jogadores)):

    if jogadores[i] > 0: 
    
        if i >= 10:
            if jogadores[i] < 10:
                print(f'  {i+1}     |     {jogadores[i]}     |       {(jogadores[i]/votos)*100:.2f}     |')
            else:
                print(f'  {i+1}     |     {jogadores[i]}    |       {(jogadores[i]/votos)*100:.2f}     |')
        else:
            if jogadores[i] < 10:
                print(f'  {i+1}      |     {jogadores[i]}     |       {(jogadores[i]/votos)*100:.2f}     |')
            else:
                print(f'  {i+1}      |     {jogadores[i]}    |       {(jogadores[i]/votos)*100:.2f}     |')
            
    
    if jogadores[i] > jogadores[melhorJogador]:
        melhorJogador = i
print('========================================')
print(f'\nO melhor atleta foi o Camisa {i+1}, com {jogadores[i]} votos, correspondendo a {(jogadores[i]/votos)*100:.2f} do total de votos.')
print('========================================')