'''
EXERCISE: Create a function using while loops to calculate cube numbers
up to a certain limit
'''


def print_cubes_upto_limit(n):
    i = 1
    while i**3 < n:
        print(i**3)
        i += 1


print_cubes_upto_limit(30)
