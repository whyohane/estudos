'''Exercise 6 - make a list that contains each fruit with exactly 5 characters'''

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

fruits_with_only_five_characters = []

for x in fruits:
    if len(x) == 5:
        fruits_with_only_five_characters.append(x)

print("Lista com frutas de apenas 5 caracteres: ")
print(fruits_with_only_five_characters)