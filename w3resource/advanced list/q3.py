'''3. Write a Python function that finds all the permutations of the members of a list. '''

def permutations_list(list):
    if len(list) == 0:
        return [[]]
    
    permutations = []

    for i in range (len(list)):

        element = list[i]
        others_elements = list[:i] + list[i+1:]

        for permutacao in permutations_list(others_elements):

            permutations.append([element] + permutacao)
    return permutations

list = [1, 2, 3, 4]

permutations = permutations_list(list)

for permutacao in permutations:
    print(permutacao)
