'''# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']'''

def vowels_check(word):

    vowels = 'aeiouAEIOU'
    count = 0

    for vowel in vowels:
        count += word.count(vowel)

    if count == 2: 
        return True
    
    return False

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

fruits_with_only_two_vowels = [fruit for fruit in fruits if vowels_check(fruit)]

print(fruits)
print(fruits_with_only_two_vowels)