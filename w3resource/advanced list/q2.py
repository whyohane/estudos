'''2. Write a Python function find the length of the longest increasing sub-sequence in a list. '''

def longest_subsequence(list):

    lenght_list = len(list)
    count = 1
    another_count = 0
    i = 0

    for i in range(lenght_list - 1):

        if list[i] < list[i+1]:

            count += 1
            i+= 1

            if count > another_count:
                another_count = count

        else:
            i+= 1
            count = 1

    return another_count

nums = []

# Início do Programa

conditional = int(input("Digite quantos valores deseja entrar na lista: "))

for i in range(conditional):

    num = int(input("Digite o número da posição {}: ".format(i+1)))
    nums.append(num)

subsequence = longest_subsequence(nums)

print("A maior subsequencia crescente dos números lidos é: {}".format(subsequence))
