'''
EXERCISE:  Given its size, display a tile where the main diagonal 
is represented by X, the bottom by D, and the top by U.
'''


def print_a_tile(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                print('X', end=' ')
            elif j > i:
                print('U', end=' ')
            else:
                print('D', end=' ')

        print()


print_a_tile(10)