'''12. Write a Python program to find the first non-repeated element in a list. '''

def non_repeated_element(list):
    
    new_list = {}

    for i in list:

        if i in new_list:
            
            new_list[i] += 1

        else:

            new_list[i] = 1
    
    for i in list:

        if new_list[i] == 1:
            return i
        
    return None

list = [1, 2, 1, 2, 1, 2, 3, 1, 2, 1, 2, 4]
print("A lista: {}".format(list))
element = non_repeated_element(list)
print("O primeiro membro não repetido é: {}".format(element))



