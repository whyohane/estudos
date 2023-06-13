# Exercise 1

'''1 - rewrite the above example code using list comprehension syntax. Make a variable named 
uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]'''

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

uppercased_fruits = [x.upper() for x in fruits]

print(fruits)
print(uppercased_fruits)