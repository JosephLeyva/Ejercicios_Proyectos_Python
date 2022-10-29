'''
EXERCISE: Create a function using while loops to calculate square numbers
up to a certain limit
'''


def print_squares_upto_limit(n):
    i = 1
    while i**2 < n:
        print(i**2, end=' ')
        i += 1
    print()


print_squares_upto_limit(60)
