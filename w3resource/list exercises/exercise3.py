'''# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
Hint: You'll need a way to check if something is a vowel.'''

def vowels_check(word):

    vowels = 'aeiouAEIOU'
    count = 0

    for vowel in vowels:
        count += word.count(vowel)

    if count > 2: 
        return True
    
    return False

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if vowels_check(fruit)]

print(fruits)
print(fruits_with_more_than_two_vowels)