'''
EXERCISE: Create a function that, given a number, make the sum from 1 to n
'''


def sum_upto_n(n):
    sum_ = 0
    for i in range(1, n+1):
        sum_ += i
    return sum_


print(sum_upto_n(6))
