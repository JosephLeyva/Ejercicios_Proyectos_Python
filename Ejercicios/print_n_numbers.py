'''
EXERCISE: Write a method that prints all successive integers from 1 to n 
'''


def print_n_numbers(n):
    for i in range(1, n+1):
        print(i, end=", ")
    print('\b\b ')


print_n_numbers(12)
