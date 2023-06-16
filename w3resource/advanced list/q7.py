'''7. Write a Python a function to find the union and intersection of two lists. '''

def union_and_intersection_of_two_lists(first_list, second_list):

    union = []
    intersection = []

# First the intersection

    for i in first_list:

        for j in second_list:
            
            if i == j :
                
                if j in intersection:

                    pass

                else:

                    intersection.append(j)   

# Now the union

    for i in first_list:

        union.append(i)
    
    for i in second_list:

        if i in union:

            pass

        else:

            union.append(i)

    return intersection, union

# Início do Programa

first_list = []
second_list = []

count_first_list = int(input("Digite quantos valores deseja entrar na primeira lista: "))

for i in range(count_first_list):

    num = int(input("Digite o número da posição {}: ".format(i+1)))
    first_list.append(num)

count_second_list = int(input("Digite quantos valores deseja entrar na primeira lista: "))

for i in range(count_second_list):

    num = int(input("Digite o número da posição {}: ".format(i+1)))
    second_list.append(num)

intersection_, union_= union_and_intersection_of_two_lists(first_list, second_list)

print("A união das duas listas é: {}".format(union_))
print("A interseção das duas listas é: {}".format(intersection_))
