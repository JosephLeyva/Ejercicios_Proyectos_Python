'''
EXERCISE: Create a method that creates a multiplication table of a certain number
'''


def print_multiplication_table(n, from_=1, to=10):
    for i in range(from_, to+1):
        print(f"{n} * {i} = {n*i}")


print_multiplication_table(7)
