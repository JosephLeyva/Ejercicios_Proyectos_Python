'''
EXERCISE: Determine whether a number is primer or not
'''


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


for i in range(1, 100):
    if is_prime(i):
        print(i)
