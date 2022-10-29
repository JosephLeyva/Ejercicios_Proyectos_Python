'''
EXERCISE: Write a method that returns the sum of n integers
'''


def sum_of_n(*args):
    sum_ = 0
    for i in args:
        sum_ += i
    return sum_


print(sum_of_n(1, 3, 5, 8, 3))
