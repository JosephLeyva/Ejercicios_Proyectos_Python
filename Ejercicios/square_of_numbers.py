'''
EXERCISE: Write a method that prints the squares of all
successive integers from 1 to n
'''

def print_squares_of_numbers(n):
    for i in range(1,n+1):
        print(f"{i} * {i} = {i*i}")

print_squares_of_numbers(10)