'''8. Write a Python function to remove duplicates from a list while preserving the order. '''

def remove_duplicates(list):

    new_list = []

    for i in list:

        if i in new_list:

            pass

        else:

            new_list.append(i)

    return new_list

# Starting now:

list = []
list = ['Anna', 'John', 'Marie', 'Anna', 'Camila', 'Anna']

same_order = remove_duplicates(list)

print("A lista é:\n {}".format(list))
print("A lista sem itens repetidos é: \n{}".format(same_order))