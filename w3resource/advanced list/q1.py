#1. Write a Python function to reverse a list at a specific location. 

def reverse_list(list, start_list, end_list): #definimos os parametros, a lista como entrada e as posições inicial e final.
#essa função basicamente troca as posições de lugares.
    while start_list < end_list:

        list[start_list], list[end_list] = list[end_list], list[start_list]
        start_list += 1
        end_list -= 1
    return list
        
nums = []
new_list = []

print("Programa para reverter a lista.\n")
count = int(input("Digite quantos números deseja adicionar na primeira lista: "))

for i in range (count):
    num = int(input("Digite um número para adicionar na lista: "))
    nums.append(num)

start_list = int(input("Digite a posição inicial que deseja reverter: \nOBS: a posição inicial é zero: "))
print("A última posição da lista é: {}".format(len(nums)-1))
end_list = int(input("Digite a posição final: "))

print(nums)
new_list = reverse_list(nums, start_list, end_list)
print("A lista na posição reversa é:")
print(new_list)



    
    