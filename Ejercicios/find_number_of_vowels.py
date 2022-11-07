'''
EXERCISE: Given a string, find the number of vowels that contain that string
'''

string_ = input("Enter a string: ")

count = 0
for letter in string_:
    if letter in 'AEIOUaeiou':
        count += 1

print("Number of vowels:",count)
